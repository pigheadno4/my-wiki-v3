<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/general/merchant-responses/merchant-advice-codes -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Merchant Advice Codes
slug: /docs/reference/general/merchant-responses/merchant-advice-codes/
createTime: '2025-04-01T21:59:56.588Z'
updateTime: '2025-04-01T21:59:56.603Z'
---



# Merchant Advice Codes

Merchant Advice Codes (MACs) are introduced by Mastercard to clearly communicate to merchants the reason for declining transactions, and the course of action that merchants can take. If present, the MAC contains information about why the payment failed, whether it can be retried and in some cases, the recommended duration after which it should be retried.

In the transaction responsemerchant_advice_codeand its corresponding descriptionmerchant_advice_code_textwill be returned.

Following are the merchant advice codes and the corresponding text for these codes:

| Merchant Advice Code | Merchant Advice Code Text |
| --- | --- |
| 01 | New account information available |
| 02 | Cannot approve at this time, try again later |
| 03 | Do not try again |
| 04 | Token not supported |
| 21 | Stop recurring payment |
| 24 | Retry after 1 hour |
| 25 | Retry after 24 hours |
| 26 | Retry after 2 days |
| 27 | Retry after 4 days |
| 28 | Retry after 6 days |
| 29 | Retry after 8 days |
| 30 | Retry after 10 days |
| 40 | Consumer non-reloadable prepaid card |
| 41 | Consumer single-use virtual card number |
| 43 | Consumer multi-use virtual card number |

