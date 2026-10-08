---
title: "Braintree UnionPay Configuration"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/unionpay/configuration"
raw_files:
  - "braintree/docs/guides/unionpay/configuration-2026-09-16.md"
tags: [braintree, unionpay, configuration, credit-cards, deprecation]
---

## Overview

This collected, unversioned [[braintree]] configuration page contains only an availability notice: the dedicated UnionPay integration is deprecated because UnionPay can now be processed as a credit card through its partnership with Discover. Its practical action is to follow the separately linked credit-card guide rather than treat this page as an active UnionPay configuration procedure. [[braintree-payment-methods]]

## Key takeaways

- The captured page provides no configuration steps, SDK or package version, client/server placement, environment, merchant-access condition, account-enablement instruction, or payment lifecycle.
- The Discover credit-card statement is provider migration direction from this snapshot, not proof of current support, merchant or card eligibility, account enablement, successful authorization, settlement, or funding.

> [!warning] Deprecated dedicated integration
> Do not infer that the dedicated UnionPay path remains available or enabled. The page redirects to a separate credit-card guide but does not document that route's setup, qualifications, runtime behavior, or successful execution.

## Detail locators

- Page identity and configuration slug: frontmatter and `# Configuration`, raw lines 5-14.
- Dedicated-integration deprecation, Discover credit-card direction, and credit-card-guide navigation: `AVAILABILITY`, raw lines 17-18.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Credit-card guide navigation: [[source-braintree-credit-cards-overview]] — linked by the captured page; no behavior or current availability is inferred here
- UnionPay overview: [[source-braintree-docs-guides-unionpay-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/unionpay/configuration-2026-09-16|Braintree UnionPay configuration (2026-09-16 snapshot)]] — fully read pinned webpage containing the deprecation and Discover credit-card redirect
