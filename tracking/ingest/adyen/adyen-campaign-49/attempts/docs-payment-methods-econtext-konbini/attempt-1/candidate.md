---
title: "Japanese convenience stores via econtext"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/econtext-konbini"
raw_files:
  - "adyen/docs/payment-methods/econtext-konbini/2026-09-15.md"
tags: [adyen, econtext, konbini, japan, jpy, cash, voucher]
---

## Overview

This Adyen method overview, captured on 2026-09-15 and marked last modified 2023-02-06 in the raw, describes **Japanese convenience-store payments through partner econtext**. It separates a 7-Eleven redirect from native voucher display for other listed stores, then a later in-store cash payment. It gives a default offer-expiry window and a JP/JPY capability matrix, and routes to Web, API-only and Pay by Link guides. It is not a complete integration recipe or evidence of current store/merchant eligibility or a paid transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page lists **7-Eleven, Lawson, Mini Stop, Family Mart, Seicomart and Pay-easy**. It specifically marks **7-Eleven as requiring a local entity**. That condition is store-specific in this snapshot; the page does not establish the applicant's present eligibility (raw lines 23–30).
- On the website, the shopper provides **full name, telephone number and email address**. For **7-Eleven**, they are redirected to 7-Eleven's page to see the voucher; for another listed convenience store, the voucher appears natively on the merchant website. The shopper then goes to the selected store, provides the reference number and phone number to obtain a voucher ticket, pays the cashier **in cash**, and receives a receipt. Voucher display or ticket issue precedes payment; neither alone proves the sale is paid (raw lines 32–40).
- By default the **offer stays open up to seven days**, allowing payment up to seven days after voucher generation; the page says to contact Adyen Support to change offer expiry. This is an offer window, not an assertion that cash payment occurs immediately or a promise of late-payment acceptance (raw line 42).
- The matrix labels **7-Eleven** as **Cash and ATM / Redirect / JP / JPY** and **other convenience stores** as **Cash and ATM / Additional action / JP / JPY**. It marks recurring, refunds, separate captures and chargebacks unavailable for both rows. These are method-level snapshot indicators, not proof that a specific merchant/account is enabled (raw lines 44–47).
- Integration routes are **Web** prebuilt UI, **API only** for a merchant-built UI on website/iOS/Android, and **Pay by Link**. The links are navigation; this overview does not specify request fields or webhooks for the child integrations (raw lines 49–67).

## Detail locators

- Partner, store list and 7-Eleven local-entity condition: raw lines 23–30.
- Shopper data, redirect/native voucher, in-store ticket/cash/receipt sequence: raw lines 32–40.
- Default offer-expiry window and Support route: raw line 42.
- JP/JPY flow and capability matrix: raw lines 44–47.
- Web, API-only and Pay by Link routes: raw lines 49–67.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/econtext-konbini/2026-09-15|Japanese convenience stores via econtext overview, captured 2026-09-15]]
