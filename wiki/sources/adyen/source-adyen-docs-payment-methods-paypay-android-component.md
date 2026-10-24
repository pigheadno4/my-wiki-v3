---
title: "PayPay Android Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/android-component"
raw_files:
  - "adyen/docs/payment-methods/paypay/android-component/2026-09-15.md"
tags: [adyen, paypay, android, components, redirect]
---

## Overview

This 2026-09-15-modified and captured [[adyen]] PayPay guide gives **Android Components** additions for an existing integration, split by Sessions and Advanced server-side flow and routed through [[adyen-online-payments]]. It is a PayPay-specific supplement to linked main integration guides. Its redirect, simulator and component snippets do not establish current PayPay availability, a completed shopper return, authorization, capture or settlement.

## Key takeaways

- In the **Sessions flow**, prerequisites are existing Android Components Sessions integration, **Checkout API v68 or later**, existing handling for `action.type: redirect`, and adding PayPay in Adyen Customer Area. The page says no extra PayPay-specific `/sessions` parameters or configuration are needed. It imports `com.adyen.checkout:instant`, plus `components-compose` when using Jetpack Compose, and uses `InstantPaymentComponent` for method `paypay` obtained from the checkout session. Its Compose example requires a distinct key for a different screen/session or component reset.
- In the **Advanced flow**, prerequisites are an existing Android Components Advanced integration, handling the redirect additional action, and Customer Area addition. It uses the same `instant` module and optional Compose module, with method `paypay` selected from `/paymentMethods` response and `InstantPaymentComponent`; its example also requires a unique Compose key. It says no extra PayPay-specific configuration or `/payments` parameters. The v68+ Checkout API condition is stated in the Sessions table; this page does **not** state the same minimum in the Advanced table.
- Both TEST sections list two specific DGFT closed-loop acquirer accounts, one **AUTHFlow** and one **SALEFlow**, and say the shopper is redirected to a **DGFT simulator** without requiring the PayPay app. The guide points to TEST Customer Area Payment list to inspect test-transaction status; selecting a simulator account or seeing a redirect is not a final payment result.
- For LIVE integration, the page states that an **activated PayPay smartphone app** must be accessed through a **Japan local IP address**. It does not give a currency rule, PayPay-provider onboarding procedure, webhook result contract or post-redirect return processing steps here; those remain with the linked main flow/provider guidance. The old snapshot does not prove live merchant eligibility or successful processing.

## Detail locators

- [[raw/adyen/docs/payment-methods/paypay/android-component/2026-09-15|Pinned raw]], lines 15–42: purpose, Sessions prerequisites, Checkout API version, redirect and no-extra-session-parameters claim.
- Same raw, lines 44–126: Sessions imports, no extra configuration and Compose/XML `InstantPaymentComponent` examples.
- Same raw, lines 128–149: TEST simulator accounts, LIVE Japan IP/app condition and Advanced prerequisites.
- Same raw, lines 151–241: Advanced imports, no extra configuration, method source, component examples and no extra `/payments` parameters.
- Same raw, lines 243–254: repeated TEST simulator and LIVE app/IP statements.

## Related

- [[adyen-payment-method-variants]] — method-variant context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/android-component/2026-09-15|PayPay Android Component]]
