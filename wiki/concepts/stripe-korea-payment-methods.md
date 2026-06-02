---
title: "South Korean Payment Methods (Stripe)"
type: concept
category: technology
tags: [stripe, south-korea, krw, local-payment-methods, kakao-pay, naver-pay, samsung-pay, payco, wallets, installments]
---

## Definition

Stripe enables acceptance of South Korean local payment methods (all locally-issued cards + major wallets) without a local South Korean entity, via a **local processor partner**. Distinct from the Nigerian MoR model — Stripe describes this as a "local processor partner" arrangement rather than merchant of record.

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

Local card issuers offer installments on purchases ≥50,000 KRW. Merchant receives full amount upfront; customer repays issuer over time. If customer can't complete installments, merchant keeps funds.

## Korean Consumer Law — Refund Requirements

- 7-day right to full refund for goods/services (unless used/damaged)
- Non-refundable conditions must be clearly displayed
- If goods differ from contract: refund within 3 months of purchase or 30 days after discovering discrepancy (whichever comes first)
- Subscriptions: 7-day full refund if unused; pro-rated cancellation anytime

## Subscription Requirements

- **30-day notice** before price increase or first charge on previously free service
- **7-day payment reminder** before charge date (email, SMS, or mail)
- Easy cancellation button or clear instructions required

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

- **Accounts v2 + v1 dual-path** throughout (same structure as kr_card save guide)
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
- **Buyer email required**: must pass `billing_details.email` in `payment_method_data` for Direct API
- **NICEPAY disclosure required** — same as kr_card
- **Checkout**: add `kakao_pay` to `payment_method_types`; provide buyer email; all line items in `krw`
- **Direct API**: `stripe.confirmPayment()` with `payment_method_data.type: 'kakao_pay'` + `return_url`
- **Post-payment**: `payment_intent.succeeded` webhook

### KR Card (`kr_card`)

- **Minimum**: 100 KRW; all three modes (payment/setup/subscription)
- **NICEPAY disclosure required**: must display on checkout page — *"This transaction is processed through NICEPAY in accordance with NICEPAY's terms of use"* (link to `start.nicepay.co.kr`)
- **Checkout**: add `kr_card` to `payment_method_types`; all line items in `krw`; testing: select "Local cards" → Stripe-hosted redirect page
- **Direct API**: create PaymentIntent with `kr_card` + `payment_method_data: { type: 'kr_card' }`; `stripe.confirmPayment()` client-side with `return_url`
- **Post-payment**: `payment_intent.succeeded` webhook

## Sources

- [[source-stripe-local-payment-methods-by-country]] — hub page: Nigeria + South Korea local payment methods
- [[source-stripe-korea-payment-methods]] — South Korea overview: local processor model, payment methods, installments, refunds, disputes, subscription rules
- [[source-stripe-kr-card-accept-payment]] — KR card integration: kr_card, 100 KRW minimum, NICEPAY disclosure required, confirmPayment(), redirect flow
- [[source-stripe-kr-card-set-up-future-payments]] — KR card save/recurring: Accounts v2 + v1, confirmKrCardSetup(), setup_future_usage, automatic capture only for recurring
- [[source-stripe-subscriptions-kr-card]] — KR card subscription: KRW-only, 3 paths (SetupIntents/Subscriptions API/Checkout), off_session+mandate_data required, local processor redirect
- [[source-stripe-subscriptions-kakao-pay]] — Kakao Pay subscription: identical structure to KR card, kakao_pay PM type, KRW-only
- [[source-stripe-subscriptions-naver-pay]] — Naver Pay subscription: identical structure, naver_pay PM type, KRW-only
- [[source-stripe-kakao-pay-accept-payment]] — Kakao Pay integration: kakao_pay, buyer email required, 100 KRW min/2M KRW stored value max, not in SG, NICEPAY disclosure
- [[source-stripe-kakao-pay-set-up-future-payments]] — Kakao Pay save/recurring: Accounts v2 + v1, confirmKakaoPaySetup(), NICEPAY account authorization, automatic capture only
- [[source-stripe-naver-pay-accept-payment]] — Naver Pay integration: naver_pay, funding source card/points, 28 countries (incl. SG), NICEPAY disclosure, branding guidelines
- [[source-stripe-naver-pay-set-up-future-payments]] — Naver Pay save/recurring: Accounts v2 + v1, confirmNaverPaySetup(), automatic capture only, same ngn currency bug
- [[source-stripe-payco-accept-payment]] — PAYCO integration: payco, payment mode only (no recurring), 28 countries, NICEPAY disclosure, simpler than Naver Pay
