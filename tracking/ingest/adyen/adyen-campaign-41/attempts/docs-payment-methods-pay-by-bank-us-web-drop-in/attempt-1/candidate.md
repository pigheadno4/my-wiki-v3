---
title: "Adyen Pay by Bank (US) Web Drop-in guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/web-drop-in/2026-09-15.md"
tags: [adyen, pay-by-bank-us, web, drop-in, plaid, ach, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds Pay by Bank (US) to an existing Web Drop-in integration, in either Sessions or Advanced server-side flow. It specifies Drop-in 5.70.0 or later, Support-mediated Customer Area setup, country selection, ACH capture risk, tokenization guidance, test scenarios and a Plaid live-registration gate. It does not prove current account eligibility, an executed payment, capture or settlement. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-pay-by-bank-us]].

## Key takeaways

- Both Sessions and Advanced tabs require an existing Web Drop-in integration at minimum version 5.70.0 and Support contact to add Pay by Bank (US) in Customer Area. The v6 import example shows only `AdyenCheckout` with a trailing comma, despite saying to import resources for this method; it does not identify a separate method class. `/sessions` is described as the default since Drop-in v5.0.0. No method-specific Drop-in configuration, redirect-handling step or outcome-handling step is added here because the guide assigns those to the existing Drop-in integration.
- The `/sessions` countryCode row displays a required checkmark but its prose says only US is currently supported and US is the default if countryCode is omitted. The `/payments` row is explicitly optional and recommends including countryCode for possible future non-US-bank expansion. Preserve the `/sessions` marker/prose tension rather than stating unequivocally that omission either succeeds or fails. This snapshot does not prove present geographic or bank eligibility.
- The guide strongly recommends immediate capture to reduce insufficient-funds risk. Plaid account, balance and risk checks occur at authorization, but the issuing bank does not hold authorized funds. It explicitly says insufficient funds remain possible even with immediate capture because ACH Direct Debit capture is asynchronous. Do not equate authorization, an immediate capture request, captured funds and settlement.
- Pay by Bank (US) tokenization for recurring transactions is described as supported; the page strongly recommends asking explicit shopper permission and transparency about schedule and amount to reduce chargeback risk. It links the general Tokenization guide for token creation, use and management rather than specifying request fields here. This recommendation is not itself a field-level consent contract or evidence of a created token.
- The test redirect resembles live but not every refusal reason is simulatable. The guide gives amount/username-based approval and refusal scenarios plus a `custom_balances` option. Its simulated chargeback flow moves directly to Chargeback, while the documented test request first returns `Authorised`; the chargeback starts only after capture and settlement, followed by a `CHARGEBACK` webhook. These test states are not live funds or risk proof.
- For live use, add the method in live Customer Area and wait for Plaid to register the merchant account with participating banks. The guide says registration takes up to one business week after Plaid starts it, shoppers cannot connect during registration, and a `paymentMethod.created` webhook marks when live acceptance can start. Support setup, Customer Area addition and that webhook are distinct from an already completed live payment.

## Detail locators

- Sessions/Advanced Drop-in v5.70.0 prerequisites and Support setup: pinned raw lines 21–37.
- v6 import, `/sessions` default, countryCode required-marker/default tension and optional `/payments` countryCode: pinned raw lines 39–65.
- Drop-in configuration/redirect/outcome delegation: pinned raw lines 67–77.
- Authorization-versus-ACH-capture risk and tokenization recommendation: pinned raw lines 79–97.
- Payment-flow test scenarios and limits: pinned raw lines 99–127; test chargeback sequence: lines 129–148.
- Plaid live-registration gate and `paymentMethod.created` webhook: pinned raw lines 150–154.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[adyen-tokenization]] — recurring token lifecycle; fields belong to linked guide
- [[source-adyen-docs-payment-methods-pay-by-bank-us]] — method overview and ACH return/chargeback context

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/web-drop-in/2026-09-15|Pay by Bank (US) Web Drop-in guide, 2026-09-15]]
