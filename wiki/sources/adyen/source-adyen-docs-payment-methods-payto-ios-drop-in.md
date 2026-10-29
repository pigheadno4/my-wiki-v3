---
title: "PayTo iOS Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payto/ios-drop-in/2026-09-15.md"
tags: [adyen, payto, australia, ios, drop-in, mandate]
---

## Overview

This 2026-09-15-captured Adyen guide adds **PayTo to an existing iOS Drop-in integration**. It separates one-time payments, subscription agreement setup and first payment, and later subscription charges across Sessions and Advanced server-side flows. A bank agreement invitation, `Pending` response or `await` action is not payment authorization. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Both flows require existing iOS Drop-in, Checkout API **v70 or later**, and PayTo added in Customer Area; Advanced additionally requires handling `action.type: await` (raw lines 25–34, 279–289). Its action-handling link points to a `#handle-the-redirect` anchor despite identifying **await**; do not recast the action as redirect. The guide says no PayTo-specific Drop-in configuration parameters are needed (raw lines 257–261, 291–295).
- **Sessions one-time** `/sessions` additions require shopper first and last name. Optional statement, line items and reference are listed; the page recommends a unique reference but says it is not required, with a **35-character PayTo maximum** (raw lines 52–66). The response describes an `adhoc`, `exact`, one-payment mandate with amount equal to the request and a default end date one day after the request (raw lines 91–100). The sample request at raw lines 70–89 has a missing comma between `shopperReference` and `returnUrl`; it is not copy-ready JSON.
- **Sessions subscription setup and first payment** requires shopper name, `storePaymentMethod: true`, `recurringProcessingModel: Subscription`, `shopperInteraction: Ecommerce`, and mandate frequency, end date, amount, amount rule and remarks. `mandate.count` is conditionally needed when frequency is not `adhoc`; the table lists further optional start date, line items and reference (raw lines 121–147). Its example is a first **AUD 30** payment with a **weekly up-to-AUD 90** agreement and one payment per week (raw lines 149–159). This illustrates an agreement cap, not authorization of all later charges. The example request has a missing comma after `shopperReference` (raw lines 161–193).
- The shopper receives a bank notification to **authorize or decline the agreement**. After acceptance, a `RECURRING_CONTRACT` webhook includes a `recurringDetailReference`; later subscription payments are stated to be possible only through **Advanced flow or API-only**, not Sessions (raw lines 216–223, 475–478). Keep agreement acceptance separate from the outcome of any payment made under it.
- **Advanced one-time** `/payments` additions require `paymentMethod: payto`, a bank or PayID `shopperAccountIdentifier`, and shopper first/last name; optional statement, line items and reference follow (raw lines 309–325). The example returns `resultCode: Pending` with `action.type: await` (raw lines 327–372). The listed identifier shapes include BSB-account number, PayID email, phone, ABN and organization identifier; consult the raw regex table rather than treating its sample values as a universal validator (raw lines 541–551).
- **Advanced subscription setup** adds required storage, Subscription/Ecommerce flags and mandate terms to the account identifier and shopper name (raw lines 374–403). The shopper is asked to approve or decline via their bank (raw line 475). A later `/payments` charge requires `paymentMethod: payto`, a `storedPaymentMethodId` from the `recurring.token.created` webhook and `shopperInteraction: ContAuth`; the stored method may be used **only within the accepted agreement's conditions** (raw lines 479–488). The guide also mentions `RECURRING_CONTRACT`/`recurringDetailReference` for agreement acceptance; do not collapse these different webhook/reference names into one identifier (raw lines 218, 477, 486, 575–583).
- **Webhook finality:** `OFFER_CLOSED` reports an agreement failure or shopper cancellation, `AUTHORISATION` reports a payment on an accepted agreement and can be authorized or rejected, `REFUND_FAILED` can follow an initially received refund, and `DISABLE_RECURRING` reports agreement termination/token deletion (raw lines 225–255, 553–583). Test identifiers simulate agreement expiry/refusal, payment refusal/error and successful cases (raw lines 263–277, 585–599). These are test scenarios, not live bank-operation evidence.

> [!warning] Illustrative request examples
> Several `/payments` curl examples omit a shell continuation after `-X POST` before `-d` (raw lines 327–354, 417–455, 490–513), and some JSON examples omit commas (raw lines 70–89, 161–193, 417–455, 490–513). The response examples are also displayed in `bash` fences as curl commands (raw lines 102–119, 358–372, 459–473, 517–539). Use the tables and API contract, not copied snippets, to build requests.

## Detail locators

- Sessions prerequisites, one-time fields and mandate defaults: raw `## Sessions flow Drop-in`, lines 25–119.
- Sessions subscription setup, bank agreement and later-flow restriction: raw lines 121–223.
- Sessions status webhooks and test scenarios: raw lines 225–277.
- Advanced prerequisites, one-time fields and pending await response: raw `## Advanced flow Drop-in`, lines 279–372.
- Advanced subscription and subsequent stored-method conditions: raw lines 374–539.
- Identifier formats, status webhooks and tests: raw lines 541–599.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/ios-drop-in/2026-09-15|PayTo iOS Drop-in, captured 2026-09-15]]
