---
title: "Braintree Marketplace Developer Guide Overview"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview"
raw_files:
  - "braintree/docs/guides/braintree-marketplace/overview-2026-09-16.md"
tags: [braintree, marketplace, developer-guide, sub-merchants, service-fees, escrow]
---

## Overview

This collected developer-guide overview is an orientation and navigation page for Braintree Marketplace. It identifies the marketplace owner and providers, summarizes the service-fee and disbursement model, states compatibility and approval boundaries, defines the page's core terminology, and routes readers to dedicated Marketplace guides. It is distinct from the article-level overview and from language-specific operation pages; this snapshot does not establish current Marketplace availability or merchant eligibility.

## Key takeaways

- The page describes a marketplace owner facilitating purchases from multiple providers. In its Braintree Marketplace framing, transactions can be split, a service fee can be designated for the owner, and the remaining funds can be disbursed to the sub-merchant; the page also says Braintree verifies a newly onboarded sub-merchant's identity after basic contact information is collected.
- The documented compatibility boundary requires the master merchant and all sub-merchants to be domiciled in the US. The page says Marketplace is incompatible with PayPal, Braintree recurring billing, and most third-party shopping carts, and requires special Braintree approval for all merchant accounts before setup.
- The overview defines the master merchant as the Marketplace owner, a sub-merchant as an individual provider or seller, and the service fee as the share of sub-merchant transaction revenue routed to the master merchant. It also introduces escrow and onboarding/disbursement-problem webhooks as terms; their procedures and lifecycle details remain in dedicated guides.
- This page is a router, not an operation specification. It links the master merchant to onboarding, onboarding confirmation, transaction creation with service fees, and holding transaction funds in escrow; request fields, SDK methods, responses, testing, updates, and release behavior require their dedicated source or raw pages.

> [!warning] Snapshot and support boundary
> New merchants seeking a Marketplace solution are directed to Braintree Sales. Collection of this page and its description of Marketplace capabilities do not prove current product support, account approval, eligibility, enablement, onboarding success, transaction success, settlement, or disbursement. Preserve the page's explicit US-domicile, incompatibility, and special-approval qualifications when using it for navigation.

## Detail locators

- New-merchant Sales route: opening `AVAILABILITY`, lines 17-18, repeated under `## Compatibility`, lines 30-31.
- Marketplace-owner/provider model, transaction splitting, service-fee allocation, disbursement and identity-verification orientation: opening overview, lines 20-26.
- US domicile, PayPal/recurring-billing/shopping-cart incompatibilities and special merchant-account approval: `## Compatibility`, lines 33-36.
- Master merchant, sub-merchant, service fee, escrow and webhook terminology: `## Terminology`, lines 40-44.
- Navigation to the four named Marketplace API feature areas: `## API features`, lines 47-54.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/onboarding/node-2026-09-16|Braintree Marketplace onboarding guide - Node.js]] - unread navigation-only route for onboarding procedure and conditions; no Node-specific behavior is imported here
- [[raw/braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16|Braintree Marketplace confirmation guide - Node.js]] - unread navigation-only route for confirmation procedure and state boundaries; no Node-specific behavior is imported here
- [[raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16|Braintree Marketplace transaction creation guide - Node.js]] - unread navigation-only route for service-fee transaction creation and held-funds details; no Node-specific behavior is imported here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16|Braintree Marketplace developer-guide overview]] - complete collected overview covering purpose, compatibility, terminology and API-feature navigation
