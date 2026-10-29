---
title: "Adyen Klarna Debit Risk API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/api-only"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/api-only/2026-09-15.md"
tags: [adyen, klarna-debit-risk, api-only, redirect, sepa-direct-debit, recurring]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Klarna Debit Risk to an existing API-only integration. It describes method discovery, a merchant-built payment form, `/payments` redirect and return handling, result presentation, and a recurring-token path through SEPA Direct Debit. It is a method-specific add-on, not a complete base API integration or evidence of merchant enablement or successful payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Prerequisites are an existing API-only integration with redirect handling for `action.type: redirect` and Klarna Debit Risk added in Customer Area. The merchant-built form needs no additional Debit Risk fields, but must pass the shopper's correct country code. The `/paymentMethods` table lists AT, BE, DE, NL, ES and **CH**, with EUR and **CHF**; it does not map each country to a currency or prove method availability for a particular account. The guide does not resolve the relationship between its coverage table and the separate method overview.
- The ordinary `/payments` table requires `paymentMethod.type: directEbanking`, `returnUrl` and `countryCode`; `shopperLocale`, email and telephone are optional in this table. The 10 EUR German example uses `DE` and `de-DE`. The page says no extra form details are required, yet the server request still needs these method identifiers and return data. Its curl example has `-X POST` on one line without a continuation before `-d`; treat this as illustrative rather than a copy-ready shell command.
- Redirect the shopper to the `action.url` from `/payments`. For mobile, the guide recommends a device browser rather than an embedded WebView and mentions SFSafariViewController/Chrome Custom Tabs for GET. On return, send the URL-decoded `redirectResult` in `/payments/details`, then use its `resultCode` and `pspReference`. `Pending`/`Received` are intermediate and require the later `AUTHORISATION` webhook. If the shopper never returns, use webhook outcome. `Authorised` and `AUTHORISATION: true` indicate shopper completion/bank processing, **not guaranteed funds**: the linked Debit Risk overview warns that non-settlement can still become an undefendable chargeback.
- Recurring payments use **SEPA Direct Debit** after a Debit Risk payment creates a shopper token. The guide strongly recommends explicit permission and clear amount/schedule disclosure to reduce chargebacks. The initial token request table calls for `directEbanking`, return URL, country code, recurring model, shopper interaction, non-PII shopper reference and `storePaymentMethod: true`; the `recurring.token.created` webhook gives `storedPaymentMethodId`. Later token payments are only for shopper-absent `Subscription` or `UnscheduledCardOnFile`, using `sepadirectdebit`, token ID and `ContAuth`. The initial-token table marks `countryCode` required so the shopper can proceed, but its adjacent curl and other initial-token examples omit it. The table describes initial online `shopperInteraction` as `Ecommerce`, but those examples say `ContAuth`; some also serialize `storePaymentMethod` as a string rather than a boolean. The page does not resolve these example conflicts or say whether the API rejects the samples.
- The guide calls for test-environment checks and enabling Debit Risk on the live merchant account before accepting live payments. Neither sample responses nor this checklist establish a completed or settled live transaction.

> [!warning] Contradiction
> This API-only page's `/paymentMethods` table includes CH and CHF, while the [[source-adyen-docs-payment-methods-klarna-debit-risk|Klarna Debit Risk overview]] lists only AT/BE/DE/NL/ES in EUR. These dated snapshots do not establish which coverage applies to a merchant or which country/currency pairs are supported.

## Detail locators

- Requirements, form, method-discovery country/currency table: pinned raw lines 23–53; `/paymentMethods` examples: lines 55–340. Compare with overview raw lines 30–42 for the CH/CHF discrepancy.
- `/payments` parameter table and German example: lines 342–380; code examples: lines 383–703.
- Redirect, `/payments/details`, result codes and webhook fallback: lines 705–764.
- SEPA recurring, initial-token table and examples, token-created webhook, shopper-absent use and future-payment examples: lines 766–1763. Initial-token `countryCode` is table-required at line 787 but omitted by examples at lines 802–1143. Test/live checklist: lines 1765–1771.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-klarna-debit-risk]] — overview with narrower EUR coverage and non-settlement warning

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/api-only/2026-09-15|Klarna Debit Risk API-only guide, captured 2026-09-15]]
