### Minor Changes

- 145d3c5: Adds the Braintree with PayPal Checkout with Vault button component.
- 2bcb79d: Add a new static UI component for braintree paypal one time payment.
- 63d8fca: Add the Braintree-PayPal Billing Agreement Hook
- 61ee8ca: Makes presentationMode optional for v6 buttons and hooks, and sets a default value for each hook.
- 3d3b60e: Add Braintree-PayPal integration documentation.
- 0ff45b7: Implementing GooglePay hook and the button component
- 82da8dd: Adds Braintree Checkout with Vault hook
- 1974cd9: Adds Braintree-PayPal Billing Agreement button component.

### Patch Changes

- 6e97c29: Fix onError type intersection in ApplePayButtonElementProps by adding Omit<HTMLAttributes, "onError"> consistent with ButtonProps pattern
- 658db62: Fixing ApplePay styling issue
- ee72ab1: Update README with Apple component documentation.
- 5112bf2: Fix to prevent ApplePaySession completePayment twice
- Updated dependencies [9007a82]
- Updated dependencies [6e1de75]
- Updated dependencies [0ff45b7]
- Updated dependencies [164d373]
  - @paypal/paypal-js@9.8.0