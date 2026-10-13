---
title: "Adyen Data Quality and Risk Field Reference"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/configure-your-risk-profile/risk-field-reference"
raw_files:
  - "adyen/docs/risk-management/configure-your-risk-profile/risk-field-reference/2026-09-15.md"
tags: [adyen, risk-management, protect, data-quality, risk-fields, checkout-api]
---

## Overview

This Adyen Docs snapshot explains how payment-request data supports Protect's machine-learning risk classification, risk lists, and custom-rule matching. It gives an example field-to-risk-use table for merchants configuring an online payment request. See [[adyen]] and [[adyen-risk-management]]. The page is guidance about risk-data quality and configured signal use, not a guarantee of fraud classification or a complete Checkout API request schema.

## Key takeaways

- The page uses `amount` and `reference` as examples of fields mandatory to make a payment, while saying `shopperIP`, `shopperReference`, and `shopperEmail` are **not always required** but strongly recommended. Its table heading “Required field in payment request” names fields for the corresponding listed risk data point or rule use; it must not be read as making every table row universally mandatory for every payment.
- Machine-learning fraud and bot-attack rules use payment-request data along with historical shopper data and payment-form interaction patterns. Risk lists and custom rules require the relevant request data to be present to trigger the intended action. Adyen recommends collecting as many useful fields as possible and avoiding dummy or placeholder values; that is advice about data quality, not a universal API-requiredness statement.
- The example table maps billing and delivery addresses, email, IP, shopper name/reference/phone, card information, account creation date, browser information, delivery timing, and `riskData` to particular risk-list, machine-learning, or custom-rule uses. Consult the raw table for each exact field and applicable use rather than sending every example indiscriminately.
- For a custom `hoursToDelivery` rule, the table says to include delivery timing as `deliveryDate` with Checkout API v69 or earlier and `deliverAt` with v70 or later. This is a version-specific risk-field mapping, not a statement that every payment requires a delivery date.
- For Web Drop-in/Components, the page describes additional risk data collected for submission when the shopper pays, with an option to collect more outside checkout. A Web API-only integration can collect and submit that data too. The linked data-collection guide owns the exact client implementation.

## Detail locators

- Opening, raw lines 15–21 — purpose and mandatory-versus-recommended field distinction.
- `## Data quality`, raw lines 23–33 — machine-learning inputs, rule/list matching, data-quality recommendation, and Web integration routes.
- Example risk-field table, raw lines 35–66 — data-point-to-risk-use mappings and exact request fields, including Checkout API version split for delivery timing and `riskData`.
- `## See also`, raw lines 68–75 — linked risk lists, custom and machine-learning rules, post-authorization rules, data collection, and Uplift guidance.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — Protect and risk-rule concept.
- [[source-adyen-docs-risk-management-fraud-data-collection]] — separate Web collection-flow guidance.

## Raw Sources

- [[raw/adyen/docs/risk-management/configure-your-risk-profile/risk-field-reference/2026-09-15|Adyen Docs — Data quality and risk field reference (2026-09-15 snapshot)]]
