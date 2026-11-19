---
title: "Real-Time Payments (Stripe)"
type: concept
category: technology
tags: [stripe, real-time-payments, paynow, payto, promptpay, swish, pay-by-bank, pix, open-banking, instant-transfer]
---

## Definition

Real-time payment methods let customers directly transfer money from their bank account or alternate funding source. Stripe supports real-time payments across multiple regions.

> Note: The real-time payments hub page ([[source-stripe-real-time-payments]]) listed "Pay by Bank" as a Brazil method — this was an error. Brazil's real-time payment method is **Pix** (`pix`), confirmed by the Pix product page ([[source-stripe-pix]]). The hub page Brazil entry has been removed from the table above.

## Supported Methods

| Method | API enum | Customer region | Redirect | SetupIntents | setup_future_usage | Mobile |
| --- | --- | --- | --- | --- | --- | --- |
| Pay by Bank (UK/Europe) | `pay_by_bank` | UK, Finland, France, Germany, Ireland | Yes | No | No | No |
| PayNow | `paynow` | Singapore | No | No | No | Yes |
| PayTo | `payto` | Australia | No | Yes | Yes | No |
| Pix | `pix` | Brazil | No | No | No | Yes |
| PromptPay | `promptpay` | Thailand | No | No | No | Yes |
| Swish | `swish` | Sweden | Yes | No | No | Yes |
| UPI | `upi` | India | Yes (mobile) | Unknown | Unknown | Yes |

**No manual capture** for any real-time payment method.

## Key Differentiators

**PayTo** (Australia): unique among real-time methods — supports SetupIntents, `setup_future_usage`, and Express Checkout Element. Also supports disputes (final, non-appealable), mandate-based recurring, and Billing. Identity verification required to activate.

**PayNow** (Singapore): also supports Terminal.

**Redirect required**: Pay by Bank (UK/Europe) and Swish only.

**Subscriptions/Invoicing**: Pay by Bank, PayNow, PromptPay, and Swish support subscriptions/invoicing only via `send_invoice` (not `charge_automatically`). **Pix** supports automatic recurring via **Pix Automático** (mandate-based, charge_automatically). **PayTo** also lists Billing=Yes and Recurring=Yes — whether it supports `charge_automatically` requires verification against the PayTo accept-a-payment guide.

> [!info] Evolving
> PayTo's billing collection method (`send_invoice` vs `charge_automatically`) is unconfirmed. Verify against the PayTo accept-a-payment guide.

## Pix Details

**QR code or Pix string** real-time payment — Brazil customers only, BRL currency. Processed via **Ebanx** (Stripe's Brazil partner).

**Business locations**: 35 international merchant countries + BR (invite only, one-time only). Settlement currency varies by account country (BRL/USD/EUR/GBP/CAD/AUD/SGD).

**Transaction limits**: min 0.50 BRL, max 3,000 USD per payment. Single buyer cap: 10,000 USD/month per business.

**Refunds**: 90-day window. Reflected within minutes.

**Disputes**: Limited (fraud, account takeover). **Non-challengeable** — funds removed from Stripe balance automatically.

**IOF tax** (3.5% on international transactions): merchant chooses who pays via `amount_includes_iof` (`never` = customer pays, default; `always` = merchant absorbs). API users must display Ebanx T&C disclosures. Checkout/Elements handle disclosures automatically.

**Statement descriptor**: ignored — Ebanx shown as recipient; merchant name in `identifier` field only.

**Recurring**: via **Pix Automático** (separate sub-product with mandate-based authorization). Not available for BR accounts.

**Prohibited categories**: crypto businesses, insurance, telehealth/medicine, non-profits/charities.

**Connect**: MoR-sensitive. Capability: `pix_payments`.

**Integration**: Checkout, Elements, Direct API. Checkout supports setup mode and subscription mode (redirects to Pix Automático for recurring — unique among real-time methods). `expires_after_seconds` configurable (default 4 hours, max 14 days) via `payment_method_options.pix`. Tax ID (CPF/CNPJ) required by Brazilian law — Elements captures automatically; Direct API must collect explicitly.

**Save/recurring (Pix Automático)**: Checkout and Direct API only (no Elements). Requires `mandate_options` (`amount`, `payment_schedule`) in `payment_method_options.pix`. Direct API uses `stripe.confirmPixSetup()` (SetupIntent) or `stripe.confirmPixPayment()` (PaymentIntent + `setup_future_usage: off_session`). QR data exposed via `next_action.pix_display_qr_code` (`data`, `image_url_svg`, `image_url_png`, `expires_at`, `hosted_instructions_url`). Mandate revocation → `mandate.updated` event → bring customer back on-session.

**Pix Automático — recurring mechanics**: customer authorizes mandate (amount + billing cycle) in bank app. Bank sends **3-day pre-debit notification** before each charge — effective billing = schedule + 3 days. PaymentIntent in `processing` during this window; confirmation typically 3 days, up to 7 with retries. Retry on failure: once daily for 3 days. Daily `payment_schedule` prohibited — all payments fail. Default mandate `amount`: 400 BRL. Not available for BR merchant accounts. **Not available for BR-based merchant accounts** (international merchants only).

## PayTo Details

**Mandate-based** real-time payment — Australia customers only, AUD only, AU merchant accounts only. **Identity verification required** before activation.

**Payment flows**: PayID (unique identifier linked to bank account) or Account + BSB numbers. Customer receives push notification or email to authorize mandate in banking app.

**Delayed notification**: Stripe sends final status within 60 seconds of mandate authorization.

**Mandates** via `payment_method_options.payto.mandate_options`: `amount`, `amount_type` (`fixed` or `maximum`), `payment_schedule`, `purpose`, `start_date`, `end_date`, `payments_per_period`. One-off: Stripe auto-sets all fields. Recurring: merchant specifies least permissive terms.

**Bank limits**: Several major banks (ANZ, CBA, Westpac, Macquarie) reject mandates over 25,000 AUD and mandates with no maximum amount. Westpac additionally declines high-risk merchant ad-hoc payments over 1,000 AUD. Business account coverage is lower than consumer. 44 supported banks.

**Disputes**: Final and non-appealable. Stripe sends `charge.dispute.created` + `charge.dispute.closed` events.

**Refunds**: Up to 2 years. Typically minutes; some banks may take several days.

**Connect**: Direct, Destination, Separate charges and transfers. Capability: `payto_payments`.

## Pay by Bank (UK/Europe) Details

**Open banking** real-time payment — UK, Finland, France, Germany, Ireland. France/Germany/Ireland in **private preview**. EUR and GBP only.

**Transaction limits**: £0.50–£10,000 default. Higher amounts require contacting Stripe.

**No disputes** — customer authenticates in banking app; no chargeback process.

**Refunds**: **730-day (2-year)** window. Partial refunds supported. Free; processing fees non-refundable.

**Connect**: Yes — Direct, Destination, Separate charges and transfers. Capability: `pay_by_bank_payments`. 35 merchant countries (US, AU, SG, most of Europe).

**Product support**: Connect, Payment Links, Checkout (not subscription mode), Elements — Express Checkout Element and Mobile Payment Element **not** supported.

**Integration**: Checkout and Elements (PaymentIntents) paths only — no Direct API. Checkout requires `payment_method_options.pay_by_bank.statement_descriptor` (business name shown on customer's bank statement). Checkout business locations: DE and GB only (EU private preview). Test: "Authorize test payment" → success; "Fail test payment" → failure.

## PayNow Details

**QR code** real-time payment — Singapore customers only, SGD only. SG merchant accounts only. **1.3% pricing** (explicitly stated).

**Payout**: T+1 (funds available next day).

**Refunds**: **90-day** window. Asynchronous; `refund.updated`/`refund.failed` webhook events.

**QR code expiration**: 1 hour — error `payment_intent_payment_attempt_expired`. Must webhook customer back to create new PaymentIntent/QR code.

**Statement descriptor**: **cannot be customized** — `STRIPE PAYMENTS SINGAPORE PTE. LTD.` always shown.

**Duplicate protection**: QR code rejected after first successful use.

**No disputes** — QR authentication prevents chargebacks.

**Billing**: subscriptions and invoices via `send_invoice` only (no auto-charge). Also supports Terminal (in-person, must manually list).

**Prohibited categories**: Petroleum/Fuel Dealers/Service Stations/Automated Fuel Dispensers.

**Connect**: Direct, Destination, Separate charges and transfers. Capability: `paynow_payments`. Must set correct MCC for connected accounts.

**Integration**: Checkout and Direct API paths — no Elements path. Direct API uses `stripe.confirmPayNowPayment(clientSecret)` (PayNow-specific, not generic `confirmPayment`); renders QR code inline, no redirect. Page must stay open while customer scans; fulfillment via `payment_intent.succeeded` webhook.

## UPI Details

**QR code (desktop) / redirect (mobile)** real-time payment — India customers only, INR only. Developed by NPCI.

**Transaction limits**: 1 INR – 100,000 INR. Recurring max: **15,000 INR**.

**Refunds**: **60-day** window. Asynchronous — up to 7 business days.

**Disputes**: Supported but **non-contestable** — funds removed from Stripe balance immediately on acceptance.

**Recurring**: UPI AutoPay (e-mandate). Billing: Invoicing, Subscriptions (no `send_invoice` restriction mentioned).

**36 merchant countries** (US, AU, SG, most of Europe).

**Connect**: Yes.

**Integration**: 4 paths — Checkout, Checkout Sessions API, Payment Intents API, Direct API. Checkout supports setup mode and subscription mode (e-mandate). QR expires in **5 minutes** (`payment_intent.payment_failed` on expiry). Off-session/recurring notifications are **delayed** (unlike one-time which are immediate).

**Save/recurring**: Checkout (setup mode) or Direct API via `stripe.confirmUpiSetup()` (SetupIntent) or PaymentIntent + `setup_future_usage: off_session`. Full billing address required (name, Indian address). `next_action.upi_handle_redirect_or_display_qr_code` (parallel to Swish). On-session saved payments still redirect to UPI app. Detach via `detachPaymentMethod` → `mandate.updated` + `payment_method.detached` events.

**UPI AutoPay (e-mandate) — RBI requirements**: (1) AFA: customer enters UPI PIN to authorize mandate setup. (2) **24-hour pre-debit notification** before each charge (SMS/app with exact amount + cancellation option) — Stripe sends automatically. Initial charge window: 5 minutes after setup. SetupIntent path: Stripe debits then immediately refunds. Mandate defaults: `amount` = 15,000 INR, `amount_type` = `maximum`, `end_date` = 10 years. Scheme max: 40 years. Adaptive Pricing: do NOT pass mandate params.

## PromptPay Details

**QR code** real-time payment — Thailand customers only, THB only. TH merchant accounts only. Instant confirmation.

**Statement descriptor**: ignored — `STRIPE PAYMENTS (THAILAND) LTD` shown with unique reference code.

**Refunds**: customer must provide bank account number for routing — Stripe emails customer to request. Refund fails without it.

**Duplicate QR risk**: re-scanning a completed QR **can deduct funds again** (unlike PayNow which rejects duplicate scans). Stripe reimburses excess to merchant balance; merchant must refund customer outside Stripe.

**Disputes**: "Not applicable" — Stripe reviews irregularities directly.

**Billing**: `send_invoice` only. Mobile Payment Element: iOS only (not Android).

**Connect**: Yes. No payout timing specified.

**Integration**: Checkout and Direct API only — no Elements path. Direct API uses `stripe.confirmPromptPayPayment()` (PromptPay-specific, parallel to PayNow's `confirmPayNowPayment`); opens inline QR modal. Only requires `billing_details.email` (simpler than PayNow or Pix). Fulfillment via `payment_intent.succeeded` webhook.

## Swish Details

**Mobile redirect + desktop QR** — Sweden customers only, SEK only.

**Stripe as merchant of record** — unique among real-time methods: Stripe's name shown as payment recipient in Swish app and as statement descriptor. Merchant name appears in message field only. Factoring addendum in Swish legal terms applies.

**27 merchant countries** — European focus only (no US/AU/SG).

**Refunds**: **365-day** window. Full and partial. Multiple partials supported. Takes a few minutes.

**No disputes. No recurring. No billing/invoicing.**

**Product support**: Connect, Checkout (not subscription/setup), Elements (not Express Checkout Element), Payment Links only.

**Prohibited categories**: Wine/Champagne producers, alcoholic beverage wholesalers, package liquor stores, pawn shops, art dealers, real estate rental agents, legal services/attorneys, precious metals/jewelry, digital wallet top-ups.

**Connect**: Direct, Destination, Separate charges and transfers.

**Integration**: Checkout, Elements, Direct API, iOS/Android SDK. Direct API requires displaying a legal notice that Stripe is the merchant of record (EN/SE/other languages); Checkout and Elements handle automatically. `next_action.swish_handle_redirect_or_display_qr_code` exposes `hosted_instructions_url`, `qr_code.data`, `qr_code.image_url_png/svg`. Optional `payment_method_options.swish.reference` (order reference shown in Swish app). Desktop QR refreshable up to 20 times. Cancelable before expiry.

## Bizum Details

**Real-time payment** — Spain customers only, EUR only. **No Connect**. **No manual capture**. Phone-number authentication via buyer's bank app.

**Transaction limits**: €0.50–€5,000. 28 merchant countries.

**Onboarding**: must provide tax/national ID and set `business_type` before capability activates.

**Disputes**: 120-day customer window; **40-day** merchant evidence (longest of any method reviewed); 90-day decision.

**Refunds**: **395-day** window (longest of any payment method reviewed).

**Integration**: four paths (Checkout, Checkout Sessions API, PaymentIntents API, Direct API). Direct API requires collecting the customer's Bizum-registered phone number (`billing_details[phone]`); no redirect needed — Stripe.js polls for result. Mobile supported via iOS (StripePaymentsUI) and Android (Compose) SDKs.

## Sources

- [[source-stripe-real-time-payments]] — overview: 5 methods, product/API support matrices, PayTo standout
- [[source-stripe-upi]] — UPI: India QR/redirect, 60-day refunds, 15k INR recurring limit, non-contestable disputes, UPI AutoPay
- [[source-stripe-upi-accept-payment]] — UPI integration: 4 paths, Checkout setup/subscription mode, 5-min QR expiry, delayed off-session notifications
- [[source-stripe-upi-set-up-future-payments]] — UPI save/recurring: confirmUpiSetup(), full address required, next_action QR data, on-session still redirects
- [[source-stripe-upi-autopay]] — UPI AutoPay: RBI AFA + 24-hour pre-debit notification, mandate defaults (15k INR, 10yr), Adaptive Pricing caveat
- [[source-stripe-pix]] — Pix: Brazil QR/string, Ebanx partner, IOF tax, Pix Automático recurring, non-challengeable disputes
- [[source-stripe-pix-accept-payment]] — Pix integration: 3 paths, setup/subscription mode in Checkout, expires_after_seconds, CPF/CNPJ required
- [[source-stripe-pix-save-payment-details]] — Pix save/recurring: Checkout + Direct API, confirmPixSetup/confirmPixPayment, next_action.pix_display_qr_code, mandate revocation
- [[source-stripe-pix-automatico]] — Pix Automático: 3-day pre-debit notification, mandate customization fields, retry logic, daily schedule prohibited
- [[source-stripe-promptpay]] — PromptPay: TH-only QR, refund requires customer bank input, duplicate QR risk, send_invoice only, iOS Mobile Element
- [[source-stripe-promptpay-accept-payment]] — PromptPay integration: Checkout + Direct API, confirmPromptPayPayment(), email only, inline QR modal
- [[source-stripe-swish]] — Swish: SE-only mobile redirect + desktop QR, Stripe as MoR, 365-day refunds, no billing, extensive prohibited categories
- [[source-stripe-swish-accept-payment]] — Swish integration: 3 paths + mobile SDK, Direct API legal notice required, next_action QR data, 20 QR refreshes, cancelable
- [[source-stripe-payto]] — PayTo: Australia mandate-based, disputes (final), recurring, 44 banks, mandate field details
- [[source-stripe-pay-by-bank]] — Pay by Bank (UK/Europe): open banking, 730-day refunds, no disputes, Connect support, 35 merchant countries
- [[source-stripe-pay-by-bank-accept-payment]] — Pay by Bank integration: Checkout + Elements paths, statement_descriptor required, DE/GB only for Checkout
- [[source-stripe-paynow]] — PayNow: SG-only QR code, 1.3% pricing, T+1 payout, 90-day refunds, no statement descriptor, Terminal support
- [[source-stripe-paynow-accept-payment]] — PayNow integration: Checkout + Direct API, confirmPayNowPayment(), inline QR (no redirect)
- [[source-stripe-bizum]] — Bizum: Spain-only phone auth, 395-day refunds, 40-day evidence window, onboarding requirements
- [[source-stripe-bizum-accept-payment]] — Bizum integration guide: 4 paths, Direct API phone-number collection, mobile SDK support, test data
