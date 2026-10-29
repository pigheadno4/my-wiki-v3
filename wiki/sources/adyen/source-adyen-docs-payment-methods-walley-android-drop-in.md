---
title: "Walley Android Drop-in v5 integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/walley/android-drop-in/2026-09-15.md"
tags: [adyen, walley, android, drop-in, b2b]
---

## Overview

This 2026-09-15-captured Walley Android Drop-in add-on is expressly for **v5.0.0**, released October 2023, and points earlier-version integrations to a separate guide. It covers method-specific additions to existing Sessions and Advanced Android Drop-in flows; it does not prove current availability, account enablement, or a successful payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-walley|Walley overview]] for B2C/B2B method types, country/currency scope, recurring marks, and the 90-day capture limit.

## Key takeaways

- Both server-side flow tabs require an existing **Android Drop-in version 5.0.0 or later** integration in their respective Sessions or Advanced flow, plus Walley added in Customer Area. This page is titled for v5.0.0 specifically and links an earlier-version guide; it does not document the behavior of every later SDK version (raw lines 19–39).
- For the method-specific add-on, the Sessions `/sessions` request and Advanced `/payments` request require **no additional Walley fields**. Drop-in requires **no additional Walley configuration** in either flow. The base guides still own ordinary payment request and Android setup requirements (raw lines 41–67).
- For **test scenarios** using Walley's technical documentation and Adyen's `/payments` endpoint, the page says to put `CivRegNo` in `socialSecurityNumber`; a **B2B test transaction** also provides `company.name` and `company.registrationNumber` as shown in its example. These are scenario-specific test directions, not universal live request fields or proof of B2B enablement (raw lines 69–82).
- The “See also” tokenization link is generic navigation. The Walley overview marks recurring with a cross for both B2C and B2B, so this child page does not establish Walley recurring support (raw lines 84–89; [[source-adyen-docs-payment-methods-walley]]).

## Detail locators

- Version and earlier-guide routing: raw `# Walley Drop-in integration` lines 15–21.
- Sessions and Advanced prerequisites: raw `## Requirements` lines 23–39.
- No-extra-field and no-extra-configuration statements: raw lines 41–67.
- Test-only `CivRegNo` and B2B company data: raw `## Test and go live` lines 69–82.
- Generic related navigation: raw `## See also` lines 84–89.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-walley]]
- [[source-adyen-docs-payment-methods-walley-android-drop-in-earlier-versions]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/android-drop-in/2026-09-15|Walley Android Drop-in v5 guide, captured 2026-09-15]]
