# Metronome Campaign 14 Pilot Verdict

## Verdict

`fail_no_reviewer_hypothesis`

Do not use a Sol-medium worker plus mechanical coordinator checks as the only
quality gate for routine Metronome ingestion. The five-page calibration produced
zero qualifying pages, so the manifest's promotion gate failed and no canonical
wiki content is authorized.

This is a model-and-review-policy result, not a finding that the layered ingest
architecture is unsuitable. The raw corpus, isolated candidates, receipts,
structured suggestions, coordinator ownership, and deterministic validation all
behaved as intended.

## Calibration results

| Job | Worker handoff | Independent full-source result | Material finding |
| --- | --- | --- | --- |
| `hybrid-business-models` | valid on attempt 1 | changes requested | missed the `PAYMENT_INTENT` versus existing `INVOICE` Stripe Tax contradiction and related reciprocal updates |
| `asc-606-revenue-recognition` | valid on attempt 1 | changes requested | missed an invoice-timing contradiction, the generic ASC 606 concept audit, and several fact-bearing reciprocal updates |
| `netsuite-integration` | valid on attempt 1 | changes requested | overgeneralized availability and timing, inferred optional-metadata sync behavior, and omitted durable concept updates |
| `list-invoice-breakdowns` | attempt 1 failed quote-substring validation; attempt 2 passed | changes requested | overstated the status filter, missed a zero-filter ambiguity and 404 contract, blurred inherited-field optionality, and missed cross-source finalization boundaries |
| `discounting-on-commits` | valid on attempt 1 | changes requested | missed the conflict between commit-specific precedence and the legacy amendment precedence rule |

The pass criterion was zero material factual inversion, unsupported durable claim,
important omission, or missed contradiction across all five pages. The observed
result was `0 passed / 5 evaluated`.

## Mechanical observations

- Deterministic validation correctly rejected three non-exact quotes in the first
  schema-heavy API submission.
- Several post-verdict retry candidates also violated the existing suggestion
  contract by proposing an unsupported `update_kind` or a source-page
  `target_path`. These retries are retained as evidence but do not change the
  first-attempt verdict.
- The NetSuite retry repaired the candidate's first semantic findings, but its
  shared suggestions still lacked adequate quote coverage. Better candidate prose
  therefore did not remove the need for independent semantic review.

## Production decision

- Keep independent strong-model review for Metronome pages whose source candidate
  or shared suggestions carry cross-source semantics, contradictions, accounting
  boundaries, integration state, or API schema interpretation.
- Do not promote Campaign 14 candidates or apply their shared suggestions.
- Do not expand this no-review policy to Stripe, Adyen, PayPal, Braintree, or
  another PSP from this result.
- Stop retrying Campaign 14. Its remaining `queued` and `failed` job states are
  preserved as truthful negative-calibration evidence, matching the earlier
  Campaign 13 stop pattern rather than forcing artificial approvals or terminal
  rejections.

## Small next step

If speed optimization continues, test a narrower policy rather than another broad
model swap: keep deterministic validation for all pages, require independent review
for shared semantic updates and contradiction-bearing pages, and separately pilot
review omission only for truly isolated source pages that make no shared concept
changes. That proposal requires a new exact manifest and user approval.
