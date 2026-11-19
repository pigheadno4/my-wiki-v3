---
title: "Stripe: Boleto Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
canonical_url: "https://docs.stripe.com/payments/boleto"
original_format: webpage
raw_files:
  - "stripe-payments-boleto-2026-11-07.md"
  - "stripe-boleto-2025.md"
tags: [stripe, vouchers, boleto, brazil, brl, cash, recurring, connect, subscriptions]
---

## Summary

[[stripe]] describes Boleto as a reusable, regulated Brazil voucher method. A Brazil merchant or Connect platform gives a Brazil customer a BRL voucher, and the customer pays it before expiry at a bank, authorized agency, ATM or online bank portal. Voucher generation, method access, subscription creation and invoice finalization are not payment confirmation. Stripe confirms after payment asynchronously; settlement and payout availability have separately dated descriptions.

## Eligibility, amount and timing

The 2026-11-07 overview lists Brazil merchant/platform and customer locations, BRL presentment, domestic coverage only, B2B and B2C, and **BRL 5.00–49,999.99** per transaction. It says there is no Boleto-specific MCC requirement, but the website must satisfy Stripe account activation requirements. Access is labeled **instant provisional** and Stripe may review eligibility after activation; neither label establishes account-specific approval or paid funds.

The November page labels payment confirmation **up to one business day** and settlement **up to two business days (T+2)** without explicitly giving the new settlement clock's starting event. Its flow says confirmation typically comes on the next business day after customer payment. The earlier **2026-05-07** capture instead says confirmation after one business day and **funds available for payout two business days after confirmation**. Preserve these as dated timing labels: settlement, payout availability and bank payout arrival are not interchangeable.

## Voucher and payment flow

The customer selects Boleto and supplies contact and tax ID details. Stripe hosts a voucher page with a number the customer can copy or a PDF to download. Voucher expiry defaults to **three days** and is configurable from **0–60 days**. Desktop and mobile use the same browser-hosted voucher flow. A customer pays through an authorized channel; only subsequent asynchronous confirmation establishes successful payment. A visible voucher or browser return is not success.

Use `payment_intent.next_action.boleto_display_details.number` for the customer-visible voucher number. It identifies the voucher, **not** a processor transaction ID. The overview says no processor transaction ID appears under `latest_charge.payment_method_details.boleto`.

## Capabilities and product support

The November matrix supports recurring payments, Billing, Invoicing, Customer Portal, Connect, SetupIntents, PaymentIntents with `setup_future_usage`, Checkout Sessions/PaymentIntents, full-page and embedded Checkout, Payment Links and Payment Element. It explicitly marks **off-session payments unsupported**. Manual, partial, multi- and over-capture, authorization extensions, standard full/partial refunds and standard full/partial disputes are unsupported. The matrix also excludes Managed Payments, Radar, Terminal, Express Checkout Element, Payment Method Messaging Element and in-app payments.

**Recurring is not automatic debit:** a dated May subscription guide shows a `Subscription` creation request with `collection_method: "charge_automatically"` and `off_session: true`; that is a request example, not proof of an accepted or successful off-session Boleto payment. The May invoice guide says even `charge_automatically` requires the customer to pay each emailed voucher. The November overview's no-off-session matrix qualifies the payment behavior but does not by itself prove the older Subscription request is invalid. Keep Subscription creation, invoice collection and customer voucher payment as separate actions. See [[source-stripe-boleto-subscription]] and [[source-stripe-boleto-invoices]] for dated setup details.

## Refunds and disputes

Stripe Boleto **full and partial refund capability is unsupported**. The May page advises a separate process to credit customers needing a refund; this does not mean all remediation is impossible. Boleto has no standard customer dispute or chargeback process, but bank-side mishandling can cause similar irregularities. In that case, Stripe **contacts the merchant with next steps**; neither capture promises Stripe will resolve the issue without merchant action.

## Descriptor and Connect identity

For Boleto and other non-card payments, a request-level `statement_descriptor` sets the full descriptor, falling back to the account-level value when omitted; `statement_descriptor_suffix` applies only to cards. A bank or payment channel may display or omit descriptor details and may show Stripe on the voucher or receipt. For Connect destination charges without `on_behalf_of`, the platform account supplies the descriptor; with `on_behalf_of`, the connected account supplies it, subject to legacy API-version behavior. The broad Connect checkmark does not prove a particular account's eligibility or statement display.

## Related

- [[stripe]] — Stripe company page.
- [[stripe-vouchers]] — voucher-method concept.
- [[source-stripe-boleto-accept-payment]] — integration-specific webhook and voucher details.
- [[source-stripe-boleto-subscription]] — dated subscription request example.
- [[source-stripe-boleto-invoices]] — dated invoice collection and customer-payment behavior.

## Raw Sources

- [[raw/stripe-payments-boleto-2026-11-07]] — full webpage capture fetched 2026-11-07 (142 lines).
- [[raw/stripe-boleto-2025]] — earlier webpage capture fetched 2026-05-07 (116 lines); no italic fixes; four SVG flow diagrams downloaded to assets/.
