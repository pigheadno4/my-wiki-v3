---
title: "Zip Android Drop-in earlier versions | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/zip/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, zip, android, drop-in, redirect, recurring]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] page is titled **Zip Drop-in v4.x.x integration** and describes an existing Android Drop-in integration that presents Zip, redirects the shopper to Zip's website, and returns for result handling. It includes payment-data, webhook and recurring-token sections. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-zip|the Zip overview]] for broader method context. The page's title and its later-version Sessions tab must be kept distinct.

## Key takeaways

- The requirement row names an **Advanced flow Android Drop-in** integration and says to add Zip in Customer Area (raw lines 26–31). To discover Zip, the page gives `/paymentMethods` **AU/AUD** and an amount value (lines 33–41). It calls for shopper details for Zip risk checks and purchased-item data (lines 21–24). These captured values do not prove current availability or a merchant's enablement.
- The page says Drop-in returns `paymentComponentData.paymentMethod`; pass it to the server, and send a `returnUrl` obtained through `RedirectComponent.getReturnUrl(context)` for possible redirection (lines 43–54). It then presents **two endpoint tabs**: `/sessions`, described as the default with Drop-in **v5.0.0 or later**, and `/payments` for an additional use case (lines 56–68, 705–719). The `/sessions` inclusion sits inside a page explicitly titled **v4.x.x**, so do not infer that the v5 default applies to v4. Both tables have blank **Required** cells for the shopper fields and `lineItems`; the page's preceding prose nevertheless says to supply shopper details and item information. The `/payments` table adds `paymentMethod.clickAndCollect: true` if the shopper picks up the order; `lineItems.imageURL` is optional with a 500-character maximum (lines 60–68, 707–719).
- The `/payments` response example has `RedirectShopper` and a redirect `action`; the page says pass that action from server to client (lines 1399–1415). After Zip returns the shopper to the app, Drop-in supplies `actionComponentData.details` for server-side `/payments/details` (lines 1417–1450). The example `Authorised` result is illustrative, not a promise of any transaction's outcome.
- Result codes include `Authorised`, `Cancelled`, `Error`, `Pending`/`Received` and `Refused`. **Pending/Received is not a final result**: wait for an `AUTHORISATION` webhook. If the shopper never returns, use webhooks; the page lists `AUTHORISATION` true/false and `OFFER_CLOSED` true for an incomplete/timed-out offer (lines 1452–1472).
- The page describes Zip recurring transactions: create a token with `storePaymentMethod: true` and `shopperReference` on `/payments`; **after settlement**, a `recurring.token.created` webhook provides `storedPaymentMethodId` (lines 1474–1495). A later `/payments` request uses that ID, matching `shopperReference`, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile` (lines 1497–1507). This is a documented flow, not proof of token creation, merchant eligibility or successful subsequent charges.
- TEST instructions point to Zip test credentials/accounts and payment-status checks in test Customer Area. Before live acceptance, submit a Zip request in live Customer Area (lines 1707–1713). The `/payments` curl example includes literal `{hint:...}` markup inside JSON (around lines 735–737), so it is illustrative rather than copy-ready.

## Detail locators

- v4.x.x title, redirect, risk/item data and Advanced prerequisite: raw lines 15–31.
- AU/AUD discovery and Drop-in-to-server handoff: lines 33–54.
- `/sessions` v5-default note, fields and v71 TEST examples: lines 56–704.
- `/payments` additional-use-case fields, click-and-collect and v72 TEST examples: lines 705–1398; literal hint markup in curl at lines 735–737.
- Redirect action, return and `/payments/details`: lines 1399–1450.
- Result codes and terminal webhook routing: lines 1452–1472.
- Settlement-gated recurring token and later payment fields: lines 1474–1507; sample requests: 1509–1705.
- TEST and live request routes: lines 1707–1713.

## Related

- [[adyen-online-payments]] — provider online-payment integration concept.
- [[source-adyen-docs-payment-methods-zip]] — Zip method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/android-drop-in/earlier-versions/2026-09-15|2026-09-15 Zip Android Drop-in earlier-versions guide]]
