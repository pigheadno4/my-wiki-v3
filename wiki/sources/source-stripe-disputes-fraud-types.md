---
title: "Stripe — Common Types of Online Fraud"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-fraud-types-2026.md"
tags: [stripe, fraud, disputes, stolen-cards, card-testing, friendly-fraud, marketplace-fraud, overpayment]
---

## Summary

7 fraud type categories with definitions, examples, liability implications, and prevention notes.

## 7 Fraud Types

| Type | What it is | Key rule |
| --- | --- | --- |
| **Suspected fraud** | Stripe AI flags post-authorization suspicious activity; also EFWs from card issuer | Consider proactive refund; partially refunded payments can still be disputed for full original amount |
| **Stolen cards** | Stolen card/details used online; business may not detect until cardholder disputes | Business bears loss + dispute fee |
| **Overpayment fraud** | Stolen card + fake third-party service; business pays out to fraudster then faces dispute | Never pay out to third parties at buyer's request |
| **Card testing** | Validating stolen cards on low-friction sites before using elsewhere | CAPTCHA + rate limiting; see card testing guide |
| **Alternative refunds** | Overpay → claim wrong amount → request refund via different channel | **Never refund via different method than original** — closed cards can still be refunded |
| **Marketplace fraud** | Fraudulent seller takes payment, doesn't deliver; platform bears liability if unrecoverable | Connect platform responsibility for negative balances |
| **Friendly fraud** | Legitimate cardholder disputes own purchase (accidental or deliberate) | Visa CE 3.0 challenges this by showing prior non-fraud transactions with same cardholder |

## Key Rules

- Partially refunded payments can be disputed for the **full original amount**
- Always refund via the original payment method — closed cards can still receive refunds
- Visa CE 3.0: Stripe auto-identifies qualifying prior transactions to pre-populate dispute response for friendly fraud

## Related Pages

- [[disputes]] — concept page (updated with fraud types)
- [[source-stripe-disputes-best-practices]] — prevention best practices
- [[source-stripe-disputes-visa-ce3]] — CE 3.0 API for friendly fraud

## Raw Sources

- [[stripe-disputes-fraud-types-2026]] — verbatim fraud types guide
