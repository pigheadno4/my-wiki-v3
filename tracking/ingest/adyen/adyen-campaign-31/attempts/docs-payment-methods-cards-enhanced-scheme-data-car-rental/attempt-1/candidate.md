---
title: "Adyen car-rental enhanced scheme data"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/car-rental"
raw_files:
  - "adyen/docs/payment-methods/cards/enhanced-scheme-data/car-rental/2026-09-15.md"
tags: [adyen, cards, enhanced-scheme-data, car-rental]
---

## Overview

This [[adyen]] guide covers car-rental enhanced scheme data (ESD) for **US domestic** card transactions by businesses with eligible travel-related MCCs. It names rental dates and agreements as industry data and describes conditional Visa downgrade prevention and Mastercard industry-rate qualification. Sending the fields does not by itself establish merchant eligibility, a particular interchange rate, or payment/capture success. This child guide inherits the parent ESD requirements, including its Advanced-flow online integration and webhook prerequisites. [[adyen-online-payments]]

## Key takeaways

- Eligible MCCs in this snapshot are **3351–3500, 7512, and 7513** for Mastercard and Visa, and **7519** for Mastercard only. The page limits car-rental ESD to commercial and consumer cards. These are stated categories, not evidence that a specific merchant or card is enabled. See raw lines 17–52.
- For automatic or delayed automatic capture, it recommends sending car-rental ESD in Checkout API `/payments` under `additionalData.carRental`. For manual single/multiple partial capture, it points to Classic API `/capture`, because Checkout API does **not** support car-rental ESD in capture requests. The `travelEntertainmentAuthData.market` and `.duration` fields are payment-request-only. Do not transfer this Classic capture route to Checkout capture. See raw lines 32–41 and 54–66.
- The guide marks rental agreement number, renter name, return city/state/country/location ID, checkout date, and return date as required; other listed fields include rate, rental days, location, tax/fuel/insurance and one-way charges. The table's precise field names and its required column are at raw lines 68–90. These are guide-level fields, not a complete API schema.
- There are material source inconsistencies: the “Send car rental data” section begins “Include airline data,” despite the car-rental heading and fields; the Classic capture instructions name `additionalData.enhancedSchemeData.carRental`, while the adjacent Classic v72 example uses flattened `additionalData` keys such as `carRental.rentalAgreementNumber`. The examples also place `-X POST` on a line without the joining backslash before `-d`, and include raw **test** card data. Treat snippets as illustrations to check against the relevant API/version and card-data-handling requirements, not copy-ready live requests. See raw lines 61–66 and 94–188.

## Detail locators

- MCC/scheme table and Checkout-vs-Classic capture limit: raw lines 26–59.
- Required and other car-rental fields: raw lines 68–90.
- Checkout API v72 TEST `/payments` and Classic Payment API v72 TEST `/capture` examples: raw lines 94–188. A test-card table follows at raw lines 190–197.
- The linked parent ESD overview owns general eligibility and invalid/incomplete-data behavior; this page's links alone do not establish actual fee savings or an authorization result.

## Related

- [[adyen-online-payments]]
- [[adyen-payment-capture]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/car-rental/2026-09-15|Adyen car-rental ESD snapshot]]
