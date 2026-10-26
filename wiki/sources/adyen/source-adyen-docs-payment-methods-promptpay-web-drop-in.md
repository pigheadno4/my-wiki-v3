---
title: "PromptPay Web Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/promptpay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/promptpay/web-drop-in/2026-09-15.md"
tags: [adyen, promptpay, web, drop-in, thailand]
---

## Overview

This [[adyen]] page gives PromptPay-specific additions to an **existing Web Drop-in** integration, with separate Sessions and Advanced prerequisite tabs. Its method-specific work is Support-assisted Customer Area setup and, for Web Drop-in v6, an import of `PromptPay`. It leaves payment flow and results to the linked base guides. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-promptpay|PromptPay overview]] for the QR-only method and TH/THB scope. This 2026-09-15 snapshot does not establish current merchant eligibility or a successful payment.

## Key takeaways

- **Prerequisites:** The Sessions tab calls for an existing Web Drop-in Sessions integration; the Advanced tab calls for an existing Web Drop-in Advanced integration. Both say to contact Adyen Support to add PromptPay in Customer Area. This page does not state a Checkout API minimum or that Support has approved a given merchant. See raw lines 21–37.
- **Version and import:** Only **if using Web Drop-in v6**, the page says to import `AdyenCheckout` and `PromptPay` from `@adyen/adyen-web`. It separately says `/sessions` is the default endpoint with Drop-in v5.0.0 or later, while `/payments` applies to an additional use case. Those statements describe different integration contexts; the v6 import note is not a claim that v6 is the minimum supported version. See raw lines 39–52.
- **Method-specific request/configuration:** The page says no additional PromptPay fields and no PromptPay-specific Drop-in configuration steps are required. This assumes the existing integration's ordinary server requests and result handling; the page does not give a QR action contract or webhook decision table. See raw lines 47–56.
- **Testing and live gate:** The page instructs testing with real payment details and small amounts, checking test status in Customer Area, and contacting Support to add PromptPay in the live Customer Area before live acceptance. These are documented steps, not proof of a test result, absence of real-money effects, or live approval. See raw lines 58–64.

## Detail locators

- Sessions/Advanced base integration and Support setup: raw lines 21–37.
- Conditional v6 import, v5+ Sessions default, no extra method fields/configuration: raw lines 39–56.
- TEST and live instructions: raw lines 58–64. For QR display, return handling and final payment outcome, use the relevant child/base guides and webhook evidence.

## Related

- [[source-adyen-docs-payment-methods-promptpay]] — method overview and QR-only Adyen scope.
- [[adyen-webhooks]] — payment outcome context outside this short add-on.

## Raw Sources

- [[raw/adyen/docs/payment-methods/promptpay/web-drop-in/2026-09-15|PromptPay Web Drop-in, 2026-09-15 snapshot]]
