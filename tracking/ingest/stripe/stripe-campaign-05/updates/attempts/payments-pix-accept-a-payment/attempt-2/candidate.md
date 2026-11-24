---
title: "Stripe: Accept a Pix One-Time Payment"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/pix/accept-a-payment"
raw_files:
  - "stripe-pix-accept-payment-2025.md"
tags: [stripe, real-time-payments, pix, brazil, brl, checkout, elements, direct-api, tax-id, cpf, cnpj]
---

## Overview

The May 6, 2026 acceptance guide covers Checkout, Elements with PaymentIntents, and Direct API. Customers in Brazil use their bank app to scan a QR code or paste a Pix string. The November 7, 2026 capture links to the same three variants.

## One-time payment paths

- **Checkout**. The May compatibility table lists BR, US, EU, CA, GB, AU, SG and CH as business locations for payments from customers in Brazil. The May guide requires all line-item Prices in BRL and one-time line items for one-time Pix. It distinguishes dynamic selection from manual configuration, where the examples include `pix` in `payment_method_types`. The hosted example uses `success_url` and the embedded example uses `return_url`. The setup and recurring subscription route is [[source-stripe-pix-automatico|Pix Automático]].
- **Elements**. The May guide creates the PaymentIntent on the merchant server, passes the client secret to Stripe.js and uses `confirmPayment`. Its server examples distinguish Accounts v2's `customer_account` from Customers v1's `customer`. The guide says Elements collects CPF/CNPJ for cross-border transactions whether confirmation is on the client or server.
- **Direct API**. The merchant server creates the PaymentIntent and passes its client secret to the browser. The May browser example calls Stripe.js `confirmPixPayment` with that secret and a `return_url` to display the QR code and redirect the customer after they complete payment. Its HTML form collects name, email and CPF for individuals or CNPJ for businesses under `payment_method.billing_details`. It describes the government tax-ID requirement for cross-border transactions. To display the Pix string or QR code yourself, the May guide uses `handleActions: false` and `next_action.pix_display_qr_code`.

The May Elements guide uses `payment_intent.succeeded` for fulfillment after payment. The Direct API return page checks the retrieved PaymentIntent status. Rendering or scanning instructions and a browser return do not establish payment success. The May guide’s live flow requires a Brazilian bank account with Pix enabled.

## May 2026 expiration by path

| Path | Documented behavior |
| --- | --- |
| Checkout | `payment_method_options.pix.expires_after_seconds` can be 10 to 1,209,600 seconds (14 days). The default is 14,400 seconds (4 hours). |
| Elements | The guide says the QR code expires 4 hours after creation. Stripe then sends `payment_intent.payment_failed`. |
| Direct API | Use `expires_after_seconds` for 10 to 259,200 seconds (3 days) from PaymentIntent confirmation, or an `expires_at` Unix timestamp 10 seconds to 3 days ahead. Setting both causes an error. If neither is set, expiry defaults to 4 hours from confirmation. |

The Direct API guide says `next_action` can echo the requested `expires_at` even when actual expiry differs. Use `payment_intent.payment_failed` to identify expiry. Customers cannot pay an expired code. The merchant can confirm with another payment method or cancel the Intent after expiry, or cancel the Intent before expiry.

## Testing and troubleshooting

The May guide documents a sandbox tax ID (`000.000.000-00`) and a hosted **Simulate scan** test page. The ordinary delayed-success, `succeed_immediately`, `expire_immediately` and `expire_with_delay` email patterns ignore configured expiry. The `fill_never` pattern follows the expiry configuration and generates `payment_intent.payment_failed`. See each variant’s **Test your integration** section and the May Elements **Error codes** table for exact inputs, responses and recommended actions.

## Related

- [[stripe-real-time-payments]] — Stripe real-time payment methods, including Pix
- [[stripe-pix]] — Pix and its separate mandate-based subscription flows
- [[source-stripe-pix]] — Pix payment method and availability
- [[source-stripe-pix-automatico]] — Pix Automático recurring payments
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-pix-accept-payment-2025|May 6, 2026 Pix one-time acceptance guide]] — full Checkout, Elements and Direct API capture.

## Related raw API references

- [[raw/stripe-payments-pix-accept-a-payment-2026-11-07|November 7, 2026 acceptance variant index]] — navigation to Checkout, Elements and Direct API.
