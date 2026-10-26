---
title: "Adyen Pay by Bank (US) API-only integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us/api-only"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/api-only/2026-09-15.md"
tags: [adyen, pay-by-bank-us, api-only, ach, redirect, tokenization]
---

## Overview

Adyen's Pay by Bank (US) API-only guide adds the method to an existing API-only checkout with a merchant-built payment form. This is a 2026-09-15 capture whose metadata says last modified 2019-09-06; it describes an API-only redirect and ACH Direct Debit-backed lifecycle, not evidence of current merchant eligibility or a completed payment. See [[adyen]], [[adyen-online-payments]], and [[adyen-tokenization]].

## Key takeaways

- The merchant needs an existing API-only integration and must contact Adyen Support to add Pay by Bank (US) in the Customer Area. For discovery, request `/paymentMethods` with USD and US; the returned method is named Pay by Bank with type `paybybank_AIS_DD`. The form cannot show an issuing-bank list from this response. When the shopper selects it, obtain authorization to debit the bank account under the ACH rule stated by this guide; its sample authorization text is a recommendation, not a mandatory verbatim script (raw lines 21-44).
- For `/payments`, this page marks `paymentMethod.type` and `returnUrl` required, with a 1024-character maximum for the latter. `countryCode` is optional, defaults to US, and is currently limited to US in this snapshot; the page recommends including it for possible future non-US bank support. The USD/US and Checkout v72 requests are examples of this API-only route, not a general eligibility or SDK guarantee (raw lines 46-75).
- The `/payments` response supplies a redirect `action.url`; send the shopper there. For mobile integrations, the page strongly recommends the device's default browser, and for an HTTP GET redirect shown in an app it recommends SFSafariViewController or Chrome Custom Tabs over WebView. After return, send the URL-decoded `redirectResult` in `/payments/details` and use its `resultCode` to inform the shopper (raw lines 161-220).
- `Pending` or `Received` means the final result is unknown, potentially for minutes or hours. The guide says the final result comes through an `AUTHORISATION` webhook and an unauthorised offer closes after 30 minutes, optionally signalled by `OFFER_CLOSED`; when a shopper does not return, use webhooks for the outcome. `Authorised` is described as payment success with funds arriving in 2–3 days, but authorization is not capture, settlement, or immunity from chargeback. The table also distinguishes `Cancelled`, `Error`, and risk `Refused` (raw lines 218-237).
- Capture promptly is strong advice because Plaid's authorization-time balance/risk checks do not hold bank funds; even immediate ACH capture can fail for insufficient funds because capture is asynchronous (raw lines 239-245).
- Tokenized recurring payments are supported. The guide strongly recommends explicit shopper permission for future charges, then shows initial tokenization parameters with `paybybank_AIS_DD`, token retrieval from the response or `recurring.token.created`, and later token requests with stored-method ID, shopper reference, `ContAuth`, and `Subscription`. The requests are TEST examples, not proof of consent, token creation, or a successful later debit (raw lines 247-501).
- TEST can simulate selected payment and chargeback cases, but not all refusal reasons. A chargeback simulation can return `Authorised` first; the test chargeback begins after capture and settlement and is later reported by `CHARGEBACK` webhook. Live acceptance requires adding the method in the live Customer Area and completed Plaid registration with participating banks; the guide says registration can take up to one business week after Plaid starts and sends `paymentMethod.created` when live acceptance can begin (raw lines 503-558).

## Detail locators

- API-only and Customer Area prerequisites, USD/US discovery, ACH debit authorization: raw lines 21-44.
- Required payment fields, redirect response, return and details handling: raw lines 46-220.
- Result codes, webhook outcomes, capture risk: raw lines 218-245.
- Recurring token creation and later-payment examples: raw lines 247-501.
- TEST simulations, live Plaid registration and readiness webhook: raw lines 503-558.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/api-only/2026-09-15|Pay by Bank (US) API-only guide (2026-09-15 snapshot)]]
