---
title: "Adyen Marketplace refund currency conversion"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/currency-conversion/refunds"
raw_files:
  - "adyen/docs/marketplaces/currency-conversion/refunds/2026-09-15.md"
tags: [adyen, marketplaces, platforms, currency-conversion, refunds, pilot]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplace overview describes a **limited-availability pilot** for reconverting a refund so the customer receives funds in the original payment's processing currency while the user's balance is debited in the settlement currency. In [[adyen-currencies-and-fx]], a refund conversion uses the prevailing rate plus Adyen's markup and can leave a remainder to book. The page is an orientation and routing guide, not proof of current pilot access, a guaranteed FX quote, refund execution or bank receipt.

## Key takeaways

- In the example, the customer paid PLN 201.74 and the user received CZK 1000.00. A refund debits the user in CZK and credits the customer in PLN; the refund conversion applies the prevailing exchange rate plus markup. These figures illustrate the two money directions and currency roles, not an assured refund result or rate. See raw lines 19–26.
- Re-converting the settlement-currency refund may not equal the processing-currency amount the customer originally paid; that leftover is the **remainder**. The guide says a same-day refund remainder is **usually** negative, not always negative. See raw lines 28–30.
- The refund request **can** include a `type=Remainder` split to book that amount to the user or the marketplace. If omitted, the remainder is booked to the marketplace's liable balance account. Adyen recommends an explicit Remainder item for per-transaction reconciliation in the Balance Platform Accounting Report; the recommendation does not make the item a universal required field. The overview does not provide the child routes' request fields or refund outcome event. See raw lines 32–34.
- The next-step link labelled **Your marketplace** points to the platform route, but its description says to book the remainder “to the customer.” That conflicts with the body choice between user and marketplace and with the liable-account default. Treat the line as inconsistent navigation text, not a third destination; follow the appropriate child guide for implementation. See raw lines 32 and 36–46.

## Detail locators

- Pilot availability and change warning: raw lines 19–20.
- Original processing/settlement currencies, refund money direction, rate and markup: raw lines 24–26.
- Remainder cause, usual same-day sign, optional split, liable default and reconciliation advice: raw lines 28–34.
- User and marketplace routes and conflicting customer description: raw lines 36–46.

## Related

- [[adyen]] — provider profile.
- [[adyen-currencies-and-fx]] — canonical currency and FX concept.
- [[adyen-platforms]] — user, marketplace and liable balance-account context.
- [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-user]] — user-booking child route when present.
- [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-platform]] — marketplace-booking child route when present.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds]] — separate Platforms URL for the equivalent overview.

## Raw Sources

- [[raw/adyen/docs/marketplaces/currency-conversion/refunds/2026-09-15|Marketplace FX-refund overview — pinned 2026-09-15 raw snapshot]]
