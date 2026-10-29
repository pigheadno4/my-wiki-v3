---
title: "Pix Android Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pix/android-drop-in/2026-09-15.md"
tags: [adyen, pix, android, drop-in, sessions, advanced, qr-code]
---

## Overview

This 2026-09-15-captured Adyen page describes Pix additions to an existing Android Drop-in integration in Sessions or Advanced flow. The Sessions section gives method-specific session fields and optional button configuration; the Advanced section adds payment-request fields and a `qrCode` action. This is an add-on to the main integration, not a complete implementation or evidence of current merchant enablement or payment success. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Android Drop-in Sessions integration, Checkout API v68 or later, and Pix setup in Customer Area. The `/sessions` table marks `amount` required; it lists `shopperName`, `socialSecurityNumber` (shopper CPF/CNPJ), `shopperStatement` and line-item fields without required marks. Its `shopperStatement` maximum is 140 characters. See raw lines 25–50.
- Advanced requires an existing Android Drop-in Advanced integration, Pix setup in Customer Area and handling of an additional `action.type: qrCode`. Its `/payments` table marks `paymentMethod` and `amount` required. The `paymentMethod` row calls it `state.data.paymentMethod` from a frontend `onSubmit` event, but this page does not reconcile that Web-like wording with Android Drop-in; do not infer an Android callback or field-source contract from the phrase. It calls `shopperName` and `socialSecurityNumber` advisable because they appear to the shopper, rather than required. Its `shopperStatement`, if provided, must be under 60 characters. See raw lines 551–600; the example response has `Pending` with a `qrCode` action at lines 1088–1107.
- The optional `setSubmitButtonVisible` setting can hide the submit button when false; the table gives default true in both flows. The Sessions and Advanced `CheckoutConfiguration` Kotlin snippets have an unlabeled nested block, so they are not copy-ready Android syntax. See raw lines 510–526 and 565–581.
- Advanced `sessionValidity` is listed without a required mark. The page says its default Pix expiry is one hour for Checkout API v71 or earlier and 24 hours for v72 or later. These version-specific defaults and the Sessions/Advanced statement-length limits must not be merged. See raw lines 45–49 and 593–600.
- The page says a payment can be refunded within 90 days through Customer Area or API. It calls Pix asynchronous: in the test environment, a pending offer can be promoted to sale in test Customer Area, then inspected under Payment list and used for reconciliation testing. For live acceptance, the captured instruction is to submit a Pix request in live Customer Area. These are snapshot instructions, not proof of a completed test, refund, or live payment. See raw lines 528–549 and 1110–1127.

> [!warning] Example and action-guide scope
> The Sessions and Advanced `CheckoutConfiguration` snippets have unlabeled nested blocks (raw lines 519–526, 573–581); preserve the optional submit-button setting/default from their tables, but do not copy the snippets as complete Kotlin configuration. The Advanced `paymentMethod` table describes `state.data.paymentMethod` from `onSubmit` (raw line 591) without reconciling that wording to Android Drop-in; retain the required field without inferring an Android callback contract.
>
> The Sessions sample carries `sessionValidity: 2021-12-21` (raw line 70), and the Advanced request examples carry `2025-10-01` (for example lines 630 and 1074), dates already past this 2026-09-15 capture. Do not copy those timestamps as current expiry values. The Advanced requirement names a `qrCode` action but links to a base-guide `#handle-the-redirect` anchor (raw line 558); verify the Android Drop-in handling for the actual QR action. The example `Pending` response is not final payment success.

## Detail locators

- Sessions prerequisites, fields and example: raw `## Sessions flow Drop-in`, lines 25–504.
- Sessions optional submit-button configuration, refund and test/live steps: raw lines 506–549.
- Advanced prerequisites, optional button configuration and `/payments` field table: raw lines 551–600.
- Advanced request examples and `Pending`/`qrCode` response: raw lines 602–1108.
- Advanced refund and test/live steps: raw lines 1110–1127.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/android-drop-in/2026-09-15|Pix Android Drop-in, captured 2026-09-15]]
