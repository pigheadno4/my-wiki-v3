---
title: "Adyen Wallets India Web Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wallets-india/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/wallets-india/web-drop-in/2026-09-15.md"
tags: [adyen, wallets-india, web-drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen page describes adding **Wallets India** to an existing **Web Drop-in** integration, with separate Sessions and Advanced server-side flow sections. It specifies method-specific setup and links to the underlying Drop-in guides; it does not supply issuer selection, redirect/return handling, country/currency eligibility, or payment-result mechanics. Its instructions are a dated page snapshot, not proof of current merchant enablement or payment success. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** Existing Sessions-flow Web Drop-in, **Checkout API v68 or later**, and Wallets India added in Customer Area are listed prerequisites. No method-specific additional `/sessions` parameters or Drop-in configuration are required by this page. The v68 requirement is stated in the Sessions tab and should not be silently applied to the Advanced tab. (raw lines 23–39, 53–57)
- **Advanced:** Existing Advanced-flow Web Drop-in and Customer Area method setup are listed. The page says no method-specific extra Drop-in configuration or `/payments` parameters are needed, and supplies no explicit Checkout API minimum for this tab. The Advanced integration link contains an unresolved `{{getParameter('platform')}}` template value, so it is not a reliable literal platform URL. (raw lines 67–76, 90–100)
- Optional individual imports are framed as tree-shaking optimization. Both tabs' prose says to include `WalletINElement`, but both code examples import `Wallet_in` from `@adyen/adyen-web`. This is a material name mismatch; the snippet should not be treated as a verified import without checking the selected Web package/version. (raw lines 41–51, 78–88)
- Both tabs state **Wallets India currently has no test platform** and require submitting a **Wallets India request in live Customer Area** before live acceptance. This is not evidence that a live account is approved, a redirect completed, or a payment was authorized, captured or settled. (raw lines 59–65, 102–108)
- “No additional parameters/configuration” is scoped to this method-specific add-on; it does not waive the base integration's required server requests, shopper interaction, callbacks, issuer choice, redirect handling or payment-result processing. This page does not describe those downstream steps. (raw lines 19–21, 37–57, 92–108)

## Detail locators

- Sessions prerequisites and request/configuration statements: raw lines 23–57.
- Sessions no-test-platform and live request: raw lines 59–65.
- Advanced prerequisites, request/configuration statements and optional import: raw lines 67–100.
- Advanced no-test-platform and live request: raw lines 102–108.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-wallets-india-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wallets-india/web-drop-in/2026-09-15|Adyen Wallets India Web Drop-in guide, 2026-09-15 snapshot]]
