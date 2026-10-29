---
title: "Oney Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oney/web-component"
raw_files:
  - "adyen/docs/payment-methods/oney/web-component/2026-09-15.md"
tags: [adyen, oney, web, components, installments, capture]
---

## Overview

This [[adyen|Adyen]] page, fetched 2026-09-15 and marked last modified 2020-07-10, adds Oney to an existing Web Components integration through Sessions or Advanced flow. It covers shopper and order details, installment Components, capture, refund and test/live steps. See [[adyen-online-payments]]. The captured examples and setup instructions do not establish current account eligibility or a successful payment.

## Key takeaways

- Build the selected Web Components Sessions or Advanced base integration and add Oney in Customer Area first. `/sessions` is described as the default with Components v5.0.0 or later; `/payments` is for an additional use case. TEST curl examples use Checkout API v69 for `/sessions` and v72 for `/payments`, with `facilypay_3x`, FR/EUR and a web `returnUrl`; language snippets have their own library versions. These examples are not proof of live enablement.
- Both endpoint tables mark `lineItems`, shopper email/reference/name, telephone number and billing address required. Oney approves only if `lineItems` total matches `amount.value`; shopper reference has minimum length three, name maximum length 32, and billing postal code five characters. Delivery address, date of birth, locale and country code are unmarked; see the raw tables for country-specific phone and locale descriptions. Optional `oneydata.trustFlag` needs Oney enablement; `oneydata.merchantPays` overrides the configured interest-fee payer.
- Create a DOM target and Component per supported installment type. The table lists `facilypay_3x` and `4x` for FR/ES, `6x` for ES, and `10x` and `12x` for FR/ES. Shopper fields default to editable; optional visibility can be hidden, readOnly or editable, but hiding fields does not remove the duty to send their information in the payment request.
- Authorisation alone is insufficient for shipping: wait for successful capture. Capture may be manual or automatic, with or without delay; after more than six days, the authorization expires and payment must be authorised again. Cancel before capture; refund after capture. The page states EUR 1 minimum refund and refunds up to 13 months after capture, with a partial-refund request amount.
- Test sections give France and Spain scenarios and country/installment minimum amounts; the minimum table also includes Italy, which is absent from the Component installment-country table. The page says to request Oney 3x4x in live Customer Area before accepting live payments. The French `telephoneNumber` in both TEST curl examples (`+33 1 76 35 07 90`, lines 87 and 804) conflicts with the tables' required French mobile prefix `+336` or `+337` followed by eight digits (lines 59–60 and 773–774); do not treat the example number as validated Oney input. Its Advanced C# example sets `CountryCode = "EUR"`, unlike the table's FR/ES country codes and the other FR examples; do not copy that value as a validated country code.

## Detail locators

- Base flow, Customer Area and shipment prerequisite: pinned raw lines 15–43. API field tables and examples: `/sessions` lines 49–762; `/payments` lines 763–1253.
- Installment types and Component visibility: lines 1255–1323. Capture, cancellation, refund and limits: lines 1325–1345. Test scenarios, amount table and live request: lines 1347–1425.
- Example/table discrepancies: French mobile prefixes versus TEST sample telephone number at lines 59–60, 87, 773–774 and 804; Advanced C# `CountryCode = "EUR"` lines 1007–1012 versus FR/ES `/payments` field table lines 763–785; Italy minimum test amount lines 1413–1421 versus Component country table lines 1270–1276.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/oney/web-component/2026-09-15|Oney Web Component guide, fetched 2026-09-15]]
