---
title: "Stripe — Set Up and Configure Smart Disputes"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-smart-disputes-setup-2026.md"
tags: [stripe, disputes, smart-disputes, api, evidence, intended-submission-method, radar-sessions]
---

## Summary

Configuration guide for Smart Disputes: API integration via `intended_submission_method`, data quality recommendations at charge time and dispute time, and `smart_disputes.status` packet lifecycle.

## Key API Fields

### `intended_submission_method` (on dispute update)

| Value | Behavior |
| --- | --- |
| `prefer_manual` (default) | Submits your evidence if added; falls back to Smart Disputes packet if no evidence provided |
| `prefer_smart_disputes` | Merges your evidence with Smart Disputes evidence → strongest packet; **recommended** |

Set to `prefer_smart_disputes` when updating disputes for best results.

### `smart_disputes` on Dispute object

| Field | Description |
| --- | --- |
| `smart_disputes.status` | `available` / `requires_evidence` / `unavailable` |
| `smart_disputes.recommended_evidence` | Array of fields (or field groups) that would strengthen packet or make dispute eligible |

**Status meanings**:
- `available` — packet ready; auto-submitted if no action taken
- `requires_evidence` — provide `recommended_evidence` fields to unlock
- `unavailable` — not eligible; additional evidence won't change this

If `prefer_smart_disputes` is set but status is not `available` → Stripe falls back to manual evidence until packet becomes available.

### `evidence_details.submission_method`

Post-submission field on Dispute object showing how evidence was submitted.

## Data to Provide at Charge Time

Include via stripe.js / Radar Sessions (for fraud signals) plus these API fields:

| Data | Key fields |
| --- | --- |
| Customer identity | email, phone, name, billing address |
| Product | line_items (on PaymentIntent/Checkout), product images/URL/description |
| Shipping | shipping address, tracking_number, carrier, recipient phone |
| Receipt | receipt_email |

For Stripe-hosted products (Checkout, Payment Links, Billing): enable cardholder name, phone, billing address, email, ToS acceptance in Dashboard settings. Add business URL to business profile.

## Data to Provide at Dispute Time

Two types of additional evidence via Dashboard or API:

1. **Recommended evidence** (`smart_disputes.recommended_evidence` array) — dynamically generated; can unlock `requires_evidence` → `available`
   - Example: adding `tracking_number` + `shipping_carrier` enables auto-pull of delivery history and proof of delivery from fulfillment providers
2. **Additional evidence** (`uncategorized_file` / custom fields) — any supporting context not in recommended fields

## Example API Flow

```js
// Set prefer_smart_disputes + provide recommended evidence
stripe.disputes.update('dp_123', {
  evidence: {
    shipping_tracking_number: '123',
    shipping_carrier: 'ups',
  },
  intended_submission_method: 'prefer_smart_disputes',
  submit: true,
})
```

## Related Pages

- [[disputes]] — concept page (updated with API fields)
- [[source-stripe-smart-disputes]] — Smart Disputes overview
- [[source-stripe-disputes-api]] — general disputes API

## Raw Sources

- [[stripe-disputes-smart-disputes-setup-2026]] — verbatim Smart Disputes setup guide
