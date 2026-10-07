---
title: "Braintree PayPal Commerce Channel API — Getting Product Information"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/getting-product-information"
raw_files:
  - "braintree/docs/guides/paypal-commerce-channel-api/getting-product-information-2026-09-16.md"
tags: [braintree, paypal-commerce-channel-api, product-search, retailer, sku]
---

## Overview

This collected, unversioned Braintree website guide describes getting a retailer's product information through the PayPal Commerce Channel API after obtaining a retailer-specific access token. Its request example uses the Braintree sandbox Commerce endpoint; the snapshot does not establish current API availability, merchant or channel eligibility, production enablement, or an exact SDK or API version. See [[braintree]] and the provider-level route [[braintree-payment-platform]].

## Key takeaways

- The documented search supports SKU, product URL, combined name-and-description text, and name-only query parameters. Results are products containing variants; each variant has a unique SKU. Exact query forms and the sample sandbox request are kept in the raw locators.
- No matches return an empty collection. The guide identifies product `in_stock` and each variant's `sku` as properties to track, and says the selected variant SKU must be passed when a user proceeds to place an order.
- The page permits caching search results for up to a few minutes, then says the linked ordering flow obtains up-to-date product information when calculating the full cost. This snapshot-specific guidance is not a guarantee of current data freshness, inventory, price, availability, or a successful order.
- Each product can include a `web_buy_link`, described as a URL for purchase through PayPal Commerce's web client and an alternative to constructing a channel-owned purchasing experience. The presence of a link or this documented option does not prove current availability, eligibility, purchase completion, fulfillment, settlement, or funding.

## Detail locators

- **Access-token scope and search dimensions:** `Getting Product Information` (raw lines 14–23).
- **Sandbox request example:** raw lines 25–33.
- **Product and variant response structure:** raw lines 34–144; field values are examples rather than guarantees.
- **Empty results and tracked properties:** raw lines 145–148.
- **Selected SKU, short caching guidance, refreshed full-cost information, and hosted web-buy alternative:** raw lines 150–153.

## Related

- [[braintree]]
- [[braintree-payment-platform]]
- [[source-braintree-docs-guides-paypal-commerce-channel-api-ordering-a-product|Braintree PayPal Commerce Channel API — Ordering a Product]] — linked follow-on navigation

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-channel-api/getting-product-information-2026-09-16|Braintree PayPal Commerce Channel API — Getting Product Information (2026-09-16 snapshot)]]
