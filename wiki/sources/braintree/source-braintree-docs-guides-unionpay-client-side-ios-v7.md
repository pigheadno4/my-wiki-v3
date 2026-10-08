---
title: "Braintree UnionPay Client-Side iOS v7 Deprecation Notice"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/unionpay/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/unionpay/client-side/ios/v7-2026-09-16.md"
tags: [braintree, unionpay, ios, client-side, deprecated]
---

## Overview

This 2026-09-16 [[braintree|Braintree]] website snapshot is routed as a client-side iOS v7 UnionPay page, but its captured body contains only an availability notice. The notice says the dedicated UnionPay integration is deprecated because UnionPay can now be processed as a credit card through its partnership with Discover, and it points readers to the credit-card guide. [[braintree-payment-methods]]

## Key takeaways

- The page provides no UnionPay iOS implementation procedure, client action or server handoff. The iOS v7 route and generic client-side title therefore do not establish behavior for an exact Braintree iOS SDK package or the separately versioned GitHub implementation.
- Treat the Discover credit-card direction as a route from this captured website notice, not as proof of current support, merchant or card eligibility, environment enablement, or a successfully executed payment.

> [!warning] Deprecated route and body mismatch
> Do not infer a working dedicated UnionPay iOS v7 flow from the URL or title. The only substantive body text deprecates that integration and redirects readers to credit-card processing through Discover.

## Detail locators

- Canonical URL, iOS v7 slug and client-side title: raw lines 1, 7 and 14.
- Dedicated UnionPay deprecation, Discover credit-card replacement direction and credit-card-guide link: `**AVAILABILITY**`, raw lines 17-18.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Credit-card guide navigation: [[source-braintree-credit-cards-overview]] (linked by this snapshot; not used here as behavioral evidence)
- UnionPay overview: [[source-braintree-docs-guides-unionpay-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/unionpay/client-side/ios/v7-2026-09-16|Braintree UnionPay client-side iOS v7 route (captured 2026-09-16)]] - complete captured page containing route metadata, the generic title and the deprecation notice
