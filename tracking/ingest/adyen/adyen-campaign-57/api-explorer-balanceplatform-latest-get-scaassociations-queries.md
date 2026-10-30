# Fixed query audit: GET /scaAssociations

Source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-get-scaassociations.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/get/scaAssociations

## Q1

For `balanceplatform/latest/get/scaAssociations`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Balance Platform API v2 test-server GET endpoint returns a paginated list of SCA device associations for an entity (raw lines 5–10). Query parameters `entityId` and `entityType` select an account holder, legal entity or payment instrument; the table marks these and `pageNumber`/`pageSize` required, yet states defaults zero/five for the latter two (lines 14–20). It does not resolve omission behavior. The page names no role or other prerequisite, but documents 401 authentication and 403 insufficient-permission responses (lines 72–92).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 response lists association entries with device and entity identifiers/types, `createdAt`, and `active` or `pendingApproval` status, plus pagination totals and links (lines 24–50). The two-entry JSON is illustrative (lines 128–163). Errors cover 400 validation, 401 authentication, 403 permission, and 500 processing (lines 53–126). `pendingApproval` does not establish approval; this GET response documents no create/delete transition, verification, propagation timing, payment or funds movement. The source URL says `latest`, while its displayed server is `https://balanceplatform-api-test.adyen.com/bcl/v2` (lines 1, 9–10); it cannot prove current latest version or live availability.
