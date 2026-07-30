---
title: "Launch a Pay-as-you-go Business Model"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/pay-as-you-go"
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/pay-as-you-go-2026-07-13.md"
tags: [metronome, pay-as-you-go, usage-based-billing, contracts, pricing, stripe]
---

## Overview

This implementation guide uses the fictional AutoSales business to illustrate a pay-as-you-go packaging and provisioning flow in Metronome. It combines usage events, products, a shared rate card, a customer contract, and an optional Stripe invoice route; its request payloads are illustrative and dedicated API and integration references remain the implementation authority.

## Key takeaways

- The guide describes PayGo as paying in arrears for software resources or features used, rather than committing to a fixed subscription or long-term contract.
- Its Basic, Better, and Best illustration combines four usage products with an optional monthly AI-model fee; products limited to Better and Best receive a `premium` tag.
- The Basic example uses a tag-scoped `entitled: false` override and says that, absent a billing schedule, its usage invoice defaults to monthly.
- The worked Stripe sequence creates a Stripe customer, configures the Metronome customer with `stripe_collection_method: send_invoice`, then creates the contract; this configuration must not be described as automatically charging the card.
- The illustrative upgrade ends Basic and creates a six-month Best contract with a monthly recurring scheduled charge, but its top-level contract end field requires schema verification.

## Worked PayGo flow

The guide models four usage products and one monthly-fee product. It recommends a `premium` tag for products available only in Better and Best, then applies standard usage pricing in one rate card. The Basic contract selects that rate card and uses a tag-scoped `entitled: false` override for `premium` products.

For the optional Stripe route, the guide tells AutoSales to create the Stripe customer and add a preferred card, then gives a Metronome customer payload with `direct_to_billing_provider`, the Stripe customer ID, and `stripe_collection_method: send_invoice`. The guide's later statement that billing begins automatically preserves its worked sequence, but [[source-metronome-integrations-invoice-integrations-stripe]] says `send_invoice` emails payment instructions. That source reserves the default-payment-method requirement for `charge_automatically`; therefore this guide does not establish automatic card charging or that a preferred card is generally required for `send_invoice`.

For its illustrative upgrade, AutoSales ends the Basic contract and creates a Best contract for six months, retaining the rate card and adding a monthly `scheduled_charges` recurring schedule for the AI-model product. The guide uses top-level `ending_at` in that Best contract payload, whereas the current create-contract reference documents optional, exclusive top-level `ending_before`. The nested recurring schedule itself uses `ending_before`; retain the guide's six-month commercial intent and the scheduled charge's bound, but do not treat the displayed top-level contract payload as schema-valid without verification. The guide's end-then-create sequence is one worked upgrade path, not a general contract-lifecycle rule.

## Documentation boundaries

> [!warning] Entitlement and access wording
> The guide says a rate card with `entitlements` set to `true` can later disable product access and illustrates `entitled: false` for the `premium` tag. Existing rate-card documentation describes `entitled` as default invoice inclusion. These sources do not establish that the setting itself controls application authorization; preserve the plan-packaging example without inferring an access-control mechanism.

> [!warning] Best contract end-field mismatch
> The guide's Best example uses top-level `ending_at`, but [[source-metronome-api-reference-contracts-create-a-contract]] documents optional, exclusive top-level `ending_before`. Its nested recurring schedule separately uses `ending_before`. Verify the current create-contract schema before implementing the displayed payload.

> [!info] Stripe collection boundary
> The guide's Stripe example pairs an instruction to add a preferred card with `stripe_collection_method: send_invoice`. [[source-metronome-integrations-invoice-integrations-stripe]] describes `send_invoice` as emailed payment instructions, and requires a default payment method for `charge_automatically`; do not infer automatic card collection or a general preferred-card requirement from this `send_invoice` example.

The guide does not define complete customer or contract schemas, field requiredness, validation, idempotency, date-boundary behavior, invoice finalization, proration, numeric denomination, or invoice-destination configurations. It says invoicing and payment workflows can use destinations other than Stripe, without defining those destinations or their delivery behavior.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-usage-based-billing]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-integrations]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/pay-as-you-go-2026-07-13|2026-07-13 snapshot — pay-as-you-go packaging, provisioning, and Stripe example]]
