---
title: "PayPay Flutter Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/paypay/flutter-component/2026-09-15.md"
tags: [adyen, paypay, flutter, components, redirect]
---

## Overview

This 2026-09-15-modified and captured [[adyen]] PayPay page gives **Flutter Components** additions for an existing integration, split by Sessions and Advanced server-side flows and routed through [[adyen-online-payments]]. It states only PayPay-specific additions; its “no additional parameters/configuration” language does not waive the base Flutter integration requirements. Redirect and simulator instructions are not proof of shopper return, final authorization, capture or settlement.

## Key takeaways

- **Sessions flow** requires an existing Flutter Components Sessions integration, **Checkout API v68 or later**, pre-existing handling of `action.type: redirect`, and adding PayPay in Adyen Customer Area. It says no extra PayPay-specific `/sessions` parameters and no extra PayPay configuration. Its “Integration type” link unexpectedly targets `advanced-flow?platform=Flutter&integration=Drop-in`, while the redirect/create-session links target Sessions/Components; preserve the link mismatch instead of treating the linked Drop-in page as a Sessions Component instruction.
- **Advanced flow** requires an existing Flutter Components Advanced integration, redirect handling and Customer Area addition. The page says no extra PayPay configuration or `/payments` parameters. Its “Integration type” link also targets Flutter **Drop-in**, while the redirect/payment links target Flutter **Components**. The v68+ Checkout API condition appears only in the Sessions requirements table; no Flutter SDK version is stated here.
- Both TEST sections list DGFT closed-loop **AUTHFlow** and **SALEFlow** acquirer accounts. The page says the shopper is redirected to a **DGFT simulator** to complete the test transaction, with no PayPay app required, and points to TEST Customer Area Payment list for status inspection. These are testing instructions, not evidence that a particular transaction succeeded.
- For LIVE integration, the page states that an **activated PayPay smartphone app** must be accessed through a **Japan local IP address**. This source does not specify a currency, PayPay-provider onboarding steps, deep-link implementation, post-return/webhook outcome contract or any current merchant eligibility. Consult the linked main integration flow for base redirect/return requirements; no live payment is demonstrated here.

## Detail locators

- [[raw/adyen/docs/payment-methods/paypay/flutter-component/2026-09-15|Pinned raw]], lines 15–46: purpose, Sessions requirements and no-extra-PayPay-parameter/configuration claims, including mixed link targets.
- Same raw, lines 48–59: TEST DGFT accounts, simulator and LIVE app/Japan-local-IP condition.
- Same raw, lines 61–83: Advanced requirements, link targets and no-extra-configuration/`/payments` claims.
- Same raw, lines 85–96: repeated TEST/LIVE conditions for Advanced flow.

## Related

- [[source-adyen-docs-payment-methods-paypay-android-component]] — separate native Android Components supplement; not Flutter implementation authority.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/flutter-component/2026-09-15|PayPay Flutter Component]]
