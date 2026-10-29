---
title: "MB WAY Flutter Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mb-way/flutter-drop-in/2026-09-15.md"
tags: [adyen, mb-way, flutter, drop-in, portugal]
---

## Overview

This 2026-09-15-captured Adyen guide adds **MB WAY-specific steps to an existing Flutter Drop-in** integration. It separates Sessions and Advanced server-side flows and covers request fields, `await` action handling, and test/live setup. It does not describe an App2App request/deep-link recipe and is not proof of current merchant enablement or payment success. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** the page requires an existing Flutter Drop-in Sessions flow, Checkout API **v68 or later**, and contacting Adyen Support to add MB WAY in Customer Area. It marks `shopperStatement` required on `/sessions`; the v71 sample uses **PT/EUR** and an app-scheme `returnUrl`. The Sessions requirement's integration-type link actually points to an **Advanced-flow URL**, whereas the create-session link points to Sessions; follow the flow heading and the matching base guide (raw lines 25–65).
- **Advanced:** the page requires an existing Flutter Drop-in Advanced flow that handles `action.type: await`, plus Customer Area setup. Its `/payments` table marks `paymentMethod.type = mbway` and `paymentMethod.telephoneNumber` required, while `shopperStatement` is optional. The example response is **Pending** and includes an `await` action for a waiting screen while the shopper completes payment in the MB WAY app; Pending is not final authorization (raw lines 95–105, 115–165).
- The guide says **no additional MB WAY configuration parameters** are needed in either flow (raw lines 68–72, 107–111).
- To test, it permits any telephone number and gives an example; it lists `shopperStatement` suffixes for test `resultCode` outcomes. Those test-trigger instructions refer to `/payments` even in the Sessions section, so do not infer a separate Sessions trigger recipe. Before live acceptance, MB WAY must be added in **live Customer Area** (raw lines 74–93, 168–187).
- The separate [[source-adyen-docs-payment-methods-mb-way|MB WAY overview]] distinguishes Web phone-number confirmation from mobile App2App authorization and gives the **PT/EUR** capability matrix and **daily cumulative user limit**. Those are method-level snapshot facts; this Flutter child guide only specifies its phone-number `/payments` request and does not itself provide App2App implementation steps (overview raw lines 23–36).

## Detail locators

- Add-on scope, Sessions prerequisites, request field and example: raw lines 15–65; note mismatched Sessions requirement link at line 33.
- Sessions configuration and test/live notes: raw lines 68–93.
- Advanced prerequisites, `await` handling, fields and Pending response: raw lines 95–165.
- Advanced test/live notes: raw lines 168–187.
- Method-level shopper journeys, PT/EUR matrix and daily cumulative user limit: [[source-adyen-docs-payment-methods-mb-way]] and its pinned raw lines 23–36; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/flutter-drop-in/2026-09-15|MB WAY Flutter Drop-in guide, captured 2026-09-15]]
