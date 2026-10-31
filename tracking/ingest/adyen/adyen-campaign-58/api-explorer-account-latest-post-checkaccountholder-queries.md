# Fixed retrieval audit — api-explorer-account-latest-post-checkaccountholder

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-account-latest-post-checkaccountholder.md` — https://docs.adyen.com/api-explorer/Account/latest/post/checkAccountHolder
Pinned raw: `raw/adyen/api-explorer/Account/latest/post/checkAccountHolder/2026-09-15.md`

## Q1

**Prompt:** For `Account/latest/post/checkAccountHolder`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** It documents `POST /checkAccountHolder` to trigger verification of a Classic account holder even before checks are required by current processing volume. The listed server is test `https://cal-test.adyen.com/cal/services/Account/v6`; the URL segment `latest` does not itself prove a different deployed version. The request table marks `accountHolderCode` (string, the Classic holder identifier), `accountStateType` (string, `Processing` or `Payout`), and `tier` (integer) as required properties. The example renders `tier` as a string, so the example and declared table type differ. A 403 means insufficient permissions, but this page does not identify a credential role. See source Overview, Key takeaways, and Detail locators; raw lines 5–30 and 93–103.

## Q2

**Prompt:** What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** 200 is labeled succeeded; 202 is accepted for processing with processing explicitly incomplete. The optional success fields include `invalidFields` (errors preventing processing), `pspReference` (request identifier), and `resultCode`. Listed errors are 400, 401, 403, 422 and 500, with optional error properties and only illustrative 400/403 bodies. This page does not report a completed verification result, approved holder, account state transition, payout eligibility, deletion, propagation, or financial outcome; request success cannot establish those. The only listed server is test Account API v6 in a 2026-09-15 capture; it gives no current live eligibility or production result. For differentiated `Payout` versus `Processing` outcomes and notification route, follow the source's related Classic onboarding guide. See source Key takeaways, Detail locators and Related; raw lines 9–10, 31–64 and 67–155.
