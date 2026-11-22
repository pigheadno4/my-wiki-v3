---
title: "Stripe: Accept Meses Sin Intereses Card Payments"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/meses-sin-intereses/accept-a-payment"
raw_files:
  - "stripe-mx-installments-accept-payment-2025.md"
tags: [stripe, mexico, installments, meses-sin-intereses, checkout, payment-element, payment-intents, invoices, payment-links]
---

## Summary

The May 1, 2026 guide covers Checkout, Payment Element, Direct API, Invoices and no-code Payment Links. Mexican consumer credit card customers pay across billing statements. The issuer collects the installments, and the merchant receives payment on the ordinary card payout schedule with fees deducted. Installments add a fee to the standard credit card fee. The separate Mexico overview documents eligibility for Stripe Mexico accounts, MXN transactions and supported Mexican-issued consumer credit cards, subject to issuer support and plan-specific amounts (May integration raw lines 16–22). [[source-stripe-mx-installments]]

## Key Integration Details

### Checkout

With dynamic payment methods, installments appear when eligible. For manual configuration, the May Checkout Sessions example enables `payment_method_options.card.installments.enabled`. This route supports Checkout `payment` mode only. The sample redirects customers to the Checkout Session URL (May raw lines 24–77).

### Payment Element

The May Elements guide also lets eligible installments appear with dynamic payment methods. Its manual PaymentIntent example sets `payment_method_options.card.installments.enabled` to `true`. With dynamic methods, leave that parameter unset. The guide warns that setting it to `false` can cause errors. The browser initializes Elements with the PaymentIntent client secret and calls `confirmPayment` with a `return_url`. The guide says `processing_error` and `transaction_not_allowed` may indicate the issuer does not support the selected plan. It directs the customer to retry with a different plan or without installments (May raw lines 78–133).

### Direct API

1. The browser collects card details with Stripe.js and Elements and creates a card `PaymentMethod`. The May sample loads `https://js.stripe.com/dahlia/stripe.js` directly from Stripe and sends the PaymentMethod ID to the server (May raw lines 138–208).
2. The server creates an MXN `PaymentIntent` with that ID and installments enabled, leaving it unconfirmed during plan lookup. It sends the intent ID and `payment_method_options.card.installments.available_plans` to the client (May raw lines 210–261).
3. The customer chooses an available plan or immediate payment. The client sends that choice and the intent ID, then the server confirms the same intent. The sample endpoint returns `success: true` alongside the actual intent status when the confirmation call returns. The sample UI treats only `succeeded` as payment success (May raw lines 314–436).

A plan persists on the intent until cleared. When reconfirming without installments, explicitly unset `payment_method_options[card][installments][plan]`, including when a customer switches to a card that does not support installments. Plan availability, plan selection and a confirmation response are distinct from a successful payment. A Checkout return alone does not establish payment success (May raw lines 68–70 and 370–497).

### Invoices

The May guide enables installments for individual invoices using `collection_method: 'send_invoice'`. It excludes subscriptions and automatic invoice collection. The server examples first create an `InvoiceItem` with the Price in `pricing.price`, then separately create an `Invoice` that includes pending invoice items with `pending_invoice_items_behavior: 'include'` and enables card installments in `payment_settings`. Both calls use `customer_account` for a customer-configured Accounts v2 Account or `customer` for a Customers v1 Customer. May describes Accounts v2 as generally available for Connect users and in public preview for other Stripe users, with a preview API version required for participants (May raw lines 8–14 and 511–610).

On the hosted invoice page the card must support installments and the total must be at least 300 MXN for plans to appear. Which plans appear depends on the issuer, transaction and plan settings. The May Dashboard workflow enables cards and **Allow payment with card installments** for the invoice (May raw lines 612–622 and 695–724).

### Payment Links and Dashboard Settings

The May no-code path enables installments for Payment Links in Dashboard payment method settings. Those settings also control enablement for no-code Checkout. The Dashboard lets the merchant select monthly plans and configure per-plan minimum and maximum amounts across compatible existing installments integrations (May raw lines 695–701 and 725–750).

## API Version Notes for Plan Lookups

- The historical May Direct API and Invoicing response examples show selected plans under `PaymentIntent.charges.data` and on the PaymentIntent. The API version change dated `2022-11-15` removes `PaymentIntent.charges` and instructs integrations to use `latest_charge` for the most recent charge (May raw lines 443–489 and 624–693). [PaymentIntent changelog](https://docs.stripe.com/changelog/2022-11-15/removes-charges-attribute-paymentintent)
- The May Invoicing sample retrieves a PaymentIntent ID directly from the Invoice after payment. The separate `2025-03-31.basil` change removes `Invoice.payment_intent` and documents the Invoice Payment relationship. An invoice can have multiple payments. The changelog shows inspection of `invoice.payments` and expansion of `payments.data.payment.payment_intent` for Stripe payments of that type (May raw lines 624–693). [Invoicing changelog](https://docs.stripe.com/changelog/basil/2025-03-31/add-support-for-multiple-partial-payments-on-invoices)

The separate May and November Mexico product overviews list recurring payments as **Yes**. The overviews leave recurring implementation and eligibility unspecified. The May limits on Checkout mode and individual invoices still apply. [[source-stripe-mx-installments]]

## May Sandbox Test Cards

| Number | Test result |
| --- | --- |
| 4000004840000008 | Offers 3, 6, 9, 12, 18 and 24 months |
| 4242424242424242 | Offers no installment plans |

The test examples cover plan display in the sandbox (May raw lines 751–758).

## Related Pages

- [[stripe]]
- [[stripe-installments]] — installment products and market scope
- [[source-stripe-mx-installments]] — Mexico eligibility, plan thresholds and fees

## Raw Sources

- [[raw/stripe-mx-installments-accept-payment-2025|May 1, 2026 Mexico installments integration guide]] — Checkout, Elements, Direct API, Invoices, Payment Links, settings and test cards.

## Related raw API references

- [[raw/stripe-payments-meses-sin-intereses-accept-a-payment-2026-11-07|November 7, 2026 integration variant index]] — navigation to Checkout, Elements, Direct API, Invoices, No code (Payment Links) and Terminal. The Terminal implementation body was outside the capture.
