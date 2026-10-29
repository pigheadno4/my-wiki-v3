---
title: "Adyen Walley Android Components v5.0.0 integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/android-component"
raw_files:
  - "adyen/docs/payment-methods/walley/android-component/2026-09-15.md"
tags: [adyen, walley, android, components, sessions, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds Walley to an existing Android Components integration. The page identifies itself as **v5.0.0**, released October 2023, and directs earlier versions to a separate guide. Both Sessions and Advanced flows are covered with a minimum Android Components version of 5.0.0. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-walley]] for Walley's method and regional overview.

## Key takeaways

- Start with the appropriate existing Android Components flow, version 5.0.0 or later, and add Walley in Customer Area. The page distinguishes Sessions and Advanced base integration routes. Earlier versions have a separate guide; this page's no-additional-field statements must not be applied to those versions or to another platform. See raw lines 21–39.
- For this Android Components guide, Walley specifies no additional fields for a Sessions `/sessions` request or an Advanced `/payments` request, and no additional Walley Component configuration for either flow. Base integration requirements still apply. After configuration, Sessions creates the checkout session and Advanced launches and shows the Component. See raw lines 41–67.
- For testing through Adyen `/payments`, map Walley's `CivRegNo` to `socialSecurityNumber`; the page shows a B2B company object with `name` and `registrationNumber`. Check verification-payment status in the **test** Customer Area payment list. This test guidance is not a claim of live enablement, successful payment, or universal B2B request requirements. See raw lines 69–82.
- The See also links navigate to Android Components, webhooks, tokenization, and API Explorer. They do not by themselves establish Walley-specific webhook or recurring behavior. See raw lines 84–89.

## Detail locators

- Version scope and earlier-version route: raw lines 19–21.
- Sessions and Advanced prerequisites: raw lines 23–39.
- Per-flow API and Component configuration statements: raw lines 41–67.
- Walley test scenarios, `CivRegNo` mapping, B2B example, status route: raw lines 69–82.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-walley]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/android-component/2026-09-15|Fully read Walley Android Component raw]]
