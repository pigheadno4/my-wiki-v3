---
title: "Adyen EPS Android Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/android-component"
raw_files:
  - "adyen/docs/payment-methods/eps/android-component/2026-09-15.md"
tags: [adyen, eps, android, components, sessions, advanced, redirect, recurring]
---

## Overview

This 2026-09-15 EPS Android Component add-on describes method-specific setup for existing Sessions and Advanced Android Components integrations, including the `EPSComponent` with or without Jetpack Compose. It delegates base redirect/action handling to the parent flow guides and describes future recurring payments through SEPA Direct Debit rather than repeated EPS redirects. The page is integration guidance, not proof of current method enablement or payment success. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-eps|the EPS overview]].

## Key takeaways

- The Sessions path requires an existing Sessions Android Components integration, Checkout API v68 or later, redirect handling for `action.type=redirect`, and EPS added in Customer Area. It states no EPS-specific additions to an ordinary `/sessions` request. The v68+ requirement appears in the Sessions requirement table; the separate Advanced table does not state an API minimum.
- The Advanced path requires an existing Advanced Android Components integration, additional-action handling for `action.type=redirect`, and EPS added in Customer Area. It likewise states no EPS-specific additions to an ordinary `/payments` request. These 'no additions' statements do not negate the later tokenization fields for recurring SEPA payments.
- Both paths import `com.adyen.checkout:eps`; with Compose they also import `components-compose`. Both use `EPSComponent`. Sessions examples select EPS from `checkoutSession` and pass that session to the provider, while Advanced examples select EPS from the `/paymentMethods` response and omit a session argument. Compose examples use a distinct component key when the screen/session changes; non-Compose examples attach to a view. `setSubmitButtonVisible` is optional, defaults true, and may be set false. The shown configuration snippets have doubled opening braces and a placeholder `value`, so they are illustrative rather than copy-ready Kotlin.
- The recurring section says EPS recurring transactions use SEPA Direct Debit. It strongly recommends explicit shopper permission and transparency on amount/schedule to reduce chargeback risk. For token creation it specifies `storePaymentMethod=true` and a shopper reference of at least three characters in `/payments` even under the Sessions section; after settlement, `recurring.token.created` provides `storedPaymentMethodId`, and the server must receive recurring-token lifecycle events. A later token `/payments` request uses `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. The page does not spell out a Sessions-specific token-creation request despite repeating this `/payments` recipe there.
- Test statuses can be checked in the test Customer Area. A live EPS request in live Customer Area is required before acceptance. Neither route proves availability or completion for a merchant; the capture has no test transaction evidence.

## Detail locators

- Page scope and flow split: pinned raw lines 15–25. Sessions prerequisites, v68+ and no additional ordinary session fields: lines 29–42. Sessions module imports, optional button configuration and Component examples: lines 44–142.
- Sessions SEPA recurring consent, `/payments` token creation, settlement webhook and future request fields: pinned raw lines 144–183. Test/live gates: lines 185–189.
- Advanced requirements and redirect action: pinned raw lines 191–199. Imports, optional button configuration and `EPSComponent` examples: lines 201–301. No additional ordinary `/payments` fields: lines 303–307. Repeated SEPA token recipe and test/live gates: lines 309–354. Configuration snippet brace/placeholder issue: lines 79–87 and 235–244.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-eps]] — method overview and capability marks

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/android-component/2026-09-15|EPS Android Component guide, captured 2026-09-15]]
