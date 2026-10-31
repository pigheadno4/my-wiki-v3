---
title: "Adyen Webhooks latest ISSUER_COMMENTS notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/ISSUER_COMMENTS"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/ISSUER_COMMENTS/2026-09-15.md"
tags: [adyen, webhooks, disputes, chargebacks]
---

## Overview

This 2026-09-15 snapshot of the Adyen Webhooks `latest` API Explorer POST reference describes an incoming `ISSUER_COMMENTS` notification. The issuer can include free-text information about why it initiated or continued a dispute; the page says issuer comments can be received for chargebacks and pre-arbitration cases. This is a notification reference, not a merchant dispute action. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The example has `eventCode: ISSUER_COMMENTS` and illustrative `additionalData` keys for issuer-comment type, explanation, dispute amount change reason, cancellation, order details, damaged or defective goods, return attempts, and items not received. `additionalData` is optional in the parameter table; the example does not make these keys required or guarantee every comment type.
- The item table marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. It marks outer `live` and `notificationItems`, the item wrapper, and `originalReference` optional. `merchantReference` is the merchant's payment reference, `pspReference` identifies the associated transaction or request, and `originalReference` is described for modifications.
- `success` describes execution of the event named by `eventCode`, not the outcome or finality of the underlying dispute. The table describes optional `reason` as a refusal explanation if `success` is false, yet the example supplies a nonempty `reason` alongside `success: "true"`. Interpret that field in context; this page does not resolve the mismatch.
- The response section shows `200 Success` and says webhook events are accepted on the basis of HTTP status. That is webhook acceptance, not dispute resolution or a financial outcome.

## Detail locators

- Pinned raw, lines 5–7: event purpose and chargeback/pre-arbitration scope.
- Pinned raw, lines 11–27: envelope and item requiredness, identities, `live`, event time and `success`/`reason` descriptions.
- Pinned raw, lines 29–68: illustrative payload and the `reason`/`success` mismatch.
- Pinned raw, lines 69–72: HTTP status acceptance statement.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/ISSUER_COMMENTS/2026-09-15|ISSUER_COMMENTS API Explorer reference, captured 2026-09-15]]
