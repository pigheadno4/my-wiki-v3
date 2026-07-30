# Metronome Campaign 06 Quality Audit

Date: 2026-07-30

Scope: ten Campaign 06 source pages, all 1,641 raw lines, linked Metronome concepts, company page, provider index, log, and campaign receipts.

## Method

An independent GPT-5.6 Sol reviewer read every source and complete raw page. Each page received one core, one boundary, and one implementation-trap query. The reviewer also checked raw, company, concept, related-source, provider-index, and campaign-evidence links without editing the repository.

## Query results

| Job | Core | Boundary | Trap | Final |
| --- | --- | --- | --- | --- |
| `api-introduction` | Pass | Pass | Pass | 3 pass |
| `postman` | Pass | Pass | Pass | 3 pass |
| `api-quickstart` | Pass | Pass | Pass | 3 pass |
| `send-usage-events` | Pass | Pass | Pass | 3 pass |
| `provision-customer` | Pass | Pass | Initially partial: creation-time configuration recommendation omitted; repaired | 3 pass |
| `how-metronome-works` | Pass | Pass | Pass | 3 pass |
| `create-products-contracts` | Pass | Pass | Pass | 3 pass |
| `provision-contract` | Pass | Pass | Pass | 3 pass |
| `create-manage-rate-cards` | Pass | Pass | Pass | 3 pass |
| `create-a-billable-metric` | Pass | Pass | Pass | 3 pass |

Initial result: 29 pass, 1 partial, 0 fail.

Final result after the bounded source repair: 30 pass, 0 partial, 0 fail.

## Finding and repair

The customer-provisioning raw page recommends setting `customer_billing_provider_configurations` at customer creation. The promoted source explained the creation and later-add paths but omitted this preference. The source now states the recommendation while retaining the later `/setCustomerBillingProviderConfigurations` option.

No other unsupported inference, missing nested rule, contradiction collapse, broken link, or duplicate company/index entry was found.

## Link policy and result

- Every source-to-company, concept, related-source, and raw target resolves.
- Every Campaign 06 source appears exactly once in `wiki/companies/metronome.md` and `wiki/metronome-index.md`.
- Company and provider-index reverse catalogs are exhaustive.
- Concept citations remain fact-based: a concept cites a source when that source contributes a durable fact. A broader navigation link from a source does not force a low-value reciprocal citation.

This bounded policy avoids mechanically adding sixteen navigation-only backlinks and is the Campaign 06 interpretation of reverse-link reconciliation.

## Process evidence

- Ten jobs were approved.
- Nine jobs passed on attempt 1.
- `provision-customer` attempt 1 failed closed because a claimed quote was absent from raw; the failure is retained. A fresh Terra attempt 2 passed byte-for-byte quote validation and full Sol review.
- Raw hashes match the manifest.
- All ten promoted sources pass targeted wiki validation.
- Capsule validation reconciles 225 raw pages, 40 sources, and 185 pending pages.
- The full suite passed 548 tests before the final one-sentence content repair; targeted wiki and capsule validation passed again after that repair.

## Graduation decision

Campaign 06 content quality passes, but it does not graduate the workflow to reduced testing or parallel review. The declared zero-malformed-first-attempt criterion was not met. Keep the current conservative mode for the next bounded campaign, while retaining the proposed mature-mode design for later evidence.
