# Fixed retrieval audit — createAccountHolder

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-createaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/createAccountHolder

## Q1

For `Account/latest/post/createAccountHolder`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Classic Account API v6 test-server operation creates a sub-merchant account holder identified by `accountHolderCode`; a default account is created unless `createDefaultAccount` is false. Required request properties include `accountHolderCode`, `accountHolderDetails`, its address/country, and `legalEntity`. Business/NonProfit requires `businessDetails` and at least one shareholder; Individual requires `individualDetails`; `phoneNumber` is required absent `fullPhoneNumber`, but both business and individual examples omit both phone fields (raw lines 126–177), so neither example is a complete valid-request recipe. POS onboarding requires store details. Supplying a bank UUID on creation fails that bank-account creation but permits holder creation; supplying `legalArrangementCode` fails the request. The 403 error is insufficient permissions. Locators: pinned raw lines 5–25, 31, 54, 67, 73, 89, 100, 117–119, 372–373. Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-createaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/createAccountHolder.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 response schema includes new holder/account codes, holder status, payout/processing states, invalid fields, request reference and verification checks. Its sample `Active` and `allowPayout: true` values illustrate one payload; `allowPayout` aggregates conditions such as KYC and disablement. Errors listed are 400, 401, 403, 422 and 500. The page is a 2026-09-15 capture of a v6 test-server endpoint, so it does not prove live eligibility, current availability, approved verification, completed payouts or other money movement. It does not describe a deletion or asynchronous settlement outcome for this operation. Locators: pinned raw lines 9–10, 178–181, 286–343, 346–408, 410–552. Route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-createaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/createAccountHolder.
