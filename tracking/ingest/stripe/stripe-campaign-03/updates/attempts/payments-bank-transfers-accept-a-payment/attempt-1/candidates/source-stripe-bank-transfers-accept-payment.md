---
title: "Stripe: Accept a Bank Transfer"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/bank-transfers/accept-a-payment"
raw_files:
  - "stripe-bank-transfers-accept-payment-2025.md"
tags: [stripe, bank-transfers, payment-intents, customer-balance, webhooks, checkout, reconciliation]
---

## Overview

Stripe's November 7, 2026 capture of this URL is a variant index. Its headline names **Checkout Sessions or Payment Intents** for accepting bank transfers and links Elements with each API, hosted Checkout, and Direct API variants. The capture contains no steps or prerequisites for the newly linked Elements Checkout Sessions variant. The detailed integration facts below come from the May 5, 2026 full capture; the index does not confirm their current availability or retire them. See [[stripe]], [[stripe-bank-transfers]], and [[stripe-checkout]].

## Key takeaways from the May 5 guide

- A bank transfer is a push payment to a customer-linked virtual account. Stripe describes reconciliation through customer cash balance; underpayment can partially fund an open PaymentIntent, while an invoice remains open until fully funded. Excess after reconciliation remains in customer balance. With several open payments or invoices, automatic reconciliation uses details such as the reference and amount; a Customer can instead use manual reconciliation. See raw lines 16, 28–50.
- The captured PaymentIntent and hosted Checkout examples require an associated **Customer**; the PaymentIntent request populates `customer`, and the Checkout Session passes an existing Customer. The guide separately recommends customer-configured Accounts v2 objects for most uses but marks Accounts v2 public preview for non-Connect users and requires a preview version for preview participants. Do not treat that note as proof that all May 5 Customer parameter examples work unchanged with Accounts v2. See raw lines 8–14, 71–85, 950–1000.
- The May 5 Checkout bank-transfer route is a single-use, delayed-notification payment method in `payment` mode with one-time line items in one currency; `setup` and `subscription` modes are not supported in that route. Submission can lead to a hosted instruction page while funding remains pending. `checkout.session.completed` denotes form submission there; `checkout.session.async_payment_succeeded` and a `succeeded` PaymentIntent denote successful transfer and fulfillment. See raw lines 940–975, 1182–1205.
- In the PaymentIntent route, first confirmation with insufficient cash balance emits `payment_intent.requires_action` even if some pre-existing balance was applied. Later insufficient incoming funds applied to the Intent emit `payment_intent.partially_funded`; `payment_intent.succeeded` marks payment success. Updating a partially funded Intent's amount returns its applied funds to customer balance; Stripe may then fund other open Intents, and manual reconciliation requires reapplying funds. See raw lines 722–744, 1954–1976.

## May 5 integration detail

**PaymentIntent creation.** The Elements route creates the Intent server-side, then collects details with the client Payment Element and confirms with `stripe.confirmPayment`. The Direct API route creates and confirms server-side with `payment_method_data.type: 'customer_balance'`; when balance is insufficient, its `next_action.type` is `display_bank_transfer_instructions` for client display. The client must use the exact supplied bank details. A browser return to `return_url` alone does not prove payment: retrieve and inspect PaymentIntent status. See raw lines 83–85, 345–394, 494–603, 1384–1413, 1700–1715.

The manual PaymentIntent examples specify `payment_method_types: ['customer_balance']`, `funding_type: 'bank_transfer'`, and a regional `bank_transfer.type`:

| Region | Manual `bank_transfer.type` | May 5 qualification |
| --- | --- | --- |
| US | `us_bank_transfer` | USD example |
| UK | `gb_bank_transfer` | GBP example |
| EU | `eu_bank_transfer` | The manual FR `country` option selects the displayed IBAN country; Dashboard-managed selection instead uses Customer country or Stripe account fallback. The guide says new localized VBANs are unavailable for ES. |
| JP | `jp_bank_transfer` | JPY example; automatic-method examples include `return_url`, while manual examples omit it. |
| MX | `mx_bank_transfer` | MXN example; automatic-method examples include `return_url`, while manual examples omit it. |

The `return_url` in those JP/MX examples is not a stated region-wide requirement. In the May 5 guide, Dashboard-managed dynamic methods are an alternative to manual selection; it says the `automatic_payment_methods` parameter is optional in the latest API version of that capture because the feature is enabled by default. These are dated examples, not a present-day API-version guarantee. See raw lines 87–91, 153–189, 193–343, 1388–1392, 1469–1513, 1517–1687, 1853–1858.

**Funding and reconciliation.** If customer balance fully covers the Intent at creation/confirmation, the guide describes immediate `succeeded`. Otherwise instructions include `amount_remaining`; a partial payment is not reflected in the merchant's account balance until complete. Receive both `payment_intent.requires_action` and `payment_intent.partially_funded` for the two underfunding moments, and verify `payment_intent.succeeded` before fulfillment. The guide recommends webhooks for completion. See raw lines 191, 722–744, 1700–1715, 1954–1976.

**Checkout.** In the May 5 hosted Checkout example, create a Session with `customer`, `mode: 'payment'`, `customer_balance`, bank-transfer funding options, and same-currency one-time line items. A sufficient pre-existing balance can redirect to `success_url` after immediate success; otherwise the customer sees `hosted_instructions_url` and must still transfer funds. Monitor delayed status via webhooks. These hosted-flow facts do not establish how the November index's Elements Checkout Sessions variant works. See raw lines 950–1000, 1002–1189, 1196–1205.

**Environment and limits.** Dashboard instruction emails are optional; in a sandbox, they go only to addresses linked to the Stripe account. The `fund_cash_balance` API/Dashboard/CLI examples simulate funds for testing, not a live payment. The older Direct API section distinguishes unique live customer bank details from invalid test details that may not be unique. The May 5 guide also documents a method-specific temporary `payment_method_rate_limit_exceeded` error. See raw lines 711–720, 798–806, 930–938, 1207–1224, 1700–1704, 2030–2036, 2118–2126.

## Related

- [[stripe-bank-transfers]] — provider concept and bank-transfer source routes.
- [[stripe-checkout]] — Checkout Session context; the hosted bank-transfer flow above is dated May 5.

## Related raw API references

- [[raw/stripe-payments-bank-transfers-accept-a-payment-2026-11-07|November 7, 2026 variant index]] — navigation only: Elements Payment Intents API, Elements Checkout Sessions API, Checkout, and Direct API links. Linked variant content was not captured here.

## Raw Sources

- [[raw/stripe-bank-transfers-accept-payment-2025|May 5, 2026 full guide]] — detailed Elements PaymentIntent, hosted Checkout, and Direct API variants; 2,180 lines.
