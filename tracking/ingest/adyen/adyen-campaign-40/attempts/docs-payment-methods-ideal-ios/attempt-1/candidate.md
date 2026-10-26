---
title: "Adyen iDEAL | Wero iOS integration chooser"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/ios"
raw_files:
  - "adyen/docs/payment-methods/ideal/ios/2026-09-15.md"
tags: [adyen, ideal, wero, ios, drop-in, components]
---

## Overview

This 2026-09-15 captured Adyen page is an iOS integration chooser for iDEAL | Wero. It links separate Drop-in and Components child guides and four base iOS guides for the Sessions/Advanced and Drop-in/Components combinations. It contains no method setup, request, redirect, tokenization or result procedure; those details belong to the linked guides. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Drop-in option is described as Adyen's all-in-one UI route and links [[source-adyen-docs-payment-methods-ideal-ios-drop-in]]. The Components option links [[source-adyen-docs-payment-methods-ideal-ios-component]], but its description literally says "Use the None"; this apparent placeholder does not identify a component or establish any API behavior.
- The See also section says to create the main integration before adding iDEAL | Wero. It offers base integration links for iOS Drop-in with Sessions, iOS Components with Sessions, iOS Drop-in with Advanced, and iOS Components with Advanced. This chooser does not itself state SDK/API minimums, method eligibility, payment-state handling, or an executed outcome.

## Detail locators

- iOS scope and Drop-in/Components child choices, including the "None" wording: pinned raw lines 15–27.
- Base integration prerequisite and four Sessions/Advanced links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[source-adyen-docs-payment-methods-ideal-ios-drop-in]] — iOS Drop-in method guide
- [[source-adyen-docs-payment-methods-ideal-ios-component]] — iOS Components method guide

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/ios/2026-09-15|iDEAL | Wero iOS chooser, 2026-09-15]]
