# C56 fixed-query audit — api-explorer-payment-latest-post-getauthenticationresult

Full raw read: numbered contiguous lines 1–167; SHA-256 056a3effccb8d8f8d9094fa272874e5ef2c0d88be782989b7de6ee2c7cf6343f.

Canonical source: [[source-adyen-api-explorer-payment-latest-post-getauthenticationresult]] — https://docs.adyen.com/api-explorer/Payment/latest/post/getAuthenticationResult

- Q1: For `Payment/latest/post/getAuthenticationResult`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - Answer: This is Payment API v68 `POST /getAuthenticationResult` on `pal-test`, returning the result after 3DS authentication only (raw lines 5–10). `merchantAccount` used for authentication and transaction `pspReference` are marked required properties (14–18), and both appear in the request example (20–28). The body itself has no separate requiredness label. The related Payment API overview identifies this Classic API as inactive and directs new integrations to Checkout; it does not make this a Checkout endpoint.
- Q2: For `Payment/latest/post/getAuthenticationResult`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - Answer: A 200 can return optional `threeDS1Result` and/or `threeDS2Result` authentication fields, including ECI, values, IDs and status fields (29–58). The raw has no 200 example, payment `resultCode`, authorization/capture/settlement transition or webhook outcome. It lists 400/401/403/422/500 errors; examples only for 400/401/500 (61–167). The captured test server is v68 despite `latest` in the URL, so neither current version nor live payment status follows (1, 9–10).
