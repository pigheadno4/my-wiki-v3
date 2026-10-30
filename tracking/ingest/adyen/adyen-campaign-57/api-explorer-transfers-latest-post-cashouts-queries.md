# Fixed retrieval queries: api-explorer-transfers-latest-post-cashouts

Source: `wiki/sources/adyen/source-adyen-api-explorer-transfers-latest-post-cashouts.md` — https://docs.adyen.com/api-explorer/transfers/latest/post/cashouts
Pinned raw: `raw/adyen/api-explorer/transfers/latest/post/cashouts/2026-09-15.md` (SHA-256 `933a53125bf1adc80edc7909cf2d3d246a7177120222dcef2e970b365f19a9b6`).

## Q1

For `transfers/latest/post/cashouts`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** `POST /cashouts` initiates a cashout request, on the captured Transfers API v4 TEST server (raw lines 5–10). The body requires an instructing balance-account ID and amount with currency/value in minor units (lines 17–19, 27). Optional `counterparty.transferInstrumentId` names the destination transfer instrument; absent it, funds remain in the instructing balance account after settlement (lines 20–21). The top-level `transferInstrumentId` is superseded in this schema by the counterparty field (line 29). Optional fee contains required nested amount fields if supplied, and description/beneficiary reference are allowed only with the counterparty instrument (lines 22–28). Errors include invalid credential (401) and insufficient permissions (403), but this page names no specific role, capability or eligibility prerequisite (lines 103–123). See the separate Platforms cashout-request guide for those conditions.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 means the request succeeded and returns a cashout ID and transfer references; schema transfer types include `cashoutRepayment` and `cashoutFee` (lines 56–81). The example shows two transfer references and amounts but is not evidence they booked or that a bank received funds (lines 216–259). Listed errors are 400 malformed, 401 invalid credential, 403 permission, 404 not found, 422 validation, 429 rate limit and 500 server failure (lines 84–214). This API page gives no webhook or final settlement/credit state, nor specific capability approval or live eligibility; the captured server is TEST `/btl/v4`, and `latest` is not a fixed release (lines 1–10).

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-transfers-latest-post-cashouts.md` — https://docs.adyen.com/api-explorer/transfers/latest/post/cashouts
