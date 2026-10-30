# Fixed retrieval queries: api-explorer-management-latest-post-me-allowedorigins

Source: `wiki/sources/adyen/source-adyen-api-explorer-management-latest-post-me-allowedorigins.md` — https://docs.adyen.com/api-explorer/Management/latest/post/me/allowedOrigins
Pinned raw: `raw/adyen/api-explorer/Management/latest/post/me/allowedOrigins/2026-09-15.md` (SHA-256 `9c7c195a0278557df70cfade65df982cfc986631535659444ae8a71d873c0af6`).

## Q1

For `Management/latest/post/me/allowedOrigins`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** `POST /me/allowedOrigins` adds an origin to the allowed-origin list of the API credential identified by the API key in the request, so its scope is that credential (raw lines 5–8). Any Management API role can make the request (line 10). The body requires `domain`; `id` and `_links` are optional, and nested `_links.self` is marked required only inside a supplied links object (lines 17–24). This captured endpoint gives no exact domain syntax, wildcard, scheme/port or duplicate rule. It points to separate allowed-origin guidance (line 7). The only server listed is Management API v3 TEST (lines 12–13).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 says the request succeeded and its response requires `domain`, with optional ID and links (lines 26–38). It does not specify propagation timing, browser acceptance, deletion or credential life cycle. Errors listed are 400, 401, 403, 422 and 500 (lines 41–138), without JSON examples. The capture does not prove current live credential access; `latest` is not a fixed version, while the listed server is `/v3` TEST (lines 1–13). No financial outcome is involved.

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-management-latest-post-me-allowedorigins.md` — https://docs.adyen.com/api-explorer/Management/latest/post/me/allowedOrigins
