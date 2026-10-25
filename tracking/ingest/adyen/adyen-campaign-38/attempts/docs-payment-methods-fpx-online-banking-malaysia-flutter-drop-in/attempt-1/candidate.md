---
title: "FPX Online Banking Malaysia Flutter Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/flutter-drop-in/2026-09-15.md"
tags: [adyen, fpx, malaysia, flutter, drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15-captured guide describes FPX Online Banking Malaysia additions to an existing Flutter Drop-in integration, split by Sessions and Advanced server-side flow. Its redirect, testing and live-request guidance is a dated integration reference, not evidence of current enablement or payment outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** the requirements name an existing **Sessions-flow Flutter Drop-in** integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and contacting Adyen Support to add FPX Online Banking Malaysia in Customer Area. It states no additional `/sessions` parameters or method-specific configuration. The integration-type row nevertheless links to an **Advanced-flow** Flutter URL, while the redirect and session-creation links use Sessions URLs; follow the explicit label and retain the link conflict. (raw lines 25–48)
- **Advanced flow:** separately requires an existing Advanced-flow Flutter Drop-in integration, redirect handling and FPX added in Customer Area. It states no extra configuration or `/payments` parameters. This section does not give an API version minimum; the Sessions v68+ requirement should not be generalized from this page. The setup route differs from Sessions: an add-in-Customer-Area link here versus contacting Support there. (raw lines 58–80)
- **Test and live boundaries:** both sections say to use issuer IDs available for the relevant country/region, check test payments in test Customer Area, and submit a request in **live Customer Area** before accepting live payments. The test sentence calls the method an “Online banking Malaysia Component” despite this being a Drop-in page and supplies no issuer list or observed outcome. (raw lines 50–56, 82–88)

## Detail locators

- Sessions prerequisites, Support route, no extra session parameters/configuration and integration-link conflict: raw lines 25–48.
- Advanced redirect prerequisite, Customer Area route, and no extra configuration/payment parameters: raw lines 58–80.
- Test issuer guidance, Component wording and separate live request: raw lines 50–56, 82–88.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/flutter-drop-in/2026-09-15|Adyen FPX Malaysia Flutter Drop-in guide, 2026-09-15 snapshot]]
