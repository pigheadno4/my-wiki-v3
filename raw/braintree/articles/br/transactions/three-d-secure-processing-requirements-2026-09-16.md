<!-- Source URL: https://developer.paypal.com/braintree/articles/br/transactions/three-d-secure-processing-requirements -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: '3D Secure Processing Requirements '
slug: /articles/br/transactions/three-d-secure-processing-requirements/
createTime: '2025-04-02T01:30:20.834Z'
updateTime: '2025-04-02T01:30:20.933Z'
---



# 3D Secure Processing Requirements


## Applicable card types

The requirements for processing below will apply to the following card types:


- Visa
- Mastercard


### Visa debit cards

In Brazil, issuers tend to approve transactions for debit cards at higher rates if they are authenticated using 3D Secure.


### Mastercard debit cards

Mastercard has issued a requirement for debit cards to be processed using either a standard 3D Secure authentication, or a [data-only 3D Secure authentication](/braintree/docs/guides/3d-secure/advanced-options#using-data-only-3d-secure).

Given the above requirements from issuers and card brands, it is our recommendation that debit cards are [authenticated using 3D Secure](/braintree/docs/guides/3d-secure/configuration) to achieve the highest approval rates.

