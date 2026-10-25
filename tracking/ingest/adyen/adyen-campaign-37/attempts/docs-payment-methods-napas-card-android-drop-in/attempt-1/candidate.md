---
title: "Napas card Android Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/napas-card/android-drop-in/2026-09-15.md"
tags: [adyen, napas-card, android, drop-in, online-payments]
---

## Overview

This 2026-09-15 guide adds Napas card to an existing Android Drop-in integration on its v5.0.0 guide path, with separate Sessions and Advanced server-side tabs. Earlier versions have a separate guide. This page gives method-specific setup and test scenarios, not a record of a successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Versioned prerequisites:** both Sessions and Advanced paths require an Android Drop-in integration at minimum version 5.0.0 and Napas card added in Customer Area. The page says it is for v5.0.0, released October 2023, and directs earlier versions elsewhere; it does not state a Checkout API version minimum. (raw lines 19–39)
- **Request and configuration additions:** the Sessions tab says Napas card needs no extra `/sessions` fields or Drop-in configuration; the Advanced tab says the same for `/payments`. The page then routes Sessions to checkout-session creation and Advanced to launching/showing Drop-in in the main guides. It does not state an action type, payment-method identifier, redirect return handling or final webhook sequence here. (raw lines 41–67)
- **TEST scenarios:** the page says to select any bank from its list and gives four test-card/one-time-password rows labeled successful, blocked card, insufficient funds and amount over limit. These are source-labeled test scenarios, not observed outcomes. Test payment status is checked in Customer Area Payment list. The exact test values remain in the pinned raw table. (raw lines 69–80)
- **Live gate and scope:** before live Napas acceptance, the page says to submit a request in the live Customer Area. This does not prove current enablement, card authorization, capture or settlement. This method-specific page gives no country/currency or issuer-eligibility rule; those require separate evidence. (raw lines 69–88)

## Detail locators

- v5.0.0 guide scope and earlier-version route: raw lines 19–21.
- Sessions/Advanced prerequisites and no extra fields/configuration: raw lines 23–59.
- Main-guide continuations: raw lines 61–67.
- Four test-card scenarios, status lookup and live request: raw lines 69–82.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-napas-card-android-drop-in-earlier-versions|Earlier-version Android Drop-in guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/android-drop-in/2026-09-15|Adyen Napas card Android Drop-in guide, 2026-09-15 snapshot]]
