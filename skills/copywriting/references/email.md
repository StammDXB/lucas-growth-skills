# Email and Newsletter

Load when: writing any email, sequence, broadcast, or newsletter.

Email is read once, often in preview, usually on a phone, sometimes with images
off. It has no navigation, no scroll-back, no second chance. That constraint set
drives everything below.

## The measurement fact that invalidates most email advice

**Open rate is no longer a valid metric.** Apple Mail Privacy Protection affects
roughly 55 to 60% of all opens, and Apple holds 64.66% of email client share.
MPP opens are "not considered reliable opens."
Source: https://www.litmus.com/email-client-market-share (May 2026)

Consequence: any subject-line claim of the form "X increased opens by Y%" that
post-dates 2021 and does not describe MPP filtering is uninterpretable.

**Rule: never A/B test a subject line on open rate.** Test on click-to-delivered
or conversion. Treat pre-2021 open-rate literature as suggestive only.

## Compliance constraints that are copy decisions

These are legal and platform requirements, not style preferences.

**Transactional emails carrying an upsell.** Under 16 CFR 316.3(a)(2), a mixed
message becomes legally commercial if *either* the subject line would lead a
reasonable recipient to conclude it contains a promotion, *or* the transactional
content does not appear "in whole or in substantial part, at the beginning of
the body."
Source: https://www.law.cornell.edu/cfr/text/16/316.3

So: transactional content first and substantial, upsell strictly below it,
subject line describes the transaction only. A promotional subject line on a
receipt reclassifies the message and triggers full CAN-SPAM obligations.

**Gmail bulk sender requirements** (5,000+/day): spam complaint rate below
0.30%, aim below 0.10%. SPF, DKIM and DMARC required. One-click unsubscribe
header **plus a clearly visible unsubscribe link in the body**. Headers and
content "should be accurate, and not misleading or deceptive."
Source: https://support.google.com/a/answer/81126

The 0.30% ceiling is the real link between copy and deliverability. Complaints
come from **expectation mismatch**: unexpected sender, unexpected frequency,
unexpected content type. Not from word choice.

## Deliverability folklore to reject

If a copy suggestion is justified by "spam filters do not like that word,"
reject it. If it is justified by "this will surprise the reader and generate a
complaint," honour it.

- **Spam trigger word lists** ("free", "guarantee", "act now"). No traceable
  primary source. Modern filtering is dominated by authentication, domain and IP
  reputation, and engagement. Directional evidence: the most respected
  independent deliverability blog publishes on DMARC, DKIM2, SPF and BIMI, and
  not on trigger words.
- **The 60/40 image-to-text ratio.** No traceable origin. The real risk is
  different and worth encoding: an image-only email has no text for filters or
  for readers with images off, and renders blank. Fix by making the email
  comprehensible as text, not by hitting a ratio.
- **Link count caps.** What matters is link quality: URL shorteners, mismatched
  display text versus href, low-reputation domains. Raw count is not the
  mechanism.

## Structure by type

| Type | Structure | Quality bar | Distinct failure |
|---|---|---|---|
| Cold outreach | Trigger observation, implication for them, one specific proof, interest-based ask. 50 to 125 words. | Delete the personalized line. If the email still parses, the personalization was decoration. | Personalization that proves research but not relevance ("saw you went to X"). |
| Nurture | One belief per email, each attacking a different objection. An arc, not repetition. | Email 4 must be unreadable as email 1. | Restating the value prop five ways and calling it nurture. |
| Launch | Problem, mechanism, proof, objection, scarcity. Deadline logic must be real. | The reason to act now survives the reader asking "why now?" aloud. | Manufactured urgency. Converts once, then trains the list to ignore you. |
| Transactional + upsell | Transactional first and substantial. Upsell below. | The 316.3(a)(2) two-part test above. | Promotional subject on a receipt. |
| Editorial newsletter | See below. | Would a subscriber notice if it stopped arriving? | Drifting into promotion, breaking the opt-in contract. |
| Re-engagement | Name the silence, make leaving easy, one low-friction action. 2 to 3 emails, then suppress. | Willingness to actually remove people. | Re-engaging inactives into a list that then blows the 0.30% ceiling. |

## Sequence design

- Welcome: 3 to 5. Email 1 delivers the promised thing and sets cadence. Nothing else.
- Nurture: 5 to 7, one objection each, spaced 2 to 4 days.
- Launch: 5 to 8, compressed into 7 to 10 days.
- Re-engagement: 2 to 3, then suppress.

**The build test:** write the one-sentence argument of each email in a column.
If any two are interchangeable, or if reordering costs nothing, you have a
broadcast series, not a sequence. Each email should make the *next* objection
the live one.

## The cutting heuristic

One email, one idea, one action.

**For every paragraph, name which objection it removes.** Paragraphs that remove
no objection are ego, context-setting, or hedging. They go.

Second pass: anything the reader already believes is deletable. Agreement costs
attention and buys nothing.

## CTAs in email specifically

The web constraint set does not apply. Rule: **one destination, multiple entry
points.**

Repeating the same link two or three times (early text link, mid-body, close) is
fine and helps. Two *different* CTAs is the actual error, because it turns a
decision into a comparison.

Never put the only CTA inside an image or a button-only element. With images
blocked, the email renders with no action. Every CTA needs a text-link fallback.

## The editorial newsletter as its own craft

The opt-in is for value, not offers, so the governing question is retention, not
conversion.

The structural pattern that sustains multi-year readership is **a fixed
container with variable contents**. Readers subscribe to a rhythm they can
predict and a voice they cannot get elsewhere. Consistency of slot and shape does
more for retention than variance in peak quality.

Worth studying: Stratechery (analytical throughline), Lenny's Newsletter
(operator-grade specificity), NextDraft (voice-driven curation), Total Annarchy
(craft and personal register), Morning Brew (tone on commodity news). Inbox
Collective (https://inboxcollective.com) is the strongest single source on
newsletter retention and business model.

Failure mode specific to this type: the newsletter becomes a distribution
channel for promotions, the implicit contract breaks, unsubscribes and
complaints rise. Complaints feed the 0.30% ceiling. **Editorial drift is a
deliverability risk.**

## Diagnosable failures

1. Sender-centric opening. Diagnostic: I/we outnumbers you/your in the first 50 words.
2. Decorative personalization. Diagnostic: removing it leaves the email intact.
3. Two CTAs. Diagnostic: two distinct destinations.
4. Sequence that repeats instead of builds. Diagnostic: emails reorderable at no cost.
5. Image-dependent action. Diagnostic: with images off, no CTA is reachable.
6. Deceptive subject. Diagnostic: subject promises what the body does not deliver.
7. Promotional subject on transactional. Diagnostic: fails the 316.3(a)(2) test.
8. Manufactured urgency. Diagnostic: the deadline has no mechanism behind it.
9. Unearned length. Diagnostic: a paragraph that removes no objection.
10. Editorial drift. Diagnostic: promotional content exceeds the opt-in contract.

## Worked example

**Before** (cold outreach, 96 words)

> Subject: Quick question
>
> Hi Sarah, I hope this email finds you well! I saw that you recently attended
> the Hospitality Innovation Summit, which looked amazing.
>
> I'm reaching out because we're a leading provider of AI-powered marketing
> automation for hospitality groups. We help companies like yours streamline
> operations, increase revenue, and delight guests through our best-in-class
> platform.
>
> Would you be open to a 30-minute call next week? You can book on my calendar
> here. Also, feel free to check out our case studies page.

Diagnosis: vague subject failing the accuracy standard; decorative
personalization; vendor-centric second paragraph; three abstract claims and zero
proof; two CTAs; high-friction ask.

**After** (61 words)

> Subject: Your three properties, one booking system
>
> Sarah,
>
> You mentioned at the Innovation Summit that Rosewood's three properties still
> run separate booking stacks. That is usually where the revenue leaks: guests
> who book one property never get seen by the other two.
>
> We fixed exactly that for a four-property group last year. Cross-property
> repeat bookings went from 4% to 19% in two quarters.
>
> Worth a look?

What changed: subject now accurately describes the body. Personalization is
load-bearing, because removing it removes the reason for the email. Her problem
stated before anything about the sender. One concrete proof replaces three
abstractions. One CTA, interest-based, answerable in two words, as a text line
so it survives image blocking.

## Evidence notes

Verified: the Litmus client-share and MPP figures, the Gmail bulk sender
requirements, and 16 CFR 316.3(a)(2), all cited above.

Not verified: subject-line formulas (specificity, question, number, direct
statement) are widely repeated with no traceable controlled origin, and their
historic metric is now unmeasurable. Use them as generative options, never as
claims. The newsletter characterizations above are secondary sources.
