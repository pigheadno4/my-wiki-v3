# Fixed retrieval queries: api-explorer-balanceplatform-latest-post-pins-reveal

Source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-post-pins-reveal.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/pins/reveal
Pinned raw: `raw/adyen/api-explorer/balanceplatform/latest/post/pins/reveal/2026-09-15.md` (SHA-256 `4128c1a937fd69fad11f1ab03d98d9ed7ec29f1a2e92d56b571c2b64b559eac2`).

## Q1

For `balanceplatform/latest/post/pins/reveal`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** `POST /pins/reveal` returns an encrypted PIN block for the specified card, identified by `paymentInstrumentId`; decrypted data may be used to show the PIN in a UI (raw lines 5–7). The credential needs the Bank Issuing PIN Reveal Webservice role (lines 9–11). Request-schema required properties are `paymentInstrumentId` and `encryptedKey`, an encrypted symmetric session key using Adyen's public key (lines 18–22). The request example is illustrative (lines 24–32). The captured server is Balance Platform API v2 TEST (lines 13–14).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 says the request succeeded and its response requires `encryptedPinBlock` plus the 16-digit `token` needed to extract it (lines 35–42, 124–134). The response is encrypted, not a plaintext PIN or proof of decryption, display, cardholder authentication or payment authorization. Listed errors are 401 authentication required, 403 insufficient permission, 422 validation and 500 server error (lines 45–122). Generic 422/500 payloads describe changing a balance account and creating a payment instrument, not PIN-reveal lifecycle constraints (lines 162–188). No deletion, propagation, financial outcome or live account access is established by this TEST snapshot; the `latest` URL is not a fixed release identifier (lines 1–14).

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-post-pins-reveal.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/pins/reveal
