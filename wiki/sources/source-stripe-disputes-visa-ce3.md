---
title: "Stripe — Visa Compelling Evidence 3.0 Disputes"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-visa-ce3-2026.md"
tags: [stripe, disputes, visa, ce-3, compelling-evidence, friendly-fraud, api]
---

## Summary

API-level details for submitting Visa Compelling Evidence 3.0 (CE 3.0) to fight friendly fraud disputes. Covers qualifying criteria, the enhanced evidence object structure, status lifecycle, and test setup.

## Qualifying Criteria

All of the following must be true:

1. Visa transaction with **network reason code 10.4**
2. **2 prior undisputed transactions** using the same payment method, **120–364 days** before the disputed transaction; must be paid, not validation charges
3. **Product descriptions** provided for all 3 transactions (disputed + 2 prior)
4. `merchandise_or_services` set to `merchandise` or `services`
5. All 3 transactions share **2 main** OR **1 main + 1 secondary** evidence elements:

| Main elements | Secondary elements |
| --- | --- |
| Customer purchase IP | Shipping address |
| Customer device fingerprint OR customer device ID | Customer email address |
| | Customer Account ID |

> Device fingerprint + device ID together is NOT a valid combination.

## API Object Structure

Evidence goes in `evidence.enhanced_evidence.visa_compelling_evidence_3`:

```json
{
  "enhanced_evidence": {
    "visa_compelling_evidence_3": {
      "disputed_transaction": {
        "customer_email_address": "...",
        "customer_purchase_ip": "...",
        "merchandise_or_services": "merchandise",
        "product_description": "..."
      },
      "prior_undisputed_transactions": [
        { "charge": "ch_...", "customer_email_address": "...", "customer_purchase_ip": "...", "product_description": "..." },
        { "charge": "ch_...", "customer_email_address": "...", "customer_purchase_ip": "...", "product_description": "..." }
      ]
    }
  }
}
```

Eligibility tracked in `evidence_details.enhanced_eligibility.visa_compelling_evidence_3`.

## CE 3.0 Status Values

| Status | Meaning |
| --- | --- |
| `requires_action` | Check `required_actions[]` array for what's missing |
| `qualified` | Ready to submit CE 3.0 evidence |
| `not_qualified` | Evidence ineligible; standard submission used instead |

CE 3.0 status is separate from `dispute.status` (won/lost).

## Submission Notes

- Use `submit: false` to save evidence without submitting
- **Also fill standard `evidence` object** — fallback if CE 3.0 is rejected by Visa
- Stripe autofills when eligible; all prior transactions must have been Stripe-processed
- Check `enhanced_eligibility_types` array on dispute object for eligibility

## Testing

| Method | Value |
| --- | --- |
| Card number | `4000000404000038` |
| PaymentMethod | `pm_card_createCe3EligibleDispute` |
| Token | `tok_createCe3EligibleDispute` |

In test mode, any 2 test transactions work as `prior_undisputed_transactions` (no date/method validation). Simulate win/loss with `uncategorized_text: "winning_evidence"` or `"losing_evidence"`.

## Related Pages

- [[disputes]] — concept page (updated with CE 3.0 API details)
- [[source-stripe-disputes-api]] — general disputes API (retrieve/update/list)
- [[source-stripe-disputes-best-practices]] — CE 3.0 Dashboard workflow
- [[stripe-3d-secure]] — liability shift for fraudulent disputes

## Raw Sources

- [[stripe-disputes-visa-ce3-2026]] — verbatim Stripe Visa CE 3.0 API guide
