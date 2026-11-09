---
title: "Stripe — Visa Compliance Disputes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/api/visa-compliance"
raw_files:
  - "stripe-disputes-api-visa-compliance-2026-11-07.md"
  - "stripe-disputes-visa-compliance-2026.md"
tags: [stripe, disputes, visa, compliance, noncompliant, api]
---

## Summary

Stripe's API guide for identifying, closing, and responding to Visa compliance disputes, called pre-compliance disputes by Visa. These are Visa network-rule cases, distinct from the ordinary chargeback response path. The 2026-05-10 and 2026-11-07 captures at the same canonical URL describe the same fee, response, and test flow; the later diff changes presentation and illustrative JSON formatting, not a documented outcome or API rule.

## Identifying Visa Compliance Disputes

Any one of these indicators on the `Dispute` object can identify a Visa compliance dispute:

| Field | Value |
| --- | --- |
| `payment_method_details.card.case_type` | `compliance` |
| `enhanced_eligibility_types` | contains `visa_compliance` |
| `reason` | `noncompliant` |

See the 2026-11-07 raw guide lines 19–40 and 2026-05-10 raw guide lines 18–39. The dispute JSON is illustrative.

## Close or Respond

| Action | API route | Visa compliance network fee and effect |
| --- | --- | --- |
| Close | [Close dispute](https://docs.stripe.com/api/disputes/close) | Acknowledges the dispute as lost; avoids this Visa 500 USD network fee. Closing is irreversible. |
| Respond with evidence | [Update dispute](https://docs.stripe.com/api/disputes/update) | Contesting requires acknowledging the 500 USD or local-equivalent network fee, in addition to applicable Stripe dispute fees. Stripe refunds this network fee if you win. |

Closing's avoidance of the Visa network fee does not establish treatment of any separate Stripe dispute fee. These are guide statements, not proof of a particular account's eligibility, fees, or dispute outcome. See the 2026-11-07 raw guide lines 9–11 and 42–56; the 2026-05-10 guide lines 8–10 and 41–55.

## Responding: Required Fee Acknowledgment

Set `evidence.enhanced_evidence.visa_compliance.fee_acknowledged` to `true` when submitting evidence. Without acknowledgment, Stripe says it returns an error and does not submit the evidence. The guide says Stripe withdraws the network fee from the balance asynchronously after evidence submission, typically within 1–2 days, and refunds it if the dispute is won. The `evidence_details.enhanced_eligibility.visa_compliance.status` value `fee_acknowledged` records acknowledgment; it does not establish a win. The JSON examples include ellipses and are illustrative, not executable payloads. See the 2026-11-07 raw guide lines 52–100 and the 2026-05-10 guide lines 51–96.

## Testing

For the guide's test-mode Visa compliance dispute, use card number `4000008400000779`, PaymentMethod `pm_card_createComplianceDispute`, or token `tok_createComplianceDispute`. In test mode, evidence without fee acknowledgment is rejected. The `uncategorized_text` strings `winning_evidence` and `losing_evidence` simulate overall dispute outcomes; they do not predict or prove a live case result. See the 2026-11-07 raw guide lines 102–114 and the 2026-05-10 guide lines 98–110.

## Related Pages

- [[disputes]] — concept page with the Visa compliance API route
- [[source-stripe-disputes-responding]] — broader dispute response guidance
- [[source-stripe-disputes-visa-ce3]] — distinct Visa CE 3.0 enhanced evidence path

## Raw Sources

- [[raw/stripe-disputes-api-visa-compliance-2026-11-07|Visa compliance API guide, fetched 2026-11-07]]
- [[raw/stripe-disputes-visa-compliance-2026|Visa compliance API guide, fetched 2026-05-10]]
