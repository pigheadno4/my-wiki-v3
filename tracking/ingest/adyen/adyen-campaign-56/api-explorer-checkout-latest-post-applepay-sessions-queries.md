# Fixed retrieval checks — api-explorer-checkout-latest-post-applepay-sessions

Canonical source: [[source-adyen-api-explorer-checkout-latest-post-applepay-sessions]] — https://docs.adyen.com/api-explorer/Checkout/latest/post/applePay/sessions
Pinned capture: `raw/adyen/api-explorer/Checkout/latest/post/applePay/sessions/2026-09-15.md` (2026-09-15); Checkout API v72 TEST server. Read audit: contiguous numbered raw lines 1–58; SHA-256 verified against trusted input.

## Q1: For `post/applePay/sessions`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?

This endpoint returns Apple Pay session data for merchant/session validation in an API-only Apple Pay integration using Adyen's Apple Pay certificate (raw lines 5–9). It is distinct from Checkout payment-session creation and payment authorization. The request table marks `displayName`, `domainName`, and `merchantIdentifier` required: merchant name and ID come from `/paymentMethods` configuration, while the Customer Area Apple Pay domain must match `window.location.hostname` (lines 22–27). The captured server is v72 TEST (lines 11–12).

## Q2: For `post/applePay/sessions`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP 200 establishes request success; the response body contains required Base64 encoded `data` for completing Apple Pay merchant validation (raw lines 39–47). Its abbreviated body is illustrative (lines 49–58). No error-response schema or failure examples appear in this capture, and the response does not establish completed validation, payment authorization, capture or settlement. The `latest` URL preserves this captured v72 TEST snapshot, not current live/latest availability (lines 1–2, 11–12).
