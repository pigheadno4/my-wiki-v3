---
title: "GitHub: paypal/paypal-js (SDK v6 + React v9.x)"
type: source
date_ingested: 2026-04-17
original_format: github-repo
raw_files:
  - "github-paypal-js-v6.md"
tags: [paypal, javascript-sdk-v6, react, typescript, npm, hooks, ssr, card-fields, monorepo]
---

## Summary

Monorepo at `github.com/paypal/paypal-js` (commit `ffee35f`). Two packages: `paypal-js` (core script loader) and `react-paypal-js` (React wrapper v9.x for SDK v6). Focused on the `/src/v6/` directories.

## Key implementation insights

### PayPalProvider (`PayPalProvider.tsx`)

- Accepts `clientId | clientToken` (mutually exclusive), plus `components`, `pageType`, `eligibleMethodsResponse`
- On mount: calls the v6 core loader from `paypal-js` and then `createInstance`; eligibility is fetched separately with `useEligibleMethods` or supplied through `eligibleMethodsResponse`
- Uses React context + reducer pattern (`PayPalDispatchContext`) to broadcast SDK state
- `eligibleMethodsResponse` prop enables SSR hydration: skips client-side eligibility fetch if provided

> [!warning] Contradiction
> The original summary said `PayPalProvider` automatically called `findEligibleMethods()` on mount. The exact `@paypal/react-paypal-js@9.3.0` source and cumulative v9 changelog show that the provider's default eligibility request was removed. Client code uses `useEligibleMethods()`; SSR code can supply `eligibleMethodsResponse`. See [[source-github-paypal-js]].

### usePayPalOneTimePaymentSession (`usePayPalOneTimePaymentSession.ts`)

- Accepts `orderId | createOrder` (mutually exclusive) + callbacks
- Returns `{ handleClick, isPending, error }`
- **Critical**: passes `createOrder()` promise (not awaited) to `session.start()` — avoids transient activation issues
- Internally calls `sdkInstance.createPayPalOneTimePaymentSession(callbacks)`

### useEligibleMethods (`useEligibleMethods.ts`)

- Calls `sdkInstance.findEligibleMethods({ currencyCode })`
- Dispatches result to provider reducer — makes eligibility available to all button components via context
- Button components read eligibility from context to self-show/hide

### PayPalCardFieldsProvider (`PayPalCardFieldsProvider.tsx`)

- Creates `CardFieldsSession` via `sdkInstance.createCardFieldsOneTimePaymentSession()`
- Provides session via `PayPalCardFieldsProviderContext`
- Accepts field-level event callbacks: `blur`, `focus`, `change`, `empty`, `notempty`, `validitychange`, `cardtypechange`, `inputsubmit`

### usePayPalCardFieldsOneTimePaymentSession (`usePayPalCardFieldsOneTimePaymentSession.ts`)

- Returns `{ submit, submitResponse, error }`
- `submit(orderId)` calls `cardFieldsSession.submit(orderId, { billingAddress })`
- `submitResponse.state`: `"succeeded"` | `"failed"` | `"canceled"`
- `submitResponse.data.orderId` and `submitResponse.data.liabilityShift` on success

### server.ts (SSR)

- Exports `useFetchEligibleMethods` — async function for Next.js server components
- Takes `{ environment, headers, payload }` — payload is order-like structure for eligibility context
- Returns `FindEligiblePaymentMethodsResponse` to pass to `PayPalProvider.eligibleMethodsResponse`

### Types (`types/index.ts`)

- `OnApproveDataOneTimePayments` — `{ orderId: string }`
- `OnApproveDataSavePayments` — `{ vaultSetupToken: string }`
- `OnCancelDataOneTimePayments`, `OnCancelDataSavePayments`
- `OnErrorData`, `OnCompleteData`
- `INSTANCE_LOADING_STATE` enum: `PENDING | RESOLVED | REJECTED`
- `FindEligiblePaymentMethodsResponse` — returned by `findEligibleMethods`

## Monorepo structure

```
packages/
├── paypal-js/          @paypal/paypal-js — core script loader
│   └── src/v6/         v6 API: loadScript, destroySDKScript
└── react-paypal-js/    @paypal/react-paypal-js — React wrapper
    └── src/v6/
        ├── components/ PayPalProvider, button components, card fields
        ├── hooks/      all session + utility hooks
        ├── context/    React context providers
        ├── types/      TypeScript definitions
        └── server.ts   SSR utilities
```

## Related pages

- [[source-npm-react-paypal-js-v9]] — npm README for @paypal/react-paypal-js v9.1.1 (high-level API docs)
- [[source-paypal-payments-quickstart]] — Underlying PayPal JS SDK v6 quickstart
- [[paypal-checkout]] — PayPal Checkout concept page

## Raw Sources

- [[github-paypal-js-v6]] — stub file with file list and "What each file covers" table
