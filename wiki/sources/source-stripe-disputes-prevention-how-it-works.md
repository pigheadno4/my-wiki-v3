---
title: "Stripe — How Dispute Prevention Works"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-prevention-how-it-works-2026.md"
tags: [stripe, disputes, prevention, rdr, ethoca, order-insights, verifi, ce-30, friendly-fraud, visa, mastercard]
---

## Summary

Deep-dive on Stripe's dispute prevention products: RDR (Visa/Verifi), Ethoca Alerts (Mastercard), Order Insights (Visa/Verifi lookup), and CE 3.0 pre-dispute blocking. No integration required.

## Products Overview

| Product | Network | Provider | What it does |
| --- | --- | --- | --- |
| RDR (Rapid Dispute Resolution) | Visa | Verifi | Auto-resolves disputes via rules; fee per dispute |
| Ethoca Alerts | Mastercard | Ethoca | Auto-resolves chargebacks via rules |
| Order Insights (OI) | Visa | Verifi | Sends transaction data to issuer when cardholder calls; deflects before dispute |
| CE 3.0 with OI | Visa | Verifi | Forces issuer to block dispute if CE 3.0 criteria met |

## RDR Details

- Ruleset-based: e.g. "resolve all potential fraud disputes under $10"
- Resolved disputes: don't count toward rate; no dispute received fee charged
- **Limitation**: only resolves full-amount disputes on non-refunded transactions (no partial resolution)
- Rules apply only to chargebacks initiated after enrollment

## Ethoca Alerts Details

- Same rate/fee benefits as RDR but for Mastercard
- Helps exit ECM, HECM, EFM monitoring programs

## Order Insights (OI) Data Fields

When cardholder initiates lookup at issuer, Stripe sends available data:

| Category | Key fields |
| --- | --- |
| Receipt | orderDate, orderNumber, invoiceNumber, subtotalAmount, orderTotalAmount |
| Payment | paymentMethod (last 4), billingName, cvvChecked |
| Product | productDescription, unitPriceAmount, quantity |
| Customer | firstName, lastName, emailAddress, accountId, lengthOfRelationship |
| Billing address | address1, city, region, postalCode, country |
| Merchant | merchantName, merchantUrl, merchantContactPhone, termsAndConditions |
| Delivery | address + region + country (ISO 3166-1 alpha-3) |
| Shipping | shippingCarrier, trackingNumber |
| Device | ipAddress |

Stripe pulls data from what you provided at transaction time — no real-time integration required.

## CE 3.0 Pre-Dispute Blocking (OI + CE 3.0)

For Visa 10.4 disputes: if prior transactions exist, Visa auto-selects 2–5 most recent non-fraud transactions and requests data. If **≥2 prior transactions** have:
- Complete product descriptions
- Matching IP address
- Matching email OR customer delivery address

→ **Issuer must block the dispute** — it's never filed; no fees; no dispute rate impact.

**Key requirement**: transactions must include IP address, customer email, product descriptions, and ideally shipping/customer address. Set up at onboarding via Dashboard.

## Related Pages

- [[disputes]] — concept page (updated with OI/CE 3.0 pre-dispute details)
- [[source-stripe-disputes-prevention]] — dispute prevention overview
- [[source-stripe-disputes-visa-ce3]] — CE 3.0 post-dispute API

## Raw Sources

- [[stripe-disputes-prevention-how-it-works-2026]] — verbatim prevention how-it-works guide
