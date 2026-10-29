---
title: "Adyen Bancontact mobile Android Component v5 integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/android-component"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/android-component/2026-09-15.md"
tags: [adyen, bancontact, mobile, android, components, online-payments]
---

## Overview

A short add-on page for **Bancontact mobile** in an existing **Android Components** integration. It explicitly targets **v5.0.0**, released October 2023, and routes earlier versions to a separate guide. Both Sessions and Advanced flow prerequisites require Android Components **at least v5.0.0** and Bancontact added in the Customer Area. This is not a Bancontact card or Android Drop-in guide. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- For the **Sessions** flow, the page says Bancontact requires **no additional `/sessions` fields** and no extra Component configuration. It then links to the base Android Components step for creating the checkout session. See raw lines 27–32, 41–45, 51–63.
- For the **Advanced** flow, it likewise says **no additional `/payments` fields** and no extra Component configuration, then links to the base step to launch and show the Component. See raw lines 34–39, 47–67.
- The page is intentionally an add-on: it supplies no payment action payload, app-switch/QR behavior, redirect-result processing, webhook result taxonomy, tokenization/recurring procedure, or capture/refund procedure. Use the linked base integration or a relevant method-specific guide for those topics; do not import behavior from Bancontact card or another platform merely because it shares the name. See raw lines 15–79.
- It states Bancontact mobile has **no test platform** and recommends a **EUR 0.01 live penny test**. That is the source's recommendation, not evidence that a merchant is live-enabled or a payment was executed. See raw lines 69–73.

## Detail locators

- v5.0.0 identity, release month and earlier-version route: raw lines 15–21.
- Sessions/Advanced prerequisites and Customer Area setup: raw lines 23–39.
- No-extra-fields and no-extra-configuration statements: raw lines 41–59.
- Base-guide continuation links: raw lines 61–67.
- No-test-platform and live penny-test statement: raw lines 69–73.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/android-component/2026-09-15|Bancontact mobile Android Component documentation capture (2026-09-15)]]
