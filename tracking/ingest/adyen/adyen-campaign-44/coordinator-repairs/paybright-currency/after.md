---
title: "Adyen PayBright payment-method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright"
raw_files:
  - "adyen/docs/payment-methods/paybright/2026-09-15.md"
tags: [adyen, paybright, bnpl, installments, canada, redirect]
---

## Overview

This Adyen [[adyen|Adyen]] PayBright overview was fetched on 2026-09-15 and carries a 2022-12-05 last-modified marker. It describes a Canadian buy now, pay later redirect method and routes to integration guides. The page explicitly says PayBright was acquired by Affirm and that Adyen will not accept new PayBright integrations. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-affirm|Affirm]].

## Key takeaways

- The described shopper offer is four equal installments. PayBright performs shopper risk checks before approving the payment; if successful, the page says PayBright takes full fraud risk and pays the merchant up front. These are conditional page claims, not evidence of an approved shopper, merchant payout or settlement.
- The described checkout redirects the shopper to PayBright to fill in or confirm details and validate information. After the installment request is accepted, the shopper can return to the merchant website or app. A return or acceptance message alone is not proof of Adyen authorization or capture.
- The page's feature matrix identifies a CA/CAD redirect BNPL method. It marks recurring unsupported; refunds, partial and multiple partial refunds, separate, partial and multiple partial captures supported. Chargebacks are marked supported with an unresolved “See note” marker; this capture contains no explanatory note. Treat the matrix as historical documentation rather than current account-level eligibility.
- Navigation links lead to Web, iOS, Android, API-only and Pay by Link paths. This overview does not specify SDK versions, request fields, detailed result handling or implementation prerequisites; follow the relevant child guide for those details.

> [!warning] Contradiction
> The overview matrix lists Canada (`CA`) and `CAD` (raw lines 31–33), while [[source-adyen-docs-payment-methods-paybright-ios-drop-in|the iOS Drop-in guide]] shows Canadian `/payments` Java/PHP examples with `USD` (raw lines 883–888 and 970–976). These examples do not establish USD support. The overview also states that Adyen accepts no new PayBright integrations; later live-request instructions in the guides do not override that restriction.

## Detail locators

- Identity, acquisition/new-integration warning, four-installment offer and risk/payment wording: pinned raw lines 15–23.
- Redirect and shopper confirmation sequence: pinned raw lines 25–29.
- Feature matrix, including the unresolved chargeback note: pinned raw lines 31–33.
- Web, iOS, Android, API-only and Pay by Link navigation: pinned raw lines 35–65.

## Related

- [[adyen-online-payments]] — main Adyen online payment concept
- [[source-adyen-docs-payment-methods-affirm]] — separate Affirm method overview

## Related raw API references

- [[raw/adyen/docs/payment-methods/paybright/web/2026-09-15|PayBright Web guide]]
- [[raw/adyen/docs/payment-methods/paybright/ios/2026-09-15|PayBright iOS guide]]
- [[raw/adyen/docs/payment-methods/paybright/android/2026-09-15|PayBright Android guide]]
- [[raw/adyen/docs/payment-methods/paybright/api-only/2026-09-15|PayBright API-only guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/2026-09-15|PayBright overview, fetched 2026-09-15]]
