---
title: "Stripe: Accept an Affirm Payment"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/affirm/accept-a-payment
original_format: webpage
raw_files:
  - "stripe-affirm-accept-payment-2025.md"
tags: [stripe, bnpl, affirm, buy-now-pay-later, checkout, payment-intents, elements]
---

## Summary

The detailed guide captured on May 6, 2026 describes four Affirm web/API integration variants: Checkout (hosted or embedded), Checkout Sessions API with Elements, Payment Intents API with Elements, and Direct API. The November 7, 2026 capture at the same canonical URL is a variant index only. It links those four variants plus iOS and Android; it does not restate their requirements or establish current mobile behavior. The May integration details below remain dated.

## November 2026 variant navigation

The November index lists [Checkout](https://docs.stripe.com/payments/affirm/accept-a-payment.md?payment-ui=checkout), Elements with [Checkout Sessions API](https://docs.stripe.com/payments/affirm/accept-a-payment.md?payment-ui=elements&api-integration=checkout) or [Payment Intents API](https://docs.stripe.com/payments/affirm/accept-a-payment.md?payment-ui=elements&api-integration=paymentintents), [Direct API](https://docs.stripe.com/payments/affirm/accept-a-payment.md?payment-ui=direct-api), and Mobile [iOS](https://docs.stripe.com/payments/affirm/accept-a-payment.md?payment-ui=mobile&platform=ios) or [Android](https://docs.stripe.com/payments/affirm/accept-a-payment.md?payment-ui=mobile&platform=android). These are navigation targets, not fetched variant instructions. [November raw lines 9-20]

## May 2026 detailed guide

**Eligibility and Checkout constraints.** The guide says to check the account's Affirm eligibility in Payment methods settings. Its Checkout description lists customers in the US or Canada, USD or CAD, payment mode, one-time line items, and domestic currency; setup and subscription modes are excluded. Affirm is a single-use payment method with a customer redirect to choose a loan plan. These are May-capture claims, not revalidated by the November index. [May raw lines 20-42, 51-55]

**Checkout and Checkout Sessions API with Elements.** Hosted or embedded Checkout creates a Checkout Session. The Elements variant creates a server-side Session with `ui_mode: 'elements'`, passes a Checkout Session client secret to the client, collects a valid customer email, mounts the Payment Element, and calls `checkout.confirm`. Its Session expiry is described as 24 hours. Customer email may come from `customer_email`, an Accounts v2 `customer_account`, or a Customers v1 `customer` in the May examples; these are alternatives, not universal requirements to create both identities. [May raw lines 64-113, 251-323, 493-545, 593-737]

**Payment Intents API with Elements.** The May flow calls `elements.submit()`, creates a PaymentIntent on the server, supplies its PaymentIntent client secret, then calls `stripe.confirmPayment` with a return URL. The May examples distinguish Accounts v2 `customer_account` from Customers v1 `customer`. Session creation, PaymentIntent creation, a client secret, or a return to the browser alone does not prove payment success. [May raw lines 745-1257]

**Direct API.** The May flow creates a server-side PaymentIntent and passes its client secret to Stripe.js `confirmAffirmPayment` with a return URL. Its server-confirm alternative enters `requires_action` and uses `next_action.redirect_to_url` for customer action; the guide calls for server-side webhook verification. Optional shipping and billing details are recommended, not described as universal prerequisites. [May raw lines 1337-1537, 1600-1669]

**Payment outcome boundary.** In the Checkout path, `checkout.session.completed` means the buyer authorized the payment; the guide says to wait for `payment_intent.succeeded` before fulfillment, or handle `payment_intent.payment_failed` and `requires_payment_method`. The redirect and browser return are not payment success signals. [May raw lines 195-205]

**Shipping and fallback.** For Checkout, the guide recommends `payment_intent_data[shipping]` even when Checkout does not collect shipping because it can improve loan acceptance. It recommends additional methods such as cards because Affirm declines more often; after a failed or abandoned Affirm attempt, the PaymentMethod can detach and the PaymentIntent can return to `requires_payment_method`. [May raw lines 116, 223-249]

**No-action timeout — conflicting May wording.** The prose says a customer who takes no action within 12 hours after redirect to Affirm reaches `requires_payment_method`; the error table instead describes 12 hours after initial checkout creation. The May guide itself gives these different start points, so this source does not choose one clock origin. [May raw lines 227-239, 1701-1713]

**Manual capture — conflicting May path instructions.** The Payment Intents API with Elements section says capture within seven days and describes partial capture with `amount_to_capture` no greater than the total. The Direct API section says capture within 30 days and says full amount only. Both describe an authorized PaymentIntent in `requires_capture`, but the windows and amount rules conflict across the May sections; verify the applicable variant before acting. Separately, the Checkout sandbox section says an uncaptured **test-mode** PaymentIntent expires ten minutes after successful authorization. That is a test condition, not a live capture deadline. [May raw lines 209-219, 1271-1313, 1556-1589]

**Failure and cancellation categories.** The May error table lists `payment_method_provider_decline`, `payment_intent_payment_attempt_expired`, `amount_too_small`/`amount_too_large`, and `payment_method_not_available`. It separately lists `affirm_checkout_canceled` as a **charge outcome reason**, which cannot distinguish a buyer cancellation from an Affirm loan rejection; it is not identified there as an error code. [May raw lines 231-249, 1705-1723]

**Example versions.** The May Elements examples use Stripe.js `dahlia` and list `@stripe/stripe-js` 7 or later, React Stripe.js 5 or later, and loader 8 or later. These are example-specific, dated version statements; the November index provides no replacement version guidance. [May raw lines 368-399]

## Raw Sources

- [[raw/stripe-affirm-accept-payment-2025|May 6, 2026 detailed Affirm guide]] — factual historical capture; filename reflects an earlier naming convention.

## Related raw API references

- [[raw/stripe-payments-affirm-accept-a-payment-2026-11-07|November 7, 2026 Affirm variant index]] — navigation-only capture at the canonical URL; linked variant content was not fetched in this packet.

## Related

- [[stripe]] — Stripe company context.
