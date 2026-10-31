---
title: "Adyen Webhooks latest PREARBITRATION_ACCEPTED notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/PREARBITRATION_ACCEPTED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_ACCEPTED/2026-09-15.md"
tags: [adyen, webhooks, disputes, pre-arbitration]
---

## Overview

This 2026-09-15 snapshot of the Adyen Webhooks `latest` API Explorer POST reference identifies `PREARBITRATION_ACCEPTED` as an incoming notification for an accepted pre-arbitration case. The page does not identify who accepted the case or give a request example. It is a webhook reference, not a merchant action to accept a dispute. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The item table marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. It marks outer `live` and `notificationItems`, the item wrapper, `additionalData`, and `originalReference` optional. These are the table's schema markings; no example on this page illustrates which optional fields appear for this event.
- `merchantReference` is the merchant's payment reference, `pspReference` identifies Adyen's associated transaction or request, and the table describes `originalReference` for modifications. `eventDate` records when the event was generated. `success` reports whether the named event executed successfully; optional `reason` is described for a false `success` value. Do not read `success` as a separate chargeback, payment, or settlement outcome.
- The response section shows `200 Success` and says webhook events are accepted on the basis of HTTP status. That describes notification acceptance, not a new pre-arbitration decision.

## Detail locators

- Pinned raw, lines 5–7: endpoint title and accepted-case description.
- Pinned raw, lines 11–27: request body table, field requiredness and descriptions.
- Pinned raw, lines 29–32: HTTP status acceptance.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_ACCEPTED/2026-09-15|PREARBITRATION_ACCEPTED API Explorer reference, captured 2026-09-15]]
