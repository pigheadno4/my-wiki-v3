---
title: "Adyen Alipay HK API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/api-only"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/api-only/2026-09-15.md"
tags: [adyen, alipayhk, api-only, web, online-payments]
---

## Overview

This [[adyen]] guide, modified and captured 2026-09-15, adds Alipay HK to an existing **Web-linked Advanced API-only** integration. It covers `HK`/`HKD` method discovery, merchant-built selection, redirect handling and TEST/live setup. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alipayhk|Alipay HK overview]] for the separate dated HK/HKD wallet/redirect matrix. Method lookup, setup and sample response do not establish current merchant eligibility, final authorization, capture or settlement. See primary raw lines 15–29 and 44–99.

## Key takeaways

- The prerequisite is an existing API-only integration linked here to a **Web Advanced** main flow, `action.type: redirect` handling and Alipay HK added in Customer Area. The guide describes a merchant-built payment-method choice and says the existing integration handles the redirect. It does not provide a deep-link/return callback, final webhook or payment-state procedure itself. See raw lines 23–42 and 101–103.
- To retrieve Alipay HK with `/paymentMethods`, the page specifies `countryCode: HK` and `amount.currency: HKD`. Its Checkout TEST `/v72/paymentMethods` HK/HKD example shows `type: alipay_hk`; this is a dated sample, not a stated minimum API version or proof of current merchant enablement. See raw lines 44–83.
- The high-level **How it works** list says the shopper enters details in the merchant form and that item information is sent “if applicable,” while the more specific form section says no shopper information needs collecting and the `/payments` section says no additional Alipay HK parameters. The high-level shopper-detail wording does not establish a required field; the item-data instruction is conditional and gives no Alipay HK field schema. Preserve that distinction and follow the base Advanced integration for ordinary request fields. See raw lines 31–40 and 85–87.
- The shown curl command has `-X POST` without a line-continuation character before `-d`; it is not paste-ready as shown. The `idempotency-key` header appears in the example, not as a stated Alipay HK-specific requirement. See raw lines 53–70.
- The TEST section publishes test credentials and directs readers to TEST Customer Area's payment list. It separately says a live Customer Area request for AlipayHK is needed before accepting live payments. The existence of those credentials, a method-list response or request submission does not establish an executed test, approved live account or successful payment. See raw lines 89–99.

## Detail locators

- **Web Advanced prerequisite, redirect and shopper-form wording:** raw lines 19–42.
- **HK/HKD method discovery, TEST v72 sample, `alipay_hk` type and curl defect:** raw lines 44–83.
- **No extra Alipay HK `/payments` fields, TEST credentials and live request:** raw lines 85–103.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/api-only/2026-09-15|Alipay HK API-only — captured 2026-09-15]]
