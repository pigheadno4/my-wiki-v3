# Fixed retrieval audit — unSuspendAccountHolder

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-unsuspendaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/unSuspendAccountHolder

## Q1

For `Account/latest/post/unSuspendAccountHolder`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

This Classic Account API v6 operation targets an existing account holder, identified by required `accountHolderCode`, and moves its status from Suspended to Inactive. Suspension may follow `/suspendAccountHolder` or an expired verification deadline. Unsuspension is allowed only without any verification check in FAILED status. The page lists insufficient permissions as the 403 error. Locators: pinned raw lines 5–20, 132–133. Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-unsuspendaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/unSuspendAccountHolder.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP 200 says the request succeeded; HTTP 202 means accepted for processing but incomplete. Response schemas can report holder status, scheduled events, payout and processing states, validation fields, a request reference and result code. Unsuspension goes to Inactive, not Active; `allowPayout` aggregates KYC and disablement conditions, so neither unsuspension nor a response receipt proves processing or payouts are enabled. Errors listed are 400, 401, 403, 422 and 500. This 2026-09-15 capture names a v6 test server; it does not establish current live availability, completed 202 processing, verification approval, state propagation or financial outcome. No deletion behavior is specified. Locators: pinned raw lines 7–13, 30–103, 106–194. Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-unsuspendaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/unSuspendAccountHolder.
