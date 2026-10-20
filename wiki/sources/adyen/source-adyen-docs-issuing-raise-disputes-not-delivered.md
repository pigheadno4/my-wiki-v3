---
title: "Adyen Issuing: raise a non-delivery dispute"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/raise-disputes/not-delivered"
raw_files:
  - "adyen/docs/issuing/raise-disputes/not-delivered/2026-09-15.md"
tags: [adyen, issuing, disputes, cardholders, non-delivery]
---

## Overview

This 2026-09-15 Issuing guide describes how a platform raises a `notDelivered` dispute for a cardholder who did not receive goods or services and could not resolve the issue with the merchant. The platform should first check whether the merchant already refunded the transaction. The guide creates a draft dispute through the Balance Platform Transfers API, optionally uploads evidence, lets the cardholder review or edit it, then submits it to the card scheme for review and a possible chargeback. Creation or submission does not establish a successful dispute or returned funds.

## Key takeaways

- The page defers its overarching prerequisites and limits to the parent Raise disputes guide; it does not restate them. Find the original transaction ID in the Balance Platform Accounting Report, Customer Area or Transfer webhooks, then `POST /disputes` with `type=notDelivered`, that `transactionId`, and `notDeliveredInfo`. The `descriptionOfIssue`, `isDeliveryLate`, `lastExpectedDate` and `whatWasNotDelivered` fields are marked required inside that object.
- An optional `disputedAmount` cannot exceed the transaction amount; omitting it disputes the whole transaction. If supplied, its currency and minor-unit value are required. Conditional fields include `agreedDeliveryLocation` when delivery was to the wrong location and `didCardholderReturn` when `isDeliveryLate=true`. The free-text dispute `description` must exclude PII and is limited to 50 characters.
- Preserve the returned dispute `id` for attachments, edits, submission, closure and lifecycle tracking. The creation response and `balancePlatform.dispute.created` webhook describe a **draft**. Optional supporting attachments are Base64-encoded JPEG/PDF/TIFF, at most 2 MB; the guide's filename table limits names to 4–17 characters including extension.
- Let the cardholder review the dispute before submission. A draft can be patched without resending the complete object, or moved to `submitted` or `closed`. Once submitted to the card scheme, the dispute cannot be updated, attachments cannot be uploaded or deleted, and it cannot be closed. A `submitted` response or updated webhook records submission, not a win or chargeback.
- Process `balancePlatform.dispute.updated` for later status changes. For `chargeback` or `secondPresentment`, match `balancePlatform.transfer.created` by ARN and reconcile the cardholder balance account. The response example is not valid JSON as printed (missing colons after two keys) and depicts `whatWasNotDelivered` as an object although the request table and request example show a string; use the field table and current API schema before implementing.

## Detail locators

- `## Requirements` and `## 1. Raise a non-delivery dispute`: parent-guide prerequisite link, original transaction ID routes, POST field table, conditional fields, sample request, response status and draft webhook.
- `## 2. Upload attachments (optional)`: file types, encoding, size/name limits and attachment ID.
- `## 3. Review the dispute`, `## 4. Edit dispute details (optional)`, `## 5. Submit the dispute`: cardholder confirmation, partial PATCH, irreversible submission boundary and updated webhook.
- `## 6. Process webhooks for status changes`: later status monitoring, ARN transfer matching and reconciliation.

## Related

- [[adyen-issuing]] — Issuing product context.
- [[adyen]] — provider profile.

## Related raw API references

- [[raw/adyen/docs/issuing/raise-disputes/2026-09-15|Raise disputes]] — parent guide for overarching prerequisites and limits; navigation only, not evidence read for this entry.

## Raw Sources

- [[raw/adyen/docs/issuing/raise-disputes/not-delivered/2026-09-15|Non-delivery dispute guide (fetched 2026-09-15)]]
