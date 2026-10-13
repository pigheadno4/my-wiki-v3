---
title: "Cartes Bancaires (CB)"
type: concept
category: standard
tags: [cartes-bancaires, france, local-card-network, co-badged, disputes, eur]
---

## Definition

Cartes Bancaires (CB) is France's domestic card network. More than 95% of CB cards are co-badged with Visa or Mastercard, allowing merchants to process them over either network.

**Currency**: EUR only. **Customer location**: Europe (primarily France).

## Co-badging

Under EEA regulations, businesses must offer customers a choice of which network processes their co-badged card at checkout. See [[source-stripe-cartes-bancaires]] for the co-badged cards compliance guide.

Stripe auto-retries on Visa/MC if a CB charge is declined for technical reasons, improving acceptance rates.

## Business Availability

41 countries (including most of Europe + US/CA/AU/HK/JP/MX/SG/NZ). Non-France businesses must process one CB payment first to fully enable the method.

## Payment Properties

- Recurring, manual capture, multicapture, partial refunds: all supported
- Connect, Checkout, Payment Links, Subscriptions, Invoicing, Terminal: supported
- Elements: supported (Express Checkout Element excluded)
- Terminal: France requires specific regional configuration

## Disputes

- Fewer dispute reasons than Visa/MC → lower dispute rate on average
- **Stripe processing:** Stripe says businesses cannot contest Cartes Bancaires disputes. For Adyen's distinct, limited automatic-defense grounds and its non-defendable reason code 45, see [[source-adyen-docs-risk-management-chargeback-guidelines-cartes-bancaires-chargebacks]] and [[adyen-risk-management]].
- **Dispute fee: 0 EUR**
- CB may withdraw a dispute → status becomes `won`

## Sources

- [[source-adyen-docs-risk-management-chargeback-guidelines-cartes-bancaires-chargebacks]] — Adyen-specific automatic-defense grounds and non-defendable reason code 45 (2026-09-15 webpage snapshot).

- [[source-stripe-cartes-bancaires]] — primary source: properties, business countries, dispute rules, integration notes
