# C60 PREARBITRATION_ACCEPTED fixed retrieval queries

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-prearbitration-accepted.md` — https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_ACCEPTED. Pinned raw: `raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_ACCEPTED/2026-09-15.md`.

## Q1

The captured `Webhooks/latest/post/PREARBITRATION_ACCEPTED` POST reference identifies a notification that the pre-arbitration case was accepted (raw lines 5–7). It supplies no request example, no identity of the accepting actor, and no case-specific transition sequence. The request-body table marks item `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required, while top-level `live`/`notificationItems`, the item wrapper, `additionalData`, `originalReference`, `paymentMethod`, and `reason` are marked optional (lines 11–27). `merchantReference` identifies the merchant payment reference, `pspReference` is Adyen's transaction/request reference, `originalReference` is described for modifications, and `eventDate` is event-generation time (lines 20–25). The table describes `live` as live/test origin (line 14).

## Q2

`success` reports execution of the event named by `eventCode`; optional `reason` is described for `success = false` (raw lines 26–27). The response section shows `200 Success` and says webhook events are accepted by HTTP status (lines 29–32). HTTP acceptance is separate from the accepted pre-arbitration case described in the heading and cannot establish chargeback, payment, capture, or settlement outcome. The page does not state delivery, ordering, retry, deduplication, or signature-verification rules, and it has no request example to clarify optional fields. `latest` is the captured path label, not a fixed semantic version (lines 1–7).
