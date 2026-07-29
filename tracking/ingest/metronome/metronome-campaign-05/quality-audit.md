# Metronome Campaign 05 Quality Audit

Date: 2026-07-30

Scope: five Campaign 05 source pages, their complete raw pages, linked Metronome concepts, company page, provider index, and log.

## Method

An independent GPT-5.6 Sol reviewer read all five canonical source pages and all 1,790 lines of their raw pages. Each page was tested with one core, one boundary, and one contradiction, ambiguity, or implementation-trap question. The reviewer also checked all 41 source-page wikilink occurrences, reciprocal links, provider routing, campaign model routing, and coverage arithmetic.

The reviewer was read-only. Sol independently verified each non-pass finding against the raw and source before applying bounded content repairs.

## Question results

| # | Test | Initial result | Final result |
| ---: | --- | --- | --- |
| 1 | Idempotency mechanism selection, conflicts, and lifetimes | Pass | Pass |
| 2 | `uniqueness_key` release and resource boundary | Partial: Alerts-only release was omitted. | Pass: documented that no release path is stated for the other keyed resources. |
| 3 | Cached HTTP 500 versus different-key retry guidance | Pass | Pass |
| 4 | Status codes and client remediation | Pass | Pass |
| 5 | `429` scopes and undocumented numeric/backoff details | Pass | Pass |
| 6 | 4XX-only error envelope and 5XX recovery boundary | Pass | Pass |
| 7 | Streaming aggregation behavior and availability surfaces | Partial: UI, API, Plans, and Contracts availability was omitted. | Pass: restored all four surfaces. |
| 8 | Group-key prerequisites, immutability, and cardinality warning | Pass | Pass |
| 9 | Forward-only metric matching versus assisted reflow | Pass | Pass |
| 10 | Customer endpoint, authentication, required field, success status, and ID | Partial: bearer authentication and HTTP `200` were omitted. | Pass: restored both without changing the preserved ID ambiguity. |
| 11 | Customer alias, name, and provider-configuration boundaries | Pass | Pass |
| 12 | `customer_id` versus `data.id` and unidentified 409 key | Pass | Pass |
| 13 | Legacy amendment lifecycle, minimum input, and response | Pass | Pass |
| 14 | Suppressing invoices for point-in-time commit schedules | Partial: `do_not_invoice` was omitted. | Pass: documented its scope, effect, and false default. |
| 15 | Nested requirements for a `TIERED` override | Fail: `tiers: [{}]` appeared sufficient because the required tier `multiplier` was omitted. | Pass: documented that every tier requires `multiplier`; `size` remains optional. |

Initial result: 10 pass, 4 partial, 1 fail.

Final result after bounded repairs: 15 pass, 0 partial, 0 fail.

## Findings and adjudication

### Fixed — required multiplier on every tiered-override tier

The amendment source required a positive priority and at least one tier but omitted the nested schema rule that every `OverrideTierInput` requires `multiplier`. This could produce an invalid mutation payload, so it was the audit's only hard failure and was repaired in `source-metronome-api-reference-contracts-amend-a-contract.md`.

### Fixed — four source completeness gaps

- The idempotency source now states that `uniqueness_key` retention lasts until release but release is available only for Alerts; the page documents no release path for contracts, customer-level commits or credits, or future contract edits.
- The billable-metrics source now states that all four streaming aggregations are available in the UI, API, Plans, and Contracts.
- The customer source now preserves the endpoint's bearer authentication and exact HTTP `200` success response.
- The amendment source now documents `do_not_invoice` for commit invoice schedules, including its false default.

### Fixed — usage-based-billing concept traceability

The billable-metrics source linked `metronome-usage-based-billing`, but that concept did not link back and retained open questions that the source partly answered. The concept now summarizes the metering-to-product/rate-card/contract chain, narrows the remaining questions, and links the source.

### Preserved — raw and cross-page ambiguities

No correction was made where the sources already preserved an upstream uncertainty: cached-error retry guidance, assisted reflow limits, `customer_id` versus `data.id`, request-body requiredness, the unidentified customer 409 key, legacy amendment mutation and invoice-state semantics, response-ID meaning, credit selector wording, and cached-error behavior for a multi-object amendment.

## Traceability and structural checks

- All 41 audited wikilink occurrences resolve; no audited source repeats a wikilink.
- All five raw links route to the exact immutable snapshots reviewed.
- The Metronome company page links all five sources, and appropriate source, concept, and related-source reverse links are present after the usage-based-billing repair.
- Each Campaign 05 source appears exactly once in `wiki/metronome-index.md`.
- Counts reconcile to 225 raw pages, 30 source summaries, and 195 pages pending.
- Campaign routing reconciles to two standard Terra jobs, three strong Sol jobs, and 1,790 raw lines.

## Acceptance and next scale

Campaign 05 passes after the six bounded content and traceability repairs above. The audit introduced no scheduler, result schema, retry, or validator change.

For the next campaign, retain the current rolling ceiling of three workers and serial full-raw strong-model review. A ten-page campaign may be proposed, but review strength should not be relaxed: the only material failure occurred in the 1,133-line nested OpenAPI page despite strong-tier routing.
