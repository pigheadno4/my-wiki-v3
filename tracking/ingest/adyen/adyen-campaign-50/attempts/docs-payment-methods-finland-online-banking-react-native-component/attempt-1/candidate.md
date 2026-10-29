---
title: "Adyen Online banking Finland React Native Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/react-native-component/2026-09-15.md"
tags: [adyen, finland-online-banking, react-native, component, paytrail, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online banking Finland to a React Native Components integration. It explicitly excludes Sessions flow, then describes Advanced-flow redirect, method-specific request fields, sample redirect response, and Paytrail test guidance. It supplements [[adyen-online-payments]] and does not show a completed payment or current merchant enablement. [[adyen]]

## Key takeaways

- **Flow scope:** The page states that React Native Components **do not support Sessions flow**. Its supported route here is an existing Advanced-flow React Native Components integration with redirect handling for `action.type: redirect` and Online banking Finland added in Customer Area. No method-specific configuration parameters are needed. The Advanced integration-type row's link points to a **Drop-in** base URL despite saying Components, while the redirect and payment links point to Components; treat that link as a navigation mismatch, not as a switch to Drop-in. The page states no Checkout API minimum. [Raw: lines 25–53]
- **Advanced request fields:** The method-specific `/payments` table marks `paymentMethod.type: ebanking_FI` and `shopperEmail` required. It says `paymentMethod.issuer` is relevant and required **only for the Issuer redirect flow**. Its `returnUrl` row is unmarked, with a stated maximum of 1024 characters. The EUR amount 1000 and HTTPS return URL shown in examples are illustrations. [Raw: lines 49–80]
- **Incomplete request examples:** All displayed curl and language-library `/payments` request samples omit `paymentMethod` despite the table's required type. They also use `s.hopper@@example.com`, a malformed double-`@` placeholder. The curl block lacks a continuation after `-X POST` before `-d`, and the Node snippets reference `Config`/`EnvironmentEnum` without shown imports. Do not copy these as complete runnable payment requests. The language-library version labels and `liveEndpointUrlPrefix` comments are sample-scoped, not an established API minimum. [Raw: lines 64–345]
- **Redirect and result:** The example response has `resultCode: RedirectShopper`, a GET `action.type: redirect`, `paymentMethodType: ebanking_FI` and an action URL. This is an intermediate redirect, not final authorization. The child page does not give a return/details or webhook result sequence. [Raw: lines 347–361]
- **Test/refund boundary:** Before live acceptance, the page instructs testing with Paytrail's test environment and sample data. It says **testing multiple partial refunds is currently not available**. The separately approved [[source-adyen-docs-payment-methods-finland-online-banking]] overview checks multiple partial refunds but has a missing “See note” qualification; do not recast the child test limitation as proof of live refund support or impossibility. [Child raw: lines 363–367; overview raw: lines 34–36]

> [!WARNING] Required type is missing from every sample request
> The table requires `paymentMethod.type: ebanking_FI` (raw line 57), but the curl and all language examples omit `paymentMethod` (raw lines 66–345). The example email is malformed. The prose/table requirements, not these incomplete snippets, should guide a complete request.

## Detail locators

- Unsupported Sessions flow, Advanced prerequisites and link mismatch: pinned raw lines 25–47.
- Required and conditional fields: pinned raw lines 49–60.
- Incomplete test-environment request examples: pinned raw lines 62–345.
- Redirect response and Paytrail test limitation: pinned raw lines 347–367.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-finland-online-banking]] — approved Paytrail/FI/EUR overview and separate bank-selection/refund-note caveats.

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/react-native-component/2026-09-15|Online banking Finland React Native Component guide, captured 2026-09-15]]
