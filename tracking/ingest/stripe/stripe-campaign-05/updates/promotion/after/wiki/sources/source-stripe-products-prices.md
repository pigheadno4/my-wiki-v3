---
title: "Stripe Products and Prices"
type: source
date_ingested: 2026-04-20
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-products-prices-how-products-and-prices-work-2026-11-07.md"
  - "stripe-products-prices-manage-prices-2026-11-07.md"
  - "stripe-products-prices-2025.md"
  - "stripe-manage-products-prices-2025.md"
tags: [stripe, products, prices, catalog, subscriptions, checkout, invoices, pricing-models]
---

## Summary

The April 20 and [November 7, 2026 catalog overviews](https://docs.stripe.com/products-prices/how-products-and-prices-work) explain how [[stripe]] Products describe goods and services and Prices specify amounts, currencies, billing intervals, and tax behavior. Merchants can create them in the Dashboard or import a catalog using the Products and Prices APIs for Checkout, Payment Links, Subscriptions, Invoices, and Quotes.

The April 20 and [November 7, 2026 management guides](https://docs.stripe.com/products-prices/manage-prices) separately describe editing, archival, currency selection, catalog imports, and Dashboard copies.

## Key Takeaways

- **Catalog design** — November recommends one Product for each distinct customer-facing option, entitlement, tax code, or separately displayed item. For the same Product, use Prices for different intervals or currencies and a replacement Price when the amount changes. The Starter, Professional, and Enterprise example uses three Products with monthly and annual Prices for each. Checkout, Payment Links, and invoices display the Product name per line item. Items sharing a Product also share its name and description.
- **Subscription limits** — the maximum recurrence is three years. Outside flexible billing for mixed intervals, all Prices on a Subscription must share both `recurring.interval` and `recurring.interval_count`.

## Product and Price lifecycle

- **Product.** Give the Product a name. An optional custom ID can map it to your own catalog. Optional description, image and tax code affect downstream integrations. The management guide requires at least one Price to save a Product in the Dashboard. This is a Dashboard save requirement. The API also documents creating a Product with `default_price_data` in one request.
- **Price.** A Price belongs to a Product and carries the amount, currency, and recurrence or other pricing model. One Product can have multiple Prices. A default Price must be active, and the first Price added with a new Dashboard Product becomes the default.
- **Change an amount.** Create a replacement Price, switch to its ID and archive the old Price with `active=false`. The guide lists `metadata`, `nickname` and `active` in its generic edit note, separately illustrates `lookup_key` in a Price update, and documents adding currency options to an existing Price in the Dashboard. These passages do not establish an exhaustive edit-field list.
- **Archive.** Archiving a Product or Price prevents adding that item to new invoices or subscriptions. Existing subscriptions using the archived item remain active until canceled. Both archive passages say existing Payment Links using the Product are deactivated, including the paragraph about a Price. For an existing Product, archive prose links to updating `active=false`, while both archive examples submit a Product-create request with `active=false`. The create examples do not demonstrate updating the existing Product. Unarchive by updating `active=true`.
- **Delete.** The management guides say only Products without associated Prices can be deleted, while their Dashboard paragraph says to delete or archive an associated Price first. These passages leave the archive-only deletion path unresolved. The Dashboard can delete an unused Price. The Price API documents archival instead of deletion. Stripe retains archived catalog information for transaction history.

## Product vs Price

| | Product | Price |
| --- | --- | --- |
| Defines | What you sell | How much and how often |
| ID | Merchant may choose an ID | Stripe-generated |
| Creation | Name required | Currency and Product association, with amount parameters depending on billing scheme |
| Other fields | Description, image, tax code, and the optional `default_price` pointing to a Price | Recurring fields for recurring Prices. When calculating taxes, `tax_behavior` is required if no default is configured in Stripe Tax. An explicit `inclusive` or `exclusive` value cannot be changed. |

For `POST /v1/prices`, pass an existing Product ID via `product` or create the related Product with `product_data.name`, as shown in the November Invoice Items API example's `createPrice` prerequisite. For non-tiered Prices, the November Prices API reference requires one of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount`. Tiered Prices use `billing_scheme=tiered`, `tiers`, and `tiers_mode`. Set or change the default Price on the Product.

## Price Types

| Type | Notes |
| --- | --- |
| One-time | Single charge |
| Recurring | Subscription billing with a recurrence interval |
| Inline (`price_data`) | API-created for a specific Checkout Session, Payment Link, Subscription or invoice and excluded from Dashboard catalog listings and searches. The direct Dashboard URL remains available, and associated Products may persist. The management guide says the inline Price is effectively archived by default and cannot be updated or reused. |
| Pay-what-you-want | Customer chooses the amount for a one-time payment |
| Multi-currency | One Price can offer amounts in multiple currencies |
| Tiered / usage-based | Tiered amounts use volume or graduated tiers. Usage-based prices can charge per unit of reported usage or use tiered billing. |

When the merchant explicitly passes amount and currency for an API invoice item or charge, Stripe uses those values. The November catalog overview assigns the choice of localized amount and currency to the merchant in these cases. It recommends `pricing.price` to pass a Price ID for invoice items. Automatic localization is unverified across Price-ID routes.

## Compatibility Table (key entries)

These entries are the same in the April and November catalog overviews.

| Feature | Checkout | Payment Links | Quotes | Subscriptions | Invoices |
| --- | --- | --- | --- | --- | --- |
| Product images | ✓ | ✓ | Ignored | Ignored | Ignored |
| Recurring prices | ✓ | ✓ | ✓ | ✓ | ✓ |
| Multi-currency prices | ✓ | ✓ | Ignored | ✓ | Ignored |
| Tiered prices | ✓ | **Disallowed** | ✓ | ✓ | ✓ |
| Usage-based prices | ✓ | **Disallowed** | ✓ | ✓ | ✓ |
| Decimal amounts | ✓ | **Disallowed** | ✓ | ✓ | ✓ |
| Customer chooses price | ✓ | ✓ | **Disallowed** | **Disallowed** | **Disallowed** |

**Disallowed** means the feature precludes using that Product or Price with the listed API. **Ignored** means the feature has no effect and the Product or Price remains usable.

The separate November 7 Payment Links create guide lists flat-rate or tiered pricing for recurring products and flat-rate or package pricing for one-off products. Its tiered wording conflicts with the two catalog tables. Its flat-rate request examples document the creation routes below and leave exact tiered support by route, subtype, and version unresolved. They do not establish general support for metering, decimal amounts, or all package combinations. See [[stripe-payment-links]].

## How Each API Uses Prices

- **Checkout** — specify a Price ID per line item or use inline `price_data`. The Session computes totals and shows the Product name and image. The management guides describe selecting a supported local currency based on IP, with default-currency fallback and an explicit `currency` option. Applicable Prices, coupons, promotion codes and shipping rates in a Session must share a default currency and all support the local currency for automatic selection.
- **Payment Links** — create the link in the Dashboard or use `POST /v1/payment_links`. The November create guide demonstrates `line_items[][price]` for an existing Price ID or `line_items[][price_data]` with `product_data` to create a Product and Price inline. Both examples include a quantity. The link computes totals and shows the Product name and image. The management guide describes local-currency selection when all included Prices support it, default fallback, and a `currency` override. The Prices must share a default currency.
- **Subscriptions** — use recurring Prices. Outside flexible billing the intervals and counts have to match. The separate May mixed-interval guide describes flexible billing, interval alignment, and API version requirements. The November mixed-interval selector routes to Dashboard and API variants. See [[stripe-subscriptions]] and [[stripe-subscriptions-mixed-interval]]. Checkout uses its currency-selection flow. For directly created subscriptions, pass `currency` to select a nondefault option. Subscription schedules use `phases.currency` and otherwise follow the Price default.
- **Quotes** — specify a Price ID for a one-off invoice or subscription, or select a Product in the Dashboard. On customer acceptance Stripe creates the relevant billing objects. Acceptance does not establish collection. The management guides say Quotes use the Price’s default currency.
- **Invoices** — a Price ID can identify the line item's Price. Stripe uses `product.name` when rendering the invoice on the web or as a PDF. The separate November Invoice Items API reference also documents inline `price_data` and the explicit amount and currency fields. When selecting a multi-currency Price’s currency for an invoice item, explicitly pass `currency` even if it matches the Customer default. The management guides say omitting the parameter prevents this multi-currency path from working.

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
- [[paypal-subscriptions]] — PayPal's equivalent subscription/plan model

## Raw Sources

- [[raw/stripe-products-prices-how-products-and-prices-work-2026-11-07|November 7, 2026 Products and Prices overview]]
- [[raw/stripe-products-prices-manage-prices-2026-11-07|November 7, 2026 Products and Prices management guide]] — Dashboard and API management paths.
- [[raw/stripe-products-prices-2025|April 20, 2026 Products and Prices overview]] — custom IDs, amount replacement, price_data, compatibility, subscription constraints, and archive rules
- [[raw/stripe-manage-products-prices-2025|April 20, 2026 Manage Products and Prices guide]] — CRUD operations, lookup_key and transfer_lookup_key, multi-currency per-API rules, rounding per line item, delete rules, one-time copy to live mode, and import synchronization
