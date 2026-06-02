---
title: "Stripe: Accept a Boleto Payment"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-boleto-accept-payment-2025.md"
tags: [stripe, vouchers, boleto, brazil, brl, checkout, elements, direct-api, webhooks, expires-after-days]
---

## Summary

Integration guide for Boleto via Checkout, Checkout Sessions API, Payment Intents API, and Direct API. Customer redirects to `hosted_voucher_url` (not `success_url`). Configurable expiry (0–60 days). `stripe.confirmBoletoPayment()` for Direct API. Payment confirmed next business day (Mon–Fri, excl. Brazilian holidays).

## Key Details

**Four integration paths**: Checkout, Checkout Sessions API (Elements), Payment Intents API (Elements), Direct API.

**Checkout**: Subscription mode Yes. Customer redirected to `hosted_voucher_url` after form submission (not `success_url`). Three async webhook events:
- `checkout.session.completed` → voucher generated (send `hosted_voucher_url` to customer)
- `checkout.session.async_payment_succeeded` → customer paid; fulfill order
- `checkout.session.async_payment_failed` → voucher expired; contact customer for new order

**`expires_after_days`**: `payment_method_options.boleto.expires_after_days`. Range: 0–60 days. Default: 3. Expiry at 23:59 America/Sao_Paulo (UTC-3). Configurable per-account in Dashboard.

**Voucher customization**: branding (icon, accent color, brand color) from Dashboard Branding Settings.

**Payment instruction emails**: opt-in via Dashboard Email Settings — Stripe sends Boleto number + hosted voucher link on PaymentIntent confirmation.

**Direct API**: `stripe.confirmBoletoPayment()` — Boleto-specific method. `payment_intent.succeeded` fires next business day (Mon–Fri, excluding Brazilian holidays). `next_action.boleto_display_details` contains `hosted_voucher_url` and `expires_at`.

**Tax ID test values**: CPF `000.000.000-00`, CNPJ `00.000.000/0000-00`.

**Test email scenarios**: any email (3-min delay), `*succeed_immediately@*`, `*expire_immediately@*`, `*expire_with_delay@*`, `*fill_never@*`.

## Raw Sources

- [[stripe-boleto-accept-payment-2025]] — verbatim webpage content (1,625 lines); fixed `*Customers*` ×2, `*Prices*` ×1, `*webhook*` ×3, `*fulfillment*` ×1, `*sandbox*` ×3, `*PaymentIntent*` ×2, `*client secret*` ×3, `*confirm*` ×1
