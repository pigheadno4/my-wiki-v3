---
title: "Adyen Titres-restaurant payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/titres-restaurant"
raw_files:
  - "adyen/docs/payment-methods/titres-restaurant/2026-09-15.md"
tags: [adyen, titres-restaurant, meal-vouchers, france, conecs, prepaid-cards]
---

## Overview

This [[adyen|Adyen]] payment-method overview, fetched 2026-09-15 and marked **last modified 2023-06-21**, describes French Titres-restaurant meal-voucher prepaid cards. Employers provide the cards to employees for food and beverages. The captured page states a **EUR 25 daily spending limit**, says any excess purchase amount may be paid with another method, and says the cards cannot be used on Sundays or public holidays. These are historical page claims, not verified current legal or issuer rules. See [[adyen-online-payments]].

## Key takeaways

- **Issuer/channel distinction:** The page lists **Bimpli, Sodexo and Up Déjeuner** meal vouchers for online processing with Adyen, and **Edenred** for in-person processing. It says all meal-voucher cards are co-badged with **Conecs**. Do not infer online Edenred support or in-person support for every named online issuer from this overview.
- **Captured feature matrix:** The single row describes direct prepaid/gift-card payments in **FR/EUR**. It marks **separate captures supported**. Recurring, full/partial/multiple partial refunds, partial/multiple partial captures and chargebacks are marked unsupported. This matrix is a 2023-modified documentation snapshot, not account-specific eligibility or a guarantee of a particular issuer's current behavior.
- **Activation:** Before integration, the page says the merchant needs official authorization from the Mealvoucher National Comission, which provides a *Carte de domiciliation CONECS* and CONECS MID. A **separate contract with each issuer** to be accepted is also required; its activation steps name Bimpli, Sodexo and Up Déjeuner. The source's spelling of the commission is retained as written; current authorization criteria require fresh verification.
- **Integration routes:** The page links Web, iOS and API-only child guides, plus an in-person Terminal API gift-card route. Those links are navigation, not evidence that every issuer or merchant account is enabled on every channel.

## Detail locators

- Method identity, historical daily limit, split remainder and Sunday/holiday restriction: pinned raw lines 15–19. Issuer/channel and Conecs statements: line 21.
- FR/EUR direct prepaid/gift-card feature matrix: lines 23–25. Authorization, CONECS MID and issuer-contract steps: lines 27–34. Web, iOS, API-only and in-person routes: lines 36–60.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/titres-restaurant/2026-09-15|Titres-restaurant overview, fetched 2026-09-15]]
