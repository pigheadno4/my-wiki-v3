# C59 fixed-query answers: balancePlatform.mandate.updated

Canonical route: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-mandate-updated]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.updated). Evidence: [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.mandate.updated/2026-09-15]].

## Q1

Adyen sends the incoming `balancePlatform.mandate.updated` webhook when a direct debit mandate is updated; the linked guide is for UK direct debits (raw lines 5–7). The request-body table requires top-level `data`, `environment` and `type`, while `timestamp`, `data.mandate` and every listed mandate child are optional (lines 11–27). Optional children cover balance-account, payment-instrument and mandate IDs, counterparty and timestamps; mandate status lists `pending`, `approved`, `cancelled`, and mandate type lists `bacs` (lines 16–24). No particular status transition is stated. This endpoint page does not state a version; the separately captured [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/overview/2026-09-15|family overview]] is headed Configuration webhooks v2 (overview raw line 5).

## Q2

The event establishes that a mandate was updated, but the optional status field does not establish approval or cancellation for every event (raw lines 7, 16–24). The page does not establish direct-debit authorization, collection, booked funds, settlement or bank receipt. Any `2xx` accepts the webhook (lines 29–37), which is receiver acknowledgement rather than a debit outcome. The endpoint page lacks delivery-order, retry, deduplication, authentication/signature, failure/reversal and current-version guarantees (full raw lines 1–37).
