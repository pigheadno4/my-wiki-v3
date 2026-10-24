---
title: "Adyen Alipay overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay"
raw_files:
  - "adyen/docs/payment-methods/alipay/2026-09-15.md"
tags: [adyen, alipay, wallets, online-payments, payment-methods]
---

## Overview

This [[adyen]] Alipay overview, modified and captured 2026-09-15, describes high-level geographic scope, a 12-hour payment-offer window, a capability matrix and integration-route links. It says global merchants can offer Alipay for online stores/mobile apps and in-store overseas, but Adyen does **not** support processing Alipay payments within China. See [[adyen-online-payments]]. This historical overview does not establish current merchant eligibility or any completed authorization, capture or settlement. See raw lines 15–33 and 35–83.

## Key takeaways

- The overview's explicit region boundary is that Alipay is available only for merchants **selling outside China** and Adyen does not process Alipay payments **within China**. Its table labels countries `International` and currencies `Multiple`, without naming a specific supported country or currency. The broad labels do not override the explicit processing boundary or prove a particular account/currency is enabled. See raw lines 23–33.
- An initiated Alipay transaction's **offer stays open for 12 hours**, allowing shoppers up to that interval to complete payment. An open offer is not an authorization or final result. This overview supplies no redirect/return or webhook mechanics to determine outcome; use the selected integration guide for that flow. See raw lines 27–29 and 35–83.
- The matrix labels this as a wallet with `Payment flow: None`; marks recurring, separate capture, partial/multiple partial capture and chargebacks unavailable; and marks refunds, partial refunds and multiple partial refunds supported in this snapshot. These are overview capability marks rather than a capture/refund procedure, guaranteed account configuration or proof that an eligible payment was captured. The `None` matrix label does not itself establish that child web/mobile journeys have no shopper handoff. See raw lines 31–33.
- The page links Web, iOS, Android, React Native and Flutter pre-built UI paths; API-only for a merchant-built website/iOS/Android UI; Pay by Link; and in-person payments. These are routing choices, not child-guide prerequisites, SDK/API versions or evidence of live availability. See raw lines 35–83.
- The page gives large historical Alipay usage figures without a measurement date or method. Treat those as dated marketing context, not a current operational or market-size measurement. See raw line 23.

## Detail locators

- **Outside-China processing boundary and 12-hour offer:** raw lines 23–29.
- **Overview matrix for wallet type, region/currency labels, refunds and unsupported features:** raw lines 31–33.
- **Web/native/API-only/Pay by Link/in-person child routes:** raw lines 35–83.

## Related

- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/alipay/web/2026-09-15|Alipay Web chooser]] — linked child navigation; not evidence for this overview's implementation details.
- [[raw/adyen/docs/payment-methods/alipay/api-only/2026-09-15|Alipay API-only guide]] — linked child navigation; its request and outcome behavior remains separate authority.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/2026-09-15|Alipay overview — captured 2026-09-15]]
