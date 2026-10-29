---
title: "Adyen Online banking Czech Republic Android Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/android-drop-in/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, android, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Czech Republic** to an existing Android Drop-in integration. It covers Sessions and Advanced flow prerequisites, method-specific request/configuration additions, and test/live guidance. It is a Drop-in add-on, not a complete integration or proof of current merchant enablement. See [[adyen]], [[adyen-online-payments]], and the separate CZ/CZK method overview [[source-adyen-docs-payment-methods-online-banking-czech-republic]].

## Key takeaways

- **Sessions:** start with an existing Android Drop-in Sessions integration using **Checkout API v68 or later** and add the method in Customer Area. The guide says **no additional parameters** are needed when creating the payment session. This means no method-specific additions in this Drop-in guide, not that the base `/sessions` request needs no fields. See raw lines 25–40.
- In Sessions, the optional `onlineBankingCZ { setSubmitButtonVisible(value) }` configuration controls submit-button visibility: set it to `false` to hide; the stated default is `true`. The row has no required mark. The displayed `CheckoutConfiguration(...)` is illustrative rather than a complete constructor. See raw lines 42–63.
- **Advanced:** start with an existing Android Drop-in Advanced integration, handle `action.type: redirect`, and add the method in Customer Area. The same optional submit-button configuration applies. The guide says **no additional parameters** are needed for the `/payments` request in this Drop-in flow. Its v68 API minimum appears only in the Sessions requirements. See raw lines 75–112.
- The separate API-only guide describes merchant-side bank issuer selection and includes `paymentMethod.type`/`issuer` in examples, while this Drop-in add-on says no additional request parameters. Keep the UI-mode scope separate: do not transfer the API-only example fields into this Drop-in guide as explicit requirements, or read the Drop-in sentence as a universal API schema rule. See raw lines 38–40 and 108–112, and [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]].
- For both flows, the page says to test with **real payment details and small amounts**, check test-payment status in Customer Area > Payments > Payment list, and add the method in Customer Area to accept live payments. These are instructions in the captured guide, not evidence that a payment was run, a merchant is enabled, or a redirect reached final authorisation. See raw lines 65–73 and 114–120.

## Detail locators

- Sessions prerequisites and absence of method-specific `/sessions` additions: raw lines 25–40.
- Sessions optional submit-button configuration: raw lines 42–63.
- Sessions test and live guidance: raw lines 65–73.
- Advanced prerequisites, optional configuration and absence of method-specific `/payments` additions: raw lines 75–112.
- Repeated test and live guidance: raw lines 114–120.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/android-drop-in/2026-09-15|Fully read Online banking Czech Republic Android Drop-in raw]]
