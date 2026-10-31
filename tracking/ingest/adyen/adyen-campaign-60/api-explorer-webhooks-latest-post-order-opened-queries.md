# Fixed retrieval answers — Webhooks latest POST /ORDER_OPENED

## Q1

[[source-adyen-api-explorer-webhooks-latest-post-order-opened]] routes to the 2026-09-15 snapshot of the Adyen Webhooks `latest` incoming POST /ORDER_OPENED reference ([canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/ORDER_OPENED)). The page says the first partial payment was made and the order created (raw lines 5–7). Its item example uses `eventCode: ORDER_OPENED` and `success: \"true\"` (lines 42–48). The nested table marks amount, eventCode, eventDate, merchantAccountCode, merchantReference, pspReference and success required (lines 18–27), while originalReference is optional and generically describes the original payment request for modifications (line 23); the example omits it. Outer `live` and `notificationItems` are marked No (lines 14–16). No further trigger timing or order resource ID is defined here.

## Q2

[[source-adyen-api-explorer-webhooks-latest-post-order-opened]] records `200 Success` and HTTP-status-based webhook acceptance (raw lines 54–57; [canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/ORDER_OPENED)). That receipt is separate from the item's required `success` event outcome; optional `reason` explains refusal when success is false (lines 26–27). The page describes order creation, not order completion, capture, settlement or bank receipt (lines 5–7). It supplies no delivery/order/retry/deduplication/signature guarantee. `latest` is the captured route label, not a numeric version pin.
