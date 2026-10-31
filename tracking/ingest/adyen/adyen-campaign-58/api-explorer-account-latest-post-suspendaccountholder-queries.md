# Fixed retrieval audit: api-explorer-account-latest-post-suspendaccountholder

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-suspendaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/suspendAccountHolder

## Q1

For `Account/latest/post/suspendAccountHolder`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** `POST /suspendAccountHolder` changes a Classic account holder's status to `Suspended` at the captured Account API v6 test host; the only request field listed is required `accountHolderCode` (raw lines 5–17). The 401 and 403 sections indicate authentication and sufficient permission, without naming a specific role (lines 116–130). The page gives no additional request prerequisite or idempotency field. Its optional response status object includes a nested required `status`, optional payout/processing states and scheduled event fields; event presence is no proof of execution (lines 35–63). The separate Classic verification guide describes suspended holders as unable to update data, process payments or receive payouts, and advises removing/hiding them from the platform (guide raw lines 136–145). Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-suspendaccountholder.md`; URL: https://docs.adyen.com/api-explorer/Account/latest/post/suspendAccountHolder.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** HTTP 200 is labeled success; HTTP 202 is expressly accepted but incomplete (raw lines 29–30, 66–67). Both response schemas expose optional `accountHolderStatus`, `invalidFields`, `pspReference` and `resultCode`; the nested status enum includes `Active`, `Inactive`, `Suspended`, `Closed` (lines 32–100). `payoutState.allowPayout` aggregates multiple conditions; platform `disabled: false` does not ensure payouts, and an optional scheduled `RefundNotPaidOutTransfers` event is not completed refund evidence (lines 36–54). The separate guide says unsuspension requires no failed verification check and returns the holder to `Inactive` (guide raw lines 104–108, 144); this endpoint does not itself document a completed later transition. Errors 400, 401, 403, 422 and 500 are documented with illustrative 400/403 JSON (raw lines 103–191). The snapshot provides only a v6 test host, no live status, current eligibility, completed propagation, refund or payout proof. Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-suspendaccountholder.md`; URL: https://docs.adyen.com/api-explorer/Account/latest/post/suspendAccountHolder.
