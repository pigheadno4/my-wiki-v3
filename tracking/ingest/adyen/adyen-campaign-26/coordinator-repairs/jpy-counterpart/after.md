---
title: "Adyen Currency Codes, Minor Units, and FX Fees"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/currency-codes"
raw_files:
  - "adyen/docs/development-resources/currency-codes/2026-09-15.md"
tags: [adyen, currencies, minor-units, amounts, foreign-exchange, fx-fees]
---

## Overview

This Adyen Docs snapshot lists currency codes and decimal counts for API amount values and explains how Adyen describes currency conversion rates and FX management fees. It is a provider-specific amount-formatting reference, linked to [[adyen]] and [[adyen-currencies-and-fx]]. Its currency table and fee categories are snapshot evidence, not a determination of current account, payment-method, or currency availability or a fee quote for a transaction.

## Key takeaways

- Most Adyen APIs expect the amount `value` in the currency's minor units; Terminal API is the stated exception. The raw gives GBP 10 → 1000, JPY 10 → 10, and BHD 10 → 10000 as examples for two-, zero-, and three-decimal currencies. The separate [[source-adyen-docs-marketplaces-balance-updates-use-cases|Marketplace Balance webhook example]] labels a JPY 1,000 threshold but sets `conditions.value: 100000` and shows `available: 95000`; that page does not establish a webhook-specific amount scale, so verify the current Balance webhook API contract before reusing its threshold (Marketplace raw lines 169–188, 197–234).
- Adyen's table, rather than ISO 4217 decimals, governs minor-unit submission for four named differences: CLP uses 2 decimals, CVE 0, IDR 0, and ISK 2 in this snapshot. In particular, ISO lists ISK with zero decimals, while this Adyen request convention uses two.
- When Adyen converts currencies, the page describes an FX reference rate and an FX management fee or spread. The fee calculation is specified in the merchant's Adyen contract. By default, the page groups currencies into two categories for the fee; it also describes an optional scheme-rate setup for Visa and Mastercard, while other methods use the currency category. The document supplies no universal numeric rate or merchant-specific fee.
- The full code/decimal table and category-one currency list are in the raw locators below; applying either list to a later payment should use current Adyen documentation and the merchant's configured terms.

## Detail locators

- Opening, raw lines 15–19 — currency-code and amount-value purpose.
- `## Currency codes`, raw lines 21–162 — snapshot code, currency-name, and decimal table, including CLP/CVE/IDR/ISK.
- `## Minor units`, raw lines 164–172 — Terminal API exception and GBP/JPY/BHD amount examples.
- `### Different number of decimals`, raw lines 174–178 — ISO-versus-Adyen differences and ISK example.
- `## Currency conversion rates and fees`, raw lines 180–197 — FX reference rate, contract-specific management fee, default currency categories, and optional Visa/Mastercard scheme-rate setup.

## Related

- [[adyen]] — provider page.
- [[adyen-currencies-and-fx]] — Adyen-specific amount and FX concept.
- [[adyen-terminal-api]] — separately documented Terminal API surface, named as the minor-unit exception here.

## Raw Sources

- [[raw/adyen/docs/development-resources/currency-codes/2026-09-15|Adyen Docs — Currency codes and minor units (2026-09-15 snapshot)]]
