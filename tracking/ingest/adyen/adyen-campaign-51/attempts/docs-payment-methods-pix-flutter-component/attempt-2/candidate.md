---
title: "Adyen Pix Flutter Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/pix/flutter-component/2026-09-15.md"
tags: [adyen, pix, flutter, components, qr-code, brazil]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Pix** to an existing Flutter Components integration. It separates Sessions and Advanced server-side flows, describes method-specific request fields and an Advanced `qrCode` action, and gives refund and test/live instructions. Its examples use BR/BRL, but do not prove current account enablement or a completed payment. This is a method add-on to [[adyen-online-payments]], not a complete Flutter integration. See [[adyen]].

## Key takeaways

- **Sessions prerequisites and navigation:** The page names an existing Flutter Components Sessions flow, Checkout API v68 or later, and adding Pix in Customer Area (raw lines 25–33). Its integration-type link instead targets an **Advanced Flutter Drop-in** base guide (line 31), while the create-session link targets Flutter Components Sessions (line 39). Use the flow identity and inspect the base-guide target before implementing; the first link is inconsistent.
- **Sessions request and samples:** The method-specific `/sessions` table marks `amount` required. It leaves `shopperName`, `socialSecurityNumber` (CPF/CNPJ shown on the Pix form), `shopperStatement` (maximum 140 characters), and `lineItems` fields unmarked (raw lines 37–48). The TEST v71 examples use BR/BRL and an app-scheme `returnUrl`; some show `paymentMethod.type: pix` and a `sessionValidity` dated 2021, while other SDK examples omit those fields. This is not an established Sessions requiredness rule or a current expiration value. The page says no additional Pix configuration parameters are needed (raw lines 50–90, 124–137, 275–305, 345–357, 488–509).
- **Advanced prerequisites and request:** The Advanced section names existing Flutter Components and Customer Area setup, with `action.type: qrCode` handling; its integration-type link also targets Flutter **Drop-in**, and the action-handling link points to a `handle-the-redirect` anchor despite naming `qrCode` (raw lines 530–546). Its `/payments` table marks `paymentMethod` from front-end `state.data.paymentMethod` and `amount` required. It leaves `shopperName` and `socialSecurityNumber` unmarked but advises sending both to help the shopper identify the payment. The Pix add-on table calls the required `/payments.paymentMethod` value front-end `state.data.paymentMethod`, while the captured Flutter Components Advanced base guide describes `onSubmit` returning `data` and `/payments.paymentMethod` as the complete event `payload` (base raw `raw/adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15.md`, lines 22256–22269 and 22332–22341). Do not treat the web-style `state.data.paymentMethod` path as a verified Flutter Components field (Pix raw lines 550–565).
- **Advanced limits and outcome:** For `/payments`, a provided `shopperStatement` must be under 60 characters, versus the Sessions table maximum of 140. `sessionValidity` defaults to one hour on Checkout API v71 or earlier and 24 hours on v72 or later; the v72 examples set a fixed 2025 date, not a present-time default (raw lines 45–48, 560–563, 567–606). The example response is `resultCode: Pending` with `action.type: qrCode` and `qrCodeData` (lines 1053–1073). That is a QR presentation step, not proof of payment completion; this child page does not give a final webhook-result recipe.
- **Refund, simulation and live gate:** The page says a Pix payment may be refunded within 90 days in Customer Area or through an API (raw lines 511–513, 1075–1077). It calls Pix asynchronous and instructs **test-environment** simulation by promoting a pending offer to a sale, then checking paid/promoted test offers in Payment list and testing reconciliation. A live Pix request in live Customer Area is needed before acceptance (raw lines 515–528, 1079–1092). These captured instructions are not evidence of an actual payment, refund, reconciliation run or merchant approval.

> [!warning] Base links and sample scope
> Both integration-type rows call the integration Flutter Components but target Flutter Drop-in base guides (raw lines 31 and 538). The Sessions create-session and Advanced make-payment links target Components (lines 39 and 552). Follow the correct flow and platform integration; do not infer a QR action from a redirect-anchor label. The Pix table's `state.data.paymentMethod` wording differs from the Flutter Components base guide's `onSubmit` data/complete payload handoff (base raw lines 22256–22269 and 22332–22341); verify the callback mapping. Dated request examples and simulated test promotion are not live-payment outcomes.

## Detail locators

- Sessions requirements and request-field table: pinned raw lines 25–48; examples and no-extra-configuration statement: lines 50–509.
- Sessions refund and asynchronous test/live procedure: raw lines 511–528.
- Advanced requirements and request-field table: raw lines 530–565; v72 examples: lines 567–1051.
- Advanced Pending/qrCode response, refund and test/live procedure: raw lines 1053–1092.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/flutter-component/2026-09-15|Pix Flutter Component guide, captured 2026-09-15]]
