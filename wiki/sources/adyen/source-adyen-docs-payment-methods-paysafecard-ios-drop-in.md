---
title: "PaySafeCard iOS Drop-in integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/ios-drop-in/2026-09-15.md"
tags: [adyen, paysafecard, ios, drop-in, redirect]
---

## Overview

This 2026-09-15-captured PaySafeCard iOS Drop-in page gives **method-specific additions** to existing Sessions and Advanced iOS Drop-in integrations. It relies on the main flow guides for base setup, and is not evidence of current account enablement, completed redirect handling, or successful live payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard overview]] for method-level scope.

## Key takeaways

- **Sessions flow:** requires an existing iOS Sessions Drop-in integration, **Checkout API v68 or later**, and PaySafeCard added in Customer Area. Its method-specific `/sessions` table marks `shopperReference` required as the merchant's unique shopper identifier. The guide says no additional PaySafeCard Drop-in configuration is needed (raw lines 25–44, 268–272).
- **Advanced flow:** requires an existing iOS Advanced Drop-in integration, **redirect handling** for `action.type: redirect`, and PaySafeCard added in Customer Area. Its method-specific `/payments` table also marks `shopperReference` required. The illustrated response has `resultCode: RedirectShopper` and a redirect action; method selection and base request handling remain in the main integration guide (raw lines 286–312, 599–613).
- Both flow sections give a **test-only 16-digit code**, tell merchants to check test payments in test Customer Area, and direct merchants to contact Support to add PaySafeCard in the **live** Customer Area before acceptance. Those are test/setup instructions, not proof of merchant enablement or a live transaction (raw lines 274–284, 615–625).

> [!warning] Direct versus redirect wording across captured pages
> The [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard overview]] matrix labels its flow **Direct** (overview pinned raw lines 25–27), whereas this iOS Drop-in child's Advanced requirements say `action.type: redirect` and its response example shows a redirect (child raw lines 292–296, 599–613). Preserve both and verify applicable behavior for the chosen integration; do not erase the child's redirect requirement based on the overview label.

> [!warning] Request examples are illustrative
> The Advanced `/payments` examples list amount, reference, return URL, merchant account and shopper reference but omit a `paymentMethod` object/type (raw lines 314–597); they do not form a complete PaySafeCard request recipe. The Advanced examples use a website `https://...` return URL despite this being an iOS guide, while Sessions examples use `adyencheckout://...` (raw lines 62, 330 and repeated library examples). Both curl snippets omit a continuation between `-X POST` and `-d` (raw lines 55–56, 323–324). Verify return routing with the selected iOS base guide and do not copy these snippets as complete commands.

## Detail locators

- Scope, Sessions requirements and `shopperReference` field: raw `# PaySafeCard iOS Drop-in` and `## Sessions flow Drop-in` lines 15–44.
- Sessions examples, no-extra-config and test/live: raw lines 46–284.
- Advanced requirements, no-extra-config and `shopperReference` field: raw `## Advanced flow Drop-in` lines 286–312.
- Advanced examples, redirect response and test/live: raw lines 314–625.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/ios-drop-in/2026-09-15|PaySafeCard iOS Drop-in guide, captured 2026-09-15]]
