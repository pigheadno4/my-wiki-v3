### Minor Changes

- aa4de45: Adds Venmo vault support to the v6 React SDK:
  - `VenmoOneTimePaymentButton` now accepts a `savePayment` prop to vault the buyer's Venmo account while completing an order (VAULT_WITH_PAYMENT).
  - New `VenmoSavePaymentButton` component for a vault-only flow with no purchase (VAULT_WITHOUT_PAYMENT), supporting both lazy (`createVaultToken`) and eager (`vaultSetupToken`) vault setup token creation.

### Patch Changes

- Updated dependencies [adc91b9]
  - @paypal/paypal-js@11.2.1