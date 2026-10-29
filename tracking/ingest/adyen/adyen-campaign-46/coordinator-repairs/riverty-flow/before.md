---
title: "Adyen Riverty overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/riverty"
raw_files:
  - "adyen/docs/payment-methods/riverty/2026-09-15.md"
tags: [adyen, riverty, buy-now-pay-later, invoices, online-payments]
---

## Overview

This 2026-09-15 [[adyen]] Docs capture is a Riverty **buy now, pay later invoice-payment overview**. It describes a direct payment flow, shopper payment choices, a country/currency and feature matrix, and Web/API-only child routes. The page was last modified 2024-07-16; its claims are a documentation snapshot, not merchant approval, an executed payment or verified settlement. [[adyen-online-payments]]

## Key takeaways

- **Merchant funding and risk roles:** The page says Riverty invoice payments are immediately settled in full to merchants, Riverty assumes shopper liability and credit risk and handles reminders/debt collection, while disputes are handled directly with merchants. It separately says funds are settled T+2 and Riverty is unavailable for sales day payout. Read “immediately settled in full” with the stated T+2 settlement timing rather than promising instant fund receipt; the page does not show a transaction or payout record (raw lines 21–23).
- **Shopper payment choices:** It lists payment in 14 days, a monthly consolidated invoice, secure direct debit, or split installments. The split-installment option is expressly limited to Germany, Austria and Netherlands; that narrower option scope must not be expanded to every country in the matrix (raw lines 25–30).
- **Captured method scope and feature marks:** The matrix labels Riverty Buy Now Pay Later with a **Direct** flow, countries DE/AT/CH/NL/BE and currencies EUR/CHF. It marks recurring unsupported and refunds, partial refunds, separate captures, partial captures and chargebacks supported. The page does not map each currency or each shopper option to every listed country, nor does a feature mark establish that a modification or chargeback occurred (raw lines 32–34).
- **Integration routes:** Web points to prebuilt UI solutions for websites; API only points to a merchant-built UI for website, iOS or Android. This overview does not provide request fields or outcome handling; use the selected child guide for those details (raw lines 36–48).

## Detail locators

- Method identity, merchant/Riverty responsibilities, T+2 and sales day payout limit: pinned raw lines 15–23.
- Shopper payment-choice list and split-installment geography: pinned raw lines 25–30.
- Direct-flow country/currency and feature matrix: pinned raw lines 32–34.
- Web and API-only child links: pinned raw lines 36–48.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods]] — broader payment-method catalog.

## Raw Sources

- [[raw/adyen/docs/payment-methods/riverty/2026-09-15|Riverty overview, captured 2026-09-15]]
