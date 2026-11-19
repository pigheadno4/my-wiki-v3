---
title: "Stripe: Accept Installment Card Payments (Japan)"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/jp-installments/accept-a-payment"
raw_files:
  - "stripe-jp-installments-accept-payment-2025.md"
tags: [stripe, japan, installments, checkout, payment-element, payment-intents, invoices, payment-links]
---

## Summary and evidence boundary

The full guide captured **2026-05-01** describes Japan installment card payments through Checkout, Payment Element, Direct Payment Intents API, Invoices, and Payment Links, with sandbox card examples. It points to separate Japan installment compatibility requirements; see [[stripe-jp-installments]] and [[source-stripe-jp-installments]] for the dated JP account, card, currency, plan, and bonus-window context.

The **2026-11-07** canonical capture at this URL is a variant index with links for Checkout, Elements, Direct API, Invoices, and No code/Payment Links. It provides no implementation parameters, eligibility, test-card behavior, or payment outcome. The instructions below remain attributed to the May full guide; the November index does not establish that any variant was removed, changed, or currently available to a particular account.

## Checkout and Payment Element — May 2026 guide

- **Checkout:** For dynamic payment methods, the May guide says installments appear automatically. Otherwise its server Checkout Session example sets `payment_method_options.card.installments.enabled: true`. Installments are for Session `payment` mode, not `setup` or `subscription`. Creating the Session and redirecting to its URL are steps in checkout, not payment-success evidence.
- **Payment Element:** The same dynamic-method distinction applies when creating the server PaymentIntent: installments appear automatically with dynamic payment methods, so **omit** `payment_method_options[card][installments][enabled]` entirely. With a non-dynamic configuration, the example sets it to `true`. Setting it to `false` with dynamic methods may cause errors. Return the PaymentIntent client secret to the browser, initialize Elements, and use `confirmPayment` with the Payment Element and a `return_url`. A `processing_error` or `transaction_not_allowed` decline may mean the issuer does not support the selected plan; the guide says to retry with another plan or without installments.

## Direct API — May 2026 guide

1. Collect card details in browser Stripe.js and a Card Element, then create a PaymentMethod with the publishable key; load Stripe.js directly from `js.stripe.com`.
2. Send the PaymentMethod ID to the server. Create a JPY PaymentIntent with the card installment option enabled for this Direct API example, but **do not confirm it yet**; return its ID and `payment_method_options.card.installments.available_plans` for this card. The example's plan counts are illustrative, not a guarantee for every issuer or card.
3. Let the customer choose a returned plan or immediate payment on the client and send that selection to the server.
4. Confirm the PaymentIntent on the server with the selected `payment_method_options.card.installments.plan`, and inspect the returned status. After a plan is set, it persists until explicitly unset. If a card with an installment plan declines and the customer retries with a card without installments, explicitly unset the plan when confirming again.

Plan availability, selection, or a confirmation request does not establish a successful charge. The May example displays a success message only for a returned `succeeded` status.

## Invoices and Payment Links — May 2026 guide

- **Invoices:** Installments apply to individual invoices, not subscriptions. The guide requires `collection_method: 'send_invoice'`, not `charge_automatically`. An API example uses `customer_account` for a customer-configured Account or `customer` for a Customer, with a Price and card installments enabled in invoice payment settings. The customer chooses a plan on the hosted invoice page; after payment, the guide retrieves the Invoice's PaymentIntent to inspect the selected plan. Invoice creation or delivery alone is not payment.
- **Payment Links:** The May guide says installments can be enabled or disabled in Dashboard payment-method settings and are enabled by default for that route. This is dated guide text, not a fresh November settings check.

## Sandbox examples — May 2026 guide

| Brand | Success test card | Failure test card |
| --- | --- | --- |
| Visa | `4000003920000003` | `4000003920000029` (`card_declined`) |
| Mastercard | `5200003920000008` | — |
| JCB | `3530111333300000` | — |
| Diners | `36000039200009` | — |

PaymentMethod examples: `pm_card_jp`, `pm_card_jp_mastercard`, `pm_card_jcb`, `pm_card_jp_diners`, and declined `pm_card_jp_visa_installmentsDeclined`. The declined Visa example can return available plans before the issuer declines the transaction; plan availability is not authorization.

## Related Pages

- [[stripe]] — company overview
- [[stripe-jp-installments]] — Japan requirements, brand support, and bonus windows
- [[stripe-installments]] — wider installments family
- [[source-stripe-jp-installments]] — dated Japan installment properties and eligibility

## Raw Sources

- [[raw/stripe-jp-installments-accept-payment-2025|Full multi-variant guide captured 2026-05-01]]

## Related raw API references

- [[raw/stripe-payments-jp-installments-accept-a-payment-2026-11-07|Canonical variant-navigation index captured 2026-11-07]] — links to Checkout, Elements, Direct API, Invoices, and No code/Payment Links; no variant implementation behavior is established by this index.
