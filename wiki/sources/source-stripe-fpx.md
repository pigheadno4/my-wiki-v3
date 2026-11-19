---
title: "Stripe: FPX Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/fpx"
raw_files:
  - "stripe-payments-fpx-2026-11-07.md"
  - "stripe-fpx-2025.md"
tags: [stripe, fpx, malaysia, myr, bank-redirect, authenticated, brn]
---

## Summary

The November 7, 2026 FPX overview describes a single-use Malaysian bank redirect for MY customers and MYR domestic payments. A customer selects a bank, authenticates there, and returns to the merchant. The business must provide its Business Registration Number (BRN) to process FPX payments and receive payouts. The page distinguishes B2C immediate success display from B2B pending display before asynchronous confirmation. This documentation does not prove an individual payment succeeded or settled. See [[stripe]], [[stripe-fpx]], and [[stripe-bank-redirects]].

## Eligibility and payment flow

The November page lists Malaysia as both business and customer location; merchants and Connect platforms can be eligible, subject to account review or capability restrictions after activation. It says there are no additional FPX website or MCC requirements beyond Stripe account activation requirements. FPX is MYR-presented and domestic, not cross-border. Limits differ by business model: **B2C 1.00–30,000.00 MYR**, **B2B 2.00–1,000,000.00 MYR**. The older May 3, 2026 accept-payment guide gives **RM2–RM30,000** in its *legacy Elements* path; preserve that dated UI scope rather than using it as a universal current limit.

The customer selects FPX and a bank, then is redirected to the bank's browser authorization surface; on mobile it may open the bank app. The customer signs in and completes bank-specific authentication, then automatically returns to the merchant page according to the November overview. The May 3 overview's diagram described merchant return as optional. The November page says B2C payments immediately display successful, while B2B payments initially display **pending** until asynchronous confirmation and then display successful. Its property table says immediate confirmation and instant provisional access, while settlement can take up to **T+5 business days**. A browser return, pending display, or provisional access is not independent proof of success, funds availability, or settlement. For server-side outcome handling, the May 3 accept-payment guide points to `payment_intent.succeeded` rather than a client callback; see [[source-stripe-fpx-accept-payment]].

## Product and API boundaries

The November overview marks full-page/embedded Checkout, Payment Links, Payment Element, iOS and Android in-app payments, Billing, Invoicing, Connect, Checkout Sessions and PaymentIntents supported. **iOS and Android Payment Sheet is B2C only.** The Billing/Invoicing support footnote says **`send_invoice` collection method only**. FPX is single use and the same table marks recurring payments, PaymentIntents with `setup_future_usage`, SetupIntents and off-session payments unsupported; broad Billing support does not imply automatic recurring charging. The May 3 overview and accept-payment guide explicitly excluded Checkout setup and subscription modes; the guide's legacy Elements section also said FPX was not supported with Billing, while the May 3 bank-redirects matrix listed FPX Subscriptions via `send_invoice`. Keep that same-day guide-versus-matrix conflict dated and route-specific; the November broad Billing row does not establish automatic recurring charges. Express Checkout Element, Payment Method Messaging Element, Customer Portal, Terminal and manual/partial/multi/over-capture are not supported in the November table.

FPX does not support standard disputes or chargebacks: the overview says customers cannot file a bank chargeback and Stripe does not withdraw funds because of a dispute. If a customer contacts their bank, the bank refers them to the merchant, who can issue a refund. This does not remove the merchant's refund obligations or establish that a refund completed.

## Refunds: dated change and final state

The May 3 overview said a refund could be submitted within **60 days** and took approximately **one week**. The November 7 overview says full or partial refunds can be submitted within **180 days**, normally take up to **14 days** and may take **six weeks**. They are asynchronous and cannot be canceled after submission. The refund is a separate credit to the customer's bank account, not a card-like reversal; its bank statement entry may reference the original payment descriptor without saying "refund". Check the Refund object's `status` or verified `refund.updated`/`refund.failed` event for the final outcome. On failure, Stripe returns the amount to the merchant's Stripe balance and the page directs the merchant to refund by another method. A submitted refund is not a completed customer refund. The separate May 3 accept-payment guide also states 60 days; retain that dated conflict until its own guide is reconciled.

## Statement descriptors and PayNet reconciliation

The FPX bank statement shows a seller ID, seller description, and seller order number. Full `statement_descriptor` controls the seller order number; `statement_descriptor_suffix` applies only to cards. For Connect destination charges without `on_behalf_of`, Stripe uses the platform descriptor; direct charges and charges with `on_behalf_of` use the connected account descriptor. To reconcile with PayNet records, retrieve the PaymentIntent with `latest_charge` expanded and read `latest_charge.payment_method_details.fpx.transaction_id`. The older accept-payment guide also details a mandatory confirmation page, bank list, legacy Elements path and separate FPX balance; those route-specific details remain under [[source-stripe-fpx-accept-payment]].

## Raw Sources

- [[raw/stripe-payments-fpx-2026-11-07|FPX overview — November 7, 2026 full capture]]
- [[raw/stripe-fpx-2025|FPX overview — May 3, 2026 capture; filename retains 2025 suffix]]

## Related raw guide

- [[raw/stripe-fpx-accept-payment-2025|FPX accept-payment guide — May 3, 2026; Checkout, legacy Elements and route-specific constraints]]
