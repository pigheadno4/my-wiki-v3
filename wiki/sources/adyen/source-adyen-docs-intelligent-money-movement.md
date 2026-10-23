---
title: "Adyen Intelligent Money Movement overview"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/intelligent-money-movement"
raw_files:
  - "adyen/docs/intelligent-money-movement/2026-09-15.md"
tags: [adyen, intelligent-money-movement, enterprise-accounts, payouts, issuing]
---

## Overview

This 2026-09-15-captured Intelligent Money Movement (IMM) page describes an **enterprise cash-management** solution combining Adyen payment processing with balance-platform enterprise financial features. It presents a high-level funds-flow sequence and links to a selectable integration overview; it does not specify a merchant's approved architecture, enabled products, API procedures, legal ownership or completed transfer. [[adyen]] [[adyen-financial-products]]

## Key takeaways

- The overview lists incoming funds from processed payments, third-party bank transfers or a verified bank account; enterprise accounts for storing/managing funds; outbound payouts to third-party bank accounts/cards or a verified bank account; and Adyen-issued debit cards for payments. These are described capabilities, not proof that all routes are available to a specific enterprise or region. See raw lines 19-26.
- Its illustrated processing path has online/in-person purchases processed, purchase funds settled in the merchant account, then transferred from merchant account to a balance account in the balance platform. **After** funds settle in the balance account, the page presents sending funds from the enterprise account to third-party bank accounts/cards or paying counterparty merchants with Adyen-issued cards. Adding funds from verified or third-party bank accounts is a separate listed possibility. See raw lines 28-45. Do not collapse merchant-account settlement, balance-account settlement, a payout instruction and beneficiary receipt into one event.
- The integration-overview section offers a selection of online payments, in-person payments, enterprise-account fund management, third-party payouts and expense-card issuance, then links to a generated overview. This page does not contain the generated plan or define which combination is eligible, configured or required for a particular business. See raw lines 49-63.
- This enterprise IMM overview is distinct from the existing [[adyen-financial-products]] concept's **platform-facing** product-family description for platform users. This page itself supplies no account/entity-role mapping, KYC/consent/PCI rules, API version, region/currency eligibility, fee, timing, booking webhook or failure/retry behavior; follow the relevant product guides before making those claims.

## Detail locators

- Opening product identity and capability list, raw lines 15-26.
- `## Flow of funds`, raw lines 28-47: merchant-account to balance-account sequence, third-party outbound options, issued-card spending and optional bank funding; linked diagram is not an API specification.
- `## Integration overview`, raw lines 49-63: selectable offerings and link to a separate generated overview.

## Related

- [[adyen-financial-products]] — related financial-product umbrella, with platform-user scope distinct from this enterprise overview.
- [[adyen-payouts]] — separate payout service and legacy API routes.
- [[adyen-business-accounts]] — distinct platform-user account product.
- [[adyen-payments]] — payments channel overview.

## Raw Sources

- [[raw/adyen/docs/intelligent-money-movement/2026-09-15|Adyen Intelligent Money Movement overview, captured 2026-09-15]]
