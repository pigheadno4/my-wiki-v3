---
title: "Hosted Checkout | Adyen Standard online payments"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/hosted-checkout"
raw_files:
  - "adyen/docs/standard/integration/hosted-checkout/2026-09-15.md"
tags: [adyen, standard-integration, online-payments, hosted-checkout, sessions]
---

## Overview

This 2026-09-15 [[adyen]] **Standard online-payments** guide explains an Adyen-hosted shopper payment page. The merchant payment server creates a Checkout API session, the website or app redirects the shopper to its returned URL, the merchant server retrieves a session result after return, and a separate webhook server receives the payment outcome. It is a bounded [[adyen-online-payments]] Standard integration route, not evidence of a deployed checkout, authorization, capture or settlement. [Raw: lines 15–19, 35–79]

## Key takeaways

- The guide's setup table calls for Customer Area merchant-admin and API-credential management roles, an API credential/key, default payment credential roles, a Standard webhook and test/live preparation. For session creation it specifies Checkout API **v72 or later** and a server-side library released **March 30, 2026 or later**. The server creates the session; the browser is redirected to the Adyen-hosted page. These are this guide's gates, not a blanket claim about older integrations. [Raw: lines 21–54]
- Creating the theme in Customer Area requires merchant-admin or Hosted Checkout and Pay by Link Settings role. The documented `POST /sessions` table marks amount, merchant account, return URL, payment reference, country code, shopper email, shopper reference, `mode: hosted`, and theme ID as required. Yet the `shopperEmail` description calls it “strongly recommended”; preserve that internal wording difference instead of treating the field's runtime validation as proven. The return URL has a 1,024-character limit, protocol and encoding conditions, and **must not contain PII**; shopper reference likewise excludes PII. [Raw: lines 287–328]
- The session response supplies `url` and `expiresAt`; the page says the default Hosted Checkout expiry is **one hour**, and it may also end after too many attempts. On mobile browsers the guide directs iOS SFSafariViewController or Android Chrome Custom Tabs instead of WebViews because some methods fail in WebViews. A redirect returns `sessionId` and `sessionResult`, which the merchant server sends to `GET /sessions/{id}?sessionResult=...` to show the **current session result**. [Raw: lines 614–665, 946–951]
- Session-result statuses include `completed`, `paymentPending` for asynchronous methods and `expired`. The response's `status` does **not change**; do not poll that same result for later payment changes. The guide says to use Standard webhooks or Customer Area Transactions for updates and to update the order system from the `AUTHORISATION` webhook, matching `merchantReference`; `success: true` and `false` have different outcomes. A completed session or example `Authorised` result is not capture, settlement or fulfillment proof. Example request, session response and webhook amounts/IDs differ and are illustrative, not one coherent transaction trace. [Raw: lines 330–353, 614–634, 811–921]
- Live setup is separate from test: apply/configure a live account, request live payment methods and use live endpoints; keep all API calls for one payment session in the **same live endpoint region** to avoid errors. Failed attempts can return a shopper to Hosted Checkout, and multiple payment-attempt webhooks can share a `sessionId`. The supported-method list is a dated guide list, not proof a particular merchant has any method enabled. [Raw: lines 924–1021]

## Detail locators

- Product identity, roles and Checkout API/library gates: raw lines 15–54.
- Server, redirect, session-result and webhook flow: raw lines 56–103.
- Language-specific library setup and example request versions: raw lines 105–285, 330–612.
- Theme role, session fields and PII limits: raw lines 287–328.
- Session URL/expiry, mobile-browser container and return query: raw lines 614–665, 946–951.
- Immutable result statuses, AUTHORISATION webhook and order matching: raw lines 811–921.
- TEST/LIVE split, same-region gate, retries and supported-method catalog: raw lines 924–1027.

## Related

- [[adyen-online-payments]] — main Standard checkout concept
- [[source-adyen-docs-standard]] — bounded Standard integration checklist
- [[source-adyen-docs-standard-integration-drop-in]] — alternative Standard Drop-in UI path
- [[source-adyen-docs-online-payments-out-of-app-payments-on-ios]] — separate iOS out-of-app route

## Raw Sources

- [[raw/adyen/docs/standard/integration/hosted-checkout/2026-09-15|Pinned Standard Hosted Checkout guide]]
