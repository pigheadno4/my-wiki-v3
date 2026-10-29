---
title: "PaySafeCard payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/2026-09-15.md"
tags: [adyen, paysafecard, prepaid, gift-cards, customer-data-exchange]
---

## Overview

This 2026-09-15-captured PaySafeCard overview describes an online prepaid method, its overview capability and country/currency tables, a conditional Customer Data Exchange route for EU gambling KYC, and Web/mobile/API-only integration choices. It is a dated source snapshot, not evidence of current market availability, merchant-account entitlement, regulatory compliance, or a successful live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page describes PaySafeCard as an online **prepaid** method. Its promotional statements about market leadership, cash-like safety and suitability for particular shoppers are source marketing claims, not measured current facts or a security guarantee (raw line 23).
- The capability matrix labels it **Prepaid and gift cards**, with a **Direct** payment flow, **International** countries and **Multiple** currencies. It marks **recurring** and **refunds** with checks, while **partial refunds**, **multiple partial refunds**, **separate captures**, **partial captures**, **multiple partial captures**, and **chargebacks** are crossed. These are overview marks rather than a complete recurring/refund implementation recipe or proof of enabled merchant capability (raw lines 25–27).
- In EU countries **where gambling-customer KYC is required**, the page says Customer Data Exchange **can be used** to prevent acquiring funds from an anonymous shopper. This is a conditional feature statement, not a universal KYC mandate, guarantee of compliance, or proof of account setup; the linked child guide owns implementation (raw lines 29–31).
- The page lists country/region, its `countryCode` label, and currency pairs in a table (raw lines 33–86). The table repeats **Belgium/BE/EUR** and **Ireland/IE/EUR** rows and uses **UAE** and **UK** as `countryCode` entries. Retain those literal captured values; verify accepted request codes and present availability against current Adyen configuration before implementation. Do not infer every currency is accepted in every listed market from the top-level “Multiple” label.
- Integration navigation links pre-built UI routes for **Web, iOS, Android, React Native and Flutter** and an **API-only** merchant-built UI route for website/iOS/Android. The “See also” 3D Secure and Capture links are general navigation, not PaySafeCard-specific capability evidence (raw lines 88–131).

> [!warning] Captured country table
> The source repeats Belgium and Ireland and labels United Arab Emirates `UAE` and United Kingdom `UK` in the `countryCode` column (raw lines 39–41, 54–59, 83–84). Do not silently normalize these values or treat the captured table as a current API validation contract.

> [!warning] Contradiction — captured child guide differs
> This overview labels the flow **Direct** (raw lines 25–27), while [[source-adyen-docs-payment-methods-paysafecard-api-only|the API-only guide]] explicitly requires `action.type: redirect` and returns a redirect action (child raw lines 25–28, 570–585). Its discovery list uses **AE, GB, GIB, SRB** (child raw line 50), while this overview uses **UAE, UK, GI, RS** for the same named regions (overview raw lines 51, 76, 83–84). Retain both captured statements; these pages do not resolve accepted request codes or eliminate redirect handling. Check the relevant current API/account configuration before implementation.

## Detail locators

- Method positioning and capability matrix: raw `# PaySafeCard` lines 15–27.
- Conditional EU gambling Customer Data Exchange statement: raw `## Customer Data Exchange` lines 29–31.
- Country/region and currency table: raw `## Supported countries/regions and currencies` lines 33–86.
- Platform chooser and general See also links: raw lines 88–131.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/2026-09-15|PaySafeCard method overview, captured 2026-09-15]]
