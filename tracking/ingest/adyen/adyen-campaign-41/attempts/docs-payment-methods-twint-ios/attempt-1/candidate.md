---
title: "Adyen TWINT iOS integration chooser"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/ios"
raw_files:
  - "adyen/docs/payment-methods/twint/ios/2026-09-15.md"
tags: [adyen, twint, ios, drop-in, components]
---

## Overview

This 2026-09-15 Adyen page is a TWINT iOS integration chooser. It links separate Drop-in and `TwintComponent` child guides, plus four main iOS integration routes covering Sessions/Advanced with Drop-in/Components. It does not itself give TWINT setup, request fields, redirect processing, tokenization or payment outcomes. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in choice is described as an all-in-one UI solution and links [[source-adyen-docs-payment-methods-twint-ios-drop-in]]. The Components choice names `TwintComponent` and links [[source-adyen-docs-payment-methods-twint-ios-component]]. The name alone is navigation, not proof of the child guide's initialization, version or runtime behavior.
- The page says to create the main integration before adding TWINT and supplies iOS Drop-in and Components links for both Sessions and Advanced flows. It does not establish merchant eligibility, country/currency limits, Checkout API or SDK versions, action types, recurring use or a successful payment; consult the selected child and main integration guide.

## Detail locators

- iOS scope and Drop-in/Components child choices: pinned raw lines 15–27.
- Main integration prerequisite and four Sessions/Advanced routes: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[source-adyen-docs-payment-methods-twint-ios-drop-in]] — iOS Drop-in child guide
- [[source-adyen-docs-payment-methods-twint-ios-component]] — iOS Component child guide

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/ios/2026-09-15|TWINT iOS chooser, 2026-09-15]]
