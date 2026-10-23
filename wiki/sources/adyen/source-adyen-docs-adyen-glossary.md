---
title: "Adyen Docs: Payments glossary"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/adyen-glossary"
raw_files:
  - "adyen/docs/adyen-glossary/2026-09-15.md"
tags: [adyen, glossary, payments, terminology]
---

## Overview

This [[adyen|Adyen]] glossary defines general payment-industry and Adyen-specific terms spanning card participants, authentication, payment lifecycle, account/platform resources, online and POS channels, and reporting. Its metadata says last modified 2025-07-24; the pinned snapshot was fetched 2026-09-15. It is a terminology aid under [[adyen-payments]], not a consolidated implementation contract or evidence that any merchant has a feature enabled.

## Key takeaways

- The glossary distinguishes **authentication**, which checks the person making a transaction, from **authorization**, which checks and reserves funds, then describes capture, cancellation of an uncaptured authorization, refund after capture, and asynchronous webhook results for modifications. Its heading `Capture (or Clearing and settlement)` uses broad shorthand; product-specific lifecycle and payout sources remain authoritative for the actual capture, clearing, settlement, and bank-receipt stages. The Authorization definition also parenthetically calls Visa/Mastercard issuers, while this same glossary separately defines them as card networks; do not propagate that parenthetical as a participant rule.
- It defines an Adyen account's company and merchant levels and says test precedes live activation. The separate **Capability** entry is for an account holder on a Balance Platform, while **Legal entity** is a Balance Platform API resource used for verification. These terms do not by themselves confer merchant-account access, platform capability, legal-entity approval, live processing, or payout eligibility.
- Merchant, acquirer, issuer, gateway, processor, PSP, marketplace, payfac, platform, and merchant of record have separate entries. The marketplace/payfac descriptions sketch roles and money flows; they do not determine the seller, liable entity, split configuration, settlement route, or payout destination in a specific implementation.
- POS terminology includes legacy Adyen POS Application/Library entries marked as replaced by Terminal API, plus online/offline processing, terminal, tender and store. Treat those as glossary descriptions with historical and configuration scope, not as current terminal-model or offline-approval guarantees.
- Security and recurring terms include PAN/BIN, CVC as sensitive authentication data, 3DS/ACS, SCA, tokenization and stored-card payments. The BIN entry explicitly says BIN alone cannot determine card type or issuing country/region. The glossary's PCI, regulatory, regional-acquiring, and recurring-storage statements are dated descriptions; they are not current compliance advice or a substitute for route-specific requirements.

## Detail locators

- **Accounts, participant and authentication vocabulary** — raw lines 19–109.
- **BIN, payment lifecycle, capability and card terms** — raw lines 111–215.
- **Disputes, platform KYC, money/currency and channel definitions** — raw lines 217–369.
- **Merchant/MoR, offline/POS and payment participant definitions** — raw lines 371–540.
- **References, recurring/refund, security and transaction terms** — raw lines 541–696.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-payments]]
- Account structure: [[adyen-account-structure]]
- Platforms: [[adyen-platforms]]
- 3D Secure: [[adyen-3d-secure]]
- Payment terminals: [[adyen-payment-terminals]]

## Raw Sources

- [[raw/adyen/docs/adyen-glossary/2026-09-15|Adyen Docs — glossary (2026-09-15)]]
