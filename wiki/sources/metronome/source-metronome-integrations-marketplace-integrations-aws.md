---
title: "Invoice with AWS Marketplace"
type: source
date_ingested: 2026-08-24
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/marketplace-integrations/aws.md"
raw_files:
  - "metronome/integrations/marketplace-integrations/aws-2026-07-13.md"
tags: [metronome, aws-marketplace, marketplace-invoicing, metering, billing-providers]
---

## Overview

This guide documents the native Metronome-to-AWS Marketplace invoicing path: prepare an AWS listing, delegate AWS metering and entitlement access to Metronome through a cross-account IAM role, map each Marketplace customer into Metronome, and select AWS on that customer's contract. The guide also defines what Metronome sends to AWS and identifies correction, cutoff, currency, lifecycle, and true-up limits that remain merchant-owned.

The page is an integration guide rather than a complete API or settlement contract. Its configuration steps and returned or entered identifiers do not by themselves prove AWS acceptance, activation, downstream delivery, payment, tax, settlement, or reconciliation.

## Listing and pricing prerequisites

An organization must first be an approved AWS Marketplace seller. The listing uses **Units** as the dimension unit type and chooses one of two sales motions that must also be represented when the Marketplace customer is configured in Metronome:

- **Contract with Consumption** uses fixed-term lengths. Create one or more contract dimensions corresponding to the pricing models configured in Metronome; AWS also uses those dimensions for lifecycle events such as subscription end and renewal. Select **Single dimension per contract** and an appropriate contract duration.
- **Usage-based pricing** can be started or stopped at any time by the customer. The contract-dimension and contract-purchasing steps above are not required.

The two dimension layers have different identifier and pricing rules:

- **Contract dimensions, Contract with Consumption only:** API identifiers and display names may be chosen freely. Leave **Activate pay-as-you-go pricing for additional usage** unchecked for every contract dimension, and set every contract-dimension price to `$0`.
- **Single usage dimension:** create exactly one usage dimension for the integration and name its API identifier `usage_fee`; price it at `$0.01` per unit. The mandatory usage-dimension identifier does not constrain the freely chosen contract-dimension identifiers or display names.

The guide says deviations from the dimension prices cause the integration to fail. It does not define when or how AWS or Metronome validates the listing, what error identifies each mismatch, or whether saving configuration proves the listing is ready to receive metering records.

## IAM role and credential boundary

Metronome requires a seller-owned AWS IAM role with `aws-marketplace:BatchMeterUsage`, `aws-marketplace:GetEntitlements`, `aws-marketplace:ListEntities`, and `aws-marketplace:DescribeEntity` allowed on `Resource: "*"`. The seller configures the role's trust using the Metronome AWS account ID and unique external ID shown by the Metronome integration flow, leaves **Require MFA** unchecked, attaches the policy, and names the role with the required `metronome-marketplace` prefix. Environment-specific suffixes such as `-production` and `-staging` are permitted examples. The role ARN is then entered in Metronome and saved.

The AWS account ID, external ID, AWS account that owns the role, and role ARN are distinct identifiers. The page does not document least-privilege resource scoping beyond the shown wildcard, credential validation timing, role rotation, external-ID rotation, independent update, rollback, deletion, audit evidence, or recovery if AWS access later fails.

## Customer and contract identifier layers

| Layer | Documented identity or selection |
| --- | --- |
| AWS listing | Product code, region, pricing model, and marketplace dimensions |
| Metronome account integration | Metronome AWS account ID, generated external ID, and seller role ARN |
| Customer billing-provider configuration | AWS customer ID, AWS product code, AWS region, and conditional `aws_is_subscription_product` |
| Contract routing | AWS Marketplace as the contract's billing provider with direct provider delivery |

The AWS customer ID comes from the token sent to the listing's fulfillment URL. The product code comes from the AWS Marketplace Portal. The guide recommends `us-east-1` unless another region was deliberately selected and says a wrong region returns an error that the AWS customer cannot be found. The usage-based checkbox, or `aws_is_subscription_product` in the API examples, is used only for an AWS **Usage-based pricing** product and is omitted or left unselected for **Contract with Consumption**.

A Metronome contract must reflect the Marketplace contract or subscription, including relevant commits and credits, and select AWS under billing configuration. The alternative API examples attach `customer_billing_provider_configurations` during customer creation or set the configuration for an existing customer, then put `billing_provider: "aws_marketplace"` and `delivery_method: "direct_to_billing_provider"` on contract creation. These examples establish the documented layer separation but do not replace the dedicated customer and contract API schemas, validation, idempotency, or recovery authorities.

> [!warning] Billing-provider lifecycle contradiction
> This AWS guide says a billing provider cannot be added or changed after the contract is created. [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] instead documents later provider changes through a contract provider schedule, including next-period transitions to or from AWS Marketplace. The sources do not state whether the AWS sentence is stale, UI-specific, or limited to initial contract configuration. Verify the applicable product and API lifecycle before implementation.

## Metering semantics

After AWS is configured for the customer, selected on the contract, and usage events are sent, Metronome begins metering calculated invoice totals to AWS. Each metering request sums the amount accrued since the previous request across all of that customer's contract invoices whose billing provider is AWS. The AWS metering-record quantity is the total dollar amount expressed in USD cents. The guide does not specify request cadence, rounding, duplicate-record handling, acknowledgement state, read-after-write visibility, or reconciliation keys.

Credits and commits have marketplace-specific treatment:

- **Prepaid commits:** Metronome meters the amount owed on the service-period date of each scheduled invoice, not its creation timestamp.
- **Credits:** Because contract credits are unpaid, only invoice overage after the credit is fully drawn down is metered.
- **Postpaid commits:** Usage reflected on invoice totals is metered during the contract, but an end-of-contract shortfall true-up invoice is not sent to AWS. The merchant must handle that true-up directly in the marketplace because Metronome finalizes it after its grace period, when the Marketplace metering endpoint has closed.

> [!warning] Marketplace coverage qualification
> [[source-metronome-guides-invoices-overview]] says marketplace invoicing supports all Metronome charge types. This dedicated AWS guide says a postpaid-commit true-up is not sent and that only USD invoices are delivered. Treat the overview as a routing summary and preserve these AWS-specific delivery exclusions.

## Lifecycle, correction, outage, and currency limits

When Metronome detects a Marketplace subscription lifecycle change, it stops metering and updates the customer's Metronome status. The merchant remains responsible for representing that status in its own application and, when relevant, ending the Metronome contract. The guide names the app's contract-end-date control and `/contracts/updateEndDate`, but it does not reconcile that route name with other contract-edit documentation; verify the current mutation authority before calling it.

AWS Marketplace accepts only positive metering quantities. If Metronome has already sent more than the corrected bill, adding a Metronome credit cannot reduce the AWS total. Metronome instead stops billing until new usage catches up; if that is insufficient, the merchant must issue a manual AWS Marketplace refund. The page does not define pause-state visibility, automatic resumption timing, refund synchronization, or downstream accounting treatment.

AWS accepts metering requests for only one hour after a customer's Marketplace contract ends. Metronome sends a final request 15 minutes after the scheduled end, while late usage may continue to reach a Metronome invoice for up to 24 hours after the billing period; usage arriving after the Marketplace cutoff cannot be billed through AWS. After an outage, Metronome includes accrued usage in the next request, but cannot recover it once the contract has ended and AWS's one-hour window has elapsed. Ingestability or Metronome invoice inclusion is therefore not proof of AWS billability.

The integration supports only USD-fiat invoices. Metronome errors when an AWS-billed contract's rate card uses a non-USD fiat currency. If the contract also has other non-USD invoices, such as scheduled-charge invoices, only its USD invoices are sent to AWS. The page does not define mixed-currency aggregation, conversion, tax, rounding beyond the USD-cent metering quantity, or reconciliation of excluded invoices.

## Operational unknowns and ownership

The guide assigns listing creation, AWS seller approval, product fulfillment setup, customer fulfillment-token decoding, accurate contract provisioning, application lifecycle state, direct true-up handling, and manual refunds to the merchant or AWS-side workflow. Metronome owns calculation and the described metering attempts once the required configuration and usage are present.

It does not define AWS acceptance and entitlement propagation after setup, activation or health checks, exact metering schedule, AWS-side record identity, partial failure, retry policy, concurrency, rollback, role rotation, alerting, payment collection, tax, settlement, disputes, remittance, financial reconciliation, or proof that an AWS invoice or payment completed. Operators need separate AWS and Metronome authorities and production evidence for those outcomes.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-integrations]], [[metronome-security-principles]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-event-ingestion]]
- Related sources: [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/integrations/marketplace-integrations/aws-2026-07-13|2026-07-13 snapshot - AWS Marketplace listing, IAM, customer provisioning, metering, and lifecycle limits]]