---
title: "Cash Vouchers (Stripe)"
type: concept
category: technology
tags: [stripe, vouchers, boleto, konbini, multibanco, oxxo, cash, in-person, brazil, japan, portugal, mexico]
---

## Definition

Cash voucher payment methods let customers complete online purchases in-person at authorized locations (convenience stores, ATMs, banks). Customers receive a digital voucher code after checkout and pay with cash at a physical location. Stripe supports four voucher methods.

## Supported Methods

| Method | API enum | Country | Currency | Subscriptions | Invoicing | SetupIntents |
| --- | --- | --- | --- | --- | --- | --- |
| Boleto | `boleto` | Brazil | BRL | Yes | Yes | Yes |
| Konbini | `konbini` | Japan | JPY | send_invoice only | send_invoice only | No |
| Multibanco | `multibanco` | Portugal | EUR | send_invoice only | send_invoice only | No |
| OXXO | `oxxo` | Mexico | MXN | No | No | No |

**No manual capture. No redirect required.** All use PaymentIntents.

## Payment Flow

1. Customer selects voucher payment at checkout
2. Customer receives digital voucher with reference code (email or app)
3. Customer pays in-person with cash at authorized location (convenience store, ATM, bank)
4. Merchant receives payment notification (up to 1 business day)

## Use Cases and Limitations

**Best for**: customers without cards or bank accounts; markets with low card authorization rates (e.g., Mexico).

**Not suitable for**: immediate delivery businesses (1 business day confirmation lag); businesses requiring refunds (not all methods support them).

## Connect Notes

- Boleto, Multibanco, OXXO: standard Connect support
- Konbini Connect: requires invite to create charges on behalf of other accounts

## Boleto Details

**Regulated by Central Bank of Brazil**. BR merchants only. BRL only.

**Confirmation**: 1 business day. **Payout**: T+2 business days after confirmation.

**Amount limits**: 5.00 – 49,999.99 BRL.

**No refunds** — must create separate process. **No customer disputes** (bank irregularities handled by Stripe).

**Recurring**: full subscriptions + invoicing (not `send_invoice`-only). SetupIntents, setup_future_usage, and Customer Portal all supported.

**Integration**: 4 paths (Checkout, Checkout Sessions API, Payment Intents API, Direct API). Checkout: customer redirected to `hosted_voucher_url` (not `success_url`). Three async Checkout webhook events: `checkout.session.completed`, `checkout.session.async_payment_succeeded`, `checkout.session.async_payment_failed`. `expires_after_days`: 0–60 days (default 3), in `payment_method_options.boleto`. Expiry at 23:59 America/Sao_Paulo. Direct API: `stripe.confirmBoletoPayment()`; `payment_intent.succeeded` fires next business day Mon–Fri excl. Brazilian holidays.

**Subscriptions and invoices**: both `send_invoice` and `charge_automatically` supported (unique among vouchers). `charge_automatically` requires name, Brazilian address, and tax ID as default payment method on Customer; Boleto emailed automatically each cycle. `send_invoice` has customer re-enter details each cycle; invoice must have due date. **Important**: even with `charge_automatically`, Boleto is never a true auto-debit — customer must still actively pay the voucher (Stripe emails a payment link).

## Konbini Details

**Japan-only** cash voucher, JPY only, JP merchants only. Pay at FamilyMart, Lawson, Ministop, Seicomart.

**Instant payment confirmation**. **Payout**: T+4 business days.

**Amount limits**: 120 JPY – 300,000 JPY.

**Refunds**: Yes — customer provides bank account info; Stripe emails to request, then auto-processes.

**Billing**: `send_invoice` only (no `charge_automatically`).

**Connect**: partial — requires invite for `on_behalf_of`. No Customer Portal.

**Integration**: Checkout and Direct API (no Elements). Checkout: `hosted_voucher_url` redirect (not `success_url`), same 3 async webhook events as Boleto. `expires_after_days`: 1–60 days, default 3, expiry at 23:59:59 JST. `expires_at` (Unix timestamp) mutually exclusive with `expires_after_days`. `product_description`: up to 22 Shift JIS chars shown at kiosk. `confirmation_number`: 10–11 digits (commonly customer phone); all-zeros blocked; if too common → rejected. Direct API: `stripe.confirmKonbiniPayment()`; `next_action.konbini_display_details` has per-store `payment_code` + `confirmation_number`. Expiration buffer prevents premature failures. Refund: customer provides bank account → 45-day timeout → failed.

**Prohibited categories** (19+): sole proprietors under 3 years, RMT, gambling, money-making/investment info, gambling strategies, MLM/pyramid schemes, gore, unscientific content, prohibited medical products, public order offenses, import facilitation, foreign money transfer, loans, dating sites, e-cigarettes/vaping, fortune-telling. Financial partner and convenience stores may also reject at discretion.

## Multibanco Details

**Portugal customers only, EUR only**. 33 merchant countries (Europe + US, includes Gibraltar).

**Two flows**: online banking (entity + reference → log in → pay) and ATM (entity + reference → pay at ATM).

**Confirmation delay**: several days, especially over weekends (bank transfer-based; unlike Konbini's instant confirmation).

**Amount limits**: €0.50 – €99,999.

**Refunds**: **365-day** window. Typically 1 day to customer. `destination_details.multibanco.reference` provides refund identifier.

**No disputes** (customer pushes funds).

**Billing**: `send_invoice` only. No recurring. Capability: `multibanco_payments`.

**Connect**: Direct, Destination, Separate charges and transfers (standard, no invite required).

**Integration**: Checkout, Direct API, iOS/Android SDK. `hosted_voucher_url` redirect. 7-day voucher expiry → `processing` (4-day bank transfer buffer) → `requires_payment_method`. If funds arrive after buffer → Stripe auto-refunds. `stripe.confirmMultibancoPayment()` for web Direct API; email only required. `next_action.multibanco_display_details`: `entity`, `reference`, `expires_at`, `hosted_voucher_url`.

## OXXO Details

**Mexico-only** cash voucher, MXN only, MX merchants only. OXXO convenience stores only.

**Payment confirmation**: next business day (with settled funds).

**Amount limits**: 10.00 – 10,000.00 MXN (lowest ceiling of all 4 vouchers).

**No refunds**. **No disputes**. **No subscriptions or invoicing** (most limited of the 4 vouchers).

**Connect**: Yes (standard, no invite required).

**Integration**: Checkout, Checkout Sessions API, Payment Intents API, Direct API, iOS, Android. `hosted_voucher_url` redirect. `expires_after_days`: 1–7 days (default 3), expiry at 23:59 America/Mexico_City. `stripe.confirmOxxoPayment()` for web Direct API; email only required. `next_action.oxxo_display_details.expires_after` (note: `expires_after`, not `expires_at` as with Multibanco/Konbini).

**Unsupported categories** (4): Direct Marketing - Other, Direct Marketing - Subscription, Gift/Card/Novelty/Souvenir Shops, Service Stations.

## Sources

- [[source-stripe-vouchers]] — hub page: 4 methods, product/API support matrices
- [[source-stripe-boleto]] — Boleto: Brazil cash voucher, no refunds, 1-day confirmation, T+2 payout, 5–49,999.99 BRL
- [[source-stripe-boleto-accept-payment]] — Boleto integration: 4 paths, hosted_voucher_url, expires_after_days, confirmBoletoPayment(), next-biz-day webhook
- [[source-stripe-boleto-subscription]] — Boleto subscriptions: both send_invoice + charge_automatically, tax ID required for auto-charge, setup flow
- [[source-stripe-boleto-invoices]] — Boleto invoices: same collection method logic, auto_advance, charge_automatically still requires customer to pay voucher
- [[source-stripe-konbini]] — Konbini: Japan cash voucher, instant confirmation, T+4 payout, 120–300k JPY, 19+ prohibited categories
- [[source-stripe-konbini-accept-payment]] — Konbini integration: Checkout + Direct API, confirmKonbiniPayment(), confirmation_number, product_description, expires_after_days
- [[source-stripe-multibanco]] — Multibanco: Portugal voucher, 2 flows (online/ATM), delayed confirmation, 365-day refunds, send_invoice only
- [[source-stripe-multibanco-accept-payment]] — Multibanco integration: 3 paths + mobile, 7-day expiry + 4-day buffer, confirmMultibancoPayment(), entity+reference
- [[source-stripe-oxxo]] — OXXO: Mexico cash voucher, next-biz-day confirmation, 10–10k MXN, no refunds, no subscriptions, 4 prohibited categories
- [[source-stripe-oxxo-accept-payment]] — OXXO integration: 4 paths + mobile, confirmOxxoPayment(), expires_after (not expires_at), 1–7 day expiry
