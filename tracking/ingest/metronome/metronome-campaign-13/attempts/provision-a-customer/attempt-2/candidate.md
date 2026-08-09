---
title: "Provision a customer"
type: source
review_level: independent
date_ingested: 2026-08-04
canonical_url: "https://docs.metronome.com/guides/customers-billing/manage-customers/provision-a-customer.md"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/manage-customers/provision-a-customer-2026-07-13.md"
tags: [metronome, customers, contracts, ingest-aliases, billing-provider-configurations, usage-filters]
---

## Overview

This guide explains Metronome customer provisioning as creation of a customer object plus one or more associated contracts. It covers prerequisites, app and API customer creation, ingest aliases, billing-provider configurations, contract terms, invoice consolidation, discounts and overrides, usage filters, and custom fields. A customer needs at least one provisioned contract before metering and rating for billing can start.

## Key takeaways

- Provisioning starts with usage events connected to Metronome, a billable metric, a product, and a rate card.
- Ingest aliases map internal customer identifiers to a Metronome customer ID. They can model sub-organization hierarchies, split usage in invoice presentation, and be added retroactively so earlier alias-keyed usage is associated with the customer.
- Billing-provider configurations are created on the customer and then assigned to contracts. Multiple configurations allow one customer to be billed in multiple systems, one per contract; the AWS example is not billed to AWS until a contract uses that provider configuration.
- Contracts reference rate cards and can bundle commits, discounts, fixed products, and scheduled charges. The worked WidgetsExpress example combines a one-year prepaid commit with a recurring quarterly platform fee.
- Multiple contracts can use distinct rate cards, dates, and discounts. Usage filters route events to a selected contract, with documented group-key requirements for streaming and SQL billable metrics.

## Details

### Prerequisites and customer creation

The page requires connected usage events, a billable metric, a product, and a rate card. The app flow is Customers → Add a customer, followed by a name, an ingest alias, and optionally a custom field on Settings. The API example posts to `/v1/customers` with `ingest_aliases`, `name`, and a `custom_fields.sfdc_account_id` value. The guide describes both sales-led workflows (for example, scheduling creation after a Salesforce CPQ opportunity closes) and product-led workflows triggered by website signup.

### Ingest aliases

An ingest alias lets existing customer identifiers remain in usage payloads while Metronome associates that usage with the correct customer. The guide also uses aliases to attach enterprise sub-organizations to one parent customer and says group keys can change invoice presentation. Aliases may be set at creation or later; the retroactive example sends usage keyed by an alias first and adds that alias to an existing customer later.

### Billing-provider configuration

Before configuring a billing destination, the relevant system must be connected; the page points to Stripe and AWS/Azure Marketplace integration guides. It recommends setting `customer_billing_provider_configurations` during customer creation. The AWS example includes `billing_provider: "aws_marketplace"`, customer/product/region configuration, and `delivery_method: "direct_to_billing_provider"`. The customer is created with that configuration, but billing to AWS starts only after a contract sets AWS as its `billing_provider_configuration`; if omitted initially, `/setCustomerBillingProviderConfigurations` can add one later. A BETA note says a configuration can be archived with the customer or through `/archiveCustomerBillingProviderConfigurations`; an archived configuration becomes reusable on a new customer, and an active contract using it is archived immediately and no longer bills to that destination.

### Contract provisioning

A contract encodes products, rates, and access duration, references a specific rate card, and can include commits, discounts, fixed products, and other terms. The app sequence selects the customer, adds a contract, fills in basic information and an AWS billing provider, then adds a prepaid commit and scheduled charge. The example contract describes a $10,000 one-year prepaid commit for cloud products plus a $1,000 quarterly platform fee, with the commit paid upfront and usage billed monthly. The `/contracts/create` example includes a customer, rate-card alias, start time, billing-provider configuration, prepaid commit schedules, recurring scheduled charges, and a monthly usage-statement schedule anchored to contract start.

### Invoice consolidation

The optional `scheduled_charges_on_usage_invoices` setting applies to all contract charges, including commits. The page says consolidation is selected when the exclusive last day of the usage service period matches the scheduled invoice date and the corresponding usage invoice has not finalized. Consolidation happens when the contract is created and after future contract changes. In the `ALL` example, January's finalized invoice contains the monthly charge, February's draft invoice combines the monthly charge with January usage, and later invoices follow that model if the contract does not change.

### Discounts and overrides

Discounts can be supplied at contract creation or by editing an existing contract, using credits, product-rate overrides, price tiers, and other terms. With dimensional pricing, the guide says to set overrides for each group-key/product combination. Its WidgetsExpress example overrides cloud-tagged products to 5% below the basic rate card, represented in the API example by a `multiplier` of `0.95`.

### Usage filters

A customer can hold several contracts at once, with distinct rate cards, dates, and discounts, while drawing on shared customer-level commits and credits. A usage filter routes usage to one contract; the example assigns `region = US` to a US contract and later schedules an update that includes both US and EU. For streaming billable metrics, the usage-filter group key must exist on the underlying metric (and in a compound group key when dimensional pricing and presentation keys are also used). For SQL billable metrics, the group key must be present as a property in the underlying events, such as `properties.region`.

### Custom fields

Custom fields add metadata to a contract or commit and can support downstream revenue-recognition workflows. The SFDC example maps a `salesforce_opportunity_id` to Metronome contracts and revenue derived from them.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/manage-customers/provision-a-customer-2026-07-13|2026-07-13 snapshot — Provision a customer]]
