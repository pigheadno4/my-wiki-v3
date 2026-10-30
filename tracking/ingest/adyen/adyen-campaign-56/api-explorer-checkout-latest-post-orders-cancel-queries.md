## api-explorer-checkout-latest-post-orders-cancel

Pinned raw: `raw/adyen/api-explorer/Checkout/latest/post/orders/cancel/2026-09-15.md`. Canonical source: `source-adyen-api-explorer-checkout-latest-post-orders-cancel` — https://docs.adyen.com/api-explorer/Checkout/latest/post/orders/cancel

- Q1: For `post/orders/cancel`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?
  - A: It requests cancellation of an order. The captured Checkout API page lists the v72 test server; the required body has `merchantAccount` and `order`, with matching encrypted `orderData` and order `pspReference`. `Idempotency-Key` is optional. The stated effect is rollback of payments in that order through cancellation or refund, depending on method (raw lines 5–26).
- Q2: For `post/orders/cancel`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - A: A 200 response includes a cancellation-request `pspReference` and `resultCode: Received`, meaning Adyen received the request for processing, not that cancellations/refunds finished. The page lists 400, 401, 403, 422 and 500 errors with examples (raw lines 40–119, 121–194). The `latest` URL is a captured v72 test-server snapshot; it supplies no live outcome or current-version proof (raw lines 1–10).
