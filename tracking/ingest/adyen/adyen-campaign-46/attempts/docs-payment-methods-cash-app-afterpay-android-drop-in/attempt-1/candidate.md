---
title: "Adyen Cash App Afterpay Android Drop-in v5.0.0"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/android-drop-in/2026-09-15.md"
tags: [adyen, cash-app-afterpay, android, drop-in, sessions, advanced]
---

## Overview

This 2026-09-15-captured guide adds Cash App Afterpay to an existing Android Drop-in integration, with Sessions and Advanced flow tabs. The page identifies itself as for **v5.0.0**, released in October 2023, and routes earlier versions to a separate guide. Its short scope does not establish current account eligibility, final payment success or live activation. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Both flow tabs require an existing Android Drop-in integration at **minimum v5.0.0** and Cash App Afterpay added in Customer Area. Sessions and Advanced base integrations are linked separately (pinned raw lines 21–39).
- For this Android Drop-in v5.0.0 guide, the Sessions `/sessions` request and Advanced `/payments` request require **no additional Cash App Afterpay-specific fields**. Both Drop-in configuration tabs likewise require no additional Cash App Afterpay-specific configuration. The guide then sends Sessions readers to create the checkout session and Advanced readers to launch and show Drop-in (lines 41–67). These statements concern method-specific additions; the linked base flow still supplies its own integration requirements.
- Testing needs an Afterpay sandbox shopper account for US and a test card. The page gives sandbox account steps and CVV values 000 and 051 for simulated authorised/refused outcomes. Live Cash App Afterpay acceptance requires submitting a request in the live Customer Area (lines 69–87). Test instructions do not demonstrate a live or successful merchant payment.

## Detail locators

- Version boundary, flow-specific prerequisites and Customer Area setup: pinned raw lines 15–39.
- Method-specific API/configuration requirements and next base-flow steps: lines 41–67.
- Sandbox account/card tests and live request: lines 69–87; related base guide/webhook/API routes: lines 89–93.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-cash-app-afterpay]] — method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/android-drop-in/2026-09-15|Cash App Afterpay Android Drop-in v5.0.0 guide, captured 2026-09-15]]
