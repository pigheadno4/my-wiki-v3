---
title: "Adyen Affirm Web Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/affirm/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/affirm/web-drop-in/2026-09-15.md"
tags: [adyen, affirm, bnpl, web, drop-in, sessions, advanced]
---

## Overview

This 2026-09-15 capture explains how to add Affirm to an existing Adyen Web Drop-in integration in either Sessions or Advanced flow, after adding the method in Customer Area. It is a method-specific integration guide, not evidence of current account enablement, shopper approval or successful live capture. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-affirm|Affirm overview]].

## Key takeaways

- The page requires an existing Sessions or Advanced Web Drop-in integration and adding Affirm in Customer Area. Web Drop-in v6 users import `AdyenCheckout` and `Affirm`. Its `/sessions` tab says Sessions is the default with Drop-in v5.0.0 or later; its `/payments` tab addresses an additional use case. Those Drop-in versions are not stated Checkout API minimums.
- Both endpoint tables mark shopper first/last name, telephone number and email required. `shopperReference` is optional with a three-character minimum if provided. Although the `countryCode` requiredness cell is blank, the prose requires it for Canada or the UK because omission defaults to US. The outer billing/delivery-address and `lineItems` rows are not marked required; the guide requires `stateOrProvince` for Canadian and US addresses, allows its omission for UK addresses, defaults a missing delivery address to the billing address, and recommends optional line items to improve approval rates. See the endpoint-specific tables before constructing a request.
- The curl examples use Checkout test `/v69/sessions` and `/v72/payments` respectively. Both curl bodies contain literal `{hint:state.data...}` markup inside the JSON address-key strings even though the tables name `billingAddress` and `deliveryAddress`; do not copy those marked-up keys as API field names. The example versions and sample values are not general API minimums or proof of a valid production request.
- `allowedCountries` controls the Affirm address-form dropdown, defaults to US and CA, and can include GB; it does not itself set a transaction's `countryCode`. Optional `data` pre-fills shopper fields. A `readOnly` visibility group needs corresponding pre-filled data; the default groups and values are listed in the raw.
- After sending goods, the guide instructs capture within 28 days; capture starts the shopper's installment schedule and the authorization expires if not captured in time. For a lesser fulfilled amount, this guide instructs capturing the authorized amount and then refunding the difference. The separate [[source-adyen-docs-payment-methods-affirm|Affirm overview]] marks partial and multiple-partial capture supported in its feature matrix, so these captures disagree on the partial-capture path; this guide does not establish when partial capture can replace its full-capture/refund instruction.
- Affirm supplies test credentials and, after review of test transactions, live-processing credentials. Live acceptance also requires a request for Affirm in the live Customer Area and supplying those live credentials. The test payment list is a status-check route, not evidence of a successful transaction.

## Detail locators

- Prerequisite flows and Customer Area addition: pinned raw lines 21–37. Web v6 import: lines 39–45. `/sessions` default statement and fields: lines 47–64; sample test endpoint and marked-up address keys: lines 66–115.
- `/payments` additional-use-case statement, fields, test endpoint and marked-up address keys: pinned raw lines 766–821. The endpoint-specific example bodies continue in the raw; confirm request shape against the prose and Checkout API reference rather than treating copied hint markup as JSON field names.
- `allowedCountries` address dropdown and GB example: pinned raw lines 1259–1279. Shopper pre-fill and visibility/defaults: lines 1281–1367. Capture timing, installment trigger, expiry and lesser-amount refund instruction: lines 1369–1373. Test/live credential and Customer Area gates: lines 1375–1381.
- Cross-page capture conflict: this guide's pinned raw line 1373 versus [[raw/adyen/docs/payment-methods/affirm/2026-09-15|Affirm overview raw]] lines 27–29. Do not silently substitute one partial-capture workflow for the other.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-affirm]] — method overview, financing and capability table

## Raw Sources

- [[raw/adyen/docs/payment-methods/affirm/web-drop-in/2026-09-15|Affirm Web Drop-in guide, captured 2026-09-15]]
