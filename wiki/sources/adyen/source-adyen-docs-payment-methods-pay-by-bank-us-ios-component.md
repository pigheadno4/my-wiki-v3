---
title: "Adyen Pay by Bank (US) iOS Redirect Component guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us/ios-component"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/ios-component/2026-09-15.md"
tags: [adyen, pay-by-bank-us, ios, components, plaid, ach, capture, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds Pay by Bank (US) to an existing iOS Components integration in Sessions or Advanced server-side flow. It covers Component selection (including stored methods), bank redirect/outcome delegation to the base integration, ACH capture risk, recurring-token navigation, testing, and Plaid live registration. It is a provider snapshot, not proof of current merchant or bank eligibility, completed registration, captured funds, or a successful payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Flow/version and country:** both Sessions and Advanced require an existing iOS Components integration at **version 5.70.0 or later** and Pay by Bank (US) added in Customer Area. The API section calls `/sessions` the default for base Components v5.0.0+, but that statement does not lower this method's 5.70.0 minimum. The Sessions `countryCode` table marks the field required yet says only **US** is currently supported and US is the default if omitted; preserve this table/prose tension rather than asserting omission is valid. The `/payments` row for an additional use case marks `countryCode` optional and recommends it for future non-US bank support, while still saying US is the current supported/default value. (raw lines 21–57)
- **Component and redirect:** for a regular method, the Swift samples check for `PayByBankUSPaymentMethod` and present `PayByBankUSComponent`; for a stored method, they check for `StoredPayByBankUSPaymentMethod` and present `StoredPaymentMethodComponent`. Sessions delegates to `session`; the `/payments` example delegates to `self`. The page says the existing Components integration handles redirect and payment outcome, with no Pay by Bank (US)-specific extra handling here. A Component presentation or bank return does not establish authorization or settlement. (raw lines 59–130)
- **Capture and recurrence:** Adyen strongly recommends immediate capture because Plaid's authorization-time balance/risk checks do **not** hold the shopper's funds. It explicitly says insufficient funds remain possible even with immediate capture because ACH Direct Debit capture is asynchronous. It supports tokenization for recurring transactions, strongly recommends explicit shopper permission and disclosure of schedule/amount, and links to general token creation, reuse and management instructions rather than giving a complete token request here. (raw lines 132–150)
- **TEST paths:** the test redirect mimics LIVE but not all refusal reasons can be simulated. The page gives amount/username scenarios, including `custom_balances`; in the chargeback simulation, `custom_chargeback_rXX` uses an ACH return reason code. The simulated request can be `Authorised` before capture/settlement and then produce a `CHARGEBACK` webhook. Thus a test `Authorised` result is not a guarantee against later ACH return. (raw lines 152–201)
- **LIVE gate:** adding the method in the live Customer Area starts Plaid registration with participating banks. The page says registration takes up to one business week **from when Plaid starts**; shoppers cannot connect during that period and live acceptance must wait until completion. A `paymentMethod.created` webhook signals when live acceptance can start. Merely submitting or adding the request is not completed registration. (raw lines 203–207)

## Detail locators

- Sessions/Advanced iOS Components minimum and countryCode table/prose tension: pinned raw lines 21–57.
- Regular/stored Component examples and delegate differences: pinned raw lines 59–122; redirect/outcome scope: lines 124–130.
- Authorization-time checks versus asynchronous ACH capture risk and recurring consent: pinned raw lines 132–150.
- Payment/chargeback test scenarios and Authorised-to-CHARGEBACK sequence: pinned raw lines 152–201.
- Plaid live registration delay and `paymentMethod.created` gate: pinned raw lines 203–207.

## Related

- [[adyen-online-payments]] — main provider Components/payment context
- [[adyen-tokenization]] — provider recurring-token lifecycle
- [[source-adyen-docs-payment-methods-pay-by-bank-us]] — method and ACH risk overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/ios-component/2026-09-15|Pay by Bank (US) iOS Component guide, 2026-09-15]]
