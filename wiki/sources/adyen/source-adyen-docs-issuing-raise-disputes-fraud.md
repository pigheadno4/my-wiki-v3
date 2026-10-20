---
title: "Adyen Issuing: Raise a fraud dispute"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/raise-disputes/fraud"
raw_files:
  - "adyen/docs/issuing/raise-disputes/fraud/2026-09-15.md"
tags: [adyen, issuing, cards, fraud, disputes]
---

## Overview

This 2026-09-15-captured Adyen Issuing guide explains how a platform raises a **fraud** dispute for a transaction on an Adyen-issued physical or virtual card, on behalf of its cardholder. If the cardholder notices fraudulent transactions, the guide says to close the card and dispute those transactions; it also says to close a card suspected lost or stolen immediately, even if no fraudulent transaction has occurred. The page defers general requirements and limitations to its parent Raise disputes guide.

## Key takeaways

- Locate the transaction ID through the Balance Platform Accounting Report, Customer Area or Transfer webhooks. Create a dispute with Transfers API `POST /disputes`, `type: fraud`, `transactionId` and required `fraudInfo` fields. The `description` field is limited to 50 characters and must not contain PII. See raw lines 27–47. The illustrated `/btl/api/v4/` request uses a **test** host (raw lines 49–66).
- The creation response supplies a **dispute ID** and initial **draft** status; Adyen sends `balancePlatform.dispute.created`. Keep the dispute ID for attachments, edits, submission, closure and lifecycle lookup. Draft creation is not card-scheme submission or a successful chargeback. See raw lines 68–100.
- Supporting attachments are optional; the cardholder should review the dispute before confirming submission. While still a draft, the platform can use `GET /disputes/{id}` for review and `PATCH /disputes/{id}` for edits. Attachment formats, encoding and size are at raw lines 124–159; review and editing steps are at lines 173–207.
- When the cardholder confirms, the platform submits by PATCHing `status: submitted`. **After submission, the dispute can no longer be updated, have attachments uploaded or deleted, or be closed.** The page describes scheme review and chargeback **if successful**, not a guaranteed recovery. Process `balancePlatform.dispute.updated` status changes; for `chargeback` or `secondPresentment`, match `balancePlatform.transfer.created` by ARN and reconcile the cardholder balance account. See raw lines 209–259.
- `fraudInfo.reportOnly: true` is described as reporting fraud with **no further action such as a chargeback or fee reversal**; its default is false. See raw line 45.

## Source tension

The `reportOnly` description gives a lost/stolen-card example **without fraudulent transactions** (raw line 45), but the same POST table marks `transactionId` required and the creation flow starts by locating a transaction (raw lines 29–47). The captured page does not explain which transaction ID to use when none exists. Do not infer that a transaction-free API report is supported.

The example POST response for dispute `4VXM2L64EHSACNUU` gives ARN `15265674260001677835046` (raw lines 82 and 96), while the created and updated webhook examples for that same dispute ID give ARN `715265674260001677835046` (raw lines 108, 117, 237 and 246). Because later reconciliation instructs ARN matching (raw line 259), these examples are not one coherent correlation specimen; the page does not establish which example ARN is authoritative.

## Detail locators

- Fraud request fields, draft response/statuses and created webhook: [[raw/adyen/docs/issuing/raise-disputes/fraud/2026-09-15|raw lines 27–122]].
- Optional attachments, cardholder review, edits and submission lock: [[raw/adyen/docs/issuing/raise-disputes/fraud/2026-09-15|raw lines 124–253]].
- Status webhooks, transfer correlation and further lifecycle navigation: [[raw/adyen/docs/issuing/raise-disputes/fraud/2026-09-15|raw lines 255–269]].

## Related

- [[adyen-issuing]] — Issuing card and balance-platform source catalog.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/raise-disputes/fraud/2026-09-15|Raise a dispute for fraudulent activities (captured 2026-09-15)]]
