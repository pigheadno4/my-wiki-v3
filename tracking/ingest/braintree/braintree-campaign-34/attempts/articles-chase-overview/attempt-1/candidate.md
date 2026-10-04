---
title: "Braintree Chase Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/chase/overview"
raw_files:
  - "braintree/articles/chase/overview-2026-09-16.md"
tags: [braintree, chase, merchant-account, processor, banking-partner]
---

## Overview

This collected Braintree article is the landing page for direct-link-only guidance tailored to merchant accounts funded by Chase. It says the page is sent when at least one of the recipient's merchant accounts is Chase-funded; it does not establish that every account uses Chase or that the account-specific guidance applies to another merchant, processor or banking partner.

The 2026-09-16 snapshot is Braintree-hosted documentation, not independent Chase authority or proof of current account eligibility, pricing, support or payment execution.

## Key takeaways

- The page identifies a specific account relationship: receiving its link means at least one merchant account is funded by Chase.
- It serves as a portal to account-tailored articles that are available through direct links and are not discoverable through Braintree's support-site search. The page recommends bookmarking the portal for later retrieval.
- Braintree explains that accepted payment types and other processing details can vary by banking partner, while generic public support articles can omit important account-specific details.
- The partner bank is determined during the application process and depends mostly on signup timing and business domicile. A merchant with multiple merchant accounts can have more than one partner bank. These are page-scoped explanations, not a universal rule for every Braintree or Chase account.

> [!warning] Keep account and processor scope attached
> Do not transfer guidance reached through this portal to a different merchant account, banking partner, processor or region without reading that guidance and verifying its scope. The portal itself does not document pricing terms, transaction behavior, settlement or funding outcomes.

## Detail locators

- Chase-funded merchant-account condition: opening `**NOTE**`, raw lines 17-18.
- Portal purpose and direct-link-only discoverability: paragraph after the note, raw line 22.
- Bookmark recommendation: bold recommendation, raw line 24.
- Banking-partner variation, limits of generic support, application-time determination and multi-account qualification: final paragraph, raw line 26.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/chase/overview-2026-09-16|Braintree Chase Overview article]] - fully read 2026-09-16 snapshot describing a Chase-funded merchant-account portal, direct-link-only account guidance and banking-partner variability
