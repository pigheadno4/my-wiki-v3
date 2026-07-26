### Major Changes

-   62bf29b: Updated v6 SDK React error handling

### Minor Changes

-   1bf66b4: Render web components using isHydrated.
-   62bf29b: Upgrade react-paypal-js Typescript version to v5.3.3 and update build configuration.
-   aa89d81: Updates PayPalProvider with SDK eligibility hydration.
-   83e4316: Created V6 React Card Field components for each field type
-   ff7fbdb: Updates the V6 rollup config to apply bundle-level use client directive to client bundle.
-   ac3bb9e: Adding error handling to payment session hooks to help merchants identify and resolve when session creation methods throw errors due to missing components.
-   35f2a0b: Adds PayPal Save Payment Button component.
-   13f06a8: Removes v6 PayPalProvider default eligibility request and adds useEligibleMethods hook.
-   62bf29b: Add V6 instance provider and context hook
-   823a813: Adds 3 static UI components: PayPal Credit One Time Payment, PayPal Credit Save Payment, and PayPal Subscriptions.
-   d663dd3: Refactors SDK Web Component typescript declarations.
-   3e3f3c2: Adding dataSdkIntegrationSource to the script tag for analytics purpose
-   7310bfb: Enables using a merchant ID as a prop in the PayPalProvider
-   99b63b3: Adds PayPal Subscription Payment Session hook.
-   3483634: Update the README to account for the react-paypal-js v9 release.
-   62bf29b: Adds 2 methods for client side and server side eligibility methods requests.
-   cd1dc60: Adds rollup plugin copy to include type declaration files in the build.
-   ab6dc9c: Updating PayPalProvider with clientId enhancements
-   36ff502: Changes the homepage URL to point to V6 storybook.

### Patch Changes

-   62bf29b: Add `<PayPalOneTimePaymentButton>`
-   0c02589: Created usePayPalCardFieldsSavePaymentSession hook
-   a2541f0: docs: update react storybook link
-   89ff843: Export v6 session hook argument types and rename some types.
-   2f0f473: Adding isPending to hook and buttons to allow deferred clientToken
-   62bf29b: Fixes a build warning log by upgrading typescript-eslint packages from v5 to v6.
-   62bf29b: Enhancing the Paypal and PayLater hooks to handle redirect and direct app switch presentation modes.
-   62bf29b: Refactor to use names PayPalCardFieldsProvider and PayPalCardFieldsProviderContext
-   a76de16: Fix useEligibleMethods to correctly trigger new API request when payload changes. Previously, if eligibility data already existed in context, the hook would skip fetching even when a different payload was provided. Now the hook compares the current payload with the stored payload using deep equality to determine if a new request is needed.
-   00069d9: Passes savePayment prop to the create session method within the useCreatePayPalOneTimePaymentSession hook.
-   da89628: Add PayPalCardFieldsProviderContext Tests
-   9e81bfc: Revert commit 35b5076e7da9fb252cfa8e33f03fae7be7025980
-   62bf29b: Add v6 paypal-messages hook and types.
-   62bf29b: Adds an early resolve to loadCoreSdkScript if a v6 core script already exists.
-   06ad677: Adds Credit One Time Payment and Credit Save Payment react hooks
-   62bf29b: Update createOrder call in useVenmoOneTimePaymentSession hook to match usePayLaterOneTimePaymentSession
-   e3ffe7a: Fixes a type error in static UI components using the ButtonProps type.
-   c7d1c3c: Fixes a bug caused by exporting a server only function.
-   62bf29b: Adding PayLater UI Component
-   0212046: Checking clientToken to render the PayPalProvider children while rendering the provider
-   81cbb7f: Integrate useEligibleMethods hook into PayLaterOneTimePaymentButton component to automatically fetch and dispatch eligibility to context. Also fixes React Strict Mode compatibility by resetting lastFetchRef on cleanup.
-   62bf29b: Refactor paypal provider test utils.
-   38f520d: Audit and update JSDoc comments for V6 hooks and components. Add missing doc comments for usePayLaterOneTimePaymentSession and useVenmoOneTimePaymentSession, fix inaccurate documentation in useFetchEligibleMethods and usePayPal, and normalize doc style across all payment session hooks and button components.
-   62bf29b: feat: add v5 storybook to github pages
-   62bf29b: Update presentation mode options types and integration.
-   62bf29b: - Default `PayPalProvider` `components` to `["paypal-payments"]`.
    -   Update session hooks to check `loadingStatus` before returning an error for no `sdkInstance`.
    -   `PayPalContext` export was removed since merchants won't need to use that directly.
    -   Check only `window` for `isServer` SSR function.
-   9155ce6: Implement on and update methods on CardFieldsProvider
-   64d7760: Adding BCDC UI button component
-   62bf29b: Created CardFieldsProvider and context for creating and providing Card Fields sessions
-   62bf29b: Adds v6 venmo ui component.
-   f55c494: Update v6 jsx namespace.
-   47db663: Fix useEligibleMethods type imports.
-   d13a400: Adding wrapper for bcdc container
-   62bf29b: Fix lint warnings.
-   169c977: Ensure the paypal-js dependency is at a minimum of v9.3.0
-   165895e: Fixing the hook error handling to be simple and generic
-   62bf29b: Implementing BCDC hook.
-   62bf29b: Created usePayPalCardFieldsOneTimePaymentSession hook
-   62bf29b: Remove ssr tests.
