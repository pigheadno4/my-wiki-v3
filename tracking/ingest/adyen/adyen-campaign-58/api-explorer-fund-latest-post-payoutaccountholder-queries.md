# Fixed retrieval audit: api-explorer-fund-latest-post-payoutaccountholder

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-payoutaccountholder.md` — https://docs.adyen.com/api-explorer/Fund/latest/post/payoutAccountHolder

## Q1

For `Fund/latest/post/payoutAccountHolder`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The Classic Fund API v6 test-host request pays out from `accountCode` to its owning `accountHolderCode`, both marked required (raw lines 5–18). `amount` is top-level optional in this table despite the stated purpose of a specified amount; nested `currency` and minor-unit `value` are required if amount is supplied, and multi-currency accounts require currency selection (lines 19–21). Optional holder-owned `bankAccountUUID` or `payoutMethodCode` selects the destination, with automatic selection described when either is blank; the page does not resolve precedence if both are set (lines 19, 22, 25). `payoutSpeed` permits `STANDARD`/`SAME_DAY`; merchant reference and description are optional, with a 200-character/character-set constraint. The example description uses an en dash outside that set (lines 23–42). Authentication and permissions are reflected by 401/403 errors, without a named role (lines 98–112). Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-payoutaccountholder.md`; URL: https://docs.adyen.com/api-explorer/Fund/latest/post/payoutAccountHolder.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** HTTP 200 is labeled success; 202 is accepted but explicitly incomplete. Both response schemas have optional bank UUID, invalid fields, merchant reference, payout speed, request-identifying `pspReference` and result code (raw lines 43–82). The separate Classic manual-payout guide says to wait for `ACCOUNT_HOLDER_PAYOUT` (guide raw line 105), whose status guide distinguishes Initiated, Confirmed and Failed and allows later bank return even after Confirmed (notification raw lines 20–55). Thus a 200, 202, reference or bank UUID is not recipient-credit evidence. Errors 400, 401, 403, 422 and 500 are listed (raw lines 85–147). This snapshot names only a v6 test host (lines 1–10); it establishes no live account eligibility, available balance, destination approval, current speed availability or completed payout. Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-payoutaccountholder.md`; URL: https://docs.adyen.com/api-explorer/Fund/latest/post/payoutAccountHolder.
