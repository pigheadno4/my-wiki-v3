---
title: "Stripe — Review Payments (Radar)"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-reviews-2026.md"
tags: [stripe, radar, reviews, fraud, smart-refunds, review-queue, fraud-teams]
---

## Summary

Radar for Fraud Teams manual review queue: examine elevated-risk payments, Smart Refunds recommendations, and assignment workflow. Webhooks: `review.opened` / `review.closed`.

## Payment Method Support for Review

Most Radar-supported PMs. **Cannot review**: ACH Direct Debit, SEPA Direct Debit.

## Review Queue

Two views:
- **List view**: risk level, customer name, payment method, amount/date/time
- **Detailed view**: risk insights (why Radar scored as it did), related payments (same email/IP/card); `J`/`K` keyboard navigation

Payments in review are typically already processed (unless capture-later flow).

## Smart Refunds (Fraud Teams)

Post-completion fraud protection — recommends refunds based on EFW/dispute likelihood:

| Confidence | Chance of EFW or dispute |
| --- | --- |
| Very high | 72% |
| High | 60% |
| Medium | 40% |
| Low | 30% |
| Very low | 15% |

## Actions

| Action | Effect |
| --- | --- |
| Approve | Close review; no payment change |
| Refund | Refund without fraud report (permanent) |
| Refund and report fraud | Refund + adds email + card fingerprint to block lists |

Disputed payment → review auto-closed.

## Review Assignments

Self-assign to avoid duplicate work. Filter by owned/unassigned. Can't assign to other team members.

## Webhooks

- `review.opened` — payment added to review queue
- `review.closed` — review closed (includes `reason`)

## Best Practices

- Add metadata for context (Google Maps links to shipping address, order info)
- Don't add review bottleneck if no natural fulfillment delay
- Use risk insights + related payments for informed decisions
- Collect reviewer insights → translate into custom Radar rules

## Related Pages

- [[stripe-radar]] — concept page (updated with review queue)
- [[source-stripe-radar-risk-evaluation]] — risk levels that trigger review
- [[source-stripe-radar-risk-settings]] — risk controls that auto-place elevated payments in review

## Raw Sources

- [[stripe-radar-reviews-2026]] — verbatim review payments guide (3 screenshots)
