---
title: "Adyen Docs: Online payments"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments"
raw_files:
  - "adyen/docs/online-payments/2026-09-15.md"
tags: [adyen, online-payments, checkout, webhooks]
---

## Overview

This Adyen documentation overview introduces [[adyen-online-payments]] for accepting card, wallet, and local payment methods on websites and mobile apps. It maps the solution's supported use cases and features, outlines a three-part integration architecture, and routes readers to the integration checklist, build guide, and plugin path.

The page is an overview rather than proof of current method availability, account eligibility, a particular library version, or successful payment execution.

## Key takeaways

- The overview covers one-off payments, subscriptions, bookings, and account top-ups, alongside authentication, risk management, donations, and recurring-payment detail storage. See **Seamless checkout → Transaction types** and **Seamless checkout → Features** in the raw snapshot.
- Its architecture separates a payments server that calls Checkout API endpoints, a client website or app that collects shopper payment details and passes payment information to that server, and a webhook server that receives payment-status and other payments-related activity.
- API Libraries for the server and Drop-in/Components for the client are recommendations in this page, not stated requirements. See **Integration architecture → Payments server** and **Integration architecture → Client website or app**.
- The page says Adyen frequently releases library versions and updates APIs, and recommends keeping integrations current and reviewing the product lifecycle; claims about exact behavior therefore need versioned implementation or API evidence.
- The overview also describes payment-method processing through a single API and management of in-person payments and unified channel data on the same platform. See **One platform** for the page's scope and wording.

## Detail locators

- **Release notes** — library/API updates and the update/lifecycle recommendation.
- **Seamless checkout → Transaction types** — one-off payments, subscriptions, bookings, and top-ups.
- **Seamless checkout → Features** — 3D Secure 2, risk management, donations, and stored payment details for recurring payments.
- **One platform** — single-API and online/in-person platform positioning.
- **Integration architecture** — payments-server, client, and webhook-server responsibilities; recommended server and client integration surfaces.
- **Next steps** — integration checklist, build guide, and plugin routes.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/2026-09-15|Adyen Docs — Online payments (2026-09-15)]]
