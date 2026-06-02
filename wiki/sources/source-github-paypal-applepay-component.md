---
title: "GitHub: paypal/paypal-applepay-components"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-applepay-component.md"
tags: [paypal, apple-pay, graphql, apm, applepay-component]
---

## Summary

PayPal's internal JS component that powers `paypal.Applepay()` in the JS SDK. Implements 3 public methods via GraphQL. Very similar pattern to the Google Pay component but with an additional `validateMerchant` step required by Apple Pay's merchant validation flow. v1.8.2.

## Three Core Functions

### `config()`

Calls `POST /graphql?GetApplepayConfig` with variables: `buyerCountry`, `clientId`, `merchantId`.

GraphQL query returns: `merchantCountry`, `supportedNetworks`, `isEligible`, `merchantCapabilities`, `tokenNotificationURL`.

`mapGetConfigResponse()` transforms the GQL response by adding:
- `currencyCode` — from JS SDK query param (defaults to "USD")
- `countryCode` — copied from `merchantCountry`

Returns `ConfigResponse`:
```js
{
  isEligible, countryCode, merchantCountry, currencyCode,
  merchantCapabilities, supportedNetworks, tokenNotificationURL
}
```

### `validateMerchant({ validationUrl, displayName, domainName })`

Calls `POST /graphql?GetApplePayMerchantSession`.

**Key detail**: merchant session response is **base64-encoded** — decoded with `atob()` before returning.

Returns `{ merchantSession: ApplePaySession, paypalDebugId }`.

If `domainName` not provided, falls back to `getMerchantDomain()` (strips protocol from `window.location.origin`).

### `confirmOrder({ orderId, token, billingContact, shippingContact })`

Calls `mutation ApproveApplePayPayment` with `productFlow: "CUSTOM_DIGITAL_WALLET"`.

**Key fix**: Apple Pay returns countryCode in **lowercase** — both `shippingContact.countryCode` and `billingContact.countryCode` are automatically uppercased before the GraphQL call.

Sends `PayPal-Partner-Attribution-Id` header from `getPartnerAttributionID()`.

## Comparison with Google Pay Component

| Aspect | Apple Pay | Google Pay |
| --- | --- | --- |
| Extra step | `validateMerchant` required | Not needed |
| Session encoding | base64 (decoded with `atob`) | Not applicable |
| countryCode fix | Auto-uppercased (Apple sends lowercase) | Not needed |
| 3DS | Not in this component (uses ApplePaySession) | `initiatePayerAction` via ZalgoPromise |
| productFlow | `"CUSTOM_DIGITAL_WALLET"` | `"CUSTOM_DIGITAL_WALLET"` |
| Partner header | Yes (`PayPal-Partner-Attribution-Id`) | No |

## Flow Types

| Type | Description |
| --- | --- |
| `ConfigResponse` | isEligible, countryCode, merchantCountry, currencyCode, merchantCapabilities, supportedNetworks, tokenNotificationURL |
| `ValidateMerchantParams` | validationUrl, displayName?, domainName? |
| `ValidateMerchantResponse` | merchantSession (ApplePaySession), paypalDebugId |
| `ConfirmOrderParams` | orderId, token, billingContact?, shippingContact? |
| `ApplePayPaymentContact` | phoneNumber?, emailAddress?, givenName?, familyName?, addressLines?, locality?, postalCode?, countryCode?, etc. |
| `ApplePayPaymentToken` | paymentMethod, transactionIdentifier?, paymentData? |
| `ApplepayType` | config, validateMerchant, confirmOrder |

## Related Pages

- [[paypal-apple-pay]] — Apple Pay via PayPal concept page
- [[paypal-apm]] — APM overview
- [[source-paypal-apm-apple-pay]] — Integration guide docs
- [[source-github-paypal-googlepay-component]] — Google Pay component (similar pattern)

## Raw Sources

- [[github-paypal-applepay-component]] — stub file pointing to detail directory
