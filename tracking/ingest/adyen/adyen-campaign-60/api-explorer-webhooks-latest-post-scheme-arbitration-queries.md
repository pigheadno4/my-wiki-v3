# Fixed retrieval checks: SCHEME_ARBITRATION

## Q1

The captured Adyen `Webhooks/latest` `POST /SCHEME_ARBITRATION` is an incoming dispute notification that the issuer escalated a pre-arbitration case to scheme arbitration (raw lines 5–7). The item schema requires `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and event-scoped `success`; `originalReference` is optional and described for modifications as the original payment-request reference (lines 18–27). `live`, `notificationItems`, and `NotificationRequestItem` are marked optional in the table (lines 14–16). There is no example payload, event-specific success value, deadline, or timing sequence in this reference. Canonical source: [[source-adyen-api-explorer-webhooks-latest-post-scheme-arbitration]]; https://docs.adyen.com/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION .

## Q2

The established case state is issuer escalation to scheme arbitration, not an arbitration decision or money movement (raw lines 5–7). The `200 Success` response says webhook events are accepted by HTTP status code (lines 29–32), which concerns receiver acceptance. The schema's `success` is scoped to execution of the event code and has no example value on this page (line 27). No delivery ordering, retry/deduplication, signature verification, reversal, deadline, or financial-finality rule is supplied by this 2026-09-15 `latest`-route snapshot. Canonical source: [[source-adyen-api-explorer-webhooks-latest-post-scheme-arbitration]]; https://docs.adyen.com/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION .
