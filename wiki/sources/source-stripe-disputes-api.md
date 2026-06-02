---
title: "Stripe — Use the API to Respond to Disputes"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-api-2026.md"
tags: [stripe, disputes, chargebacks, api, evidence, file-upload, webhooks]
---

## Summary

Programmatic dispute management via the Stripe API: retrieve, update (evidence submission), and list disputes. Covers evidence types, file upload, and multiple disputes on one payment.

## Core API Operations

### Retrieve a Dispute
```js
stripe.disputes.retrieve('{{DISPUTE_ID}}')
```
Returns `Dispute` object including `evidence`, `evidence_details.due_by` (deadline), `evidence_details.submission_count`.

### Update a Dispute (Submit Evidence)
```js
stripe.disputes.update('{{DISPUTE_ID}}', { evidence: { ... } })
```
Two evidence field types:
- **Text-based**: string values (e.g. `customer_email_address`, `shipping_date`, `service_date`)
- **File-based**: `file_upload` object ID (e.g. `shipping_documentation`, `customer_communication`, `service_documentation`)

**Text limit**: 150,000 combined characters across all text fields.

**File upload workflow**: Upload with File Upload API (`purpose: "dispute_evidence"`) → get `File_upload` object ID → pass as evidence field value.

Catch-all fields: `uncategorized_text` (plaintext) and `uncategorized_file` (single file). Fill specific fields when possible for best win rate.

### List Disputes
```js
// Filter by PaymentIntent
stripe.disputes.list({ payment_intent: '{{PAYMENT_INTENT_ID}}' })

// Filter by Charge
stripe.disputes.list({ charge: '{{CHARGE_ID}}' })
```
Each dispute has a unique ID even if multiple disputes exist on the same payment.

## Multiple Disputes on One Payment

Rare but possible — e.g. customer disputes one item for damage and another for defect in the same order. List by PaymentIntent/Charge to find all, then retrieve/update each by its unique dispute ID.

## Related Pages

- [[disputes]] — concept page (updated with API section)
- [[source-stripe-disputes-responding]] — Dashboard dispute response guide
- [[source-stripe-disputes-best-practices]] — evidence formatting and file limits

## Raw Sources

- [[stripe-disputes-api-2026]] — verbatim Stripe disputes API guide
