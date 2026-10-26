---
title: "Pay by Bank (US) iOS Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/ios-drop-in/2026-09-15.md"
tags: [adyen, pay-by-bank-us, ios, drop-in, ach, capture, tokenization]
---

## Overview

This 2026-09-15 Pay by Bank (US) iOS guide adds the method to an **existing** Drop-in integration for either Sessions or Advanced flow. It covers method setup and country-code guidance, delegates redirect and outcome handling to Drop-in, and flags asynchronous ACH capture risk, recurring-consent advice, TEST scenarios, and a live Plaid registration gate. It is a documentation snapshot, not evidence of merchant enablement or payment success. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Both Sessions and Advanced flows require an existing **iOS Drop-in v5.70.0 or later** integration. Before beginning, contact Adyen Support to add Pay by Bank (US) in Customer Area. See raw lines 21–37.
- The `/sessions` `countryCode` table displays a required mark, yet the same row says **US is the default if omitted** and currently the only supported country. For `/payments`, in an additional-use-case path, `countryCode` is optional but recommended for potential future non-US bank support. It determines which banks Plaid shows. Preserve the table-versus-description tension; future support is not current support. See raw lines 39–57.
- No method-specific Drop-in configuration is required. The existing Drop-in handles the redirect and gets the payment outcome; this page does not specify an extra method-specific redirect or outcome procedure. See raw lines 59–69.
- Adyen **strongly recommends immediate capture**. Plaid performs balance and risk checks at authorization, but the issuing bank does not hold authorized funds. Balance may be insufficient at capture; even immediate capture retains that risk because ACH Direct Debit capture is asynchronous. Authorization is not assured funds or settlement. [[adyen-payment-capture]] See raw lines 71–77.
- Pay by Bank (US) supports tokenization of shopper details for recurring transactions. The page **strongly recommends** explicit shopper permission and transparency about schedule and amount to reduce chargeback risk; it delegates creation, reuse and management details to the general Tokenization guide. [[adyen-tokenization]] See raw lines 79–89.
- TEST redirect mimics live but cannot simulate every refusal. Amount fixtures include USD 3.53 approval and USD 27.53 risk refusal; `custom_balances` lets the tester choose bank-account balances. For simulated ACH chargebacks, `custom_chargeback_rXX` maps to a reason code; the request first reports `Authorised`, then the chargeback flow begins **after capture and settlement**, with a `CHARGEBACK` webhook. These are TEST fixtures, not live outcome guarantees. See raw lines 91–140.
- Live use requires adding the method in live Customer Area **and** waiting for Plaid to register the merchant account with participating banks. The page says this takes up to one business week **from Plaid starting the process**; shoppers cannot connect their bank account during registration and live payments cannot be accepted until completion. A `paymentMethod.created` webhook announces readiness. See raw lines 142–146.

## Detail locators

- Sessions/Advanced iOS version and Support prerequisites: raw lines 21–37.
- `/sessions` versus `/payments` country-code guidance: raw lines 39–57.
- Drop-in configuration, redirect and outcome delegation: raw lines 59–69.
- ACH capture risk and recurring permission: raw lines 71–89.
- TEST payment and chargeback simulation: raw lines 91–140.
- Live Plaid registration and readiness webhook: raw lines 142–146.

## Related

- [[adyen-online-payments]] — main iOS Drop-in integration route.
- [[adyen-payment-capture]] — authorization versus capture outcome boundary.
- [[adyen-tokenization]] — general recurring-token workflow.
- [[source-adyen-docs-payment-methods-pay-by-bank-us]] — method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/ios-drop-in/2026-09-15|Pay by Bank (US) iOS Drop-in, captured 2026-09-15]]
