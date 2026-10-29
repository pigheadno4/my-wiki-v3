---
title: "Online banking Poland Android Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/android-drop-in/2026-09-15.md"
tags: [adyen, online-payments, online-banking-poland, android, drop-in]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Online banking Poland for an existing Android Drop-in integration in Sessions or Advanced flow. It covers request additions, optional submit-button display, redirect handling in Advanced flow, and test/live setup. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-poland]] for the method overview. This snapshot does not prove current merchant entitlement or payment success.

## Key takeaways

- Sessions requires an existing Android Drop-in Sessions integration, Checkout API v68 or later, and Online banking Poland setup in Customer Area. The /sessions table marks shopperEmail required and limits it to 50 characters. Its PL/PLN 1000 and app-style returnUrl are sample values. See raw lines 25–67.
- Both flows show optional setSubmitButtonVisible configuration: false hides the submit button; true is the stated default. The table leaves its Required cell blank. See raw lines 268–287 and 308–327.
- Advanced requires an existing Android Drop-in Advanced integration, redirect handling for action.type redirect, and method setup. Its /payments table marks shopperEmail required with a 50-character maximum and lists paymentMethod.issuer for the selected bank without marking it required. The example uses type onlineBanking_PL, issuer 141, PLN 1000, and a web returnUrl; these are example values. The shown RedirectShopper response carries a redirect action, not a final paid outcome. See raw lines 298–339, 341–364 and 673–687.
- The page sends test-payment status checks to the test Customer Area Payment list and says live acceptance requires a request for Online banking Poland in the live Customer Area. See raw lines 290–296 and 689–693.

> [!warning] Example syntax
> Both Kotlin configuration snippets contain an extra anonymous brace block before setSubmitButtonVisible (raw lines 280–287 and 320–327). Treat the field description as the documented option and verify SDK syntax in the base Drop-in guide; the snippets are not complete executable recipes.

## Detail locators

- Sessions prerequisites and required shopperEmail: raw `## Sessions flow Drop-in`, lines 25–44.
- Sessions sample request and returnUrl: raw `## Add additional parameters to your /sessions request`, lines 38–67.
- Optional submit button configuration and snippet: raw `## Add additional configuration for Online banking Poland`, lines 268–287 and 308–327.
- Advanced prerequisites and fields: raw `## Advanced flow Drop-in`, lines 298–339.
- Advanced request example and redirect response: raw `## Add additional parameters to your /payments request`, lines 332–364, and lines 673–687.
- Test/live guidance: raw `## Test and go live`, lines 290–296 and 689–693.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/android-drop-in/2026-09-15|Online banking Poland Android Drop-in, captured 2026-09-15]]
