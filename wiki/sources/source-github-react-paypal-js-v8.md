---
title: "GitHub: @paypal/react-paypal-js v8.x source"
type: source
date_ingested: 2026-04-13
original_format: github-repo
raw_files:
  - "github-react-paypal-js-v8.md"
tags: [paypal, react, javascript-sdk, github, paypal-script-provider, paypal-buttons, card-fields, hooks, context-api, typescript, v8]
---

## GitHub: @paypal/react-paypal-js v8.x Source

Source code for the React wrapper of the PayPal JS SDK v5. Provides the implementation behind the components and hooks documented in the npm README.

Repo URL: <https://github.com/paypal/paypal-js>

Branch: `release/react-paypal-js-v8` | Package path: `packages/react-paypal-js`

Commit SHA: `a074daab91e24b0f05232e942509f3f268a6a758` | Reviewed: 2026-04-13

## Key Takeaways from Source

### All public exports (`src/index.ts`)

The definitive list of what `@paypal/react-paypal-js` v8 exposes:

**Components:**
`PayPalScriptProvider`, `PayPalButtons`, `PayPalMarks`, `PayPalMessages`, `BraintreePayPalButtons`, `PayPalHostedFieldsProvider`, `PayPalHostedField`, `PayPalCardFieldsProvider`, `PayPalCardFieldsForm`, `PayPalNameField`, `PayPalNumberField`, `PayPalExpiryField`, `PayPalCVVField`

**Hooks:**
`usePayPalScriptReducer` (from `scriptProviderHooks`), `usePayPalHostedFields`, `usePayPalCardFields`

**Constants:**
`FUNDING` — re-exported from `@paypal/sdk-constants` with proper TypeScript typing (addresses a known issue where the upstream module lacks type definitions)

### `PayPalScriptProvider` internals (`src/components/PayPalScriptProvider.tsx`)

- Calls `loadScript()` from `@paypal/paypal-js` on mount (unless `deferLoading={true}`)
- Dispatches `LOADING_STATUS` actions through context as script loads/fails
- Wraps children in `ScriptContext.Provider`

### `scriptReducer` — the state machine (`src/context/scriptProviderContext.ts`)

Three actions:
- `LOADING_STATUS` — updates `loadingStatus` (INITIAL → PENDING → RESOLVED/REJECTED) and optional error message
- `RESET_OPTIONS` — **destroys the existing script tag** first, then resets to PENDING with new options (this is how currency/locale changes trigger a full SDK reload)
- `SET_BRAINTREE_INSTANCE` — Braintree-specific

Key implementation detail: `RESET_OPTIONS` calls `destroySDKScript()` which removes the `<script>` element from the DOM by its unique ID (hashed from options). This ensures only one SDK script exists at a time.

### `PayPalButtons` lifecycle (`src/components/PayPalButtons.tsx`)

- Waits for `isResolved` before rendering (doesn't render during script load)
- Wraps in `ErrorBoundary` to catch render errors
- Uses `useEffect` to call `paypal.Buttons(props).render(container)` when the script resolves
- Re-renders when props change (style, createOrder, onApprove, etc.)

### Card Fields architecture (`src/components/cardFields/`)

- `PayPalCardFieldsProvider` — creates the `cardFields` instance via `paypal.CardFields({ createOrder, onApprove, onError })`, stores it in a dedicated card fields context
- `PayPalCardField` — base component used by Name/Number/Expiry/CVV fields; calls `cardFields.NameField().render(container)` etc.
- `PayPalCardFieldsForm` — calls `cardFields.Form().render(container)` for the all-in-one variant
- `usePayPalCardFields` hook — reads from card fields context, exposes `{ cardFields, fields }` for `submit()` and per-field DOM manipulation

### TypeScript types

- `ScriptProviderReducerState` — `{ loadingStatus, loadingStatusErrorMessage, options }`
- `PayPalButtonsComponentProps` — extends the JS SDK `ButtonsComponentOptions` (all callbacks + style)
- `PayPalCardFieldsComponentProps` — `createOrder`, `onApprove`, `onError`, `inputEvents`, `style`

## Files Saved

See stub file for full path list and per-file descriptions: [[github-react-paypal-js-v8]]

## Raw Sources

- [[github-react-paypal-js-v8]] — stub file with repo metadata and file navigation table
- Detail directory: `raw/github-react-paypal-js-v8/`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout (Standard)
- [[paypal-expanded-checkout]] — Expanded Checkout (Card Fields)
- [[source-paypal-react-paypal-js-readme]] — npm README (usage docs; this source provides the implementation)
- [[source-github-paypal-js]] — sibling package `@paypal/paypal-js` (the vanilla loader this wraps)
- [[source-paypal-javascript-sdk-reference]] — JS SDK API reference (callbacks consumed by these React components)
