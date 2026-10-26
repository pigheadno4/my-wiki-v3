---
title: "Swish for Android"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/android"
raw_files:
  - "adyen/docs/payment-methods/swish/android/2026-09-15.md"
tags: [adyen, swish, android, online-payments, integration-chooser]
---

## Overview

This 2026-09-15 Adyen page is an Android Swish integration chooser. It links Android Drop-in and Components child guides and the four main Android Sessions/Advanced guides. It gives no complete request flow, API/SDK version, method eligibility or payment outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in route is described as Adyen's all-in-one UI solution; the Components route points to `InstantPaymentComponent` and says it handles a redirect to Swish (raw lines 19–27). These are route descriptions, not the child guides' detailed action-type or return-handling rules.
- The page says to build the main integration first, then links Android Drop-in and Components base guides for both Sessions and Advanced server-side flows (lines 29–36). It does not claim the same configuration or request fields for all four choices.
- The chooser supplies neither setup/merchant approval details nor test/live steps. Follow the linked child and base guides for implementation and verify merchant availability separately; this snapshot alone does not establish current enablement or a successful payment.

## Detail locators

- Drop-in child route: raw lines 19–23.
- Components child route and its high-level redirect wording: raw lines 25–27. That wording alone does not determine `action.type`; consult the child integration guide for action handling.
- Four base Android Sessions/Advanced routes: raw lines 29–36.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/android/2026-09-15|Swish Android chooser, fetched 2026-09-15]]
