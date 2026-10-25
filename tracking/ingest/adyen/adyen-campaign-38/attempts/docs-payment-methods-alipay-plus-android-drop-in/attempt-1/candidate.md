---
title: "Alipay+ Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/android-drop-in/2026-09-15.md"
tags: [adyen, alipay-plus, android, drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15-captured guide describes Alipay+-specific additions to an existing Android Drop-in integration, split into Sessions and Advanced server-side flows. It documents setup and configuration, not current merchant or wallet eligibility or any observed payment outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions scope:** the Sessions path requires an existing Android Drop-in Sessions integration, Checkout API **v68 or later**, and Alipay+ added in Customer Area. It says no extra `/sessions` parameters are needed. The configuration table offers `setSubmitButtonVisible`: `false` hides the submit button, `true` is the default, and its Required cell is blank. This is a configuration option, not a mandatory Alipay+ setting. (raw lines 25–61)
- **Advanced scope:** the Advanced path separately requires an existing Android Drop-in Advanced integration, redirect handling for `action.type: redirect`, and Alipay+ added in Customer Area. It presents the same optional submit-button configuration and says no extra `/payments` parameters are needed. The page does not state that the Sessions v68+ floor applies to Advanced. (raw lines 78–114)
- **Environment and live-request warning:** both sections state there is **no Alipay+ test environment** and recommend live penny tests using an Alipay+ wallet app with a card, with payment details viewed in live Customer Area. That is the source's recommendation, not a test performed here or permission to transact. Both sections say to submit a live Customer Area request for **“Alipay”** before accepting live **Alipay+** payments; the label mismatch remains unresolved on this page, so it does not prove Alipay+ enablement. (raw lines 64–76, 116–126)

## Detail locators

- Sessions requirements, request/configuration scope and example: raw lines 25–61.
- Advanced redirect requirement, configuration and request scope: raw lines 78–114.
- No-test-environment statement, live penny-test recommendation and Alipay/Alipay+ request-label mismatch: raw lines 64–76, 116–126.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/android-drop-in/2026-09-15|Adyen Alipay+ Android Drop-in guide, 2026-09-15 snapshot]]
