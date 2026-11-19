---
title: "Stripe: Afterpay and Clearpay Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
canonical_url: "https://docs.stripe.com/payments/afterpay-clearpay"
original_format: webpage
raw_files:
  - "stripe-payments-afterpay-clearpay-2026-11-07.md"
  - "stripe-afterpay-clearpay-2025.md"
tags: [stripe, bnpl, afterpay, clearpay, cash-app, buy-now-pay-later, installments, connect, disputes]
---

## Summary

Afterpay (Clearpay in the UK) is a single-use buy now, pay later method. Stripe redirects the customer to Afterpay for authentication, plan selection and approval; Afterpay collects installments from the customer after an accepted payment. The 2026-11-07 page labels access “instant provisional,” payment confirmation “immediate,” and settlement on the standard payout schedule. Merchant upfront funding after acceptance is distinct from a completed customer return, a succeeded PaymentIntent and bank payout.

## Eligibility and coverage

- Stripe merchant or Connect platform/marketplace accounts in AU, CA, GB, NZ and US can accept supported domestic customers and currencies (AUD, CAD, GBP, NZD, USD); B2C is supported, B2B is not. Check Payment methods settings. Stripe may review eligibility after activation, and the account website must meet Stripe's activation requirements.
- **General availability is domestic only**: the customer and business must be in the same country. The 2026-11-07 capture additionally marks cross-border transactions **private preview**. This qualifies the older page's unqualified “domestic only”; it does not establish general cross-border availability or a merchant's preview access.
- For dynamic methods in Checkout Sessions or the Payment Element, Stripe filters by customer country, using the two-letter shipping country then geocoded client IP. With manually listed `payment_method_types`, the integration must present Afterpay only to eligible customers or use dynamic methods.
- The short prohibited list is alcohol, donations, pre-orders, NFTs and B2B. The new page separately distinguishes **prohibited** MCCs, which cannot use Afterpay, from **restricted** MCCs that can require additional account information; consult its MCC table and terms for the complete list. The older 2026-05-06 short list also named bars/lounges. Its omission from the new short list is not permission for that business category.

## Payment options and limits

| Market | Currency | Pay in 4 | Monthly installments |
| --- | --- | --- | --- |
| AU | AUD | 1–4,000; four interest-free bi-weekly payments | — |
| CA | CAD | 1–2,000; four interest-free bi-weekly payments | — |
| NZ | NZD | 1–4,000; four interest-free bi-weekly payments | — |
| GB | GBP | 1–1,200; four interest-free bi-weekly payments | — |
| US | USD | 1–2,000; four interest-free bi-weekly payments | 400–4,000; 6 or 12 months, interest-bearing |

The page's top-level AUD 1–4,000 limit is an AU example, not a universal limit. In the US, Pay in 4 and monthly overlap from USD 400–2,000; monthly alone applies above USD 2,000 to USD 4,000. Non-US markets list Pay in 4 only.

## Payment flow and capabilities

On desktop, the customer goes to the Afterpay site to create or sign in to an account; on mobile, the installed app opens, otherwise the site. The customer chooses a plan and accepts repayment terms within **3 hours**, then returns to checkout when authorized. A redirect/return alone does not prove a succeeded PaymentIntent. The overview's 3-hour customer authorization window should not be substituted for the separate accept-a-payment guide's PaymentIntent `requires_action` expiry.

Manual and partial capture are supported. Multi-capture, over-capture, recurring payments, extended/flexible/incremental/decremental/re-authorizations are not. The new matrix supports full-page and embedded Checkout, Payment Links, Payment Element, in-app payments, Payment Method Messaging Element, Managed Payments and Connect; APIs include Checkout Sessions and PaymentIntents. It marks Billing, Invoicing, Customer Portal, Radar, Terminal, Express Checkout Element, SetupIntents, PaymentIntents with `setup_future_usage`, and off-session payments unsupported.

**Dated product-support conflict:** the 2026-05-06 capture listed **one-time Invoicing in private preview**, explicitly excluding subscription invoices; the 2026-11-07 matrix marks Invoicing unsupported. Neither page explains the change or establishes current preview access. Keep the older private-preview fact dated rather than generalizing either matrix to another date.

After a completed payment, expand the PaymentIntent's `latest_charge` and read `latest_charge.payment_method_details.afterpay_clearpay.order_id` for the Afterpay order ID. The customer's bank/card statement shows *AFTERPAY* with the merchant descriptor; set a custom descriptor on the PaymentIntent before confirmation if needed. The Payment Method Messaging Element can display Afterpay branding; use Clearpay branding for UK consumers.

## Refunds and disputes

Submit full or partial refunds through the Dashboard or Refunds API within **120 days** of the original payment. They are asynchronous, take up to **10 business days**, cannot be canceled, and are not reversals: Afterpay cancels remaining scheduled installments and returns amounts already paid. Check Refund `status` in Dashboard/API and final `refund.updated` or `refund.failed` events. A failed refund returns the amount to the Stripe balance and requires another customer refund method. Submission is not proof of success.

Customers have **120 calendar days from purchase** to open one full-amount dispute per payment; partial disputes are unsupported. Stripe withholds the disputed amount. The merchant has **14 calendar days from creation** to submit evidence through the Dashboard or the Disputes API with Files API uploads; the Dashboard and Dispute `evidence_details.due_by` show the deadline. The 2026-11-07 page says Afterpay decides within **30 calendar days of dispute creation**. A win returns the funds; a loss makes the balance charge permanent. Afterpay covers losses from customer fraud or inability to repay installments, while Stripe may ask the merchant to stop or pause shipment.

**Dated dispute-clock conflict:** the 2026-05-06 page says the 30 calendar days run **from evidence submission**. Both captures agree on the 120-day filing and 14-day evidence windows; do not silently treat the two decision clocks as equivalent.

## Dated integration and Connect notes

The 2026-05-06 page reports the US rebrand to **Cash App Afterpay** and says no integration changes are needed **unless the merchant has custom Afterpay components**. The November page omits that notice; omission alone does not reverse it. The older page also explicitly supports Connect direct, destination, and separate charges and transfers, with correct MCCs for connected accounts using Express Dashboard or a dashboard not hosted by Stripe. The November page confirms Connect generally and expands prohibited/restricted MCC eligibility, but does not re-enumerate charge types. The integration guide has its own billing-details, shipping and PaymentIntent-state details.

## Related

- [[stripe]] — Stripe company page.
- [[stripe-bnpl]] — Buy now, pay later concept.

## Raw Sources

- [[raw/stripe-payments-afterpay-clearpay-2026-11-07]] — full webpage capture fetched 2026-11-07 (302 lines).
- [[raw/stripe-afterpay-clearpay-2025]] — earlier full webpage capture fetched 2026-05-06 (196 lines); fixed `_Connect_` → `*Connect*`; MP4 video CDN URL left as-is.
