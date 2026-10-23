---
title: "Adyen Android card-payment integration chooser"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/android"
raw_files:
  - "adyen/docs/payment-methods/cards/android/2026-09-15.md"
tags: [adyen, cards, android, integration-navigation]
---

## Overview

This [[adyen]] Android card-payments page is a short **integration chooser**. It points developers to Drop-in, Components, or a custom card integration, with separate links to Android Sessions-flow Drop-in and Components guides. It describes the choices at a high level; it does not specify a complete payment flow, SDK/API version, prerequisite, merchant enablement, PCI scope, or successful transaction outcome. [[adyen-online-payments]]

## Key takeaways

- **Drop-in** is linked as an all-in-one card-payment UI for an Android app; **Components** is linked as a pre-built card Component. These are descriptions of child routes, not implementation or feature guarantees. See raw lines 19–27.
- The **Custom integration** link says to build the UI, collect shopper card details, and use Adyen modules to encrypt them. This is navigation to a separate guide, not an instruction to handle plaintext card data without assessing the child guide's card-data and PCI requirements. See raw lines 29–31.
- The closing links point to Android Drop-in and Components **Sessions-flow** integration guides. That navigation does not say every option or child guide uses Sessions, nor provide the steps of either guide. See raw line 33.

## Detail locators

- Integration-choice links and descriptions: raw lines 19–31.
- Additional Android Sessions-flow navigation: raw line 33.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/android/2026-09-15|Adyen Android cards integration chooser snapshot]]
