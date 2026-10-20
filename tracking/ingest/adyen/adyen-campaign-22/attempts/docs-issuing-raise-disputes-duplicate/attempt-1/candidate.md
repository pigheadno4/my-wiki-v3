---
title: "Adyen Issuing: raise a duplicate-charge dispute"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/raise-disputes/duplicate"
raw_files:
  - "adyen/docs/issuing/raise-disputes/duplicate/2026-09-15.md"
tags: [adyen, issuing, disputes, duplicate-charges, cardholders]
---

## Overview

This 2026-09-15 Issuing guide describes a platform raising a `duplicate` dispute for two charges for one purchase, either on the same card or on two Adyen-issued cards. The platform uses the Balance Platform Transfers API to create a draft against one transaction and identify its matching duplicate, offers the cardholder review and optional evidence, then submits to the card scheme for review and a possible chargeback. A draft or submitted status does not establish a win or returned funds.

## Key takeaways

- The page defers overarching requirements, limits and preparations to the parent Raise disputes guide. Find both transaction IDs using the Balance Platform Accounting Report, Customer Area or Transfer webhooks. `POST /disputes` with `type=duplicate`, the disputed `transactionId`, and `duplicateInfo` containing the other `duplicateTransactionId` and `sameCard`; `sameIssuer` is optional. The disputed and duplicate transactions must have the same amount. The optional `description` is limited to 50 characters and must contain no PII.
- Keep the returned dispute `id` for attachments, updates, submission, closure and lifecycle tracking. Creation returns `draft` and is followed by a `balancePlatform.dispute.created` webhook. Optional supporting attachments are Base64-encoded JPEG/PDF/TIFF files of at most 2 MB; the filename table limits names to 4–17 characters including extension.
- Let the cardholder review the draft. The page allows a partial PATCH without resending the whole dispute object. After the cardholder confirms submission, PATCH the dispute status to `submitted`. Submission to the card scheme ends the ability to update or close the dispute or upload/delete attachments; a `submitted` response and updated webhook show submission, not chargeback success.
- Process `balancePlatform.dispute.updated` for later states. For `chargeback` or `secondPresentment`, match `balancePlatform.transfer.created` by ARN and reconcile the cardholder balance account. The request/response examples show `sameCard` and `sameIssuer` as quoted strings even though the field tables call them booleans; the PATCH table also labels `duplicateTransactionId` boolean while the POST table and examples use a string. These examples are not reliable schema proof.

## Detail locators

- `## Requirements` and `## 1. Raise a duplicate charge dispute`: parent-guide requirement link, transaction-ID sources, POST fields, same-amount condition, sample payload, draft response and created webhook.
- `## 2. Upload attachments (optional)`: accepted file types, encoding, size/name limits and attachment ID.
- `## 3. Review the dispute` through `## 5. Submit the dispute`: cardholder review, partial PATCH and irreversible submission boundary.
- `## 6. Process webhooks for status changes`: dispute status, ARN matching and account reconciliation.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[adyen]] — provider context.

## Related raw API references

- [[raw/adyen/docs/issuing/raise-disputes/2026-09-15|Raise disputes]] — parent guide for overarching requirements and lifecycle; navigation only for this entry.

## Raw Sources

- [[raw/adyen/docs/issuing/raise-disputes/duplicate/2026-09-15|Duplicate-charge dispute guide (fetched 2026-09-15)]]
