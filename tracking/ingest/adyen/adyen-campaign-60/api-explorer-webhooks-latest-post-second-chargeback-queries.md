# Fixed retrieval answers — api-explorer-webhooks-latest-post-second-chargeback

Canonical source: [[source-adyen-api-explorer-webhooks-latest-post-second-chargeback]]; URL: https://docs.adyen.com/api-explorer/Webhooks/latest/post/SECOND_CHARGEBACK. Pinned raw: `raw/adyen/api-explorer/Webhooks/latest/post/SECOND_CHARGEBACK/2026-09-15.md`.

## Q1

This captured incoming `POST /SECOND_CHARGEBACK` reference says the issuing bank declined material defending the original chargeback and the disputed amount is deducted from the merchant account (raw lines 5–7). The body table marks outer `live`, `notificationItems`, and item wrapper optional, but `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required within the item (lines 11–27). The merchant and PSP references identify the merchant's payment and Adyen transaction/request; `originalReference` is optional and absent in the sample (lines 22–25, 33–59). The amount row says currency/value are URL parameters for HTTP POST, but the example nests them in a JSON object (lines 18, 43–46); the format is unresolved here. The example sets `eventCode: SECOND_CHARGEBACK` and `success: "true"` (lines 47–54), with success scoped to event execution (line 27). The page gives no event timing beyond generic ISO 8601 `eventDate`.

## Q2

The declined defense and deduction are the page's stated event meaning (raw line 7). `success: "true"` in the example means execution of `SECOND_CHARGEBACK`, not a successful defense (lines 27, 47–54). The example's nonempty `reason` with success true differs from the table's conditional refusal explanation (lines 26, 53–54). HTTP status accepts the event at the receiver (lines 60–63), separately from the issuer decision and funds effect; no response body is shown. The page supplies no delivery/order/retry/deduplication/signature rule or deprecation statement. `latest` is a captured route label, not evidence of later versions.
