<!-- Repo: https://github.com/paypal/paypal-js -->
<!-- Commit SHA: ffee35fcf23a510d691931ec237624edbb4762b2 -->
<!-- Date reviewed: 2026-04-17 -->
<!-- Detail directory: raw/github-paypal-js-v6/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-js-v6/packages/paypal-js/src/v6/index.ts
  raw/github-paypal-js-v6/packages/paypal-js/src/load-script.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/index.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/components/PayPalProvider.tsx
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/components/PayPalOneTimePaymentButton.tsx
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/usePayPalOneTimePaymentSession.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/useEligibleMethods.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/usePayPal.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/components/PayPalCardFieldsProvider.tsx
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/usePayPalCardFieldsOneTimePaymentSession.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/types/index.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/server.ts
  raw/github-paypal-js-v6/packages/react-paypal-js/README.md
  raw/github-paypal-js-v6/packages/react-paypal-js/CHANGELOG.md
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/paypal/paypal-js at commit ffee35fcf23a510d691931ec237624edbb4762b2, then save any newly discovered files into raw/github-paypal-js-v6/ preserving their repo-relative paths -->

# paypal/paypal-js — SDK v6 + React v9.x

Monorepo containing two packages:
- `packages/paypal-js` — core JS SDK script loader
- `packages/react-paypal-js` — React wrapper (v9.x, SDK v6 API)

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-paypal-js-v6/packages/paypal-js/src/v6/index.ts` | v6 SDK entry: `loadScript`, `destroySDKScript`, types |
| `raw/github-paypal-js-v6/packages/paypal-js/src/load-script.ts` | Core script loading logic, caching, options validation |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/index.ts` | Public exports for `@paypal/react-paypal-js/sdk-v6` |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/components/PayPalProvider.tsx` | Provider implementation: SDK init, eligibility, context dispatch |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/components/PayPalOneTimePaymentButton.tsx` | One-time payment button: uses session hook + web component |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/usePayPalOneTimePaymentSession.ts` | Core session hook: createOrder/orderId, handleClick, presentationMode |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/useEligibleMethods.ts` | Eligibility check hook, dispatches to provider reducer |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/usePayPal.ts` | SDK context accessor: sdkInstance, loadingStatus, error, isHydrated |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/components/PayPalCardFieldsProvider.tsx` | Card Fields session provider, field event callbacks |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/hooks/usePayPalCardFieldsOneTimePaymentSession.ts` | Card Fields submit + submitResponse state machine |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/types/index.ts` | All TypeScript types and interfaces for SDK v6 |
| `raw/github-paypal-js-v6/packages/react-paypal-js/src/v6/server.ts` | SSR: useFetchEligibleMethods for Next.js server components |
| `raw/github-paypal-js-v6/packages/react-paypal-js/README.md` | Full package README with all components, hooks, migration guide |
| `raw/github-paypal-js-v6/packages/react-paypal-js/CHANGELOG.md` | Version history, v9.0 breaking changes |
