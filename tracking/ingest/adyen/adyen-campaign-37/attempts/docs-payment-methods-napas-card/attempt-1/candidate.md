---
title: "Adyen Napas card Vietnam overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card"
raw_files:
  - "adyen/docs/payment-methods/napas-card/2026-09-15.md"
tags: [adyen, napas, vietnam, cards, redirect, online-payments]
---

## Overview

This Adyen page, last modified 2023-02-20 and captured 2026-09-15, introduces **Vietnamese Napas-network ATM card payments offered through partner MoMo**. It describes the shopper redirect/authentication journey, a historical VN/VND capability row and routes to channel guides. It is not a merchant setup procedure, a card-data-handling specification or proof of payment authorization. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Provider and shopper journey:** Adyen identifies **MoMo as its partner** for ATM card payments through the local Napas network. After a shopper chooses Napas card on a website or mobile app, the page describes a local-bank list, bank selection, redirect to the Napas Payment Gateway, entry of the Napas ATM card number and PIN **on that gateway page**, OTP authentication using an email/SMS code, and redirect back to the merchant site/app. These are shopper/provider steps; the page does not instruct the merchant to collect the card number, PIN or OTP and does not say a return redirect proves a successful payment. (raw lines 17–29)
- **Historical capability row:** The table labels the payment type “Credit and debit cards,” flow **Redirect**, country **VN** and currency **VND**. Its positive refund mark includes **“See note,” but no explanatory note is present in this captured page**. It marks recurring, partial/multiple partial refunds, separate/partial/multiple partial captures and chargebacks with x. Treat these as historical matrix markers, not a definitive current merchant refund entitlement, a completed refund or settlement. The ATM-card prose and broader table category are both retained without equating Napas to every credit card. (raw lines 19, 31–33)
- **Integration navigation:** The chooser links Web, iOS, Android, API-only custom UI for website/iOS/Android, and Pay by Link. These links do not establish child-page API/SDK versions, merchant eligibility, details/webhook handling, safe collection of payment credentials, or a completed transaction. (raw lines 35–65)

## Detail locators

- Partner MoMo, ATM card scope and shopper bank/gateway/PIN/OTP/return sequence: raw lines 17–29.
- VN/VND Redirect row and unresolved refund “See note” qualification: raw lines 31–33.
- Web, iOS, Android, API-only and Pay by Link routes: raw lines 35–65.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/2026-09-15|Adyen Napas card overview, 2026-09-15 snapshot]]
