---
title: "Adyen TWINT API-only guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/api-only"
raw_files:
  - "adyen/docs/payment-methods/twint/api-only/2026-09-15.md"
tags: [adyen, twint, api-only, switzerland, chf, redirect, capture, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds TWINT to an existing API-only integration. It covers CH/CHF discovery, additional-action handling, capture and partial-capture limits, recurring token creation and reuse, and TEST/LIVE setup. It gives only a high-level shopper redirect/app confirmation path; it does not supply a concrete `/payments` action response, return/`/payments/details` procedure or final authorization webhook here. This snapshot does not prove current merchant eligibility, created token, capture, funds transfer or payment success. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Base flow and form conflict:** the guide requires an existing API-only integration, handling `action.type: redirect` or `sdk`, and TWINT added in Customer Area. Its high-level sequence has shopper selection, a merchant-built form, TWINT-hosted page and shopper authorization in the app. Step 2 says the shopper enters details in the form, while the dedicated form section says **no shopper information needs collecting**; do not infer a required data-entry field from the sequence. Discovery via `/paymentMethods` specifies `countryCode: CH` and `amount.currency: CHF`, returning `type: twint`. The example's `-X POST` lacks a shell continuation before `-d`, so it is not a reliable copy-paste command. The guide says no extra TWINT-specific `/payments` parameters beyond the base flow. (raw lines 23–87)
- **Capture limits:** the page says TWINT is captured automatically by default with Customer Area Capture Delay set to **Immediate** or **1–7 days**. If set to **Manual**, capture must occur before TWINT authorization expires after **7 days**. It allows a partial capture, **not multiple partial captures**; any amount unclaimed after partial capture is automatically cancelled. Its prose names `modificationAmount` for the capture request, whereas the JSON example uses `amount` and a `reference`; treat the example as illustrative and verify the endpoint contract before implementation. (raw lines 89–116)
- **Recurring:** token creation adds `storePaymentMethod: true` and a shopper-unique `shopperReference` of at least three characters to `/payments`. After details are stored, a `recurring.token.created` webhook carries `storedPaymentMethodId`, the initial payment `pspReference` as `eventId`, and the shopper reference; the merchant server must receive token lifecycle events. Later token payments use that ID, the same shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. The CHF examples illustrate Subscription; several language snippets leave `paymentRequest` undefined or have incomplete setup, so they are not all runnable recipes. The token webhook is not proof a particular stored method or later payment succeeded. (raw lines 118–389)
- **Environment:** TEST status is checked in Customer Area; accepting LIVE TWINT requires submitting a separate request in the **live** Customer Area. The page does not say that submission by itself activates the method. (raw lines 391–399)

## Detail locators

- Requirements, shopper sequence, form contradiction and CH/CHF discovery: pinned raw lines 23–83.
- No extra `/payments` fields; capture settings, seven-day expiry and partial-capture example mismatch: pinned raw lines 85–116.
- Token creation/webhook and subsequent shopper-absent model fields: pinned raw lines 118–155; examples: lines 157–389.
- TEST status and LIVE request gate: pinned raw lines 391–399.

## Related

- [[adyen-online-payments]] — main provider payment/action context
- [[adyen-tokenization]] — provider token lifecycle
- [[source-adyen-docs-payment-methods-twint]] — TWINT method overview and shopper handoff

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/api-only/2026-09-15|TWINT API-only guide, 2026-09-15]]
