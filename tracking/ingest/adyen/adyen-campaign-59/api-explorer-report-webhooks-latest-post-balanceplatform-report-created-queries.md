# C59 fixed-query answers: balancePlatform.report.created

Canonical route: [[source-adyen-api-explorer-report-webhooks-latest-post-balanceplatform-report-created]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/report-webhooks/latest/post/balancePlatform.report.created). Evidence: [[raw/adyen/api-explorer/report-webhooks/latest/post/balancePlatform.report.created/2026-09-15]].

## Q1

Adyen sends the incoming `balancePlatform.report.created` event after a report is generated and ready for download, and the body contains a download URL (endpoint raw lines 5–7). The separately captured [[raw/adyen/api-explorer/report-webhooks/latest/overview/2026-09-15|family overview]] is headed Report webhooks v1 (overview raw line 5). The request body requires top-level `data`, `environment`, and `type`, while `timestamp` is optional (endpoint raw lines 13–16, 31–33). Within `data`, `downloadUrl`, `fileName` and `reportType` are required; account-holder, balance-account, platform, resource ID and event date are optional (lines 17–30). The report-type list spans accounting, balance, fee, payment-instrument, payout and statement reports (line 30). The TEST example is one accounting-report notification (lines 35–52), not a definition of every report's content.

## Q2

The event establishes generated-report availability, not that the report was fetched or its transactions reconciled; it does not prove booked funds, settlement or bank receipt (raw lines 7, 35–52). Download requires an authenticated GET, but the prose calls for report credentials from an Adyen contact (line 9) while the `downloadUrl` schema says API credentials (line 27). The source preserves that conflict rather than selecting one. Any `2xx` accepts the webhook (lines 53–61); the sample `[accepted]` response is receiver acknowledgement (lines 63–72). The reference does not state delivery-order, retry, deduplication, signature, failure/reversal or current-version guarantees (full raw lines 1–72).
