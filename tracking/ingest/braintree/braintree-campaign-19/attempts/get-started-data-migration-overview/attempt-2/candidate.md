---
title: "Braintree Data Migration Overview"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/data-migration/overview"
raw_files:
  - "braintree/articles/get-started/data-migration/overview-2026-09-16.md"
tags: [braintree, data-migration, vault, payment-methods]
---

## Overview

This collected Braintree overview identifies the two data-portability directions: importing customer and credit-card records into a new Braintree gateway and exporting them when leaving Braintree. It is an orientation and routing page, not the dedicated import or export procedure; it also records the collected page's fee, timing, non-migratable-data, ACH and wallet-export boundaries.

## Key takeaways

- Braintree says it does not charge fees for data migrations. The page does not establish whether another processor or service provider charges fees.
- Migration timing varies with integration complexity and the completeness of intake materials. Braintree says its team confirms an estimated timeline only after all required information is submitted.
- Braintree says it can import and export customer and credit-card records, but cannot migrate subscription or transaction information. For an import, the page says plans must be recreated in the Control Panel and subscriptions created after migration; for an export, it points to separate report and API routes. Those links are navigation, not evidence here for the linked operations.
- A stored ACH payment method rests on a customer agreement to be charged only by the processor with which it was stored, so Braintree requires merchants to agree to additional legal terms. The specific addendum and privacy-policy obligations remain at the raw locator below.
- Secure tokens associated with Apple Pay and Google Pay network transactions are not transferable between providers; the page therefore excludes Apple Pay and Google Pay payment methods from Braintree exports.

> [!warning] Collected migration boundary
> This overview does not document the dedicated import or export process and does not establish current migration support, eligibility, processor participation, completion timing or successful reuse of migrated data. Its 2026-09-16 collection date is not current-support proof.

## Detail locators

- Customer and credit-card portability in both migration directions: `# Overview`, line 16.
- No Braintree migration fee: `## Fees`, line 21.
- Complexity, intake-completeness and estimated-timeline qualification: `## Time frame`, line 26.
- Customer/card scope, subscription and transaction exclusion, plus linked post-migration or export routes: `## Data migration restrictions`, line 31.
- ACH processor agreement and merchant legal-term requirement: `## Data migration restrictions`, lines 33-37.
- Apple Pay and Google Pay token non-transferability and export exclusion: `## Data migration restrictions`, line 39.
- Dedicated import and export guides plus contact route: `## Getting started`, lines 42-46.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-data-migration]]
- Dedicated migration routes (navigation only for this source): [[source-braintree-get-started-data-migration-imports]] and [[source-braintree-get-started-data-migration-exports]]

## Raw Sources

- [[raw/braintree/articles/get-started/data-migration/overview-2026-09-16|Braintree Data Migration Overview article]] - complete collected page covering migration directions, fees, timeline qualification, data restrictions, ACH terms and wallet export exclusions
