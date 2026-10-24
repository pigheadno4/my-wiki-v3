---
title: "MoMo Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/android-drop-in/2026-09-15.md"
tags: [adyen, momo, android, drop-in, online-payments, recurring-payments]
---

## Overview

This [[adyen]] page, captured 2026-09-15, adds MoMo wallet to an **existing Android Drop-in** integration. It splits the method-specific additions by Sessions and Advanced server flows, and includes a separate recurring-token route and test/live guidance. It is not a full Android integration, a desktop-QR guide, or evidence of present merchant eligibility or successful authorization, capture, settlement or refund. See [[adyen-online-payments]] and raw lines 15–25.

## Key takeaways

- **Sessions Drop-in:** the page requires an existing Android Sessions Drop-in integration, **Checkout API v68 or later**, and adding MoMo in Customer Area. It states no additional MoMo-specific `/sessions` parameters or configuration. The Sessions requirements table does not separately specify redirect handling; the page points to the main integration guide for shared steps. See raw lines 19–46.
- **Advanced Drop-in:** the page requires an existing Android Advanced Drop-in integration, redirect handling for `action.type: redirect`, and adding MoMo in Customer Area. It states no additional MoMo configuration or base `/payments` parameters. Its Advanced requirements do **not** separately state the Sessions v68 minimum. The no-extra-parameter statement is for the base MoMo payment path; recurring-token requests below have additional fields. See raw lines 299–358.
- The recurring section says MoMo supports token-based future transactions. For initial token creation it specifies `storePaymentMethod: true` and a unique `shopperReference` in `/payments`, with a server able to receive recurring token lifecycle webhooks. It says `recurring.token.created`, carrying `storedPaymentMethodId`, is received **when the initial payment has settled**. This `/payments` wording also appears within the Sessions section; it is page wording, not proof that every Sessions integration directly calls `/payments`. Shopper-consent mechanics are not described here. See raw lines 48–71 and 321–344.
- For a later token payment, the page specifies `paymentMethod.storedPaymentMethodId` (or lookup through `/listRecurringDetails`), the same `shopperReference`, `shopperInteraction: ContAuth`, and a `recurringProcessingModel`: `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The cURL/language samples show `momo_wallet`, VND and TEST values as examples, not proof of a created token or successful later charge. The Java samples use `setRecurringDetailReference` instead of the prose's `storedPaymentMethodId`; review the applicable library/model before copying that example. See raw lines 73–139 and 346–412.
- The page directs testers to MoMo's test app and scenario-specific MoMo test credentials, then to payment status in Adyen's **test** Customer Area. It separately requires a request for MoMo in the **live** Customer Area before accepting live payments. Its test directions mention mobile-browser app download and desktop-browser QR scanning; those are test contexts, not a change of this page's Android Drop-in scope. Setup, redirect and test status lookup alone do not establish a final payment outcome. See raw lines 286–297 and 559–568.

## Detail locators

- Sessions prerequisites and no-extra-fields/configuration: raw lines 25–46.
- Sessions recurring fields, settlement-gated token webhook and sample requests: raw lines 48–283. The cURL path uses `/v68/payments`; the Java example uses `setRecurringDetailReference` (lines 128–130) versus the stated `paymentMethod.storedPaymentMethodId` (line 77).
- Test app, credentials, test Customer Area and live request after Sessions: raw lines 286–297.
- Advanced prerequisites, redirect, configuration/request statements and recurring route: raw lines 299–358.
- Advanced TEST examples and repeated test/live instructions: raw lines 360–568.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/android-drop-in/2026-09-15|MoMo Android Drop-in guide — captured 2026-09-15]]
