---
title: "Trustly Android Drop-in v4.x.x integration | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/trustly/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, trustly, android, drop-in, advanced-flow, earlier-versions]
---

## Overview

This Adyen earlier-versions guide is scoped by its title to Trustly Android Drop-in v4.x.x. It adds Trustly to an existing Advanced-flow Android Drop-in integration: the merchant enables Trustly in Customer Area, discovers it with a supported country/currency and amount, sends Drop-in's selected payment method to its server, and redirects the shopper to Trustly's app or website for completion. The page's introductory Android Drop-in link and See also link point to Sessions-flow guides, while its explicit requirement and payment-action link specify Advanced flow; use the Advanced requirement for this described procedure rather than treating those navigation links as proof of Sessions support (raw lines 15–38, 364, 431–435).

## Key takeaways

- `/paymentMethods` uses `countryCode` and `amount.currency` to show available methods. The guide says any *supported* country and currency, with SE/SEK only as examples; the merchant also supplies amount in minor units (raw lines 28–38).
- For the Advanced flow, the client passes `paymentComponentData.paymentMethod` to the server. The server POSTs `/payments` with that method and a `returnUrl` from `RedirectComponent.getReturnUrl(context)`; the response `action` directs the client redirect. Example values such as `adyencheckout://your.package.name`, checkout-test API v68 and the language-library versions are illustrative, not universal requirements (raw lines 38–45, 47–346, 348–364).
- On return to the app, Drop-in supplies `actionComponentData.details` for a server POST to `/payments/details`. The response `resultCode` is for shopper presentation and `pspReference` identifies the transaction; the shown `Authorised` response is an example, not a verified payment (raw lines 366–403).
- The result table distinguishes `Authorised`, `Cancelled`, `Error`, `Pending`/`Received`, and `Refused`. For `Pending` or `Received`, the final result is unknown and the guide says to wait for an `AUTHORISATION` webhook. If the shopper does not return, webhooks determine the outcome: `AUTHORISATION` success false/true indicates failure/success, and `OFFER_CLOSED` success true means the shopper did not complete the payment. The table's statement about funds arriving in three days is a source claim for `Authorised`, not proof of settlement for a specific transaction (raw lines 401–421).
- The source points to a Trustly test environment and test login-number format, and says a request for Trustly in live Customer Area precedes live acceptance (raw lines 423–429).

## Detail locators

- v4.x.x title, Advanced-flow setup and Sessions-link tension: raw lines 15–26, 364, 431–435.
- Discovery and server payment/return URL handoff: raw lines 28–45.
- Versioned payment examples and redirect action: raw lines 47–364.
- Return, `/payments/details`, intermediate statuses and webhook outcomes: raw lines 366–421.
- Test guidance and live Customer Area request: raw lines 423–429.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/android-drop-in/earlier-versions/2026-09-15|Trustly Android Drop-in v4.x.x, fetched 2026-09-15]]
