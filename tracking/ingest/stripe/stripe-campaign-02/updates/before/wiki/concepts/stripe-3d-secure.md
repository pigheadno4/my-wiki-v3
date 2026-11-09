---
title: "Stripe 3D Secure (3DS)"
type: concept
category: technology
tags: [stripe, 3d-secure, 3ds2, sca, authentication, liability-shift, radar, payment-intents]
---

## Definition

3D Secure (3DS) is a card authentication protocol that verifies the cardholder's identity before payment authorization. Stripe supports 3DS2 (runs when bank supports it, falls back to 3DS1). 3DS1 is deprecated — use Payment Intents/Setup Intents API for 3DS2.

**Platforms**: Web, iOS, Android, React Native. Also available standalone for use with other PSPs.

## SCA Readiness

**SCA applies if**: EEA business + EEA customers + card payments. Charges API is NOT SCA-ready.

**SCA-ready products**: Payment Intents API, Setup Intents API, Checkout, Billing.

**Grandfathering** (previous authorization agreements): EU cards saved before Dec 31 2020; UK cards saved before Sep 14 2021 — Stripe checks automatically; bank can still decline → `requires_payment_method`.

**Off-session readiness checklist**:

- Authenticate at card save time
- `setup_future_usage: 'off_session'` when saving during payment
- SetupIntent `usage: 'off_session'` when saving without payment
- Set `off_session: true` on PaymentIntent when charging

**MIT mandate**: require customer permission + frequency + amount determination language at checkout. Liability shift does NOT apply when bank uses an exemption (payment not authenticated via 3DS).

**Platforms**: use `setAppInfo`; notify Stripe + customers when SCA-ready update released.

## When 3DS Triggers

Stripe triggers 3DS automatically for:

- **SCA** (Europe) — Strong Customer Authentication mandate
- **Japan** — Credit Card Security Guidelines
- **Issuer soft decline** — issuer requests authentication
- **Stripe optimizations** — Adaptive Acceptance or other features
- **Radar rules** — Dashboard-configured fraud rules
- **Manual API** — `payment_method_options[card][request_three_d_secure]`

3DS does NOT apply to: wallets, off-session payments.

## PaymentIntent State Flow

1. Confirm PaymentIntent → Stripe assesses 3DS need
2. If required: `requires_action` → display 3DS UI
3. After authentication: `processing` → `succeeded` / `requires_capture`
4. If failed: `requires_payment_method`

Special result `attempt_acknowledged` → payment proceeds (check `three_d_secure.result` on Charge).

## Manual 3DS via API

```js
paymentIntents.create({
  payment_method_options: {
    card: { request_three_d_secure: 'any' }  // or 'challenge'
  }
})
```

- `'any'`: preference for frictionless flow
- `'challenge'`: preference for challenge flow (customer must respond)
- Overrides Radar rules on that PaymentIntent/SetupIntent/Checkout Session
- Works at create or confirm time; issuer determines final flow

Check `three_d_secure.authentication_flow` on Charge/SetupAttempt for actual flow used.

## Web Display Options

| Method | How |
| --- | --- |
| Auto popup (default) | `confirmCardPayment` / `handleCardAction` |
| Redirect | Pass `return_url`; `next_action.redirect_to_url.url` |
| Iframe | Embed `redirect_to_url.url` in `<iframe>`; no `sandbox` attribute; `postMessage('3DS-authentication-complete')` back |

**Iframe constraints**: no `sandbox`; issuer controls fonts/colors; supported sizes: 250×400, 390×400, 500×600, 600×400, fullscreen. Return page must `postMessage` to parent, then `retrievePaymentIntent` to check status.

## Mobile Integration

**PaymentSheet / PaymentSheet.FlowController**: handles 3DS automatically — no additional work needed.

**Manual iOS** (`STPPaymentHandler`): timeout ≥ 5 min; `STPThreeDSUICustomization` for colors/fonts.

**Manual Android** (`PaymentAuthConfig.Stripe3ds2Config`): timeout ≥ 5 min; `StripeUiCustomization` for UI.

**React Native** (`threeDSecureParams` in `StripeProvider`): timeout ≥ 5 min; `urlScheme` for auto-dismiss.

## Test Cards (Web)

| Number | 3DS | Notes |
| --- | --- | --- |
| 4000000000003220 | Required | Always requires 3DS2 |
| 4000002500003155 | Required | Required for MIT/off-session unless set up |
| 4000008400001629 | Required | Authenticates then declines |
| 4000000000003055 | Supported | Optional — Radar won't request by default |
| 4242424242424242 | Supported | Not enrolled — no challenge even if requested |
| 378282246310005 | Not supported | Proceeds without auth |

**Mobile test cards**: 4000582600000094 (Out of Band), 4000582600000045 (OTP), 4000582600000102 (Single Select), 4000582600000110 (Multi Select)

## Liability Shift

- Successful 3DS → fraudulent disputes shift to card issuer
- Dispute inquiries on 3DS payments **must be responded to** (risk "no-reply" chargeback invalidating shift)
- Liability may also shift if 3DS required by network but unavailable (issuer outage)
- Exceptions: excessive fraud monitoring programs; some industries (e.g., Visa excludes wire transfer/money orders)
- ECI returned in `three_d_secure.electronic_commerce_indicator` on Charge

## Import 3DS Results (External Auth)

For travel aggregators (Expedia/Sabre) or third-party 3DS providers. Pass cryptogram directly to Payment Intents API.

**Availability**: AU/CA/CH/EU/GB/HK/MX/NZ/SG/US (GA); beta elsewhere; excluded: IN/MY/TH. Raw card path requires PCI DSS validation + Stripe review.

**Key parameters**: `payment_method_options.card.three_d_secure: { version, electronic_commerce_indicator, cryptogram, transaction_id }`; always `confirm: true` + `error_on_requires_action: true`.

**Exemption import**: `exemption_indicator: 'low_risk'` → Stripe re-assesses via TRA; check `exemption_indicator_applied` on Charge.

**Cartes Bancaires**: `network: 'cartes_bancaires'` + `cb_avalgo` (required) + optional CB-specific fields.

## Standalone 3DS

Decouples 3DS authentication from payment authorization — run auth on Stripe, authorize with any PSP. Enterprise use: API-level control, issuer observability, per-transaction customized flows.

**Output**: 3DS cryptogram → import into Stripe OR send to any other PSP.

**Availability**: IC+ pricing only; Visa/MC/Amex/Discover/Cartes Bancaires; all Stripe card-payment countries except Malaysia and Thailand.

## SCA Exemptions (EEA / Switzerland / UK)

> Exemption approved → **no liability shift** to issuer.

| Exemption | Key thresholds |
| --- | --- |
| **Low Value** | < 30 EUR / 25 GBP; cumulative cap: 100 EUR or 5 txns since last SCA |
| **TRA / Low Risk** | Stripe fraud rate: 0.13% → 100 EUR; 0.06% → 250 EUR; 0.01% → 500 EUR. Current Stripe limits: EEA ≤ 250 EUR, UK/Swiss ≤ 220 GBP |
| **MIT (off-session)** | Outside SCA scope; no challenge, no liability shift; requires mandate + auth at save time |

**Data Only** (3DS2.2+): frictionless; no liability shift (issuer not contacted); Mastercard Identity Check Insights via Adaptive Acceptance / Authorization Boost only (EEA/UK). Stripe AI handles automatically.

## Sigma Analytics

**Table**: `authentication_report_attempts` (Analytics Tables). One row per attempt; use `is_final_attempt` to deduplicate retried payments.

**Key columns**: `threeds_outcome_result`, `authentication_flow`, `sca_exemption_requested/mechanism/status`, `charge_outcome/reason`, `is_final_attempt`.

**Auth success**: `threeds_outcome_result` in `('attempt_acknowledged', 'authenticated', 'delegated', 'exempted')`.

Deduplication impact example: raw auth rate 59% → deduped 80% (dedup groups same `customer_id`+`currency`+`amount` close in time).

## Sources

- [[source-stripe-3d-secure-authentication-flow]] — primary: full flow, manual triggering, web/iOS/Android/RN display, liability shift, test cards
- [[source-stripe-sca-exemptions]] — SCA exemptions (EEA/CH/UK): Low Value, TRA limits, MIT, Data Only (no liability shift on exemption/Data Only)
- [[source-stripe-standalone-3ds]] — Standalone 3DS: decouple auth from authorization, IC+ only, cryptogram output to any PSP, no Malaysia/Thailand
- [[source-stripe-3ds-import]] — Import 3DS results: travel/third-party 3DS, confirm+error_on_requires_action, exemption import, Cartes Bancaires cb_avalgo
- [[source-stripe-3ds-sigma-query]] — Sigma authentication_report_attempts: is_final_attempt dedup, auth rate calc, SCA exemption columns, 3 example queries
- [[source-stripe-sca-readiness]] — SCA readiness: impacted businesses, SCA-ready products, grandfathering rules (EU Dec 2020 / UK Sep 2021), off-session checklist, MIT mandate
- [[source-stripe-moto]] — MOTO: out-of-scope SCA exemption, PCI compliance required, `moto` parameter on PI/SI, bank has final say
