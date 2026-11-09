---
title: "Stripe Billing — Migrate to Stripe Tax"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/taxes/migration"
raw_files:
  - "stripe-billing-taxes-migration-2026-11-07.md"
  - "stripe-billing-taxes-migration-2026.md"
tags: [stripe, billing, subscriptions, tax, stripe-tax, migration, automatic-tax]
---

## Overview

The May 13 and November 7, 2026 captures describe two ways to migrate existing [[stripe]] Billing subscriptions to [[stripe-tax]]: automated Dashboard tooling and manual updates through Dashboard or API. Activate Stripe Tax first. Tax is calculated from product classification and customer location; the guide does not establish a completed migration, tax assessment or payment for any account.

## Automated migration

- The November guide limits the automated tool to **live mode**; it does not support sandboxes, test subscriptions, or legacy test mode for existing users. To test automatic tax on future sandbox invoices, edit each subscription in the Dashboard and enable **Calculate tax automatically**.
- In the live-mode migration tool, review subscriptions and recommended actions, choose whether to include subscriptions without a billing address, inspect projected results, and confirm. The include-without-billing-address option is enabled by default, but can be disabled; its presence does **not** mean every such subscription qualifies for inferred location. The projected breakdown distinguishes billing-address, inferred-location and unresolved outcomes. Remaining subscriptions need manual updates.
- The automated path covers active subscriptions not already collecting tax automatically, with price `tax_behavior` set and either sufficient address information or an eligible inferred location. Subscriptions with schedules, and subscriptions using Connect destination charges or separate charges and transfers, require manual updates.
- Stripe removes manual tax rates and emails on completion. The **May 13 capture** says removal could take up to **five business days**; the November guide no longer gives a completion duration. The automated tax change is not prorated and takes effect at the next billing cycle. Wait a few days before rerunning the tool; check and fix subscriptions that failed in the first attempt meanwhile.

## Inferred locations and eligibility

- The November guide says Stripe checks shipping and billing addresses, payment-method billing details, and IP address before considering inferred location. It uses inference only if all higher-priority sources are missing or empty, **not** when a present higher-priority address is invalid or incomplete. Inference applies only when the alternative is collecting no tax at all. When none of those sources is available, Stripe can match customer email to previous transaction location data in its first-party network; missing email or no match can leave a subscription unresolved.
- Using inferred locations requires an active customer portal with address updates enabled so customers can provide a full address. Inference may contain country, postal code and first address line. Without a street address, a postal code may not identify the exact jurisdiction where rates vary within that postal-code area; this is a precision warning, not evidence that a particular invoice is wrong. The guide labels inferred locations in customer or transaction details.
- Once eligible migration stores an inferred location, changing email or name does not recalculate it. A valid billing or shipping address takes precedence. Any non-empty invalid or incomplete address also takes precedence and invokes invalid-location behavior. Clearing an address can reuse previously stored inference only when no higher-priority source remains; clearing does not create a new inference or refill the address fields.

## Manual migration

1. Check customer tax location through Dashboard, export, or a Customer retrieve request with `tax` expanded; the default response omits that field. `supported` means the location is usable for automatic tax. `unrecognized_location` calls for a usable address. `not_collecting` means a recognized jurisdiction lacks an active collection registration; proceeding assesses no tax unless an appropriate registration is added. `failed` calls for retry or support. The guide's Customer API examples are Node.js in May and curl in November.
2. Set a product `tax_code` where needed; otherwise Stripe Tax uses the preset product tax code in settings. Set a price's `tax_behavior` to `exclusive` or `inclusive` as needed. Once set to either value, `tax_behavior` cannot be changed on that price; create a new price and archive the old one to change behavior.
3. For subscriptions without existing tax rates, enable `automatic_tax.enabled=true` for subsequent invoices. With existing rates, clear both subscription `default_tax_rates` and each item's `tax_rates`, enable automatic tax, and use `proration_behavior=none`; the Dashboard path clears existing rates. The May API example uses Node.js, while November uses curl for the no-rate case and Ruby for rate clearing. Those example changes do not establish SDK deprecation.
4. For a subscription schedule that sets `automatic_tax[enabled]=false`, remove that setting from all phases, set `default_settings.automatic_tax.enabled=true`, and pass all current and future phases on update. To avoid a prorated item, the guide also describes an **API-only** scheduled update: preserve manual rates in the current phase and enable automatic tax with cleared rates in the next phase. The examples are Node.js in May and curl/Ruby in November.
5. Create a preview invoice for each subscription and inspect `automatic_tax.status`, `tax`, `total_tax_amounts`, and line-item `tax_amounts`. `requires_location_inputs` calls for more customer location information; `failed` calls for retry or support. The November footnote says enabling inferred locations **might** move a previously location-blocked subscription to `complete`; it does not guarantee a particular tax amount or completed payment.

## Detail locators

- Automated tool, exclusions, projected outcome and dated completion wording: both raws, "Update existing subscriptions using automated tooling".
- Tax-location status and API expansion: both raws, "Check customer locations".
- Hierarchy, customer portal, precision warning and stored-inference behavior: November raw, "Inferred locations" and "Customer update effects on stored inferred locations".
- Product code fallback and immutable price behavior: both raws, "Update products and prices".
- Rate clearing, subscription schedules and next-cycle scheduling examples: both raws, "Update subscriptions".
- Preview statuses and conditional inferred-location footnote: both raws, "Confirm updates".

## Related

- [[stripe-tax]] — provider tax concept and reciprocal source route
- [[stripe-subscriptions]] — subscriptions context
- [[source-stripe-billing-taxes-collect]] — collecting taxes on recurring payments
- [[stripe]] — provider context

## Raw Sources

- [[raw/stripe-billing-taxes-migration-2026-11-07|Stripe Tax subscription migration guide, fetched 2026-11-07]]
- [[raw/stripe-billing-taxes-migration-2026|Stripe Tax subscription migration guide, fetched 2026-05-13]]
