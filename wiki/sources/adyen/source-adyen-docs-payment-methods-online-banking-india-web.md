---
title: "Adyen Online Banking India for Web"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-india/web"
raw_files:
  - "adyen/docs/payment-methods/online-banking-india/web/2026-09-15.md"
tags: [adyen, online-banking-india, web, drop-in, components]
---

## Overview

This 2026-09-15-captured Adyen page is a Web integration **router** for Online Banking India. It points to separate Web Drop-in and Web Components guides and to four main integration guides covering Sessions and Advanced flows for each UI. It does not itself give request fields, eligibility, redirect processing, or payment-result rules. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-india]] for the payment-method overview.

## Key takeaways

- Choose the Web Drop-in guide for the all-in-one website UI, or the Web Components guide for the `OnlineBankingIN` website Component. See raw lines 19–27. The latter guide has its own source route: [[source-adyen-docs-payment-methods-online-banking-india-web-component]].
- Build the main Web integration before adding Online Banking India. This router links the main Sessions and Advanced guides for both Drop-in and Components. See raw lines 29–36. Follow the chosen child guide for method-specific setup and outcomes; these links do not themselves establish which setup is currently available to a merchant.

## Detail locators

- Web Drop-in and Components child-guide links: raw lines 19–27.
- Sessions/Advanced main integration links for both Web UIs: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-india]]
- [[source-adyen-docs-payment-methods-online-banking-india-web-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-india/web/2026-09-15|Fully read Online Banking India Web router raw]]
