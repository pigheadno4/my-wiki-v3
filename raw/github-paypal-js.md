<!-- Repo: https://github.com/paypal/paypal-js -->
<!-- Commit SHA: f59f94baefea4b2ddb38553669ed0ac4ede86167 -->
<!-- Date reviewed: 2026-04-13 -->
<!-- Detail directory: raw/github-paypal-js/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-js/packages/paypal-js/README.md
  raw/github-paypal-js/packages/paypal-js/src/load-script.ts
  raw/github-paypal-js/packages/paypal-js/src/utils.ts
  raw/github-paypal-js/packages/paypal-js/types/script-options.d.ts
  raw/github-paypal-js/packages/paypal-js/types/v6/index.d.ts
  raw/github-paypal-js/packages/paypal-js/types/v6/components/paypal-payments.d.ts
  raw/github-paypal-js/packages/paypal-js/types/apis/orders.d.ts
  raw/github-paypal-js/packages/paypal-js/package.json
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-js/ preserving their repo-relative paths -->

## paypal/paypal-js

Monorepo containing two packages:

- `@paypal/paypal-js` — Vanilla JS loader and TypeScript types for the PayPal JS SDK
- `@paypal/react-paypal-js` — React library (README already ingested separately)
- `@paypal/react-paypal-js-storybook` — Storybook docs (not saved — out of scope)

Focus of saved excerpts: the `@paypal/paypal-js` package — `loadScript` API, utility functions, TypeScript types for SDK v5 and v6.

## What each saved file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-paypal-js/packages/paypal-js/README.md` | Full `loadScript` API, v6 SDK `loadCoreSdkScript`, TypeScript usage, merchantId array handling, CDN usage |
| `raw/github-paypal-js/packages/paypal-js/src/load-script.ts` | Caching logic, namespace resolution, `loadCustomScript` implementation, `validateArguments` |
| `raw/github-paypal-js/packages/paypal-js/src/utils.ts` | `processOptions` — how camelCase options are converted to query params and data attributes |
| `raw/github-paypal-js/packages/paypal-js/types/script-options.d.ts` | `PayPalScriptOptions` TypeScript interface — all query params + data attributes |
| `raw/github-paypal-js/packages/paypal-js/types/v6/index.d.ts` | `PayPalV6Namespace`, `createInstance`, `Components` type union, `SdkInstance`, eligibility types |
| `raw/github-paypal-js/packages/paypal-js/types/v6/components/paypal-payments.d.ts` | V6 `paypal-payments` component — session types, `onApprove`, `onShippingAddressChange` |
| `raw/github-paypal-js/packages/paypal-js/types/apis/orders.d.ts` | Orders API TypeScript types |
| `raw/github-paypal-js/packages/paypal-js/package.json` | Package metadata, export paths (`sdk-v6` subpath), peer dependencies |
