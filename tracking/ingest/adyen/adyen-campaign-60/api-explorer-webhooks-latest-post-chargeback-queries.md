# Fixed retrieval checks: CHARGEBACK

## Q1

The 2026-09-15 captured `Webhooks/latest` `POST /CHARGEBACK` is an incoming Adyen payment chargeback notification: the payment was charged back and funds were deducted from the account (raw lines 5–7). The request example sets `eventCode` to `CHARGEBACK` (line 57), `live` to test (`false`, line 34), and supplies a notification item containing payment amount, merchant account/reference, original payment reference, and Adyen `pspReference` (lines 53–65). The schema marks item `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and event-scoped `success` required; `originalReference` is optional, and `reason` is explained for `success=false` (lines 18–27). It states no general trigger clock or defense transition. Canonical route: https://docs.adyen.com/api-explorer/Webhooks/latest/post/CHARGEBACK ; source stem: `source-adyen-api-explorer-webhooks-latest-post-chargeback`.

## Q2

The page states the charged-back, deducted-funds event (line 7), while its `200 Success` response says webhook acceptance is based on HTTP status code (lines 71–74); receipt acceptance is a different action. The sample's `defensePeriodEndsAt`, `defendable`, `hmacSignature` and capture IDs occur in generic `additionalData` (lines 38–52), without a requiredness, verification or defense-process rule. This pinned page specifies no delivery ordering, retry/deduplication guarantee, signature-validation procedure, reversal/finality rule, or version beyond the `latest` route and 2026-09-15 snapshot. Canonical route: https://docs.adyen.com/api-explorer/Webhooks/latest/post/CHARGEBACK ; source stem: `source-adyen-api-explorer-webhooks-latest-post-chargeback`.
