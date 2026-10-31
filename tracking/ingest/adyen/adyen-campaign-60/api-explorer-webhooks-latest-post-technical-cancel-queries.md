# C60 fixed-query answers: TECHNICAL_CANCEL

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-technical-cancel.md`; canonical URL: `https://docs.adyen.com/api-explorer/Webhooks/latest/post/TECHNICAL_CANCEL`.

## Q1

The captured `Webhooks/latest` POST reference is an incoming `TECHNICAL_CANCEL` notification reporting the result of a technical cancel request (raw lines 5–7); it is not the merchant cancellation request endpoint. The displayed request table marks top-level `live`, `notificationItems`, and nested `NotificationRequestItem` wrapper optional, while `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` within an item are required (lines 11–27). `eventCode` identifies the event type and is `TECHNICAL_CANCEL` in the example (lines 19, 45). `merchantReference` is the merchant's payment reference; `pspReference` is Adyen's transaction or request reference; optional `originalReference` corresponds to the original payment request for modifications (lines 22–25). `success` is the event outcome, with `reason` described if false (lines 26–27). The example shows test-origin EUR 1000 and distinct original and PSP references; it is illustrative (lines 29–58). `eventDate` is event-generation time (line 20); this page does not give technical-cancel request eligibility or a timing limit.

## Q2

`success` reports whether the `TECHNICAL_CANCEL` event executed, while the response section lists `200 Success` and says webhook events are accepted based on HTTP status (raw lines 27, 59–62). Receiver acceptance is distinct from the technical-cancel result. The event is a cancellation-result notification, with no refund, settlement, or bank-receipt claim here (lines 5–7). The 62-line reference gives no delivery-order, retry, deduplication, signature-verification, or later financial-finality rule. `latest` is a captured API Explorer path; the immutable raw was fetched 2026-09-15 (lines 1–3). Follow the canonical source route above for the evidence and raw link.
