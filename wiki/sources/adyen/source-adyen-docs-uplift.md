---
title: "Adyen Uplift overview and module guidance"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/uplift"
raw_files:
  - "adyen/docs/uplift/2026-09-15.md"
tags: [adyen, uplift, online-payments, optimization, risk, checkout]
---

## Overview

This 2022-modified, 2026-09-15-captured Uplift overview presents Adyen's recommendations, experiments, dashboards and five modules for balancing payment conversion, risk and cost. It describes intended optimization opportunities, not measured uplift for a merchant or proof that a feature is enabled or a payment succeeded. [[adyen]] [[adyen-uplift]]

## Key takeaways

- The page says Uplift analyzes company/merchant settings, payment setup, risk performance and historical data, then shows graphs, recommendations and resources. Recommendations may suggest payment methods, feature toggles or risk-profile changes and show an **expected** effect for evaluation; they do not establish the realized effect. Uplift was still being developed in this snapshot, and experience can differ by region, country and integration type. See raw lines 25-29 and 44-56.
- The stated integration prerequisite is an online payments integration that supports Uplift; module-specific integration and data-point requirements are delegated to the linked Uplift requirements page. Recommendations are limited to those applicable to the integration and relevant country/region; the page says Uplift is optimized for online and omnichannel integrations. See raw lines 31-42. These statements do not establish live account eligibility.
- Customer Area access is role-gated. Viewing Uplift or Checkout overview requires **Merchant admin** or **Merchant report**. Changing Protect settings requires **Risk admin** or **Merchant change risk settings**; changing Optimize settings requires **Merchant admin** or **Merchant manage Uplift optimize settings**; adding/changing payment-method order requires **Change payment methods**. These are role descriptions, not proof of a user's assigned permissions. See raw lines 38-41.
- The Uplift overview route is **Uplift > Uplift overview**, with recommendations under **Uplift > Recommendations**. The separate Checkout dashboard route is **Insights > Checkout**, and the page says analytics and data tracking must be enabled to use it. Dashboard views and experiments support evaluation; they do not itself activate a recommendation. See raw lines 58-72.
- The five modules have distinct subjects: **Tokenize** for tokenized online payments, with shopper consent for stored details and possible PCI DSS scope reduction (raw lines 74-91); **Protect** for fraud/conversion risk evaluation, with data collection suggested and its linked data-collection route requiring a Web integration (raw lines 93-110); **Authenticate** for 3D Secure 2 decisions, whose Authentication Engine is described as included with native or redirect 3D Secure 2 integrations on Web, Android or iOS (raw lines 112-126); **Optimize** for method, routing, messaging, retry and cost recommendations (raw lines 128-143); **Personalize** for checkout analysis and payment-method ordering, whose dynamic ordering depends on module requirements (raw lines 145-159). Linked feature pages own their implementation details; this overview alone does not prove feature availability, account configuration, authorization, fraud prevention, cost reduction or conversion lift.

## Detail locators

- Opening and `## Requirements`, raw lines 15-42: product positioning, development/region caveat, integration, role and recommendation limits.
- `## Evaluate performance and take action`, raw lines 44-72: data basis, recommendation examples, Customer Area routes and separate Checkout dashboard tracking prerequisite.
- `## Tokenize` and `## Protect`, raw lines 74-110: stored-detail consent, tokenization/PCI positioning, risk tools and Web data-collection link.
- `## Authenticate`, raw lines 112-126: 3D Secure 2 routing and stated integration condition.
- `## Optimize` and `## Personalize`, raw lines 128-159: recommendations, checkout analysis, dynamic ordering condition and linked tools.

## Related

- [[adyen-uplift]] — Uplift product concept.
- [[source-adyen-docs-partners-uplift-enablement]] — separate partner enablement guidance; its integration details should be read on their own terms.
- [[adyen-risk-management]] — risk domain context.
- [[adyen-online-payments]] — online integration context.

## Raw Sources

- [[raw/adyen/docs/uplift/2026-09-15|Adyen Uplift overview, captured 2026-09-15]]
