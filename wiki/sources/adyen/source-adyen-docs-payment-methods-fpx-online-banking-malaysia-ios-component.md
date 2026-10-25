---
title: "FPX Online Banking Malaysia iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/ios-component"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/ios-component/2026-09-15.md"
tags: [adyen, fpx, malaysia, ios, components, redirect, online-payments]
---

## Overview

This 2026-09-15-captured guide gives the FPX Online Banking Malaysia additions to an **existing iOS Components integration**, split by Sessions and Advanced server-side flows. It shows `InstantPaymentComponent` initialization and redirects, while deferring the main flow and outcome handling to the linked integration guides. It is a historical setup reference, not proof of current merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** requires an existing Sessions-flow iOS Components integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and FPX Online Banking Malaysia added in Customer Area. No extra `/sessions` parameters or method-specific configuration are stated. The Swift example obtains `molpay_ebanking_fpx_MY` from the session payment methods, creates `InstantPaymentComponent`, assigns the session as delegate, and initiates payment. A method-availability guard in the example is not proof that an account has this method enabled. (raw lines 25–70)
- **Advanced flow:** separately requires an existing Advanced-flow iOS Components integration, redirect handling and Customer Area setup. No extra method-specific configuration or `/payments` parameters are stated. Its Swift example selects `molpay_ebanking_fpx_MY`, initializes `InstantPaymentComponent`, assigns `self` as delegate, and initiates payment. The page gives no Advanced-flow Checkout API minimum; do not transfer the Sessions v68+ requirement without further authority. (raw lines 80–123)
- **Source link mismatch:** the Advanced integration-type row says **iOS Components** but links to an Advanced `integration=Drop-in` target; the redirect and payment links instead target Components. The row's label and link conflict and should not be treated as interchangeable integration evidence. (raw lines 86–90, 121–123)
- **Testing and live gate:** in both flow sections, the page says test using issuer IDs available to the Online Banking Malaysia Component for the relevant country/region, inspect test payment status in test Customer Area, and submit a separate request in **live Customer Area** before accepting live payments. It provides no issuer-ID list or observed test/live outcome. (raw lines 72–78, 125–131)

## Detail locators

- Sessions prerequisites, no-extra-parameter/configuration statements and initializer: raw lines 25–70.
- Advanced prerequisites, initializer, no-extra-parameter statement and link mismatch: raw lines 80–123.
- Test issuer-ID guidance, test status location and live request gate: raw lines 72–78, 125–131.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/ios-component/2026-09-15|Adyen FPX Malaysia iOS Component guide, 2026-09-15 snapshot]]
