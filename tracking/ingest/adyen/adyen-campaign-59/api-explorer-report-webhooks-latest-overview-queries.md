# Fixed retrieval answers: Report webhooks v1 overview

## Q1

The 2026-09-15 captured overview is headed **Report webhooks v1**. It says Adyen sends webhooks when reports have been generated and are ready to download, and its sole listed endpoint is incoming `POST balancePlatform.report.created` (“Report generated”). It mentions programmatic HTTP GET and manual Balance Platform Customer Area download. It does not define the POST event payload, required properties, report identity fields or state transitions. See pinned raw lines 5–16; route: [[source-adyen-api-explorer-report-webhooks-latest-overview]], https://docs.adyen.com/api-explorer/report-webhooks/latest/overview.

## Q2

The catalog establishes a report-readiness notification, not proof that a report was downloaded or that the underlying transactions are booked, settled, reconciled or received by a bank. It provides no delivery, ordering, retry, deduplication, signature or event-finality contract and no failure/reversal details. The heading says v1; `latest` is only the captured URL label and does not establish today's current version. See pinned raw lines 5–16; route: [[source-adyen-api-explorer-report-webhooks-latest-overview]], https://docs.adyen.com/api-explorer/report-webhooks/latest/overview.
