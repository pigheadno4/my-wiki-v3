---
title: "Braintree Marketplace Article Overview"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/overview"
raw_files:
  - "braintree/articles/guides/braintree-marketplace/overview-2026-09-16.md"
tags: [braintree, marketplace, sub-merchants, service-fees, escrow]
---

## Overview

This collected article-level overview explains the Braintree Marketplace product model, compatibility scope, and core terminology. It describes a marketplace owner facilitating purchases from multiple providers, Braintree splitting transactions and disbursing funds between the owner and sub-merchants, and the owner's service-fee role. It is distinct from the developer-guide overview and language-specific operation pages; this snapshot does not establish current Marketplace support or merchant eligibility.

## Key takeaways

- Braintree Marketplace is described as allowing a marketplace owner to split transactions, designate a service fee on each transaction, and have Braintree disburse the corresponding funds to the owner and sub-merchant. The article also says onboarding can begin with basic contact information and that Braintree verifies the sub-merchant's identity; it does not document an API procedure or promise approval.
- The documented compatibility boundary requires the master merchant and every sub-merchant to be domiciled in the US. The article says Marketplace is incompatible with PayPal, Braintree recurring billing, and most third-party shopping carts, and that every merchant account needs special Braintree approval before use.
- The article defines the master merchant as the Marketplace owner, the sub-merchant as an individual provider or seller, and the service fee as the portion of sub-merchant transaction revenue routed to the master merchant.
- Its terminology also frames escrow as an optional hold through Braintree's banking partner until disbursement, and webhooks as server notifications about merchant onboarding results or problems disbursing funds to a sub-merchant's bank account. Detailed setup, API methods, state handling, and lifecycle behavior belong to dedicated guides.

> [!warning] Snapshot availability and eligibility boundary
> New merchants seeking a Marketplace solution are directed to Braintree Sales. Collection of this article and its product description do not prove current availability, support, account approval, eligibility, enablement, onboarding success, transaction success, settlement, or disbursement. Preserve the explicit US-domicile, incompatibility, and special-approval conditions when using this snapshot.

> [!warning] Unresolved recurring-billing conflict
> This article states that Braintree Marketplace is incompatible with Braintree recurring billing. [[source-braintree-marketplace-guide-testing-go-live-node]] says applicable Marketplace integrations should recreate recurring-billing plans or settings in production. The collected documents do not resolve this contradiction; do not infer Marketplace recurring-billing support.

## Detail locators

- New-merchant Sales route: opening `AVAILABILITY`, lines 17-18, repeated under `## Compatibility`, lines 30-31.
- General marketplace-owner/provider model and Braintree transaction-splitting, service-fee, disbursement, and identity-verification orientation: opening overview, lines 22-24.
- US domicile, PayPal/recurring-billing/shopping-cart incompatibilities, and special merchant-account approval: `## Compatibility`, lines 27-35.
- Master merchant, sub-merchant, service fee, escrow, and webhook definitions: `## Terminology`, lines 38-45.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Conflicting collected recurring-billing route: [[source-braintree-marketplace-guide-testing-go-live-node]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16|Braintree Marketplace developer-guide overview]] - separate navigation-only guide route; no developer-guide or language-specific operation behavior is imported here

## Raw Sources

- [[raw/braintree/articles/guides/braintree-marketplace/overview-2026-09-16|Braintree Marketplace article overview]] - complete collected article covering the product model, compatibility conditions, and core terminology
