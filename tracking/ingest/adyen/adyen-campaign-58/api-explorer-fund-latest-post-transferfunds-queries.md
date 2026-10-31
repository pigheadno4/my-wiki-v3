# Fixed retrieval answers — api-explorer-fund-latest-post-transferfunds

Canonical source route: [[source-adyen-api-explorer-fund-latest-post-transferfunds]] (`wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-transferfunds.md`), https://docs.adyen.com/api-explorer/Fund/latest/post/transferFunds. Pinned evidence: `raw/adyen/api-explorer/Fund/latest/post/transferFunds/2026-09-15.md` (SHA-256 `52cf80325929ea14161608db5881293c934d3ddceb8c0f9c114148da077dd094`).

## Q1

> For `Fund/latest/post/transferFunds`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

`POST /transferFunds` transfers between accounts in one Classic platform, even when account holders differ (raw lines 5–7). Required request properties are `amount.currency` (three-character ISO code), `amount.value` (integer minor units), `sourceAccountCode`, `destinationAccountCode` and `transferCode`; `merchantReference` is optional for linking transactions (lines 14–23). The source holder must be Active with payouts allowed, and the destination holder must be Active (lines 20–22). Permitted transfer codes vary by platform account and are defined in its service level agreement; the page's local-regulation language is historical source guidance, not a current compliance ruling (lines 5–7, 23). The separate [[source-adyen-docs-classic-platforms-fund-transfer]] says Support enables the feature and codes and additionally requires destination processing allowed (its raw lines 30–48). 401/403 indicate authentication/permission failures, without a named role in this operation reference (operation raw lines 90–113). Route: [[source-adyen-api-explorer-fund-latest-post-transferfunds]], https://docs.adyen.com/api-explorer/Fund/latest/post/transferFunds.

## Q2

> What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The operation labels 200 request succeeded and 202 accepted with processing incomplete (raw lines 39–60). Both response bodies mark `invalidFields`, `merchantReference`, `pspReference` and `resultCode` optional (lines 44–74). `pspReference` identifies the request, not final money movement. The companion Classic guide explicitly says the response only reports receipt and that `TRANSFER_FUNDS` webhooks give the asynchronous outcome (its raw lines 68–81). Errors are 400, 401, 403, 422 and 500 (operation raw lines 77–139). `merchantReference` is not documented as idempotency control (line 21). The captured `cal-test` Fund v6 endpoint gives no current live eligibility, completed transfer, later reversal, or external bank payout proof (lines 9–10). Route: [[source-adyen-api-explorer-fund-latest-post-transferfunds]], https://docs.adyen.com/api-explorer/Fund/latest/post/transferFunds.
