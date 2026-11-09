---
title: "Stripe 3D Secure (3DS)"
type: concept
category: technology
tags: [stripe, 3d-secure, 3ds2, sca, authentication, liability-shift, radar, payment-intents]
---

## Definition

3D Secure (3DS) is cardholder authentication before payment authorization. The May and November 2026 captures recommend Payment Intents or Setup Intents for 3DS2 and say major card brands no longer support 3DS1, yet both also describe fallback to 3DS1 when a bank lacks 3DS2. This tension does not establish that any current card or network can use that fallback. The November guide states protocol support through version 2.3.1. See [[source-stripe-3d-secure-authentication-flow]] (https://docs.stripe.com/payments/3d-secure/authentication-flow; old raw/stripe-3d-secure-authentication-flow-2025.md:8-15; new raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md:9-17).

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

Not every transaction supports 3DS; this guide gives wallets and off-session payments as examples. Its test table also describes a card requiring 3DS2 for off-session payment unless set up for future use, so do not infer a blanket off-session exclusion. See [[source-stripe-3d-secure-authentication-flow]] (https://docs.stripe.com/payments/3d-secure/authentication-flow; old raw/stripe-3d-secure-authentication-flow-2025.md:57,484; new raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md:56,442).

## PaymentIntent State Flow

1. Confirm PaymentIntent → Stripe assesses 3DS need
2. If required: `requires_action` → display 3DS UI
3. Successful authentication leads Stripe to attempt a charge and the PaymentIntent to `processing`; the later payment outcome can be `succeeded`, `requires_capture`, or `requires_payment_method`.
4. Failed authentication can lead to `requires_payment_method`. Authentication, authorization, capture, and settlement are distinct outcomes; a sandbox test card authenticates and then declines. After an iframe return, retrieve the PaymentIntent and inspect its status. See [[source-stripe-3d-secure-authentication-flow]] (https://docs.stripe.com/payments/3d-secure/authentication-flow; old raw/stripe-3d-secure-authentication-flow-2025.md:74-81,284-294,485; new raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md:73-80,248-258,443).

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
- Overrides dynamic Radar 3DS rules on that PaymentIntent/SetupIntent/Checkout Session, but Stripe's mandatory authentication rules still run; the November guide says Stripe APIs cannot manually turn off 3DS.
- For PaymentIntents/SetupIntents, request at create or confirm time; for Checkout Sessions, at creation. The issuer determines the final authentication flow, so `any` and `challenge` are preferences. The May capture calls the custom-rule tier Radar for Fraud Teams; November calls it Radar Plus. See [[source-stripe-3d-secure-authentication-flow]] (https://docs.stripe.com/payments/3d-secure/authentication-flow; old raw/stripe-3d-secure-authentication-flow-2025.md:87-93,164-172; new raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md:86-94,137-145).

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

- Successful 3DS authentication alone does **not** guarantee liability shift for any payment or dispute. Shift can be expected for successfully authenticated payments later receiving eligible fraud disputes, subject to network and payment/dispute conditions; the older guide already said it *typically* applies and listed exceptions.
- A `charge.succeeded` event confirms payment success only; `three_d_secure.result=authenticated` confirms 3DS authentication only. ECI in `three_d_secure.electronic_commerce_indicator` on the Charge can help assess eligibility but guarantees no shift.
- Respond to inquiries on 3DS-authenticated charges: failure can cause a no-reply financial chargeback that could invalidate shift. An inquiry is a request for information, distinct from a financial chargeback.
- Shift can sometimes apply if the network requires 3DS but the card or issuer lacks it; monitoring programs, network/industry exclusions, or post-authorization downgrade can instead prevent shift after authentication. The wire-transfer/money-order examples are specifically Visa exclusions; other dispute reasons follow the standard process. See [[source-stripe-3d-secure-authentication-flow]] (https://docs.stripe.com/payments/3d-secure/authentication-flow; old raw/stripe-3d-secure-authentication-flow-2025.md:539-557; new raw/stripe-payments-3d-secure-authentication-flow-2026-11-07.md:497-529).

## Import 3DS Results (External Auth)

For travel aggregators (Expedia/Sabre) or third-party 3DS providers. Pass cryptogram directly to Payment Intents API.

**Availability**: AU/CA/CH/EU/GB/HK/MX/NZ/SG/US (GA); beta elsewhere; excluded: IN/MY/TH. Raw card path requires PCI DSS validation + Stripe review.

**Key parameters**: `payment_method_options.card.three_d_secure: { version, electronic_commerce_indicator, cryptogram, transaction_id }`; always `confirm: true` + `error_on_requires_action: true`.

**Exemption import**: `exemption_indicator: 'low_risk'` → Stripe re-assesses via TRA; check `exemption_indicator_applied` on Charge.

**Cartes Bancaires**: `network: 'cartes_bancaires'` + `cb_avalgo` (required) + optional CB-specific fields.

## Standalone 3DS

Decouples 3DS authentication from payment authorization: run authentication on Stripe, then submit the cryptogram in a separate payment authorization request through Stripe's import route or another PSP. Authentication success alone does not establish authorization, capture, settlement, issuer payment approval, or liability shift. The 2026-11-07 guide details request modes, issuer output, 3RI and non-payment cases, and the authentication sequence; see [[source-stripe-standalone-3ds]].

**Availability**: The 2026-05-08 capture said available to businesses on Interchange Plus pricing, without claiming exclusivity. The 2026-11-07 capture omits pricing eligibility, so current account/tier requirements remain unresolved. Both captures list Visa, Mastercard, American Express, Discover, and Cartes Bancaires and exclude Malaysia and Thailand from the stated Stripe card-payment-country footprint. This standalone scope is separate from the result-import availability matrix above.

## SCA Exemptions (EEA / Switzerland / UK)

> Exemption approved → **no liability shift** to issuer.

| Exemption | Key thresholds |
| --- | --- |
| **Low Value** | < 30 EUR / 25 GBP; issuer SCA can still be required after cardholder-initiated cumulative spend exceeds 100 EUR/85 GBP or five transactions since the last SCA. |
| **TRA / Low Risk** | Provider fraud-rate ceilings: 0.13% → up to 100 EUR/85 GBP; 0.06% → up to 250 EUR/220 GBP; 0.01% → up to 500 EUR/440 GBP. The 2026-11-07 capture reports qualifying EEA transactions up to 250 EUR and UK/Swiss up to 220 GBP; availability depends on Stripe-wide fraud rates and offering access, not a guaranteed account entitlement. |
| **MIT (off-session)** | Qualifying saved-card later charges are technically outside SCA; authenticate the card when saved and obtain agreement for later charges. The guide describes no challenge or liability shift for the MIT path, without proving every future charge qualifies or cannot need action. |

**Data Only**: A successful request can offer a frictionless experience for a payment not subject to SCA, without liability shift. Authentication goes to the card network; the issuer still receives an authorization message carrying network risk data, though no issuer authentication request is sent. The standard Data Only flow requires 3DS 2.2+; separately named Mastercard Identity Check Insights was described in the 2026-11-07 capture as offered to Adaptive Acceptance and Authorisation Boost users in EEA/UK. This does not establish every account's eligibility or transfer the standard-flow version rule to all Data Only products.

## Sigma Analytics

**Table**: `authentication_report_attempts` (Analytics Tables). One row per attempt; use `is_final_attempt` to deduplicate retried payments.

**Key columns**: `threeds_outcome_result`, `authentication_flow`, `sca_exemption_requested/mechanism/status`, `charge_outcome/reason`, `is_final_attempt`.

**Auth success**: `threeds_outcome_result` in `('attempt_acknowledged', 'authenticated', 'delegated', 'exempted')`.

Deduplication impact example: raw auth rate 59% → deduped 80% (dedup groups same `customer_id`+`currency`+`amount` close in time).

## Sources

- [[source-stripe-3d-secure-authentication-flow]] — May and November 2026 Web/mobile authentication-flow guide, manual triggering, sandbox tests, and conditional fraud-dispute liability guidance
- [[source-stripe-sca-exemptions]] — captured EEA/Swiss/UK SCA request and issuer-approval scope, dated low-value/TRA limits, qualifying MIT, and Data Only network-versus-issuer routing without liability shift
- [[source-stripe-standalone-3ds]] — Standalone 3DS: separate authentication and authorization, 2026-11-07 feature/workflow detail, dated 2026-05-08 Interchange Plus statement with current tier eligibility unresolved
- [[source-stripe-3ds-import]] — Import 3DS results: travel/third-party 3DS, confirm+error_on_requires_action, exemption import, Cartes Bancaires cb_avalgo
- [[source-stripe-3ds-sigma-query]] — Sigma authentication_report_attempts: is_final_attempt dedup, auth rate calc, SCA exemption columns, 3 example queries
- [[source-stripe-sca-readiness]] — SCA readiness: impacted businesses, SCA-ready products, grandfathering rules (EU Dec 2020 / UK Sep 2021), off-session checklist, MIT mandate
- [[source-stripe-moto]] — MOTO: out-of-scope SCA exemption, PCI compliance required, `moto` parameter on PI/SI, bank has final say
