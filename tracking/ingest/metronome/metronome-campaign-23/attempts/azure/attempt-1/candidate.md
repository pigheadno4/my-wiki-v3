---
title: "Metronome Integration: Azure Marketplace"
type: source
date_ingested: 2026-08-26
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/marketplace-integrations/azure.md"
raw_files:
  - "metronome/integrations/marketplace-integrations/azure-2026-07-13.md"
tags: [metronome, azure-marketplace, marketplace-billing, invoicing, integrations]
---

## Overview

This guide describes a native integration in which a merchant configures an Azure Marketplace SaaS offer and customer subscription, Metronome calculates contract invoice totals, and Metronome submits metering quantities to Azure. The merchant remains responsible for the Azure listing and activation, SaaS customer state, matching the Metronome contract to the accepted offer, lifecycle handling in its application, postpaid true-ups that miss the marketplace window, and manual refunds when Azure cannot accept a downward correction.

## Query-critical facts

- The Azure offer must use the guide's fixed metering shape: a zero-price flat-rate plan and one `usage_fee` dimension priced at `.01` with zero included quantity. Metronome says deviating from the required dimension values makes the integration fail. Metronome authentication uses the merchant's Microsoft Entra tenant ID, application/client ID, and client secret.
- Before Metronome provisioning, the customer must finish Azure Marketplace signup, exist in the merchant's SaaS system, and have an Azure subscription activated with a unique Subscription ID and `saasSubscriptionStatus` of `Subscribed`. The customer billing-provider configuration carries `azure_subscription_id`; the Metronome contract must mirror the accepted offer and select Azure delivery.
- Once Azure is selected and usage events arrive, Metronome meters the accrued total since the previous metering request across contract invoices routed to Azure. Each metering-record quantity is the total dollar amount in USD cents.
- Prepaid commit purchases are metered on the scheduled invoice's service-period date; free credits are not metered, so only overage after full drawdown is sent; postpaid usage is metered during the contract, but an end-of-contract true-up that finalizes after the marketplace endpoint closes is not sent and must be handled directly in Azure.
- On detected marketplace subscription lifecycle changes, Metronome stops metering and updates its customer status. The merchant must keep application status correct and end the Metronome contract when relevant.
- Azure metering accepts only positive quantities. A later Metronome credit cannot reduce an already submitted Azure bill; Metronome pauses billing until usage catches up, and an insufficient correction requires a merchant-issued manual refund through Azure support.
- The integration accepts only USD-fiat invoices. A non-USD rate card causes contract creation with Azure to error; on a contract with other non-USD invoices, only USD invoices are sent. After subscription end, Azure billability has a one-hour late-event window, Metronome disables metering after two hours, and outage catch-up cannot recover usage after the contract and window have ended.

## Material boundaries and contradiction

This Metronome guide documents configuration and intended submission behavior; it does not prove Azure listing approval, subscription activation, metering-record acceptance, invoice delivery, payment, settlement, tax, refund completion, or reconciliation. It says a billing provider cannot be added or changed after contract creation, while the separate billing-provider schedule authority permits next-period transitions to or from Azure Marketplace; the sources do not explain whether the guide's statement is stale, UI-specific, or limited to initial provisioning.

## Raw-detail coverage map

Use the raw page for the complete Partner Center offer, plan, pricing, preview, Entra credential, Metronome UI, customer activation, customer and contract payload, lifecycle, and contract-end procedures; exact required dimension values; all credit and commit metering cases; and the correction, outage, grace-window, and currency examples. Follow the dedicated Azure and Metronome API authorities for current external activation and complete endpoint schemas.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-integrations]], [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-credits-and-commits]], [[metronome-currencies-and-custom-pricing-units]]

## Raw Sources

- [[raw/metronome/integrations/marketplace-integrations/azure-2026-07-13|2026-07-13 snapshot - Azure Marketplace offer, identity and contract mapping, metering lifecycle, financial limits, late usage, and USD-only boundary]]
