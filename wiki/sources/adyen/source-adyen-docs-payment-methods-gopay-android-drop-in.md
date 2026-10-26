---
title: "GoPay Android Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gopay/android-drop-in/2026-09-15.md"
tags: [adyen, gopay, android, drop-in, redirect, tokenization, recurring]
---

## Overview

This [[adyen]] guide adds GoPay to an existing Android Drop-in checkout using either Sessions or Advanced server-side flow. It also documents token creation and distinct later `Subscription` and `CardOnFile` requests. The token is delivered only after the initial payment settles and the recurring lifecycle webhook arrives. See [[adyen-online-payments]] and [[adyen-tokenization]]. This dated guide does not prove current merchant eligibility, a completed payment, or token issuance.

## Key takeaways

- **Sessions:** Requires an existing Android Drop-in Sessions integration with Checkout API v68 or later and GoPay added in Customer Area. The `/sessions` table marks `shopperInteractionDevice` and a relevant `channel` as required. It says no GoPay-specific Drop-in configuration is needed. Its example uses ID/IDR and `channel: Android`, but does not establish a general country/currency eligibility matrix. This Sessions section does not itself state a redirect prerequisite; use the linked base guide for action mechanics. See raw lines 25–77.
- **Advanced:** Requires an existing Android Drop-in Advanced integration, handling `action.type: redirect`, and Customer Area setup. It says no GoPay-specific configuration is needed. Its `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo`, and a relevant `channel` as required. The example response gives `RedirectShopper` and a redirect action, an intermediate handoff rather than final authorization. No Advanced Checkout API minimum or Android SDK release is specified here. See raw lines 364–439.
- **Create a token:** For a GoPay payment intended to create a recurring token, the page lists `storePaymentMethod: true`, a shopper-unique `shopperReference` of at least three characters, and `recurringProcessingModel` on `/payments`, with a server receiving recurring-token lifecycle webhooks. Only after the initial payment **settles** does the described `recurring.token.created` event carry `storedPaymentMethodId`. See raw lines 79–100 and 441–462.
- **Later payment models differ:** `Subscription` uses the stored method ID, shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription`, with final status reported by an `AUTHORISATION` webhook. `CardOnFile` also lists `ContAuth`, but explicitly requires a GoPay redirect for the shopper to enter a PIN, then `/payments/details` with `redirectResult` and a later final-status webhook. Do not treat the CardOnFile request label as proof that no shopper challenge occurs. See raw lines 102–114, 319–352, 464–476 and 681–714.
- **Test and live:** The guide tells merchants to contact Adyen Support for testing and consult GoPay's knowledge base. Live acceptance requires a separate GoPay request in the live Customer Area. No test or live outcome is shown here. See raw lines 354–362 and 716–722.

> [!warning] Android example has Web values and incomplete syntax
> The Advanced Android `/payments` example uses a website `returnUrl`, a Windows/Chrome `browserInfo` profile, and `channel: web` (raw lines 394–422), whereas the Sessions example uses an app-style return URL and `channel: Android` (raw lines 49–70). Both curl examples place `-d` after `-X POST` without a shell continuation and render structured device/browser data as quoted JSON-like strings. Later Subscription examples leave currency, method type and return URL blank. These cannot be copied as a proven Android request or used to override the stated channel requirement. The CardOnFile return instruction also says “back to your page” in this Android guide; treat it as generic return wording, not an Android return-URL contract. See raw lines 47–70, 116–317, 394–422, 478–679 and 709.

## Detail locators

- Sessions requirements/request and Advanced requirements/request/redirect response: raw lines 25–77 and 364–439.
- Token creation and settlement-gated webhook: raw lines 79–100 and 441–462.
- Subscription examples and final-status webhook: raw lines 102–325 and 464–687; CardOnFile shopper PIN, return/details and final webhook: raw lines 327–352 and 689–714.
- TEST Support and live Customer Area gates: raw lines 354–362 and 716–722.

## Related

- [[adyen-android-sdk]] — separately versioned native Drop-in architecture; this page pins no SDK version.
- [[adyen-tokenization]] — broader recurring-token lifecycle.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/android-drop-in/2026-09-15|GoPay Android Drop-in, 2026-09-15 snapshot]]
