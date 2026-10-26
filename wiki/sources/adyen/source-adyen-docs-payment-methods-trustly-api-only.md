---
title: "Adyen Trustly API-only guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/api-only"
raw_files:
  - "adyen/docs/payment-methods/trustly/api-only/2026-09-15.md"
tags: [adyen, trustly, api-only, online-banking, redirect, webhooks, chargebacks]
---

## Overview

This Adyen Trustly API-only guide was last modified 2023-05-26 and captured 2026-09-15. It describes a merchant-built payment form, Trustly discovery, server-side `/payments`, shopper redirect, `/payments/details`, result display, webhooks, and TEST/LIVE setup. Its `RedirectShopper` example is an intermediate action, not final authorization or received funds. The captured guide does not establish current merchant/bank eligibility or a successful payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-trustly]].

## Key takeaways

- **Prerequisites and discovery:** the page requires an existing API-only integration and Trustly added in the **test** Customer Area. If using `/paymentMethods` for discovery, it instructs a supported country/region and currency, minor-unit amount and channel `Web`, `iOS` or `Android`; **SE/SEK are examples**, not an exhaustive eligibility list. Discovery returns `paymentMethod.type: trustly`. (raw lines 21–41)
- **Payment and redirect:** the merchant server sends `/payments` with `paymentMethod.type: trustly`. The guide includes shopper `countryCode` to preselect the country on Trustly's hosted page; it says to include this for a better shopper experience and notes ISO alpha-2 with **QZ** as its Kosovo exception. Its sample uses SE/SEK, a return URL and TEST environment. The `/payments` example returns `RedirectShopper` and `action.type: redirect`; redirect the shopper to `action.url`. For mobile, the page strongly recommends the device default browser and, for HTTP GET shown in-app, SFSafariViewController or Chrome Custom Tabs rather than WebView objects. These are recommendations, not mandatory API fields. (raw lines 43–70, 361–385)
- **Return and result:** after shopper return to the website, the merchant POSTs `/payments/details` with `details.redirectResult` URL-decoded from the return. The response's `resultCode` is for shopper display and `pspReference` identifies the transaction. The table covers Authorised, Cancelled, Error, Pending/Received and Refused. For Pending/Received, final result is not yet known and the guide says wait for an `AUTHORISATION` webhook; if the shopper fails to return, it says wait for webhooks, including `AUTHORISATION` true/false or `OFFER_CLOSED` true for timeout. The Authorised sample and shopper display do not alone prove funds were received. (raw lines 387–438)
- **Material settlement conflict:** this page's Authorised row says the payment was successful and “You will receive the funds in 3 days” (raw line 426). The related Trustly overview says a successful `AUTHORISATION` only confirms issuer/Trustly verification and bank-transfer initiation; funds may never arrive, with an 8-calendar-day chargeback path and undefendable Trustly chargebacks (related overview raw lines 38–53). Treat the API-only row as an optimistic presentation statement, **not a funding guarantee**. Preserve the overview's authorized-but-unfunded risk when deciding fulfillment or settlement.
- **TEST/LIVE:** the guide points to a Trustly test environment, permits any digits matching `YYMMDD-XXXX` for its Login ID/Personal number test value, and directs TEST payment checks to Customer Area. LIVE acceptance requires a Trustly request in the **live** Customer Area. Test examples and a live request instruction are not evidence of account activation or executed payments. (raw lines 440–446)

## Detail locators

- Historical timestamp, API-only prerequisite and discovery scope: pinned raw lines 5–41.
- Server-side Trustly request and SE/SEK TEST examples: pinned raw lines 43–359.
- `RedirectShopper` action and browser recommendations: pinned raw lines 361–385.
- URL-decoded return, `/payments/details`, result codes and webhooks: pinned raw lines 387–438.
- TEST/LIVE guidance: pinned raw lines 440–446.
- Related overview's authorization-versus-funds and chargeback warning: [[source-adyen-docs-payment-methods-trustly]], raw lines 38–53; this guide's three-day statement: pinned raw line 426.

## Related

- [[adyen-online-payments]] — main provider payment and webhook context
- [[source-adyen-docs-payment-methods-trustly]] — bank-transfer and chargeback qualification
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/api-only/2026-09-15|Trustly API-only guide, 2023-modified and 2026-09-15-captured]]
