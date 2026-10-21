---
title: "Convert a Marketplace payment between processing and settlement currencies"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/currency-conversion/payments"
raw_files:
  - "adyen/docs/marketplaces/currency-conversion/payments/2026-09-15.md"
tags: [adyen, marketplaces, currency-conversion, payments]
---

## Overview

This pinned Marketplace orientation page distinguishes the **processing currency** paid by a customer from the **settlement currency** received by a user. If they differ, the described currency conversion exchanges the former for the latter so the customer is debited and the user credited in their respective currencies. The page marks currency conversion **limited availability / pilot** and says the process may change; current enablement is not established. See [[adyen]] and [[adyen-currencies-and-fx]] (raw lines 19–26).

## Key takeaways

- First fix the goods or services price in **either** the user's settlement currency or the customer's processing currency. Calculate its amount in the other currency using the day's prevailing exchange rate, then include costs in both currencies in a POST `/payments` request (raw lines 28–39).
- Fixing the **settlement-currency** price keeps the user's amount in their chosen currency fixed; the customer-facing processing amount is calculated. Fixing the **processing-currency** price keeps the customer's amount fixed; the user's settlement amount is calculated. The linked detailed pages own their respective request fields, calculation and remainder behavior (raw lines 41–51).
- This page describes intended flow and navigation, not a specific rate, required API role, account eligibility, authorized payment, capture, final booking, settlement, payout or bank receipt. A POST request alone does not prove either side's money movement (raw lines 28–51).

## Detail locators

- Limited availability and actor/currency definitions: raw lines 15–26.
- Price fixing, conversion and request sequence: raw lines 28–39.
- Separate fixed-settlement and fixed-processing implementation guides: raw lines 41–51.

## Related

- [[adyen]]
- [[adyen-currencies-and-fx]]
- [[adyen-platforms]]
- [[source-adyen-docs-marketplaces-currency-conversion-payments-fix-settlement-currency]]
- [[source-adyen-docs-marketplaces-currency-conversion-payments-fix-processing-currency]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/currency-conversion/payments/2026-09-15|Pinned currency-conversion payments overview]]
