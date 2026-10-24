---
title: "UPI Android Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/android-component"
raw_files:
  - "adyen/docs/payment-methods/upi/android-component/2026-09-15.md"
tags: [adyen, upi, android, components, india]
---

## Overview

This 2026-09-15 Adyen guide describes UPI-specific Android Component setup for **existing Sessions or Advanced** integrations. It shows a general UPI Component, an Advanced-flow UPI Intent `appId` request field, and a TEST simulator checklist. It does not specify UPI AutoPay mandates or a live merchant approval procedure. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** requires an existing Android Components Sessions integration with **Checkout API v68 or later** and UPI added in Customer Area. It says no additional UPI-specific `/sessions` parameters. The UPI module is imported with `YOUR_VERSION`; Compose also imports `components-compose`. The optional `setSubmitButtonVisible` configuration has a blank Required column, and the page shows Compose and non-Compose `UPI.PROVIDER.get` routes using a payment method from `checkoutSession`. (raw lines 23–139)
- **Advanced:** requires an existing Android Components Advanced integration, UPI added in Customer Area, and handling an additional `action.type: await`. The action-handling link on that row uses a `#handle-the-redirect` anchor; the page does not establish that `await` and redirect handling are identical. Its Component obtains the UPI payment method from a `/paymentMethods` response, with Compose and non-Compose routes. The same optional submit-button setting is listed. This section has no stated Checkout API minimum; its example `/payments` URL uses **v72**, which is an example version, not a universal floor. (raw lines 163–274, 275–305)
- For **Advanced UPI Intent only** (`paymentMethod.type: upi_intent`), `paymentMethod.appId` is required and identifies the shopper's Third Party Application Provider (TPAP); the raw table lists possible app IDs. The TEST v72 request illustrates `gpay`, IN/INR and a `returnUrl`. Do not generalize the `appId` condition to all UPI options or infer a mandatory app/device selection flow from this example. (raw lines 275–305)
- The TEST checklist describes an Adyen-hosted Payment Simulator redirect for UPI Intent and a **“UPI QR (on web)”** scan path, then says to select and validate an outcome through webhook/Customer Area. That QR phrase is web-scoped text inside this Android guide, so it does not by itself establish an Android QR UI. The checklist asks the tester to select a simulator outcome but lists `eventCode: AUTHORISED` without an outcome condition. That is the page's listed webhook code, not a guarantee for every selected outcome; no alternative codes are given. The page presents no observed webhook, payment success or capture/settlement proof. (raw lines 141–161, 307–327)
- The page contains placeholder dependencies/keys and a configuration snippet with nested bare braces around `setSubmitButtonVisible(value)`; those snippets need SDK/version-aware implementation review. This page does not state the UPI Collect transition dates or give Collect/AutoPay instructions; the method overview and their own guides are separate evidence. (raw lines 51–83, 96–139, 183–215, 228–273)

## Detail locators

- Sessions prerequisites, imports, optional configuration and component mounting: raw lines 23–139.
- Sessions TEST simulator and webhook/Customer Area checklist: raw lines 141–161.
- Advanced action/Component setup and optional configuration: raw lines 163–274.
- Advanced UPI Intent `appId` condition and TEST v72 example: raw lines 275–305.
- Advanced TEST simulator/checklist: raw lines 307–327.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-upi]]
- [[source-adyen-docs-payment-methods-upi-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/android-component/2026-09-15|Adyen UPI Android Component, 2026-09-15 snapshot]]
