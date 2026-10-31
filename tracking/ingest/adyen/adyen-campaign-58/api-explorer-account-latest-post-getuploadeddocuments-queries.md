# Fixed-query audit: api-explorer-account-latest-post-getuploadeddocuments

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-getuploadeddocuments.md` — https://docs.adyen.com/api-explorer/Account/latest/post/getUploadedDocuments
Pinned evidence: `raw/adyen/api-explorer/Account/latest/post/getUploadedDocuments/2026-09-15.md` (SHA-256 `aa28dd2a719518fd59a978fa49e13e7776bc82ed810a60709b067da701ab7561`).

## Q1

For `Account/latest/post/getUploadedDocuments`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** This Account API v6 TEST operation returns documents previously uploaded for an account holder, which Adyen uses in verification (raw lines 5–10). The request requires `accountHolderCode`; `bankAccountUUID` and `shareholderCode` are optional request selectors (lines 14–19). Separately, the 200 response's document-detail descriptions conditionally require a linked `bankAccountUUID` for bank-statement verification and a linked `shareholderCode` for listed identity documents of a Business legal entity (lines 38–47); those descriptions do not change request-body requiredness. Authentication and permissions are reflected by 401/403 responses (lines 72–86). The captured page's driving-licence back description repeats FRONT, conflicting with the adjacent front description (line 42). Retrieve `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-getuploadeddocuments.md` at https://docs.adyen.com/api-explorer/Account/latest/post/getUploadedDocuments.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 says the request succeeded; `documentDetails` is an optional array, and `documentType` is required within its objects. Other optional response fields include `invalidFields`, request `pspReference`, and `resultCode` (raw lines 30–56). The page lists 400, 401, 403, 422, and 500 error responses, with illustrative 400/403 JSON (lines 59–147). It does not show document-content bytes, a verification approval result, deletion or propagation behavior, or a financial outcome. The sole listed server is TEST Account v6 (lines 9–10), and the raw capture is dated 2026-09-15 (line 2); neither proves current live availability or a particular account holder's verification status. Retrieve `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-getuploadeddocuments.md` at https://docs.adyen.com/api-explorer/Account/latest/post/getUploadedDocuments.
