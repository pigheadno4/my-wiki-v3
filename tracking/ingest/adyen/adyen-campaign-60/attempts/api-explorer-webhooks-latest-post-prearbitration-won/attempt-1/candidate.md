---
title: "Adyen Webhooks latest POST /PREARBITRATION_WON"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_WON"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_WON/2026-09-15.md"
tags: [adyen, webhooks, disputes, prearbitration]
---

## Overview

This 2026-09-15 API Explorer Webhooks `latest` POST /PREARBITRATION_WON snapshot describes an incoming notification that the cardholder's bank accepted the pre-arbitration case. The POST heading names an event, not a merchant operation. See [[adyen]], [[adyen-webhooks]], and [[adyen-risk-management]].

## Key takeaways

- The table marks top-level `live` and `notificationItems` optional. Within a `NotificationRequestItem`, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and string `success` are marked required. The example uses `eventCode: "PREARBITRATION_WON"`; `live` distinguishes live and test origin.
- `merchantReference` identifies the merchant's payment reference; `pspReference` is Adyen's reference for a transaction or request. Optional `originalReference` is described for modifications as corresponding to the original payment request, but is absent from the example. The generic `amount` table calls it the payment amount and says HTTP POST notification currency/value are URL parameters; the JSON example nests currency/value in an amount object. This page does not reconcile those representations or identify the amount as a dispute recovery.
- The string `success` describes whether the named event was executed successfully. If false, optional `reason` gives a refusal explanation. The example shows `success: "true"`, an empty `reason`, and `paymentMethod: "bankTransfer_IBAN"`; these are sample values. The event description identifies the cardholder bank's acceptance of a pre-arbitration case, but this page does not establish settlement, a credited amount, or finality beyond that stated case event.
- The response lists `200 Success` and HTTP-status-based webhook acceptance, distinct from event `success` and the case outcome. This page gives no delivery, ordering, retry, deduplication, signature, reversal, or subsequent arbitration rule.

## Detail locators

- Event identity and cardholder-bank acceptance: raw lines 5–7.
- Body field requiredness, references, amount wording, reason and success scope: raw lines 11–27.
- Example event code, amount, and string success: raw lines 29–54.
- HTTP response acceptance: raw lines 55–58.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_WON/2026-09-15|API Explorer PREARBITRATION_WON webhook reference (2026-09-15)]]
