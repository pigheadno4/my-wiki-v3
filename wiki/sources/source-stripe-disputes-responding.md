---
title: "Stripe — Respond to Disputes"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-responding-2026.md"
tags: [stripe, disputes, chargebacks, evidence, visa-ce-30, liability-shift, inquiries, dispute-response]
---

## Summary

Step-by-step guide to responding to Stripe disputes via Dashboard: reviewing dispute category, understanding the claim, accepting vs countering, submitting evidence, and checking outcomes.

## Notification Channels

On dispute creation, Stripe notifies via: email, Dashboard, `charge.dispute.created` webhook event, and push notification. All link to the Dispute details page.

## Response Deadline

**7–21 days** depending on card network. Missing the deadline = automatic loss, no recovery of funds.

## Automation Tools

| Tool | Purpose |
| --- | --- |
| Stripe Workflows | No-code automation for dispute tasks; compatible with Payments, Invoicing, Billing, Radar |
| Stripe Apps | Fraud/chargeback apps from the Stripe marketplace |

## Special Dispute Types

### Inquiries
- Appear in Dashboard as disputed payments but are pre-dispute
- Respond to prevent formal escalation (saves time, fees, card network rating)
- **Accepting an inquiry does NOT resolve it** — must submit evidence to counter
- If escalated to chargeback: must submit a separate response for the chargeback

### Visa Compliance Disputes
- Issued when card issuer believes transaction doesn't conform to Visa network rules
- Extra **500 USD** network fee (or local equivalent) on top of standard dispute fee
- 500 USD fee refunded if you win; standard dispute fee not refunded

### Fraudulent Disputes — Visa CE 3.0
- Applies to **Visa 10.4 (Card absent fraud)** disputes
- Stripe auto-evaluates eligibility from transaction history; notifies in Dashboard + email
- Pre-populates required evidence fields in response form — **don't edit pre-populated fields** (editing may affect CE 3.0 eligibility)
- CE 3.0 eligibility = significantly higher win likelihood

### Fraudulent Disputes — Liability Shift (3DS)
- Stripe auto-provides ECI and 3DS data in response form
- Additional merchant evidence still recommended on top of auto-provided data

## Responding Process

1. **Review dispute category** — determines evidence requirements; check `reason` on Dispute object
2. **Review bank's claim** — actual documents from card network; may include account owner's text description
3. **Contact account owner** — may clarify complaint; record all communication as evidence
4. **Accept or counter**:
   - **Accept dispute**: signals no contest; do not use for inquiries
   - **Counter dispute**: opens evidence submission form; triggers dispute countered fee

## Evidence Submission Rules

- **One shot only** — cannot amend or add files after submission
- **4.5 MB** combined max file size
- **19 pages** max for Mastercard evidence
- One file per evidence type (combine multiple into single multi-page file)
- Do NOT include: audio/video, requests to call/email, external links
- For CE 3.0: look for "(Required for CE 3.0)" badge; don't edit pre-populated fields
- For liability shift: ECI + 3DS data auto-populated

## Dispute Statuses

| Status | Meaning |
| --- | --- |
| `under_review` | Evidence submitted; awaiting issuer decision |
| `won` | Issuer ruled in merchant's favor; funds returned; countered fee refunded |
| `lost` | Issuer upheld dispute; dispute fee not returned (Mexico: may be returned) |

## Related Pages

- [[disputes]] — concept page (updated with responding details)
- [[source-stripe-disputes-how-disputes-work]] — full dispute lifecycle
- [[stripe-3d-secure]] — 3DS liability shift and ECI

## Raw Sources

- [[stripe-disputes-responding-2026]] — verbatim Stripe dispute response guide
