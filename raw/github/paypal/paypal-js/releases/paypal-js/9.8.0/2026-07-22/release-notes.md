### Minor Changes

- 0ff45b7: Consolidating the shared GooglePay types to paypal-js package.

### Patch Changes

- 9007a82: Add optional submit options to CardFields submit() method, including billingAddress and name fields for 3DS authentication support
- 6e1de75: Fix a typescript bug that was making .start options required.
- 164d373: Update paypal one time payment session start options to be optional.