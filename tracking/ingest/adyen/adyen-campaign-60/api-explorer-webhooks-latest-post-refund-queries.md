# C60 REFUND fixed retrieval queries

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-refund.md` — https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUND. Pinned raw: `raw/adyen/api-explorer/Webhooks/latest/post/REFUND/2026-09-15.md`.

## Q1

The incoming `Webhooks/latest/post/REFUND` reference reports the result of a request to refund a payment (raw lines 5–7). Its example sets `eventCode: REFUND`, `success: "false"`, and a reason that the transaction had not been captured; it includes EUR amount, `originalReference`, merchant reference and PSP reference (lines 29–55). The item table marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required; top-level `live`/`notificationItems` and the item wrapper are marked optional (lines 11–27). `merchantReference` is the merchant payment reference, `pspReference` Adyen's transaction/request reference, and optional `originalReference` is described for modifications (lines 22–25). `eventDate` records event-generation time (line 20). The example's failed reason is illustrative.

## Q2

`success` describes execution of the event named by `eventCode`; optional `reason` explains a refusal when false (raw lines 26–27). The response section shows `200 Success` and says webhook events are accepted based on HTTP status (lines 56–59). Acceptance of the webhook is distinct from the refund result and cannot prove shopper bank receipt or finality. This endpoint does not state delivery, ordering, retry, deduplication, signature-validation or later-reversal rules. Its `latest` path is a capture label, not a fixed semantic version (lines 1–7); the wider refund lifecycle is routed through `[[adyen-refunds]]`.
