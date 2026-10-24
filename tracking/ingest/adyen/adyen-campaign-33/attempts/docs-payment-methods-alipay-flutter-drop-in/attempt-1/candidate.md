---
title: "Adyen Alipay Flutter Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay/flutter-drop-in/2026-09-15.md"
tags: [adyen, alipay, flutter, drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen page gives **Alipay-specific additions** for an existing **Flutter Drop-in** integration, with separate Sessions and Advanced server-side sections. It does not define the full base payment flow, geographic/currency eligibility, shopper return, webhook outcome or settlement behavior. Its dated setup text is not evidence of current method approval or payment success. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The table states existing Sessions Flutter Drop-in, **Checkout API v68 or later**, existing `action.type: redirect` handling, and Alipay added in Customer Area. It says no Alipay-specific `/sessions` parameters or extra Drop-in configuration are needed. The integration-type label says Sessions but its link points to an **Advanced-flow** URL; the redirect and `/sessions` links point to Sessions. Keep the intended flow explicit rather than relying on that mismatched link. (raw lines 25–48)
- **Advanced:** The table states existing Advanced Flutter Drop-in and Customer Area method setup, and the page says no Alipay-specific extra configuration or `/payments` parameters are needed. Its Checkout API row literally says **“vredirect or later”**, an invalid version expression; this page therefore gives no reliable Advanced minimum. Unlike the Sessions table, the Advanced table has no separate redirect-handling row, so this page alone does not establish the exact Advanced redirect prerequisite. (raw lines 60–82)
- In both flow sections, Adyen **recommends** live penny tests using an Alipay wallet app with a card and viewing those transactions in **live Customer Area**. These are proposed **real live payments**, not a TEST platform or proof such payments occurred. Separately, the page says a request for Alipay in **live Customer Area** is needed before accepting live Alipay payments; submission alone does not establish approval. No live test or provider operation was performed for this ingestion. (raw lines 50–58, 84–92)
- “No additional parameters/configuration” is method-specific and does not waive the underlying Flutter Drop-in integration's own requirements. This page supplies no authorization, capture, refund, settlement or final webhook proof, and does not document a post-handoff payment outcome. (raw lines 19–23, 38–48, 72–92)

## Detail locators

- Sessions requirements, redirect and method-specific `/sessions`/configuration statements: raw lines 25–48.
- Sessions recommended live penny tests and live method request: raw lines 50–58.
- Advanced requirements, invalid version row and no-extra-configuration/`/payments` statements: raw lines 60–82.
- Advanced recommended live penny tests and live method request: raw lines 84–92.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/flutter-drop-in/2026-09-15|Adyen Alipay Flutter Drop-in guide, 2026-09-15 snapshot]]
