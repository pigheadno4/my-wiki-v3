### Minor Changes

- 0ae4e9d: Add Braintree PayPal Pay Later (BNPL) support and a companion eligibility hook for v6.
  - `useBraintreePayPalPayLaterSession` — manages a Pay Later session (`error`, `isPending`, `handleClick`), consistent with the existing one-time-payment, billing-agreement, and checkout-with-vault hooks.
  - `useBraintreeEligibleMethods` — fetches eligibility via `findEligibleMethods` and caches it on the provider, deduplicating by checkout instance + options and refetching when either changes.
  - Provider-level failures are now surfaced separately and labeled (`Braintree provider error: …`, with the original error as `cause`), distinct from "checkout instance not available", so consumers can tell which layer failed.
  - Add `shippingCallbackUrl`, `shippingAddressOverride` (now typed as `BraintreeShippingAddressOverride` instead of `Record<string, unknown>`), and `contactPreference` options to the one-time, Pay Later, and checkout-with-vault session types.
  - `BraintreeEligibilityResult.getDetails` is now strongly typed per funding source.

- fba3cff: Add `BraintreePayPalPayLaterButton`, a prebuilt v6 button that renders
  `<paypal-pay-later-button>` and drives the Braintree PayPal Pay Later (BNPL) flow via
  `useBraintreePayPalPayLaterSession`, sourcing `countryCode`/`productCode` from provider
  eligibility.

  Docs: clarify that the Pay Later and Credit buttons require eligibility to be fetched first —
  via `useEligibleMethods` (client) or `useFetchEligibleMethods` (server) — with updated JSDoc
  and README examples.

### Patch Changes

- b6e0982: Fix jest-environment-dom package migration bug.
- d4f6cdc: Type the `<paypal-basic-card-button>` JSX element's buyer-country input as the kebab-case `buyer-country` attribute instead of a camelCase `buyerCountry` prop. The element's observed attribute is `buyer-country`, so a camelCase JSX prop is lowercased to `buyercountry` on React <19 and never reaches it. Buyer country is normally determined by the SDK; this only corrects the JSX type for the case where a merchant sets the attribute directly.
- edf33ab: Raises an error when the Google Pay script has not loaded when the React component has mounted.
- a648de2: Fix stale error and potential perpetual loader bug in useEligibleMethods.
- 3b84cd6: Fix: `useFetchEligibleMethods` now requires the `environment` option, matching the `loadCoreSdkScript` / `PayPalProvider` change in v10.0.0. Previously, omitting `environment` silently fell through to the sandbox eligibility API (`https://api-m.sandbox.paypal.com`), which could cause a production server-rendered checkout to hydrate `PayPalProvider` with sandbox eligibility data while the client loaded the production SDK — surfacing as missing or incorrect payment buttons. TypeScript users will now see a compile error if `environment` is omitted; runtime callers will see a thrown `Error`. Pass `environment: "production"` or `environment: "sandbox"` explicitly.

  ```ts
  // Before (silently used sandbox)
  const response = await useFetchEligibleMethods({ headers, payload });

  // After (required)
  const response = await useFetchEligibleMethods({
    environment: "production", // or "sandbox"
    headers,
    payload,
  });
  ```

- Updated dependencies [d7f697b]
- Updated dependencies [983beb7]
- Updated dependencies [7d44dcc]
  - @paypal/paypal-js@10.0.1