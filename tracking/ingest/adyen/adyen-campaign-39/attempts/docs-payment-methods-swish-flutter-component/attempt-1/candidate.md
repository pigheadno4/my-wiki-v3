---
title: "Swish Flutter Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/swish/flutter-component/2026-09-15.md"
tags: [adyen, swish, flutter, components, online-payments, qr]
---

## Overview

This 2026-09-15 Adyen guide gives Swish-specific additions to an existing Flutter Components integration for either Sessions or Advanced server-side flow. It provides setup, action handling, TEST simulator and LIVE request routes. The page is a historical guide, not proof of current merchant enablement or completed live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** The guide requires an existing Flutter Components Sessions integration, Checkout API v68 or later, and Swish addition in Customer Area (raw lines 25–33). It says no extra Swish parameters are needed for `/sessions` and no extra Component configuration is needed (lines 35–45).
- **Advanced:** The guide requires an existing Flutter Components Advanced integration, handling an additional `action.type: qr` action, and Swish addition in Customer Area (lines 55–65). It states that no extra Swish configuration or `/payments` parameters are needed (lines 67–77). The linked action guide's anchor says “handle-the-redirect,” but this page explicitly specifies `qr`; do not replace QR action handling with a redirect assertion.
- **TEST and LIVE:** The source says Swish payments in the test environment are authorised within 15 seconds and describes simulating refusal scenarios by putting a Merchant Swish Simulator error code such as `FF08` in `shopperStatement` (lines 47–51, 79–83). This is source-described TEST behavior, not a live latency promise. It directs checking test payment status in Customer Area. Accepting LIVE Swish payments requires a separate request in the LIVE Customer Area (lines 53, 85).
- **Link mismatch:** Both Flutter Components prerequisite labels point to URLs with `integration=Drop-in`; the Sessions link additionally points to an Advanced-flow path (lines 31, 63). Treat those links as navigation that needs checking, not evidence that the described Components flow is Drop-in or that Sessions is Advanced. The page does not state a Flutter SDK version or a country/currency eligibility matrix.

## Detail locators

- Sessions prerequisites, no-extra-parameter/configuration statements and TEST/LIVE guidance: raw lines 25–53.
- Advanced prerequisites and `qr` action handling, including mismatched link anchor: raw lines 55–65.
- Advanced no-extra-configuration/`/payments` statements and repeated TEST/LIVE guidance: raw lines 67–85. The `shopperStatement` refusal code is a test fixture, not a production request requirement.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/flutter-component/2026-09-15|Swish Flutter Component, fetched 2026-09-15]]
