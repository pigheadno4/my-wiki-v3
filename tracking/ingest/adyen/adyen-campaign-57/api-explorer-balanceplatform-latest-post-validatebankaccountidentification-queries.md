# Fixed query check — api-explorer-balanceplatform-latest-post-validatebankaccountidentification

Pinned source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-post-validatebankaccountidentification.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/validateBankAccountIdentification
Pinned raw: `raw/adyen/api-explorer/balanceplatform/latest/post/validateBankAccountIdentification/2026-09-15.md` (SHA-256 `4d92702d384f5f2aa76cc2514914792c5a7248d8881fee40651062f63ee9e39e`).

## Q1
For `balanceplatform/latest/post/validateBankAccountIdentification`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The captured TEST Balance Platform API v2 `POST /validateBankAccountIdentification` validates bank account identification details before a separate transfer or transfer-instrument creation (raw lines 5–10). Its body table marks only top-level `accountIdentification` required and does not enumerate nested required fields (14–17). The IBAN and US-local request objects are examples, not exhaustive type rules or verified account data (19–41); the same sample values appear in invalid-detail 422 responses (169–208). The 403 section says insufficient permissions but names no role (68–69). There is no account holder, transfer instrument or transfer created by this described call.

## Q2
What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** The 200 section says to inspect the actual response code for status but provides no success-body schema or example (42–46). Errors documented are 401, 403, 422 and 500, with 422 request validation and invalid IBAN or US account/routing examples (48–125, 155–208). The generic 422 example describes changing a payment instrument's balanceAccountId, while the 500 example describes payment-instrument creation, so neither supplies this endpoint's ownership or verification semantics (159–166, 210–222). The page says nothing about bank-account ownership confirmation, transfer-instrument verification/approval, transfer initiation, booking, payout or propagation. The `latest` URL and TEST `/bcl/v2` server in a 2026-09-15 capture do not prove current LIVE availability or a financial outcome (1–10).
