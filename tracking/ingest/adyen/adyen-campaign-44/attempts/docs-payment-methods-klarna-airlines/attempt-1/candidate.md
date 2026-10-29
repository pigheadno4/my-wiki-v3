---
title: "Klarna for airlines | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/airlines"
raw_files:
  - "adyen/docs/payment-methods/klarna/airlines/2026-09-15.md"
tags: [adyen, klarna, airlines, travel, online-payments]
---

## Overview

This 2026-09-15 Adyen Docs guide adds **airline-specific data** to Klarna `/sessions` or `/payments` requests. It is a supplement to a Klarna payment integration: it defines travel information under `additionalData`, required `lineItems` fields, and an airline capture note. It does not provide a complete checkout or final-outcome flow, or prove any airline's current eligibility. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-klarna]] and [[adyen]].

## Key takeaways

- For both endpoint tabs, `additionalData.additionalDataAirline` is marked required. The listed fields include an alphanumeric customer reference, leg departure/destination three-letter IATA airport codes, two-letter carrier accounting code, travel date/time formatted `yyyy-MM-dd HH:mm`, and passenger first/last name and traveller type (`mr`, `mrs`, `ms`). Each leg/passenger key needs a numeric `[itemNr]` suffix even when only one item exists. The single- and multi-leg JSON blocks are examples, not the whole payment request or proof of valid airport codes.
- Optional `additionalData.openinvoicedata.merchantData` can carry Base64-encoded JSON of relevant product, purchase and customer details following Klarna's specification. **If the format is wrong, Klarna's risk engine will not consume the data and Klarna will not return validation errors for it.** The field being accepted in an API response therefore cannot establish that risk data was consumed. The general Klarna Web Drop-in guide additionally says not to include this field in TEST because test values cause an error; read the exact integration/environment before sending it.
- Both `/sessions` and `/payments` airline `lineItems` tables mark `quantity`, `description` (maximum 10,000 characters) and `amountIncludingTax` (minor units) mandatory. They are method-specific request obligations, not a statement that other line-item fields or airline data are universally optional.
- This airline page says immediate/automatic capture is supported because flight bookings are locked when payment is made, and says the default manual capture flow is also supported. The general Klarna Web Drop-in guide conditions automatic capture on immediate delay plus shipping within 24 hours and otherwise requires manual capture within 90 days. These pages give different contexts; the captured evidence does not settle whether an airline booking bypasses that general shipping condition. Verify the applicable merchant configuration and scheme rule before treating automatic capture as enabled. No capture or settlement outcome is shown here.

## Detail locators

- Airline-specific scope and both request routes: raw lines 15–19.
- `/sessions` required airline fields, numbering rule, single/multi-leg fixtures and optional `merchantData` silent non-consumption: `## Additional data`, lines 21–91.
- `/payments` parallel airline fields, numbering rule, fixtures and optional `merchantData` warning: lines 93–159. Field labels vary in whether `airline.` is printed before `leg`; use the selected endpoint's API reference for exact keys rather than treating labels as a complete payload.
- Mandatory airline `lineItems.quantity`, `description` and `amountIncludingTax` in both endpoint tabs: `## Line items`, lines 161–183.
- Airline immediate/manual capture statement: `## Capture payments`, lines 185–187; compare the general Web Drop-in capture conditions in [[source-adyen-docs-payment-methods-klarna-web-drop-in]].

## Related

- [[adyen-online-payments]] — provider online-payment context.
- [[source-adyen-docs-payment-methods-klarna]] — product, country and currency overview.
- [[source-adyen-docs-payment-methods-klarna-web-drop-in]] — Web Drop-in field and capture conditions that need context-specific reconciliation.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/airlines/2026-09-15|2026-09-15 Klarna airline-specific request fields and capture note]]
