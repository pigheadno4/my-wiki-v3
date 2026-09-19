### Minor Changes

- 4286bfc: Added new PayPalCardNameField component to use with Card Fields
- 7060972: Add React wrappers for all 50 v6 SDK Local Payment Methods (LPMs) to the existing `@paypal/react-paypal-js/sdk-v6` entry. The legacy `@paypal/react-paypal-js` entry remains unaffected.

  Each LPM ships three usage patterns:

  ```tsx
  import {
    PayPalProvider,
    IdealOneTimePaymentButton,
    useIdealOneTimePaymentSession,
    IdealPaymentButton,
  } from "@paypal/react-paypal-js/sdk-v6";
  ```

  - An all-in-one named button, e.g. `IdealOneTimePaymentButton`.
  - A split hook + standalone button, e.g. `useIdealOneTimePaymentSession` + `IdealPaymentButton`.
  - A generic dynamic-selector button, `LPMOneTimePaymentButton`.

  PayPal and LPM components imported from `@paypal/react-paypal-js/sdk-v6` share the same `PayPalProvider`, React context, and SDK instance. Named LPM factory calls are annotated as side-effect free, allowing compatible bundlers to remove unused React wrapper components and hooks. When at least one LPM is used, the shared `LPM_REGISTRY` remains because the factories access it by runtime key.

  The rendered payment fields can be prefilled with initial values (mapping to the SDK `createPaymentFields({ value })` option):
  - `LPMOneTimePaymentButton` (and the named `*OneTimePaymentButton` components) accept a `fieldValues` prop, e.g. `fieldValues={{ name: "John Doe", email: "john@example.com" }}`.
  - The field components returned by the `use*OneTimePaymentSession` hooks accept a `value` prop.

  Each entry in `LPM_REGISTRY` also carries a `testBuyerCountry` (ISO 3166 alpha-2) so sandbox/testing integrations can set the buyer country the LPM session creators require.

- 3dbd4a7: Updates the useVenmo one time payment hook to accept the sandboxSupport object and pass it to .start.

### Patch Changes

- Updated dependencies [d4bc19a]
- Updated dependencies [cb9899e]
- Updated dependencies [a6997f0]
  - @paypal/paypal-js@11.1.0