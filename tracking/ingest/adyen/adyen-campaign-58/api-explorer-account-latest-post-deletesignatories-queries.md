# Fixed retrieval audit — api-explorer-account-latest-post-deletesignatories

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-deletesignatories.md` — https://docs.adyen.com/api-explorer/Account/latest/post/deleteSignatories
Pinned raw: `raw/adyen/api-explorer/Account/latest/post/deleteSignatories/2026-09-15.md`

## Q1

**Prompt:** For `Account/latest/post/deleteSignatories`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** It documents `POST /deleteSignatories`, which deletes signatories associated with a Classic account holder. The test server is `https://cal-test.adyen.com/cal/services/Account/v6`. The request table marks `accountHolderCode` (string, holder **from which** signatories are removed) and `signatoryCodes` (array of strings, signatories **to be deleted**) as required properties. The page gives no request example, array cardinality, idempotency guarantee, or named permission role; 403 is described only as insufficient permissions. See canonical source Overview and Key takeaways; raw lines 5–19 and 82–92.

## Q2

**Prompt:** What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** 200 is labeled request succeeded; 202 means accepted for processing but explicitly incomplete. Optional response fields are `invalidFields` (validation errors that would prevent processing), `pspReference` (request reference), and `resultCode`. Neither 202 nor a reference proves completed deletion or downstream verification change. Listed errors are 400, 401, 403, 422 and 500; body fields are optional, and only 400/403 illustrative examples are shown. The page has no completed-deletion notification, propagation timing, verification outcome, payment/payout result, live-production result or current eligibility evidence. The listed server is test Account API v6 in the 2026-09-15 capture, notwithstanding `latest` in the URL. See canonical source Key takeaways and Detail locators; raw lines 9–10, 20–53 and 56–144.
