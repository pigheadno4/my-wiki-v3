---
title: "Stripe — Set Up and Configure Smart Disputes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/disputes/set-up-smart-disputes
raw_files:
  - "stripe-disputes-set-up-smart-disputes-2026-11-07.md"
  - "stripe-disputes-smart-disputes-setup-2026.md"
tags: [stripe, disputes, smart-disputes, api, evidence, intended-submission-method, radar-sessions]
---

## Summary

The 2026-11-07 setup guide describes Smart Disputes enrollment, evidence packet submission choices, data-quality guidance at charge and dispute time, and `smart_disputes.status` packet availability. After enrollment, Stripe builds packets for eligible disputes when enough data is available; merchants can accept, submit manually, or let an available packet submit before the deadline. Submission is not a guarantee of a win. The guide links to preview-version Disputes API documentation; this captured link does not establish general availability.

## Key API Fields

### `intended_submission_method` (on dispute update)

| Value | Behavior |
| --- | --- |
| `prefer_manual` (default) | Submits your evidence if added; otherwise submits a Smart Disputes packet only if one is available |
| `prefer_smart_disputes` | Merges your evidence with generated Smart Disputes evidence when a packet is available; **recommended** by Stripe for stronger submissions |

Stripe recommends `prefer_smart_disputes` when updating a dispute to combine merchant and generated evidence. This preference does not itself make an unavailable packet eligible.

### `smart_disputes` on Dispute object

| Field | Description |
| --- | --- |
| `smart_disputes.status` | `available` / `requires_evidence` / `unavailable` |
| `smart_disputes.recommended_evidence` | Array of fields (or field groups) that would strengthen packet or make dispute eligible |

**Status meanings**:
- `available` — packet ready; auto-submitted if no action taken
- `requires_evidence` — recommended field groups can make a packet available if the dispute's scoped rules are satisfied
- `unavailable` — not eligible; additional evidence won't change this

If `prefer_smart_disputes` is set but status is not `available`, Stripe falls back to any manual evidence supplied while no Smart Disputes packet is available. `unavailable` cannot be changed by adding more fields.

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

At dispute time, additional evidence can strengthen an available packet or, if scoped rules are satisfied, make a `requires_evidence` packet available. The setup guide distinguishes:

1. **Recommended evidence** (`smart_disputes.recommended_evidence` array) — dynamically generated field alternatives or groups based on dispute reason and network rules. In the guide's example, either `customer_email` or both `shipping_carrier` and `shipping_tracking_number` prompt re-evaluation; the move to `available` remains conditional on scoped rules. A Dashboard tracking ID can help Stripe retrieve fulfillment data such as delivery history and proof of delivery.
2. **Additional evidence** — Dashboard context outside the recommended fields, such as screenshots, or custom fields through the Disputes API. The separate [[source-stripe-disputes-api]] capture documents `uncategorized_file` for submitting a single file; this setup capture describes an additional-evidence field but does not name that API key.

## Example API Flow

The earlier 2026-05-10 capture used the Node example below. The 2026-11-07 capture renders the same evidence keys, submission preference, and `submit=true` in curl; this presentation change adds no separate runtime requirement. `evidence_details.submission_method` can be inspected after submission to see how evidence was submitted.

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

- [[raw/stripe-disputes-set-up-smart-disputes-2026-11-07|Set up and configure Smart Disputes, 2026-11-07]] — current setup guide with corrected recommended evidence key and curl example
- [[raw/stripe-disputes-smart-disputes-setup-2026|Set up and configure Smart Disputes, 2026-05-10]] — earlier setup guide with Node example
