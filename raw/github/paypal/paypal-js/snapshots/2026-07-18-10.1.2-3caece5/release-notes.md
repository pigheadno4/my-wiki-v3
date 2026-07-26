### Patch Changes

- 110a043: `ApplePayOneTimePaymentButton` no longer writes a `disabled` attribute to Apple's `<apple-pay-button>`, which ignored it and manages its own enabled/disabled state internally via `canMakePayments()`. The non-functional `disabled` prop has been removed — merchants control presentation themselves.
- a987b2e: Adds 1 enum value to the paypal messages element logoType property.
- Updated dependencies [4619c74]
  - @paypal/paypal-js@10.0.3