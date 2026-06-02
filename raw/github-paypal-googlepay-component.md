<!-- Repo: https://github.com/paypal/paypal-googlepay-component -->
<!-- Commit SHA: 513783dd408f5c8deb723c7b063a2142c589f985 -->
<!-- Date reviewed: 2026-04-16 -->
<!-- Detail directory: raw/github-paypal-googlepay-component/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-googlepay-component/README.md
  raw/github-paypal-googlepay-component/src/googlepay.js
  raw/github-paypal-googlepay-component/src/constants.js
  raw/github-paypal-googlepay-component/src/types.js
  raw/github-paypal-googlepay-component/src/util.js
  raw/github-paypal-googlepay-component/src/index.js
  raw/github-paypal-googlepay-component/src/mock.js
  raw/github-paypal-googlepay-component/src/__tests__/googlepay.test.js
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-googlepay-component/ preserving their repo-relative paths -->

# PayPal Google Pay Component (with 3DS)

GitHub: https://github.com/paypal/paypal-googlepay-component
Version: 1.3.5

## What each file covers

| File | What to find there |
| --- | --- |
| `raw/github-paypal-googlepay-component/README.md` | Repo overview |
| `raw/github-paypal-googlepay-component/src/googlepay.js` | 3 core functions: googlePayConfig (GraphQL), confirmOrder (GraphQL mutation), initiatePayerAction (3DS via getThreeDomainSecureComponent) |
| `raw/github-paypal-googlepay-component/src/constants.js` | FPTI_TRANSITION event names, DEFAULT_GQL_HEADERS, ORDER_INTENT values |
| `raw/github-paypal-googlepay-component/src/types.js` | Flow types: ConfigResponse, ConfirmOrderParams, ApprovePaymentResponse, GooglePayType, GooglePayPaymentMethodData, GooglePayPaymentContact |
| `raw/github-paypal-googlepay-component/src/util.js` | Helper utilities: getMerchantDomain, getPayPalDomain, getConfigQuery (GraphQL query builder), PayPalGooglePayError class |
| `raw/github-paypal-googlepay-component/src/index.js` | Main exports |
| `raw/github-paypal-googlepay-component/src/mock.js` | Mock data for config and confirmOrder responses |
| `raw/github-paypal-googlepay-component/src/__tests__/googlepay.test.js` | Test cases: config fetch, confirmOrder, 3DS flow, error handling |
