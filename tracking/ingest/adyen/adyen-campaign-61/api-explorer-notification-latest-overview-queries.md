# Fixed query answers — api-explorer-notification-latest-overview

## Q1

The 2026-09-15 capture is the **Classic Platforms – Notifications v6** API Explorer overview. Adyen produces notifications for endpoints specified in a subscription, while the separate Notification Configuration API manages those subscriptions. The page directs new implementations to its newer integration guide. Its 19-row POST catalog names event types including `/ACCOUNT_CLOSED`, `/ACCOUNT_CREATED`, `/PAYMENT_FAILURE` (failed capture/refund booking), `/REPORT_AVAILABLE`, and `/TRANSFER_FUNDS` (funds transferred between accounts). It gives no per-event request or response schema, required fields, resource IDs, numeric limits, lifecycle, reversal, deletion or timing rule. Raw lines 5–12 and 14–37. Canonical source: [[source-adyen-api-explorer-notification-latest-overview]]; [API Explorer URL](https://docs.adyen.com/api-explorer/Notification/latest/overview).

## Q2

This overview establishes a catalog and the subscription/configuration split, not acceptance of a specific notification, an account or payment state, or financial completion. It gives no receiver acknowledgement or decision contract, delivery order, retry, deduplication, signature or failure/reversal mechanics. The classic-integration and newer-guide direction is explicit, but the page gives no migration procedure or proof of current availability. Individual event references and the Classic notification documentation are needed for payload and outcome detail. Raw lines 5–12 and 14–37. Canonical source: [[source-adyen-api-explorer-notification-latest-overview]]; [API Explorer URL](https://docs.adyen.com/api-explorer/Notification/latest/overview).
