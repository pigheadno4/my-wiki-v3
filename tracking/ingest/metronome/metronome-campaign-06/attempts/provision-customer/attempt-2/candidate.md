---
title: "Metronome Provision a Customer"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/provision-customer"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/provision-customer-2026-07-13.md"
tags: [metronome, customers, contracts, ingest-aliases, billing-integrations, marketplaces]
---

## Overview

This implementation guide describes provisioning a Metronome customer as an invoice recipient, including assigning ingest aliases and optional billing-provider configurations. A customer must have at least one contract before it can start rating for billing; customer provisioning is therefore distinct from assigning the contract that selects the billing destination.

## Key takeaways

- An ingest alias maps an internal customer identifier to a Metronome customer ID, so usage sent with that alias is associated with the correct customer without replacing the application's identifier.
- Aliases can model a parent enterprise and sub-organizations, and an alias added later to an existing customer retroactively associates earlier usage keyed on that alias.
- The guide supports application-UI creation or programmatic creation from sales-led and product-led system triggers. Its API example stores an SFDC account identifier in a customer custom field.
- One customer can have multiple `customer_billing_provider_configurations`, but each contract is assigned one configuration and can therefore bill to one configured system. The relevant external billing system must be connected before its customer configuration is set up.
- An AWS Marketplace customer configuration can be supplied at creation or added later. Creating it on the customer alone does not route invoices to AWS; a contract must select it as its `billing_provider_configuration`.

## Customer identity and creation flows

An ingest alias lets a producer keep its own customer entities while Metronome resolves usage to the corresponding customer. The guide also presents aliases as an account-hierarchy mechanism: an enterprise can be the Metronome customer and its sub-organizations can be aliases attached to it. Group keys can then change the generated invoice's presentation for sub-organization usage.

Aliases may be supplied when the customer is created or later. The page says a later alias assignment retroactively associates usage already sent with that alias, which can keep Metronome out of the customer-signup hot path while usage is metered.

The app flow is: open **Customers**, select **Add a customer**, add a name and ingest alias, and optionally set a customer custom field in **Settings**. For programmatic flows, the source gives a sales-led example in which a Salesforce CPQ opportunity closing triggers an API job; it describes an analogous product-led flow triggered by website signup. The illustrated `POST /v1/customers` payload contains `ingest_aliases`, `name`, and an `sfdc_account_id` custom field.

## Billing configuration and contract assignment

The guide describes `customer_billing_provider_configuration` as a customer-level record for a billing destination. It must be created before it can be assigned to a contract. A customer can hold multiple configurations, so its contracts can route to different systems, one per contract. Before setting up a configuration, Metronome must be connected to the relevant billing system; the page points to Stripe invoicing and AWS/Azure marketplace setup.

For the AWS Marketplace example, the creation payload includes `billing_provider: aws_marketplace`, `aws_customer_id`, `aws_product_code`, `aws_region`, and `delivery_method: direct_to_billing_provider`. The resulting customer has the AWS configuration, but billing to AWS begins only after a contract is created with that configuration as its `billing_provider_configuration`. If the customer was created without a configuration, the page says `/setCustomerBillingProviderConfigurations` can add one later.

> [!warning] Archiving boundary
> The source labels archival behavior beta. It says a customer billing-provider configuration can be archived with the customer or through `/archiveCustomerBillingProviderConfigurations`; it then becomes reusable on a new customer. If an archived configuration is attached to an active contract, it is archived on that contract immediately and no longer bills to its associated destination.

## Documentation boundaries

This guide does not define the full customer API request or response schema, required fields, alias limits, authentication, idempotency, validation errors, billing-provider configuration schema for systems other than the AWS example, contract creation request shape, or invoice lifecycle. The dedicated customer-creation, contract-creation, and billing-integration references remain the authority for those details.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-integrations]], [[metronome-invoicing]]
- Related sources: [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/provision-customer-2026-07-13|2026-07-13 snapshot — customer provisioning, ingest aliases, and billing configuration]]
