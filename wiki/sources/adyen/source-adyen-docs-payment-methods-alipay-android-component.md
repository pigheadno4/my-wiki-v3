---
title: "Adyen Alipay Android Component guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/android-component"
raw_files:
  - "adyen/docs/payment-methods/alipay/android-component/2026-09-15.md"
tags: [adyen, alipay, android, component, wallets]
---

## Overview

This [[adyen]] guide adds Alipay to an **existing Android Components integration**, with separate Sessions and Advanced server-side flows and Jetpack Compose/non-Compose client examples. It describes method-specific additions, not a standalone integration or proof of current merchant eligibility, authorization, capture or settlement. It states no country or currency restriction on this page; use the main integration and applicable Alipay eligibility authority for those questions. [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites and server request:** Use an existing Sessions-flow Android Components integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and Alipay added in Customer Area. The guide says no **additional Alipay-specific** parameters are needed when creating `/sessions`; the main flow's request and redirect requirements still apply. See raw lines 23–42.
- **Advanced prerequisites and server request:** Use an existing Advanced-flow Android Components integration, redirect handling for `action.type: redirect`, and Alipay added in Customer Area. It says no additional Alipay-specific `/payments` parameters are needed. The Advanced requirement table does **not** restate the Sessions section's v68+ prerequisite as an Advanced-specific version rule. See raw lines 138–146 and 234–238.
- **Client Component:** Both flows import `com.adyen.checkout:instant:YOUR_VERSION`; Compose also imports `components-compose`. Both use `InstantPaymentComponent` and state no extra Alipay configuration parameters. Sessions obtains the `alipay` payment method from `checkoutSession`; Advanced selects `type == "alipay"` from the `/paymentMethods` response. Compose examples require a new unique key for a different screen or payment session. These are client setup/selection examples, not payment-result handling. See raw lines 44–125 and 148–232.
- **Live gate and outcome boundary:** The guide recommends live penny tests with an Alipay wallet app and viewing resulting payment details in the live Customer Area. Before accepting live Alipay payments it says to submit a request in the **live** Customer Area. It does not specify a final webhook, authorization result, capture, settlement or refund flow here; follow the linked main integration and lifecycle authorities for those states. See raw lines 128–136 and 240–248.

## Detail locators

- Sessions prerequisites, request and redirect links: raw lines 23–42.
- Sessions dependency, configuration and Compose/non-Compose launch: raw lines 44–125.
- Advanced prerequisites, dependency, configuration, Component and request: raw lines 138–238.
- Live testing recommendation and live Customer Area request, repeated for each flow: raw lines 128–136 and 240–248.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/android-component/2026-09-15|Adyen Alipay Android Component snapshot]]
