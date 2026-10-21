---
title: "Adyen Marketplace-path currency conversion overview"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/currency-conversion"
raw_files:
  - "adyen/docs/marketplaces/currency-conversion/2026-09-15.md"
tags: [adyen, marketplaces, platforms, currency-conversion, foreign-exchange, pilot]
---

## Overview

This 2023-modified, 2026-09-15-captured Marketplace-path overview introduces Adyen's pilot currency conversion for transactions processed on behalf of platform users: a transaction can be accepted in one currency and settled in another. It is a navigation hub for separate payment and refund guides, not an implementation recipe or evidence that a given marketplace, currency pair or user has access. See [[adyen]] and [[adyen-currencies-and-fx]] for provider and FX context; [[adyen-platforms]] supplies the modern platform model.

## Key takeaways

- The page explicitly labels currency conversion **limited availability** and in pilot, warns that processes and documentation may change, and directs interested platforms to their Adyen contact. Its broad description of customer and user preferred currencies does not define rates, spreads, split destinations, eligible regions or exact API fields; the linked payment and refund guides own those details.
- Adyen describes modifying per-transaction API requests so acceptance/processing currency differs from settlement currency. Keep the customer's payment currency separate from the user's settlement currency, and keep conversion separate from payout to a bank. This page does not demonstrate authorization, capture, conversion execution, balance booking, payout or bank receipt.
- Child routes are **Payments** for converting users' payments and **Refunds** for converting users' refunds. These are separate flows; do not infer that a payment conversion automatically defines its refund's FX rate, remainder booking or recipient.

## Detail locators

- Pilot/limited-availability warning and Adyen-contact route: raw lines 15–20. Different acceptance and settlement currencies: lines 24–26. Payment and refund child links: lines 28–36.

## Related

- [[adyen]] — provider context.
- [[adyen-currencies-and-fx]] — main currencies and FX concept.
- [[adyen-platforms]] — modern platform integration context.
- [[source-adyen-docs-marketplaces-currency-conversion-payments-fix-processing-currency]] — fixed-customer-currency payment path.
- [[source-adyen-docs-marketplaces-currency-conversion-payments-fix-settlement-currency]] — fixed-user-settlement-currency payment path.
- [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-user]] — refund remainder to user.
- [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-platform]] — refund remainder to platform.

## Raw Sources

- [[raw/adyen/docs/marketplaces/currency-conversion/2026-09-15|Adyen Docs: Currency conversion (2026-09-15 snapshot; page last modified 2023-11-21)]]
