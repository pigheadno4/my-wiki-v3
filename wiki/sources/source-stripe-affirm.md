---
title: "Stripe: Affirm Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-affirm-2025.md"
tags: [stripe, bnpl, affirm, buy-now-pay-later, installments, connect, disputes]
---

## Summary

Deep-dive on Affirm as a Stripe payment method. Covers payment options, Standard vs Enhanced financing packages (with tier tables), prohibited categories, refund mechanics, dispute process, Connect requirements, and buyer country filtering.

## Key Details

**Domestic only**: customer country must match merchant country (US or CA).

**Payment options**:
- Pay in 30 (USD only, $35–$49.99, 0% interest-free)
- Pay in 4 (0% APR, biweekly over 6 weeks)
- Monthly installments up to 36 months (10–36% APR)

**Financing packages** — Standard vs Enhanced (Enhanced = more 0% APR tiers):

| Order range | Standard notable | Enhanced notable |
| --- | --- | --- |
| $50–$99.99 | Pay in 4 - 0% APR | Pay in 4 - 0% APR |
| $100–$499.99 | Pay in 4 + interest-bearing only | Pay in 4 + 6 months 0% APR |
| $700–$1,699.99 | 6 months 0% APR + interest bearing | 6 + 12 months 0% APR |
| $1,700–$30,000 | 6 months 0% APR + interest bearing | 6 + 12 months 0% APR |

Platforms don't qualify for 0% APR plans. Configurable in Dashboard (not for connected accounts).

**Refunds**: up to 120 days; async (`refund.updated`/`refund.failed` webhook); no fee credits. Affirm pauses customer plan and credits payments made (minus interest).

**Disputes**: no time limit for customer; 30-day max resolution; merchant has 15 days to submit evidence; Affirm covers fraud losses; `charge.dispute.created` event.

**Prohibited**: B2B services, home improvement, titled goods (cars/boats), professional services, NFTs, pre-orders. Healthcare allowed with additional requirements.

**Connect**: direct, destination, separate charges + transfers all supported. Requires `affirm_payments` capability + correct MCC set.

**Buyer country**: shipping address → geocoded IP fallback.

## Raw Sources

- [[stripe-affirm-2025]] — verbatim webpage content (242 lines); fixed 3× `_italic_` → `*italic*`; MP4 video CDN URL on line 82 left as-is
