<!-- Repo: https://github.com/paypal/paypal-applepay-components -->
<!-- Commit SHA: 258fa156e4bb33f569e865e0f8dc9881f833ef11 -->
<!-- Date reviewed: 2026-04-16 -->
<!-- Detail directory: raw/github-paypal-applepay-component/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-applepay-component/README.md
  raw/github-paypal-applepay-component/src/applepay.js
  raw/github-paypal-applepay-component/src/constants.js
  raw/github-paypal-applepay-component/src/types.js
  raw/github-paypal-applepay-component/src/util.js
  raw/github-paypal-applepay-component/src/index.js
  raw/github-paypal-applepay-component/src/__tests__/applepay.test.js
  raw/github-paypal-applepay-component/src/__tests__/util.test.js
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-applepay-component/ preserving their repo-relative paths -->

# PayPal Apple Pay Component

GitHub: https://github.com/paypal/paypal-applepay-components
Version: 1.8.2

## What each file covers

| File | What to find there |
| --- | --- |
| `raw/github-paypal-applepay-component/README.md` | Repo overview |
| `raw/github-paypal-applepay-component/src/applepay.js` | 3 core functions: config (GraphQL), validateMerchant (GraphQL), confirmOrder (GraphQL mutation + countryCode uppercase fix) |
| `raw/github-paypal-applepay-component/src/constants.js` | FPTI_TRANSITION event names, DEFAULT_GQL_HEADERS |
| `raw/github-paypal-applepay-component/src/types.js` | Flow types: ConfigResponse, ValidateMerchantParams/Response, ConfirmOrderParams, ApplePayPaymentToken, ApplePayPaymentContact, ApplepayType |
| `raw/github-paypal-applepay-component/src/util.js` | mapGetConfigResponse (adds currencyCode + countryCode from GQL response), getMerchantDomain, getCurrency, PayPalApplePayError class |
| `raw/github-paypal-applepay-component/src/index.js` | Main exports |
| `raw/github-paypal-applepay-component/src/__tests__/applepay.test.js` | Tests for config, validateMerchant, confirmOrder including error cases |
| `raw/github-paypal-applepay-component/src/__tests__/util.test.js` | Tests for mapGetConfigResponse, getMerchantDomain |
