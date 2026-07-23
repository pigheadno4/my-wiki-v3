---
title: "Google Pay (via PayPal)"
type: concept
category: technology
tags: [google-pay, paypal, apm, mobile-payments, 3d-secure, push-payment]
---

## Google Pay (via PayPal)

Google Pay is a digital wallet payment method that allows buyers to pay using cards stored in their Google account. PayPal supports Google Pay as an APM through its JS SDK and Orders v2 API.

## Key Constraints

- **Browser support**: all major browsers (Chrome, Firefox, Safari, Edge) — no browser restriction unlike Apple Pay
- **Availability**: 36 countries, 22 currencies
- **Scope**: one-time payments with buyer present only — no vault/merchant-initiated recurring support
- **Japan**: TPAN not supported by local processors; must override `allowedAuthMethods = ['PAN_ONLY']`

## Integration

Dual SDK required — both PayPal JS SDK (`components=googlepay`) and Google Pay SDK (`pay.google.com/gp/p/js/pay.js`).

Three PayPal SDK touchpoints:

| Method | Purpose |
| --- | --- |
| `paypal.Googlepay().config()` | Returns `allowedPaymentMethods` + `merchantInfo` for building `PaymentDataRequest` |
| `paypal.Googlepay().confirmOrder({ orderId, paymentMethodData })` | Confirms order with Google Pay token |
| `paypal.Googlepay().initiatePayerAction({ orderId })` | Triggers 3DS when `PAYER_ACTION_REQUIRED` |

### Flow

1. `config()` → check eligibility, get allowed payment methods
2. `isReadyToPay()` → render Google Pay button if eligible
3. `loadPaymentData()` → show Google Pay sheet
4. `onPaymentAuthorized` → create order → `confirmOrder()` → capture
5. If `PAYER_ACTION_REQUIRED`: `initiatePayerAction()` → check `liability_shift` → capture

## Version 9 React Package Evidence

`@paypal/paypal-js@9.8.0` exposes Google Pay through the `googlepay-payments` v6 component. Its session formats eligibility configuration for Google's `PaymentsClient`, confirms an order using Google payment-method data, and leaves button rendering and payment-sheet control to Google's SDK rather than a PayPal web component.

`@paypal/react-paypal-js@9.3.0` adds `GooglePayOneTimePaymentButton` and `useGooglePayOneTimePaymentSession`. The React component checks `isReadyToPay()`, mounts the native button returned by `PaymentsClient.createButton()`, creates the merchant order during authorization, and calls the PayPal session's `confirmOrder()`.

> [!info] Version-specific 3DS boundary
> In the exact `@paypal/paypal-js@9.8.0` type surface, `initiatePayerAction()` is documented as a no-argument placeholder for future 3DS support. This differs from the established integration guidance above, which calls `initiatePayerAction({ orderId })`. Do not infer complete Google Pay 3DS handling from the 9.8.0 wrapper types alone; verify the deployed SDK and current product documentation.

## 3DS Handling

`confirmOrder()` returns `status: PAYER_ACTION_REQUIRED` → call `initiatePayerAction({ orderId })` → check `orderResponse.payment_source.google_pay.card.authentication_result.liability_shift` → capture if acceptable.

## Comparison with Apple Pay (via PayPal)

| | Google Pay | Apple Pay |
| --- | --- | --- |
| Browser support | All major browsers | Safari only (without latest SDK) |
| Countries | 36 | 34 (go-live); 36 (integration guide) |
| Vault/recurring | Not supported | Supported (merchant-initiated only) |
| SDK touchpoints | 3 | 4 |
| Japan quirk | PAN_ONLY override required | No |

## Go Live

Production onboarding: `paypal.com/bizsignup/add-product?product=payment_methods&capabilities=GOOGLE_PAY`

## Relevant Companies

- [[paypal]] — PayPal supports Google Pay as an APM via JS SDK and Orders API

## Sources

- [[source-paypal-apm-google-pay]] — Full integration guide: dual SDK, `confirmOrder`/`initiatePayerAction`, Japan PAN_ONLY override, 38 test cards across 5 countries
- [[source-github-paypal-js]] — package-qualified Google Pay v6 types, React hook, and native-button implementation
