---
title: "Adyen Wallets India Web Component add-on"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wallets-india/web-component"
raw_files:
  - "adyen/docs/payment-methods/wallets-india/web-component/2026-09-15.md"
tags: [adyen, wallets-india, web-component, india, online-payments]
---

## Overview

This [[adyen]] guide describes method-specific additions for **Wallets India** in an existing **Web Components** integration, with separate Sessions and Advanced flows. It does not name individual wallet issuers, currencies, shopper regions, redirect actions or final payment statuses. The page's “no extra parameters” statements concern this add-on and do not replace the base server-side flow. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** the page requires an existing Sessions Web Components integration, **Checkout API v68+**, and Wallets India added in Customer Area. It says no extra Wallets-India-specific `/sessions` fields or configuration are needed, and shows importing `WalletINElement` and mounting the Component. See raw lines 23–75.
- **Advanced:** the page separately requires an existing Advanced Web Components integration and Wallets India added in Customer Area. It shows the same import/mount pattern and says no extra Wallets-India-specific `/payments` fields or configuration are needed. This section does **not** restate the Sessions v68+ version as its own prerequisite. See raw lines 83–132.
- Both flow samples import `WalletINElement`, then invoke `newWalletINElement(checkout, ...) ` without defining that identifier or using the standard `new WalletINElement` syntax. Their comments mention a “configuration object ... that you created” even though the prose says no method-specific configuration is needed. These are source-example inconsistencies; the snippets are not self-contained implementation proof. See raw lines 45–74 and 94–125.
- The page says Wallets India **has no test platform** in this snapshot. Before live acceptance it instructs the merchant to **submit a request** for Wallets India in live Customer Area. A request is not approval or proof of live method availability, and this guide gives no test-payment or payment-outcome evidence. See raw lines 77–81 and 134–138.

## Detail locators

- Sessions prerequisites, request note and Component snippet: raw lines 23–75.
- Advanced prerequisites, request note and Component snippet: raw lines 83–132.
- Repeated test/live limitations: raw lines 77–81 and 134–138.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wallets-india/web-component/2026-09-15|Adyen Wallets India Web Component snapshot]]
