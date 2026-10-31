# Fixed retrieval audit — api-explorer-payout-latest-overview

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-overview.md` — https://docs.adyen.com/api-explorer/Payout/latest/overview
Pinned raw: `raw/adyen/api-explorer/Payout/latest/overview/2026-09-15.md`

## Q1

**Prompt:** For `Payout/latest/overview`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** It is the legacy **Payout API v68** overview for storing payout details and submitting, confirming or declining payouts. It says the API is deprecated and closed to new integrations, directs new integrations to the Transfers API, and sends existing users to their Adyen contact about migration. Use requires two API credentials with distinct duties: storing/submitting versus confirming/declining. API key and basic authentication examples appear; missing credentials route to Support. The six POST endpoints are `/confirmThirdParty`, `/declineThirdParty`, `/payout`, `/storeDetail`, `/storeDetailAndSubmitThirdParty`, and `/submitThirdParty`. This catalog gives no field or permission-role contract for an individual call. See canonical source Overview/Key takeaways; raw lines 5–45 and 68–78.

## Q2

**Prompt:** What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** This overview has no operation response or error schema, default-denial statement, submission/confirmation outcome, cancellation effect, propagation rule, or recipient-credit evidence. Its endpoint summaries distinguish submit, confirm, decline and instant-card `/payout` as different operations, but do not prove their execution. The capture's endpoint version is `v68`; the listed server is TEST `pal-test`. Live access uses credentials from the live Customer Area and a company-specific prefix host. `latest` in the canonical documentation URL does not prove a newer runtime contract or current eligibility. Its deprecated Payout API is not the newer Transfers API. See canonical source Overview/Key takeaways/Detail locators; raw lines 5–11, 23–29 and 47–78.
