# Metronome Campaign 02 Quality Audit

Date: 2026-07-29

Scope: five Campaign 02 source pages, their complete raw pages, linked Metronome concepts, company page, provider index, and log.

## Method

An independent reviewer read all five canonical source pages and all 1,442 lines of their raw pages. Each page was tested with one core, one boundary, and one contradiction or trap question. Hard failures were unsupported facts, wrong implementation fields or conditions, wrong provider attribution, unpreserved contradictions, broken raw routing, or cross-page disagreement.

The reviewer was read-only. Sol independently adjudicated every finding and made the approved shared-file changes.

## Question results

| # | Test | Initial result | Final result |
| ---: | --- | --- | --- |
| 1 | High-volume batch size and throughput figures | Partial: the equivalent 6.6-million-per-minute figure was omitted. | Pass: added alongside 110,000 events per second and the separate 5,000-events-per-second default limit. |
| 2 | High-volume producer controls and recovery | Pass | Pass |
| 3 | Infrastructure capacity versus default account limit | Pass | Pass |
| 4 | Stripe Dashboard app capabilities | Pass | Pass |
| 5 | App versus native Stripe invoice delivery | Pass | Pass |
| 6 | Linked-customer visibility and automatic Metronome customer creation | Pass | Pass |
| 7 | Enterprise access, invoice, rollover, discount, and support-charge terms | Pass | Pass |
| 8 | Contract edit versus transition | Pass | Pass |
| 9 | `product`/`product_id` and $300,000 commit/scheduled-charge inconsistencies | Pass | Pass |
| 10 | Customer, contract, and multiple-Stripe-account routing | Fail: contract-level `billing_provider_configuration_id` and its lookup route were omitted. | Pass: source and both integration concepts now distinguish it from customer-level `delivery_method_id`. |
| 11 | Non-retroactive activation and one-hour/72-hour payment timing | Pass | Pass |
| 12 | Payment-gated mapping and Stripe invoice representation limits | Pass | Pass |
| 13 | Customer-commit endpoint and required fields | Pass | Pass |
| 14 | Prepaid/postpaid conditions, priority tie, scope, and targeting | Pass | Pass |
| 15 | Unlisted `409` and recurring-schedule/postpaid ambiguity | Pass | Pass |

Initial result: 13 pass, 1 partial, 1 fail.

Final result after bounded repairs: 15 pass, 0 partial, 0 fail.

## Findings and adjudication

### Fixed — contract-level multi-account routing

The raw Stripe invoice guide distinguishes two selectors:

- Customer configuration uses `delivery_method_id` when multiple Stripe accounts are connected.
- Contract creation uses `billing_provider_configuration_id`, obtained from `/getCustomerBillingProviderConfigurations`, to select one of that customer's configurations.

The initial source and concepts retained the first selector but only summarized the second as independent contract routing. This could block a correct implementation, so it was treated as a hard failure and repaired in:

- `wiki/sources/metronome/source-metronome-integrations-invoice-integrations-stripe.md`
- `wiki/concepts/metronome/metronome-invoicing.md`
- `wiki/concepts/metronome/metronome-integrations.md`

### Fixed — equivalent throughput unit

The high-volume source retained 110,000 events per second but omitted the raw page's equivalent 6.6 million events per minute. This was a soft completeness issue and is now restored.

### Rejected — Stripe ownership attribution

The reviewer treated `wiki/metronome-index.md` calling Stripe the owner as inconsistent with maintaining Metronome as an independent provider capsule. These statements concern different things: Stripe completed its acquisition of Metronome in January 2026, while “independent provider capsule” describes this wiki's storage and ingestion boundary. Stripe's official acquisition announcement confirms the ownership fact:

- https://stripe.com/en-nl/newsroom/news/stripe-completes-metronome-acquisition

No ownership correction was warranted. Collection of that announcement as a separate raw source remains outside this documentation-only campaign.

### Deferred — general index validator boundary

`validate_wiki.py` expects page frontmatter, while the root and PSP index files intentionally use an H1-first catalog format. This is a pre-existing repository-wide convention, not a Campaign 02 source-quality defect. The Metronome provider-aware validator remains the structural gate for capsule index reconciliation. No validator or index-format redesign was introduced during this audit.

## Traceability and structural checks

- All five `canonical_url` values match their raw-page source URLs after the intentional removal of the raw `.md` suffix.
- All five `raw_files` values exist.
- All five path-qualified `## Raw Sources` links resolve to their intended snapshots.
- Source, company, concept, index, and log coverage reconciles to 225 raw pages, 15 source summaries, and 210 pages pending ingest.
- The two raw-document inconsistencies in the enterprise guide and the API response/schema ambiguities in create-commit remain explicit warnings.

## Acceptance

Campaign 02 passes this quality audit only after the two bounded repairs above. No new coordinator machinery, retry behavior, schema, or parallel-ingest abstraction was introduced.
