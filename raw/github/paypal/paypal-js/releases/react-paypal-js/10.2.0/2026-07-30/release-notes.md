### Minor Changes

- d9c0200: Add `useBraintreePayPalMessages`, a v6 hook for rendering PayPal promotional / BNPL messaging (`<paypal-message>`) via Braintree.
  - Wraps `BraintreePayPalCheckoutInstance.createMessages` on the shared instance from `useBraintreePayPal`. Because Braintree's `createMessages` is asynchronous (unlike the PayPal SDK's synchronous `createPayPalMessages`), the instance is created in an effect that awaits the Promise and guards against unmount / instance change before storing it.
  - Returns `error`, `isReady`, `isLoading`, and `handleFetchContent(options)`, which fetches message content for a `<paypal-message>` element and resolves to a content object exposing `update({ amount })` so the displayed amount can change without re-fetching.
  - Provider-level failures are surfaced separately and labeled (`Braintree PayPal context error: …`), distinct from instance/fetch errors, so consumers can tell which layer failed.
  - Adds `BraintreeMessagesOptions`, `BraintreeMessagesInstance`, `BraintreeMessageContent`, and `BraintreeFetchMessageContentOptions` types, plus `createMessages` on `BraintreePayPalCheckoutInstance`.

- 31e7976: Rename the v6 server-side `useFetchEligibleMethods` to `fetchEligibleMethods` and move it out of the `hooks/` directory. It is a plain server-side async function (`import "server-only"`, called with `await`), not a React hook — the `use` prefix falsely signaled a hook and tripped `eslint-plugin-react-hooks` (`rules-of-hooks` / `no-unnecessary-use-prefix`) in consumer projects, producing false "React Hook cannot be called in an async function / conditionally" errors.

  Also renames the client hook `useEligibleMethods`'s public option/result types `UseFetchEligibleMethodsOptions` / `UseFetchEligibleMethodsResult` to `UseEligibleMethodsOptions` / `UseEligibleMethodsResult` to match the hook name.

  All previous names remain exported as `@deprecated` aliases, so this is non-breaking:
  - `useFetchEligibleMethods` → `fetchEligibleMethods` (from `@paypal/react-paypal-js/sdk-v6/server`)
  - `UseFetchEligibleMethodsOptions` → `UseEligibleMethodsOptions`
  - `UseFetchEligibleMethodsResult` → `UseEligibleMethodsResult`

  The deprecated aliases will be removed in the next major release.

### Patch Changes

- 383aa32: This change fixes the condition to skip eligibility request if it has already been server hydrated. This change also updates the README to demonstrate how the SDK can be hydrated with a server-side fetched response via the v6 PayPal Provider.
- e3bb955: Stop shipping the TypeScript incremental-build cache (`dist/tsconfig.lib.tsbuildinfo`) in the published npm package. The build-info file is now written to `node_modules/.cache/tsc/` instead of `dist/`, trimming ~72 kB unpacked (~25 kB gzipped) from the tarball. No functional or API change — the library output is byte-identical.
- Updated dependencies [09f2994]
- Updated dependencies [d9c0200]
  - @paypal/paypal-js@10.1.0