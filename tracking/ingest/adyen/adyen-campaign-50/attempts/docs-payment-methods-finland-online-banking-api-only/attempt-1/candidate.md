---
title: "Online banking Finland API-only integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/api-only"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/api-only/2026-09-15.md"
tags: [adyen, online-banking-finland, paytrail, api-only, redirect, finland]
---

## Overview

This 2026-09-15-captured Adyen add-on explains **Online banking Finland** in an existing Web **API-only Advanced** integration. It covers FI/EUR method discovery, two bank-selection routes, a conditional issuer ID, redirect/details processing, and asynchronous outcome checks. It is a method supplement to [[adyen-online-payments]], not a complete base integration, current issuer-availability guarantee, or evidence that a payment ran. See [[adyen]].

## Key takeaways

- **Prerequisites and bank choice:** The existing API-only integration must handle `action.type: redirect`, and Online banking Finland must be added in Customer Area. The default form shows an Online banking Finland button and uses a **Paytrail payment page for bank selection**. Alternatively, the merchant displays issuer banks, sends the shopper-selected issuer ID to its server and redirects directly to that issuer. The page lists eleven issuer IDs and says the listed issuers are the same in test and live, or can be obtained from `/paymentMethods`; treat this as captured documentation, not current availability (raw lines 19–70).
- **Discovery and request fields:** For `/paymentMethods`, the page specifies `countryCode: FI`, `amount.currency: EUR`, and an amount value, then shows `ebanking_FI` with issuers in an example response. For `/payments`, its method table marks `paymentMethod.type: ebanking_FI` and `shopperEmail` required. `paymentMethod.issuer` has no unconditional required mark but the text says it is **required for the issuer-redirect route**; the default Paytrail-selection sample omits it. The `returnUrl` row is unmarked and gives a 1024-character maximum; redirect return handling remains part of the base flow. The examples use TEST v72, FI/EUR and `fi-FI`, without establishing a general API minimum (raw lines 72–80, 387–455, 457–480, 798–823).
- **Sample/prose limitations:** The “How it works” prose says to include information about purchase items, but the later method-specific `/payments` table and examples do not name or supply an item field. The `/paymentMethods` curl/selected SDK examples include payment-like fields absent from the discovery table and other SDK examples; several snippets use `s.hopper@@example.com`, and the curl samples omit a continuation after `-X POST`. Use the documented field table and base API contract to construct a real request, rather than treating these examples as copy-ready (raw lines 31–36, 74–138, 218–251, 446–480).
- **Redirect and finality:** The sample `/payments` response is `RedirectShopper` with `action.type: redirect`. Send the shopper to the returned `action.url`; after return, submit URL-decoded `redirectResult` in `/payments/details`. The page recommends a system/default browser or platform browser component rather than WebView on mobile. `Pending` or `Received` is nonfinal and calls for an **AUTHORISATION** webhook; if the shopper never returns, use webhooks. The table distinguishes AUTHORISATION success true/false and OFFER_CLOSED success true. Its `Authorised` row says funds arrive in three days; that is a captured provider statement, not a settlement guarantee for a specific payment (raw lines 1148–1225).
- **Testing and method-level boundaries:** The page directs testing with Paytrail sample data before live acceptance and states **testing multiple partial refunds is currently unavailable** (raw lines 1227–1231). The separately captured Online banking Finland overview's matrix marks multiple partial refunds supported (overview pinned raw lines 34–36); support marking and test-environment availability are different claims. Its overview describes an Adyen-hosted bank-selection page, whereas this API-only child calls the default page Paytrail; the host wording should not replace the returned `action.url` or imply a verified host invariant (overview raw lines 23–32; child raw lines 38–50, 1164–1176).

## Detail locators

- Requirements, two bank-selection modes and issuer table: pinned raw lines 23–70.
- FI/EUR discovery request, SDK examples and issuer response: pinned raw lines 72–444.
- Conditional issuer, required type/email, returnUrl and two payment samples: pinned raw lines 446–1146.
- Redirect/details and outcome/webhook tables: pinned raw lines 1148–1225.
- Test-data and multiple-partial-refund test limitation: pinned raw lines 1227–1231.

## Related

- [[adyen-online-payments]]
- [[raw/adyen/docs/payment-methods/finland-online-banking/2026-09-15|Separately captured method overview for provider-level context]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/api-only/2026-09-15|Online banking Finland API-only guide, captured 2026-09-15]]
