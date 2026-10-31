# C60 PREARBITRATION_LOST fixed-query answers

## Q1

The 2026-09-15 Adyen Webhooks `latest` POST `/PREARBITRATION_LOST` snapshot describes an incoming event: the cardholder's bank declined the pre-arbitration case (raw lines 5–7; [[source-adyen-api-explorer-webhooks-latest-post-prearbitration-lost]]; https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_LOST). The item table requires amount, eventCode, eventDate, merchantAccountCode, merchantReference, pspReference, and success, while originalReference is optional (raw lines 18–27). The sample has `PREARBITRATION_LOST`, EUR 1000, a pspReference, reason text, and `success: "true"`; it lacks originalReference (raw lines 44–55). Success is defined for execution of the named event (raw line 27).

## Q2

The response section says HTTP status governs webhook-event acceptance and labels `200 Success` (raw lines 61–64; [[source-adyen-api-explorer-webhooks-latest-post-prearbitration-lost]]; https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_LOST). This receiver acceptance is separate from the reported bank decline, and the example's event-scoped `success=true` is not payment success (raw lines 5–7, 27, 48–55). The generic reason description says refusal text appears when `success=false`, while the sample has reason text with `success=true` (raw lines 26, 54–55). The page gives no later dispute-stage, funds-movement, delivery-order, retry, deduplication, or signature-verification guarantee; `latest` is a captured label, not a fixed version (raw lines 1–5).
