---
title: "Online banking Thailand for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/api-only"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/api-only/2026-09-15.md"
tags: [adyen, online-banking, thailand, api-only, redirect]
---

## Overview

This 2026-09-15 guide adds Thailand online banking to an existing Adyen Web API-only Advanced-flow integration. It covers bank/issuer selection, TH/THB method discovery, a redirect payment request, return handling through `/payments/details`, and webhook-qualified outcomes. It is a method supplement, not a standalone integration. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The merchant needs an existing API-only integration that handles `action.type: redirect`, and must add Online banking Thailand in Customer Area. The merchant-built form shows available banks, then sends the selected bank's issuer ID to the server. The page lists five issuer IDs and says the `/paymentMethods` response can supply the issuer list. See raw lines 23–56.
- Method discovery requests specify `countryCode: TH` and `amount.currency: THB`; the example `/paymentMethods` result has type `molpay_ebanking_TH` and an `issuers` array. The v72 TEST endpoint and language-library versions are examples, not stated minimums. See raw lines 58–85 and 343–378.
- The `/payments` table names `paymentMethod.type: molpay_ebanking_TH`, `paymentMethod.issuer` for the selected bank, and `returnUrl` required only for issuer redirect, not QR-code flow. The shown request includes all three and returns `RedirectShopper` with a `redirect` action. The page demonstrates issuer redirect; it does not describe a full QR-code flow. See raw lines 380–415 and 715–729.
- After redirecting to `action.url`, the merchant posts the URL-decoded `redirectResult` to `/payments/details`. Its `resultCode` can be Authorised, Cancelled, Error, Pending/Received or Refused. For Pending/Received, final network confirmation may take minutes or hours and the final result arrives in an AUTHORISATION webhook; if the shopper does not return, wait for webhooks. A redirect or return alone is not final authorization. See raw lines 731–791.
- The How it works text calls for item information, yet the `/payments` section says no parameters are needed before listing method fields; its examples contain no item fields. The PHP payment sample uses `setType("TH")` where the parameter table and JSON/Node/Go examples use `molpay_ebanking_TH`. Treat these as unresolved prose/example conflicts, not as alternative proven request schemas. See raw lines 31–35, 380–390, 402–415, 477–480 and 562–565.
- Test guidance uses available issuer IDs and Customer Area Payment list; a separate request in live Customer Area is required before live acceptance. The test paragraph calls it an Online banking Thailand Component despite this API-only title, so do not infer Component requirements from that wording. See raw lines 793–799.

## Detail locators

- Prerequisites, five-bank form and TH/THB discovery: raw lines 23–65.
- Method discovery examples and response: raw lines 67–378.
- `/payments` request/response and sample inconsistency: raw lines 380–729.
- Return, result-code, asynchronous webhook and live-request instructions: raw lines 731–799.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/api-only/2026-09-15|Online banking Thailand for API only (2026-09-15)]]
