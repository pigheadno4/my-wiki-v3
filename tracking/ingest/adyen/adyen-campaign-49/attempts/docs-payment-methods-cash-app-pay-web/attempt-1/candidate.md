---
title: "Adyen Cash App Pay Web integration router"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/web"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/web/2026-09-15.md"
tags: [adyen, cash-app-pay, web, integration-router, online-payments]
---

## Overview

This 2026-09-15-captured Adyen page is a short Web integration router for **Cash App Pay**. Its metadata records a 2019-10-08 last-modified timestamp. It links a method-specific Web Drop-in guide, a Web Component guide, and general Web UI guides. It does not specify request fields, client/server flow, eligibility, or payment outcomes. Cash App Pay is distinct from Cash App Afterpay. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Method-specific UI routes:** The page describes Web Drop-in as an all-in-one UI solution for Cash App Pay and links a Web Component as another UI route. These link descriptions provide navigation, not verified child-guide behavior or a payment result. [Raw: lines 19–27]
- **General Web routes:** It also points to general Web Drop-in and Components guides. This router does not state a Sessions/Advanced choice, SDK or Checkout API version, redirect handling, account setup, capture, chargeback, or test/live procedure. Read the linked method child guides for implementation detail. [Raw: lines 21–29]
- **Overview route:** The separately approved [[source-adyen-docs-payment-methods-cash-app-pay]] overview supplies method-level US/USD and capability context, including conditions around authorization adjustment and chargebacks. It also preserves a Direct overview versus API-only redirect/subtype label distinction. Those claims do not come from this Web router; this page is not evidence for Cash App Afterpay behavior. [Raw: lines 15–29]

## Detail locators

- Capture and last-modified metadata: pinned raw lines 1–13.
- Web Drop-in and Component child links: pinned raw lines 15–27.
- General Web UI links: pinned raw line 29.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-cash-app-pay]] — approved Cash App Pay overview for method-level facts, distinct from Cash App Afterpay.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/web/2026-09-15|Cash App Pay Web router, captured 2026-09-15]]
