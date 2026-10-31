# C60 AUTORESCUE fixed retrieval queries

Canonical retrieval route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-autorescue.md` — https://docs.adyen.com/api-explorer/Webhooks/latest/post/AUTORESCUE. Pinned raw: `raw/adyen/api-explorer/Webhooks/latest/post/AUTORESCUE/2026-09-15.md`.

## Q1

The `Webhooks/latest/post/AUTORESCUE` reference says the Auto Rescue process ended (raw lines 5–7). This is an incoming POST notification with an example `eventCode` of `AUTORESCUE` (lines 29–59). The item parameter table marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required, while `live`, `notificationItems`, the item wrapper, `additionalData`, and `originalReference` are marked optional (lines 11–27). The table identifies `merchantReference` as the merchant payment reference, `pspReference` as Adyen's transaction/request reference, and `originalReference` as the original payment request reference for modifications (lines 22–25). The example includes `retry.rescueReference`, `merchantOrderReference`, amount, original reference and `hmacSignature` (lines 33–58); it does not make those example values or optional fields universally required. `eventDate` is the event-generation timestamp (line 20).

## Q2

The item `success` value reports whether the `eventCode` event executed successfully; if false, optional `reason` explains refusal (raw lines 26–27). The response section shows `200 Success` and says events are accepted based on HTTP status (lines 60–63), which is a webhook receipt rule rather than payment, capture or settlement proof. This reference provides no delivery ordering, retry, deduplication, signature-verification, or financial-finality contract. The example contains `hmacSignature` but gives no validation rule (lines 38–42). `latest` is the captured API Explorer path label, not a pinned semantic version (lines 1–7). No broader lifecycle conclusion follows from this single process-ended page.
