---
title: "Adyen Online banking Slovakia iOS Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/ios-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/ios-component/2026-09-15.md"
tags: [adyen, online-banking-slovakia, ios, components, redirect]
---

## Overview

This 2026-09-15-captured, **iOS-titled** Online banking Slovakia method add-on describes Sessions and Advanced Components paths, bank issuer selection, redirect handling and test/live setup. Its body mixes Android prerequisites and Kotlin configuration with Swift Component snippets, so it is not a complete, internally consistent iOS implementation recipe. The [[source-adyen-docs-payment-methods-online-banking-slovakia|method overview]] identifies an SK/EUR bank-redirect method; the guide's sample EUR request does not establish current merchant eligibility or a successful payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions as written:** The requirements row asks for an existing **Android Components Sessions** integration, Checkout API **v68 or later**, redirect handling, and addition of Online banking Slovakia in Customer Area. It says no extra method parameters for `/sessions`. The section then gives a nonrequired `setConfig` row with placeholder “value,” a Kotlin `Configuration.Builder` fragment, and a Swift `OnlineBankingComponent` example using `InstantPaymentMethod` with an empty `configuration:` argument. These are captured fragments, not a validated iOS configuration contract (raw lines 25–89).
- **Advanced as written:** The requirements again name **Android Components**, require redirect handling and Customer Area addition, but print “Checkout API v or later” with the version missing. Do not extend the Sessions v68 minimum to Advanced from this page. The prose says no additional Online banking Slovakia configuration parameters, while the Swift initializer still leaves `configuration:` empty (raw lines 99–137).
- **Advanced payment request:** The `/payments` table marks `paymentMethod.issuer` required as the bank the shopper selected. Test examples use `paymentMethod.type: onlineBanking_SK`, issuer `cs`, EUR 1000 minor units and an HTTPS `returnUrl`; these are sample values, not an exhaustive bank list or iOS return-route specification. The source gives no local final-result procedure beyond its redirect requirement and linked base guides (raw lines 139–459).
- **Testing and live setup:** Both flow sections say to test using real payment details and small amounts, check test payment status in the test Customer Area, and add the method in Customer Area to accept live payments. These are source instructions, not evidence of a completed test, live enablement, or current availability (raw lines 91–97, 461–467).

> [!warning] Mixed platform and incomplete examples
> Despite the iOS title and Swift `OnlineBankingComponent` snippets, the Sessions and Advanced requirement links and redirect links select **Android** (raw lines 33–35, 107–109); the Sessions configuration example is **Kotlin** (lines 56–67). The Swift initializers leave `configuration:` blank (lines 77–89, 126–137). The Sessions `setConfig(value)` row is a placeholder with no required mark (lines 48–67), while Advanced says no additional method configuration (line 116). The Advanced minimum-version row omits its version (line 108). Use the appropriate iOS base integration and active SDK/API contract before applying any of these fragments; do not turn Android snippets or the blank minimum into iOS requirements.

## Detail locators

- Sessions prerequisites, no extra request field, placeholder configuration and Swift initializer: pinned raw lines 25–89.
- Sessions test/live statements: raw lines 91–97.
- Advanced prerequisites, blank version and no-extra-configuration statement: raw lines 99–137.
- Required issuer and TEST payment examples: raw lines 139–459.
- Repeated test/live statements: raw lines 461–467.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]] — method overview for SK/EUR and bank redirect.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/ios-component/2026-09-15|Online banking Slovakia iOS Component guide, captured 2026-09-15]]
