---
title: "South Korean Payment Methods (Stripe)"
type: concept
category: technology
tags: [stripe, south-korea, krw, local-payment-methods, kakao-pay, naver-pay, samsung-pay, payco, wallets, installments]
---

## Definition

Stripe describes acceptance of South Korean local cards and wallets without a local South Korean entity through Stripe and a **local processor partner**. The Korea overview does not expressly designate a merchant-of-record role; any comparison with the separate Nigerian arrangement is an inference, not a legal classification established here.

## Payment Methods

| Method | One-time | Recurring | Notes |
| --- | --- | --- | --- |
| All local KR cards (kr_card) | Yes | Yes | |
| Kakao Pay | Yes | Yes | Not available in Singapore |
| Naver Pay | Yes | Yes | |
| Samsung Pay | Yes | No | |
| PAYCO | Yes | No | |

Customers select their card issuer and authenticate via their card/bank's app rather than manually entering card details.

## Key Properties

- **Currency**: KRW only
- **Business locations**: 28 countries (AT, BE, CY, DE, DK, EE, ES, FI, FR, GB, GR, HK, HR, HU, IE, IT, JP, LT, LU, LV, MT, NL, PT, SE, SG, SI, SK, US)
- **Payout timing**: T+4 (US), T+7 (outside US)
- **Recurring**: Yes (cards, Kakao Pay, Naver Pay); No (Samsung Pay, PAYCO)
- **Manual capture**: Yes; **Partial capture**: No
- **Connect**: Yes
- **Disputes**: Yes — customer has 365 days to file; merchant has **7 days** to respond; 45-day decision; final outcome
- **Refunds**: Full + partial, 365-day window

## Installments

Local card issuers can offer installments on purchases of at least 50,000 KRW. The customer repays the issuer while the business receives the full purchase amount up front relative to those installments; this is not a promise of immediate external payout. The overview separately says funds enter the Stripe balance four days after approval and lists T+4 US/T+7 non-US payout timing. It says the business keeps funds if the customer cannot complete issuer installments.

## Korean Consumer Law — Refund Requirements

- The May and November 2026 Stripe overviews say customers are **generally** entitled to a full refund within seven days of receiving goods or services, unless used or damaged; applicability is conditional and this overview is not a transaction-specific legal determination.
- Non-refundable conditions must be clearly displayed
- If goods differ from contract: refund within 3 months of purchase or 30 days after discovering discrepancy (whichever comes first)
- Subscriptions: 7-day full refund if unused; pro-rated cancellation anytime

## Subscription Requirements

- The dated Korea overviews say to **notify and obtain customer consent at least 30 days** before a subscription price increase or first charge for a previously free service.
- Remind customers **7 days before payment** by email, text, or mail.
- The page advises an easy cancellation button or clear instructions to minimize disputes; it does not itself establish a mandatory button implementation.

## Dispute Details

7 supported reason codes: Credit not processed, Duplicate, Fraudulent, General, Product not received, Product unacceptable, Subscription canceled.

Best evidence: POS data/system logs, subscription terms/policies, usage records and communications.

## Integration

Dashboard-driven: enable South Korean payment methods → auto-surfaced in Checkout/Elements/Invoicing/Payment Links/Subscriptions. Also available via Payment Intents API.

### PAYCO (`payco`)

- **Payment mode only** — no setup/subscription mode, no recurring
- **28 business locations** (all 28 including SG); 100 KRW min; 2M KRW stored value max
- **No buyer email required**, no funding source parameter — simpler than Naver Pay
- **NICEPAY disclosure required** — same text as all other KR methods
- **Checkout**: add `payco` to `payment_method_types`; all line items in `krw`
- **Direct API**: `stripe.confirmPayment()` with `payment_method_data.type: 'payco'` + `return_url`

### KR Card — Save / Recurring (`kr_card`)

- **Accounts v2 supported**: both `customer_account` (Accounts v2, GA for Connect / preview otherwise) and `customer` (v1) variants available throughout
- **SetupIntent path**: `setupIntents.create({ payment_method_types: ['kr_card'], payment_method_data: { type: 'kr_card' }, usage: 'off_session'|'on_session', customer|customer_account })` → `stripe.confirmKrCardSetup()` with `return_url` + `mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } }`
- **PaymentIntent `setup_future_usage` path**: `setup_future_usage: 'off_session'`, `confirm: true`, `mandate_data` with explicit `ip_address` + `user_agent`
- **Recurring payments**: `capture_method: 'automatic'` required — manual capture not supported for off-session recurring
- **Checkout setup mode**: `mode: 'setup'`, `kr_card` in `payment_method_types`; testing: select "Local card" → "Continue to Local card"
- **Detach**: fires `mandate.updated` + `payment_method.detached`
- **Source bug**: Stripe docs use `currency: 'ngn'` in the `setup_future_usage` PaymentIntent examples — should be `krw`

### Kakao Pay — Save / Recurring (`kakao_pay`)

- **May 2026 Accounts v2 + v1 paths**: the saved-payment guide shows a customer-configured Account with `customer_account` and a separate Customers v1 `customer` path. At that capture, Accounts v2 was generally available for Connect users, in public preview for other Stripe users, and required a preview API version for preview participants. The November 2026 variant index does not verify current access. See [[source-stripe-kakao-pay-set-up-future-payments]].
- **Checkout authorization**: explicitly states customer must authorize their **NICEPAY account** for future payments
- **SetupIntent path**: `setupIntents.create({ payment_method_types: ['kakao_pay'], payment_method_data: { type: 'kakao_pay' }, usage: 'off_session', customer|customer_account })` → `stripe.confirmKakaoPaySetup()` with `return_url` + `mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } }`
- **Recurring caveat**: `capture_method: 'automatic'` required — manual capture not supported
- **Detach**: fires `mandate.updated` + `payment_method.detached`
- **Source bug**: `currency: 'ngn'` in `setup_future_usage` PaymentIntent examples (same copy-paste error as kr_card guide)

### Naver Pay — Save / Recurring (`naver_pay`)

- **Accounts v2 + v1 dual-path** — same structure as kr_card and kakao_pay save guides
- **`stripe.confirmNaverPaySetup()`** — client-side setup confirmation; `mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } }`
- **Recurring caveat**: `capture_method: 'automatic'` required — manual capture not supported
- **Detach**: fires `mandate.updated` + `payment_method.detached`
- **Source bug**: `currency: 'ngn'` in `setup_future_usage` PaymentIntent examples — same copy-paste error as kr_card and kakao_pay guides

### Naver Pay (`naver_pay`)

- **28 business locations** — includes Singapore (unlike Kakao Pay)
- **Minimum**: 100 KRW; stored value top-up max: 2,000,000 KRW (no max for card passthrough)
- **Modes**: payment + setup + subscription (recurring supported)
- **No buyer email required** — unlike Kakao Pay
- **Funding source**: `payment_method_data.naver_pay.funding` = `'card'` (default, linked Naver Pay card) or `'points'` (Naver Pay Points balance)
- **NICEPAY disclosure required** — same as other KR methods
- **Branding**: must comply with Naver Pay [overseas brand guidelines](https://developers.pay.naver.com/design/brand/overseas)
- **Checkout**: add `naver_pay` to `payment_method_types`; all line items in `krw`
- **Direct API**: `stripe.confirmPayment()` with `payment_method_data.type: 'naver_pay'` + `return_url`

### Kakao Pay (`kakao_pay`)

- **Not available in Singapore** — 27 business locations (all KR card countries minus SG)
- **Minimum**: 100 KRW; stored value top-up max: 2,000,000 KRW (no max for card passthrough)
- **Modes**: payment + setup + subscription (recurring supported)
- **Buyer email (May 2026 guide)**: Direct API PaymentIntent creation supplies `payment_method_data.billing_details.email`; Checkout prose also requires buyer email, though its Session examples do not show a field for it.
- **NICEPAY merchant-page disclosure (May Direct API client path)**: the Direct API section requires processor identity and NICEPAY terms text/link on the merchant checkout page. The May Checkout section does not state how hosted or embedded Checkout supplies this disclosure; the November variant index gives no answer.
- **Checkout (May)**: dynamic payment methods may surface Kakao Pay automatically; manual configuration adds `kakao_pay` to `payment_method_types`. All line items use `krw`.
- **Direct API (May)**: server-created KRW PaymentIntent, client `stripe.confirmPayment()` with `payment_method_data.type: 'kakao_pay'` and `return_url`; verify PaymentIntent status after redirect.
- **Post-payment (May)**: `payment_intent.succeeded` event indicates completion; sandbox authorize/fail states do not guarantee a live outcome. See [[source-stripe-kakao-pay-accept-payment]].

### KR Card (`kr_card`)

- **Minimum**: 100 KRW; all three modes (payment/setup/subscription)
- **NICEPAY disclosure required**: must display on checkout page — *"This transaction is processed through NICEPAY in accordance with NICEPAY's terms of use"* (link to `start.nicepay.co.kr`)
- **Checkout**: add `kr_card` to `payment_method_types`; all line items in `krw`; testing: select "Local cards" → Stripe-hosted redirect page
- **Direct API**: create PaymentIntent with `kr_card` + `payment_method_data: { type: 'kr_card' }`; `stripe.confirmPayment()` client-side with `return_url`
- **Post-payment**: `payment_intent.succeeded` webhook

## Android SDK `23.18.0` Evidence

PaymentSheet release notes announce PAYCO, Korean cards, Naver Pay and Kakao Pay support. Compiled API adds `PaymentMethod.Type.Payco`, `KrCard`, `NaverPay` and `KakaoPay` with corresponding `PaymentMethodCreateParams` creation overloads. PaymentSheet forms/routing and request/confirmation implementation are excluded; do not infer merchant eligibility, recurring support or mandate handling from those declarations. This release does not announce ordinary PaymentSheet Samsung Pay support; the separate Crypto Onramp Samsung Pay history has its own scope. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

## Sources

- [[source-github-stripe-android]] - Android 23.18.0 Korean-method declarations and PaymentSheet announcements, with implementation limits

- [[source-stripe-local-payment-methods-by-country]] — hub page: Nigeria + South Korea local payment methods
- [[source-stripe-korea-payment-methods]] — May 8 and November 7, 2026 full South Korea overviews: local processor partner, Dashboard enablement, KRW method matrix, redirect/approval/balance/payout stages, conditional refunds, disputes, and 30-day notice-plus-consent subscription rule. November adds only an interest-registration preview for descriptive decline codes; enrollment and returned codes are unverified.
- [[source-stripe-kr-card-accept-payment]] — KR card integration: kr_card, 100 KRW minimum, NICEPAY disclosure required, confirmPayment(), redirect flow
- [[source-stripe-kr-card-set-up-future-payments]] — KR card save/recurring: Accounts v2 + v1, confirmKrCardSetup(), setup_future_usage, automatic capture only for recurring
- [[source-stripe-subscriptions-kr-card]] — KR card subscriptions (May 2026 detailed variants; November 2026 variant index): KRW pricing, SetupIntents, direct Subscriptions API, and hosted Checkout paths; path-specific mandate and off-session examples

> [!warning] Contradiction
> The May SetupIntents opening describes a first Subscriptions API call, while its steps begin with a SetupIntent. Its confirmation prose names `payment_method_types` while the commands use `payment_method_data`. Neither the examples nor the November index establish universal `off_session` or `mandate_data` requirements across all three paths. See the dated [[source-stripe-subscriptions-kr-card]].
- [[source-stripe-subscriptions-kakao-pay]] — Kakao Pay subscription: 2026-05-13 full guide with SetupIntents, Subscriptions API, and Checkout variants and a dated KRW instruction; 2026-11-07 capture is a three-link variant index only. The comparison with KR card is limited to the three-path organization.
- [[source-stripe-subscriptions-naver-pay]] — Naver Pay subscription: 2026-05-13 full guide with SetupIntents, Subscriptions API, and Checkout variants plus a dated KRW instruction; 2026-11-07 capture is a three-link variant index only. Comparison with the other Korean guides here is limited to three-path organization.
- [[source-stripe-kakao-pay-accept-payment]] — May 2026 full Kakao Pay Checkout and Direct API acceptance guide: dated KRW, buyer email, location and amount conditions; explicit NICEPAY merchant-page text/link belongs to its Direct API client section. November 2026 capture is a two-route variant index only; redirect and browser return are not payment-success evidence.
- [[source-stripe-kakao-pay-set-up-future-payments]] — May 2026 full Kakao Pay save/recurring guide: dated Accounts v2 eligibility and v1 identity, Checkout NICEPAY authorization, Direct API `confirmKakaoPaySetup()`, and automatic capture for later recurring charges; November 2026 capture is a Checkout/Direct API variant index only. The May guide's `ngn` saving examples conflict with its `krw` payment examples, and its optional manual redirect PaymentIntent does not contain the fields for future saving.
- [[source-stripe-naver-pay-accept-payment]] — Naver Pay integration: naver_pay, funding source card/points, 28 countries (incl. SG), NICEPAY disclosure, branding guidelines
- [[source-stripe-naver-pay-set-up-future-payments]] — Naver Pay save/recurring: Accounts v2 + v1, confirmNaverPaySetup(), automatic capture only, same ngn currency bug
- [[source-stripe-payco-accept-payment]] — PAYCO integration: payco, payment mode only (no recurring), 28 countries, NICEPAY disclosure, simpler than Naver Pay
