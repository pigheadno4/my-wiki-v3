---
title: "MB WAY iOS Drop-in integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mb-way/ios-drop-in/2026-09-15.md"
tags: [adyen, mb-way, ios, drop-in, app2app]
---

## Overview

This 2026-09-15-captured MB WAY iOS Drop-in page gives method-specific additions to existing **Sessions** and **Advanced** iOS Drop-in integrations, including a standard phone-number/waiting-screen path and an optional mobile **App2App** switch. It relies on the main flow guides and does not prove current merchant enablement, a completed app switch or a successful live payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-mb-way|MB WAY overview]] for PT/EUR scope and the user-level daily cumulative limit.

## Key takeaways

- **Sessions:** requires an existing iOS Sessions Drop-in integration, Checkout API **v68 or later**, and MB WAY in Customer Area. Its method-specific `/sessions` table marks `shopperStatement` required as text shown on the shopper's bank statement. The page says no extra MB WAY Drop-in configuration is needed (raw lines 25–44, 67–71).
- **Advanced standard path:** requires an existing iOS Advanced Drop-in integration, handling for `action.type: await`, and MB WAY in Customer Area. Its method-specific `/payments` table marks `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber` required; `shopperStatement` has no required mark. A `Pending` response carries an `await` action for a waiting screen while the shopper completes payment in the MB WAY app. `Pending` is not final authorization (raw lines 96–167).
- **Optional App2App:** the page says this mobile path avoids **manual** phone-number entry and deep-links to MB WAY. Send `channel: iOS` or `Android` and a `returnUrl`; a missing channel or `Web` selects the standard phone-number path. On a successful request, use the returned `action.url` containing an MB WAY deep link with the return URL appended. **Do not wrap the deep link in an intermediate “glue page”**; on authorization the shopper returns to the app via `returnUrl`. The sample `action.type` is annotated “await, or the specific type returned by the API,” so dispatch on the actual returned action (raw lines 169–225).
- **Test/live:** any phone number is said to work in test, with an example. The `shopperStatement` suffixes `-c1`, `-c3`, and `-c5` simulate Authorised, Pending and Refused `resultCode` values; this test instruction refers to `/payments`. Live acceptance requires MB WAY added in the live Customer Area (raw lines 75–94, 227–248).

> [!warning] Flow-specific examples
> The Advanced standard `/payments` table requires a telephone number, while the **conditional** App2App example omits it after setting `channel: iOS`; do not turn the standard field mark into an unconditional App2App requirement (raw lines 120–124, 171–198). The App2App request and response examples include inline comments inside `json` fences (lines 184–218). The Advanced standard curl example uses a website return URL despite the iOS context, whereas Sessions and App2App examples use app-scheme return URLs (lines 60, 140, 195). Both curl snippets omit a line continuation between `-X POST` and `-d` (lines 53–54, 133–134). These examples require validation against the base iOS flow before implementation.

## Detail locators

- Scope and Sessions prerequisites, `shopperStatement`, no-extra-configuration: raw lines 15–71.
- Sessions test/live and result-code simulation: raw lines 73–94.
- Advanced requirements, fields and `Pending`/`await` result: raw lines 96–167.
- Conditional App2App request, deep link, no glue page and app return: raw `## Enable App2App switch` lines 169–225.
- Advanced test/live and result-code simulation: raw lines 227–248.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/ios-drop-in/2026-09-15|MB WAY iOS Drop-in guide, captured 2026-09-15]]
