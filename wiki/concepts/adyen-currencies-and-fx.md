---
title: "Adyen Currencies and FX"
type: concept
category: technology
tags: [adyen, currencies, minor-units, foreign-exchange]
---

## Overview

Adyen's API currency reference pairs each currency code with an amount decimal count. In the 2026-09-15 snapshot, most Adyen APIs require amount values in minor units; Terminal API is the stated exception. For CLP, CVE, IDR, and ISK, Adyen says its table's decimals take precedence over the differing ISO 4217 counts when submitting minor-unit amounts. The snapshot lists CLP 2, CVE 0, IDR 0, and ISK 2.

Where Adyen converts a transaction amount between currencies, it describes an FX reference rate plus an FX management fee or spread. The fee calculation comes from the merchant's Adyen contract; the default currency-category route and optional Visa/Mastercard scheme-rate route are detailed in the source. The snapshot does not establish a current currency's availability or a merchant-specific conversion rate or fee.

## Sources

- [[source-adyen-docs-development-resources-currency-codes]] — Adyen currency-code and decimal table, Terminal API exception, four ISO differences, and contract-qualified FX fee structure (webpage snapshot, 2026-09-15).
