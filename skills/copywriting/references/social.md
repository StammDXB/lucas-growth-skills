# Social Posts and Captions

Load when: writing a post or caption for LinkedIn, X, or Instagram.

Social media is the most folklore-heavy area in marketing. Everything below is
graded. VERIFIED means an official platform document, engineering blog, or the
original paper. FOLKLORE means repeated everywhere and traceable to nothing.

## The finding that changes how you write for LinkedIn

**LinkedIn ranks on dwell and skip, not on likes.**

LinkedIn's engineering blog states the feed ranks with a head targeting
"passive tasks (click, skip, long-dwell) and active tasks (like, comment,
share)." Passive tasks are named first, and **skip is an explicit prediction
target**. The model trains on "what you've read, liked, commented on, returned
back to, or simply scrolled past."
Source: https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed (March 2026)

The rationale, from LinkedIn's earlier dwell-time post: "Click and viral actions
can be rare, especially for passive consumers of the feed," they are "primarily
binary indicators," and "Clicks are noisy indicators of engagement." LinkedIn
built a P(skip) model and reported a "Large decrease in the number of skipped
updates."
Source: https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time

**Consequence:** a post that holds a reader eleven seconds with zero likes feeds
the ranker better than one that earns a reflexive like in one second. This kills
the entire engineer-the-comment school mechanically, not just on taste grounds.
Write to hold attention, not to extract a reaction.

## What the diffusion literature actually shows

**Goel, Anderson, Hofman and Watts, "The Structural Virality of Online
Diffusion," Management Science 62(1), 2016.** Roughly 1 billion diffusion events
on Twitter, ~622 million unique pieces of content.

- Average cascade size is **1.3**.
- "about 99% of adoptions are accounted for by either the root nodes themselves
  or the immediate followers of root nodes." Almost nothing spreads past one hop.
- Only **0.025%** of diffusion trees reach 100 nodes, "roughly 1 out of every
  4,000 cascades."
- "viral hits appear at a rate closer to one in a million."
- "popularity is largely driven by the size of the largest broadcast."

**Salganik, Dodds and Watts, Science 311, 2006.** 14,341 participants, eight
independent social-influence worlds plus a control.

- "Increasing the strength of social influence increased both inequality and
  unpredictability of success."
- "The best songs rarely did poorly, and the worst rarely did well, but any
  other result is possible."

**Where this honestly leaves advice:**

1. There is no viral formula, and its absence is a finding, not a gap in your knowledge.
2. Reach is mostly broadcast. Distribution you control dominates content properties.
3. **Craft is downside protection, not upside generation.** Quality reliably removes the floor and cannot manufacture the ceiling. That is the right reason to hold a bar and the wrong reason to expect a spike.
4. Judge on the median across 20-plus posts. Single-post performance is nearly noise.
5. You cannot control cascades. You *can* control dwell and skip, and LinkedIn published that those are the targets.

## Per platform

### LinkedIn

- **3,000 character limit.** VERIFIED: https://www.linkedin.com/help/linkedin/answer/a528176/
- **The "see more" fold.** Commonly cited as ~140 mobile / ~210 desktop. UNVERIFIED, no official source. Write so the first ~140 characters stand alone as a complete, non-teasing thought. That is safe whichever number is real.

Structure: hook that survives truncation and needs no context; body making one
claim with evidence; close that lands a position or concedes a limit.
Specificity is the dwell engine. Abstraction is the skip trigger.

**Engagement pods are an explicit policy violation.** LinkedIn Professional
Community Policies: "Don't do things to artificially increase engagement with
your content. Respond authentically to others' content and don't agree with
others ahead of time to like or re-share each other's content."
Source: https://www.linkedin.com/legal/professional-community-policies

### X

The open-sourced algorithm repo documents post-ranking heuristics: "Author
Diversity," "Content Balance (In network vs Out of Network)," "Feedback
fatigue," and deduplication.
Source: https://github.com/twitter/the-algorithm

**The repo does not publish prediction targets or engagement weights.** Every
specific weight in circulation (the "a reply is worth 27x a like" genre) comes
from a 2023 snapshot and is not in current documentation. Grade FOLKLORE. Do not
encode numeric weights.

Author diversity and feedback fatigue mean posting frequency has diminishing and
then negative returns on a single reader's timeline.

- **280 characters standard, up to 25,000 for long posts.** VERIFIED via official help text.

Craft: X rewards a complete thought in one breath. The unit is the claim, not
the post. A 280-character post carrying a full argument beats a thread whose
argument only completes at tweet 7, because fatigue and diversity throttle the
tail. Threads work when each unit stands alone.

### Instagram

**The caption is not in Instagram's stated ranking signals.** Instagram's own
ranking explainer lists, for Feed: your activity, then post information, then
information about the poster, then history of interacting with them. Captions
appear nowhere.
Source: https://about.instagram.com/blog/announcements/instagram-ranking-explained

**Consequence, and it is a hard rule:** Instagram captions do not drive
distribution. They convert attention the image or video already won. Front-load
the payoff. No throat-clearing.

**Verified reduced-visibility list for Reels:** "low-resolution or watermarked
reels, reels that are muted or contain borders, reels that are majority text, or
reels that have already been posted on Instagram." This kills naive TikTok
cross-posting.

- **The 2,200 character caption limit is UNVERIFIED.** Universally repeated, absent from every official doc. Do not state it as fact.
- **The "125 character truncation" claim is a confusion.** 125 characters is Meta's recommended *primary text for Instagram feed ads*, a paid placement spec, not an organic truncation point.

## Hooks

The opening line does the work, because it is the only line guaranteed to render
and because it decides dwell versus skip.

| Pattern | Mechanism |
|---|---|
| Concrete anomaly | A specific number violating expectation creates a prediction error the reader must resolve. Resolution requires dwell. |
| Named cost | Stakes legible immediately, no setup needed. |
| Falsifiable claim | Invites disagreement, which is dwell, without soliciting it. |
| Compressed scene | Concrete nouns render instantly; abstractions require decoding. |
| Reversal of received wisdom | Only works if you then actually defend it. |

**Anti-patterns that now read as bait:** curiosity gap with withheld payoff;
fake-vulnerability opener; manufactured hesitation ("I debated whether to post
this"); rhetorical question as line one; countdown promise ("5 lessons from 10
years"); single-word line followed by whitespace.

**The diagnostic:** if the first line could be prefixed to a hundred different
posts unchanged, it is a throat-clear, not a hook. A real hook is unusable on
any other post.

## Engagement bait, per official policy

Meta defines it as "Posts that explicitly request engagement (such as votes,
shares, comments, tags, likes, or other reactions) for purposes other than a
specific call to action," and lists it among content it demotes.
Source: https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/engagement-bait/

Genuine requests for "help, advice, or recommendations" are explicitly exempted.

**The exemption is the design spec.** "Comment YES and I'll DM you the template"
is bait. "If you have solved this differently I want to hear it" is a request
for advice. The difference is whether the response has value to you as
information rather than as a count.

Caveat: Meta's pages discuss Facebook. None explicitly extended these demotions
to Instagram. Do not claim Instagram engagement-bait demotion as verified.

## Formatting: real versus cargo cult

| Practice | Grade | Verdict |
|---|---|---|
| First line survives truncation | Real constraint | Write to ~140 chars |
| Short paragraphs | Real | Because LinkedIn predicts skip and dense blocks get skipped, not because "the algorithm likes whitespace" |
| One sentence per line throughout | FOLKLORE | "Broetry." A recognised low-status tell. Break where meaning breaks. |
| Emoji as bullets | FOLKLORE, harmful | The strongest visual slop signature. Ban outright. |
| Hashtags for LinkedIn reach | UNVERIFIED | No official source documents a benefit. Zero to two, only if genuinely categorical. |
| Hashtags for Instagram reach | SECONDARY, negative | Mosseri has stated hashtags do not increase reach. Treat as topic labels. |
| External links suppressed | FOLKLORE | No platform documents a link penalty. Sourced nowhere. |
| "Comment then edit to add the link" | FOLKLORE | Ritual derived from the unverified link penalty. |
| Posting-time precision | FOLKLORE | Recency is a documented signal; "post at 8:47am Tuesday" is not. |
| Reposting the same Reel | VERIFIED penalty | Explicit in Instagram's ranking doc |
| Text-heavy, watermarked, bordered, muted Reels | VERIFIED penalty | Explicit |
| More posting always helps | Contradicted | X documents author diversity and feedback fatigue |

## The thought leadership post

The distinction is not tone. It is **epistemic risk**.

A post builds authority when the author has something to lose by being wrong. It
performs and cheapens when the author has arranged to be un-wrong.

**Authority markers:** a falsifiable claim stated plainly enough to argue with;
specifics that cost something to disclose; **a stated limit** ("this does not
hold below four people"); credit where the idea came from someone else.

**Cheapening markers:** universally agreeable claims; borrowed authority
(someone else's parable, the invented cab driver); vulnerability with a
guaranteed payoff; advice with no scope; post-hoc narration of a win as a
repeatable method.

**The test:** could a competent person in your field publicly disagree with this
post? If no, you have written a fortune cookie.

## AI tells

Readers are saturated and now pattern-match against generated text. Ordered by
reliability:

1. **"It's not X. It's Y."** antithesis, especially isolated on its own line.
2. **Rule of three everywhere.** Three examples, three adjectives, relentlessly.
3. **Emoji-as-bullet lists**, particularly ✅ 🚀 💡 👇.
4. **Empty setup phrases:** "Here's the thing," "Let that sink in," "The truth?"
5. **Corporate openers:** "In today's fast-paced digital landscape."
6. **Hollow symmetry.** Parallel structure carrying no actual contrast.
7. **Uniform paragraph length.** Human writing is metrically irregular.
8. **Named-entity vacuum.** No client, number, date, place, or product.
9. **Tidy resolution.** Every anecdote concludes with a clean lesson. Real events do not.
10. **Concession-free.** No scope limit, no exception. The deepest tell, because
    hedging correctly requires knowing the boundary.

**Rule:** three or more tells means rewrite from the source facts. Editing
generated text preserves its skeleton.

## Worked example

**Before**

> 🚀 Let's talk about marketing teams.
> In today's fast-paced digital landscape, businesses are constantly struggling.
> Here's the thing: it's not about working harder. It's about working smarter.
> ✅ Teams that scale headcount without structure
> ✅ Leaders who confuse activity with progress
> The truth? Architecture beats headcount. Every single time.
> What do you think? Drop a comment below! 👇
> #marketing #leadership #growth #strategy

Diagnosis: tells 1, 2, 3, 4, 5, 6, 8, 9, 10 present. Hook works on any post. No
checkable facts. Nobody can disagree with any sentence. Bait close is
policy-exposed. Hashtag stack with no documented benefit.

**After**

> A hospitality group I worked with had eleven people in marketing and nobody who
> could say which channel produced last month's bookings.
>
> They did not have a headcount problem. Eleven was plenty. They had eleven people
> pointed at eleven different definitions of the job.
>
> We cut no one. We drew one diagram: who owns demand, who owns conversion, who
> owns retention, and what number each brings on Monday.
>
> Six weeks later the same eleven people were producing a weekly number the CEO
> trusted enough to set budget against.
>
> The uncomfortable part: if your marketing team feels understaffed, a twelfth
> hire will make the ambiguity worse. Ambiguity scales faster than headcount.
>
> I am less sure this holds under four people. Below that, structure may just be
> overhead.

Why: first line is 134 characters, lands above any plausible fold, is a complete
concrete scene, and is unusable on another post. Concrete nouns and numbers drive
dwell rather than skip. Contains a falsifiable claim. Closes on a stated scope
limit, which generated text almost never produces. No CTA, hashtags, or emoji.
Irregular paragraph lengths.

## Checklist

**Universal:** first 140 characters stand alone; hook unusable elsewhere; at
least one disputable claim; at least one checkable specific; no emoji bullets;
fewer than three AI tells; close does not solicit engagement for its own sake;
irregular paragraph lengths.

**LinkedIn:** under 3,000 characters; written to hold 10-plus seconds; zero to
two hashtags; no pod coordination; includes a scope limit or concession.

**X:** complete claim within 280 characters or self-sufficient preview; not
dependent on a thread tail; no reply-solicitation; cadence accounts for author
diversity and feedback fatigue.

**Instagram:** caption converts attention the visual won; payoff in the first
clause; hashtags as topic labels; Reels not majority text, watermarked, bordered,
muted, or previously posted.

**Strategy:** judge on median across 20-plus posts; never claim a viral formula;
frame craft as downside protection.
