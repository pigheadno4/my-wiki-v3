# Fixed query answers — api-explorer-dispute-webhooks-latest-post-balanceplatform-dispute-updated

Canonical route: [[source-adyen-api-explorer-dispute-webhooks-latest-post-balanceplatform-dispute-updated]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.updated). Pinned raw: `raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.updated/2026-09-15.md`.

## Q1

The captured incoming `balancePlatform.dispute.updated` POST reference says Adyen sends it when a dispute is updated and that it only informs the server of requests (raw lines 5–7). The body table requires `data` and top-level webhook `type`; all direct `data` fields are optional, including dispute resource `id`, transaction `transactionId`, capture `arn`, `status`, `statusDetail`, dispute `type`, and `disputedAmount` (raw lines 14–27). No status/type values or request example are supplied. If `disputedAmount` is present, `currency` and minor-unit `value` are required within it. Its description says the amount cannot exceed the transaction amount and if no amount was provided, the entire transaction amount is disputed; this is not proof of a particular outcome from an omitted webhook field (raw lines 19–21).

## Q2

The event describes a dispute update/request notification, not a final win/loss, refund, reversal, or booked funds movement (raw lines 5–7, 23–26). Optional `status` and `statusDetail` report status information when supplied; the page gives no enum or lifecycle mapping. `arn` and `transactionId` are separately described identifiers and neither is required (raw lines 15, 23–25). A receiver accepts the event with any HTTP `2xx`, which does not decide the dispute (raw lines 29–37). This page does not list an environment or queued timestamp, or define delivery order, retry/deduplication, signatures, later financial outcomes, or a numbered/current version (raw lines 1–7, 9–37).
