---
title: "Stripe — How Disputes Work"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-how-disputes-work-2026.md"
tags: [stripe, disputes, chargebacks, early-fraud-warnings, inquiries, dispute-fees, chargeback-lifecycle]
---

## Summary

Complete lifecycle of Stripe card payment disputes: pre-dispute phase (EFWs + inquiries), formal chargeback process, fees, timing, and LPM dispute differences.

## Pre-Dispute Phase

### Early Fraud Warnings (EFWs)

- Sourced from Visa TC40 and Mastercard SAFE reports (JCB also)
- **80% of EFWs convert to fraud disputes** if ignored (when no 3DS liability shift)
- With 3DS liability shift: may still receive dispute; Stripe auto-provides 3DS evidence
- Optimal refund threshold: charges ≤ dispute fee; not worthwhile if charge is >35% above dispute fee
- Refund reversal window: **2 hours** post-capture (only time a refund prevents the fraud report itself)
- API: listen for EFW webhooks via `radar/early_fraud_warnings`

### Inquiries

- Pre-dispute phase used by **AmEx and Discover** (Mastercard/Visa no longer use); also Mexico Domestic
- Resolve without dispute fee: submit evidence OR issue full refund
- Unanswered inquiry → escalates to formal (likely unwinnable) chargeback
- Inquiry statuses: `warning_needs_response` → `warning_under_review` → `warning_closed` (after 120 days)
- Partially refunded charges can still escalate from inquiry to chargeback

## Formal Dispute (Chargeback)

When a formal dispute is filed, Stripe:
1. Notifies via Dashboard, email, webhooks, and API
2. Debits disputed amount + dispute fee from Stripe balance
3. Blocks ability to issue refunds while dispute is open
4. Increases dispute rate with that card network

### Timing

| Stage | Timeframe |
| --- | --- |
| Customer dispute window | ~120 days from payment (longer for future-dated events like travel/tickets) |
| Merchant response window | 7–21 days (varies by network) |
| Issuer review period | 60–75 days (varies by network) |
| Full lifecycle | 2–3 months |

### Dispute Fees

- **Dispute received fee**: non-refundable for most countries; refundable in Mexico if won; no fee for SEPA/Cartes Bancaires card disputes
- **Dispute countered fee**: applies when you submit evidence to challenge; refunded if you win; not applicable in Mexico and Japan
- Fee details: [Stripe Pricing page](https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes#fee-details)

### Responding to Disputes

- Only way to overturn: submit evidence before deadline
- Even if customer "withdraws" dispute, must submit evidence for it to close in your favor
- Accept or counter via Dashboard or API

### Unchallengeable Disputes

Immediately closed as lost with no evidence submission possible:
- Discover inquiries not responded to
- Cartes Bancaires (SEPA merchants only — not SEPA cards issued by CB elsewhere)
- Nigerian payment methods (local regulation)

### Disputed Amount

Can differ from original charge due to:
- **Currency conversion**: exchange rate at dispute ≠ rate at purchase
- **Bundled recurring disputes**: bank aggregates multiple subscription charges into one dispute
- **Partial disputes**: customer disputes only a portion
- **Partially refunded charges**: customer disputes full amount after partial refund

### Dispute Outcome

- `won`: issuer returns funds to Stripe → Stripe returns to merchant
- `lost`: no money movement (Stripe already credited issuer at chargeback initiation)
- `late win`: rare — issuer credits after loss; Stripe labels as `late win`
- Final; neither party can overturn (customer can withdraw even after loss)
- Stripe does **not** support arbitration escalation

## LPM Disputes vs Card Disputes

| Dimension | Card | LPM (e.g. Klarna, PayPal) |
| --- | --- | --- |
| Decision-maker | Card issuer | LPM provider |
| Dispute window | ~120 days | ~180 days |
| Fee structure | Varies; dispute received + countered fees | Varies by LPM |
| Evidence | Submit to card network | Submit to LPM provider |

## Related Pages

- [[disputes]] — concept page (updated with Stripe section)
- [[stripe-declines]] — decline types and Radar blocking
- [[stripe-3d-secure]] — 3DS liability shift reduces EFW exposure
- [[source-stripe-declines-overview]] — declines overview

## Raw Sources

- [[stripe-disputes-how-disputes-work-2026]] — verbatim Stripe disputes lifecycle page (includes lifecycle diagram)
