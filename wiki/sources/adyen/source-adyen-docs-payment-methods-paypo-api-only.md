---
title: "PayPo API-only integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/api-only"
raw_files:
  - "adyen/docs/payment-methods/paypo/api-only/2026-09-15.md"
tags: [adyen, paypo, api-only, redirect, poland]
---

## Overview

This 2026-09-15-captured PayPo API-only add-on describes the PayPo-specific steps for an **existing Advanced-flow API-only integration**; it points to the main integration guide for the base flow. It is a documentation snapshot, not evidence of current account enablement, shopper approval, live operation, or guaranteed funding timing. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Prerequisites are an existing API-only integration, additional-action handling for `action.type: redirect`, and adding PayPo in Customer Area. The guide's main sequence is method selection, merchant-built form, `/payments`, redirect, and capture (raw lines 19–37).
- For `/paymentMethods`, the page specifies `countryCode: PL` and `amount.currency: PLN`; its example available-method response has `type: paypo`. This is a discovery request/example, not proof that PayPo will be returned for every merchant (raw lines 45–52, 268–279).
- The PayPo-specific `/payments` table marks `paymentMethod.type: paypo`, `shopperName` with first and last name, and `shopperEmail` required; it lists billing and delivery addresses without required marks. The sample also includes amount, reference, return URL, and merchant account in the base request. The workflow prose says to include additional information about purchased items, but the PayPo-specific parameter table does **not** identify an item/order-line field. Do not infer a required item schema from that sentence or treat the sample as an exhaustive base API contract (raw lines 33–37, 281–319).
- The `/payments` response has a redirect action. Follow its `action.url`; for mobile, the page recommends the device's default browser, and for GET redirects shown in an app it recommends SFSafariViewController or Chrome Custom Tabs over WebView. On return, submit the URL-decoded `redirectResult` in `/payments/details`; use `resultCode` to display a result and retain `pspReference`. If the shopper does not return, use AUTHORISATION webhooks to learn the outcome. `Pending` or `Received` is not a final success state (raw lines 663–676, 711–771).
- Before authorization, the payment offer/link is available for **up to 72 hours**. When the shopper accepts and the payment becomes `Authorised`, the **30-day shopper term starts at authorization**, and the merchant must capture. Only **full-amount capture** is possible; immediate automatic capture can be configured when adding PayPo in the live Customer Area. The page says the merchant is funded after capture without waiting for the shopper to pay PayPo, while the result-code table says funds arrive in 2–3 days; treat timing as the page's qualified statements, not a guaranteed payout SLA (raw lines 679–709, 758–764; repeated capture section at 773–803).
- Authorization opens a shopper credit line. If the merchant cannot fulfill the order, the page advises cancellation using the original payment `pspReference`. Test credentials and verification code are **test-environment** instructions; live acceptance requires a PayPo request in the live Customer Area (raw lines 805–823).

> [!warning] Source example and wording limits
> The “How it works” sentence refers to purchased-item information, but the PayPo-specific `/payments` table lists no item field (raw lines 35, 281–291). Both curl request examples have `-X POST` on one line followed by `-d` on the next without a continuation (raw lines 63–64, 302–303); copy-pasting them as shown is not a complete executable curl command. Use the verified parameter table and main API-only guide for implementation; the examples do not establish a complete recipe.

## Detail locators

- Prerequisites and page scope: raw `# PayPo for API only` and `## Requirements` lines 15–29.
- Discovery PL/PLN values and illustrative API/library examples: raw `## Get PayPo as an available payment method` lines 45–279.
- PayPo-specific payment fields and example request: raw `## Add additional parameters to your /payments request` lines 281–319; library examples continue through line 661.
- Redirect, result handling, asynchronous webhooks: raw lines 663–771.
- Offer lifetime, authorization-based shopper term, full capture, and cancellation: raw lines 679–709 and 773–809.
- Test versus live setup: raw `## Test and go live` lines 811–823.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/api-only/2026-09-15|PayPo API-only add-on, captured 2026-09-15]]
