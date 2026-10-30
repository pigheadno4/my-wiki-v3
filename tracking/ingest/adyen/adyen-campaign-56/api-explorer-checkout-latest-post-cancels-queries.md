# C56 fixed-query audit — api-explorer-checkout-latest-post-cancels

Full raw read: numbered contiguous lines 1–225; SHA-256 15c27b2b07be25b47971c7d0cb3a7a859b410b5bfd4795f99fd56eadee9584d7.

Canonical source: [[source-adyen-api-explorer-checkout-latest-post-cancels]] — https://docs.adyen.com/api-explorer/Checkout/latest/post/cancels

- Q1: For `post/cancels`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?
  - Answer: Captured Checkout API v72 `POST /cancels` asks to cancel an authorized, not-yet-captured payment using its merchant payment `reference` as `paymentReference` (raw lines 5–9, 52). `merchantAccount` and `paymentReference` are marked required properties; optional `reference` identifies this cancel request, not the payment, and is limited to 80 characters (51–53). Optional `Idempotency-Key` is max 64 characters (20–23). By original payment PSP reference, the page routes to a different cancels endpoint; when capture state is uncertain, it routes to reversals (9–11). The page does not separately label the request body required.
- Q2: For `post/cancels`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - Answer: A 201 yields a unique cancellation-request `pspReference` and `status: received`; the later outcome is a `TECHNICAL_CANCEL` webhook, so receipt is not cancellation success or financial finality (7, 67–77). Errors shown are 400, 401, 403, 422 and 500 (80–147). The generic 422 missing-return-URL sample is not a documented `/cancels` request-field requirement (201–212 versus 26–53). The listed server is `checkout-test.adyen.com/v72`, despite `latest` in the page URL; no current-latest or live outcome follows (1, 15–16).
