# Fixed retrieval answers — api-explorer-webhooks-latest-post-payout-expire

Canonical source: [[source-adyen-api-explorer-webhooks-latest-post-payout-expire]]; URL: https://docs.adyen.com/api-explorer/Webhooks/latest/post/PAYOUT_EXPIRE. Pinned raw: `raw/adyen/api-explorer/Webhooks/latest/post/PAYOUT_EXPIRE/2026-09-15.md`.

## Q1

The captured `POST /PAYOUT_EXPIRE` reference is an incoming notification about an expired payout, and the page expressly deprecates it for new integrations (raw lines 5–11). Its request body lists optional outer `live` and `notificationItems`, with required properties inside `NotificationRequestItem`: `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` (lines 27–43). The `amount` row calls it an object but says HTTP POST currency and value are URL parameters (line 34); the JSON example places both within nested `amount` (lines 54–57). This snapshot does not resolve that representation conflict. The merchant reference identifies the payment for the merchant; the PSP reference identifies Adyen's transaction/request; optional `originalReference` refers to an original payment request for modifications (lines 38–41). The example uses `eventCode: PAYOUT_EXPIRE` and `success: "true"` (lines 58–66); success is explicitly scoped to execution of the event code (line 43). The fragment at line 23 gives no expiry trigger or interval. Response acceptance is by HTTP status code (lines 72–75), with no response body shown.

## Q2

A `PAYOUT_EXPIRE` event with `success: "true"` means the expiry event executed successfully under the field definition; it does not mean payout completion or bank receipt (raw lines 43, 58–66). HTTP status accepts the webhook event and is a separate receiver action (line 75). The page gives no delivery, ordering, retry, deduplication or signature rule, and no more precise expiry timing or payout stage (lines 5–75). It is deprecated for new integrations: new builders are directed to Transfer Webhooks; existing Payout API users are directed to Adyen for migration advice (lines 7–21). `latest` is only the captured reference path, not evidence of future version behavior.
