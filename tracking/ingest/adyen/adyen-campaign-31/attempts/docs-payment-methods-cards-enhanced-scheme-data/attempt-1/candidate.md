---
title: "Adyen enhanced scheme data for online card payments"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data"
raw_files:
  - "adyen/docs/payment-methods/cards/enhanced-scheme-data/2026-09-15.md"
tags: [adyen, cards, enhanced-scheme-data, online-payments]
---

## Overview

This [[adyen]] overview defines enhanced scheme data (ESD) as additional information sent with **online card payment or capture requests** so shoppers can see purchase detail on statements and use it for reporting. It distinguishes optional Visa/Mastercard Level 2/3 or travel data that **can** lower interchange fees by up to 1%, without affecting authorization rates, from data required for compliance or eligibility, such as American Express fraud/reporting data, that does not lower interchange. These are conditional purposes, not a fee or payment-outcome guarantee. The page routes in-person integrations to a separate POS guide. [[adyen-online-payments]]

## Key takeaways

- The stated integration prerequisite is an **Advanced-flow online payments integration** that listens for AUTHORISATION and CAPTURE webhooks. ESD type depends on scheme and merchant category code (MCC), with some industries assigned airline, car-rental, lodging, or Level 2/3 data. The MCC table is a guide to type, subject to the explicit no-ESD MCC exclusions. Eligibility must not be inferred from a child-guide link or the “all other MCCs” row alone. See raw lines 19–29, 31–39, and 57–97.
- Adyen says it processes a payment **without submitted ESD** if the business is ineligible or the data is incomplete/invalid. Once a payment is processed, its submitted ESD cannot be changed or fixed. Different ESD types cannot be combined in one request, and refunds/reversals do not use ESD; the page recommends omitting it there. These ESD limitations do not themselves state a declined authorization or failed capture. See raw lines 40–54 and 85–97.
- The overview says Checkout API `/payments/{paymentPspReference}/captures` does **not** support car-rental or lodging ESD in this snapshot; an existing Classic API integration can use `/capture` instead. This is a route/version-specific boundary, not general absence of these ESD types. See raw lines 47–50.
- For Visa interchange-fee discounts, the page calls for AVS setup and AVS data in each Visa request. That is a stated qualification for the discount, not a claim that AVS alone grants eligibility or savings. See raw line 55.
- The explicit no-ESD MCC list is 4112, 5812, 4468, 5541, 5542, 5983, and 5499; Adyen says it processes a payment from those MCCs without ESD if supplied. The nearby “all other MCCs” Level 2/3 row must be read with this exception. See raw lines 63–97.

## Detail locators

- ESD purposes, fee ceiling and authorization-rate distinction: raw lines 22–29.
- Scheme/MCC type table and exclusions: raw lines 57–97.
- Child routes under “Send ESD” cover Level 2/3, airline, car rental, lodging, American Express, and FSA/HSA: raw lines 99–123. These links are navigation; this overview does not provide their request fields or establish merchant availability.
- Source metadata reports a 2023-05-26 modification and a 2026-09-15 capture (raw lines 2, 11). Treat the displayed rules as this captured snapshot, not current scheme or compliance authority.

## Related

- [[adyen-online-payments]]
- [[adyen-payment-capture]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/2026-09-15|Adyen enhanced scheme data overview snapshot]]
