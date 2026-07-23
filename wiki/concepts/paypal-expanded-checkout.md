---
title: "PayPal Expanded Checkout"
type: concept
category: technology
tags: [paypal, expanded-checkout, hosted-card-fields, 3d-secure, acdc, liability-shift, card-fields, javascript-sdk]
---

## PayPal Expanded Checkout

PayPal Expanded Checkout (also called Advanced Credit and Debit Card / ACDC) is a more customisable checkout integration that renders hosted card input fields directly on the merchant's page, with 3D Secure (3DS) authentication support.

## How It Differs from Standard Checkout

| Dimension | Standard Checkout | Expanded Checkout |
| --------- | ----------------- | ----------------- |
| Card entry | Via PayPal pop-up | Inline hosted fields on merchant's page |
| Branding | PayPal-branded | Merchant-branded card fields |
| 3DS | Basic | Full `liabilityShift` response |
| Sandbox requirement | Standard account | Expanded Credit and Debit Card Payments capability |

## Key Components

### Card Fields (`paypal.CardFields`)

Inline hosted input fields rendered on the merchant's page via the JS SDK:
- Cardholder name
- Card number
- Expiration date
- Postal code
- CVV

Customisable to match the merchant's branding.

The exact `@paypal/checkout-components@5.0.425` runtime independently exports a public Card Fields component and retains separate Payment Fields and Hosted Buttons interfaces. This historical implementation evidence supports the component boundary, but current Expanded Checkout capability and 3DS guidance remain authoritative for merchant integration.

### `cardFields.submit()`

The merchant's own Submit/Pay button calls `cardFields.submit()` — triggering the `createOrder` callback. This differs from Standard Checkout where clicking the PayPal button starts the flow.

### React callback freshness

In `@paypal/react-paypal-js@8.9.2`, `PayPalCardFieldsProvider` and individual Card Fields proxy their callback props through a stable object. The SDK instance can therefore remain mounted while `createOrder`, `onApprove`, `onError`, and input-event callbacks read the latest React closure after component state changes. This prevents stale order quantities or stale application state without forcing the Card Fields SDK object to reinitialize.

The retained Storybook scenarios exercise changing React state across provider callbacks and each individual field's `onChange`, `onFocus`, `onBlur`, and `onInputSubmitRequest` callbacks.

### Version 9 submit options

In `@paypal/paypal-js@9.8.0`, both one-time and save-payment Card Fields sessions accept optional `submit()` options containing `name` and a billing address. The address supports address lines, administrative areas, postal code, and country code. The release identifies these fields as 3DS authentication support.

The paired `@paypal/react-paypal-js@9.3.0` Card Fields hooks pass those optional submit values through for both order IDs and vault setup tokens.

### `liabilityShift`

Returned in the `onApprove` callback after 3DS authentication. Indicates whether fraud liability has shifted from the merchant to the card issuer. Merchants use this to decide whether to capture.

### 3D Secure (3DS)

Merchant passes 3DS verification parameters in the Create Order API call. The SDK then shows the card issuer's 3DS challenge if required.

## Sandbox Requirement

Requires the **Expanded Credit and Debit Card Payments** capability enabled on the sandbox business account:

> Developer Dashboard → Apps & Credentials → App → Features → Accept payments → Expanded Credit and Debit Card Payments ✓

## Relevant Companies

- [[paypal]] — PayPal company overview

## 3DS Configuration

Passed server-side in the Create Order payload under `paymentSource.card.attributes.verification.method`:

- `SCA_ALWAYS` — authenticate every transaction
- `SCA_WHEN_REQUIRED` — only when required by regional mandate (PSD2 countries)

## `INSTRUMENT_DECLINED` — different handling for card vs button

When `data.card` is truthy (card payment), `actions.restart()` does **not** apply. Only use `actions.restart()` for PayPal button (`!data.card`) `INSTRUMENT_DECLINED` errors.

## Sources

- [[source-paypal-expanded-checkout-getting-started]] — Getting started guide
- [[source-paypal-expanded-checkout-integrate]] — Full integration guide with CardFields + 3DS code samples
- [[source-github-paypal-js]] — package-qualified React wrapper source and Card Fields callback implementation
- [[source-github-paypal-checkout-components]] — package-qualified checkout runtime and Card Fields interface
