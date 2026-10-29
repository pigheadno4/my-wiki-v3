---
title: "PaySafeCard Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/web-drop-in/2026-09-15.md"
tags: [adyen, paysafecard, web, drop-in, payments]
---

## Overview

This 2026-09-15 capture explains the PaySafeCard-specific additions to an existing Adyen Web Drop-in integration. It has distinct **Sessions flow** and **Advanced flow** instructions and points back to their main integration guides for common steps. It is an add-on rather than a complete standalone Drop-in implementation. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- In the **Sessions flow**, the guide requires an existing Web Drop-in Sessions integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and adding PaySafeCard in Customer Area. Its PaySafeCard-specific `/sessions` field is required `shopperReference`, a merchant reference uniquely identifying the shopper. See raw lines 25–46.
- In the **Advanced flow**, it requires an existing Web Drop-in Advanced integration, redirect handling, and Customer Area setup. Its PaySafeCard-specific `/payments` field is likewise required `shopperReference`. The Advanced requirements table does **not** itself state a Checkout API minimum version. See raw lines 294–326.
- Importing `Redirect` alongside AdyenCheckout and Dropin is optional when importing individual payment methods for tree shaking. The guide says the Advanced `/payments` response includes a redirect action; its example has `resultCode: RedirectShopper` and `action.paymentMethodType: paysafecard`. Handle the redirect through the relevant base integration. See raw lines 270–279, 306–315, and 613–627.
- Both flow sections give a 16-digit test code, direct readers to inspect test payments in Customer Area, and say to contact Support to add PaySafeCard in the **live Customer Area** before accepting live payments. This is a setup prerequisite, not proof of live enablement or a successful transaction. See raw lines 282–292 and 629–639.

> [!warning] Example scope
> The Sessions curl sample uses an app-style `adyencheckout://your.package.name` return URL even though this is a Web guide (raw lines 50–68); it is an example, not a universal Web return URL. The Advanced `/payments` request snippets focus on the additional shopper reference and omit an explicit payment method object (raw lines 330–611), while a separate response example shows the `paysafecard` redirect action. Use the linked main flow guide to complete the integration; do not treat these snippets as a complete copy-ready payment implementation.

> [!warning] Captured flow conflict and base link
> The linked PaySafeCard overview's capability table labels the payment flow **Direct** (overview raw lines 25–27), while this Web Drop-in child requires redirect handling in both Sessions and Advanced flows and shows an Advanced redirect action (child raw lines 35, 303, 613–627). These are conflicting labels in the two captured sources; this entry does not decide which describes current behavior. The Advanced base-integration requirement URL at child raw line 302 contains an unresolved platform-template parameter. Use this child's explicit Advanced Web Drop-in redirect-handling or make-payment links (lines 303, 322) to navigate to the base guide instead of relying on the malformed requirement URL.

## Detail locators

- Sessions prerequisites and `/sessions` addition: raw lines 25–46; example languages and SDK versions: lines 48–268.
- Optional Sessions `Redirect` import and test/live setup: raw lines 270–292.
- Advanced prerequisites, optional import, and `/payments` addition: raw lines 294–326; example languages and SDK versions: lines 328–611.
- Redirect action example and Advanced test/live setup: raw lines 613–639.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/web-drop-in/2026-09-15|PaySafeCard Web Drop-in, captured 2026-09-15]]
