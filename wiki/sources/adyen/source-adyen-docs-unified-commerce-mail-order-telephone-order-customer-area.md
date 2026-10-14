---
title: "Adyen Customer Area Virtual Terminal MOTO payments"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/mail-order-telephone-order/customer-area"
raw_files:
  - "adyen/docs/unified-commerce/mail-order-telephone-order/customer-area/2026-09-15.md"
tags: [adyen, unified-commerce, moto, virtual-terminal, customer-area, card-payments]
---

## Overview

Adyen's guide describes a merchant staff member accepting a Mail Order/Telephone Order (MOTO) card payment through the **Virtual Terminal user interface in Customer Area**—for example, entering card details relayed by a shopper to a call center. The merchant selects a merchant account and store, fills shopper/payment fields and submits the payment. This is a staff-operated Customer Area route, distinct from a merchant-built Checkout API or POS terminal MOTO integration. The 2026-09-15 documentation snapshot does not prove current account approval, a real authorization, settlement or funds availability. [[adyen]] [[adyen-unified-commerce]]

## Key takeaways

- The user needs the **Create payments from virtual terminal in the CA** Customer Area role, and the merchant subscribes to a **Standard webhook**. The guide does not describe an API credential for the operator's form or provide a CVC-specific field/retention rule; card details are entered in the Virtual Terminal UI. See `## Requirements` and the introduction.
- In Customer Area, staff select the merchant account, open **Virtual Terminal**, select the store, complete shopper and payment details, then submit. A confirmation page says whether the transaction was successful. The form always requires **Amount**, **Merchant reference** and **Country/Region**; additional fields can depend on industry/MCC, with airline data as an example. The page does not enumerate all card fields or turn that confirmation into settlement proof. See `## Make a payment` and `### Payment form`.
- The test path uses **test Customer Area** and test card details, then checks that the payment appears in the Customer Area payment list and that the merchant server receives an **AUTHORISATION** webhook. This is a prescribed test checklist, not a recorded test result. Before live use, the guide says to check form fields against business needs, submit **SAQ C-VT** for PCI DSS compliance, and train Customer Area users; live MOTO payments use **live Customer Area**. This guide does not by itself certify PCI compliance or guarantee authorization. See `## Test and go live`.

## Detail locators

- Introduction and `## Requirements`: Virtual Terminal staff/card-entry scope, required Customer Area role and Standard webhook.
- `## Make a payment` and `### Payment form`: merchant-account/store sequence, required form fields and MCC-specific additional fields.
- `## Test and go live`: test-account/test-card/payment-list/`AUTHORISATION` sequence, SAQ C-VT and training checks, live Customer Area route.

## Related

- [[adyen-unified-commerce]] — cross-channel provider hub.
- [[source-adyen-docs-unified-commerce-mail-order-telephone-order-api-request]] — separate merchant-built Checkout MOTO guide.
- [[source-adyen-docs-point-of-sale-mail-and-telephone-order-moto]] — separate MOTO route on POS terminals.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/mail-order-telephone-order/customer-area/2026-09-15|Adyen Customer Area Virtual Terminal MOTO guide, fetched 2026-09-15]]
