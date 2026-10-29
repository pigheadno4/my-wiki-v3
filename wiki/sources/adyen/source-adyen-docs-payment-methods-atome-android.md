---
title: "Adyen Atome Android integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/android"
raw_files:
  - "adyen/docs/payment-methods/atome/android/2026-09-15.md"
tags: [adyen, atome, android, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen page is an Android Atome integration chooser. It routes readers to Android Drop-in or Components method guides and to the main Sessions/Advanced integration guides. It contains no request schema, eligibility rule, payment outcome or live setup procedure. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in child is described as Adyen's all-in-one UI option for adding Atome to an Android app (pinned raw lines 19–23).
- The Components child is described as using `InstantPaymentComponent` to handle the redirect to Atome (lines 25–27). That sentence is a route description; the child guide owns implementation details.
- The page instructs readers to create the main integration before adding Atome, linking Android Drop-in and Components guides for both Sessions and Advanced flows (lines 29–36).

## Detail locators

- Android chooser identity and Drop-in/Components child links: pinned raw lines 15–27.
- Main integration prerequisite and four Sessions/Advanced routes: lines 29–36.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-atome-android-drop-in]] — Android Drop-in child
- [[source-adyen-docs-payment-methods-atome-android-component]] — Android Components child

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/android/2026-09-15|Atome Android chooser, captured 2026-09-15]]
