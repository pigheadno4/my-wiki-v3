# C57 fixed query answers: list company accounts

Canonical source route: [[source-adyen-api-explorer-management-latest-get-companies]] — https://docs.adyen.com/api-explorer/Management/latest/get/companies
Pinned raw: [[raw/adyen/api-explorer/Management/latest/get/companies/2026-09-15]] (captured 2026-09-15).

## Q1

`GET /companies` lists only company accounts accessible to the calling API credential, in pages (raw lines 5–7). The credential must have `Management API—Account read` (lines 9–11). Optional `pageSize` defaults to 10 and tops out at 100; `pageNumber` is optional (lines 18–22). The listed TEST server is Management API `/v3` (lines 13–14). A company account here is distinct from its connected API credentials, users and webhooks, and merchant-account status separately controls processing/payout capability (lines 43–56).

## Q2

A 200 means the list request succeeded; required response counts are `itemsTotal` and `pagesTotal`, while `data` and top-level `_links` are optional. Nested first/last/self are required only within `_links`; next/prev depend on page availability. Company properties including ID, status and data centers are optional in the schema (raw lines 24–58). Status descriptions say Active allows login but does not itself enable merchant processing/payouts; Inactive disables both while permitting login; Closed irreversibly disallows login and processing/payouts (line 56). These descriptions are not state transitions performed by GET. Listed failures are 400, 401, 403, 422 and 500 with common problem fields (lines 61–158). The success example's hrefs use `/v1` despite the declared `/v3` server (lines 13–14, 160–208); TEST livePrefix is empty (lines 49–51). The capture cannot prove live endpoint version, current credential reach, company enablement, merchant status, payment processing or payout execution.
