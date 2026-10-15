# Adyen Java API library upgrade retrieval probes

## Q1 — Purpose and scope

**Query:** What is the Adyen Java API library upgrade page for, and how does its version relate to Checkout API v72?

**Expected route:** [[source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api-upgrade-api-library]] via [[adyen-online-payments]].

**Answer boundary:** The 2026-09-15 guide is for an online-payments server using the Java API library. It names Java library v40.0.0 or later to support Checkout API v72, with an earlier v4.1.0 library as an example starting point. Distinguish library and API version numbers. It says migration is use-case-specific, not a linear Classic-call mapping; it does not establish successful SDK execution. Raw lines 15–47.

## Q2 — Central transition, credentials and testing limits

**Query:** How does the guide migrate Java server code, and what must remain separate across Advanced versus Sessions, live endpoint configuration, API keys, HMAC, and testing?

**Expected route:** [[source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api-upgrade-api-library]], then [[raw/adyen/docs/online-payments/upgrade-your-integration/migrate-to-checkout-api/upgrade-api-library/2026-09-15]].

**Answer boundary:** Raw lines 49–73 show `Client`/`PaymentsApi` setup with an illustrative LIVE endpoint prefix and API key. Lines 75–113 place `paymentMethods` and card `payments` examples only in the Advanced flow, with test card strings. Lines 115–157 use a separate HMAC key for payment and other webhook verification; the payment sample selects its first item, which is not a universal one-item guarantee. Lines 159–193 show idempotency and error inspection. Lines 195–202 require test-environment coverage after upgrading. Do not infer a universal live region/prefix, require Advanced calls in Sessions, equate API-key and HMAC-key roles, or claim the guide proves payment or webhook success.
