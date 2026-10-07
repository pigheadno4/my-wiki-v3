---
title: "Braintree WeChat Pay Local Payment Method"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/wechat-pay"
raw_files:
  - "braintree/docs/guides/local-payment-methods/wechat-pay-2026-09-16.md"
  - "braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md"
tags: [braintree, local-payment-methods, wechat-pay, china, limited-release]
---

## Overview

This collected, unversioned Braintree website page is a short availability and applicability record for WeChat Pay as a Local Payment Method. In the 2026-09-16 snapshot it marks WeChat Pay as limited release, limits buyer availability to China, and directs a merchant that wants to integrate it to contact their Customer Success Manager. That contact route is not proof of approval or enablement, and the snapshot does not establish current availability, individual buyer eligibility or successful payment execution.

## Key takeaways

- The applicability row identifies the payment type as `wechatpay`, buyers in China, and sellers in Austria, Belgium, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Liechtenstein, Luxembourg, Malta, Holland, Norway, Portugal, Spain, Sweden and the United Kingdom. Preserve `Holland` as the page's captured label rather than silently normalizing it.
- The row lists `EUR`, `USD` and `GBP` as currency codes and records `Min: N/A Max: 10,000 USD` under customer transaction limits. The page does not define what `N/A` means or explain whether the USD-denominated maximum applies identically when a listed currency is EUR or GBP, so this entry does not infer a minimum, conversion rule or per-currency limit.
- The same-date article-level Local Payment Methods guide says transactions are automatically presented to customers in Euros, while the WeChat row lists `EUR`, `USD` and `GBP` currency codes and a USD-denominated maximum. The sources do not reconcile currency-code listing with presentment, settlement, conversion or limit denomination, so this entry infers none of those behaviors.
- This page contains no checkout initiation, redirect, client or server flow, SDK platform or version, Sandbox or Production procedure, transaction-state transition, settlement, merchant-funding or outcome-handling detail. It is website snapshot evidence, not Braintree SDK repository or GitHub implementation/history evidence.

> [!warning] Limited-release snapshot and execution boundary
> Treat the limited-release status, buyer and seller geography, currency codes and limit as the collected page's 2026-09-16 wording. Recheck current and account-specific availability before relying on them; contacting a Customer Success Manager does not prove merchant enablement, and the page does not prove that a buyer qualifies or a payment executed, settled or funded.

> [!warning] Unresolved currency relationship
> The same-date Local Payment Methods article's blanket Euro-presentment statement is not reconciled with the WeChat row's `EUR`, `USD` and `GBP` currency codes or USD-denominated maximum. Do not infer presentment, settlement, conversion or per-currency limit behavior from either source alone.

## Detail locators

- Page identity and unversioned route: frontmatter `title` and `slug`, raw lines 5-9; `# WeChat Pay`, raw line 14.
- Limited-release status, China-buyer restriction and Customer Success Manager contact route: `### Overview > **AVAILABILITY**`, raw lines 17-21.
- Payment type, buyer and seller countries, currency codes and customer transaction limit: table under `### Overview`, raw lines 23-25.
- Umbrella Euro-presentment, primary-currency PayPal settlement and customer-conversion wording: Local Payment Methods article, `## Availability`, supporting raw line 21.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Local Payment Methods overview: [[source-braintree-local-payment-methods-overview]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this entry; they are exact-file navigation for follow-on Local Payment Methods platform, server and environment research:

- [[raw/braintree/docs/guides/local-payment-methods/overview-2026-09-16|Braintree Local Payment Methods overview]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16|JavaScript v3 Local Payment Methods configuration]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16|Android v5 Local Payment Methods configuration]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16|iOS v7 Local Payment Methods configuration]]
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Node.js Local Payment Methods server guide]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/wechat-pay-2026-09-16|Braintree WeChat Pay guide]] - fully read primary pinned snapshot covering the method identity, limited-release notice, buyer and seller geography, currency codes and customer transaction limit
- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree Local Payment Methods article]] - fully read same-date supporting snapshot for the unresolved relationship among Euro presentment, the WeChat currency-code listing and the USD-denominated maximum
