---
title: "Adyen Docs: MOTO payments through Checkout API and Web Drop-in"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/mail-order-telephone-order/api-request"
raw_files:
  - "adyen/docs/unified-commerce/mail-order-telephone-order/api-request/2026-09-15.md"
tags: [adyen, unified-commerce, moto, checkout-api, web-drop-in, webhooks]
---

## Overview

This Adyen Mail Order/Telephone Order (MOTO) guide describes a shopper contacting a merchant, a merchant user such as a call-center agent entering that shopper's card details into Web Drop-in in the merchant's UI, and the merchant server creating a Checkout API session. The payment result is delivered asynchronously through an `AUTHORISATION` webhook. This is a staff-operated MOTO card flow, not an ordinary shopper-operated ecommerce checkout, terminal MOTO flow, recurring mandate, or seller/payee and funds-flow specification. The captured page does not prove account eligibility, PCI compliance, or a successful live payment. [[adyen]] [[adyen-unified-commerce]] [[adyen-online-payments]]

## Key takeaways

- Before building, the guide says to get an API key, grant **Merchant PAL webservice role**, **Checkout webservice role**, and **Checkout encrypted cardholder data**, and subscribe to the Standard webhook. These are listed credentials/roles for this guide, not proof that a particular credential or merchant account has them. The server-side `/sessions` example uses the API key in a request header; the front-end example uses a separate public client key. See **Requirements** and **Create your instance of AdyenCheckout**, pinned raw lines 23–31 and 219–245.
- The agent enters amount and required order details in the merchant UI, which sends them to the server. The server calls Checkout `/sessions`; the UI creates Web Drop-in from returned `session.id` and `sessionData`; the agent enters the shopper's payment details into the Drop-in card form. The webhook server receives the outcome. This is a staff/card-data handling path, not proof that a raw PAN is stored by the merchant server. See **How it works**, pinned raw lines 33–45, and **Prepare your front end / Create Drop-in**, lines 112–290.
- The `/sessions` guide requires amount in currency minor units, a MOTO shopper interaction, `allowedPaymentMethods: scheme`, merchant account, unique payment reference (at least three characters), and a protocol-bearing `returnUrl` for possible redirection. Its parameter table says `shopperInteraction` should be **Moto**, but its example JSON sends **MOTO**. Treat this as an unresolved case discrepancy in the snapshot; neither form here establishes current API-schema behavior. The example targets test Checkout v71 and includes an `idempotency-key` header, which does not by itself prove retry safety. See **Create a session**, pinned raw lines 49–110.
- The front-end guide loads Adyen Web by npm or script/CSS; the script route instructs using Subresource Integrity hashes per version. It recommends avoiding an iframe and avoiding re-rendering the Drop-in container. The Card component is configured with `hideCVC: false`; this specific configuration does not prove the full merchant PCI scope or SCA treatment. See **Prepare your front end / Create Drop-in**, pinned raw lines 112–290.
- `onPaymentCompleted`, `onPaymentFailed` and `onError` handle UI events, but the guide explicitly says to wait for the asynchronous `AUTHORISATION` webhook after submission. Match `merchantReference` to the order; `success: true` denotes a successful payment outcome in this guide, while `success: false` carries a failure reason. An HTTP 201 session response or visible Drop-in event is not the final outcome. See **Get the outcome**, pinned raw lines 292–365, and event-handler table, lines 196–215.
- Before live operation, the guide points to test cards, then live-account setup, obtaining and submitting a **SAQ C-VT** form, switching to live endpoints, and matching Drop-in's live `environment` to the endpoint region. Those are described steps, not proof that a merchant is PCI compliant, approved for MOTO, exempt from SCA, or enabled in a specific region. The guide does not describe recurring charges, capture/settlement, merchant-of-record assignment, or funds distribution. See **Test and go live**, pinned raw lines 367–393.

## Detail locators

- **MOTO payments through API / Requirements** (pinned raw lines 15–31) — staff-entered Drop-in scope, API key, roles and Standard webhook.
- **How it works** (pinned raw lines 33–45) — shopper call, agent UI, server session, Drop-in and webhook flow.
- **Create a session** (pinned raw lines 49–110) — request fields, table/example case conflict, test v71 sample, session response and error route.
- **Prepare your front end** (pinned raw lines 112–172) — npm/script loading, SRI and DOM/iframe guidance.
- **Create Drop-in** (pinned raw lines 173–290) — session configuration, card/CVC setup and UI callback examples.
- **Get the outcome** (pinned raw lines 292–365) — asynchronous AUTHORISATION webhook, merchant-reference correlation, success/failure examples.
- **Test and go live** (pinned raw lines 367–393) — test paths, SAQ C-VT, live endpoints and region-matched front-end environment.

## Related

- [[adyen-unified-commerce]] — main MOTO and cross-channel source route.
- [[adyen-online-payments]] — Checkout Sessions and Web Drop-in implementation context.
- [[adyen-pci-dss-compliance]] — separate PCI scope and validation guidance; this page lists SAQ C-VT steps only.
- [[adyen-terminal-api]] — separate terminal messaging; this MOTO route uses Checkout API and Web Drop-in.

## Related raw API references

These linked guides are navigation, not independently reviewed behavior for this entry:

- Checkout Sessions API — https://docs.adyen.com/api-explorer/Checkout/latest/post/sessions
- Sessions flow Web Drop-in — https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/
- Webhooks — https://docs.adyen.com/development-resources/webhooks
- PCI DSS guide — https://docs.adyen.com/development-resources/pci-dss-compliance-guide

## Raw Sources

- [[raw/adyen/docs/unified-commerce/mail-order-telephone-order/api-request/2026-09-15|Adyen MOTO API-request guide, fetched 2026-09-15]]
