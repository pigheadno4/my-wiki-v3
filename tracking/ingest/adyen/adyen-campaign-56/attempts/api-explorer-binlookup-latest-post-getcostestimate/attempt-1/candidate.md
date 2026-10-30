---
title: "Adyen BIN Lookup API POST /getCostEstimate (captured v54)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BinLookup/latest/post/getCostEstimate"
raw_files:
  - "adyen/api-explorer/BinLookup/latest/post/getCostEstimate/2026-09-15.md"
tags: [adyen, bin-lookup, cost-estimate, surcharging, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents BinLookup API `POST /getCostEstimate` on the displayed test `https://pal-test.adyen.com/pal/servlet/BinLookup/v54` server. It estimates interchange and scheme fees **before** payment authorisation for merchants operating in Australia, the EU or the UK. Estimates depend on assumed transaction characteristics that are not all known in advance. It is an estimate/lookup, not an actual payment, charged fee or permission to surcharge. See [[adyen]], [[adyen-online-payments]] and [[adyen-currencies-and-fx]].

## Key takeaways

- The request property table marks transaction `amount.currency` and minor-unit `amount.value`, plus `merchantAccount`, required. It marks `cardNumber` and `encryptedCardNumber` optional individually but says one of those must be provided “in a payment request”; a separate recurring-detail example uses `selectedRecurringDetailReference` and `shopperReference` without either card-number field. Therefore the examples do not support a universal card-number requirement for every estimate path. Raw card numbers are for PCI-compliant use cases; the encrypted alternative is described for non-PCI-compliant use cases.
- Optional `assumptions` cover successful 3DS authentication, valid Level 3 data and installments. For merchants not using Adyen as the payment-authorisation gateway, `merchantDetails.countryCode` is required by its description. `shopperReference` is required for recurring payments; `selectedRecurringDetailReference` can select a stored detail, including `LATEST`. These are conditional descriptions within optional parent fields, not global required marks.
- The 200 response schema offers optional `costEstimateAmount` (estimated scheme fee plus interchange in settlement currency, or EUR when settlement currency cannot be determined), `costEstimateReference`, `resultCode` and card-BIN details. Some BIN fields require merchant-account settings. The examples show EUR 12 and `Success` only; those values do not predict actual fees. The introduction says the response also contains which surcharging policy is possible, but the response table shown here has no named surcharging-policy property. Treat that as an unresolved source gap, not a documented field contract or legal permission.
- The page lists 400/401/403/422/500 generic request/error schemas and a 400 error example. The captured `latest` path shows test BinLookup v54, not current version, live regional eligibility, actual fee assessment, authorization or settlement.

## Detail locators

- Regional scope, estimate purpose/assumption limit, displayed server: raw lines 5–16.
- Request schema: lines 20–45; card selectors 30–31, non-Adyen gateway condition 33–34, recurring selectors 37–45; examples 47–142.
- 200 response fields and qualification: lines 143–167; generic error schemas 170–237; response examples 239–297.

## Related

- [[adyen-online-payments]] — provider concept and reciprocal source route.
- [[adyen-currencies-and-fx]] — currency/minor-unit and settlement-currency context.

## Raw Sources

- [[raw/adyen/api-explorer/BinLookup/latest/post/getCostEstimate/2026-09-15|BinLookup API POST /getCostEstimate snapshot (2026-09-15)]]
