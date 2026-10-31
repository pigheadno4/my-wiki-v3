# api-explorer-webhooks-latest-post-prearbitration-won fixed queries

## Q1

The 2026-09-15 Webhooks `latest` POST /PREARBITRATION_WON snapshot says the cardholder's bank accepted the pre-arbitration case (raw lines 5–7; canonical source: https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_WON). It is an incoming event. The example places `eventCode: "PREARBITRATION_WON"` in a `NotificationRequestItem` (lines 31–53). The table marks top-level `live` and `notificationItems` optional, and item `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and string `success` required (lines 14–27). `merchantReference` is the merchant payment reference and `pspReference` Adyen's transaction/request reference; `originalReference` is optional and described for modifications, but absent in the example (lines 22–25, 37–49). `eventDate` is the ISO 8601 generation time (line 20). The generic amount URL-parameter wording and JSON amount example are unresolved here (lines 18, 38–41).

## Q2

`success` reports execution outcome of the named event, while HTTP status controls webhook acceptance (raw lines 26–27, 55–58; canonical source: https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_WON). The case event is cardholder-bank acceptance of pre-arbitration; the example's `success: "true"` and empty reason do not prove a credited amount, settlement, or all subsequent dispute finality (lines 5–7, 42–49). The page gives no delivery/order/retry/deduplication, signature, reversal, deprecation, or subsequent arbitration rule. `latest` is a captured reference label, not a fixed version.

Canonical source route: [[source-adyen-api-explorer-webhooks-latest-post-prearbitration-won]] — https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_WON.
