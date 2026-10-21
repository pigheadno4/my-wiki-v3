---
title: "Adyen Classic Platforms point of sale"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/platforms-for-pos"
raw_files:
  - "adyen/docs/classic-platforms/platforms-for-pos/2026-09-15.md"
tags: [adyen, classic-platforms, point-of-sale, stores, terminals, split-payments]
---

## Overview

This 2021-modified Classic Adyen for Platforms guide, captured 2026-09-15, describes in-person payments on behalf of Classic account holders: subscribe to store notifications, create a store, wait for its Active status, assign/board a terminal, then split POS payment funds between a holder account and the platform's liable account. It directs new implementations to a separate new-integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Before processing POS payments, have a Terminal API integration and work with Adyen Support to enable store creation for requested countries, currencies, MCCs and payment methods (raw lines 28–43, 109–113). Subscribe to `ACCOUNT_HOLDER_STORE_STATUS_CHANGE` and ensure the notification endpoint accepts/tests notifications; HMAC is optional in the shown subscription fields (raw lines 45–107). The prose calls this a Terminal API endpoint but its concrete request is Notification API v6 `/createNotificationConfiguration`; confirm the applicable endpoint rather than copying the prose label (raw lines 49–62).
- Add `accountHolderDetails.storeDetails` in Classic `/createAccountHolder` or `/updateAccountHolder`, with the store address, phone, merchant account, MCC, name and reference; a new business holder also needs `businessDetails.taxId`, and an existing holder needs it unless already present (raw lines 115–133). The sample response shows `Pending`; wait for a store-status-change notification with new status `Active` before POS processing (raw lines 218–253). Pending or an example Active payload is not actual activation for a particular store.
- A holder store needs at least one assigned terminal. The guide routes selection/order, Customer Area or Terminal Management API assignment, terminal configuration, shipping to the physical store and boarding (raw lines 275–294). Those setup steps do not themselves establish payment acceptance.
- Split a POS payment through store-level automatic split configuration or per-transaction instructions in the Terminal API payment request or at capture; API instructions override the automatic split for the transaction (raw lines 296–307). The Terminal API route uses `SaleToAcquirerData` split API v1 with total and item counts matching transaction amount/items; `MarketPlace`/`VAT` go to the specified account, while `Commission`/`PaymentFee` go to the platform liable account, and `MarketPlace` needs a split reference (raw lines 335–353). The example of a successful terminal response does not prove a booked split or payout (raw lines 388–405).
- If final split amounts are unknown at payment time, the guide calls for manual capture and a later `/payments/{paymentPspReference}/captures` request; it also names tipping and partial authorizations. Enabling manual POS capture applies to **all** POS account holders (raw lines 407–417). The capture response distinguishes authorization and capture PSP references and `status: received`; use the CAPTURE webhook for outcome (raw lines 872–880). The capture example is USD 80 but its NodeJS JavaScript request uses EUR; do not treat that sample currency as an authoritative template (raw lines 432–445, 640–660).

## Detail locators

- Classic scope, prerequisites and Support enablement: raw lines 19–43. Store-notification subscription, API example and test: raw lines 45–107. Store payload, business tax ID, Pending response and Active webhook gate: raw lines 109–273. Terminal assignment/boarding: raw lines 275–294.
- Automatic versus API split override: raw lines 296–307. Terminal API split fields and account destinations: raw lines 311–353. Terminal payment result: raw lines 388–405. Manual capture scope, split request and sample-language/version details: raw lines 407–870. Received response and CAPTURE webhook: raw lines 872–880.

## Related

- [[adyen-classic-platforms]] — older account-holder/account model.
- [[source-adyen-docs-classic-platforms-processing-payments]] — Classic split-payment accounting and capture context.
- [[source-adyen-docs-classic-platforms-configure-notifications]] — Classic notification configuration.
- [[adyen-platforms]] — separate newer balance-platform model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/platforms-for-pos/2026-09-15|Classic Platforms for POS, captured 2026-09-15]]
