---
title: "PaySafeCard Web Component integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/web-component"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/web-component/2026-09-15.md"
tags: [adyen, paysafecard, web, components, redirect]
---

## Overview

This 2026-09-15-captured PaySafeCard Web Component guide adds method-specific instructions to an **existing** Web Components integration, separately for Sessions and Advanced server-side flows. It depends on the main integration guides for the base flow. It does not establish current account enablement, a completed redirect, or a successful live payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard overview]] for method-level scope.

## Key takeaways

- **Sessions flow:** the guide requires an existing Sessions-flow Web Components integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and PaySafeCard added in Customer Area. It marks `shopperReference` required in the method-specific `/sessions` table to uniquely identify the shopper. It imports `Redirect`, says no extra PaySafeCard Component configuration is needed, and initializes the `Redirect` class (raw lines 25–47, 270–298).
- **Advanced flow:** the guide requires an existing Advanced-flow Web Components integration, redirect handling, and PaySafeCard in Customer Area. Its method-specific `/payments` table marks `shopperReference` required. The example response contains `resultCode: RedirectShopper` and `action.type: redirect`. The request examples include amount, return URL, reference, merchant account, and shopper reference but **omit a `paymentMethod` object/type**; do not treat these snippets as a complete payment request or infer a missing required field solely from the examples (raw lines 310–352, 354–637, 639–653).
- Both flow sections use a **test-only 16-digit code** and say to check test payments in the test Customer Area. For live acceptance, the page directs merchants to contact Support to add PaySafeCard in the live Customer Area; a test code or submitted request does not prove live enablement (raw lines 300–308, 655–663).

> [!warning] Direct versus redirect wording across captured pages
> The [[source-adyen-docs-payment-methods-paysafecard|PaySafeCard overview]] capability row labels the flow **Direct** (overview pinned raw lines 25–27), while this Web Component child requires `action.type: redirect`, uses a `Redirect` Component, and shows a redirect response (child raw lines 33–35, 290–298, 316–317, 639–653). Preserve both source statements and verify the applicable method/flow behavior before implementing; do not silently use the overview row to erase this child's redirect handling.

> [!warning] Illustrative snippets need verification
> Both Component snippets show `type:paysafecard` without quoting or defining `paysafecard` (raw lines 296–298, 340–342). The Sessions Web example uses the app-style return URL `adyencheckout://your.package.name` (lines 53–68), and both curl examples lack a continuation between `-X POST` and `-d` (lines 57–58, 363–364). The Advanced request examples omit `paymentMethod` (lines 354–637). These are not copy-ready Web payment recipes; follow the base guide and confirm the method data.

## Detail locators

- Scope and Sessions prerequisites/`shopperReference` table: raw `# PaySafeCard Web Component` and `## Sessions flow Component` lines 15–47.
- Sessions examples, import, configuration, initialization and test/live: raw lines 48–308.
- Advanced prerequisites, `shopperReference` table and request examples: raw `## Advanced flow Component` lines 310–637.
- Advanced redirect response and test/live: raw lines 639–663.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/web-component/2026-09-15|PaySafeCard Web Component guide, captured 2026-09-15]]
