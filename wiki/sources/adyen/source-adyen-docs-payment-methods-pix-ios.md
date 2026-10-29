---
title: "Pix for iOS"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/ios"
raw_files:
  - "adyen/docs/payment-methods/pix/ios/2026-09-15.md"
tags: [adyen, pix, ios, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen page is an **iOS integration chooser for Pix**. It links to iOS Drop-in and InstantPaymentComponent child guides and to the corresponding main Sessions and Advanced integration guides. It is navigation, not a request-field, QR-expiration or payment-status recipe. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-pix]] for the Brazil/BRL method context.

## Key takeaways

- The **Drop-in** route is described as the all-in-one iOS UI solution and links to the Pix iOS Drop-in child guide (raw lines 19–23). Follow [[source-adyen-docs-payment-methods-pix-ios-drop-in]] for its flow-specific QR and request details.
- The **Components** route names InstantPaymentComponent and links to the Pix iOS Component child guide (raw lines 25–27). Follow [[source-adyen-docs-payment-methods-pix-ios-component]] for implementation details; this chooser does not establish a Component version or field schema.
- The page says to establish the main integration first and links both Drop-in and Components under **Sessions and Advanced** iOS base flows (raw lines 29–36). These links do not prove QR expiry behavior, final payment, or current merchant enablement.

## Detail locators

- Drop-in and InstantPaymentComponent chooser: raw `### How do you want to integrate?`, lines 19–27.
- Main integration prerequisite and four iOS base-guide routes: raw `## See also`, lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pix]]
- [[source-adyen-docs-payment-methods-pix-ios-drop-in]]
- [[source-adyen-docs-payment-methods-pix-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/ios/2026-09-15|Pix iOS chooser, captured 2026-09-15]]
