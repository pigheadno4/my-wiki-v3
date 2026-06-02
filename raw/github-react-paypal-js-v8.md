<!-- Repo: https://github.com/paypal/paypal-js -->
<!-- Branch: release/react-paypal-js-v8 -->
<!-- Package path: packages/react-paypal-js -->
<!-- Commit SHA: a074daab91e24b0f05232e942509f3f268a6a758 -->
<!-- Date reviewed: 2026-04-13 -->
<!-- Detail directory: raw/github-react-paypal-js-v8/ -->
<!-- Files saved (read directly from these paths):
  raw/github-react-paypal-js-v8/README.md
  raw/github-react-paypal-js-v8/package.json
  raw/github-react-paypal-js-v8/src/index.ts
  raw/github-react-paypal-js-v8/src/components/PayPalScriptProvider.tsx
  raw/github-react-paypal-js-v8/src/components/PayPalButtons.tsx
  raw/github-react-paypal-js-v8/src/components/cardFields/PayPalCardFieldsProvider.tsx
  raw/github-react-paypal-js-v8/src/components/cardFields/PayPalCardFieldsForm.tsx
  raw/github-react-paypal-js-v8/src/components/cardFields/PayPalCardField.tsx
  raw/github-react-paypal-js-v8/src/components/cardFields/hooks.ts
  raw/github-react-paypal-js-v8/src/hooks/scriptProviderHooks.ts
  raw/github-react-paypal-js-v8/src/context/scriptProviderContext.ts
  raw/github-react-paypal-js-v8/src/types/scriptProviderTypes.ts
  raw/github-react-paypal-js-v8/src/types/paypalButtonTypes.ts
  raw/github-react-paypal-js-v8/src/types/payPalCardFieldsTypes.ts
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at branch release/react-paypal-js-v8, then save any newly discovered files into raw/github-react-paypal-js-v8/ preserving their relative paths from packages/react-paypal-js/ -->

## paypal/paypal-js — @paypal/react-paypal-js v8.x

React wrapper for the PayPal JS SDK v5. Part of the paypal-js monorepo, on the `release/react-paypal-js-v8` branch.

- npm package: `@paypal/react-paypal-js` v8.x
- SDK version: PayPal JS SDK v5 (CardFields)
- README already ingested separately as npm README (see [[source-paypal-react-paypal-js-readme]])

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-react-paypal-js-v8/README.md` | Full usage docs, all components, hooks, integration examples |
| `raw/github-react-paypal-js-v8/package.json` | Version, peer deps (`react >=16.3`, `@paypal/paypal-js`), exports |
| `raw/github-react-paypal-js-v8/src/index.ts` | All public exports — the definitive list of what the package exposes |
| `raw/github-react-paypal-js-v8/src/components/PayPalScriptProvider.tsx` | Core provider — `loadScript()` call, error handling, `deferLoading` logic |
| `raw/github-react-paypal-js-v8/src/components/PayPalButtons.tsx` | Buttons component — all props, `useEffect` lifecycle, re-render logic, error boundary wrapping |
| `raw/github-react-paypal-js-v8/src/components/cardFields/PayPalCardFieldsProvider.tsx` | Card Fields provider — `cardFields` instance creation, `createOrder`/`onApprove`/`onError` wiring |
| `raw/github-react-paypal-js-v8/src/components/cardFields/PayPalCardFieldsForm.tsx` | All-in-one `<PayPalCardFieldsForm />` — renders all 4 fields via `cardFields.Form().render()` |
| `raw/github-react-paypal-js-v8/src/components/cardFields/PayPalCardField.tsx` | Base individual field component — shared by `PayPalNameField`, `PayPalNumberField`, `PayPalExpiryField`, `PayPalCVVField` |
| `raw/github-react-paypal-js-v8/src/components/cardFields/hooks.ts` | `usePayPalCardFields` hook implementation — exposes `cardFields` + individual `fields` refs |
| `raw/github-react-paypal-js-v8/src/hooks/scriptProviderHooks.ts` | `usePayPalScriptReducer` + `usePayPalScriptLoading` hooks — loading state + `resetOptions` dispatch |
| `raw/github-react-paypal-js-v8/src/context/scriptProviderContext.ts` | `ScriptContext` + reducer — loading states (`isInitial`/`isPending`/`isResolved`/`isRejected`), `resetOptions` action |
| `raw/github-react-paypal-js-v8/src/types/scriptProviderTypes.ts` | `PayPalScriptProviderProps`, `ScriptProviderReducerState`, action types |
| `raw/github-react-paypal-js-v8/src/types/paypalButtonTypes.ts` | `PayPalButtonsComponentProps` — all button callback + style prop types |
| `raw/github-react-paypal-js-v8/src/types/payPalCardFieldsTypes.ts` | `PayPalCardFieldsComponentProps`, individual field props, `usePayPalCardFields` return types |
