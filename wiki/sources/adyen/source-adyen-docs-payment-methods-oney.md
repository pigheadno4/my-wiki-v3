---
title: "Adyen Oney overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oney"
raw_files:
  - "adyen/docs/payment-methods/oney/2026-09-15.md"
tags: [adyen, oney, buy-now-pay-later, online-payments]
---

## Overview

This 2026-09-15 [[adyen]] Docs capture describes Oney as a buy now, pay later installment method with a redirect checkout flow. The shopper selects Oney, enters and validates details on Oney's webpage, and sees a message that the **installment request** was accepted before returning to the merchant website or app. That message is not, by itself, evidence of final payment, capture, or settlement. The page routes to Web, API-only and Pay by Link integration material. [[adyen-online-payments]]

## Key takeaways

- **Entity and risk condition:** The page says a European-country/region entity is needed for Oney compliance checks, and Oney performs shopper risk checks at purchase time (raw lines 23–31). This statement does not establish a particular merchant's approval or a shopper's credit decision.
- **Captured method scope:** Its matrix labels Oney a redirect buy now, pay later method for FR, ES and IT in EUR. The prose says it is gaining popularity in France and Spain; the matrix also includes Italy. Country card and installment rows list France: Visa, Mastercard, Cartes Bancaires and 3x/4x/10x/12x; Spain: Visa/Mastercard and 3x/4x/6x/10x/12x; Italy: Visa/Mastercard and 3x/4x (raw lines 23, 33–41). These are captured documentation entries, not current merchant or shopper eligibility.
- **Authorization expiry:** The country table says that if capture occurs after more than six days, the payment authorization expires and the payment must be authorized again; Spain and Italy say “Same as France” (raw lines 37–41). Do not infer that a capture by day six succeeds.
- **Feature marks:** The captured matrix marks refunds, partial refunds, multiple partial refunds, separate captures and partial captures as supported. It marks recurring, multiple partial captures and chargebacks as unsupported (raw lines 33–35). These marks do not establish that any transaction modification completed.
- **Integration routes:** Web points to a prebuilt UI route; API only points to building a UI for website, iOS or Android; Pay by Link points to adding Oney to payment methods for payment links (raw lines 43–61). This overview does not specify request fields, return handling or final-result verification; consult the linked guide for a chosen route.

## Detail locators

- Identity, regional prose and European-entity/risk condition: pinned raw lines 15–25.
- Shopper redirect and installment-request message: pinned raw lines 27–31.
- Method, feature and country/installment tables: pinned raw lines 33–41.
- Web, API-only and Pay by Link guide links: pinned raw lines 43–61.

## Related

- [[adyen-online-payments]] — online payment architecture and method retrieval context.
- [[source-adyen-docs-payment-methods]] — broader payment-method catalog.

## Raw Sources

- [[raw/adyen/docs/payment-methods/oney/2026-09-15|Oney overview, captured 2026-09-15]]
