---
title: "Stripe — Dispute Evidence Best Practices"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-best-practices-2026.md"
tags: [stripe, disputes, chargebacks, evidence, best-practices, visa-ce-30, radar, fraud]
---

## Summary

Best practices for formatting and submitting dispute evidence: organization, win likelihood scoring, file limits, authorization proof, CE 3.0, and background evidence auto-population by Stripe.

## Win Likelihood (Radar for Fraud Teams)

Radar AI scores dispute win probability (1–5 dots). Not available for non-credit-card payments or inquiries.

| Dots | Win chance |
| --- | --- |
| 5 | 60% |
| 4 | 40% |
| 3 | 25% |
| 2 | 15% |
| 1 | 5% |

Even at 5 dots, win rate is only 60% — disputes are hard to overturn.

## Evidence Organization Rules

- **Chronological**: order events by date
- **Grouped by type**: receipts / communications / policies / logs in separate sections
- **Summaries**: brief explanation of what each piece proves
- **Concise**: card issuers review thousands daily; relevance beats volume

**Relevant, not exhaustive**: match evidence to the dispute reason. Don't submit full ToS — extract only the relevant subsection with callout/arrow highlighting.

## File Format Limits

| Constraint | Limit |
| --- | --- |
| Combined file size | 4.5 MB |
| Total page count | <50 pages |
| Mastercard page count | 19 pages max |
| Accepted formats | PDF, JPEG, PNG only |
| Font size | 12pt minimum |
| Orientation | US Letter or A4, portrait |

- Combine multiple items of same type into one file (one file per evidence type)
- No external links (card issuers won't follow them)
- Crop screenshots to area of interest; circle key components

## Proof of Authorization (Fraudulent Disputes)

Fraudulent disputes = >50% of all disputes. Standard authorization evidence:
- AVS match
- CVC confirmation
- Signed receipt or contract
- IP address matching billing address

Stripe auto-includes AVS/CVC results + purchase IP. Add 3DS authentication if available.

## Background Evidence (Auto-populated by Stripe)

Stripe pre-populates these when integration supports it:

| API Parameter | Data |
| --- | --- |
| `billing_address` | AVS-verified billing address |
| `customer_name` | Customer name |
| `customer_email_address` | Customer email |
| `customer_purchase_ip` | Purchase IP (with geo expansion) |
| `receipt` | Stripe-generated email receipt |
| `product_description` | Product/service details |

Manual additions: `customer_signature`, `customer_communication`, `refund_refusal_explanation`.

## Accepting Disputes

- Not an admission of wrongdoing
- Dispute fee still applies
- Dispute counts toward dispute rate regardless of win/loss — **prevention > acceptance**
- Best when you don't plan to submit evidence and don't need the funds

## Partially Refunded Payments

Always respond even if partial refund was already issued:
- Include amount + date of refund + Dashboard screenshot
- Issuer typically cancels original dispute and creates a corrected-amount dispute
- If corrected dispute is lost, `status = lost`; you keep the partially refunded amount

> Cartes Bancaires: cannot contest disputes, so cannot ask issuer to consider partial refund.

## Visa Compelling Evidence (CE 3.0)

Required for Visa fraud disputes — without it, win rate is "very low."

Stripe support:
- Auto-flags CE 3.0 eligible disputes (Visa 10.4 code)
- Searches history for qualifying prior non-fraudulent transactions
- Notifies via email + Dashboard dispute details page
- Auto-adds qualifying transactions to evidence
- Shows "(Required for Visa CE 3.0)" badge in evidence form
- Pre-populates required fields — **do not edit pre-populated fields**

## Related Pages

- [[disputes]] — concept page (updated with best practices)
- [[source-stripe-disputes-responding]] — evidence submission workflow
- [[source-stripe-disputes-visual-evidence]] — visual packet examples
- [[stripe-3d-secure]] — 3DS as authorization evidence

## Raw Sources

- [[stripe-disputes-best-practices-2026]] — verbatim Stripe dispute evidence best practices (+ file length comparison image)
