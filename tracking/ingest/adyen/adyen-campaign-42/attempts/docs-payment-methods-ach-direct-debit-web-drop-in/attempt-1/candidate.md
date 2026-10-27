---
title: "Adyen ACH Direct Debit Web Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/web-drop-in/2026-09-15.md"
tags: [adyen, ach, direct-debit, web, drop-in, sessions, advanced-flow]
---

## Overview

This captured Adyen guide adds ACH Direct Debit to an existing Web Drop-in integration through Sessions or Advanced server-side flow. It covers method-specific setup, optional Drop-in configuration, asynchronous bank outcome and test data. It does not establish current merchant eligibility, account validation, customer authorization or cleared funds. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-ach-direct-debit]] for ACH scheme, consumer-account validation, SEC code, mandate, refund and chargeback conditions.

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, ACH added in Customer Area and a subscription to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` for outdated bank details. Ordinary `/sessions` needs no extra ACH-specific request parameters. Importing `Ach` individually is optional tree shaking, not a required setup step.
- Advanced requires an existing Web Drop-in Advanced integration, ACH Customer Area setup and the same Notice of Change subscription; its ordinary `/payments` adds no ACH-specific parameters. Its requirements link contains an unresolved URL-encoded template expression for the platform, so use the guide's explicit Web/Drop-in scope rather than treating that generated URL as a verified base route. Neither flow's no-extra-parameters statement removes the ACH overview's separately stated account-validation, SEC-code or signed-mandate conditions.
- Both flows list optional Drop-in configuration: `enableStoreDetails` (Web v5.24.0 or later) shows a save-details checkbox when true and defaults false; `hasHolderName` can hide the holder-name field if the merchant supplies data and defaults true; `holderNameRequired` can make the field optional and defaults true. Showing a save-details checkbox does not itself establish a created recurring token or shopper authorization. The example is a bash-fenced `var achConfiguration = Ach.Configuration()` snippet, not a complete verified Web Drop-in wiring example.
- Receiving a payment request can precede bank authorization by up to five business days. The guide points to the Settlement details report if the bank authorizes and a `CHARGEBACK` webhook if it does not; do not treat an immediate response as settled funds. The ACH overview also states the network has no real-time authorizations and chargebacks cannot be defended.
- For an API or Customer Area ACH refund, the guide requires the **Merchant allow bank-refund** role for the relevant actor. The method overview additionally says refunds are available after settlement and Adyen delays them for three days after settlement; this page does not provide a refund execution flow.
- The guide permits test account/routing formats and uses an `ownerName` beginning `chargeback:` plus an ACH return reason such as `R01` to simulate chargebacks. It links, but does not explain, account validation with giact, tokenization and ACH chargeback/retry rules; these links do not prove account validation or general retry permission.

## Detail locators

- Sessions prerequisites, refund role, v68+, Notice of Change subscription and Customer Area setup: pinned raw lines 25–38. No added `/sessions` fields and optional `Ach` import: lines 40–56.
- Optional Web v5.24.0+ save-details checkbox and holder-name controls, with the bash-fenced configuration sample: pinned raw lines 58–75 and 131–148.
- Advanced prerequisites (including templated base URL), conditional refund role and notice, optional import, no added `/payments` fields: pinned raw lines 105–154.
- Five-business-day bank outcome and settlement/chargeback route: pinned raw lines 77–83 and 156–162. Test account data and `chargeback:R01` simulation: lines 85–103 and 164–182.
- Consumer validation, SEC/mandate, US business entity, refunds and returns are in [[source-adyen-docs-payment-methods-ach-direct-debit]]; this Drop-in add-on does not independently specify those lifecycle rules.

## Related

- [[adyen-online-payments]] — main integration concept
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH method-level eligibility, validation, authorization and funds-risk authority

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/web-drop-in/2026-09-15|ACH Direct Debit Web Drop-in, 2026-09-15]]
