---
title: "Online banking Slovakia Android Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/android-drop-in/2026-09-15.md"
tags: [adyen, online-banking-slovakia, android, drop-in, redirect]
---

## Overview

This 2026-09-15-captured, Android-titled Adyen guide adds **Online banking Slovakia to Drop-in**, splitting instructions between Sessions and Advanced server-side flows. It describes an optional Android configuration switch, required Advanced selected-bank issuer, and test/live setup. The Sessions prerequisite and request links point to **iOS** Drop-in despite the Android page title and Kotlin configuration example; verify the appropriate base Android integration guide before implementing. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-slovakia]] for method-level SK/EUR redirect and capability context.

## Key takeaways

- **Sessions flow** states that an existing Sessions Drop-in integration, Checkout API **v68 or later**, and Customer Area addition are required, but the linked integration and `/sessions` guides are explicitly `platform=iOS` (raw lines 23–38). The page says no additional `/sessions` parameters. Its optional Kotlin `onlineBankingSK` configuration has `setSubmitButtonVisible` to control submit-button visibility, and points to an **Android** configuration guide (raw lines 40–60). The mixed platform links should not be treated as a complete verified Android Sessions recipe.
- **Advanced flow** requires an existing **Android Drop-in** integration, `action.type: redirect` handling and Customer Area setup (raw lines 72–80). Its optional `setSubmitButtonVisible` configuration repeats the Kotlin `onlineBankingSK` example (raw lines 82–102).
- Advanced `/payments` must include `paymentMethod.issuer`, the issuing bank selected by the shopper (raw lines 104–112). Sample requests use `paymentMethod.type: onlineBanking_SK`, `issuer: cs`, EUR amount and `returnUrl` (raw lines 116–135, 261–289); `cs` is an example, not an exhaustive issuer list or proof of a merchant's current availability.
- The Advanced request examples cover curl and several SDK languages with test endpoint/environment and placeholder credentials. The Go sample labels library **v10.4.0** yet imports `/v9/` module paths; verify version-specific SDK syntax before reuse (raw lines 116–423, especially 291–300). Example idempotency-key placeholders are not an operational guarantee.
- The page says to test with real payment details and small amounts, check test status in test Customer Area **Payments > Payment list**, and add the method in Customer Area for live acceptance (raw lines 62–70, 426–432). These are captured instructions, not evidence of completed payment or live merchant entitlement.

## Detail locators

- Sessions requirement and iOS-linked base guides: raw `## Sessions flow Drop-in`, lines 23–38.
- Optional Android Kotlin submit-button configuration: raw lines 40–60.
- Advanced Android/redirect prerequisites and configuration: raw `## Advanced flow Drop-in`, lines 72–102.
- Required issuer and request samples: raw lines 104–423.
- Test/live instructions: raw lines 62–70 and 426–432.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/android-drop-in/2026-09-15|Online banking Slovakia Android Drop-in, captured 2026-09-15]]
