# C60 CAPTURE_FAILED fixed-query answers

## Q1

The 2026-09-15 snapshot of Adyen Webhooks `latest` POST `/CAPTURE_FAILED` describes an incoming notification for a capture request rejected by the card scheme, not a merchant capture call (raw lines 5–7; https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE_FAILED). `NotificationRequestItem` requires amount, eventCode, eventDate, merchantAccountCode, merchantReference, pspReference, and success; originalReference is optional and maps to the original payment request for modifications (raw lines 18–27). The example has eventCode `CAPTURE_FAILED`, amount EUR 1000, originalReference and pspReference, reason `Capture Failed`, and success `true` (raw lines 43–55). That success flag is scoped to execution of the named event (raw line 27).

## Q2

The page labels `200 Success` and says acceptance of webhook events depends on HTTP status (raw lines 61–64; https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE_FAILED). This is receiver acceptance. The page's stated failure is card-scheme capture rejection (raw line 7); the example's success value does not reverse that failure (raw lines 47–55). The captured reference gives no delivery ordering, retry, deduplication, signature-verification procedure, recovery instruction, settlement result, or later finality guarantee. The `latest` label is a captured snapshot, not a pinned semantic version (raw lines 1–5).

Canonical source route: [[source-adyen-api-explorer-webhooks-latest-post-capture-failed]] — https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE_FAILED.
