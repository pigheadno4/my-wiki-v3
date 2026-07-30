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

This implementation guide uses the fictional AutoSales business to show a pay-as-you-go packaging and provisioning flow in Metronome. It combines usage events, products and a shared rate card, a customer contract, and an optional Stripe invoice-and-payment route; the request payloads are illustrative rather than a complete API schema.

## Key takeaways

- PayGo charges for software resources or features used in arrears instead of a fixed subscription or long-term commitment, and the guide positions it for low-friction, self-serve product growth.
- The example packages Basic, Better, and Best plans by enabling product combinations, with a monthly AI-model fee in the Best offering.
- Its setup uses usage events, five products, a `premium` product tag, and one rate card; the narrative says the card starts with entitlements enabled and a plan can later disable selected products.
- The Stripe example creates the Stripe customer before the Metronome customer so the Stripe customer ID can be placed in Metronome's billing-provider configuration.
- The Basic contract example disables the `premium` tag with an `entitled: false` override and defaults its usage invoice to monthly because no billing schedule is supplied; the Best example instead creates a bounded, monthly recurring scheduled charge.

## Worked PayGo flow

The guide models four usage products and one monthly-fee product. It recommends tagging products available only in the Better and Best offerings as `premium`, then using a rate card with the standard usage prices. The Basic contract example selects that rate card and uses a tag-scoped `entitled: false` override to exclude `premium` products.

For the optional Stripe route, the guide first creates a Stripe customer with the payment method, then creates the Metronome customer with a `customer_billing_provider_configurations` entry for Stripe, `direct_to_billing_provider`, the Stripe customer ID, and `send_invoice`. The returned Metronome customer ID is used to create the contract. Once the contract and linked Stripe customer exist, the guide says Metronome begins billing automatically.

For the illustrated upgrade, AutoSales ends the existing Basic contract and creates a new, six-month Best contract. That contract retains the rate card and adds a monthly `scheduled_charges` recurring schedule for the AI-model product. The guide says to retain each generated contract ID for later operations.

## Documentation boundaries

> [!info] Illustrative implementation boundary
> This guide does not define the complete customer or contract request schemas, field requiredness, validation, idempotency, date-boundary behavior, invoice finalization, proration, or the numeric denomination of the scheduled-charge example. Dedicated customer, contract, rate-card, and Stripe-integration references remain the implementation authority.

> [!warning] Entitlement and access wording
> The guide says `entitlements` can later disable product access and illustrates `entitled: false` for the `premium` tag. Existing rate-card documentation describes `entitled` as default invoice inclusion. These sources do not establish whether that setting itself controls application authorization; retain the guide's plan-packaging example without inferring an access-control mechanism.

The guide's end-current-contract then create-new-contract sequence is one worked upgrade path, not a general lifecycle rule. Its statement that invoicing and payments can go to destinations other than Stripe likewise does not define those destination configurations or delivery behavior.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-usage-based-billing]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-integrations]]
- Related sources: [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/pay-as-you-go-2026-07-13|2026-07-13 snapshot — pay-as-you-go packaging, provisioning, and Stripe example]]
