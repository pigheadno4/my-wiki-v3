# Fixed retrieval checks — api-explorer-checkout-latest-post-payments-details

Canonical source: [[source-adyen-api-explorer-checkout-latest-post-payments-details]] — https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details
Pinned capture: `raw/adyen/api-explorer/Checkout/latest/post/payments/details/2026-09-15.md` (2026-09-15); Checkout API v72 TEST server. Read audit: contiguous numbered raw lines 1–100, 101–200, 201–293; SHA-256 verified against trusted input.

## Q1: For `post/payments/details`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?

It submits follow-up details for a payment created through `/payments` when that request did not reach a final state, for example after redirect (raw lines 5–7). The request-body table requires the `details` object, while its enumerated children are individually marked optional and flow-specific (lines 20–45). Authentication-only and `paymentData` cases have conditional instructions (lines 23–24, 46–47); the redirect and native 3DS request bodies are examples (lines 49–67). The captured endpoint is on `checkout-test.adyen.com/v72` (line 10).

## Q2: For `post/payments/details`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP 200 establishes request success; optional `action` may require completion work and optional `resultCode` can be final, pending, received, or require shopper interaction (raw lines 70–76, 111). Authentication-only results do not themselves authorize payment (lines 24, 111). The shown `Authorised` 200 body is an example (lines 220–230), not a universal outcome or capture/settlement proof. The page also defines 400/401/403/422/500 failure categories (lines 151–218), with illustrative error bodies (lines 232–293). The `latest` URL points to this captured v72 TEST reference; these lines do not establish live availability or current latest version (lines 1–2, 9–10).
