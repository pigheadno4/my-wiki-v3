### Patch Changes

- 39f147e: Guard the `environment` option against prototype pollution in `validateArguments()`.

  `processOptions()` already read `environment` via `Object.prototype.hasOwnProperty.call()`, but `validateArguments()` (v5 `loadScript`) and the v6 `loadCoreSdkScript` validator still destructured it directly, so a polluted `Object.prototype.environment` was picked up before those guards ran. On the v5 path a junk value would throw and break `loadScript()` entirely; on the v6 path a polluted `"sandbox"` value would pass validation and silently load the sandbox SDK. Both validators now use an own-property check so inherited values are ignored.

- 24ccc6a: Make `onApprove` genuinely optional on `PayPalOneTimePaymentSessionOptions` (and its `PayLaterOneTimePaymentSessionOptions` / `PayPalCreditOneTimePaymentSessionOptions` aliases).

  The type intersected `BasePaymentSessionOptions` — where `onApprove` is required — and re-declared `onApprove?` without `Omit`-ing it from the base first. In a TypeScript intersection a property is optional only if it is optional in every constituent, so the `?` had no effect and `onApprove` was required in practice ([#1020](https://github.com/paypal/paypal-js/issues/1020)). Because the presentation mode is only chosen later at `.start()` (a separate call) and redirect flows legitimately have no in-page approval callback, core cannot require `onApprove`. It is now re-added as optional via `Omit<BasePaymentSessionOptions, "onApprove">`, mirroring `SavePaymentSessionOptions`.

- eb54388: Emit a nested `dist/v6/esm/package.json` with `{"type":"module"}` so the v6 ESM bundle is correctly signaled as an ES module.

  The v6 build outputs ESM syntax into `.js` files, but the package has no root `"type":"module"` (it can't — that would relabel the v5 CJS bundles). Under Node's resolution rules those `.js` files therefore default to CommonJS, so a native ESM import of `@paypal/paypal-js/sdk-v6` triggers a `MODULE_TYPELESS_PACKAGE_JSON` warning plus a reparse penalty on modern Node, and fails to load outright on older Node or loaders without ESM syntax detection. The nested marker scopes the ESM declaration to the v6 directory only, leaving the v5 CJS artifacts untouched.