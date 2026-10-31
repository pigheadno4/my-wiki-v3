# api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-cardorder-created fixed query answers

Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.created/2026-09-15.md` (SHA-256 `548edf793986eb973d7530c9ebf5897dec84d7fc72f1c21b10e37bcd9bc91940`). Canonical source route: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-cardorder-created.md`. Canonical URL: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.cardorder.created

## Q1

The captured incoming `balancePlatform.cardorder.created` event indicates successful card-order creation after creation of a `type: card`, `formFactor: physical` payment instrument (raw lines 5–7). The required envelope fields are `data`, `environment` (`test` or `live`), and `type`; `timestamp` is optional queue time. Optional `data` fields include balance platform, card/PIN delivery objects, card-order item ID, event-trigger date, resource ID, payment-instrument ID and shipping method (raw lines 11–31). The two test examples identify the card-order item and payment instrument and show processing versus rejected card/PIN statuses, including an image-field error in the rejected example (raw lines 33–73). The raw gives no numbered webhook version; `latest` is the captured route label.

## Q2

Order creation does not establish successful card or PIN production/delivery: the `created` event's rejected example demonstrates the separate delivery outcome (raw lines 54–73). Nor does it prove card activation, payment authorization, capture or settlement. The table describes the `card` object as card delivery but labels nested `card.status` and `card.trackingNumber` as PIN delivery, duplicating the distinct `pin` object; this is an unresolved documentation inconsistency (raw lines 16–28). Any HTTP 2xx accepts the webhook and `notificationResponse` is optional (raw lines 74–82). The page does not establish delivery ordering, retry, deduplication or signature requirements (full raw lines 1–82).
