# Fixed retrieval answers — Webhooks latest POST /PREARBITRATION_DECLINED

## Q1

[[source-adyen-api-explorer-webhooks-latest-post-prearbitration-declined]] is the canonical retrieval route for the 2026-09-15 Adyen Webhooks `latest` incoming POST /PREARBITRATION_DECLINED reference ([canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_DECLINED)). It states that the pre-arbitration case was declined (raw lines 5–7). The schema uses a `DisputesNotificationRequestItemWrapper` (line 15) and marks nested amount, eventCode, eventDate, merchantAccountCode, merchantReference, pspReference and success required (lines 18–27). Optional originalReference has a generic modification/original-payment definition (line 23). Outer live and notificationItems are marked No (lines 14–16). No example, case ID, specific decline reason, next stage or timing rule appears.

## Q2

[[source-adyen-api-explorer-webhooks-latest-post-prearbitration-declined]] shows `200 Success` and says HTTP status controls webhook acceptance (raw lines 29–32; [canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_DECLINED)). The nested `success` string is the named event's execution outcome, with optional `reason` for a false result (lines 26–27); neither field is a general payment or dispute-win verdict. The page provides no delivery/order/retry/deduplication/signature rule or financial-finality guarantee. `latest` is a captured route label, not a numeric version pin.
