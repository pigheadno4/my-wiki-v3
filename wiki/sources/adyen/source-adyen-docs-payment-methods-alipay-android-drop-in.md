---
title: "Adyen Alipay Android Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay/android-drop-in/2026-09-15.md"
tags: [adyen, alipay, android, drop-in]
---

## Overview

This [[adyen]] guide lists Alipay-specific additions to an existing **Android Drop-in** integration, separated by **Sessions** and **Advanced** server-side flows. The main integration guides supply the base request and payment lifecycle. Method setup, a payment-list entry or a redirect action does not by itself establish a final authorization, capture or settlement result. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The guide requires an existing Android Drop-in Sessions flow with **Checkout API v68 or later** and Alipay added in Customer Area. It states no additional Alipay parameters are needed for `/sessions` or Alipay configuration. This means no method-specific additions, not that the base Sessions request is empty. Unlike the Advanced table, the Sessions requirements table does **not** separately list redirect handling; use the main Sessions guide for its action lifecycle rather than attributing that requirement to this row. See raw lines 25–46.
- **Advanced:** The section requires an existing Android Drop-in Advanced flow, `action.type: redirect` handling and Customer Area method setup. It states no additional Alipay configuration or `/payments` parameters. The Advanced section does not state the Sessions section's v68+ minimum as its own prerequisite. See raw lines 60–80.
- **Live preparation:** Both sections recommend live penny tests with an Alipay wallet app and a credit/debit card, followed by reviewing the payment in **live Customer Area**. Separately, before accepting live Alipay payments, the page says to submit an Alipay request in live Customer Area. The tests are recommendations and submission is a gate, not proof of approval or payment success. The pinned page gives no distinct TEST-environment procedure. See raw lines 48–58 and 82–90.

## Detail locators

- Sessions prerequisites, method-specific request/configuration: raw lines 25–46.
- Advanced prerequisites, redirect handling, method-specific request/configuration: raw lines 60–80.
- Duplicated live-test recommendation and live request: raw lines 48–58 and 82–90.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-alipay]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/android-drop-in/2026-09-15|Adyen Alipay Android Drop-in guide]]
