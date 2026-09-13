### Patch Changes

- 24ccc6a: Correct the `PayPalOneTimePaymentButton` README example to include the required `onApprove` callback.

  The example previously rendered `<PayPalOneTimePaymentButton orderId="ORDER-123" />` without `onApprove`, which does not type-check now that `onApprove` is correctly required for one-time PayPal payments ([#1020](https://github.com/paypal/paypal-js/issues/1020)).

- eb54388: Emit a nested `dist/v6/esm/package.json` with `{"type":"module"}` so the v6 ESM bundles (main and server) are correctly signaled as ES modules.

  The v6 build outputs ESM syntax into `.js` files, but the package has no root `"type":"module"` (it can't — that would relabel the v5 CJS bundles). Under Node's resolution rules those `.js` files therefore default to CommonJS, so a native ESM import of `@paypal/react-paypal-js/sdk-v6` (or `/sdk-v6/server`) triggers a `MODULE_TYPELESS_PACKAGE_JSON` warning plus a reparse penalty on modern Node, and fails to load outright on older Node or loaders without ESM syntax detection. The nested marker scopes the ESM declaration to the v6 directory only, leaving the v5 CJS artifacts untouched.

- Updated dependencies [39f147e]
- Updated dependencies [24ccc6a]
- Updated dependencies [eb54388]
  - @paypal/paypal-js@11.0.1