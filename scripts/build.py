#!/usr/bin/env python3
"""Compile source skills into self-contained Claude Desktop skill zips.

Skills cannot reference each other at runtime in Claude Desktop, so shared
knowledge (lenses) and validators (rubrics) are compiled into each skill that
declares them. Authoring stays DRY; distribution is self-contained.

Usage:
    python3 scripts/build.py              build all skills
    python3 scripts/build.py copywriting  build one
    python3 scripts/build.py --check      validate only, emit nothing
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
LENSES_DIR = ROOT / "lenses"
RUBRICS_DIR = ROOT / "rubrics"
BUILD_DIR = ROOT / "build"
DIST_DIR = ROOT / "dist"
# Committed Claude Code plugin tree. Desktop uses dist/*.zip; Claude Code
# consumes this directory via .claude-plugin/marketplace.json, so unlike dist/
# it must be checked in.
PLUGIN_DIR = ROOT / "plugin"

# Limits from https://agentskills.io/specification
MAX_DESCRIPTION_CHARS = 1024
MAX_NAME_CHARS = 64
MAX_SKILL_MD_LINES = 500
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Matches markdown links and bare paths pointing into bundled directories.
REF_PATTERN = re.compile(r"(?:references|assets|scripts)/[A-Za-z0-9._/-]+")
# Manifest descriptions open with the skill count, e.g. "10 skills: ..."
LEADING_COUNT = re.compile(r"^\s*(\d+)\b")


@dataclass
class Result:
    name: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a SKILL.md into (frontmatter dict, body). Raises on malformed."""
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must open with '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :]


def validate_frontmatter(fm: dict, skill_name: str, res: Result) -> None:
    name = fm.get("name")
    if not name:
        res.errors.append("frontmatter missing 'name'")
    else:
        if name != skill_name:
            res.errors.append(f"name '{name}' does not match directory '{skill_name}'")
        if len(name) > MAX_NAME_CHARS:
            res.errors.append(f"name exceeds {MAX_NAME_CHARS} chars")
        if not NAME_PATTERN.match(name):
            res.errors.append(
                f"name '{name}' must be lowercase alphanumeric with single hyphens"
            )

    desc = fm.get("description")
    if not desc:
        res.errors.append("frontmatter missing 'description'")
    elif len(desc) > MAX_DESCRIPTION_CHARS:
        res.errors.append(
            f"description is {len(desc)} chars, limit is {MAX_DESCRIPTION_CHARS}"
        )


def validate_references(skill_out: Path, body: str, res: Result) -> None:
    """Every referenced bundled file must exist.

    This repo previously shipped 46 references to files that never existed.
    That is the failure this check prevents, so it is an error, not a warning.
    """
    for ref in sorted(set(REF_PATTERN.findall(body))):
        cleaned = ref.rstrip(".,);:")
        if not (skill_out / cleaned).exists():
            res.errors.append(f"references missing file: {cleaned}")


def validate_no_orphans(skill_out: Path, body: str, res: Result) -> None:
    """Every bundled reference must be reachable from SKILL.md.

    The reverse of validate_references. Progressive disclosure means a
    reference is only ever read because the body told Claude to read it, so a
    bundled file the body never names is invisible: it costs ZIP size and
    contributes nothing. Spec quality bar item 5 requires every reference to
    carry a load-trigger.

    A warning rather than an error, because the fix is a content decision:
    either give the file a load-trigger in the body, or stop declaring it in
    skill.yaml.
    """
    refs_dir = skill_out / "references"
    if not refs_dir.is_dir():
        return
    for path in sorted(refs_dir.rglob("*.md")):
        if path.stem not in body:
            res.warnings.append(
                f"bundled but never referenced in SKILL.md: "
                f"references/{path.relative_to(refs_dir)}"
            )


def _manifest_description(path: Path, res: Result) -> str | None:
    """Pull the user-facing description out of either manifest shape."""
    if not path.exists():
        res.errors.append(f"missing manifest: {path.relative_to(ROOT)}")
        return None
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        res.errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return None
    if "plugins" in data:  # marketplace.json
        entries = data.get("plugins") or []
        return entries[0].get("description", "") if entries else ""
    return data.get("description", "")  # plugin.json


def validate_distribution(skill_names: list[str], res: Result) -> None:
    """Check the hand-maintained manifests and the plugin tree against reality.

    Two failures this catches, both of which have already shipped:

    1. Manifest drift. build.py rebuilds plugin/skills/ but never touches
       marketplace.json or plugin.json, so their descriptions go stale the
       moment a skill is added. The pack shipped advertising 7 skills while
       bundling 10, and the marketplace UI showed the stale number.
    2. A stale plugin tree, which is what running build.py without --plugin
       leaves behind. The Claude Code marketplace then serves yesterday's
       skills with no other signal that anything is wrong.
    """
    count = len(skill_names)

    for path in (
        ROOT / ".claude-plugin" / "marketplace.json",
        PLUGIN_DIR / ".claude-plugin" / "plugin.json",
    ):
        desc = _manifest_description(path, res)
        if desc is None:
            continue
        rel = path.relative_to(ROOT)
        match = LEADING_COUNT.match(desc)
        if not match:
            res.warnings.append(
                f"{rel}: description opens with no skill count, so it cannot be "
                f"checked against the {count} skills that ship"
            )
            continue
        stated = int(match.group(1))
        if stated != count:
            res.errors.append(
                f"{rel}: description says {stated} skills, but {count} ship"
            )

    for name in skill_names:
        src = SKILLS_DIR / name / "SKILL.md"
        out = PLUGIN_DIR / "skills" / name / "SKILL.md"
        if not out.exists():
            res.errors.append(
                f"plugin/skills/{name}/ is missing; run build.py --plugin"
            )
        elif src.read_text() != out.read_text():
            res.errors.append(
                f"plugin/skills/{name}/SKILL.md is stale; run build.py --plugin"
            )


def compile_skill(skill_dir: Path, check_only: bool, plugin_mode: bool = False) -> Result:
    name = skill_dir.name
    res = Result(name=name)

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        res.errors.append("no SKILL.md")
        return res

    raw = skill_md.read_text()
    try:
        fm, body = parse_frontmatter(raw)
    except ValueError as exc:
        res.errors.append(str(exc))
        return res

    validate_frontmatter(fm, name, res)

    line_count = len(raw.splitlines())
    if line_count > MAX_SKILL_MD_LINES:
        res.errors.append(
            f"SKILL.md is {line_count} lines, limit is {MAX_SKILL_MD_LINES}"
        )

    # Stage the skill: copy source, then compile in declared lenses and rubrics.
    out = BUILD_DIR / name
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(
        skill_dir, out, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__")
    )

    config_path = skill_dir / "skill.yaml"
    config = yaml.safe_load(config_path.read_text()) if config_path.exists() else {}
    config = config or {}

    refs_out = out / "references"
    refs_out.mkdir(exist_ok=True)

    for lens in config.get("lenses", []):
        src = LENSES_DIR / f"{lens}.md"
        if not src.exists():
            res.errors.append(f"declared lens not found: {lens}")
            continue
        shutil.copy2(src, refs_out / f"{lens}.md")

    for rubric in config.get("rubrics", []):
        src = RUBRICS_DIR / f"{rubric}.md"
        if not src.exists():
            res.errors.append(f"declared rubric not found: {rubric}")
            continue
        shutil.copy2(src, refs_out / f"{rubric}.md")

    # skill.yaml is a build-time artifact; it must not ship.
    (out / "skill.yaml").unlink(missing_ok=True)
    # evals are for development, not for the user's Desktop.
    shutil.rmtree(out / "evals", ignore_errors=True)

    validate_references(out, body, res)
    validate_no_orphans(out, body, res)

    if check_only or not res.ok:
        shutil.rmtree(out, ignore_errors=True)
        return res

    if plugin_mode:
        target = PLUGIN_DIR / "skills" / name
        if target.exists():
            shutil.rmtree(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(out, target)
        shutil.rmtree(out, ignore_errors=True)
        return res

    DIST_DIR.mkdir(exist_ok=True)
    zip_path = DIST_DIR / f"{name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(out.rglob("*")):
            if path.is_file():
                zf.write(path, Path(name) / path.relative_to(out))

    shutil.rmtree(out, ignore_errors=True)
    return res


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check" in sys.argv
    plugin_mode = "--plugin" in sys.argv

    if plugin_mode:
        # Rebuild from scratch so removed skills do not linger in the plugin.
        shutil.rmtree(PLUGIN_DIR / "skills", ignore_errors=True)

    if not SKILLS_DIR.exists():
        print(f"no skills directory at {SKILLS_DIR}")
        return 1

    targets = (
        [SKILLS_DIR / a for a in args]
        if args
        else sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    )

    BUILD_DIR.mkdir(exist_ok=True)
    results = [compile_skill(t, check_only, plugin_mode) for t in targets if t.is_dir()]
    shutil.rmtree(BUILD_DIR, ignore_errors=True)

    # Only meaningful across the full set: a single-skill build would compare
    # the manifests against a count of 1. Runs after compilation so --plugin
    # validates the tree it just wrote, while --check validates the committed one.
    if not args:
        dist_res = Result(name="distribution")
        validate_distribution([t.name for t in targets if t.is_dir()], dist_res)
        results.append(dist_res)

    failed = 0
    for r in results:
        if r.ok:
            note = "checked" if check_only else "built"
            print(f"  OK       {r.name} ({note})")
        else:
            failed += 1
            print(f"  FAILED   {r.name}")
            for err in r.errors:
                print(f"             {err}")
        for warn in r.warnings:
            print(f"             warning: {warn}")

    print(f"\n{len(results) - failed}/{len(results)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
