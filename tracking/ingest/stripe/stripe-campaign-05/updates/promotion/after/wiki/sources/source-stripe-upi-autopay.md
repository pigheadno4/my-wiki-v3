---
title: "Stripe: Recurring Payments (UPI AutoPay)"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/upi/upi-autopay
raw_files:
  - "stripe-payments-upi-upi-autopay-2026-11-07.md"
  - "stripe-upi-autopay-2025.md"
tags: [stripe, real-time-payments, upi, india, inr, upi-autopay, e-mandate, recurring, rbi, afa, pre-debit]
---

## Summary

The May 6 and November 7, 2026 [[stripe]] guides describe the same UPI AutoPay flow. A customer uses a UPI app to authorize an e-mandate, which supports subsequent automated payments within its terms.

## Mandate setup and initial charge

Both guides attribute the additional factor authentication (AFA) requirement to Reserve Bank of India rules. The customer must enter a UPI PIN to authorize the mandate at setup. The initial charge window is up to five minutes after the mandate is set up, and Stripe handles it automatically. In the SetupIntent flow, Stripe debits and immediately refunds the customer to avoid requiring AFA for the intended later charge. Setup PIN authorization still applies.

## Subsequent recurring payments

Both guides attribute the pre-debit notice requirement to the Reserve Bank of India. The customer must receive an SMS or app notice with the exact debit amount and a way to cancel the mandate at least 24 hours before each recurring charge.

After the merchant confirms a recurring PaymentIntent, Stripe sends that notice and waits at least 24 hours before attempting the charge. The guides describe no additional merchant action after confirmation. Sending the notice does not establish delivery, compliance, or the charge outcome.

## Mandate customization

Set `payment_method_options[upi][mandate_options]` to customize the mandate.

| Field | Default and scope |
| --- | --- |
| `description` | `Subscription`, shown in the UPI app when the customer approves the mandate |
| `amount` | `1500000` in minor units (15,000 INR), also the documented maximum for automatic AutoPay charges |
| `amount_type` | `maximum` allows charges up to the amount. Set `fixed` to authorize the exact amount. |
| `end_date` | Defaults to 10 years from mandate creation. The scheme allows up to 40 years from now. |

## Adaptive Pricing

For a customer-initiated Adaptive Pricing subscription, Stripe automatically creates the e-mandate in the selected currency when mandates support that currency. Omit explicit mandate parameters on the Checkout Session to use the automatically determined local-currency and exchange-rate values. Explicit Checkout Session mandate parameters override the automatic values. The paired guides link to separate mandate currency guidance.

## Related Pages

- [[stripe-real-time-payments]] — UPI and other real-time payment methods
- [[source-stripe-upi-set-up-future-payments]] — separate UPI setup guide

## Raw Sources

- [[raw/stripe-payments-upi-upi-autopay-2026-11-07|November 7, 2026 UPI AutoPay guide]]
- [[raw/stripe-upi-autopay-2025|May 6, 2026 UPI AutoPay guide]] — verbatim webpage content (49 lines)
