---
title: "@paypal/react-paypal-js v8.x README"
type: source
date_ingested: 2026-04-13
original_format: notes
raw_files:
  - "paypal-react-paypal-js-readme.md"
tags: [paypal, react, javascript-sdk, npm, paypal-script-provider, paypal-buttons, card-fields, hosted-fields, braintree, context-api]
---

## @paypal/react-paypal-js v8.x README

Official npm package README for `@paypal/react-paypal-js` v8.9.2 — the React wrapper for the PayPal JS SDK v5 (CardFields). Covers all components, hooks, and integration patterns.

Source URL: <https://www.npmjs.com/package/@paypal/react-paypal-js>

Version: 8.9.2 | Last updated: 2026-04-13 (published ~5 days prior)

## Key Takeaways

### Architecture: two-part design

| Part | Component | Role |
| ---- | --------- | ---- |
| Context Provider | `<PayPalScriptProvider />` | Manages JS SDK script loading; root of app |
| SDK Components | `<PayPalButtons />`, etc. | Render UI; consume context |

Key insight: the anti-pattern is bundling script loading + button rendering in a single component. `PayPalScriptProvider` at the root decouples these.

### `PayPalScriptProvider` options

All JS SDK query params + data attributes, using **camelCase** keys: `clientId`, `currency`, `intent`, `dataClientToken`, `components`, etc.

### `deferLoading` prop

Set `deferLoading={true}` to delay script loading (e.g. until user navigates to checkout). Dispatch `resetOptions` action later to trigger loading.

### `usePayPalScriptReducer` hook

Loading state: `isInitial` → `isPending` → `isResolved` / `isRejected`

Actions:
- `resetOptions` — reload SDK with new parameters (e.g. currency change)

### All available components

| Component | Use case |
| --------- | -------- |
| `<PayPalButtons />` | Standard checkout buttons |
| `<PayPalMarks />` | Payment method logos |
| `<PayPalMessages />` | Pay Later messaging |
| `<PayPalHostedFields />` | Legacy hosted card fields (v1 SDK) |
| `<BraintreePayPalButtons />` | Braintree merchants |
| `<PayPalCardFieldsProvider />` | v5 SDK card fields (current) |
| `<PayPalCardFieldsForm />` | All-in-one card form |
| `<PayPalNameField />` | Individual name field |
| `<PayPalNumberField />` | Individual card number field |
| `<PayPalExpiryField />` | Individual expiry field |
| `<PayPalCVVField />` | Individual CVV field |

### Hosted Fields vs Card Fields

| | `PayPalHostedFields` | `PayPalCardFields` |
| - | -------------------- | ------------------ |
| SDK version | v1 (legacy) | v5 (current) |
| Hook | `usePayPalHostedFields` | `usePayPalCardFields` |
| Submit | `hostedFields.submit({ cardholderName })` | `cardFields.submit()` |
| All-in-one form | No | `<PayPalCardFieldsForm />` |

### `usePayPalCardFields` hook

Returns `{ cardFields, fields }`:
- `cardFields.submit()` — submit the card form
- `fields.CVVField.focus()` — programmatic DOM manipulation of individual fields

### `components: "card-fields"` required

Must be passed in `PayPalScriptProvider` options when using `PayPalCardFieldsProvider`.

### Braintree integration

Uses `dataClientToken` (server-generated) and `actions.braintree.createPayment()` / `actions.braintree.tokenizePayment()` instead of the standard `createOrder`/`onApprove` pattern.

## Raw Sources

- [[paypal-react-paypal-js-readme]] — verbatim README content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Card Fields concept (what `PayPalCardFieldsProvider` wraps)
- [[source-paypal-javascript-sdk-configuration]] — JS SDK query params (same params passed to `PayPalScriptProvider options`)
- [[source-paypal-javascript-sdk-reference]] — JS SDK API reference (same callbacks used in React components)
- [[source-paypal-checkout-single-page-app]] — SPA integration guide (vanilla JS driver approach; `react-paypal-js` is the React-native alternative)
