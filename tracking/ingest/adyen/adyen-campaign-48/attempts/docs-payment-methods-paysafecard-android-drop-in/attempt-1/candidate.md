---
title: "Adyen PaySafeCard Android Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/android-drop-in/2026-09-15.md"
tags: [adyen, paysafecard, android, drop-in, redirect]
---

## Overview

This 2026-09-15-captured [[adyen]] guide describes the PaySafeCard-specific additions to an existing Android Drop-in integration, separately for Sessions and Advanced server flows. It gives request additions, redirect handling and test/live setup; the linked base guides own the complete integration. It does not establish current merchant eligibility or a successful live payment. See [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-paysafecard|method overview]].

## Key takeaways

- **Sessions:** Start from an existing Android Sessions Drop-in integration using Checkout API v68 or later and add PaySafeCard in Customer Area. The `/sessions` parameter table marks `shopperReference` required as the merchant's unique shopper reference, such as a user or account ID. Its v71 example uses EUR 1000 minor units, `countryCode: NL` and an Android app-scheme `returnUrl`; those are example values rather than general eligibility or return-route rules (raw lines 25–67).
- **Advanced:** Start from an existing Android Advanced Drop-in integration configured to handle `action.type: redirect`, and add PaySafeCard in Customer Area. This section states no Checkout API minimum. Its `/payments` table also marks `shopperReference` required. The sample response has `resultCode: RedirectShopper` and a redirect action, an intermediate shopper step rather than final payment success (raw lines 286–310, 597–611).
- **Drop-in configuration:** Both flow sections say no additional PaySafeCard configuration parameters are needed (raw lines 268–272, 296–300).
- **Testing and live setup:** The guide provides test code `0000 0000 0990 3417`, directs test status checks to the test Customer Area, and says to contact Adyen Support to add PaySafeCard in the live Customer Area before accepting live payments. The displayed Support URL points to the test Customer Area; these steps do not prove live enablement (raw lines 276–284, 613–621).

> [!warning] Source examples and flow labels
> The Advanced `/payments` request examples include `shopperReference` but omit a `paymentMethod` object (raw lines 316–595); treat them as additions to the linked base Advanced flow, not complete executable requests. Several Sessions SDK snippets omit construction of `createCheckoutSessionRequest` (raw lines 69–265), and both curl samples put `-X POST` on a line without a continuation before `-d` (raw lines 50–67, 316–332). The Sessions sample uses an app-scheme return URL while the Advanced sample uses HTTPS; use the corresponding base Android return handling. The [[source-adyen-docs-payment-methods-paysafecard|method overview]] marks the method's payment flow “Direct,” whereas this child guide requires an Advanced redirect action; preserve both captured descriptions without assuming the redirect is absent.

## Detail locators

- Sessions prerequisites, `/sessions` field and examples: raw `## Sessions flow Drop-in` lines 25–265.
- Sessions configuration and test/live: raw lines 268–284.
- Advanced prerequisites, `/payments` field and examples: raw `## Advanced flow Drop-in` lines 286–595.
- Redirect response and repeated test/live steps: raw lines 597–621.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]] — method overview and captured country/currency and capability tables.
- [[source-adyen-docs-payment-methods-paysafecard-android-component]] — separate Android Components route.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/android-drop-in/2026-09-15|PaySafeCard Android Drop-in guide, captured 2026-09-15]]
