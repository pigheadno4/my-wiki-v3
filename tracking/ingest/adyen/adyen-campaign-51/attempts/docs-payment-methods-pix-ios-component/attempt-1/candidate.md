---
title: "Adyen Pix iOS Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/ios-component"
raw_files:
  - "adyen/docs/payment-methods/pix/ios-component/2026-09-15.md"
tags: [adyen, pix, ios, component, qr-code, asynchronous]
---

## Overview

This 2026-09-15-captured Adyen guide adds Pix to an existing **iOS Components** integration in either Sessions or Advanced server-side flow. It covers Pix-specific request data, `InstantPaymentComponent` initialization, Advanced QR action handling, and asynchronous test/live steps. It is an add-on to the base integration, not proof of current Pix enablement or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** an existing iOS Components Sessions integration, **Checkout API v68 or later**, and Pix added in Customer Area are prerequisites. The `/sessions` table marks `amount` required; `shopperName`, `socialSecurityNumber` (CPF/CNPJ), `shopperStatement`, and `lineItems` entries are unmarked. The table gives `shopperStatement` a 140-character maximum. These are Pix additions to a base request, not the full base schema. See raw lines 25–50.
- Sessions needs no additional Pix configuration. Its Swift example obtains the supported `.other("pix")` payment method, creates `InstantPaymentComponent`, delegates to the session, and calls `initiatePayment()`. The examples are illustrative; the `/sessions` curl sample uses a historical 2021 `sessionValidity` and should not be copied as a current expiry. See raw lines 52–92 and 507–533.
- **Advanced:** an existing iOS Components Advanced integration, `action.type: qrCode` handling, and Customer Area setup are prerequisites. No additional Pix configuration is stated. The prerequisite's *iOS Components* label points to a **Drop-in** base-guide URL, while its action link points to Components; follow the integration type stated in the row and verify the base guide. See raw lines 554–576.
- In Advanced `/payments`, the table marks `paymentMethod` and `amount` required. It recommends, rather than requires, both `shopperName` and `socialSecurityNumber` to help shoppers identify the payment. The table describes `paymentMethod` using front-end `state.data.paymentMethod` from an `onSubmit` event, although this iOS example initializes an `InstantPaymentComponent` and calls `initiatePayment()`; the page does not reconcile that event wording. Do not infer an iOS callback contract from it. See raw lines 580–610.
- The Advanced table gives `shopperStatement` a **less-than-60-character** limit when supplied, versus the Sessions table's 140-character maximum. It says `sessionValidity` defaults to **1 hour through Checkout API v71** and **24 hours from v72**. An example `/payments` response contains a `qrCode` action and `resultCode: Pending`; the QR action and pending response are not final payment success. The sample expiration timestamps are historical. See raw lines 45–50, 603–608, 617–651, and 1098–1118.
- Pix is described as **asynchronous**. In the test Customer Area, a pending offer can be manually promoted to a sale, and paid/promoted records appear in **Payments > Payment list**; the page directs testing reconciliation this way. Before live acceptance it says to submit a Pix request in the live Customer Area. The page states a 90-day refund window via Customer Area or API. These are captured instructions/claims, not evidence of an actual payment, reconciliation, entitlement, or refund. See raw lines 535–552 and 1120–1137.

## Detail locators

- Sessions prerequisites and Pix `/sessions` parameter table: raw `## Sessions flow Component`, lines 25–50; language examples lines 52–505.
- Sessions no-extra-configuration and Swift initialization: raw lines 507–533.
- Advanced prerequisites, QR action and conflicting Drop-in base link: raw `## Advanced flow Component`, lines 554–564.
- Advanced Swift initialization and `/payments` table, including optional fields, expiry and statement limits: raw lines 566–610; language examples lines 612–1096.
- Pending QR response, refund and asynchronous test/live steps: raw lines 1098–1137; duplicated Sessions refund/test/live text at lines 535–552.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/ios-component/2026-09-15|Fully read Pix iOS Component raw]]
