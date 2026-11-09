---
title: "Stripe — How Dispute Prevention Works"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/disputes/get-started/prevention
raw_files:
  - "stripe-disputes-get-started-prevention-2026-11-07.md"
  - "stripe-disputes-prevention-how-it-works-2026.md"
tags: [stripe, disputes, prevention, rdr, ethoca, consumer-clarity, order-insights, verifi, ce-30, friendly-fraud, visa, mastercard]
---

## Summary

Stripe's 2026-11-07 guide covers Visa/Verifi Rapid Dispute Resolution (RDR) and Order Insights (OI), and Mastercard/Ethoca Alerts and Consumer Clarity (CC). RDR and Ethoca Alerts resolve qualifying disputes under configured rules; OI and CC supply charge details for recognition lookups. Visa CE 3.0 with OI can block a filing when its prior-transaction criteria are met. Lookups can help cardholders recognize a charge, but deflection depends on available data and is not guaranteed. These products do not require a separate product integration, but resolution onboarding requires Radar rules; OI and CC onboarding and useful transaction data are also needed for their described lookups.

## Products Overview

| Product | Network | Provider | What it does |
| --- | --- | --- | --- |
| RDR (Rapid Dispute Resolution) | Visa | Verifi | Resolves qualifying disputes via configured rules; fee per resolved dispute |
| Ethoca Alerts | Mastercard | Ethoca | Resolves qualifying chargebacks via configured rules |
| Order Insights (OI) | Visa | Verifi | Shares available transaction details with issuer/cardholder during a lookup to help identify a charge |
| Consumer Clarity (CC) | Mastercard | Ethoca | Shares available purchase and merchant details for charge-recognition lookups |
| CE 3.0 with OI | Visa | Verifi | Requires issuer to block filing when the stated prior-transaction evidence criteria are met |

## RDR Details

- Visa RDR uses a ruleset to resolve incoming qualifying disputes, for example potential fraud disputes under 10 USD; Stripe's guide says there is a fee per resolved dispute.
- Resolved disputes do not count toward the stated dispute rate and have no separate dispute-received fee.
- RDR resolves only disputes for the full original transaction amount on non-refunded transactions. Verifi does not support partial resolution or disputes on refunded transactions in this guide.

## Ethoca Alerts Details

- Mastercard Ethoca Alerts uses resolution rules; the guide says resolved disputes do not count toward dispute rates and may help with Mastercard ECM, HECM, and EFM monitoring by reducing those rates.
- **Enrollment timing:** configured Ethoca Alerts rules apply only to chargebacks initiated after enrollment. Notices for chargebacks initiated before enrollment might still arrive later.

## Resolution Onboarding

RDR and Ethoca Alerts require no separate product integration effort, but onboarding requires resolution rules through Radar to access dispute resolution and define which transactions to refund. This is a configuration requirement, not a promise that every dispute will be resolved.

## OI and CC Charge-Recognition Lookups

OI applies to Visa transactions through Verifi; CC applies to Mastercard transactions through Ethoca. When a cardholder does not recognize a charge, a digital banking app or issuer agent can initiate a lookup. Stripe sends available transaction information to the issuer, potentially helping the cardholder recognize the purchase and avoid filing a dispute. Successful deflection depends on the quality and availability of transaction-time data. Stripe does not require a separate real-time lookup service.

Using OI and CC directs Stripe to share available charge data with issuers and ultimately cardholders. Verifi and Ethoca might update fields or operational requirements, which can require adaptation. The table below is the guide's **OI lookup-field inventory**, not a verified exhaustive CC API payload schema; it does not mean every listed OI field is mandatory.

### OI Lookup Data Fields

| Category | Key fields |
| --- | --- |
| Receipt | orderDate, orderNumber, invoiceNumber, subTotalAmount, orderTotalAmount |
| Payment | paymentMethod (masked card, last 4 PAN digits), billingName, cvvChecked |
| Product | productDescription, unitPriceAmount, quantity |
| Customer | firstName, lastName, emailAddress, accountId (recognizable customer account identifier), lengthOfRelationship |
| Billing address | address1, city, region, postalCode, country |
| Merchant | merchantName, merchantUrl, merchantContactPhone, termsAndConditions |
| Delivery | address + region + country (ISO 3166-1 alpha-3) |
| Shipping | shippingCarrier, trackingNumber |
| Device | ipAddress |

Stripe pulls the available data provided at transaction time. No separate real-time service is required for the lookup.

## CE 3.0 Pre-Dispute Blocking (Visa OI)

For Visa 10.4 card-absent fraud disputes, OI-enrolled businesses can use CE 3.0 prior-transaction data during a lookup. If prior transactions exist, Visa selects the 2–5 most recent non-fraud transactions and requests data; Stripe provides the available information. If **at least two prior transactions** have complete product descriptions and matching IP addresses plus **a matching email address or customer delivery address**, the issuer must block filing. Under those conditions, the dispute is never filed and does not incur dispute fees or raise the dispute rate. OI enrollment alone does not establish that the evidence criteria have been met. The guide also describes CE 3.0 post-dispute evidence as a way to improve the chance of winning, not as a guaranteed outcome.

## OI and CC Onboarding and Data Quality

Dashboard onboarding for OI and CC collects business name, business URL, business phone number, and email. For OI, Stripe advises supplying as many eligible lookup fields as possible at transaction time. To support CE 3.0 blocking, it advises including IP address, customer email address, and product descriptions on all transactions, plus shipping or customer address where possible. For CC, Stripe advises clear merchant and purchase information on Mastercard transactions, including recognizable merchant details, itemized receipts, and subscription details where applicable. These are the guide's data-quality recommendations; neither lookup is guaranteed to prevent a dispute.

## Related Pages

- [[disputes]] — concept page
- [[source-stripe-disputes-prevention]] — dispute prevention overview
- [[source-stripe-disputes-visa-ce3]] — CE 3.0 post-dispute API

## Raw Sources

- [[raw/stripe-disputes-get-started-prevention-2026-11-07|How dispute prevention works, 2026-11-07]] — current guide covering RDR, Ethoca Alerts, OI, CC, and conditional CE 3.0
- [[raw/stripe-disputes-prevention-how-it-works-2026|How dispute prevention works, 2026-05-10]] — earlier guide retained for history and OI lookup-field context
