---
title: "Adyen Marketplaces: Manage payment methods"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payment-methods/manage-payment-methods"
raw_files:
  - "adyen/docs/marketplaces/payment-methods/manage-payment-methods/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payment-methods, management]
---

## Overview

This 2026-09-15 Marketplace-path overview routes a platform to manage payment methods its users can accept through either **Customer Area** or the **Management API**. It is a capability/navigation hub, not a procedure for adding a method, a role matrix, or proof that a method is active or usable for a particular user. [[adyen]] [[adyen-platforms]] (raw lines 15–19, 28–36)

## Key takeaways

- Both paths are described as allowing the platform to list payment methods configured for its **merchant account**, view a specific method's details, update its country/region and currency, and activate or deactivate a method for a user. The merchant-account scope and user-facing action should be kept distinct; this page gives no per-store availability or activation-outcome evidence. (raw lines 19–26)
- The page links separate Customer Area and Management API instructions. It does not state API endpoints, credential roles, validation rules, deletion timing or propagation status. Consult the linked procedure for those details before changing configuration; no change is performed by this overview. (raw lines 28–36)

## Detail locators

- Raw lines 15–26: purpose, two management surfaces and four supported action categories.
- Raw lines 28–36: Customer Area and Management API child-guide routes.

## Related

- [[adyen-platforms]] — Adyen for Platforms context.
- [[source-adyen-docs-marketplaces-payment-methods-manage-payment-methods-api]] — separate Management API procedure.
- [[source-adyen-docs-marketplaces-payment-methods-add-payment-methods]] — separate method-request route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/2026-09-15|Marketplace manage payment methods overview, captured 2026-09-15]]
