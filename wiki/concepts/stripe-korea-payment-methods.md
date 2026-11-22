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
- **Capture**: The November 2026 Korea overview lists manual capture and no partial capture for the payment-method group. The May 2026 [[source-stripe-kr-card-set-up-future-payments|dedicated KR card guide]] requires automatic capture for recurring `kr_card` payments.
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

- The May 8, 2026 Checkout guide lists 28 business locations including Singapore, KRW line items and payment mode only. It distinguishes the 100 KRW minimum and 2,000,000 KRW stored-value top-up limit from card passthrough, for which it gives no maximum.
- The May Direct API browser example calls `stripe.confirmPayment` with `payment_method_data.type: 'payco'` and `return_url`. Its examples omit email and a funding selector without establishing universal PAYCO field rules. The explicit NICEPAY disclosure and terms link belong to its Direct API client section. Verify the PaymentIntent status separately from browser return.
- The May manual Checkout Session and PaymentIntent creation examples include `payco` in the writable `payment_method_types` list. The separate `2026-09-30.endive` Create endpoint references document HTTP 400 for that request field and retain the computed response property. The PaymentIntent error is `payment_method_types_no_longer_supported`. The Intent changelog Impact paragraph separately names `2026-08-26.preview`.
- The separate `2026-07-29.dahlia` `payment_method_options.payco.setup_future_usage=none` option means no saving. The November Korea overview lists PAYCO as one-time only, and the November PAYCO acceptance capture is only Checkout/Direct API navigation. See [[source-stripe-payco-accept-payment]] for the dated request and status boundaries.

### KR Card — Save / Recurring (`kr_card`)

The 2026-05-08 [[source-stripe-kr-card-set-up-future-payments|dedicated guide]] calls for customer permission and a written agreement record. It shows a customer-configured Accounts v2 Account via `customer_account` or a Customers v1 Customer via `customer`. It describes Accounts v2 as generally available for Connect and in public preview for other users, with a preview API version for participants.

- Hosted Checkout uses `mode: 'setup'` and includes `card` and `kr_card` in both examples. Direct API setup creates a server SetupIntent and the browser passes the SetupIntent secret, return URL, and online mandate data to `stripe.confirmKrCardSetup()`.
- Saving during payment uses a separate PaymentIntent with `setup_future_usage: 'off_session'` and `confirm: true`. Supply `mandate_data` when a new mandate is needed. The optional manual redirect sample is a separate PaymentIntent example and omits the saving fields. It checks `requires_action` and `redirect_to_url` before redirecting. Use server events to verify payment status.
- A later charge uses the saved PaymentMethod ID and matching customer identity. The May guide requires automatic capture for recurring charges and `off_session: true` when the customer is outside the current checkout. Server-side detach deactivates the method and triggers `mandate.updated` and `payment_method.detached`.
- **Archived currency discrepancy**: Both May save-during-payment examples show `ngn`, while the standalone redirect and reuse examples use `krw`, consistent with the dated Korea presentment and subscription pricing guidance. The November index leaves the examples unresolved.

### Kakao Pay — Save / Recurring (`kakao_pay`)

- **May 2026 Accounts v2 + v1 paths**: the saved-payment guide shows a customer-configured Account with `customer_account` and a separate Customers v1 `customer` path. At that capture, Accounts v2 was generally available for Connect users, in public preview for other Stripe users, and required a preview API version for preview participants. The November 2026 variant index does not verify current access. See [[source-stripe-kakao-pay-set-up-future-payments]].
- **Checkout authorization**: explicitly states customer must authorize their **NICEPAY account** for future payments
- **SetupIntent path**: `setupIntents.create({ payment_method_types: ['kakao_pay'], payment_method_data: { type: 'kakao_pay' }, usage: 'off_session', customer|customer_account })` → `stripe.confirmKakaoPaySetup()` with `return_url` + `mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } }`
- **Recurring caveat**: `capture_method: 'automatic'` required — manual capture not supported
- **Detach**: fires `mandate.updated` + `payment_method.detached`
- **Source bug**: `currency: 'ngn'` in `setup_future_usage` PaymentIntent examples (same copy-paste error as kr_card guide)

### Naver Pay — Save / Recurring (`naver_pay`)

- **May customer identity**. The guide shows `customer_account` for a customer-configured Accounts v2 Account and `customer` for Customers v1. It describes Accounts v2 as generally available for Connect users and version-qualified public preview for other users.
- **Setup**. The browser uses `stripe.confirmNaverPaySetup()` with a SetupIntent secret, return URL and online `mandate_data` using `infer_from_client` in the example. The separate charge-and-save route includes `mandate_data` if a mandate needs to be created.
- **Reuse and capture**. Set `off_session: true` when the customer is outside this checkout flow. The May guide requires automatic capture for recurring payments. This recurring constraint is separate from the general manual capture property.
- **Detach**. Server detachment deactivates reuse and sends `mandate.updated` and `payment_method.detached`.
- **Currency discrepancy**. The two May charge-and-save examples use `ngn`, in conflict with the `krw` redirect and reuse examples and the separate Naver Pay acceptance guide. The capture establishes no NGN support. See [[source-stripe-naver-pay-set-up-future-payments]] for dated details.

### Naver Pay (`naver_pay`)

- **May Checkout**. 28 business locations including Singapore, KRW line items and a 100 KRW minimum. The 2,000,000 KRW cap is for stored-value top-up. The guide states no maximum for card passthrough. The compatibility table lists payment, setup and subscription modes, while the examples use payment mode. The separate [[source-stripe-naver-pay-set-up-future-payments|setup guide]] covers consent, capture for recurring payments and the historical NGN discrepancy.
- **May Direct API**. Naver server and confirm examples omit email. The separate Kakao Direct API guide requires it. The Naver creation example offers `card` (default) or `points` funding. The Basil changelog makes those parameters creation-only. The client sample supplies only the type. The Direct API merchant page carries the NICEPAY disclosure and terms, and `stripe.confirmPayment` uses the `return_url` before PaymentIntent status verification. Follow Naver Pay's [overseas brand guidelines](https://developers.pay.naver.com/design/brand/overseas) if using its branding.
- **Endive request scope**. The May manual Checkout and PaymentIntent examples use `payment_method_types`. The `2026-09-30.endive` create endpoints reject this writable field with HTTP 400. Use the separate compatibility-filtered alternatives and outcome qualifications in [[source-stripe-naver-pay-accept-payment]].

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

- **May 2026 Checkout compatibility**: KRW line items, 100 KRW minimum, and payment/setup/subscription modes. The hosted and embedded examples show payment mode. Dynamic display uses eligibility checks. The May manual examples add `kr_card` to `payment_method_types`.
- **May 2026 Direct API**: the merchant page identifies NICEPAY and links its terms. This is the dated Direct API disclosure. The browser calls `stripe.confirmPayment` using the server-created PaymentIntent's secret and returns to the merchant after the processor flow.
- **Outcome**: consult the PaymentIntent's state and handle `payment_intent.succeeded` for post-payment actions. A return or test transition does not establish a live payment.
- **API version warning**: the separately captured `2026-09-30.endive` Checkout Session Create and PaymentIntent Create references reject the historical writable `payment_method_types` field. See [[source-stripe-kr-card-accept-payment]].

## Android SDK `23.18.0` Evidence

PaymentSheet release notes announce PAYCO, Korean cards, Naver Pay and Kakao Pay support. Compiled API adds `PaymentMethod.Type.Payco`, `KrCard`, `NaverPay` and `KakaoPay` with corresponding `PaymentMethodCreateParams` creation overloads. PaymentSheet forms/routing and request/confirmation implementation are excluded; do not infer merchant eligibility, recurring support or mandate handling from those declarations. This release does not announce ordinary PaymentSheet Samsung Pay support; the separate Crypto Onramp Samsung Pay history has its own scope. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

## Sources

- [[source-github-stripe-android]] - Android 23.18.0 Korean-method declarations and PaymentSheet announcements, with implementation limits

- [[source-stripe-local-payment-methods-by-country]] — hub page: Nigeria + South Korea local payment methods
- [[source-stripe-korea-payment-methods]] — May 8 and November 7, 2026 full South Korea overviews: local processor partner, Dashboard enablement, KRW method matrix, redirect/approval/balance/payout stages, conditional refunds, disputes, and 30-day notice-plus-consent subscription rule. November adds only an interest-registration preview for descriptive decline codes; enrollment and returned codes are unverified.
- [[source-stripe-kr-card-accept-payment]] — May 2026 Checkout and Direct API guide, including the dated NICEPAY disclosure for Direct API, payment-state boundaries, and versioned Endive request-field warnings. November capture is a variant index.
- [[source-stripe-kr-card-set-up-future-payments]] — May 2026 Checkout setup and Direct API guide for consent, customer identity, separate setup and charging paths, recurring capture, and the archived currency discrepancy. November 2026 is variant navigation.
- [[source-stripe-subscriptions-kr-card]] — KR card subscriptions (May 2026 detailed variants; November 2026 variant index): KRW pricing, SetupIntents, direct Subscriptions API, and hosted Checkout paths; path-specific mandate and off-session examples

> [!warning] Contradiction
> The May SetupIntents opening describes a first Subscriptions API call, while its steps begin with a SetupIntent. Its confirmation prose names `payment_method_types` while the commands use `payment_method_data`. Neither the examples nor the November index establish universal `off_session` or `mandate_data` requirements across all three paths. See the dated [[source-stripe-subscriptions-kr-card]].
- [[source-stripe-subscriptions-kakao-pay]] — Kakao Pay subscription: 2026-05-13 full guide with SetupIntents, Subscriptions API, and Checkout variants and a dated KRW instruction; 2026-11-07 capture is a three-link variant index only. The comparison with KR card is limited to the three-path organization.
- [[source-stripe-subscriptions-naver-pay]] — Naver Pay subscription: 2026-05-13 full guide with SetupIntents, Subscriptions API, and Checkout variants plus a dated KRW instruction; 2026-11-07 capture is a three-link variant index only. Comparison with the other Korean guides here is limited to three-path organization.
- [[source-stripe-kakao-pay-accept-payment]] — May 2026 full Kakao Pay Checkout and Direct API acceptance guide: dated KRW, buyer email, location and amount conditions; explicit NICEPAY merchant-page text/link belongs to its Direct API client section. November 2026 capture is a two-route variant index only; redirect and browser return are not payment-success evidence.
- [[source-stripe-kakao-pay-set-up-future-payments]] — May 2026 full Kakao Pay save/recurring guide: dated Accounts v2 eligibility and v1 identity, Checkout NICEPAY authorization, Direct API `confirmKakaoPaySetup()`, and automatic capture for later recurring charges; November 2026 capture is a Checkout/Direct API variant index only. The May guide's `ngn` saving examples conflict with its `krw` payment examples, and its optional manual redirect PaymentIntent does not contain the fields for future saving.
- [[source-stripe-naver-pay-accept-payment]] — May 2026 Checkout and Direct API guide for KRW acceptance, creation-time card/points funding, NICEPAY disclosure and Stripe payment status. Includes versioned request warnings. November indexes the two variants.
- [[source-stripe-naver-pay-set-up-future-payments]] — May 2026 hosted Checkout setup and Direct API guide with dated customer identity, recurring automatic capture and conflicting currency examples. The November capture indexes the two variants.
- [[source-stripe-payco-accept-payment]] — May 8, 2026 PAYCO Checkout and Direct API guide with dated one-time mode, Direct API NICEPAY scope and no-save/API-version qualifications. The November 7, 2026 capture is a two-variant selector.
