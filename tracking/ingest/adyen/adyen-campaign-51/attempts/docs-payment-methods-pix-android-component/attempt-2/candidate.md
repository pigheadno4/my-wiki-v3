---
title: "Adyen Pix Android Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/android-component"
raw_files:
  - "adyen/docs/payment-methods/pix/android-component/2026-09-15.md"
tags: [adyen, pix, android, components, qr-code, asynchronous]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Pix** to an existing Android Components integration. It covers Sessions and Advanced request fields, `InstantPaymentComponent` setup, a QR-code action, payment expiry, refunds and TEST simulation. It is a method-specific guide, not proof of current merchant eligibility or a completed Pix payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** start with an existing Android Components Sessions integration, **Checkout API v68 or later**, and Pix added in Customer Area. The `/sessions` additions mark `amount` required; `shopperName`, `socialSecurityNumber` (CPF/CNPJ shown on the Pix form), `shopperStatement` (maximum 140 characters), and `lineItems.id`/`amountIncludingTax` are unmarked. The TEST v71 examples use BR/BRL and Pix, but display `sessionValidity: 2021-12-21...`, an already past date in this capture; do not copy it as a current payment-expiry value. See raw lines 25–92 and 262–504.
- Import Android `instant` for Pix, plus `components-compose` when using Jetpack Compose. `setSubmitButtonVisible` is unmarked/optional, defaults true, and false hides the button. Sessions examples retrieve `pix` from the checkout session and use `InstantPaymentComponent`; the Compose example requires a new unique key for a different screen or payment session reset. The sample configuration block contains placeholder/irregular braces and is not a complete copy-ready constructor. See raw lines 507–605.
- **Advanced:** start with an existing Android Components Advanced flow, handling the additional `action.type: qrCode`, and Pix added in Customer Area. Import the same modules, use `InstantPaymentComponent` with a `pix` payment method from `/paymentMethods`, and use the same optional submit-button setting. The v68 floor is stated in Sessions requirements only on this page. See raw lines 626–737.
- The Advanced `/payments` table marks `paymentMethod` and final `amount` required. Its description calls `paymentMethod` the front end's `state.data.paymentMethod` from `onSubmit` (raw line 746), but the Android Advanced base guide serializes `ComponentCallback` `state.data` as `paymentComponentJson` and describes the server request's `paymentMethod` as `paymentComponentData.paymentMethod` (base raw lines 13112–13114 and 13242–13253). The mapping between these wordings is unresolved here; verify the Android client-to-server handoff rather than assuming the table's property path is Android-specific. It leaves name, CPF/CNPJ, statement, `sessionValidity` and line-item fields unmarked. The page **advises** sending both `shopperName` and `socialSecurityNumber` to identify the payment to the shopper; this is not table-requiredness. The Advanced statement field says a supplied value must stay **under 60 characters**, whereas Sessions gives a **140-character maximum**. The Advanced `sessionValidity` row says the Pix payment expires by default after **1 hour on Checkout API v71 or earlier** and **24 hours on v72 or later**. Do not apply those versioned defaults to the Sessions table, which does not state them. See raw lines 738–755.
- The TEST v72 `/payments` examples use BRL and `paymentMethod.type: pix` but display `sessionValidity: 2025-10-01...`, already past by the capture date. The sample response has `resultCode: Pending` with `action.type: qrCode`, QR data and a displayed `pix.expirationDate` from 2021. A QR action or Pending response is not payment success; use the actual current response and asynchronous outcome handling. See raw lines 757–797 and 1243–1263.
- The guide says a Pix payment can be refunded within **90 days after payment** via Customer Area or API. Pix is asynchronous. In TEST, it says a pending Pix offer can be manually promoted to a sale in Customer Area; paid/promoted offers appear in Payment list, and this promotion can test reconciliation. Live acceptance requires a Pix request in the **live** Customer Area. These are captured instructions, not evidence that any promotion, refund, or live payment was performed. See raw lines 607–624 and 1265–1284.

## Detail locators

- Sessions prerequisites, request-field table and multilingual TEST examples: raw lines 25–505.
- Sessions Android module/configuration/Component setup: raw lines 507–605.
- Sessions refund and TEST/live instructions: raw lines 607–624.
- Advanced prerequisites and Android Component setup: raw lines 626–737.
- Advanced request table, Android data-handoff wording caveat, versioned expiry rule and TEST examples: raw lines 738–1241; compare Android Advanced base-guide raw lines 13112–13114 and 13242–13253.
- Pending QR action, refund and TEST/live instructions: raw lines 1243–1284.

## Related

- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15|Android Advanced base flow: ComponentCallback serialization and paymentMethod mapping, targeted lines 13112–13114 and 13242–13253; not fully read for this worker]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/android-component/2026-09-15|Fully read Pix Android Component raw]]
