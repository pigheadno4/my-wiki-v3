# Metronome Campaign 24 Retrospective

## Outcome

- Final content quality: eight of eight pages approved; the fixed three-page query audit passed 9/9 with no expansion.
- First-pass efficiency: four of eight pages approved on attempt 1; four required one full semantic retry.
- Retry shape: twelve worker attempts and twelve independent full reviews; zero targeted reviews, failed attempts, or rejected jobs.
- Total elapsed time through promotion, close validation, and final state write: 3,048 seconds (50 minutes 48 seconds).
- Coordinator repairs: 1.

## What worked

The Minimum Sufficient Source contract remained useful across API read, list/schema, mutation, integration, concept/guide, notification, and subscription-seat pages. All final sources are concise routers with exact raw backlinks, and the fixed audit passed without expansion. Dynamic slots continued useful work as soon as an agent finished instead of waiting for a batch barrier, while the coordinator promoted approved pages serially and kept canonical writes conflict-free.

Four pages passed on the first attempt: contract rate schedule, invoice issue date, GCP, and system notifications. The other four needed one substantive correction each, and no page reached attempt 3.

## Material review findings

- Credit-ledger listing initially omitted the distinction between chronological entries and ledger-level sort and missed a positive-deduction amount conflict with the shown balance decrease.
- Audit-log retrieval initially omitted the narrative-versus-OpenAPI placement conflict for `next_page`.
- API Quickstart initially treated fixed March 9 timestamps as runnable despite the July 13 snapshot and documented 34-day acceptance window.
- Manage Seats initially omitted API-wide POST idempotency, overstated nested `seat_group_key` requiredness, and did not directly ground the malformed example.

These were query-relevant facts or failure boundaries, so full semantic retries were appropriate. They also show why this campaign does not justify removing independent review from all pages yet.

## Bounded coordinator work

One coordinator repair narrowed a contract-rate concept statement from generic selector OR semantics to OR semantics across selector objects. A temporary scheduler assignment entry was corrected before dispatch after the coordinator supplied a running worker identity where a new-order identity was expected; no content or receipt was produced under the wrong identity. One reviewer could not write its `/private/tmp` result because of a local approval check, so the coordinator persisted the reviewer's exact eight-key JSON without altering the verdict or reasoning.

No new registry, state schema, performance monitor, worktree layer, or validator was added.

## Comparison with Campaign 23

- Campaign 23: 5/5 first-pass approvals, 5 attempts and 5 reviews, 1,603 seconds through close.
- Campaign 24: 4/8 first-pass approvals, 12 attempts and 12 reviews, 3,048 seconds through close.

Campaign 24 processed a larger and more varied set, but the four full retry cycles kept throughput close to the earlier per-page cost. The main remaining cost is semantic rereading, not coordinator promotion or mechanical validation.

## Recommendation

Keep Campaign 24 as the larger Metronome confirmation result: Minimum Sufficient Source quality passed, but independent review still found four material defects. For the next separately approved experiment, change only one variable—sample reviewer coverage by page risk while retaining full review for mutation, financial-schema, contradiction-prone, and cross-system pages. Do not roll reviewer removal across Stripe, Adyen, PayPal, or Braintree from this result alone.
