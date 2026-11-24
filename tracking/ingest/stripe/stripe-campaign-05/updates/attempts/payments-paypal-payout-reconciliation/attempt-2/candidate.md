---
title: "Stripe: PayPal Payout Reconciliation"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/paypal/payout-reconciliation"
raw_files:
  - "stripe-payments-paypal-payout-reconciliation-2026-11-07.md"
  - "stripe-paypal-reconciliation-2025.md"
tags: [stripe, wallets, paypal, reconciliation, settlement, payout, transaction-id, reference]
---

## Settlement and reconciliation scope

The May 7 and November 7, 2026 guides describe matching processed Stripe payments to PayPal orders when funds settle on PayPal. The merchant reconciles those transactions using its PayPal business reports or sFTP feed. For transactions settling on Stripe, Stripe reconciles the transactions before payout. The separate November [[source-stripe-paypal-settlement|settlement preference guide]] says direct businesses can choose the settlement destination when connecting their accounts. Connect funds settle on Stripe. The merchant manages payouts on PayPal when funds settle there.

Stripe's separate [Payout reconciliation report](../../raw/stripe-reports-payout-reconciliation-2026-11-07.md#L9-L26) groups transactions into automatic payout batches. It also covers platforms using manual payouts when their connected accounts have automatic payouts enabled. Other manual-payout users can use the Balance report. Stripe cannot identify the transactions included in an instant payout. See [[stripe-payouts]] and [[source-stripe-payouts-reconciliation]] for Stripe-side payout reconciliation.

## Merchant reference

Use a business-generated order or invoice ID as `payment_method_options.paypal.reference` when creating the PaymentIntent. The customer can see the reference. After the payment is processed, it appears as **Invoice ID** in the PayPal Settlement Report. Refunds and disputes derived from the original payment are associated with that reference.

| Capture | PaymentIntent create example |
| --- | --- |
| May 7, 2026 | Node server example with `amount: 1099`, `currency: "eur"`, `payment_method_types: ["paypal"]` and the PayPal reference `my_order_id`. |
| November 7, 2026 | cURL example with `amount=1099`, `currency=eur`, `automatic_payment_methods[enabled]=true` and `payment_method_options[paypal][reference]=my_order_id`. |

These examples illustrate creating the PaymentIntent and composing its method selection and reference. Account eligibility and payment confirmation or capture are separate.

## PayPal capture ID

When a business-generated order ID is unavailable, the guide recommends the PayPal capture ID at `Charge.payment_method_details.paypal.transaction_id`. Stripe documents the field as present only after capture. After processing, it maps to **Transaction ID** in the PayPal Settlement Report. The illustrative Charge has `captured: true` and `paid: true`, and shows a distinct Stripe Charge ID and PayPal payer ID. The capture ID identifies the PayPal transaction. Bank payout arrival requires separate evidence.

## PayPal Settlement Report

In a PayPal business account, go to **Activity → All Reports → Transactions → Settlement**. Contact PayPal to enable sFTP reporting. The report covers balance-impacting transactions over a 24-hour period and can be used to reconcile movements in the PayPal account against the linked bank account.

## Related

- [[stripe-wallets]] — PayPal wallet and settlement context
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-paypal-payout-reconciliation-2026-11-07|November 7, 2026 PayPal reconciliation guide]] — full capture with automatic method selection in its creation example.
- [[raw/stripe-paypal-reconciliation-2025|May 7, 2026 PayPal reconciliation guide]] — full capture with manual PayPal method selection in its creation example.
