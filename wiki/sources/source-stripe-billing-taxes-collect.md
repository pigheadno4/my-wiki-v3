---
title: "Stripe Billing — Collect Taxes for Recurring Payments"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/taxes/collect-taxes"
raw_files:
  - "stripe-billing-taxes-collect-2026.md"
tags: [stripe, billing, subscriptions, tax, stripe-tax, tax-rates, invoices, automatic-tax]
---

## Overview

The 2026-05-13 capture of this Stripe Billing guide contains two complete variants for recurring-payment tax collection: Stripe Tax, an automated paid product, and manually defined Tax Rates, a free feature. It also names native third-party tax integrations including Avalara, Anrok, and Sphere. All mechanics below are **dated May 2026 guidance**, not behavior reverified by the 2026-11-07 same-URL capture. The November capture is a short index linking to the Stripe Tax and Tax Rates variants; those variant URLs were not read for this update.

## Stripe Tax — Customer v1 subscription flow in the May capture

1. **Estimate on the server.** Before an address is available, preview an invoice with `automatic_tax.enabled=true` and `customer_details.tax.ip_address`. Stripe cautions that IP geolocation is only an initial estimate. After address collection, preview using the customer's address or shipping details, check `automatic_tax.status`, and request correction when it is `requires_location_inputs`. A zero tax amount also calls for checking registration and possible zero-tax rules. See May lines 28–102.
2. **Collect on the client without an Intent.** The captured flow creates Elements with `mode: 'subscription'`, currency and the estimated invoice total, then mounts Address Element and Payment Element. Address changes trigger a server re-estimate and `elements.update({ amount: total })`; throttle changes to avoid excessive requests. On submission, await `elements.submit()`, save customer details on the server, create the subscription on the server, then confirm the first-invoice PaymentIntent on the client with `stripe.confirmPayment()` when that payment path applies. See May lines 104–185.
3. **Validate the Customer location on the server.** The Customer v1 example sets an address and `tax.validate_location='immediately'`; invalid location can return `customer_tax_location_invalid`. Updating an existing Customer's address can change tax and totals on other automatic-tax subscriptions' future invoices. See May lines 188–245.
4. **Create the subscription on the server.** The May Node example sets `automatic_tax.enabled=true`, `customer`, `items`, `payment_settings.save_default_payment_method='on_subscription'`, and expands `latest_invoice.confirmation_secret`. It **does not** set `payment_behavior`. The following prose says an existing default payment method can pay the first invoice automatically; if the checkout should instead use newly collected payment details, pass `payment_behavior='default_incomplete'` so the first invoice is not paid automatically, then confirm its PaymentIntent. Check `latest_invoice.status`; no payment success is established by the sample. Pass the confirmation client secret only to that customer over TLS; do not store, log or expose it to others. See May lines 246–278.
5. **Handle tax and invoice exceptions.** The May guide says product tax code and tax behavior inform calculation, with a Tax Settings default if omitted (lines 280–284). On `invoice.finalization_failed` with `automatic_tax.status=requires_location_inputs`, Stripe cannot calculate tax, finalize the invoice or collect payment until the customer supplies a valid location (lines 405–411). Its refund path uses Credit Notes to record tax-liability changes; `refund_amount` creates an accompanying refund, while an existing manual refund is passed through `refunds` without `refund_amount`. Preview a line-item Credit Note before issuing a line-item refund (lines 286–403).

## Tax Rates — manual route in the May capture

- A subscription may have `default_tax_rates`; item-level `tax_rates` override the subscription default for that item. The May guide allows up to five rates per subscription item (lines 413–460).
- For changing rates on renewal, the May guide describes handling `invoice.created` and editing the draft renewal invoice during an approximately one-hour window before finalization or attempted payment/email (lines 463–469).
- Checkout examples use fixed `subscription_data.default_tax_rates` or `line_items.tax_rates`, or location-matched `line_items.dynamic_tax_rates`. The dynamic path prioritizes shipping address over billing address, then country where applicable; if no supplied rate matches, no rate is applied. The guide says fixed default/item rates cannot be combined with dynamic item rates (lines 471–559).

## Related

- [[stripe-tax]] — Stripe Tax and manual tax concepts.
- [[stripe-subscriptions]] — subscription payment and invoice context.
- [[stripe]] — Stripe provider.
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — separately sourced Metronome-created Stripe invoice tax mapping.

## Raw Sources

- [[raw/stripe-billing-taxes-collect-2026|Stripe recurring-payment tax guide, 2026-05-13]] — fully captured Stripe Tax and Tax Rates variants; factual evidence for this entry.

## Related raw API references

- [[raw/stripe-billing-taxes-collect-taxes-2026-11-07|Stripe recurring-payment tax variant index, 2026-11-07]] — navigation only; links to `?tax-calculation=stripe-tax` and `?tax-calculation=tax-rates` variants without their instructions.
