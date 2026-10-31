# Fixed retrieval answers — api-explorer-account-latest-post-deleteshareholders

Canonical source route: [[source-adyen-api-explorer-account-latest-post-deleteshareholders]] (`wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-deleteshareholders.md`), https://docs.adyen.com/api-explorer/Account/latest/post/deleteShareholders. Pinned evidence: `raw/adyen/api-explorer/Account/latest/post/deleteShareholders/2026-09-15.md` (SHA-256 `2f1d07259c3ba3d4a5dcb3543448c00b104f5864a6b0e98581fd240554c10042`).

## Q1

> For `Account/latest/post/deleteShareholders`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

It documents `POST /deleteShareholders` for deleting shareholders associated with a Classic account holder (raw lines 5–7). The request body table requires `accountHolderCode` (the account holder from which deletion is made) and `shareholderCodes` (an array of codes for shareholders to delete); the one-code example is illustrative (lines 12–30). This is destructive for the selected records. A 401 means authentication is required and a 403 means permissions are insufficient (lines 80–103); no named role or additional prerequisite is specified here. The captured server is TEST Account API v6 (lines 9–10). Route: [[source-adyen-api-explorer-account-latest-post-deleteshareholders]], https://docs.adyen.com/api-explorer/Account/latest/post/deleteShareholders.

## Q2

> What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The page labels 200 “The request has succeeded” (lines 31–47) and 202 “accepted for processing” with processing **not completed** (lines 50–64). Both schemas show optional `invalidFields`, `pspReference` and `resultCode`; `invalidFields` can describe validation errors that prevent processing (lines 36–64). The listed error classes are 400, 401, 403, 422 and 500, with only generic 400/403 JSON examples (lines 67–155). The 202 receipt is not confirmation that shareholders were removed. No final signal, propagation timing, verification/approval result or money-movement effect is specified. This captured TEST v6 reference does not prove current live availability or a performed deletion (lines 9–10). Route: [[source-adyen-api-explorer-account-latest-post-deleteshareholders]], https://docs.adyen.com/api-explorer/Account/latest/post/deleteShareholders.
