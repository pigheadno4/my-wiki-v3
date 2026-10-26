---
title: "Adyen Pay by Bank (US) Android Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us/android-component"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/android-component/2026-09-15.md"
tags: [adyen, pay-by-bank-us, android, components, ach, redirect]
---

## Overview

Adyen's 2026-09-15 Pay by Bank (US) Android Component guide adds the method to an existing Android Components integration in either Sessions or Advanced flow. It covers method setup, version-dependent Component choices, redirect/outcome ownership, ACH capture risk, recurring-token navigation, TEST scenarios and live Plaid registration. See [[adyen]], [[adyen-android-sdk]], and [[adyen-tokenization]].

## Key takeaways

- Both flow-specific requirements call for an existing Android Components integration with minimum version **5.70.0** and Support-mediated Pay by Bank (US) setup in the Customer Area (raw lines 21-37). This is the page's stated minimum, not an SDK version independently verified here.
- The API-reference tabs distinguish `/sessions` from `/payments`. The `/sessions` table marks `countryCode` required, yet its own description says US is the default if omitted; the `/payments` table marks it optional and likewise says US is the default. Both descriptions limit support to US in this snapshot and say the field determines banks shown by the partner (raw lines 39-57). Treat the Sessions required/default wording as unresolved rather than silently declaring the field optional.
- The page says no additional Pay by Bank (US) Component configuration is needed. It assigns module `paybybank-us` and `PayByBankUSComponent` to v5.8.0 or later, versus module `instant` and `InstantPaymentComponent` for v5.7.1 or earlier. That earlier-version path conflicts with the same page's 5.70.0 minimum, so it is historical/conditional guidance, not evidence that an earlier version meets the current prerequisite. Sessions and Advanced examples show regular and stored-method Component creation; they are SDK snippets, not successful-payment proof (raw lines 59-139).
- Existing Components redirect handling and payment-outcome handling are said to need no extra method-specific work. The page does not define which response or webhook proves final authorization or settlement; do not read this as a bypass of the base integration's result handling (raw lines 141-147).
- Adyen strongly recommends immediate capture because authorization-time Plaid balance/risk checks do not hold bank funds, and asynchronous ACH capture can still encounter insufficient funds even when performed immediately (raw lines 149-155).
- Pay by Bank (US) supports recurring tokenization; the page strongly recommends explicit shopper permission for future payments and routes token creation, subsequent use and management to the general tokenization guide. It gives no method-specific request schema here (raw lines 157-167).
- TEST simulations cover selected approvals, refusals, balances and ACH chargebacks, but not all refusal reasons. The chargeback simulation first returns `Authorised`, then begins after capture and settlement and is reported by `CHARGEBACK` webhook. Live acceptance requires adding the method in the live Customer Area and completed Plaid bank registration; the page says this can take up to one business week after Plaid starts and sends `paymentMethod.created` when acceptance can begin (raw lines 169-224).

## Detail locators

- Sessions and Advanced prerequisites: raw lines 21-37.
- API-reference field wording and Component version branches: raw lines 39-139.
- Redirect/outcome boundaries, capture and recurring: raw lines 141-167.
- TEST payment/chargeback simulations and live gate: raw lines 169-224.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/android-component/2026-09-15|Pay by Bank (US) Android Component guide (2026-09-15 snapshot)]]
