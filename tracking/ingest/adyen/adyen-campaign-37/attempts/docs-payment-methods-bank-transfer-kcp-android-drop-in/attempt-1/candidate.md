---
title: "Bank Transfer via KCP Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/android-drop-in/2026-09-15.md"
tags: [adyen, bank-transfer, kcp, android, drop-in]
---

## Overview

This 2026-09-15 guide gives Bank Transfer via KCP additions to an existing Android Drop-in integration, with distinct Sessions and Advanced flow sections. It is method-specific rather than a complete standalone payment integration. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Sessions requires an existing Android Sessions-flow Drop-in integration with Checkout API v68 or later and adding Bank Transfer via KCP in Customer Area. The guide states that no extra `/sessions` parameters or KCP-specific configuration parameters are needed. See raw lines 25–46.
- Advanced requires an existing Android Advanced-flow Drop-in integration, existing `action.type: redirect` handling and Customer Area setup. It states that no extra KCP configuration or `/payments` parameters are needed. The explicit redirect prerequisite and v68 requirement appear in different flow sections; do not silently apply either to the other section as a page-stated requirement. See raw lines 54–74.
- Both Test and go live sections say there are no KCP bank-transfer test credentials because authorization requires a Public Identification Certificate, described as a digital signature for individuals. The guide does not show payment completion, live readiness or current merchant eligibility. See raw lines 48–52 and 76–78.

## Detail locators

- Sessions requirements and no-additional-parameter statements: raw lines 25–46.
- Advanced requirements, redirect and no-additional-parameter statements: raw lines 54–74.
- Duplicated test-credential limitation: raw lines 48–52 and 76–78.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[source-adyen-docs-payment-methods-bank-transfer-kcp]] — separate method overview.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/android-drop-in/2026-09-15|Bank Transfer via KCP Android Drop-in (2026-09-15)]]
