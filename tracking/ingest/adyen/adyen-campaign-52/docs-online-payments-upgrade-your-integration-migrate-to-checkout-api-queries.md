# Fixed retrieval checks — Migrate to Checkout API

Source stem: `source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api`
Canonical URL: https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api
Pinned raw: `raw/adyen/docs/online-payments/upgrade-your-integration/migrate-to-checkout-api/2026-09-15.md` (SHA-256 `4a6bf14e3c0cafc57f9d12b1478d3769072b98ec586139610df9ab94ff1f5218`).

## Q1

**Question:** For a Classic API online-payments migration, which Checkout API version and server routes does this guide use, and what must change for a server-only integration?

**Answer:** The main guide targets Checkout API v72 or later; it also describes a v68-to-v68 interim route with possible later upgrade. Server-only migration changes Checkout webservice credential role, endpoint URLs and request objects, including JSON. Its matrix maps `/authorise` to `/payments`, `authorise3d`/`authorise3ds2` to `/payments/details`, and captured-payment refund, cancel, capture, reversal and amount adjustment to `/payments/{paymentPspReference}/...`; cancellation without a PSP reference uses `/cancels`. Void pending refund is unavailable in the Checkout matrix. Use environment-specific live prefix/region. The guide's test base-URL table says `/checkout/{VERSION}` but many v72 examples say `/v72`, so verify the actual versioned endpoint path instead of asserting that the two patterns are identical. Raw lines 56–83, 85–156, 1773–1776, 2349–2614.

**Retrieval route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api.md` → pinned raw lines 56–156 and 2349–2614.

## Q2

**Question:** What client, tokenization, security and payment-outcome qualifications must a Classic-to-Checkout migration preserve?

**Answer:** Classic CSE must be replaced (the guide lists Card Component, Custom Card Component or JWE); unencrypted-card use requires PCI compliance, and the exact PCI scope depends on integration type. Server API authentication still uses an API key or basic credentials, while Drop-in/Components need client key and allowed origins. Tokenization now needs per-request `shopperInteraction` and `recurringProcessingModel`, plus token-lifecycle webhook setup; the Customer Area Recurring toggle is insufficient. For a `/payments` action, handle the indicated voucher/QR/redirect/await/SDK/3DS path, and use webhook outcome where the shopper completes asynchronously or never returns. Redirect return can be sent to `/payments/details` for current payment status, although the later v67+ note says authorization already happens before return and details are no longer needed **to authorize**. Opening “webhooks unchanged” is scoped later to standard v1 webhooks, with SOAP/tokenization/changed AUTHORISATION exceptions. Classic can keep processing live payments during migration; live Checkout verification precedes stopping Classic. Raw lines 160–307, 2747–3123, 3125–3239, 3286–3290.

**Retrieval route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → source stem above → pinned raw lines 160–307, 2747–3239 and 3286–3290.
