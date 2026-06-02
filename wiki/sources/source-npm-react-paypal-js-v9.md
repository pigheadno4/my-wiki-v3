---
title: "@paypal/react-paypal-js v9.x README (SDK v6)"
type: source
date_ingested: 2026-04-17
original_format: notes
raw_files:
  - "npm-react-paypal-js.md"
tags: [paypal, react, javascript-sdk-v6, npm, hooks, typescript, ssr, card-fields, venmo, pay-later, vault]
---

## Summary

npm README for `@paypal/react-paypal-js` v9.1.1 — React wrapper for **PayPal JS SDK v6**. Major breaking change from v8.x: new import path, new provider, new return shapes. Published April 2026, 269k weekly downloads.

## Breaking changes from v8.x → v9.x

| v8.x | v9.x |
| --- | --- |
| `import from "@paypal/react-paypal-js"` | `import from "@paypal/react-paypal-js/sdk-v6"` |
| `PayPalScriptProvider` | `PayPalProvider` |
| `PayPalButtons` | `PayPalOneTimePaymentButton` or session hooks |
| `options={{ clientId }}` | `clientId={...}` or `clientToken={...}` (mutually exclusive) |
| `createOrder` returns plain `orderId` string | `createOrder` returns `{ orderId }` object |

## Key architecture

- **`PayPalProvider`** — entry point; loads SDK, creates instance, runs eligibility checks
- **Button components** — `PayPalOneTimePaymentButton`, `VenmoOneTimePaymentButton`, etc.
- **Session hooks** — for custom button UIs with full flow control
- **Card fields** — `PayPalCardFieldsProvider` + field components + session hooks
- **`useEligibleMethods()`** — checks eligibility AND feeds results to button components automatically

## PayPalProvider props (key)

- `clientId` OR `clientToken` — mutually exclusive; both accept `string | Promise<string>`
- `components` — array: `"paypal-payments"`, `"venmo-payments"`, `"paypal-guest-payments"`, `"paypal-subscriptions"`, `"card-fields"`
- `pageType` — `"checkout"`, `"product-details"`, `"cart"`, etc.
- `eligibleMethodsResponse` — SSR pre-fetched eligibility (avoids client-side fetch)

## Button components

| Component | Requires component |
| --- | --- |
| `PayPalOneTimePaymentButton` | `"paypal-payments"` |
| `VenmoOneTimePaymentButton` | `"venmo-payments"` |
| `PayLaterOneTimePaymentButton` | `"paypal-payments"` |
| `PayPalGuestPaymentButton` | `"paypal-guest-payments"` |
| `PayPalSavePaymentButton` | `"paypal-payments"` |
| `PayPalSubscriptionButton` | `"paypal-subscriptions"` |
| `PayPalCreditOneTimePaymentButton` | `"paypal-payments"` |
| `PayPalCreditSavePaymentButton` | `"paypal-payments"` |

## Session hooks (advanced / custom buttons)

| Hook | Notes |
| --- | --- |
| `usePayPalOneTimePaymentSession` | Returns `{ isPending, error, handleClick }` |
| `useVenmoOneTimePaymentSession` | Returns `{ handleClick }` |
| `usePayLaterOneTimePaymentSession` | Returns `{ handleClick }` |
| `usePayPalGuestPaymentSession` | Returns `{ handleClick, buttonRef }` — buttonRef required for guest button |
| `usePayPalSavePaymentSession` | Uses `createVaultToken` not `createOrder` |
| `usePayPalSubscriptionPaymentSession` | Uses `createSubscription` not `createOrder` |
| `usePayPalCreditOneTimePaymentSession` | Uses `<paypal-credit-button>` web component |
| `usePayPalCreditSavePaymentSession` | Uses `createVaultToken` |

## Card fields

```
PayPalProvider (components={["card-fields"]})
  └── PayPalCardFieldsProvider
        ├── PayPalCardNumberField
        ├── PayPalCardExpiryField
        ├── PayPalCardCvvField
        └── usePayPalCardFieldsOneTimePaymentSession  (or Save variant)
              └── submit(orderId) → submitResponse.state: "succeeded" | "failed"
```

## SSR (Next.js)

```typescript
import { useFetchEligibleMethods } from "@paypal/react-paypal-js/sdk-v6/server";
// Server component fetches eligibility → pass to PayPalProvider.eligibleMethodsResponse
```

## Web component custom elements

`<paypal-button>`, `<venmo-button>`, `<paypal-pay-later-button>`, `<paypal-basic-card-container>`, `<paypal-basic-card-button>`, `<paypal-credit-button>`, `<paypal-message>`

## Related pages

- [[source-paypal-react-paypal-js-readme]] — v8.x README (legacy SDK v5 API)
- [[source-github-react-paypal-js-v8]] — v8 GitHub repo
- [[source-paypal-payments-quickstart]] — Underlying PayPal JS SDK v6 quickstart
- [[paypal-checkout]] — PayPal Checkout concept page

## Raw Sources

- [[npm-react-paypal-js]] — verbatim npm README for @paypal/react-paypal-js v9.1.1
