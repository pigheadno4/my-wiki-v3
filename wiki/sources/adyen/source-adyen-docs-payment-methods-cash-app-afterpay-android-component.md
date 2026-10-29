---
title: "Adyen Cash App Afterpay Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/android-component"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/android-component/2026-09-15.md"
tags: [adyen, cash-app-afterpay, android, components, sessions, advanced-flow, online-payments]
---

## Overview

This captured [[adyen]] page is a short Cash App Afterpay add-on for an existing Android Components integration. It identifies Sessions and Advanced flow routes, says no method-specific request fields or Component configuration are needed, and gives sandbox and live-account setup steps. It labels itself for v5.0.0, released in October 2023, and directs earlier versions to a separate guide. [[adyen-online-payments]]

## Key takeaways

- **Version and setup:** Both Sessions and Advanced tabs require an Android Components integration with minimum version 5.0.0 and Cash App Afterpay added in Customer Area. This page labels itself v5.0.0; the earlier-versions guide is a separate route (raw lines 19–39).
- **Flow-specific work:** The Sessions tab says Cash App Afterpay adds no fields to the base `/sessions` request and no additional Component configuration, then links to creating the checkout session. The Advanced tab says the same for base `/payments` and configuration, then links to launching and showing the Component. These statements concern **additional Cash App Afterpay-specific** work, not a waiver of base flow requirements (raw lines 41–67).
- **Test and live gates:** The page describes an Afterpay sandbox shopper account for **US** testing. It says to enter a real email address, use a correctly formatted mobile number that is not used, enter SMS test code `111111`, and add a test card. It lists CVV `000` to simulate authorised test payments and `051` for refused test payments, with status checked in test Customer Area. Those are sandbox simulation instructions, not proof that a real payment was authorised. Live acceptance requires requesting Cash App Afterpay in live Customer Area (raw lines 69–87).

## Detail locators

- Page/version identity and Sessions/Advanced prerequisites: pinned raw lines 15–39.
- Request and Component configuration boundaries: pinned raw lines 41–67.
- Sandbox steps, test outcomes and live request gate: pinned raw lines 69–87.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-cash-app-afterpay]] — captured method overview; use this Android page for v5 Component scope.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/android-component/2026-09-15|Cash App Afterpay Android Component, captured 2026-09-15]]
