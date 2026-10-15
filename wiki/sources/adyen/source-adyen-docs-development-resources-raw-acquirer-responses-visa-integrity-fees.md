---
title: "Mapping to Visa system integrity fee categories | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees"
raw_files:
  - "adyen/docs/development-resources/raw-acquirer-responses/visa-integrity-fees/2026-09-15.md"
tags: [adyen, visa, raw-acquirer-responses, payment-retries, scheme-fees]
---

## Overview

This 2026-09-15 Adyen webpage snapshot maps raw refusal responses for failed Visa transactions to Visa system integrity fee categories. It is aimed at an online-payments integration with merchant-built retry logic, so the merchant can distinguish refusals that the page says must not be retried from those with a dated retry allowance. The page describes excessive-retry and data-quality fee types; it does not establish current fee amounts, regional applicability, merchant-specific liability, or a live scheme rule. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Before using the mapping, the page requires an online-payments integration and enabling raw responses in Customer Area. Its `refusalCodeRaw` field is available only for Visa and Mastercard transactions through Adyen's own acquiring platform; `refusalReasonRaw` contains the full raw response. See raw `## Requirements` and `## Mapping of raw responses to categories`.
- In this dated page, category 1 means do not retry; categories 2, 3, and 4 describe at most 15 retries in a 30-day period. Category 3 is associated with incorrect payment details and the page also discusses data-quality fees. Consult the raw category text and code table before interpreting any particular refusal; this snapshot is not a current retry policy.
- The raw table lists code `14` in both category 1 (no retry) and category 3 (maximum 15 in 30 days). This internal conflict leaves code `14` without a reliable single retry instruction from this page. Do not infer which row governs from the snapshot alone.

## Detail locators

- `## Categories of system integrity fees`: fee types, category meanings, retry statements, and the page's conditions.
- `## Mapping of raw responses to categories`: response-field availability and the complete code/reason/retry table, including the conflicting code `14` rows.
- `## See also`: Adyen's links to its raw responses and risk-management guides; those linked pages are navigation only here.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/development-resources/raw-acquirer-responses/visa-integrity-fees/2026-09-15|Adyen Visa integrity-fee mapping, 2026-09-15]]
