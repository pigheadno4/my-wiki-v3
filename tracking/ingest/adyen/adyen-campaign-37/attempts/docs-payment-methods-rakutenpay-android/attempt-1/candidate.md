---
title: "Rakuten Pay for Android"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/android"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/android/2026-09-15.md"
tags: [adyen, rakuten-pay, android, navigation]
---

## Overview

This 2026-09-15 Rakuten Pay for Android page is an integration chooser. It routes merchants to Android Drop-in or Components and says to establish the main Android integration before adding Rakuten Pay. It does not itself specify method setup, API fields, SDK versions, redirect implementation or payment outcomes. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The Drop-in route is described as an all-in-one UI solution for adding Rakuten Pay to an Android app. The Components route names `InstantPaymentComponent` as handling the redirect to Rakuten Pay. These are navigation descriptions, not instructions for handling the app return or final result. See raw lines 19–27.
- The See also section links four base paths: Android Drop-in and Components, each with Sessions and Advanced server-side flows. It says to create the main integration before adding Rakuten Pay. The linked guides carry their own prerequisites and behavior. See raw lines 29–36.

## Detail locators

- Integration chooser: raw lines 19–27.
- Main-integration prerequisite and four flow links: raw lines 29–36.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[source-adyen-docs-payment-methods-rakutenpay-android-drop-in]] — Android Drop-in child guide.
- [[source-adyen-docs-payment-methods-rakutenpay-android-component]] — Android Components child guide.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/android/2026-09-15|Rakuten Pay for Android (2026-09-15)]]
