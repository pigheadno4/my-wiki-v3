---
title: "Adyen UPI for Android chooser"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/android"
raw_files:
  - "adyen/docs/payment-methods/upi/android/2026-09-15.md"
tags: [adyen, upi, android, payment-methods, navigation]
---

## Overview

This [[adyen]] UPI for Android page is a **navigation chooser**. It links Drop-in and Components child guides and four main Android Sessions/Advanced integration routes. See [[adyen-online-payments]]. It does not provide child-specific SDK/API versions, UPI Intent/QR/Collect request fields, merchant eligibility, app-return behavior, webhook event contract or payment outcome. Those require the selected child and main guide. See raw lines 15–36.

## Routes and boundaries

- The page presents **Drop-in** as the all-in-one UI route and **Components** as using `UPIComponent` to handle a redirect to UPI. This is route description, not evidence of a completed redirect, shopper authorization or a working child integration. See raw lines 19–27.
- It says to follow the **applicable main integration guide**, then lists Android Drop-in/Components with both Sessions and Advanced flows. The list does not itself prove that every UPI child guide supports every flow, and it gives no minimum SDK or Checkout API version. See raw lines 29–36.
- The captured 2026-09-15 chooser provides no dated Collect migration rule or UPI AutoPay mandate conditions; those are separate UPI sources. It is not evidence of current payment-method enablement, a QR display/scan, authorization, capture, refund or settlement. See raw lines 15–36.

## Detail locators

- **Android chooser identity and purpose:** raw lines 15–17.
- **Drop-in and `UPIComponent` routes:** raw lines 19–27.
- **Four base integration links:** raw lines 29–36.

## Related

- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/upi/android-drop-in/2026-09-15|UPI Android Drop-in]] — child flow requirements and implementation detail.
- [[raw/adyen/docs/payment-methods/upi/android-component/2026-09-15|UPI Android Component]] — child flow requirements and implementation detail.
- [[raw/adyen/docs/payment-methods/upi/2026-09-15|UPI overview]] — broader method/Collect transition context, separate from this chooser.

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/android/2026-09-15|UPI for Android chooser — captured 2026-09-15]]
