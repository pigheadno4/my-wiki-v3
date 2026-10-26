---
title: "Adyen Pay by Bank (US) Android Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/android-drop-in/2026-09-15.md"
tags: [adyen, pay-by-bank-us, android, drop-in, ach, redirect]
---

## Overview

Adyen's 2026-09-15 Pay by Bank (US) Android Drop-in guide adds the method to an existing Android Drop-in integration with either Sessions or Advanced server-side flow. It covers method-specific setup, a US `countryCode` API-reference note, base Drop-in redirect/outcome ownership, ACH capture risk, tokenization navigation, TEST scenarios and Plaid live registration. See [[adyen]], [[adyen-android-sdk]], and [[adyen-tokenization]].

## Key takeaways

- Both Sessions and Advanced requirement tabs call for an existing Android Drop-in integration at minimum version **5.70.0** and contacting Adyen Support to add Pay by Bank (US) in the Customer Area (raw lines 21-37). This is the page's stated method prerequisite, not a version independently verified against SDK code.
- The API-reference section separately says `/sessions` is the default with Drop-in v5.0.0 or later; that describes the base Sessions route and does not waive the page's 5.70.0 method prerequisite. Its Sessions link contains `platform=Androidb`, a malformed platform value in this snapshot. The `/sessions` table marks `countryCode` required yet says US is the default if omitted; the `/payments` table marks it optional and also says US defaults if omitted. Both descriptions limit support to US in this snapshot and say the field selects banks shown by the partner. Leave the Sessions required/default tension unresolved (raw lines 39-57).
- No Pay by Bank (US)-specific Drop-in configuration is required. The existing Drop-in integration handles the redirect and obtains the payment outcome, so the page adds no separate method-specific redirect or result procedure. This does not itself define a final authorization, capture or settlement signal (raw lines 59-69).
- Adyen strongly recommends immediate capture: Plaid checks account balance and risk at authorization, but the issuing bank does not hold the funds. Capture is asynchronous on ACH Direct Debit and can still encounter insufficient funds even when initiated immediately (raw lines 71-77).
- The method supports tokenization for recurring transactions. The page strongly recommends explicit shopper permission and routes token creation, subsequent use and management to the general tokenization guide; it supplies no method-specific token request schema (raw lines 79-89).
- TEST can simulate selected approvals, refusals, balances and ACH chargebacks, but not all refusal reasons. A chargeback simulation first produces `Authorised`, then starts after capture and settlement and is reported by `CHARGEBACK` webhook. Live acceptance requires adding the method in the live Customer Area and completed Plaid registration with participating banks; the page says registration can take up to one business week after Plaid starts and sends `paymentMethod.created` when acceptance can begin (raw lines 91-146).

## Detail locators

- Flow prerequisites and Support setup: raw lines 21-37.
- API-reference field wording and malformed Sessions link: raw lines 39-57.
- Method configuration, redirect/outcome boundary, capture and recurring: raw lines 59-89.
- TEST payment/chargeback cases and live registration: raw lines 91-146.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/android-drop-in/2026-09-15|Pay by Bank (US) Android Drop-in guide (2026-09-15 snapshot)]]
