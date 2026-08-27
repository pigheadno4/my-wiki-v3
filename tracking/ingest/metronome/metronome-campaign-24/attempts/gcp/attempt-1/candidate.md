---
title: "Metronome Integration: GCP Marketplace"
type: source
date_ingested: 2026-08-27
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/marketplace-integrations/gcp.md"
raw_files:
  - "metronome/integrations/marketplace-integrations/gcp-2026-07-13.md"
tags: [metronome, gcp-marketplace, marketplace-billing, invoicing, integrations]
---

## Overview

This guide describes a native integration in which a merchant grants Metronome federated access to a GCP Marketplace project, configures a usage-based listing, maps each GCP entitlement to a Metronome customer and contract, and lets Metronome report calculated invoice totals to GCP. The merchant remains responsible for GCP project and listing configuration, Google review and publication, its own subscription backend and application state, matching the Metronome contract to the accepted offer, postpaid true-ups that miss the marketplace window, and manual refunds when GCP cannot accept a downward correction.

## Query-critical facts

- Metronome accesses the merchant's marketplace project through Workload Identity Federation rather than stored long-lived keys. The merchant deploys the pool, AWS workload provider, and GCP service account; enables the required IAM, service-account credential, procurement, service-control, and service-management APIs; and grants the service account procurement access for entitlement metadata and Service Controller access for usage reporting. Metronome does not require Pub/Sub access, leaving subscription-backend integration to merchant-owned service accounts.
- The GCP listing must use a `usage_fee` metric with reporting unit `count`, a custom display unit that does not imply currency, display quantity `1`, and price `0.01`; at least one listing feature must attach the usage-based plan. The guide says the metric identifier and pricing values are integration requirements and deviation causes failure.
- Identity is layered rather than interchangeable. Metronome supplies its Service Account ID, AWS Account ID, and AWS Lambda Role Name; the merchant supplies GCP Project ID and Project Number to deploy federation, then submits the resulting Provider ID and Workload Identity Configuration JSON to Metronome. Successful access validation saves the integration but does not establish Google listing approval or publication.
- Each marketplace customer is mapped with an Entitlement ID, also called Order ID, plus a Service Name identifying the product listing. The customer billing-provider configuration carries `gcp_entitlement_id` and `gcp_service_name`; a matching Metronome contract separately selects GCP with direct provider delivery.
- After GCP is selected and usage events arrive, Metronome sums the amount accrued since its previous metering request across that customer's contract invoices routed to GCP and reports the quantity as the total USD amount in cents.
- Prepaid commit purchases are metered on the scheduled invoice's service-period date; free credits are not metered, so only overage after complete drawdown is sent; and an end-of-contract postpaid shortfall true-up that finalizes after the marketplace endpoint closes is not sent and must be handled directly in GCP.
- On detected marketplace subscription changes, Metronome stops metering and updates its customer status. The merchant owns corresponding application status and ending the Metronome contract when relevant.
- GCP accepts only positive usage quantities. A later Metronome credit cannot reduce an already reported bill; Metronome pauses billing until usage catches up, and an insufficient correction requires a manual GCP refund. Only events within one hour after subscription end remain billable, Metronome disables metering after two hours, and outage backlog is included in a later request only while the contract and GCP window remain open. The integration supports USD-fiat invoices only: a non-USD contract rate card errors, and other non-USD invoices associated with the contract are not sent.

## Material boundaries and contradiction

This Metronome guide documents configuration, access validation, and intended metering behavior; it does not prove Google vendor registration, listing approval or publication, entitlement activation or freshness, metering-record acceptance, invoice delivery, payment, settlement, tax, refund completion, or reconciliation. Beyond the stated pause and outage-catch-up behavior, it does not define credential rotation or revocation, recovery from lost access, retry cadence, duplicate suppression or idempotency, partial-request handling, acceptance evidence, or reconciliation.

The guide says a billing provider cannot be added or changed after contract creation, while the separate billing-provider schedule authority permits next-period transitions to or from GCP Marketplace. The sources do not explain whether the guide's statement is stale, UI-specific, or limited to initial provisioning.

## Raw-detail coverage map

Use the raw page for the complete Workload Identity Federation, project/API, service-account permission, Producer Portal listing, metric and price, feature, Technical Integration, configuration-submission, customer provisioning, API payload, lifecycle, and contract-end procedures; every named identifier; the exact `usage_fee` settings; all prepaid, credit, and postpaid metering cases; and the positive-quantity correction, refund, outage, grace-window, and currency examples. Follow current GCP and dedicated Metronome API authorities for external approval, complete schemas, credential lifecycle, retry behavior, provider acceptance, and reconciliation.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-integrations]], [[metronome-security-principles]], [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-credits-and-commits]], [[metronome-currencies-and-custom-pricing-units]]

## Raw Sources

- [[raw/metronome/integrations/marketplace-integrations/gcp-2026-07-13|2026-07-13 snapshot - GCP federation and listing setup, identity mapping, contract routing, metering lifecycle, financial limits, late usage, and USD-only boundary]]
