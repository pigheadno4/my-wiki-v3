---
title: "BLIK Android Component integration | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/android-component"
raw_files:
  - "adyen/docs/payment-methods/blik/android-component/2026-09-15.md"
tags: [adyen, blik, android, components, sessions, advanced-flow]
---

## Overview

This Adyen BLIK Android Components add-on is explicitly for v5.0.0, released in October 2023, and sends earlier-version users to a separate guide. It covers both Sessions and Advanced server-side flows in an existing Android Components integration. Each flow lists a 5.0.0 minimum and BLIK added in Customer Area, then delegates session creation or Component launch to the corresponding base integration guide (raw lines 15–39, 61–67).

## Key takeaways

- In the Sessions path, BLIK needs no additional fields in `/sessions` and no BLIK-specific Component configuration. In the Advanced path, it needs no additional fields in `/payments` and no BLIK-specific Component configuration. These are method-specific add-on statements; the base flow's ordinary request and action requirements remain in the linked guides (raw lines 41–67).
- For BLIK-with-code TEST, the page names code `999000`, BLIK guideline compliance and end-to-end testing. Before live acceptance it says to add BLIK in live Customer Area (raw lines 69–79).
- This page gives no BLIK code form, `await` action, result-code, webhook, One Click or tokenization procedure. The linked earlier-version guide is separate and does not replace this v5 add-on's stated scope (full raw lines 1–85; earlier-version route at line 21). The snapshot does not prove current merchant enablement or a successful payment.

## Detail locators

- v5.0.0 release/scope and earlier-version route: raw lines 15–21.
- Sessions versus Advanced integration requirements and Customer Area setup: raw lines 23–39.
- No method-specific fields or Component configuration and linked base steps: raw lines 41–67.
- TEST code, BLIK guidance and live Customer Area gate: raw lines 69–79.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-blik-android-component-earlier-versions]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/android-component/2026-09-15|BLIK Android Component add-on, fetched 2026-09-15]]
