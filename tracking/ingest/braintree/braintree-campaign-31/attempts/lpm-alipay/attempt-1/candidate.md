---
title: "Braintree Alipay Local Payment Method"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/alipay"
raw_files:
  - "braintree/docs/guides/local-payment-methods/alipay-2026-09-16.md"
tags: [braintree, local-payment-methods, alipay, china, limited-release]
---

## Overview

This collected, unversioned Braintree page identifies the `alipay` Local Payment Method and records its limited-release applicability. In the 2026-09-16 snapshot, the page says Alipay is available only to buyers in China; its table lists seller availability as global except Russia, Brazil and Mainland China, names eight supported currency codes, and gives a customer maximum transaction limit of 300,000 CNY with no minimum stated. This snapshot does not establish current availability, account enablement, individual buyer eligibility or successful payment execution.

## Key takeaways

- The page's limited-release notice tells merchants who want to integrate Alipay as a Local Payment Method to contact their Customer Success Manager. That notice is an onboarding route, not proof that a merchant is approved or enabled.
- The applicability table names payment type `alipay`, buyers in China, and sellers globally except Russia, Brazil and Mainland China. It lists `AUD`, `CAD`, `EUR`, `GBP`, `HKD`, `NZD`, `SGD` and `USD` as currency codes.
- The table records `Min: N/A Max: 300,000 CNY` under customer transaction limits. The page does not explain how the CNY-denominated maximum relates to the listed transaction currencies, so this entry does not infer conversions or per-currency limits.
- This short page does not document checkout initiation, redirect behavior, a client or server flow, an SDK platform or version, a Sandbox or Production procedure, settlement, merchant funding, or transaction outcome handling. Following a setup or integration route therefore would not by itself prove that a payment executed.

## Evidence boundaries

> [!warning] Limited-release snapshot
> Treat the country, currency and limit statements as the collected page's 2026-09-16 wording. Recheck current and account-specific availability before relying on them; the page does not prove merchant enablement, buyer eligibility or a completed payment.

> [!warning] Buyer and seller geography
> Preserve the table's distinct statements that buyers are in China while sellers are global except Russia, Brazil and Mainland China. The page does not explain or reconcile that geographic scope further.

## Detail locators

- Page identity and unversioned route: frontmatter `title` and `slug`, raw lines 5-9; `# Alipay`, raw line 14.
- Limited-release status, China-buyer qualification and Customer Success Manager contact notice: `### Overview > **AVAILABILITY**`, raw lines 17-21.
- Payment type, buyer and seller countries, currency codes and customer transaction limit: availability table, raw lines 23-25.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on integration research:

- [[raw/braintree/docs/guides/local-payment-methods/overview-2026-09-16|Braintree Local Payment Methods overview]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16|JavaScript v3 Local Payment Methods configuration]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16|Android v5 Local Payment Methods configuration]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16|iOS v7 Local Payment Methods configuration]]
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Node.js server-side Local Payment Methods guide]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/alipay-2026-09-16|Braintree Alipay guide]] - fully read pinned snapshot covering the method identity, limited-release notice, buyer and seller geography, currency codes and customer transaction limit
