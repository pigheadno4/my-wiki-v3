# C60 ISSUER_COMMENTS fixed retrieval queries

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-issuer-comments.md` — https://docs.adyen.com/api-explorer/Webhooks/latest/post/ISSUER_COMMENTS. Pinned raw: `raw/adyen/api-explorer/Webhooks/latest/post/ISSUER_COMMENTS/2026-09-15.md`.

## Q1

The incoming `ISSUER_COMMENTS` POST reference says the issuer included free text relevant to a dispute, such as why it initiated or continued it; comments can be received for chargebacks and pre-arbitration cases (raw lines 5–7). The example sets `eventCode: ISSUER_COMMENTS`, includes optional `additionalData` keys for type and several comment topics, and shows original and PSP references (lines 29–68). The table marks item `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required; top-level `live`/`notificationItems` and the item wrapper are marked optional (lines 11–27). `merchantReference` identifies the merchant payment reference; `pspReference` is Adyen's transaction/request reference; `originalReference` is optional and described for modifications (lines 22–25). `eventDate` is event-generation time (line 20). The example's `issuerComments.type: chargeback` is one example, not a limit on the chargeback/pre-arbitration scope (lines 7, 38–50).

## Q2

`success` reports whether the named event executed successfully, not dispute victory or finality (raw line 27). The parameter table says optional `reason` explains refusal when `success` is false, but the example has a populated reason with `success: "true"`; the page does not reconcile that discrepancy (lines 26, 62–63). The response says `200 Success` and HTTP status determines webhook event acceptance (lines 69–72), which is separate from dispute or financial state. This reference does not state delivery, ordering, retry, deduplication, signature-validation, or finality rules. The `latest` URL is a captured path label rather than a fixed semantic version (lines 1–7).
