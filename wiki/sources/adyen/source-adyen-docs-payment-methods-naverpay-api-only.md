---
title: "Adyen NaverPay API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/naverpay/api-only"
raw_files:
  - "adyen/docs/payment-methods/naverpay/api-only/2026-09-15.md"
tags: [adyen, naverpay, api-only, korea, redirect]
---

## Overview

This 2026-09-15 NaverPay guide adds method-specific steps to an **existing API-only Advanced flow** integration. It requires redirect handling (`action.type: redirect`) and NaverPay addition in Adyen Customer Area. The API-only form lists the available NaverPay method without collecting extra shopper information. It is a historical guide; configuration, a listed method or a redirect response is not proof of current merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- For `/paymentMethods` discovery, the page specifies `countryCode: KR` and `amount.currency: KRW`; its example response names NaverPay with type `kcp_naverpay`. This is a method-discovery example, not a guarantee that a given merchant will receive it. The curl examples target Adyen Checkout **v72 TEST**, while the page also displays versioned Java, PHP, .NET, Node, Go, Python and Ruby snippets; use the matching API/library version and environment instead of treating the snippets as universal code.
- The payment examples supply KRW amount, reference, return URL and merchant account, then show a `RedirectShopper` response with `action.type: redirect`, `method: GET` and a checkoutshopper TEST URL. The existing integration is responsible for the redirect/return handling linked by the prerequisite. This page does not spell out `/payments/details`, webhook processing or a final authorization/capture/settlement result.
- **Source conflict/incompleteness:** The 'How it works' list says the payment request includes additional information about the items the shopper intends to purchase, yet the `/payments` section says no additional parameters are needed. Its payment examples contain neither item details nor an explicit `paymentMethod`/`kcp_naverpay` field. The examples therefore should not be represented as a complete validated NaverPay request; verify against the core Advanced flow and current API contract before implementation. The form section separately says no additional *shopper information* is collected.
- The page says NaverPay has **no test environment** and recommends live testing with real details and small amounts. That coexists with Adyen Checkout TEST endpoint/examples and a TEST redirect URL in the guide: these illustrate Adyen request/redirect shapes, not a successful NaverPay sandbox payment. No live test or financial operation was performed.

## Detail locators

- Existing API-only, redirect and Customer Area prerequisites; flow and form: raw lines 19–44. Discovery KR/KRW fields: raw lines 46–53. TEST v72 `/paymentMethods` example, versioned library snippets and illustrative `kcp_naverpay` response: raw lines 55–342.
- Conflicting item-data prose versus no-extra-parameters statement: raw lines 33–36 and 344–346. TEST v72 `/payments` request shape and versioned snippets: raw lines 348–622. Redirect response: raw lines 624–638. No-NaverPay-test-environment statement: raw lines 640–642.

## Related

- [[adyen-online-payments]] — Advanced flow and server/client boundary context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/naverpay/api-only/2026-09-15|NaverPay API-only guide, captured 2026-09-15]]
