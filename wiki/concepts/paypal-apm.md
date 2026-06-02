---
title: "PayPal Alternative Payment Methods (APMs)"
type: concept
category: technology
tags: [paypal, apm, bank-redirect, local-payment-methods, apple-pay, google-pay, ideal, bancontact, trustly, pay-upon-invoice]
---

## PayPal Alternative Payment Methods (APMs)

Non-card, non-PayPal-wallet payment options that PayPal supports for checkout. Covers bank redirects, digital wallets, vouchers, and deferred payments — enabling local payment preferences across Europe and beyond.

## APM Summary Table

| APM | Type | Flow | Countries | Notable |
| --- | --- | --- | --- | --- |
| Apple Pay | push | direct | Multi-country | 180-day refund |
| Google Pay | push | direct | Multi-country | 180-day refund |
| Bancontact | bank redirect | redirect | Belgium | Popular in BE |
| BLIK | bank redirect | redirect | Poland | PLN only |
| eps | bank redirect | redirect | Austria | EUR only |
| iDEAL | bank redirect | redirect | Netherlands | 0.01 EUR min; used by >50% of NL online shoppers |
| MyBank | bank redirect | redirect | Italy | EUR only |
| Przelewy24 | bank redirect | redirect | Poland | PLN + EUR |
| Trustly | bank redirect | redirect | 12 European countries | **365-day refund window** |
| Multibanco | voucher | redirect | Portugal | No minimum; **no refunds** |
| Pay upon Invoice | deferred | direct | Germany | 5 EUR min; pay after delivery |

## Payment Flow Types

- **Direct**: no redirect; payment completed inline (Apple Pay, Google Pay, Pay upon Invoice)
- **Redirect**: payer sent to external bank/provider to authorize, then returned to merchant

## Swish (Sweden) — Added Nov 2025

> [!info] Not in APM overview table
> The APM overview page (last updated Jul 2025) does not include Swish. Added November 2025.

- Sweden/SEK; **push payment** (not bank redirect); instant auto-capture
- **0.01 SEK minimum, ~1 trillion SEK maximum** (largest of all APMs)
- **Refunds up to 13 months** (longest of all APMs)
- Two buyer flows: QR code (desktop) + mobile app switch
- **Two integration patterns** (unique to Swish): PayPal-hosted (redirect to `payer-action`) vs Merchant-hosted (display `qr_details.qr_image` on own page)
- Orders API: requires `payer` object (email, name, phone) — unique among all APMs; supports both auto and manual capture; mobile app switch uses `swish://` URL scheme; seller protection eligible

## Crypto (Pay with Crypto) — Added Jan 2026

> [!info] Not in APM overview table
> The APM overview page (last updated Jul 2025) lists 11 APMs. Crypto was added Jan 2026 and is not yet reflected in that table.

- **US merchants only, global buyers** — opposite geography from bank redirect APMs
- **~100 cryptocurrencies** (BTC, ETH, SOL, PYUSD, DOGE, etc.); buyers don't need a PayPal account
- **Auto-settlement in local currency** — PayPal converts crypto; refunds in PYUSD stablecoin
- **0.01 USD minimum**; capture-only; no recurring, chargebacks, vaulting, or multi-seller
- Two buyer flows: self-custody wallet (Metamask) or exchange account (Coinbase)
- Orders V2 API only; Create Order uses `payment_source.crypto` with `country_code: US`, buyer name, `experience_context`; `cancel_url` also handles errors (error codes as query params)

## APM-Specific Restrictions

### Pay upon Invoice / Rechnungskauf mit Ratepay (Germany)

- Germany only (both buyer and merchant); **deferred payment** (BNPL); PayPal partners with Ratepay
- **5 EUR min, 2,500 EUR max**; 180-day refunds
- Merchant **funded immediately**; buyer pays Ratepay within 30 days via bank transfer
- **VAT ID required**; **Terms acceptance required** (separate Ratepay T&C); B2C only; ship within 7 days
- **Digital/virtual goods prohibited**
- Buyer info: full name, email, delivery + billing address, **date of birth**, phone (most extensive of all APMs)
- Dispute: 10-business-day response; retain proof 180 days; `notify_buyer: false` in Add Tracking API
- Error handling: must display Ratepay-specific error if risk declined (not generic error)
- Integration: FraudNet JS library + PUI Legal Component required; `PHYSICAL_GOODS` only; `PENDING_APPROVAL` response status; `payment_reference` + `deposit_bank_details` for buyer invoice; `CHECKOUT.PAYMENT-APPROVAL.REVERSED` webhook unique to PUI
- FraudNet: `f` param (session ID) sent as `PAYPAL-CLIENT-METADATA-ID` header; `s` param = `<merchant_id>_<page_id>`; fixed `fncls` key

### Google Pay

- 36 countries/22 currencies — same as Apple Pay (both add Greece vs standard 35-country list)
- Works on **all major browsers** (Chrome, Firefox, Safari, Edge) — unlike Apple Pay
- One-time payments only; Japan: must override `allowedAuthMethods = ['PAN_ONLY']` (TPAN unsupported)
- Dual SDK: PayPal (`components=googlepay`) + Google Pay (`pay.google.com/gp/p/js/pay.js`)
- Two touchpoints: `paypal.Googlepay().config()` (eligibility) and `paypal.Googlepay().confirmOrder()`
- 3DS: `PAYER_ACTION_REQUIRED` → `initiatePayerAction()` → check `liability_shift`

### Trustly (12 European countries)

- AT, DE, DK, EE, ES, FI, GB, LT, LV, NL, NO, SE — broadest European bank redirect coverage
- **EUR, DKK, SEK, GBP, NOK** (5 currencies — most of any bank redirect APM)
- 0.01 EUR minimum; **365-day refund window** (longest of all APMs)
- **Non-instant**: up to 7 days settlement; merchant receives PENDING webhook → completion webhook → ships goods
- Merchant exclusions: RU, BR, **BE, CZ, PL, SK, SI** (no Japan exclusion unlike other APMs)
- JS SDK: name-only fields; `onApprove` does NOT capture (already auto-captured); non-instant webhook pattern (PENDING → 7 days → COMPLETED); currency must match country
- Orders API: name + optional email; `cancel_url` is "placeholder for now"; DENIED webhook description mentions Multibanco (doc copy-paste error)

### Przelewy24 (Poland)

- Poland, **PLN and EUR** (unlike BLIK which is PLN only), 1 PLN minimum, 180-day refunds — bank redirect
- Same restrictions as Bancontact/BLIK/EPS/iDEAL/MyBank: no chargebacks, capture-only, global merchants (ex RU/JP/BR)
- JS SDK: `enable-funding=p24` (short alias); name+email fields (same as BLIK); no mark image
- Orders API: `payment_source.p24` with name + **email required** (unlike Bancontact/EPS name-only)

### MyBank (Italy)

- Italy/EUR only, no minimum, 180-day refunds — bank redirect
- Same restrictions as Bancontact/BLIK/EPS/iDEAL: no chargebacks, capture-only, global merchants (ex RU/JP/BR)
- JS SDK: name-only fields; no dedicated mark image; no self-serve onboarding links in docs
- Orders API: same auto-capture as Bancontact/EPS; `country_code: IT`; doc error: webhook heading mislabeled

### Multibanco (Portugal)

- Portugal/EUR only; **voucher** payment type (not bank redirect) — fundamentally different from other APMs
- **No minimum**, **maximum 99,999.99 EUR**, **no refunds**
- Non-instant settlement: buyer pays via online banking or ATM after receiving reference number
- No eligibility restrictions documented (no chargeback/capture-only limitations like other APMs)
- Merchant ships goods after receiving `PAYMENT.CAPTURE.COMPLETED` webhook
- JS SDK: `CHECKOUT.ORDER.APPROVED` returns `BARCODE_URL`; capture automatic; `PAYMENT.CAPTURE.DENIED` = voucher expired
- Orders API: 2-step (create order without payment_source → `confirm-payment-source`); `payment_reference` + `payment_entity` in GET response; 7-day payment window

### iDEAL (Netherlands)

- Netherlands/EUR only, **0.01 EUR minimum** (lowest of all APMs)
- Same restrictions as Bancontact/BLIK/EPS: no chargebacks, capture-only, global merchants (ex RU/JP/BR)
- Unique onboarding: Partners use Partner Referral API with `iDEAL` in `products` — **skip** `capabilities` array
- Merchants outside 32 listed countries need offline onboarding via Customer Success Manager + CIP process
- JS SDK: name-only fields; explicit onboarding error message documented (not seen in other APM guides)
- Orders API: two failure scenarios documented for non-onboarded merchants; `experience_context` inside `payment_source.ideal` (vs `application_context` at root for other APMs)

### EPS (Austria)

- Austria/EUR only, 1 EUR minimum
- Same restrictions as Bancontact/BLIK: no chargebacks, capture-only, no billing agreements, global merchants (ex RU/JP/BR)
- JS SDK: payment fields collect **name only** (same as Bancontact; BLIK also collects email); `enable-funding=eps&currency=EUR`
- Orders API: same auto-capture pattern as Bancontact; `payment_source.eps` with `name` + `country_code: AT` (no email field)

### BLIK (Poland)

- Poland/PLN only, 1 PLN minimum
- Same restrictions as Bancontact: no chargebacks, capture-only, no billing agreements, global merchants (ex RU/JP/BR)
- JS SDK: payment fields collect **name + email** (Bancontact collects name only); `enable-funding=blik&currency=PLN`
- Orders API: same auto-capture pattern as Bancontact; `payment_source.blik` includes optional `email` field (Bancontact does not)

### Bancontact (Belgium)

- Merchant eligibility: global (excluding Russia, Japan, Brazil)
- **No chargebacks**, no billing agreements, no shipping callbacks, no multiple seller payments
- **Capture only** (no authorization), online only
- JS SDK integration: `enable-funding=bancontact&currency=EUR`; payment fields collect name only; single-page or multi-page flow
- Orders API integration: `payment_source.bancontact` with `name` + `country_code`; `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` for auto-capture; uses `application_context` (not `experience_context`)
- **Progressive Onboarding not supported** for APMs — onboard merchants before first payment
- German merchants use multi-page flow for local regulatory compliance

## Sunset APMs

- **giropay**: sunset June 30, 2024
- **Sofort**: sunset April 18, 2024

## Privacy Disclosure

Merchants using PayPal APMs must disclose to payers that PayPal processes the payment — either via checkout text or a pre-payment privacy notice linking to the PayPal Privacy Statement.

## Relevant Companies

- [[paypal]] — PayPal company overview

## Standard APM Webhooks (shared reference)

All APMs use these 5 core webhooks: `CHECKOUT.ORDER.APPROVED`, `CHECKOUT.PAYMENT-APPROVAL.REVERSED`, `PAYMENT.CAPTURE.PENDING`, `PAYMENT.CAPTURE.COMPLETED`, `PAYMENT.CAPTURE.DENIED`. Registered via `POST /v1/notifications/webhooks`.

## Sources

- [[source-paypal-payment-methods-reference]] — Full payment method catalog: 18 entries; Google Pay mis-labeled "bank redirect"; Apple Pay "US only" (contradicts 34-country guide); iDEAL BIC restriction footnote; Multibanco absent
- [[source-paypal-apm-error-codes]] — Error code reference: 19 codes in `cancel_url` query params; `payee_not_enabled`, `currency/country_not_supported`, `order_complete_on_payment_approval`
- [[source-paypal-apm-style-reference]] — Payment fields style reference: 11 variables + 6 CSS rules; `paypal.FUNDING.OXXO` in example (OXXO = unlisted Mexican voucher APM)
- [[source-paypal-apm-js-sdk-reference]] — JS SDK reference: `paypal.FUNDING.*` constants (7 active + 2 sunset); vertical-layout-only; comma-separated `enable-funding`; `isEligible()` pattern; Trustly/Multibanco absent
- [[source-paypal-apm-handle-uncaptured-payments]] — Uncaptured payment reference: `CHECKOUT.PAYMENT-APPROVAL.REVERSED` webhook; **3-hour default capture window** (merchant-configurable); cancel + refund
- [[source-paypal-apm-method-icons]] — APM icon reference: color+white SVGs for Bancontact/BLIK/eps/iDEAL/MyBank/Przelewy24; iDEAL has no white variant; hosted at paypalobjects.com
- [[source-paypal-apm-subscribe-webhooks]] — Webhook subscription reference: 5 core events, registration via Webhooks API, webhook ID response
- [[source-paypal-apm-overview]] — APM overview: full table, payment type taxonomy, refund windows, sunset notices
- [[source-paypal-apm-apple-pay]] — Apple Pay integration: domain validation, 4 SDK touchpoints, non-Safari support, 34 countries/22 currencies, go-live onboarding
- [[source-paypal-apm-trustly]] — Trustly (12 EU countries/5 currencies): broadest bank redirect coverage; 365-day refunds; non-instant (7-day) settlement; different merchant exclusions
- [[source-paypal-apm-przelewy24]] — Przelewy24 (Poland/PLN+EUR): same restrictions as other bank redirect APMs; EUR support distinguishes from BLIK
- [[source-paypal-apm-mybank]] — MyBank (Italy/EUR): no minimum, same restrictions as Bancontact/BLIK/EPS/iDEAL (capture-only, no chargebacks)
- [[source-paypal-apm-multibanco]] — Multibanco (Portugal/EUR): voucher (non-instant), no minimum, 99,999.99 max, no refunds, no eligibility restrictions
- [[source-paypal-apm-ideal]] — iDEAL (Netherlands/EUR): 0.01 EUR min, unique onboarding (ISU skip capabilities, offline via CSM for unlisted countries)
- [[source-paypal-apm-swish]] — Swish (Sweden/SEK): push payment, 13-month refunds, 2 integration patterns (PayPal-hosted vs Merchant-hosted with `qr_details.qr_image`)
- [[source-paypal-apm-crypto]] — Pay with Crypto (US merchants, global buyers): ~100 cryptos, auto local-currency settlement, refunds in PYUSD, no PayPal account needed
- [[source-paypal-apm-pay-upon-invoice]] — Pay upon Invoice/Ratepay (Germany): BNPL, 5–2500 EUR, immediate merchant funding, VAT ID required, date of birth collected, 10-day dispute window
- [[source-paypal-apm-google-pay]] — Google Pay: 36 countries, all browsers, dual SDK, `confirmOrder`/`initiatePayerAction`, Japan PAN_ONLY override
- [[source-paypal-apm-eps]] — EPS (Austria/EUR): same restrictions as Bancontact/BLIK (capture-only, no chargebacks, global ex RU/JP/BR)
- [[source-paypal-apm-blik]] — BLIK (Poland/PLN): same restrictions as Bancontact (capture-only, no chargebacks, global ex RU/JP/BR)
- [[source-paypal-apm-bancontact]] — Bancontact (Belgium): capture-only, no chargebacks, JS SDK integration (single/multi-page), Progressive Onboarding not supported for APMs
