---
title: "Convert the currency of a refund | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/currency-conversion/refunds"
raw_files:
  - "adyen/docs/platforms/online-payments/currency-conversion/refunds/2026-09-15.md"
tags: [adyen, platforms, online-payments, currency-conversion, refunds, pilot]
---

## Overview

This 2023-last-modified [[adyen]] for Platforms overview, captured 2026-09-15, describes a **limited-availability pilot** for converting a refund so a customer can receive it in the original payment, or **processing**, currency while the user's amount is debited in the **settlement** currency. In its illustration, the customer paid PLN and the user received CZK; a refund debits the user in CZK and credits the customer in PLN. Adyen says conversion uses the prevailing exchange rate plus a conversion markup. This page does not establish current pilot access, a guaranteed rate, refund execution, or bank receipt. [[adyen-currencies-and-fx]] [[adyen-platforms]]

## Remainder and booking choice

- Because exchange rates move and Adyen applies a markup, reconverting the settlement-currency refund amount may not equal the processing-currency amount originally paid. The difference is the **remainder**. The page says a same-day refund remainder is *usually* negative, not invariably so. The PLN/CZK figures are an illustration, not a rate or exact refund promise. See raw lines 24–30.
- A refund request can include a split item with `type: Remainder` to book that leftover amount to the user's balance account or the platform. If the request does not specify the remainder booking, it goes to the platform's liable balance account. Adyen recommends including the item for per-transaction reconciliation in the Balance Platform Accounting Report; this is advice, not a stated mandatory request field. This overview does not give the child routes' request shapes, rate adjustment details, or an outcome webhook. See raw lines 32–34.
- **Pinned navigation conflict:** the next-step label **Your platform** at raw line 44 points to the platform route, but its description at line 46 says to book the remainder “to the customer.” The body at line 32 instead offers user or platform booking and says the default is the platform liable account. Treat the line-46 description as inconsistent navigation text, not a third remainder destination; use the relevant child guide for implementation details. See raw lines 32 and 36–46.

## Detail locators

- **Pilot availability and change warning:** raw lines 19–20.
- **Original processing currency, user settlement currency, prevailing refund FX rate and markup:** raw lines 24–26.
- **Remainder cause, usual same-day sign, optional split choice, liable default and reconciliation recommendation:** raw lines 28–34.
- **User/platform next-step routes and conflicting customer description:** raw lines 36–46.

## Related

- [[adyen-currencies-and-fx]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds-your-user]] — separate user-booking route
- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds-your-platform]] — separate platform-booking route

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/currency-conversion/refunds/2026-09-15|Adyen Platforms refund currency-conversion overview — collected 2026-09-15]]
