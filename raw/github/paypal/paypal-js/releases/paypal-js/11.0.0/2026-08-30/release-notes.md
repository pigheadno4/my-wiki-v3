### Major Changes

- 6b10c2b: A breaking change that removes PayPal's homegrown `ApplePaySession` browser-global typing from the v6 types.

  `@paypal/paypal-js/sdk-v6` no longer declares a stripped `ApplePaySession` class or augments the global `Window` interface with `ApplePaySession`. That augmentation conflicted with the community `@types/applepayjs` package (`TS2717` / `TS2687`), and because it shipped through the `sdk-v6` barrel it landed in every consumer's compilation — even projects that never use Apple Pay.

### Minor Changes

- c3b5dbe: Update the v6 Google Pay types for 3D Secure (SCA) support.

  `GooglePayOneTimePaymentSession.initiatePayerAction` changes from the previous no-op
  placeholder to its real signature — `initiatePayerAction(options: { orderId: string }):
Promise<InitiatePayerActionResponse>` — which resolves with the 3DS `liabilityShift` and
  rejects if the buyer cancels or authentication fails.

  Adds and exports three supporting types: `LiabilityShiftType`
  (`"UNKNOWN" | "NO" | "YES" | "POSSIBLE"`), `InitiatePayerActionOptions`, and
  `InitiatePayerActionResponse`.

- be48634: Add TypeScript types for the v6 local payment methods (LPM) components. `LPMPaymentsInstance` and the `LPMComponents` union are now exported from `@paypal/paypal-js/sdk-v6`, and `SdkInstance`/`Components`/`CreateInstanceOptions` recognize LPM component names (e.g. `"ideal-payments"`, `"bancontact-payments"`) so `createInstance` returns the LPM methods when an LPM component is requested.

  `SdkInstance` now narrows the LPM methods it exposes to only the components actually requested — for example `createInstance({ components: ["ideal-payments"] })` now types `createIdealOneTimePaymentSession` only, instead of surfacing all 50 LPM session-creation methods as optional. This is powered by a new single-source-of-truth `LPMComponentToSessionMethod` map (also exported) and an `LPMInstanceFor<T>` helper type, which replace the previous positionally-aligned `LPMComponents`/`LPMSessionMethodName` unions.

  Remove optional chaining (`?`) from `LPMInstanceFor<T>` methods since requested LPM components are guaranteed to exist at runtime on the SDK instance.

### Patch Changes

- be48634: Make `addressLine2` and `adminArea2` required (not optional) on the LPM `LPMSessionFieldBillingAddress` type, matching the internal SDK's `BillingAddress` shape where both fields are required.