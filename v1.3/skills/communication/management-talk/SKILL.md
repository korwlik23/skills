---
name: management-talk
description: >
  Use this skill to rewrite engineer-to-engineer content for engineering-org
  leadership (VPs, directors, PMs, release managers, execs in technical
  companies) and shape it for the channel it is going to — ticket comment,
  Slack post, async standup line, email, or meeting talking-points. Trigger
  when the user asks to write/rewrite for management / exec / VP / director /
  PM / release manager, asks for an "executive summary", "leadership update",
  or "status update", says "make this less technical / less jargony", or asks
  for a slack / email / standup / meeting version of work originally written
  engineer-to-engineer.
---

# Management Talk

Same audience and translation rules as a written status report, but **shaped for the
channel** — ticket comment, Slack post, async standup, email, or meeting talking-points.
The audience reads code names but not code. The channel decides the length, formatting,
and how much structure to leave on the page.

Use this any time engineering content needs to flow up the org, sideways into product /
release management, or into a non-engineering meeting — regardless of destination.

The natural input is the output of [`post-mortem`](../post-mortem/SKILL.md). post-mortem
owns the engineering truth; this skill reframes it for the channel.

## Production-Grade Operating Contract

- Before starting, read `../../../RULES.md` and apply it as the behavior, safety, validation,
  and communication baseline — including the two HARD GATES and the three-iteration rule.
- This skill **never invents facts**. If the source says "root cause unknown," the
  rewrite says "root cause unknown." Do not promote speculation to a finding for
  narrative tidiness.
- Get sign-off before posting to any external system. Print-only output (the user
  copies it themselves) needs no approval.

## When to invoke

- "write something for management / exec / VP / director / PM / release manager"
- "rewrite this for [non-eng audience]"
- "make this non-technical / less techy / less jargony"
- "send a slack update / standup note / email" *about a piece of engineering work*
- "executive summary / exec summary / leadership update / status update"
- "talking points for [meeting]" *based on an engineering update*

If the channel is unclear after the trigger, ask one short question — *"ticket, Slack,
standup, email, or meeting talking-points?"* — and stop.

## Audience — what "engineering-org leadership" means

Engineering-savvy non-engineers: VPs, directors, PMs, release managers, execs in
companies that ship technical products. They read product / framework names and
cross-reference ticket keys and PRs. They do not read code.

They want: *what's the state, what does it mean for customers, who owns it, what's next.*
They do not want: how the bug works at the function level.

This is **not** for marketing, finance, customer-facing, or true ELI5 audiences — those
need a different rewrite. Flag and confirm before producing one.

## Tone — Keep / Strip / Translate

**Keep.** Product names, framework names, team-owned component names, ticket keys, PR
numbers, customer / workload identifiers. These are the bridge between engineering and
leadership tracking — losing them breaks cross-reference.

**Strip.** Function names, file paths, struct fields, commit SHAs, code expressions,
env var names, line numbers, internal data-structure jargon. None of this is actionable
to the audience.

**Translate.** Mechanism into one or two sentences of plain-English cause-and-effect.
Not *"the worker hashed a mutable field"* but *"the system used a fingerprint that the
producer was rewriting, so duplicate-detection silently failed."* Translate without
lying — a race stays a race; a regression stays a regression.

**Don't over-strip.** Engineering-org leadership reads concept-level technical
vocabulary fluently — *race condition, idempotency, dedupe, retry, queue, latency
spike, regression, rollback, canary, soak test*. The line is between *concept exists
and matters here* (keep) and *here's the function / struct / file / SHA* (strip).
Replacing "race condition" with "timing issue" patronises the reader.

**Bias toward** active voice, concrete subjects, short paragraphs. *"We found the bug.
Sarah wrote the fix. PR is up for review."* beats *"The root cause has been identified
and a fix has been authored and submitted for review."*

**Avoid:**

- Hedging that isn't really hedging (*"we believe," "appears to," "may have"*). State
  it or don't.
- Re-stating the obvious for thoroughness (*"This bug is in our webhook system, which
  delivers notifications, which are important for customers, which..."*).
- Telling leadership how to do their job (*"you should prioritise," "this needs to
  land before X"*). Give them the facts; they decide.
- Engineering-process minutiae: bisect runs, debug iterations, debugger sessions.
  They care that you found it, not how. Exception: when the *process* itself is the
  story (*"we burned three weeks before realising the bisect was misleading"*), one
  sentence as a learning — not a play-by-play.

## Channel shapes

Same content, different shell. Pick the shape that matches the destination.

### Ticket comment / written status report

Full structured block. Bolded section labels. Easy to scan from the ticket page.

Building blocks (use as many as fit):

- **Status / TL;DR.** One bolded line. Reader can stop here and have the right answer.
  *"Fixed pending merge."* / *"Root cause unknown — investigating."* /
  *"Blocked on vendor."* / *"Customer-visible regression in 7.2; rollback in flight."*
- **Impact.** Who's affected, how badly, what they see. Customer / workload / product
  terms, not test-suite terms.
- **What broke.** Short paragraph. Plain-English mechanism, one level of why, no code
  identifiers.
- **Why now / how it slipped through.** Optional. Include when leadership will ask
  anyway: latent regression, CI gap, prior incomplete fix, change that landed during
  a freeze.
- **Owner.** Person + team + their PR / branch / ticket artifact. One link, not five.
- **Next steps.** Concrete, near-term, ordered.
- **Workaround / mitigation.** If customers are hitting it now, what can they do today?
  One sentence.
- **Risk.** Optional. Real risks only — don't manufacture risk to look thorough.

Order by what matters most for *this* item.

### Slack — channel post or DM

Single message, no walls of text. Heavy bolded section labels read as "I escaped from
the ticket tracker" — don't.

- One **bolded TL;DR** as the first line.
- 2–4 short bullets underneath: impact, owner+link, next step. Drop blocks that don't
  apply.
- One link, embedded inline. Not a link wall.
- No greeting, no signoff. The channel is the context.
- If it's a **thread reply** rather than a new post, lose the TL;DR — just lead with the
  answer.

Length target: under ~80 words for a top-level post; under ~40 for a thread reply.

### Async standup note

The audience scans 10 of these in 30 seconds. Front-load the verb.

- 1–3 lines, max.
- Pattern: *"\<state\> \<thing\>. \<owner if not me\>. \<next\>."*
- No bullets, no bolded labels. The format **is** the sentence.

### Email — internal exec / cross-team

Subject line is half the value.

- **Subject:** the TL;DR rewritten as a noun phrase.
  *"Webhook dedupe regression: fix merged, monitoring (WEBHOOK-1042)."*
- **Greeting:** match the recipient register (*Hi Sam,* / *Hi all,*).
- **Body:** the ticket-comment shape, but as flowing paragraphs separated by blank
  lines rather than bolded section labels. Two or three paragraphs is plenty.
- **Sign off** with the next decision point that needs the recipient's attention, if
  any. If none, a plain *"— [Name]"* is fine.

### Meeting talking-points

You're going to *say* this, not show it.

- Bullet list, max one short clause per bullet.
- Order is the order you'll speak in.
- Include the numbers / keys you want to reference out loud, in the bullet itself, so
  you don't fumble.
- Skip prose.

## Source material

The input is one of:

1. **A ticket key** — fetch via the ticket system's API (if integrated) and reframe
   the most recent substantive comment. Don't dump the full thread.
2. **A finished post-mortem** — the canonical input. Reuse its Summary, Impact, Fix,
   Owner, Next steps directly.
3. **Pasted technical text.**
4. **The current conversation** — if you (or the user) just produced engineering
   content and the user now says *"now in slack"* / *"now for the VP,"* reuse what's
   in context.

If the source is ambiguous, ask one question and stop.

## Output flow

1. **Confirm the channel** if not stated.
2. **Produce the draft** as a single chat block, formatted as the channel would
   render it.
3. **Ask where it goes:**
   - Default: print-only — the user copies it.
   - Post to a ticket / wiki via tooling: only if the user explicitly says so. Show
     the exact payload, wait for *"post it"* / *"go ahead"* / *"yes,"* then fire.
   - **Never post to Slack, email, or any non-ticketing channel from this skill.**
     Hand the draft to the user; they post it.
4. **One iteration is normal, three is a smell.** If the user is on the third revision,
   ask what specific framing / audience assumption you're missing — don't keep tweaking
   blindly.

## Worked example — same bug, three channels

**Source (the post-mortem from [`post-mortem`](../post-mortem/SKILL.md)):** the
webhook-retry double-processing bug. Engineering record names
`WebhookRetryWorker::idempotencyKey()`, `OrderConfirmedListener::handle`,
`redis://retry-dedupe`, prior fix PR #2790, and the experiment that nailed it.

### As a ticket comment

> **Status: Fixed, in production canary.** Customer impact contained; monitoring.
>
> **Impact:** On 2026-05-22 a Redis latency spike triggered ~412 retried webhook
> deliveries that were not deduplicated. Customers received up to two confirmation
> emails per single purchase. No data loss; ~80 duplicate notifications sent.
>
> **What broke:** Our webhook retry worker used a fingerprint to detect duplicate
> retries. The fingerprint was computed from a field that the producer was rewriting
> between attempts, so duplicate-detection silently failed and a second handler ran.
> The fingerprint logic had been in place for ~14 months; no real workload had
> triggered the overlap until the Redis spike.
>
> **A previous fix** (March 2026) added a fallback path but left the broken default
> in place — this new fix removes the broken path entirely.
>
> **Owner:** Sarah (Webhooks team). PR app/services#2871, ticket WEBHOOK-1042.
>
> **Next steps:** Production canary deployed 2026-05-23 06:00 UTC — watching for
> 24 h before full rollout. Regression test added. CI now replays 1 % of yesterday's
> events nightly to catch future dedupe regressions.

### As a Slack post

> **Webhook retry double-processing is fixed and in canary.** (WEBHOOK-1042)
>
> - May 22 Redis spike caused ~412 retried events to dedupe-miss → up to 2
>   confirmation emails per purchase. ~80 duplicates sent.
> - Root cause: dedupe fingerprint used a mutable field. Latent for 14 months.
> - Owner: Sarah, PR #2871 in canary; full rollout after 24 h watch.

### As a standup note

> Fixed webhook retry dedupe regression from the May 22 Redis spike (WEBHOOK-1042).
> Sarah's PR #2871 in canary; full rollout tomorrow if the 24 h watch is clean.

What changed between channels: same diagnosis, same owner, same next step. The ticket
comment gets every block. Slack drops "previous fix attempt" — too much for the channel.
Standup keeps just state + key + owner + next. None of them mention
`WebhookRetryWorker::idempotencyKey()` or `redis://retry-dedupe`.

## Rules

- **Never invent facts** to make the rewrite cleaner. If the engineering source says
  "root cause unknown," the rewrite says "root cause unknown."
- **Never strip a ticket key, PR number, or customer / workload name** during
  de-jargoning. They are the cross-reference bridge — losing them breaks tracking.
- **Never invent owners.** If the source doesn't name one, ask — don't guess from
  `git blame` or recent commits.
- **Get sign-off before posting to any external system.** Print-only output needs no
  approval.
- **Never post to Slack, email, or any non-ticketing channel from this skill.** Hand
  the draft to the user; they post it.
- **Stay out of advocacy.** This skill produces a status update, not a recommendation.
  If the user wants a recommendation memo, confirm before reframing.
- **One iteration is normal, three is a smell.**
