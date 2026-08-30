### Minor Changes

- c3b5dbe: Add 3D Secure (SCA) support to the Google Pay one-time payment hook and button.

  When `confirmOrder` returns `PAYER_ACTION_REQUIRED`, `useGooglePayOneTimePaymentSession`
  (and `GooglePayOneTimePaymentButton`) now launches the payer-action flow automatically. The
  3DS modal runs after Google's payment sheet closes, and `onApprove` fires only once the
  buyer completes authentication — so merchants never capture an unauthenticated order. The
  `onApprove` data now carries the resulting `liabilityShift` (via the new
  `GooglePayOnApproveData` type). A buyer cancel or authentication failure is reported through
  `onError`.

- 6b10c2b: Remove PayPal's homegrown `ApplePaySession` browser-global typing from the v6 types.

  `@paypal/react-paypal-js` now types Apple's native session via `@types/applepayjs` internally. If you reference Apple Pay's native browser global in your own code, use the bare `ApplePaySession` global (e.g. `typeof ApplePaySession !== "undefined" && ApplePaySession.canMakePayments()`) and install the community typings: `npm install --save-dev @types/applepayjs`.

### Patch Changes

- Updated dependencies [c3b5dbe]
- Updated dependencies [6b10c2b]
- Updated dependencies [be48634]
- Updated dependencies [be48634]
  - @paypal/paypal-js@11.0.0