---
title: "Stripe: Accept a Payment with Scalapay"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/scalapay/accept-a-payment"
raw_files:
  - "stripe-scalapay-accept-payment-2025.md"
tags: [stripe, bnpl, scalapay, buy-now-pay-later, consumer, installments, checkout, payment-intents]
---

## Overview

The May 6, 2026 guide describes accepting a single-use `scalapay` payment in three or four installments. The customer authorizes with Scalapay after a redirect, and the merchant receives immediate notice of success or failure. Use the resulting payment status to decide what to display or fulfill. The November 7, 2026 capture links the four implementation variants without including their instructions.

## May integration paths

| Path | Setup and return |
| --- | --- |
| Hosted Checkout | Create a Checkout Session. Use Dashboard-managed payment methods or add `scalapay` to an explicit list as shown in May. The hosted example uses `success_url`. |
| Payment Element with Checkout Sessions | Create the Checkout Session server-side, set its `return_url`, and use the Session client secret to initialize Checkout on the client. The guide shows Dashboard-managed and manually listed approaches. |
| Payment Element with PaymentIntents | Set amount and currency server-side. The examples distinguish Accounts v2 `customer_account` from Customers v1 `customer`. Use the Intent client secret and `stripe.confirmPayment` with `return_url`. |
| Direct API | Create a PaymentIntent server-side. For the recommended Stripe.js client route, call `stripe.confirmPayment` with the Intent client secret and `return_url` to handle the redirect. The optional separate server-confirm route sends `return_url` and follows `next_action.redirect_to_url` when the Intent requires action. Verify the Intent status on return. |

Both May Checkout Sessions paths list **IT, FR, ES, DE, NL, BE, IE and FI** and EUR as the supported and presentment currency. The documented mode is payment. Setup and subscription modes are excluded. Keep line items in the same currency. The May method overview lists 28 business locations, with EUR presentment and a EUR-only country map, but does not map that broader list to each integration. The acceptance guide’s May Direct API currency map includes non-EUR examples such as USD for the US and GBP for the UK. The malformed currency comment in the May hosted sample does not override its compatibility table. These are dated scope differences. See May acceptance lines 18–70, 95–197 and 1376–1391, and the separate [[source-stripe-scalapay|Scalapay method overview]].

## May PaymentIntent lifecycle

The Payment Element/PaymentIntents variant documents optional manual capture. Setting `capture_method: 'manual'` authorizes only. On successful authorization the Intent enters `requires_capture`. Capture defaults to the authorized total and accepts `amount_to_capture` up to that total. Explicit cancellation is available before capture. Stripe cancels an uncaptured Intent after seven days and sends `payment_intent.canceled`. See May lines 1094–1140. Use `payment_intent.succeeded` for completed-payment handling instead of relying on browser return.

Sandbox redirect testing offers approval and decline controls on the test page. The May guide distinguishes the live redirect to Scalapay from those test controls. The Intent error tables include `payment_intent_invalid_currency`, `payment_intent_authentication_failure` and `payment_intent_redirect_confirmation_without_return_url`. See May lines 1142–1158 and 1358–1403.

## Cross-guide coverage

The May method overview marks Connect No. The May and November BNPL product matrices both mark Connect Supported for Scalapay. The November BNPL matrix marks Mobile Payment Element Supported where May marked it Unsupported. The November acceptance selector supplies no mobile variant. The November BNPL API table omits Scalapay, leaving the May method-specific Intent guidance separately dated. See [[source-stripe-bnpl-overview]] and [[stripe-bnpl#API Support|BNPL API and Connect coverage]].

## Related Pages

- [[stripe-bnpl]] — Stripe BNPL payment methods and dated integration guides
- [[source-stripe-scalapay]] — Scalapay method overview and scope
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-scalapay-accept-payment-2025|May 6, 2026 full Scalapay acceptance guide]] — 1,403 lines, with Markdown formatting fixes and one locally captured image

## Related raw API references

- [[raw/stripe-payments-scalapay-accept-a-payment-2026-11-07|November 7, 2026 Scalapay acceptance variant index]] — Checkout, Elements with Checkout Sessions, Elements with Payment Intents, and Direct API navigation
