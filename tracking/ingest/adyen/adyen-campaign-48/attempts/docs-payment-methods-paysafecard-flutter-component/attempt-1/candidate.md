---
title: "PaySafeCard Flutter Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/flutter-component/2026-09-15.md"
tags: [adyen, paysafecard, flutter, components, online-payments]
---

## Overview

This 2026-09-15-captured [[adyen]] PaySafeCard Flutter Components add-on describes method-specific changes for existing Sessions or Advanced online-payment integrations. It is not a standalone Flutter integration guide. See [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard method overview]] for the method's broader capability and market context.

## Key takeaways

- **Sessions flow:** The page requires an existing Flutter Components Sessions integration, Checkout API v68 or later, redirect-action handling, and PaySafeCard enabled in the Customer Area. It adds `shopperReference` to `/sessions`; no PaySafeCard-specific Component configuration parameters are needed. See raw lines 25–44 and 268–272.
- **Advanced flow:** The page requires an existing Flutter Components Advanced integration, redirect-action handling, and PaySafeCard enabled in the Customer Area. It adds `shopperReference` to `/payments`; no PaySafeCard-specific Component configuration parameters are needed. The example response has `resultCode: RedirectShopper` and a `redirect` action. See raw lines 284–310 and 597–611.
- **Test and live:** The page gives a 16-digit test code, directs payment-status checks to the test Customer Area, and says to contact Adyen Support to add PaySafeCard in the live Customer Area before accepting live payments. This is a documented setup gate, not evidence of current account eligibility or a successful live transaction. See raw lines 274–282 and 613–621.

## Detail locators

- Sessions request table and language examples: raw lines 36–266. The curl sample uses a test `/v71/sessions` endpoint and NL/EUR example values; these are examples, not universal market or currency constraints.
- Advanced `/payments` table and language examples: raw lines 302–595. The curl sample uses test `/v72/payments` and EUR example values. The abbreviated samples are method add-ons, not complete executable integration recipes.
- Redirect response example: raw lines 597–611. The shopper must have redirect handling in the existing integration; the page does not establish final payment success from that intermediate response.
- **Source-link caveat:** Both the Sessions and Advanced *Integration type* rows describe Flutter Components but link to base-guide URLs whose query parameter says `integration=Drop-in`; the Sessions row also points to the Advanced-flow guide (raw lines 31 and 292). Follow the separate Components redirect links in raw lines 33 and 293, and verify the intended base guide before using those mismatched links.
- **Example caveat:** The Sessions curl sample has `-X POST` followed by `-d` without a continuation backslash (raw lines 50–66). Several library examples refer to request objects whose construction is omitted (for example raw lines 84–87 and 262–265). Treat the page's samples as illustrative fragments.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard method overview]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/flutter-component/2026-09-15|PaySafeCard Flutter Component, captured 2026-09-15]]
