---
title: "Adyen Boost Wallet Android Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boost/android-drop-in/2026-09-15.md"
tags: [adyen, boost, android, drop-in, redirect]
---

## Overview

This [[adyen]] guide describes **Boost Wallet-specific additions** to an existing **Android Drop-in** integration under separate **Sessions** and **Advanced** server-side flows. The Advanced section specifies a `redirect` action. The page expressly says **no Boost Wallet test environment is available** and refers to small-value tests in **live**; this is historical source guidance with real-money consequences, not an instruction to conduct a payment. It does not document final authorization, capture, settlement or refund results. [[adyen-online-payments]]

## Key takeaways

- **Sessions base path:** The Sessions section requires an existing Android Drop-in Sessions integration, **Checkout API v68 or later**, and Boost Wallet added in Customer Area. It says no **additional Boost Wallet-specific** /sessions parameters or configuration are needed. This section has no explicit redirect-handling requirement in its table; the Advanced section supplies that instruction. See raw lines 25–46.
- **Advanced base path:** The Advanced section requires an existing Android Drop-in Advanced integration, handling `action.type: redirect`, and Boost Wallet added in Customer Area. It says no additional Boost Wallet configuration or parameters for the ordinary /payments request. It does not state an Advanced-flow Checkout API minimum. See raw lines 54–74.
- **Test/live boundary:** Both sections say there is **no test environment available for Boost Wallet** and instruct penny tests in the **live environment**. This means the page does not offer a harmless sandbox test route; it gives no test credentials, reversal procedure, merchant approval evidence or final status path. Retain the exact historical environment restriction without treating a proposed live test as completed or safe. See raw lines 48–52 and 76–78.

## Detail locators

- Sessions requirements, base request and configuration: raw lines 25–46.
- Sessions no-TEST/live-testing statement: raw lines 48–52.
- Advanced redirect, setup and base request: raw lines 54–74.
- Repeated no-TEST/live-testing statement: raw lines 76–78.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boost]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/android-drop-in/2026-09-15|Adyen Boost Wallet Android Drop-in snapshot]]
