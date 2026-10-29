---
title: "Online banking Czech Republic API-only"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/api-only"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/api-only/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, api-only, redirect, payments]
---

## Overview

This 2026-09-15 guide adds Online banking Czech Republic to an existing Adyen Web API-only integration. The merchant-built form presents issuing banks; the shopper selects one, is redirected for payment, and returns for a /payments/details result. A webhook can supply the result if the shopper does not return. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for CZ/CZK method context.

## Key takeaways

- Prerequisites are an existing API-only integration, redirect action handling, and Customer Area setup. The guide says to show available banks and pass the selected Issuer ID to the server. Its captured table lists cs, kb, mp, pf, pg, and rf, and it also directs readers to the /paymentMethods response for issuers. Use the selected bank's returned issuer rather than treating the static list as universal/current. See raw lines 23–53.
- Discovery specifies countryCode CZ, amount.currency CZK, and the payment amount. The example /paymentMethods response contains onlineBanking_CZ and six issuer IDs. These are discovery conditions, not current account entitlement or proof that every bank is offered to a particular shopper. See raw lines 55–63 and 337–378.
- The /payments prose says no additional parameters are needed, yet the earlier form step says the selected Issuer is needed and payment samples send paymentMethod.type onlineBanking_CZ with issuer cs. The samples use EUR even though discovery and the method overview specify CZK. Preserve these tensions; do not infer EUR support or a copy-ready CZ payment request. See raw lines 41–53, 55–63, and 380–705.
- The /payments response has a redirect action. Send the shopper to action.url; on return, send URL-decoded redirectResult in /payments/details, then use resultCode and pspReference. For mobile, the page recommends the device default browser; for HTTP GET inside an app, it recommends SFSafariViewController or Chrome Custom Tabs instead of WebView. These are scoped recommendations. See raw lines 707–763.
- Pending or Received means final status is unknown; confirmation may take minutes or hours and final result comes in an AUTHORISATION webhook. The page says an offer closes if not authorised within 30 minutes, with optional OFFER_CLOSED webhook. If the shopper fails to return, AUTHORISATION success false indicates failure and success true completion. Authorised, Cancelled, Error and Refused have separate result actions. Do not treat Pending/Received or redirect return as final success. See raw lines 764–783.
- The test section says to use real payment details and small amounts, check test payments in Customer Area, and add the method there for live acceptance. This is captured guidance, not evidence of actual testing or live payment. See raw lines 785–791.

> [!warning] Request example and issuer tension
> The guide says pass selected issuer to the server (line 42), then says no additional /payments parameters (line 382), while examples include issuer cs and onlineBanking_CZ (for example lines 400–403). It does not reconcile these statements. Payment examples use EUR (line 396 and repeats) although discovery uses CZK (line 62) and the linked overview labels CZ/CZK. Verify actual selected-bank discovery and currency; do not treat samples as guarantees.

## Detail locators

- API-only prerequisite and bank issuer selection: raw lines 23–53.
- CZ/CZK discovery and method list: raw lines 55–378.
- Payment examples and caveat: raw lines 380–705.
- Redirect, details, result and webhook: raw lines 707–783.
- Test/live setup: raw lines 785–791.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/api-only/2026-09-15|Online banking Czech Republic API-only, captured 2026-09-15]]
