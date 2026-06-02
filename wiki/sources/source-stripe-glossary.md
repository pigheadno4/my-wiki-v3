---
title: "Stripe Glossary"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-glossary-2025.md"
tags: [stripe, glossary, reference, terminology, payments]
---

## Summary

Comprehensive Stripe terminology reference — 130+ terms covering payment APIs, regulatory concepts, Connect platform, billing/subscriptions, fraud/risk, and infrastructure. Useful for interpreting Stripe documentation.

## Key Payment API Terms

| Term | Definition |
| --- | --- |
| PaymentIntent | API object tracking charge attempts and payment state through the lifecycle |
| SetupIntent | Collects payment details for future charges without capturing payment |
| PaymentMethod | Stateless representation of customer payment instrument (card, bank, wallet) |
| Charge | Created when PaymentIntent is confirmed; represents one money movement attempt |
| ConfirmationToken | Captures client-side data (payment instrument + shipping) to confirm a PI/SI |
| client secret | Unique key per PI/SI/AccountSession giving client access to non-sensitive fields |

## Key Regulatory / Network Terms

| Term | Definition |
| --- | --- |
| SCA | Strong Customer Authentication — EU 2FA requirement since Sep 14, 2019 |
| 3DS / 3DS2 | Card auth layer; 3DS2 = reduced friction + meets SCA; enables liability shift |
| liability shift | With 3DS, fraud chargeback liability moves from merchant to card issuer |
| ECI | Electronic Commerce Indicator — code indicating 3DS auth method/result |
| e-mandate | Authorization from cardholder to issuer for recurring card debits |
| MIT | Merchant-initiated transaction — off-session payment with saved card; SCA-exempt if properly flagged |
| chargeback | Issuer debits merchant account in response to customer dispute |
| dispute inquiry | Pre-dispute info request; may or may not escalate to chargeback |
| AVS | Address Verification System — verifies billing address with issuer |
| CVC | Card verification code (3-4 digits); `cvc_check` field on charge |
| hard decline | Issuing bank rejected; do not retry |
| soft decline | Issuing bank rejected with "authentication required"; can retry |

## Key Billing Terms

| Term | Definition |
| --- | --- |
| billing period | Frequency invoices are generated; independent of service period |
| service period | Timeframe for measuring usage; resets independently of billing period |
| metered billing | Charge based on consumption in billing cycle |
| usage-based billing | Pricing based on usage per billing period |
| MRR | Monthly Recurring Revenue |
| dunning email | Payment reminder asking customer to update payment method |
| proration | Mid-cycle plan changes; unused time credited |
| minor currency unit | Stripe expects smallest unit (e.g. 1099 = $10.99 USD; 10 = ¥10 JPY) |

## Key Connect Terms

| Term | Definition |
| --- | --- |
| Connect | Stripe's multi-party payment routing solution for platforms/marketplaces |
| direct charge | Customer → connected account (connected account is merchant of record) |
| destination charge | Customer → platform → connected account (platform is merchant of record) |
| separate charges and transfers | Customer → platform; platform transfers to connected account(s) separately |
| on_behalf_of | Parameter making connected account the merchant of record on indirect charge |
| merchant of record | Legal entity responsible for the sale, taxes, and liabilities |
| application fee | Fee Connect platform collects from connected account per payment |

## Other Notable Terms

- **IC+**: Interchange-plus pricing — variable network cost + Stripe fee (more transparent than flat rate)
- **interchange fee**: Fee acquiring bank pays issuing bank per card transaction
- **payout**: Transfer of Stripe balance to external bank account (T+2/3/4/5 schedules)
- **settlement currency**: Currency of merchant's bank account (vs presentment currency = customer's)
- **Radar**: ML fraud detection built into Stripe; `Radar for Fraud Teams` adds manual review tools
- **Link**: Stripe's digital wallet (saves cards, bank accounts, BNPL)
- **sandbox**: Isolated test environment; preferred over test mode for new integrations
- **requires_action**: Pre-2019-02-11 name was `requires_source_action`
- **requires_payment_method**: Pre-2019-02-11 name was `requires_source`

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-payment-intents]] — PaymentIntent + SetupIntent lifecycle
- [[source-stripe-payment-methods]] — PaymentMethod API

## Raw Sources

- [[stripe-glossary-2025]] — Full Stripe glossary: 130+ terms across payment APIs, regulatory, Connect, billing, fraud, infrastructure
