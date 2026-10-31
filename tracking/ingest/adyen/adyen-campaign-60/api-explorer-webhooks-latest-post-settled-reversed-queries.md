# api-explorer-webhooks-latest-post-settled-reversed fixed queries

## Q1

The 2026-09-15 Webhooks `latest` POST /SETTLED_REVERSED snapshot describes a debit reversing a settled transaction when Adyen has not received funds from the scheme or payment method within 30 days of capture; it is available for all payment methods for Sales Day Payout merchants and requires Customer Area enablement (raw lines 5–7; canonical source: https://docs.adyen.com/api-explorer/Webhooks/latest/post/SETTLED_REVERSED). The incoming event example uses `eventCode: "SETTLED_REVERSED"` (line 46). The table marks top-level `live` and `notificationItems` optional, while item `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `originalReference`, `pspReference`, and string `success` are required (lines 14–27). `originalReference` points to the original payment request reference for modifications; `pspReference` is Adyen's transaction/request reference (lines 23–25). `eventDate` is the ISO 8601 generation time (line 20). Example `settlementReference` and `expectedValueDate` are `additionalData` values, not table-required fields (lines 17, 38–41).

## Q2

The reversal event is a debit tied to Adyen's nonreceipt of scheme/method funds within 30 days of capture; it does not prove scheme funding later resumed, re-settlement, or bank receipt (raw line 7; canonical source: https://docs.adyen.com/api-explorer/Webhooks/latest/post/SETTLED_REVERSED). String `success` reports event execution, with optional `reason` on false (lines 26–27), whereas HTTP status controls receiver acceptance (lines 60–63). The table's HTTP POST amount URL-parameter wording differs from the JSON amount object in the example (lines 18, 42–45); this snapshot does not reconcile them. It states no delivery/order/retry/deduplication, signature, post-reversal recovery, or deprecation rule. `latest` is the captured reference label, not a fixed version.

Canonical source route: [[source-adyen-api-explorer-webhooks-latest-post-settled-reversed]] — https://docs.adyen.com/api-explorer/Webhooks/latest/post/SETTLED_REVERSED.
