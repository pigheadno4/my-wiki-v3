# Fixed-query audit: api-explorer-account-latest-post-updateaccount

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-updateaccount.md` — https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount
Pinned evidence: `raw/adyen/api-explorer/Account/latest/post/updateAccount/2026-09-15.md`, SHA-256 `918ae5d7027201b4a0ac0cfcf69fbbb9443c10bf1c57cd3df8e68f0b9d5923f0`.

## Q1

For `Account/latest/post/updateAccount`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: This Account API v6 TEST endpoint updates an account; `accountCode` is the only top-level property marked required (raw lines 5–17). Optional `bankAccountUUID` and `payoutMethodCode` couple holder-held bank/card payout destinations; cross-currency bank routing is specified at line 18. Optional metadata update deletes omitted existing pairs (line 20). If `payoutSchedule` is present, nested `schedule` is marked required, and `reason` is required for `HOLD`; `HOLD` stops scheduled but permits manual payouts (lines 22–25). The action choices for existing batches are `CLOSE`, `UPDATE`, and default `NOTHING` (line 23). Payout speed values/default and description restrictions are at lines 19, 26. The page lists 401 authentication and 403 insufficient permissions, but no specific role (lines 107–130). Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-updateaccount.md` — https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount; raw locator `## Parameters > ### Request body`.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: 200 says request succeeded; 202 says accepted for processing but incomplete (raw lines 40–91). Both response tables mark `accountCode` required and other returned update fields, `invalidFields`, `pspReference`, and `resultCode` optional; `invalidFields` may identify fields causing the request to fail (lines 45–91). Listed errors are 400, 401, 403, 422, 500 (lines 94–156); example 400/403 bodies are at lines 158–182. The explicit deletion effect is omitted existing metadata pairs during metadata update (line 20); `CLOSE` closes an existing scheduled-payout batch (line 23). The page supplies no verification approval, payout execution, bank receipt, propagation timing or live eligibility evidence. The only server shown is Account API v6 TEST (line 10). Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-updateaccount.md` — https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount; raw locators `## Responses`, `## Response examples`.
