<!-- Source URL: https://developer.paypal.com/docs/checkout/pay-later/upgrade-options/ -->
<!-- Fetched: 2026-04-14 -->
<!-- NOTE: This page has nearly identical content to /docs/checkout/pay-later/customize/code-samples/ — same upgrade patterns and code snippets. See paypal-pay-later-code-samples.md for the summarized content. -->

---
title: Pay Later upgrade options
slug: /docs/checkout/pay-later/upgrade-options/
createTime: '2025-11-03T08:49:44.061Z'
updateTime: '2026-02-05T15:02:25.092Z'
---

# Pay Later upgrade options

Two upgrade options to add Pay Later messaging to an existing PayPal integration:

1. Upgrade to a JavaScript SDK integration (from legacy merchant.js)
2. Add Pay Later to an existing integration (coexistence patterns)

Content is identical to /docs/checkout/pay-later/customize/code-samples/ — see raw/paypal-pay-later-code-samples.md for full details.

Key patterns (same as code-samples):
- Legacy merchant.js → replace with JS SDK components=messages
- data-pp-payerid / data-pp-pubid = PAYER_ID, NOT client ID
- No PayPal: components=messages
- Existing SDK buttons: components=buttons,messages
- checkout.js coexistence: add data-namespace="PayPalSDK" to new SDK script, use PayPalSDK.Messages()
- Legacy REST/static: add components=messages alongside existing integration
