# Fixed query check — api-explorer-management-latest-get-me

Pinned source: `wiki/sources/adyen/source-adyen-api-explorer-management-latest-get-me.md` — https://docs.adyen.com/api-explorer/Management/latest/get/me
Pinned raw: `raw/adyen/api-explorer/Management/latest/get/me/2026-09-15.md` (SHA-256 `d7c8e9eefed67fab1ef169a868f6aaa139e8b654a0ddb7e0ab8364b3a9e91a9d`).

## Q1
For `Management/latest/get/me`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The captured Management API v3 TEST `GET /me` returns the API credential associated with the request's API key; any Management API role can call it (raw lines 5–12). Its six required top-level success fields are `id`, `username`, `roles`, `active`, `allowedIpAddresses` and public `clientKey` (35–48). The `_links` object is optional; if present, its `self` child is marked required (22–34). The active flag must be true for integration use; an empty IP list allows any source IP, while a nonempty list restricts them (35–36). Optional links may identify merchant-level credential linkage or generation resources; the company link is described specifically as present only for company-level webhooks (22–34). Optional allowed origins, company name, description and subject DN are response details (37–48). This read does not make a management change or prove access to any particular merchant account.

## Q2
What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** HTTP 200 states this credential-details request succeeded (14–17), but the page offers no success example or observed account-specific response. It lists 400, 401, 403, 422 and 500 errors with their schemas (51–148). The response can include `generateApiKey` and `generateClientKey` links whose descriptions mention predecessor-key 24-hour validity on generation; GET /me itself does not generate or rotate keys (27–30). It neither changes roles/active state/IP settings nor verifies a merchant account, payment or transfer. Its `latest` URL, 2026-09-15 capture and TEST `/v3` server do not establish current LIVE credential scope or availability (1–12).
