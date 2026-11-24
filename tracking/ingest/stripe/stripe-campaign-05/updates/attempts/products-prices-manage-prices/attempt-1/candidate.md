---
title: "Stripe Products and Prices"
type: source
date_ingested: 2026-04-20
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-products-prices-manage-prices-2026-11-07.md"
  - "stripe-products-prices-2025.md"
  - "stripe-manage-products-prices-2025.md"
tags: [stripe, products, prices, catalog, subscriptions, checkout, invoices, pricing-models]
---

## Summary

Products define what a business sells. Prices define how much and how often the business charges. These objects support Checkout, Payment Links, Subscriptions, Invoices and Quotes.

The April 20, 2026 overview at https://docs.stripe.com/products-prices/how-products-and-prices-work describes catalog objects and compatibility. The April 20 and November 7, 2026 captures of https://docs.stripe.com/products-prices/manage-prices describe Dashboard and API catalog management. Each guide has its own scope.

## Product and Price lifecycle

- **Product.** Give the Product a name. An optional custom ID can map it to your own catalog. Optional description, image and tax code affect downstream integrations. The management guide requires at least one Price to save a Product in the Dashboard. This is a Dashboard save requirement. The API also documents creating a Product with `default_price_data` in one request.
- **Price.** A Price belongs to a Product and carries the amount, currency, and recurrence or other pricing model. One Product can have multiple Prices. A default Price must be active, and the first Price added with a new Dashboard Product becomes the default.
- **Change an amount.** Create a replacement Price, switch to its ID and archive the old Price with `active=false`. The guide lists `metadata`, `nickname` and `active` in its generic edit note, separately illustrates `lookup_key` in a Price update, and documents adding currency options to an existing Price in the Dashboard. These passages do not establish an exhaustive edit-field list.
- **Archive.** Archiving a Product or Price prevents adding that item to new invoices or subscriptions. Existing subscriptions using the archived item remain active until canceled. Both archive passages say existing Payment Links using the Product are deactivated, including the paragraph about a Price. For an existing Product, archive prose links to updating `active=false`, while both archive examples submit a Product-create request with `active=false`. The create examples do not demonstrate updating the existing Product. Unarchive by updating `active=true`.
- **Delete.** The management guides say only Products without associated Prices can be deleted, while their Dashboard paragraph says to delete or archive an associated Price first. These passages leave the archive-only deletion path unresolved. The Dashboard can delete an unused Price. The Price API documents archival instead of deletion. Stripe retains archived catalog information for transaction history.

## Price types

| Type | Scope |
| --- | --- |
| One-time | Single charge |
| Recurring | Subscription billing at the specified interval |
| Inline (`price_data`) | Create a dynamic Price in the API instead of passing a stored Price ID. It is `active=false` by default and cannot be updated or reused. The April overview says it is absent from the main Dashboard catalog but viewable directly, and associated Product objects may persist. |
| Customer chooses price | One-time payments through Checkout or Payment Links |
| Multi-currency | A single Price with a default currency and additional currency options |
| Tiered / usage-based | Price tiers or usage-based pricing |

## April 2026 overview compatibility

| Feature | Checkout | Payment Links | Quotes | Subscriptions | Invoices |
| --- | --- | --- | --- | --- | --- |
| Product images | ✓ | ✓ | Ignored | Ignored | Ignored |
| Recurring prices | ✓ | ✓ | ✓ | ✓ | ✓ |
| Multi-currency prices | ✓ | ✓ | Ignored | ✓ | Ignored |
| Tiered prices | ✓ | Disallowed | ✓ | ✓ | ✓ |
| Usage-based prices | ✓ | Disallowed | ✓ | ✓ | ✓ |
| Decimal amounts | ✓ | Disallowed | ✓ | ✓ | ✓ |
| Customer chooses price | ✓ | ✓ | Disallowed | Disallowed | Disallowed |

The overview uses **Disallowed** where the Product or Price cannot be used with the API, and **Ignored** where the resource is usable but the feature has no effect. The April and November management guides document an explicit invoice-item currency path below.

## Integration and multi-currency selection

- **Checkout.** Supply each line-item Price ID. Checkout renders the Product name and image. The management guides describe selecting a supported local currency based on IP, with default-currency fallback and an explicit `currency` option. Applicable Prices, coupons, promotion codes and shipping rates in a Session must share a default currency and all support the local currency for automatic selection.
- **Payment Links.** Create a link from the catalog. It renders the Product name and image. The guide describes local-currency selection when all included Prices support it, default fallback, and a `currency` override. The Prices must share a default currency.
- **Subscriptions.** Use recurring prices. The April overview sets a three-year maximum interval and requires matching `recurring.interval` and `recurring.interval_count` unless flexible billing mode is used to support mixed intervals. Checkout uses its currency-selection flow. For directly created subscriptions, pass `currency` to select a nondefault option. Subscription schedules use `phases.currency` and otherwise follow the Price default.
- **Quotes.** Use a Price ID or select a Product in the Dashboard. Accepted quotes can create the associated invoice or subscription. The management guides say Quotes use the Price’s default currency.
- **Invoices.** Use the Price ID for API invoice items. The invoice uses the Product name in the PDF. When selecting a multi-currency Price’s currency for an invoice item, explicitly pass `currency` even if it matches the Customer default. The management guides say omitting the parameter prevents this multi-currency path from working.

## Catalog operations and tests

- **Lookup keys.** Retrieve Prices by `lookup_key`. To publish a replacement amount under the same lookup key, create a Price with `transfer_lookup_key=true`. Expand `currency_options` to retrieve currency-specific amounts.
- **Rounding.** For decimal pricing, the management guides round invoice line items after multiplying unit amount by quantity, before summing. They separately distinguish invoice-level automatic tax rounding from configurable manual tax rounding.
- **Import synchronization.** Map your Product IDs, keep Stripe Price IDs and compare current amounts. The guide’s one-active-Price convention applies to this example synchronization pattern. If the amount differs, create a replacement Price and make the old one inactive.
- **Dashboard copy to live.** The April management guide says a test Product can be copied once. The November guide says the same sandbox Product can be copied repeatedly from the Dashboard. Associated Prices copy and each copy creates a separate live Product. On both dates, later test or sandbox edits do not propagate to existing live copies.

## Detail locators

- November management lines 18–170 and 422–500 cover Product and Price creation, archival, deletion and updates. Lines 232–275 cover defaults and inline Prices.
- November management lines 277–409 cover currency options, product-specific selection, lookup keys and rounding. Lines 506–557 cover import and synchronization. November lines 591–595 and April management lines 697–701 record the dated Dashboard copy rules.
- April catalog overview lines 63–75 cover inline Price visibility. Lines 109–137 cover compatibility and recurring interval limits.

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-checkout]] — Checkout integration concept
- [[source-stripe-checkout-sessions]] — Checkout Sessions API
- [[paypal-subscriptions]] — PayPal's subscription and plan model

## Raw Sources

- [[raw/stripe-products-prices-manage-prices-2026-11-07|November 7, 2026 Products and Prices management guide]] — Dashboard and API management paths.
- [[raw/stripe-products-prices-2025|April 20, 2026 Products and Prices overview]] — catalog model, compatibility, inline pricing and subscription constraints.
- [[raw/stripe-manage-products-prices-2025|April 20, 2026 Products and Prices management guide]] — historical CRUD, lookup keys, currencies, import and test copy guidance.
