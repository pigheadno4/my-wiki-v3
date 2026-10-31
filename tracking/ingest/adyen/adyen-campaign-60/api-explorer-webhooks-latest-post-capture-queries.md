# Fixed retrieval answers — Webhooks latest POST /CAPTURE

## Q1

The 2026-09-15 snapshot is the Adyen Webhooks `latest` incoming POST /CAPTURE result-of-capture-request reference, not a merchant capture operation (raw lines 5–7; [canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE)). The item uses `eventCode` (the example is `CAPTURE`, lines 42–50) and required string `success` for the event outcome (lines 19, 27). Required nested fields include amount, eventDate, merchantAccountCode, merchantReference and pspReference (lines 18–27); `originalReference` is optional and points to the original payment request for modifications (line 23). Outer `live` and `notificationItems` are marked No in this table (lines 14–16). The page does not state a capture-trigger timing rule beyond identifying the request result.

## Q2

The response shows 200 Success and says webhook acceptance is based on HTTP status (raw lines 56–59; [canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE)). That acceptance is separate from the item's required `success` outcome; when false, optional `reason` gives a short refusal explanation (lines 26–27). The example's success true is only an example (lines 29–55). This page gives no delivery/order/retry/deduplication/signature rule, later capture-failure, settlement or bank-receipt guarantee. `latest` is a snapshot route, not a pinned numeric API version.

Canonical source route: [[source-adyen-api-explorer-webhooks-latest-post-capture]] — https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE.
