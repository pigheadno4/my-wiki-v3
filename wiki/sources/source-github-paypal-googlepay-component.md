---
title: "GitHub: paypal/paypal-googlepay-component"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-googlepay-component.md"
tags: [paypal, google-pay, 3ds, graphql, apm, googlepay-component]
---

## Summary

PayPal's internal JS component that powers `paypal.Googlepay()` in the JS SDK. Implements the 3 public SDK methods via GraphQL calls and integrates with PayPal's 3DS component for `initiatePayerAction`. v1.3.5.

## Three Core Functions

### `googlePayConfig()`

Calls `POST /graphql?GetGooglePayConfig` with variables: `clientId`, `merchantId`, `merchantOrigin`, `buyerCountry`.

Returns `ConfigResponse`:
```js
{
  allowedPaymentMethods: [{
    type, parameters: { allowedAuthMethods, allowedCardNetworks },
    tokenizationSpecification: { type, parameters: { gateway, gatewayMerchantId } }
  }],
  merchantInfo: { authJwt, merchantId, merchantName, merchantOrigin }
}
```

Throws `PayPalGooglePayError` with `GOOGLEPAY_CONFIG_ERROR` if not eligible.

### `confirmOrder({ orderId, paymentMethodData, shippingAddress, billingAddress, email })`

Calls `mutation ApproveGooglePayPayment` with `productFlow: "CUSTOM_DIGITAL_WALLET"`.

If `billingAddress` is passed, it is injected into `paymentMethodData.info.billingAddress` before sending.

Returns `ApprovePaymentResponse`:
```js
{
  id, status,
  payment_source: { google_pay: { name, card: { last_digits, type, brand } } },
  links: [{ href, rel, method }]
}
```

### `initiatePayerAction({ orderId })`

Triggers 3DS flow using `getThreeDomainSecureComponent()` from `@paypal/common-components`.

Returns `ZalgoPromise` resolving to `{ liabilityShift }`:
- `onSuccess` → `{ liabilityShift: contingencyResult.liability_shift }`
- `onCancel` / `onClose` / `onError` → `{ liabilityShift: "UNKNOWN" }`

## Key Implementation Details

- Uses GraphQL (not REST) for config and payment confirmation
- GQL headers: `x-app-name: "sdk-googlepay"`, `prefer: "return=representation"`, `disable-set-cookie: "true"`
- `PayPalGooglePayError` class includes `paypalDebugId` from `Paypal-Debug-Id` response header
- 3DS uses ZalgoPromise (PayPal's async primitive) — not a native Promise
- `productFlow` is hardcoded as `"CUSTOM_DIGITAL_WALLET"` in confirmOrder

## Flow Types

| Type | Description |
| --- | --- |
| `ConfigResponse` | allowedPaymentMethods + merchantInfo |
| `ConfirmOrderParams` | orderId, paymentMethodData, optional shippingAddress/billingAddress/email |
| `ApprovePaymentResponse` | id, status, payment_source.google_pay, links |
| `GooglePayPaymentMethodData` | description, tokenizationData, type, info (CardInfo) |
| `GooglePayPaymentContact` | name, postalCode, countryCode, phoneNumber, address fields |
| `GooglePayType` | Public interface: config, confirmOrder, initiatePayerAction |

## Related Pages

- [[paypal-google-pay]] — Google Pay via PayPal concept page
- [[paypal-apm]] — APM overview
- [[source-paypal-apm-google-pay]] — Integration guide docs

## Raw Sources

- [[github-paypal-googlepay-component]] — stub file pointing to detail directory
