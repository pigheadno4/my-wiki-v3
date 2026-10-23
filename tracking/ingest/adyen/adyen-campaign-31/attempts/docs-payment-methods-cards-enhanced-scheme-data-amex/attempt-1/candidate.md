---
title: "Adyen American Express enhanced scheme data (historical guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/amex"
raw_files:
  - "adyen/docs/payment-methods/cards/enhanced-scheme-data/amex/2026-09-15.md"
tags: [adyen, cards, american-express, enhanced-scheme-data, online-payments, historical]
---

## Overview

This [[adyen]] child guide, last modified **2023-06-08** and captured 2026-09-15, lists American Express enhanced scheme data (ESD) for **US domestic transactions**. It presents the data as additional fraud protection or reporting information and explicitly says there is **no financial incentive** for sending it to American Express (raw lines 15–19). It is a field reference within [[adyen-online-payments]], not proof that a merchant/MCC is eligible, the ESD was accepted, or a payment was authorized, captured or settled. The related [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data|ESD overview]] separately states the Advanced-flow/webhook prerequisites and MCC exclusions; this child field list does not override those conditions.

## Key takeaways

- The child page says to send its data in a **/payments** or **/capture** request and links **Checkout latest /payments** versus **Payment API v68 /capture** (raw lines 21–23, 40–42, 55–57, 75–77). Those are distinct API routes; the parent ESD overview says Checkout **/payments/{paymentPspReference}/captures** does not support car-rental or lodging ESD in its snapshot. Do not infer support for those types from this page's generic `/capture` label.
- The **Level 2/3** tab marks customer reference, total tax amount and destination postal code for Level 2, and item product code, description, quantity, unit of measure, commodity code, total amount and unit price for Level 3 as required in its table (raw lines 21–36). These are table requirements for the named ESD type, not a statement that all transactions require every ESD category.
- Separate **lodging** (raw lines 38–51), **car rental** (raw lines 53–71), and **airline** (raw lines 73–94) tables mark fields required within those categories. The rental-class ID row and airline leg rows have blank Required cells (raw lines 71, 87–94). Refer to the raw tables for exact field names and linked parameter definitions; the page gives no runnable request or response example and no error or outcome semantics.
- The source's 2023-modified field lists and links are historical. Current scheme/merchant eligibility, API version compatibility and formatting need separate authority; this page's listing alone does not establish a fee benefit or a completed payment.

## Detail locators

- US-domestic scope and no-financial-incentive statement: raw lines 15–19.
- Level 2/3 endpoint links and required-field table: raw lines 21–36.
- Lodging endpoint links and required-field table: raw lines 38–51.
- Car-rental endpoint links, required fields and blank rental-class Required cell: raw lines 53–71.
- Airline endpoint links, required fields and blank leg Required cells: raw lines 73–94.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data]]
- [[adyen-payment-capture]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/amex/2026-09-15|Full pinned Amex ESD field guide]]
