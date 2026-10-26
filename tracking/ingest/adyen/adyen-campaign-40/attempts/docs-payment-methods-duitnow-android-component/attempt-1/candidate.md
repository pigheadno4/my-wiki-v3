---
title: "DuitNow Android Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/duitnow/android-component"
raw_files:
  - "adyen/docs/payment-methods/duitnow/android-component/2026-09-15.md"
tags: [adyen, duitnow, malaysia, android, components, online-payments]
---

## Overview

This Adyen page adds DuitNow to an existing **Android Components** integration, with separate Sessions and Advanced instructions. Its metadata says last modified 2019-09-06; the pinned copy was captured 2026-09-15. It is a method-specific add-on, not a complete Android checkout guide. Both branches instruct the merchant to contact Adyen Support to add DuitNow in Customer Area. [[adyen]] [[adyen-android-sdk]] [[adyen-online-payments]]

## Key takeaways

- The **Sessions** branch requires an existing Android Components Sessions integration with minimum version **5.0.0**. Its session request needs no DuitNow-specific parameters, and its Component configuration needs no DuitNow-specific additions. Compose examples import `com.adyen.checkout:instant` plus `components-compose`; non-Compose imports `instant`. Both use `InstantPaymentComponent` and retrieve the payment method as `duitnow`. See raw lines 23–132.
- The **Advanced** branch requires an existing Android Components Advanced integration and Support-assisted method setup. It says no specific Component configuration is needed, points to the base Advanced launch guide, and gives a `/payments` example with `paymentMethod.type: duitnow` and MYR amount. The Advanced requirements table does **not** state a 5.0.0 minimum; nearby `version=5.2.0` links are guide URLs rather than an explicit minimum. See raw lines 135–200.
- The code samples are illustrative, not ready-to-run request constructors. The Sessions Compose launch snippet has a stray `Component` line and Java-labeled fence containing Kotlin/Compose code; several Advanced language snippets refer to `paymentRequest` without constructing it, whereas curl, Node JS, Python and Ruby show example request bodies. The Advanced import step links a Sessions guide, and its launch URL lacks an explicit `platform=Android` parameter. See raw lines 79–110, 150–175 and 202–399.
- The guide says to test with real payment details and small amounts, check test payment status in Customer Area, and contact Support to add DuitNow in the **live** Customer Area before acceptance. No payment response, QR/action handling sequence, webhook outcome, settlement or refund behavior is established by this page. Its snapshot and example request do not prove current merchant eligibility or a successful payment. See raw lines 177–200 and 401–407.

## Detail locators

- Sessions prerequisites and method setup: raw lines 23–36.
- Sessions library imports, configuration and Compose/View Component launch: raw lines 38–132.
- Advanced prerequisites, configuration, import and launch guide: raw lines 135–175.
- Advanced MYR/`duitnow` request and language examples: raw lines 177–399.
- TEST instructions and live Support gate: raw lines 401–407.

## Related

- [[adyen-android-sdk]] — Android Sessions and Advanced integration context.
- [[adyen-online-payments]] — online payment-method context.
- [[source-adyen-docs-payment-methods-duitnow]] — DuitNow method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/duitnow/android-component/2026-09-15|DuitNow Android Component, captured 2026-09-15]]
