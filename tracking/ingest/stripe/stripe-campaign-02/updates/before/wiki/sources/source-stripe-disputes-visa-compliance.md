---
title: "Stripe — Visa Compliance Disputes"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-visa-compliance-2026.md"
tags: [stripe, disputes, visa, compliance, noncompliant, api]
---

## Summary

API guide for identifying, closing, and responding to Visa compliance disputes (pre-compliance disputes in Visa's terminology). Key distinction: responding requires explicit fee acknowledgment, closing avoids the 500 USD network fee.

## Identifying Visa Compliance Disputes

Any of these indicators on the `Dispute` object:

| Field | Value |
| --- | --- |
| `payment_method_details.card.case_type` | `"compliance"` |
| `enhanced_eligibility_types` | contains `"visa_compliance"` |
| `reason` | `"noncompliant"` |

## Close vs Respond

| Action | Fee | API |
| --- | --- | --- |
| Close dispute | No 500 USD fee | `stripe.disputes.close(id)` — irreversible |
| Respond with evidence | 500 USD fee (refunded if won) | `stripe.disputes.update(id, { evidence: { enhanced_evidence: { visa_compliance: { fee_acknowledged: true } } } })` |

## Responding: Required Fee Acknowledgment

Must set `evidence.enhanced_evidence.visa_compliance.fee_acknowledged: true` before submitting evidence — **Stripe returns an error if this is missing**.

- Fee withdrawn asynchronously 1–2 days after submitting
- Refunded if you win
- Status reflects `fee_acknowledged` in `evidence_details.enhanced_eligibility.visa_compliance.status`

## Testing

| Method | Value |
| --- | --- |
| Card number | `4000008400000779` |
| PaymentMethod | `pm_card_createComplianceDispute` |
| Token | `tok_createComplianceDispute` |

Same fee acknowledgment requirement applies in test mode. Simulate win/loss with `uncategorized_text: "winning_evidence"` or `"losing_evidence"`.

## Related Pages

- [[disputes]] — concept page (updated with Visa compliance details)
- [[source-stripe-disputes-responding]] — general dispute response (mentions 500 USD fee)
- [[source-stripe-disputes-visa-ce3]] — Visa CE 3.0 (different enhanced evidence path)

## Raw Sources

- [[stripe-disputes-visa-compliance-2026]] — verbatim Stripe Visa compliance disputes API guide
