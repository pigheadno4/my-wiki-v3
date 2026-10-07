---
title: "Braintree Level 2 and 3 Processing Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/level-2-and-3-processing/overview"
raw_files:
  - "braintree/docs/reference/general/level-2-and-3-processing/overview-2026-09-16.md"
tags: [braintree, credit-cards, level-2, level-3, interchange]
---

## Overview

This collected [[braintree]] general-reference overview explains the purpose and high-level qualification conditions for supplying Level 2 and Level 3 data on credit-card sale transactions; see [[braintree-payment-platform]] for the provider-level context. It is an unversioned webpage snapshot with body metadata updated 2025-10-14 and raw fetched 2026-09-16, scoped to certain Visa and Mastercard corporate or purchasing cards and the stated regional merchant-account identifiers; it identifies no exact SDK/API version, processor, environment, eligible-card table or network-rule effective date, and is not current network policy, merchant/card/MCC eligibility, transaction acceptance, interchange-result, settlement or funding proof.

## Key takeaways

- The page says advanced processing levels such as Level 2 and Level 3 can help a merchant qualify for lower interchange rates on transactions made with certain Visa and Mastercard corporate and purchasing cards. The wording is conditional, not a promised rate reduction.
- Level 2 qualification requires specific data in credit-card transactions. Level 3 qualification requires specific line-item data and additional information when creating sale transactions. The overview routes the complete field lists to the separate Required Fields page rather than enumerating them.
- For US Visa Level 3 data, the snapshot says Visa mandated CEDP quality checks. It also says Braintree passes the supplied details to card networks, which report them to business cardholders for spending monitoring.
- The page states availability for US merchants with a Tax ID and EU or UK merchants with a VAT ID linked to their Braintree accounts. It directs merchants to confirm that identifier and whether their Merchant Category Code qualifies for reduced interchange, and recommends sending Level 2/3 data only when the MCC qualifies.

## Detail locators

- Conditional lower-interchange purpose and qualified Visa/Mastercard corporate or purchasing card scope: `# Overview`, line 16.
- Level 2 transaction-data requirement, Level 3 sale-time line-item/additional-data requirement, US Visa CEDP statement and network-reporting purpose: `# Overview`, line 18.
- Guide purpose and complete-field-list route: paragraph before `## Merchant requirements`, line 20.
- US Tax ID, EU/UK VAT ID, linked-account, MCC-confirmation and qualified-use conditions: `## Merchant requirements`, line 23.
- Bank-specific availability and business-use-case support route: `## Merchant requirements`, line 25.

## Related raw API references

The captured overview routes exact fields to the Level 2/3 Required Fields page and account questions to Braintree support. Those targets are navigation only for this entry and are not imported as behavioral evidence.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Detailed Node.js route: [[source-braintree-docs-reference-general-level-2-and-3-processing-required-fields-node]]
- In-Person comparison route: [[source-braintree-in-person-guides-making-a-transaction-level-2-and-level-3-data-processing]]
- Processor-specific comparison route: [[source-braintree-articles-wells-ic-transactions-level-2-and-3-processing]]

## Raw Sources

- [[raw/braintree/docs/reference/general/level-2-and-3-processing/overview-2026-09-16|Braintree Level 2 and 3 Processing overview]] - complete collected overview covering purpose, transaction-data distinction, network reporting and merchant requirements
