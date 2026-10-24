---
title: "Adyen PayPay Web Component integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/web-component"
raw_files:
  - "adyen/docs/payment-methods/paypay/web-component/2026-09-15.md"
tags: [adyen, paypay, web, component, redirect]
---

## Overview

This [[adyen]] guide adds **PayPay** to an existing **Web Components** integration through the `Redirect` Component. It provides method-specific additions for **Sessions** and **Advanced** server-side flows; the linked main integration guides still supply the general payment and redirect lifecycle. Component setup or a TEST simulator redirect is not authorization, capture, settlement or a final shopper outcome. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The guide requires an existing Sessions Web Components integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and PayPay added in Customer Area. It says no additional PayPay parameters are needed when creating `/sessions`. Import `Redirect` from `@adyen/adyen-web` and initialize/mount it; the page states no extra PayPay configuration parameters. These are PayPay-specific additions, not a replacement for the main Sessions request or redirect handling. See raw lines 25–72.
- **Advanced:** The guide separately requires an existing Advanced Web Components integration, redirect handling and PayPay added in Customer Area. It imports and initializes the same `Redirect` Component, and says no additional PayPay parameters are needed for `/payments`. The Advanced requirements table does **not** state the Sessions section's v68+ minimum; do not transfer it across flows from this page. See raw lines 87–125.
- Both initialization examples show `new Redirect(checkout, { type:paypay })`; `paypay` is unquoted and no variable declaration appears in the pinned page. Treat this as an incomplete JavaScript example requiring verification in the applicable SDK rather than a copy-ready snippet. See raw lines 70–72 and 115–119.
- **TEST and LIVE:** For TEST, the page names `DGFT_AcquirerAccount_Adyen_closedLoop_AUTHFlow` and `DGFT_AcquirerAccount_Adyen_closedLoop_SALEFlow`; it says the shopper is redirected to a DGFT simulator and does not need a PayPay app, and test transactions can be checked in Customer Area. For LIVE, it says the activated PayPay smartphone app must be accessed through a Japan local IP address. These are page-scoped test/live instructions, not proof of a merchant's live enablement, PayPay-provider outcome or a completed payment. See raw lines 74–85 and 127–138.

## Detail locators

- Add-on scope and flow split: raw lines 15–25.
- Sessions prerequisites, request, import, configuration and initialization: raw lines 27–72.
- Advanced prerequisites, import, initialization and request: raw lines 87–125.
- Duplicated TEST acquirer/simulator and LIVE app/IP guidance: raw lines 74–85 and 127–138.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypay]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/web-component/2026-09-15|Adyen PayPay Web Component guide]]
