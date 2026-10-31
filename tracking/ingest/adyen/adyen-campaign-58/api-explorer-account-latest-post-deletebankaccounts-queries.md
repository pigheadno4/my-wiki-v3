# Fixed-query audit: api-explorer-account-latest-post-deletebankaccounts

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-deletebankaccounts.md` — https://docs.adyen.com/api-explorer/Account/latest/post/deleteBankAccounts
Pinned evidence: `raw/adyen/api-explorer/Account/latest/post/deleteBankAccounts/2026-09-15.md`, SHA-256 `5ac39193a4d41414536ec2d0f36dc6ffe6cd3ef2cfbb31033843f3e0eb5eaed1`.

## Q1

For `Account/latest/post/deleteBankAccounts`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: The Account API v6 TEST endpoint `POST /deleteBankAccounts` deletes bank accounts associated with an account holder (raw lines 5–10). The request-property table marks `accountHolderCode` and `bankAccountUUIDs` (array of strings) Yes, identifying the holder and the bank accounts to delete (lines 14–18); the JSON example is at lines 20–30. The page does not separately specify body requiredness, conditional fields, or a particular permission name. It lists authentication required (401) and insufficient permissions (403) as errors (lines 80–103). Deletion is consequential, but no payout, verification, or transfer side effect is documented here. Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-deletebankaccounts.md` — https://docs.adyen.com/api-explorer/Account/latest/post/deleteBankAccounts; raw locators `## Parameters > ### Request body` and `## Responses`.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: A 200 says the request succeeded; a 202 says accepted for processing but not completed (raw lines 31–64). Success fields `invalidFields`, `pspReference`, and `resultCode` are individually optional in the response table (lines 36–64). Listed errors are 400, 401, 403, 422, and 500 with descriptions and optional error fields (lines 67–129); the 400/403 JSON examples are illustrative (lines 131–155). The capture gives no deletion-completion notification, lifecycle/propagation guarantee, verification outcome, payout or bank result, live server, or current eligibility. Its only server is Account API v6 TEST (line 10). Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-deletebankaccounts.md` — https://docs.adyen.com/api-explorer/Account/latest/post/deleteBankAccounts; raw locators `## Responses` and `## Response examples`.
