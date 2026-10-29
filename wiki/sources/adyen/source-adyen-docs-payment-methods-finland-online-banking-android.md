---
title: "Online banking Finland for Android"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/android"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/android/2026-09-15.md"
tags: [adyen, finland-online-banking, android, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen Android page is an integration chooser for Online banking Finland. It points to Android Drop-in and Components child guides plus the four Sessions/Advanced base guides. It does not specify request fields, account eligibility, payment outcome or a complete Android implementation. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-finland-online-banking]] for method context.

## Key takeaways

- The Drop-in link presents the all-in-one UI route for the Android app. The Components link says InstantPaymentComponent handles the redirect. These are child-guide routes, not this page's full setup or result contract. See raw lines 19–27; follow [[source-adyen-docs-payment-methods-finland-online-banking-android-drop-in]] or [[source-adyen-docs-payment-methods-finland-online-banking-android-component]].
- The See also list routes to Android Drop-in and Components base integrations, each in Sessions and Advanced flows. Build the main integration before adding this method. See raw lines 29–36.
- Method availability, FI/EUR scope and bank-selection qualifications are in the linked overview; this Android chooser does not independently establish them. See [[source-adyen-docs-payment-methods-finland-online-banking]].

## Detail locators

- Android Drop-in and Components child routes: raw `How do you want to integrate?`, lines 19–27.
- Main integration prerequisites and four flow/UI routes: raw `## See also`, lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]
- [[source-adyen-docs-payment-methods-finland-online-banking-android-drop-in]]
- [[source-adyen-docs-payment-methods-finland-online-banking-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/android/2026-09-15|Online banking Finland Android chooser, captured 2026-09-15]]
