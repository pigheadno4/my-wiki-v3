# Metronome Campaign 22 Retrospective

## Outcome

- Final content quality: five of five pages approved; the fixed three-page query audit passed 9/9 with no expansion.
- First-pass efficiency: zero of five pages approved on attempt 1, below the target of at least four.
- Retry shape: eleven worker attempts and eleven reviews — ten full and one targeted. Five full semantic retry cycles were required, above the target of no more than one.
- Final attempts: `get-a-product` 2, `list-products` 3, `archive-a-customer` 2, `non-monotonically-increasing-metrics` 2, and `sfdc-integration` 2.
- Coordinator content repairs: zero.
- Timing: the campaign crossed a user-requested pause, and the current ledger has no pause-duration field. Wall-clock completion time is therefore not a valid throughput measurement; the 35-minute desirability target cannot be honestly evaluated.

## What archetype v2 improved

The three checks—claim-to-evidence closure, authority separation, and concept-impact sweep—gave workers and reviewers a consistent vocabulary for identifying why a candidate was incomplete. The final pages distinguish endpoint facts from API-wide pagination or idempotency rules, preserve source conflicts and unknowns, route material facts into relevant concepts, and retain exact raw deep-dive paths. The independent close audit confirmed 5/5 mechanical integrity, 57/57 approved concept blocks exactly once, and 9/9 sampled factual, boundary, and raw-navigation queries.

Compared with Campaign 21, total attempts fell from thirteen to eleven and coordinator content repairs remained zero. This is a small operational improvement, not evidence that the playbook improved first-pass quality or campaign duration.

## Why the throughput gate failed

Every initial candidate required review correction. The recurring defects were not formatting mistakes; they were semantic coverage and ownership issues: incomplete composite-product and NetSuite surfaces, missing related concepts, cross-source idempotency facts presented as assigned-page evidence, OpenAPI nullability precision, incomplete response-map grounding, and integration fields whose implications crossed several concepts.

The concept-impact sweep was especially expensive when interpreted as an exhaustive per-page obligation. It improved the final graph, but it also turned secondary reciprocal-concept omissions into full-page retry blockers. `list-products` reached attempt 3 because its second review still found nullability, evidence-span, and authority-separation defects. Independent review therefore remained the mechanism that produced final quality; archetype self-checks did not replace it.

## Decision

Do not promote archetype v2 into Metronome production rules as a speed optimization, weaken independent review, or roll it out across Stripe, Adyen, PayPal, or Braintree. Keep it as campaign-local evidence and an optional reviewer checklist.

If another bounded experiment is run, make only one small change: treat source-page factual correctness, primary authority separation, and exact raw navigation as blocking; let the coordinator group clearly secondary reciprocal concept additions from approved worker suggestions instead of forcing another full source retry solely for a secondary concept omission. Test that rule on no more than five pages before considering adoption. Do not add a registry, new schema, model router, or performance-monitoring system.

One existing coordinator limitation was observed: reviewer orders are recorded in campaign state and command output but are not persisted over the attempt's worker `input.json`. This caused an avoidable reviewer handshake but did not affect content integrity. Record it as known operational debt; it does not justify expanding Campaign 22's scope.
