---
title: "MB WAY Android Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mb-way/android-drop-in/2026-09-15.md"
tags: [adyen, mb-way, android, drop-in, app2app, portugal]
---

## Overview

This 2026-09-15-captured Adyen guide describes **MB WAY-specific additions to an existing Android Drop-in** integration. It separates Sessions and Advanced server-side flows, a standard phone-number/MB WAY app confirmation journey, and an optional mobile App2App deep-link journey. The instructions are not a complete base integration or proof of current merchant enablement or payment success. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** use an existing Android Drop-in Sessions integration with Checkout API **v68 or later**, and add MB WAY in Customer Area. The guide marks `shopperStatement` required on `/sessions`, with text shown on the shopper's bank statement. Its v71 example uses **PT/EUR** and an app-scheme `returnUrl`; those are example values, not a standalone end-to-end recipe (raw lines 25–65).
- **Advanced flow:** use an existing Android Drop-in Advanced integration that handles the additional `action.type: await`, and add MB WAY in Customer Area. The `/payments` table marks `paymentMethod.type = mbway` and `paymentMethod.telephoneNumber` required for the standard phone-number flow, while `shopperStatement` is optional in that table. The sample response is **Pending** with an `await` action to display a waiting screen while the shopper completes payment in the MB WAY app; Pending does not establish final authorization (raw lines 112–120, 146–197).
- Both flows document optional `setSubmitButtonVisible = false` to hide the submit button; the default is true. The Kotlin snippet contains placeholders/extra braces and is illustrative, not a complete copy-ready configuration (raw lines 69–87, 124–142).
- **Optional App2App path:** the guide says this path removes manual phone-number entry and deep-links the shopper to the MB WAY app. In `/payments`, send `channel` as **iOS** or **Android** and a `returnUrl`; missing `channel` or **Web** uses the standard phone-number flow. The response's `action.url` contains the `mbway://` deep link with the provided return URL appended. Redirect directly to that action URL without an intermediate page; after authorization the shopper returns through `returnUrl` (raw lines 199–255). The App2App examples contain inline comments in JSON and an action-type placeholder, so they are illustrative rather than valid literal JSON or guaranteed response shape.
- To test, the guide permits any telephone number and gives a test example; result-code suffixes on `shopperStatement` are test triggers. Live acceptance requires MB WAY to be added in the **live Customer Area** (raw lines 91–110, 257–276). The separate [[source-adyen-docs-payment-methods-mb-way|MB WAY overview]] records the **PT/EUR** matrix, refund/capture/recurring indicators, and a **daily cumulative user limit**; those are method-level snapshot claims, not extra child-guide request fields or merchant-specific guarantees (overview raw lines 23–36).

## Detail locators

- Scope and Sessions prerequisites/field/sample: raw lines 15–65.
- Sessions configuration and test/live setup: raw lines 69–110.
- Advanced prerequisites, standard phone-number fields, Pending/await response: raw lines 112–197.
- App2App switch, channel/returnUrl, deep link and direct redirect: raw lines 199–255.
- Advanced test/live gate and result-code triggers: raw lines 257–276.
- Method-level PT/EUR, capability matrix and user daily cumulative limit: [[source-adyen-docs-payment-methods-mb-way]] and its pinned raw lines 23–36; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/android-drop-in/2026-09-15|MB WAY Android Drop-in guide, captured 2026-09-15]]
