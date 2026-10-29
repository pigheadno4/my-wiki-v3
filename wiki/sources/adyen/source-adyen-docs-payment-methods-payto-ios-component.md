---
title: "PayTo iOS Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/ios-component"
raw_files:
  - "adyen/docs/payment-methods/payto/ios-component/2026-09-15.md"
tags: [adyen, payto, ios, component, australia, mandate, subscription]
---

## Overview

This 2026-09-15-captured Adyen guide adds PayTo to an existing iOS Components integration in either Sessions or Advanced flow. It separates a one-off bank agreement/payment from a subscription agreement and later payments. A bank notification, accepted agreement, `Pending` response, or stored token does not by itself establish an authorized payment. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-payto]] for separate AU/AUD method and merchant-enablement context.

## Key takeaways

- Both flows require an existing iOS Components integration, Checkout API **v70 or later**, and PayTo added in Customer Area. The Advanced requirements link names an iOS **Drop-in** base guide even though this page is Components; its action-handling link ends in `#handle-the-redirect`, while the specified `action.type` is **await**. Follow the actual Components/await contract rather than treating those link labels as the action (raw lines 25–35, 337–348).
- For a **one-time Sessions** payment, the additional `/sessions` table requires shopper first and last name; its response describes an `adhoc`, exact-amount, one-count mandate ending by default one day after the request. The sample is AU/AUD at a test v71 endpoint and has a missing comma between `shopperReference` and `returnUrl`; the section labeled as a response is formatted as a curl command. Treat samples as illustrative, not copy-ready or evidence of payment (raw lines 39–120).
- **Subscription setup plus first payment** requires shopper name, `storePaymentMethod: true`, `recurringProcessingModel: Subscription`, `shopperInteraction: Ecommerce`, and mandate frequency, end date, amount, amount rule and remarks. `mandate.count` is table-optional but conditionally required at one or more when frequency is not `adhoc`. The weekly example describes a 30 AUD first payment after agreement acceptance and a mandate capped at 90 AUD once per week; it is an example, not a default. The Sessions subscription request example omits the table-required `storePaymentMethod: true` and has a missing comma before `recurringProcessingModel`. After bank acceptance, `RECURRING_CONTRACT` is described as providing a reference for subsequent payments. Sessions explicitly routes **subsequent** subscription payments to Advanced flow or API-only, despite also showing a stored-method Component initialization tab (raw lines 122–224, 296–321).
- Sessions uses `PayToComponent` for a one-off payment and `StoredPaymentMethodComponent` for a stored PayTo method. Advanced repeats these Component choices and requires `paymentMethod.type: payto`, `shopperAccountIdentifier` and shopper name for one-time and first subscription requests. The account identifier can be a BSB/account number or PayID form; the raw's allowed-value regex table is at lines 656–666. Advanced sample requests use test v72 and include `countryCode: AU`, `currency: AUD` and an app-style `returnUrl` (raw lines 264–321, 356–468, 489–590).
- Advanced first-payment examples return `resultCode: Pending` with `action.type: await`; the shopper receives a bank SMS, email or app notification to authorize or decline the agreement. A later **subsequent** `/payments` request uses `paymentMethod.storedPaymentMethodId` and `shopperInteraction: ContAuth` within the accepted agreement's conditions. The raw names `recurringDetailReference` in a `RECURRING_CONTRACT` webhook, says its token is in that webhook's `pspReference`, but the subsequent-payment table points to `recurring.token.created.data.storedPaymentMethodId`. Verify the actual webhook field and token mapping before using one as another (raw lines 217–254, 471–485, 590–653).
- Webhooks separate agreement and transaction outcomes: `OFFER_CLOSED` reports agreement failure/cancellation with `refusalReasonRaw`; `AUTHORISATION` on an accepted agreement can report **authorized or rejected** payment. `REFUND_FAILED` can reverse the expectation after an initially received `REFUND`; `DISABLE_RECURRING` reports expiry or cancellation of an agreement/token. The test email table simulates agreement and payment success, expiry, refusal and infrastructure error; it is test behavior, not live proof (raw lines 226–256, 323–335, 668–712).
- The captured request examples contain missing commas, omit a required flag in the Sessions subscription example, and have Advanced curl `-X POST` lines without continuation before `-d`. The Advanced integration/prerequisite links and webhook token references also need verification against the applicable base guide and active API contract before implementation (raw lines 87–89, 189–193, 345–347, 445–450, 539–570, 608–628).

## Detail locators

- Sessions prerequisites, one-off request/mandate and subscription fields: raw `## Sessions flow Component`, lines 25–224.
- Agreement/payment/refund/token webhooks and Sessions Component choices: raw lines 226–335.
- Advanced prerequisites, Components and one-time/first-subscription requests: raw `## Advanced flow Component`, lines 337–592.
- Subsequent agreement-bound payment, identifiers, repeated webhook and test sections: raw lines 594–712.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payto]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/ios-component/2026-09-15|PayTo iOS Component guide, captured 2026-09-15]]
