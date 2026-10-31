# Fixed queries — Account API POST /closeAccount

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-closeaccount.md` — https://docs.adyen.com/api-explorer/Account/latest/post/closeAccount

## Q1

For `Account/latest/post/closeAccount`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: The 2026-09-15 capture documents TEST Account API v6 `POST /closeAccount` for the account named by required request-body string `accountCode`; it is a Classic account endpoint, not an account-holder or balance-account endpoint. Closure prevents processing transactions, paying out the account's funds, and reopening it; payments made to the closed account go to the liable account. The page lists 401 authentication and 403 insufficient-permission errors but does not specify a named role or other closure prerequisite. See canonical source above; raw `raw/adyen/api-explorer/Account/latest/post/closeAccount/2026-09-15.md` lines 5–17, 80–103.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: HTTP 200 states the request succeeded; 202 states it was accepted while processing remains incomplete. The response fields, including account `status` with `Active`, `Inactive`, `Suspended`, `Closed` values, are optional in both schemas. Error classes include 400, 401, 403, 422 and 500, with generic 400/403 examples. The captured page supplies a TEST v6 server and the close/liable-account effects, but no live availability, completion notification, particular closure outcome, verification approval, payout execution, or bank receipt. A 202 alone therefore cannot prove completed closure or fund movement. See canonical source above; raw lines 5–10, 27–64, 67–155.
