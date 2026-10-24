---
title: "Adyen Touch'n Go Android Component integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/android-component"
raw_files:
  - "adyen/docs/payment-methods/touchngo/android-component/2026-09-15.md"
tags: [adyen, touchngo, android, components, wallets]
---

## Overview

This [[adyen]] guide adds Touch'n Go to an **existing Android Components** Sessions or Advanced integration. It is expressly for **v5.0.0** (released October 2023), with a separate earlier-version guide. See [[adyen-online-payments]] and [[adyen-android-sdk]]. The pinned 2026-09-15 snapshot is not evidence of current availability, merchant enablement or an executed payment.

## Key takeaways

- Both tabs require the matching existing Android Components Sessions or Advanced flow at **minimum v5.0.0** and adding Touch'n Go in Customer Area before beginning. The page does not state a Checkout API minimum. Its title/body contain malformed/truncated `Touch''n Go` / `Add Touch` text, but the canonical path and full requirement context identify the method. See raw lines 15–39.
- For Sessions `/sessions` and Advanced `/payments`, the page says no **additional Touch'n Go-specific fields** are required. It likewise says no additional method-specific Component configuration in either flow. These statements are scoped to this method add-on; the linked base integration and its standard request/action requirements still apply. See raw lines 41–67.
- After base configuration, the Sessions tab links to creating a checkout session; the Advanced tab links to launching/showing the Component. This guide gives no detailed app-switch/return, `/payments/details`, QR lifecycle, webhook or final-outcome sequence. Showing a Component or submitting a request does not demonstrate successful authorization or settlement. See raw lines 61–79.
- The page says to check **test** payment status in test Customer Area and to contact Adyen Support to add Touch'n Go in the **live Customer Area** before live acceptance. A status lookup or Support addition is setup/observation, not proof of a particular transaction's success. See raw lines 69–73.

## Detail locators

- **v5.0.0 scope and earlier-version route:** raw lines 19–21.
- **Sessions/Advanced base and Customer Area prerequisites:** raw lines 23–39.
- **No extra request fields/configuration:** raw lines 41–67.
- **TEST payment list and live Support gate:** raw lines 69–73.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-touchngo]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/touchngo/android-component/earlier-versions/2026-09-15|Touch'n Go Android Component earlier versions]] — linked historical route; behavior separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/android-component/2026-09-15|Touch'n Go Android Component guide — captured 2026-09-15]]
