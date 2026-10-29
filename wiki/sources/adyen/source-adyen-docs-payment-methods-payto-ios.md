---
title: "PayTo for iOS"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/ios"
raw_files:
  - "adyen/docs/payment-methods/payto/ios/2026-09-15.md"
tags: [adyen, payto, ios, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen page is an **iOS integration chooser for PayTo**. It links to iOS Drop-in and PayToComponent child guides and to the corresponding main Sessions and Advanced integration guides. It is navigation, not a request-field, mandate-lifecycle or payment-outcome recipe. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-payto]] for the Australian PayTo agreement and payment context.

## Key takeaways

- The **Drop-in** route is described as the all-in-one iOS UI solution and links to the PayTo iOS Drop-in child guide (raw lines 19–23). Follow [[source-adyen-docs-payment-methods-payto-ios-drop-in]] for its flow-specific agreement and payment details.
- The **Components** route names PayToComponent and links to the PayTo iOS Component child guide (raw lines 25–27). Follow [[source-adyen-docs-payment-methods-payto-ios-component]] for implementation details; this chooser does not establish a Component version or field schema.
- The page says to establish the main integration first and links both Drop-in and Components under **Sessions and Advanced** iOS base flows (raw lines 29–36). Links alone do not prove a mandate was approved, payment reached a final state, or a merchant account is enabled.

## Detail locators

- Drop-in and PayToComponent chooser: raw `### How do you want to integrate?`, lines 19–27.
- Main integration prerequisite and four iOS base-guide routes: raw `## See also`, lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payto]]
- [[source-adyen-docs-payment-methods-payto-ios-drop-in]]
- [[source-adyen-docs-payment-methods-payto-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/ios/2026-09-15|PayTo iOS chooser, captured 2026-09-15]]
