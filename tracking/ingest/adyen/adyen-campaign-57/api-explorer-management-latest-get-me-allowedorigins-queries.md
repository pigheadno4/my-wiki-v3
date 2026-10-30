# Fixed retrieval answers: api-explorer-management-latest-get-me-allowedorigins

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-management-latest-get-me-allowedorigins.md` — https://docs.adyen.com/api-explorer/Management/latest/get/me/allowedOrigins

## Q1: For `Management/latest/get/me/allowedOrigins`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

`GET /me/allowedOrigins` lists allowed-origin records for the API credential selected by the API key used in the request. Any Management API role may make the request. The capture shows the Management API v3 TEST server and no path/query/body parameter table; the response identifies domains and optionally origin IDs. This API-key credential scope differs from a client key or all credentials on an account. [Raw lines 5–26.]

## Q2: What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 schema has optional top-level `data`; within an item, `domain` and `_links.self` are marked required, while `id` and `_links` are optional. No response example appears. Errors listed are 400, 401, 403, 422 and 500. A GET response establishes retrieval only, not origin creation/deletion, propagation timing, client-key validity, browser acceptance, live configuration, verification or payment outcome; the shown server is TEST `/v3` despite `latest` in the URL. [Raw lines 11–126.]
