---
title: "Adyen Clearpay React Native Components integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/clearpay/react-native-component/2026-09-15.md"
tags: [adyen, clearpay, react-native, components, redirect, capture, refund]
---

## Overview

This 2026-09-15 Adyen Docs page adds Clearpay to an **existing React Native Components integration**. It explicitly says this Component does **not support Sessions flow** and gives an Advanced-flow path with Customer Area setup and redirect handling. Its GB/GBP test request and redirect example do not prove merchant eligibility, authorization, capture or live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Use an existing Advanced-flow React Native Components integration, with `action.type: redirect` handling and Clearpay added in Customer Area. The guide says no additional Clearpay configuration parameters are needed. The Advanced `/payments` example uses a v72 test endpoint; the page does not state an Advanced minimum Checkout API version (pinned raw lines 25–53, 66–69).
- The `/payments` table marks shopper name, email, reference (minimum three characters), country code, billing and delivery addresses and `lineItems` required; telephone number is optional. The example uses `paymentMethod.type: clearpay` and returns a `redirect` action with `RedirectShopper`, which is a shopper handoff, not a completed result (lines 55–64 and 75–144).
- Capture is automatic after authorization or manual depending on merchant-account configuration. Capture after sending goods requires delay or manual capture; partial capture requires manual capture. Clearpay says capture within 13 days after authorization. The first installment is charged during authorization; without timely capture, Clearpay cancels and refunds it. Test manual capture has a one-day limit (lines 146–156).
- Manual `/payments/{paymentPspReference}/captures` uses full or partial `amount.value`, with optional `lineItems`. A first partial capture cancels the unclaimed remainder unless Support enables multiple partial captures; each such capture creates a new invoice. Cancel before capture and refund after capture via `/payments/{paymentPspReference}/refunds`, with optional line items (lines 158–178).
- The guide includes a negative-line discount example and requires a Clearpay sandbox shopper account for testing, with a separate live Customer Area request before live acceptance. The discount example has the arithmetic and JSON problems below (lines 180–231).

> [!warning] Example and link inconsistencies
> The Advanced **Components** requirement links to an Advanced **Drop-in** base URL, while its redirect link names Components (raw lines 39–40). The discount prose says 1 GBP off Item #2, but its quantity-2 `-100` minor-unit line lowers the order total from 1000 to 800, a 2 GBP reduction; the sample also uses an ellipsis and omits a comma between item objects, so it is not copy-ready JSON (lines 182–214). The curl example lacks a line continuation after `-X POST` before `-d` (lines 73–74); verify shell syntax before use.

## Detail locators

- Sessions exclusion and Advanced prerequisites: pinned raw lines 25–47.
- Advanced fields, sample payment and redirect action: lines 49–144.
- Capture/refund, discount and test/live boundaries: lines 146–231.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-clearpay]] — GB/GBP method overview
- [[source-adyen-docs-payment-methods-clearpay-react-native-drop-in]] — separate React Native Drop-in guide

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/react-native-component/2026-09-15|Clearpay React Native Components guide, captured 2026-09-15]]
