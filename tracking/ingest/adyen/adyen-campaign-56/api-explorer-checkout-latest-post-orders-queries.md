# api-explorer-checkout-latest-post-orders query answers

Full source: `source-adyen-api-explorer-checkout-latest-post-orders` — https://docs.adyen.com/api-explorer/Checkout/latest/post/orders

Read audit: numbered contiguous raw lines 1–75, 76–150, and 151–225; SHA-256 verified.

- Q1: For `post/orders`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?
  - A: Checkout API v72 `POST /orders` creates a partial-payment **order** before `/payments` when different payment methods are used (raw 5–10). The body table requires `amount` (currency and minor-unit value), `merchantAccount`, and `reference`; `expiresAt` is optional with a one-day default. `Idempotency-Key` is optional (raw 14–28). The example does not add requirements (raw 30–42).
- Q2: For `post/orders`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - A: HTTP 200 says the request succeeded and its `resultCode` is always `Success` for **order creation**; it returns encrypted `orderData`, expiry, initial and remaining amounts (raw 43–69). This does not establish payment authorization, order closure, capture, or settlement. The snapshot lists 400/401/403/422/500 errors (raw 72–139); generic error examples cannot add endpoint body requirements, including the 422 sample's missing return URL despite no `returnUrl` in the body table (raw 20–28, 201–212). The captured server is test v72 under a `latest` URL; no current/live version is proved (raw 1–10).
