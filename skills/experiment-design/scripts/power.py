#!/usr/bin/env python3
"""Sample size and result evaluation for two-arm conversion tests.

Standard library only. No install step, no network.

    python scripts/power.py size --baseline 0.004 --mde 20 --daily-traffic 5000
    python scripts/power.py evaluate --a-n 340 --a-conv 12 --b-n 340 --b-conv 14

`size` answers "is this test runnable at all", which is the question people skip.
`evaluate` answers "is this result real", including whether the test was stopped
early, which is the most common way a real-looking result turns out not to be.
"""

from __future__ import annotations

import argparse
import math
import sys
from statistics import NormalDist

# Convention in online experimentation, not a law of nature. alpha 0.05 accepts a
# 1-in-20 false positive; power 0.80 accepts missing a real effect 1 time in 5.
# Both are defaults you may raise, never values to quote as requirements.
DEFAULT_ALPHA = 0.05
DEFAULT_POWER = 0.80

NORM = NormalDist()


def required_n_per_arm(baseline: float, target: float, alpha: float, power: float) -> int:
    """Sample size per arm for a two-sided two-proportion test.

    Normal approximation with pooled variance under the null. Adequate above
    roughly 30 expected conversions per arm; below that it understates, which is
    why check_conversion_floor() warns separately.
    """
    z_alpha = NORM.inv_cdf(1 - alpha / 2)
    z_beta = NORM.inv_cdf(power)
    pooled = (baseline + target) / 2
    numerator = (
        z_alpha * math.sqrt(2 * pooled * (1 - pooled))
        + z_beta * math.sqrt(baseline * (1 - baseline) + target * (1 - target))
    ) ** 2
    return math.ceil(numerator / (target - baseline) ** 2)


def check_conversion_floor(n: int, rate: float) -> str | None:
    """Warn when the normal approximation is being pushed past where it holds."""
    expected = n * rate
    if expected < 30:
        return (
            f"Only ~{expected:.0f} conversions expected per arm. Below ~30 the normal "
            "approximation understates the sample needed; treat this as a floor, not a target."
        )
    return None


def cmd_size(args: argparse.Namespace) -> int:
    baseline = args.baseline
    if not 0 < baseline < 1:
        print(f"error: --baseline must be a rate between 0 and 1, got {baseline}", file=sys.stderr)
        print("hint: 0.4% is 0.004, not 0.4", file=sys.stderr)
        return 2

    if args.absolute:
        target = baseline + args.mde / 100
        lift_desc = f"{args.mde:g} percentage points absolute"
    else:
        target = baseline * (1 + args.mde / 100)
        lift_desc = f"{args.mde:g}% relative"

    if not 0 < target < 1:
        print(
            f"error: a {lift_desc} lift on a {baseline:.4%} baseline gives {target:.4%}, "
            "which is not a valid rate.",
            file=sys.stderr,
        )
        return 2

    n = required_n_per_arm(baseline, target, args.alpha, args.power)
    total = n * args.arms

    print(f"Baseline:            {baseline:.4%}")
    print(f"Detectable target:   {target:.4%}  ({lift_desc})")
    print(f"Alpha {args.alpha:g}, power {args.power:g}, {args.arms} arms")
    print()
    print(f"Required per arm:    {n:,}")
    print(f"Required total:      {total:,}")

    if args.daily_traffic:
        if args.daily_traffic <= 0:
            print("error: --daily-traffic must be positive", file=sys.stderr)
            return 2
        days = math.ceil(total / args.daily_traffic)
        print(f"At {args.daily_traffic:,}/day:  {days:,} days ({days / 7:.1f} weeks)")
        if days > 28:
            print()
            print(
                "VERDICT: not runnable as scoped. Beyond ~4 weeks, seasonality and "
                "population drift contaminate the comparison faster than the test resolves.\n"
                "Change the question: test a bigger swing, move to a higher-traffic surface, "
                "or fix the constraint directly instead of measuring it."
            )
        elif days < 7:
            print()
            print(
                "NOTE: run a minimum of one full week regardless of when significance "
                "appears, so every weekday is represented in both arms."
            )

    warning = check_conversion_floor(n, baseline)
    if warning:
        print()
        print(f"WARNING: {warning}")
    return 0


def cmd_evaluate(args: argparse.Namespace) -> int:
    for label, n, conv in (("a", args.a_n, args.a_conv), ("b", args.b_n, args.b_conv)):
        if n <= 0:
            print(f"error: --{label}-n must be positive, got {n}", file=sys.stderr)
            return 2
        if not 0 <= conv <= n:
            print(
                f"error: --{label}-conv ({conv}) must be between 0 and --{label}-n ({n})",
                file=sys.stderr,
            )
            return 2

    p_a = args.a_conv / args.a_n
    p_b = args.b_conv / args.b_n
    pooled = (args.a_conv + args.b_conv) / (args.a_n + args.b_n)
    se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / args.a_n + 1 / args.b_n))

    print(f"A: {args.a_conv:,}/{args.a_n:,} = {p_a:.3%}")
    print(f"B: {args.b_conv:,}/{args.b_n:,} = {p_b:.3%}")

    if se_pooled == 0:
        print("\nNo conversions in either arm. Nothing to test.")
        return 0

    z = (p_b - p_a) / se_pooled
    p_value = 2 * (1 - NORM.cdf(abs(z)))
    se_diff = math.sqrt(p_a * (1 - p_a) / args.a_n + p_b * (1 - p_b) / args.b_n)
    margin = NORM.inv_cdf(1 - args.alpha / 2) * se_diff
    diff = p_b - p_a
    rel = (diff / p_a * 100) if p_a else float("nan")

    print(f"Observed difference: {diff:+.3%} ({rel:+.1f}% relative)")
    print(f"{1 - args.alpha:.0%} CI on the difference: [{diff - margin:+.3%}, {diff + margin:+.3%}]")
    print(f"z = {z:.3f}, two-sided p = {p_value:.4f}")
    print()

    # The CI, not the p-value, is what a decision should be read from: it shows
    # the range of effects still compatible with the data.
    if (diff - margin) <= 0 <= (diff + margin):
        print("The confidence interval contains zero. 'No difference' remains compatible with this data.")

    if args.required_n and (args.a_n < args.required_n or args.b_n < args.required_n):
        print(
            f"STOPPED EARLY: {args.required_n:,} per arm was required, "
            f"reached {min(args.a_n, args.b_n):,}."
        )
        print(
            "A p-value from a test stopped when it looked good is not a 5% false positive rate. "
            "Repeatedly checking and stopping on significance inflates it substantially. "
            "This result does not support a rollout decision."
        )
    elif p_value < args.alpha:
        print(
            f"p < {args.alpha:g} at the pre-specified sample size. Before rolling out, confirm the "
            "test ran whole weeks, that no mid-test changes were made, and that the effect holds "
            "in the second half of the window (a first-week-only effect is usually novelty)."
        )

    floor = check_conversion_floor(min(args.a_n, args.b_n), pooled)
    if floor:
        print(f"\nWARNING: {floor}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sample size and result evaluation for two-arm conversion tests."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    s = sub.add_parser("size", help="how many users, and how long, before this test can resolve")
    s.add_argument("--baseline", type=float, required=True, help="current rate, e.g. 0.004 for 0.4%%")
    s.add_argument("--mde", type=float, required=True, help="smallest lift worth detecting, in %%")
    s.add_argument("--absolute", action="store_true", help="treat --mde as percentage points")
    s.add_argument("--daily-traffic", type=int, default=0, help="total daily users across all arms")
    s.add_argument("--arms", type=int, default=2)
    s.add_argument("--alpha", type=float, default=DEFAULT_ALPHA)
    s.add_argument("--power", type=float, default=DEFAULT_POWER)
    s.set_defaults(func=cmd_size)

    e = sub.add_parser("evaluate", help="is an observed result real, and was it stopped early")
    e.add_argument("--a-n", type=int, required=True, help="users in control")
    e.add_argument("--a-conv", type=int, required=True, help="conversions in control")
    e.add_argument("--b-n", type=int, required=True, help="users in variant")
    e.add_argument("--b-conv", type=int, required=True, help="conversions in variant")
    e.add_argument("--required-n", type=int, default=0, help="per-arm sample the test was designed for")
    e.add_argument("--alpha", type=float, default=DEFAULT_ALPHA)
    e.set_defaults(func=cmd_evaluate)

    args = parser.parse_args()
    for name in ("alpha", "power"):
        value = getattr(args, name, None)
        if value is not None and not 0 < value < 1:
            print(f"error: --{name} must be between 0 and 1, got {value}", file=sys.stderr)
            return 2
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
