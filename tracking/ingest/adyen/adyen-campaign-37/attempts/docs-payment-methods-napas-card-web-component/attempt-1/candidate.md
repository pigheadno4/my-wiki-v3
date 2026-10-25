---
title: "Adyen Napas card Web Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/web-component"
raw_files:
  - "adyen/docs/payment-methods/napas-card/web-component/2026-09-15.md"
tags: [adyen, napas, vietnam, web, components, redirect, cards]
---

## Overview

This Adyen page, last modified 2019-09-06 and captured 2026-09-15, describes adding **Napas card to an existing Web Components integration**. It gives Sessions/Advanced prerequisites, versioned Component snippets, test-card fixture locations and a separate live request. It does not document final authorization, capture or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Base flows and method fields:** Sessions and Advanced tabs each require the corresponding existing Web Components integration and Napas card added in Customer Area. The page says no extra Napas-specific API fields are required. It calls `/sessions` the default with **Components v5.0.0 or later**, and links `/payments` for an additional use case; v5.0.0 is a **Components/Web SDK version**, not a Checkout API minimum. Generic optional fields belong to the endpoint reference. (raw lines 21–44)
- **Versioned Component setup:** The page creates a DOM mount element, then for **v6.0.0 or later** shows `new Redirect(checkout, { type: 'momo_atm' })`; for **v5.x.x or earlier** it shows `checkout.create('momo_atm')`. Both mount to `#momo_atm-container`. The page calls the method Napas card but uses **`momo_atm` in its examples**; retain that source identifier without assuming it is interchangeable with any other Napas type or asserting the snippet is runnable without base imports/configuration. A stray `**` appears between version sections and has no explained semantic role. (raw lines 46–76)
- **TEST and live boundary:** The guide lists TEST card and one-time-password fixtures for success, blocked card, insufficient funds and amount-over-limit scenarios. Treat them as test-only data, not live card or security-operation instructions; the values remain in raw lines 80–87. It points to test Customer Area payment status, while live acceptance separately requires a Napas card request in the **live Customer Area**. A listed “Successful” fixture or status check does not prove that a transaction was actually authorized. (raw lines 78–91)
- **Flow limit:** This page does not spell out the shopper bank/gateway/PIN/OTP redirect sequence or return/details/webhook processing; the Napas overview and base Web Components guide are separate authority. Component mounting and test credentials alone are not a completed payment. (raw lines 19–23, 46–97)

## Detail locators

- Sessions/Advanced requirements and Customer Area setup: raw lines 21–37.
- No extra Napas fields and Components v5.0.0 `/sessions` default: raw lines 39–44.
- DOM and v6/v5 `momo_atm` snippets plus stray marker: raw lines 46–76.
- TEST scenario fixtures, test status and separate live request: raw lines 78–91.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-napas-card]]
- [[source-adyen-docs-payment-methods-napas-card-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/web-component/2026-09-15|Adyen Napas card Web Component, 2026-09-15 snapshot]]
