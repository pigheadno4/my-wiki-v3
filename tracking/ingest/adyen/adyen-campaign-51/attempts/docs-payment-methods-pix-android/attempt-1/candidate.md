---
title: "Pix for Android"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/android"
raw_files:
  - "adyen/docs/payment-methods/pix/android/2026-09-15.md"
tags: [adyen, pix, android, integration-chooser]
---

## Overview

This 2026-09-15-captured Adyen page is an **Android integration chooser for Pix**. It links to Android Drop-in and InstantPaymentComponent child guides and to the corresponding main Sessions and Advanced integration guides. It is navigation, not a request-field, QR-action or payment-status recipe. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-pix]] for the Brazil/BRL method context.

## Key takeaways

- The **Drop-in** route is described as the all-in-one Android UI solution and links to the Pix Android Drop-in child guide (raw lines 19–23). Follow [[source-adyen-docs-payment-methods-pix-android-drop-in]] for actual flow-specific QR and request details.
- The **Components** route names InstantPaymentComponent and links to the Pix Android Component child guide (raw lines 25–27). Its short chooser description says “handle the redirect to Pix,” whereas the approved child source [[source-adyen-docs-payment-methods-pix-android-component]] describes an Advanced qrCode action. Treat the chooser phrase as navigation wording, not evidence that redirect handling alone implements the Pix QR action.
- The page says to establish the main integration first and links both Drop-in and Components under **Sessions and Advanced** Android base flows (raw lines 29–36). Those links do not prove QR expiry behavior, final payment, or current merchant enablement.

> [!warning] Chooser wording
> The Components teaser says “redirect to Pix” (raw line 27), while the linked method guide identifies qrCode handling. Verify the child integration guide rather than treating the teaser as an action-type specification.

## Detail locators

- Drop-in and InstantPaymentComponent chooser: raw `### How do you want to integrate?`, lines 19–27.
- Main integration prerequisite and four Android base-guide routes: raw `## See also`, lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pix]]
- [[source-adyen-docs-payment-methods-pix-android-drop-in]]
- [[source-adyen-docs-payment-methods-pix-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/android/2026-09-15|Pix Android chooser, captured 2026-09-15]]
