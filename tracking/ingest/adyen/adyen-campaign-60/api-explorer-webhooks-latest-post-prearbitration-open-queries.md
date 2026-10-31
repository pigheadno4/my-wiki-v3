# Fixed retrieval checks: PREARBITRATION_OPEN

## Q1

The captured `Webhooks/latest` `POST /PREARBITRATION_OPEN` is an incoming Adyen disputes notification that the cardholder's bank opened a pre-arbitration case (raw lines 5–7). The item schema requires `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and event-scoped `success`; `originalReference` is optional and described for modifications as the original payment-request reference (lines 18–27). `live`, `notificationItems`, and `NotificationRequestItem` are marked optional in the table (lines 14–16). There is no example payload, specific event-code value in a field, trigger clock, or merchant defense timing rule beyond the heading and bank-action description. Canonical source: [[source-adyen-api-explorer-webhooks-latest-post-prearbitration-open]]; https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_OPEN .

## Q2

The established state is case opening by the cardholder's bank, not a defense or dispute decision (raw line 7). The `200 Success` response says webhook events are accepted by HTTP status code (lines 29–32), which concerns endpoint receipt rather than case resolution or financial state. `success` is defined only as the outcome of the `eventCode`; the page supplies no event payload example or value for this event (lines 19, 27). No delivery ordering, retry/deduplication, signature procedure, reversal, deadline or finality rule is supplied in this 2026-09-15 `latest`-route snapshot. Canonical source: [[source-adyen-api-explorer-webhooks-latest-post-prearbitration-open]]; https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_OPEN .
