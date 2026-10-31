# api-explorer-webhooks-latest-post-expire fixed queries

## Q1

The 2026-09-15 API Explorer Webhooks `latest` POST /EXPIRE reference says the remaining uncaptured amount expired (raw lines 5–7; canonical source: https://docs.adyen.com/api-explorer/Webhooks/latest/post/EXPIRE). It is an incoming event; the example uses `eventCode: "EXPIRE"` inside `NotificationRequestItem` (lines 31–52). The body table marks top-level `live` and `notificationItems` optional, and marks item `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and string `success` required (lines 14–27). The event `amount` is the amount originally authorised, distinct from the remaining uncaptured amount said to expire (lines 7, 18). `originalReference` is optional and described for modifications as corresponding to the original payment request; the example omits it (lines 23, 37–49). The event date is the ISO 8601 generation time (line 20). The page has no separate trigger timing rule or fixed API version beyond the `latest` snapshot label.

## Q2

The EXPIRE item's string `success` is defined as always `true` (raw line 27; canonical source: https://docs.adyen.com/api-explorer/Webhooks/latest/post/EXPIRE). That is event-scoped: the event reports expiry of the uncaptured remainder, not successful capture, settlement, or funds receipt (lines 5–7, 18, 27). The optional `reason` description addresses `success = false`, despite the always-true EXPIRE statement, and the example supplies an empty string (lines 26–27, 47–48). The response lists `200 Success` and says webhook events are accepted on the basis of HTTP status code (lines 54–57); receiver acceptance is distinct from the expiry state. This page provides no delivery/order/retry/deduplication, signature, reversal, or deprecation contract, and `latest` is a snapshot label rather than a fixed API version.

Canonical source route: [[source-adyen-api-explorer-webhooks-latest-post-expire]] — https://docs.adyen.com/api-explorer/Webhooks/latest/post/EXPIRE.
