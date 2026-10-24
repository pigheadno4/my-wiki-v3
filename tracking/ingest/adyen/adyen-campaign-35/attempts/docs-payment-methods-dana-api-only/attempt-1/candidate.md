---
title: "DANA for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/api-only"
raw_files:
  - "adyen/docs/payment-methods/dana/api-only/2026-09-15.md"
tags: [adyen, dana, api-only, wallets, indonesia]
---

## Overview

Adyen's 2026-09-15 DANA API-only page adds DANA to an existing Web API-only Advanced-flow integration. It covers method discovery, a merchant-built payment form, redirect handling, a separate recurring-token route, and test/live setup. It is a historical snapshot, not proof of current availability, merchant eligibility, or payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Base flow:** Requires the existing API-only integration, handling `action.type: redirect`, and adding DANA in Customer Area. The shopper chooses DANA; the merchant-built form need not collect extra shopper information for this method. The existing integration handles the redirect. The page says no extra ordinary `/payments` parameters are needed, while its “how it works” step mentions additional item information *if applicable* without specifying a field here; do not infer an unconditional item requirement. [Raw lines 23–42, 87–89]
- **Discovery conflict:** The `/paymentMethods` parameter table says `countryCode: IN` and `amount.currency: INR`, but the immediately following example request uses `countryCode: ID`, `currency: IDR`, and locale `id-ID`. The page also gives a **300 IDR** minimum below which DANA does not appear. Preserve this table/example mismatch; this page alone cannot establish the correct country/currency discovery values or eligibility for a merchant. The example uses Checkout v72 TEST and an idempotency-key placeholder; it is illustrative, not a validated live request. [Raw lines 44–91]
- **Recurring:** The separately described token request includes `storePaymentMethod: true` and `shopperReference`. Once the initial payment has settled, a `recurring.token.created` webhook supplies `storedPaymentMethodId`; the merchant server needs the recurring-token lifecycle webhook. Later `/payments` use the stored ID, the shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. A request, redirect or example response does not prove token creation or settlement. [Raw lines 93–128]
- **Test/live:** The page says successful DANA live payments need a real mobile number registered with DANA, points to Customer Area for test-payment status, and requires a DANA request in live Customer Area before live acceptance. Its phrase “test successful DANA live payments” mixes environment terms; do not infer a TEST simulator. [Raw lines 329–337]

## Detail locators

- Discovery request/response examples: raw lines 44–85. The response shows method `type: dana`; no observed availability is implied.
- Recurring `/payments` examples in curl and language SDKs use IDR and TEST settings: raw lines 130–327. They do not resolve the discovery table's IN/INR contradiction.
- Final authorization, capture, settlement, failure and refund outcomes need separate payment-status or base-guide evidence.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/api-only/2026-09-15|DANA for API only (2026-09-15)]]
