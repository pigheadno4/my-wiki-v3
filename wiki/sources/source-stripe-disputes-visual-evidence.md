---
title: "Stripe — Dispute Sample Evidence Packets"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-visual-evidence-2026.md"
tags: [stripe, disputes, chargebacks, evidence, visual-examples, dispute-response]
---

## Summary

Visual evidence packet examples for 7 dispute categories, showing what a well-constructed evidence submission looks like for both approved and denied scenarios. 62 illustrative images saved to `raw/assets/stripe-disputes-evidence-*.png`.

## Categories Covered

| Category | Sub-types / scenarios |
| --- | --- |
| Credit not processed | Approved (refund proof) + Denied (refund denial) |
| Duplicate | Approved (refunded duplicate) + Denied (intentional separate purchases) |
| Fraudulent | Single flow: investigation summary → location/IP → fraud score + verification → AVS/CVV/3DS → conclusion |
| General | Order confirmation/receipts; POS data/system logs; Customer communications |
| Product not received | Physical (tracking + signature); Digital (account activity + usage logs); Service (session logs + completion) |
| Product unacceptable | Quality/functionality; Marketing materials; Support/resolution |
| Subscription canceled | Terms/policies; Cancellation records; Usage/communications |

## Key Evidence Packet Patterns

**Fraudulent dispute packet order**:
1. Investigation summary
2. IP/location data consistent with billing address and past orders
3. Fraud risk score (low) + customer verification details
4. AVS/CVV match + 3DS completion proof
5. Conclusion

**Subscription canceled packet order**:
1. Terms agreed to at signup (renewal, cancellation, refund policy)
2. No cancellation request on record; cancellation methods available
3. Renewal reminder emails sent; subscription billed regularly; usage logs

**Product not received — key differentiator**:
- Physical: tracking history with delivery date highlighted (especially if dispute filed after delivery)
- Digital: account activity log showing download/activation/login sessions
- Service: session log with schedule date, reminders, and completion confirmation

## Related Pages

- [[disputes]] — concept page
- [[source-stripe-disputes-categories]] — evidence API fields by category
- [[source-stripe-disputes-reason-codes]] — per-code evidence guidance
- [[source-stripe-disputes-responding]] — evidence submission workflow

## Raw Sources

- [[stripe-disputes-visual-evidence-2026]] — verbatim page with 62 illustrative images (saved to `raw/assets/stripe-disputes-evidence-*.png`)
