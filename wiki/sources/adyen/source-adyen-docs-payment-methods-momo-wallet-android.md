---
title: "Adyen MoMo for Android chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/android"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/android/2026-09-15.md"
tags: [adyen, momo, android, payment-methods, navigation]
---

## Overview

This [[adyen]] MoMo for Android page is a **navigation chooser**. It links Android Drop-in and Components child guides and four corresponding main Android Sessions/Advanced integration guides. See [[adyen-online-payments]]. It does not itself specify MoMo request fields, SDK/API minimum, app-switch or return behavior, tokenization, live enablement or a final payment outcome. Those questions require the selected child and main guides. See raw lines 15–36.

## Routes and boundaries

- **Drop-in** links to an all-in-one UI route for MoMo on Android. **Components** links to a guide described as using `InstantPaymentComponent` to handle a redirect to MoMo. These are child-route descriptions, not evidence of a successful app handoff or completed payment. See raw lines 19–27.
- The “See also” section instructs readers to create the **main integration before adding MoMo** and lists Android Drop-in and Components base guides for Sessions and Advanced flows. The list does not prove every child supports every flow or establish the child's version/prerequisite details. See raw lines 29–36.
- The historical 2026-09-15 chooser alone does not establish current MoMo merchant/currency eligibility, authorization, capture, settlement or refund. See raw lines 15–36.

## Detail locators

- **Android purpose and method:** raw lines 15–17.
- **Drop-in versus `InstantPaymentComponent` routes:** raw lines 19–27.
- **Main integration prerequisite and four base routes:** raw lines 29–36.

## Related

- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/momo-wallet/android-drop-in/2026-09-15|MoMo Android Drop-in]] — child flow and method requirements; separate evidence.
- [[raw/adyen/docs/payment-methods/momo-wallet/android-component/2026-09-15|MoMo Android Component]] — child flow and method requirements; separate evidence.

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/android/2026-09-15|MoMo for Android chooser — captured 2026-09-15]]
