---
title: "Braintree NAB-Funded Merchant Account Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/overview"
raw_files:
  - "braintree/articles/nab/overview-2026-09-16.md"
tags: [braintree, nab, merchant-account, banking-partner, funding]
---

## Overview

This collected Braintree-hosted page is a direct-link portal for a recipient with at least one merchant account funded by NAB. It routes the recipient to articles tailored to account-specific nuances, including timeline differences based on whether the recipient's business bank account is also with NAB or with another banking institution.

Treat this as a 2026-09-16 account-navigation snapshot. It does not say that NAB provisioned the merchant account, establish that every merchant account is NAB-funded, identify a region or currency, provide independent current NAB policy, document any linked target's behavior, or prove an individual payment-processing or funding outcome.

## Key takeaways

- The account-tailored articles are accessible only by direct links and cannot be found by searching Braintree's support website; the page therefore recommends bookmarking this portal.
- Payment-processing details, including accepted payment types, can vary by banking partner, so Braintree's generic public support articles can omit important account-specific details.
- The page says the partner bank was determined during the application process and depends mostly on when the merchant signed up with Braintree and where the business is domiciled. A merchant with multiple merchant accounts may have multiple partner banks.

> [!warning] Preserve the exact recipient condition
> Receipt of the link indicates that at least one merchant account is funded by NAB. Do not change this into NAB provisioning, apply it to every account, or infer a region or currency.

> [!warning] Business-bank relationship can affect timelines
> The page says some timelines differ depending on whether the business bank account is also with NAB or with another institution, but it provides no timeline values here. Read the relevant direct-link target before relying on a schedule, and do not transfer details from sibling processor or account routes.

## Detail locators

- At-least-one NAB-funded merchant-account recipient condition: `**NOTE**`, raw lines 17-18.
- Business-bank relationship and timeline variability: paragraph beginning `It’s important`, raw line 22.
- Account-tailored portal purpose and direct-link-only search limitation: paragraph beginning `This page is your portal`, raw line 24.
- Bookmark recommendation: bold recommendation, raw line 26.
- Banking-partner variability, generic-public-article limitation, application timing and domicile context, and multiple-account qualification: paragraph beginning `Certain aspects`, raw line 28.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/articles/nab/overview-2026-09-16|Braintree NAB overview]] - complete collected page covering the direct-link portal, NAB funding condition, business-bank timeline nuance and banking-partner variability
