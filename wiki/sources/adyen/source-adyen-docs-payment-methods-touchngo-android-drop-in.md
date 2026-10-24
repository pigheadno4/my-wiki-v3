---
title: "Adyen Touch 'n Go Android Drop-in v5 guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/touchngo/android-drop-in/2026-09-15.md"
tags: [adyen, touchngo, android, drop-in]
---

## Overview

This [[adyen]] page describes adding **Touch 'n Go** to an existing **Android Drop-in** integration. It says this guide is for **v5.0.0**, released in **October 2023**, and directs users of earlier versions to a separate guide. It has distinct **Sessions** and **Advanced** server-side tabs, each stating a **5.0.0 minimum** for the Android Drop-in integration. It is a method add-on and does not itself document shopper redirect, return processing, webhook status, or a final payment outcome. [[adyen-online-payments]]

## Key takeaways

- **Version and setup:** Both Sessions and Advanced prerequisite rows call for the respective existing Android Drop-in integration at minimum **5.0.0**, then instruct adding Touch 'n Go in Customer Area. The raw page has malformed apostrophes (`Touch''n Go`) in several setup and request sentences; that typography does not establish a distinct method. Earlier versions route to the separate earlier-version guide. See raw lines 19–39.
- **Base requests and Drop-in configuration:** For Sessions `/sessions` and Advanced `/payments`, the page says no **additional Touch 'n Go-specific fields** are needed. Both tabs likewise say no extra method configuration; they point back to their main integration guides to create the checkout session or launch Drop-in. These statements do not remove ordinary base request/configuration requirements. See raw lines 41–67.
- **Status/live boundary:** The page points to a TEST Customer Area payment list and says to contact Adyen Support to add Touch 'n Go in **live Customer Area** before live acceptance. Its Webhooks link is navigation only; no on-page redirect/details/webhook result sequence or approval proof is given. See raw lines 69–79.

## Detail locators

- Version statement, separate earlier-version route and flow prerequisites: raw lines 19–39.
- Base request/configuration scope and main-guide handoff: raw lines 41–67.
- TEST status, live Support gate and related links: raw lines 69–79.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-touchngo-android-drop-in-earlier-versions]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/android-drop-in/2026-09-15|Adyen Touch 'n Go Android Drop-in snapshot]]
