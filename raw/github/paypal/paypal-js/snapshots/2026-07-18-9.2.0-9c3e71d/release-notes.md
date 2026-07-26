### Minor Changes

-   dc4957a: Adds Braintree PayPal One Time Payment Session hook.
-   c103e7c: Adds Braintree PayPal Provider and context hook.
-   8615050: Updates typescript to version minimum 5.9.3
-   4974af9: Adding ApplePay OnetimePayment hook and button component

### Patch Changes

-   ffee35f: Fix to prevent merchant paymentRequest from overriding SDK-managed Apple Pay config
-   f37e7bb: Fixes a root package-lock missing caret for typescript.
-   88bd1b3: Fix useEligibleMethods hook returning isLoading=false with stale eligibility data when payload changes (e.g., navigating between different payment flows)
-   309d308: Use default prettier settings for code formatting
-   4f63e24: Enhances the create payment session utility to account for the Braintree hook use case.
-   Updated dependencies [f37e7bb]
-   Updated dependencies [4974af9]
-   Updated dependencies [aea0e42]
-   Updated dependencies [8615050]
-   Updated dependencies [309d308]
    -   @paypal/paypal-js@9.7.0
