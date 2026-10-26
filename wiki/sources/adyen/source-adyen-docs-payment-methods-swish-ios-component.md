---
title: "Swish iOS Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/ios-component"
raw_files:
  - "adyen/docs/payment-methods/swish/ios-component/2026-09-15.md"
tags: [adyen, swish, ios, components, qr, online-payments]
---

## Overview

This 2026-09-15 guide adds Swish to an existing Adyen iOS Components integration in Sessions or Advanced server-side flow. It covers `InstantPaymentComponent`, Advanced QR-action handling, test-simulator behavior and a separate live Customer Area request. The page does not establish current merchant eligibility or an observed payment result. [[adyen]] [[adyen-online-payments]] [[adyen-ios-sdk]]

## Key takeaways

- **Sessions:** requires an existing iOS Components Sessions integration, Checkout API v68 or later, and Swish added in Customer Area. The guide says no Swish-specific `/sessions` fields or Component configuration are needed. It selects `.other("swish")` from the Session payment methods, guards against absence, creates `InstantPaymentComponent`, sets the Session as delegate and initiates payment. The snippet is an initialization example, not payment completion. (raw lines 25–69)
- **Advanced:** requires an existing iOS Components Advanced integration, handling the additional `action.type: qr` action and Customer Area addition. It says no Swish-specific configuration or ordinary `/payments` fields are needed. The snippet selects `.other("swish")` from supplied payment methods, uses `InstantPaymentComponent`, sets `self` as delegate and initiates payment. The Advanced **Components** prerequisite label links to an **iOS Drop-in** guide; its action/payment links point to Components. The `qr` action is a handoff to handle, not evidence of authorization. (raw lines 79–122)
- **Cross-guide action naming:** This iOS Components guide names `action.type: qr` for its Advanced flow (raw line 88). The separate Web API-only guide [[source-adyen-docs-payment-methods-swish-api-only]] likewise names `qr` in its requirement but shows `qrCode` in its `/payments` example response (that guide's pinned raw lines 28 and 152). The differing example and guide scopes do not establish that these values are interchangeable or a single universal action type.
- **Test and live boundary:** the page says a test-environment Swish payment is authorised within 15 seconds and describes refusal simulation by putting an error code such as `FF08` in `shopperStatement`. That simulator-specific input does not contradict the lack of extra ordinary request fields. It directs checking the test payment list. Live acceptance requires a separate Swish request in the live Customer Area. The timing is the page's test claim, not a measured outcome for this retained snapshot. (raw lines 71–77, 124–130)

## Detail locators

- Sessions prerequisites, no extra request/configuration and `InstantPaymentComponent` delegate pattern: raw lines 29–69.
- Advanced Drop-in prerequisite misroute, `action.type: qr`, Component initialization and no extra ordinary payment fields: raw lines 83–122.
- Test simulator `shopperStatement` and live-request gate: raw lines 71–77 and 124–130.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[source-adyen-docs-payment-methods-swish]]
- [[source-adyen-docs-payment-methods-swish-api-only]] — separate Web API-only action requirement and example.

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/ios-component/2026-09-15|Swish iOS Component guide, 2026-09-15 snapshot]]
