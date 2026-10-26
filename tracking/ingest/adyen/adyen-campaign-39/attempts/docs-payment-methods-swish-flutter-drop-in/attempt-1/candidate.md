---
title: "Swish Flutter Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/swish/flutter-drop-in/2026-09-15.md"
tags: [adyen, swish, flutter, drop-in, qr, online-payments]
---

## Overview

This 2026-09-15 guide gives Swish-specific additions to an existing Adyen Flutter Drop-in integration, separated by Sessions and Advanced server-side flows. It covers Customer Area setup, an Advanced QR action, test-simulator behavior and a separate live request. It does not document an observed payment or current merchant enablement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** the requirement text names an existing Sessions Flutter Drop-in integration, Checkout API v68 or later and Swish added in Customer Area. It says no Swish-specific `/sessions` parameters or Drop-in configuration are needed. The **Sessions** prerequisite label links to an **Advanced** Flutter Drop-in URL, while session creation links to Sessions; use the label with this route conflict in view. This branch does not state a method-specific action type. (raw lines 25–47)
- **Advanced:** separately requires an existing Advanced Flutter Drop-in integration, handling an additional `action.type: qr` action and Swish added in Customer Area. It says no extra method configuration or ordinary `/payments` parameters. The action-handling link's anchor is named `handle-the-redirect` despite the explicit `qr` action label; the source gives no further QR/redirect response example here. The Sessions v68+ minimum is not repeated in this branch. (raw lines 57–79)
- **Test and live boundary:** both branches state that a Swish test payment is authorised within 15 seconds; refusal scenarios can be simulated by putting an error code such as `FF08` in `shopperStatement`, then checking the test payment list. This test-specific input does not make `shopperStatement` an extra ordinary request requirement. Accepting live Swish payments requires a separate request in the live Customer Area. The 15-second statement is source test guidance, not a measured result for this snapshot. (raw lines 49–55, 81–87)

## Detail locators

- Sessions prerequisite misroute, v68+ minimum, no extra ordinary fields/configuration: raw lines 29–47.
- Advanced `qr` action and redirect-named anchor, no extra ordinary fields/configuration: raw lines 61–79.
- Simulator `shopperStatement`, test-list status and live request: raw lines 49–55 and 81–87.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-swish]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/flutter-drop-in/2026-09-15|Swish Flutter Drop-in guide, 2026-09-15 snapshot]]
