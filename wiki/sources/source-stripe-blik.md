---
title: "Stripe: BLIK Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-blik-2025.md"
tags: [stripe, blik, poland, pln, bank-debit, disputes, connect]
---

## Summary

Reference page for BLIK on Stripe. Poland-only, PLN, customer-initiated (6-digit code from banking app). No redirect — customer stays on checkout page, enters code, then approves in-app. Covers disputes, refunds, and Connect.

## Key Details

- **Flow**: customer selects BLIK → opens banking app → generates 6-digit code (valid 2 min) → enters code in checkout → bank push notification → customer approves in-app (60 seconds, typically <10s) → immediate confirmation
- **Currency**: PLN only. **Country**: Poland customers only.
- **Recurring**: private preview. **Deferred intent**: client-side confirmation only (private preview).
- **ECE + Mobile Payment Element**: unsupported. **Deferred intent**: unsupported.
- **Business locations**: 37 countries.

**Disputes**: 
- BLIK has a claims process (fraud, double payment, order/amount mismatch)
- Stripe notifies via email, Dashboard, `charge.dispute.created` webhook
- Must submit evidence within 12 calendar days
- BLIK adjudicates — if merchant wins, amount returned; if customer wins, charge becomes permanent

**Refunds**: Full and partial; immediate or within hours depending on bank.

**Connect**: `blik_payments` capability required. Descriptor source follows charge type (Direct → connected account; Destination → platform; `on_behalf_of` → connected account).

## Raw Sources

- [[stripe-blik-2025]] — verbatim webpage content; 4 flow diagram SVGs in `raw/assets/stripe-blik-flow-*.svg`
