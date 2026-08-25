---
title: "Sync into Salesforce"
type: source
date_ingested: 2026-08-25
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/platform-integrations/sfdc-integration.md"
raw_files:
  - "metronome/integrations/platform-integrations/sfdc-integration-2026-07-13.md"
tags: [metronome, salesforce, census, integrations, crm, data-sync]
---

## Overview

This guide documents Metronome's native outbound Salesforce integration. Census acts as the ETL layer that pushes Metronome customer, contract, balance, catalog, and invoice data into Salesforce once per day so sales and revenue-operations teams can use contract terms, usage, spend, and commitment-burn signals in account workflows.

This is a setup and synchronization guide, not a Salesforce API, bidirectional provisioning, financial-reconciliation, or downstream-outcome contract. A configured integration or completed Metronome setup does not by itself prove Salesforce acceptance, object visibility, payment, tax, settlement, accounting, or reconciliation.

## Direction, environment, and setup layers

The documented direction is Metronome to Salesforce. Setup has four layers: install the Metronome-Salesforce package, activate a Census workspace, link Census to a Salesforce Production or Sandbox destination, and choose the customer population to synchronize. The process must be repeated in every Metronome environment whose data should reach Salesforce.

The package must be installed in the Salesforce instance later authenticated through Census, and the Salesforce user granting Census access must have package access. Metronome non-production links default to `test.salesforce.com`, while production links default to `login.salesforce.com`; the guide permits changing the URL to target the intended Salesforce instance. It does not define package upgrade or removal, Salesforce permission scope beyond package access and the Census authorization grant, credential rotation, connection rollback, or what happens when Metronome and Salesforce environment choices are mismatched after setup.

The final selection can include every Metronome customer or only customers linked to a Salesforce account. The UI linkage associates one Metronome customer with a supplied Salesforce account ID. The guide says the association can also be made programmatically during Metronome customer creation, but it does not give the request field, endpoint schema, validation, uniqueness, reassignment, unlinking, or propagation contract.

> [!warning] Customer-link authority gap
> This assigned guide owns the setup statement that a Salesforce account ID can be associated in the UI or during customer creation. [[source-metronome-api-reference-customers-get-a-customer]] and [[source-metronome-api-reference-customers-list-customers]] separately expose nullable `customer_config.salesforce_account_id`, and the list endpoint can filter by Salesforce account IDs, but they do not establish link freshness or mutation behavior. The current [[source-metronome-api-reference-customers-create-a-customer]] summary does not document a Salesforce account field in its request schema. Verify the current creation or update authority before implementing programmatic linkage.

## Activation, cadence, and monitoring

After **Complete Setup**, Metronome begins creating the Census workspace and associated syncs. When setup completes, Salesforce appears under active integrations and the first syncs start automatically. The first syncs can take a couple of hours; subsequent syncs are scheduled once per day, and the guide says a higher frequency cannot currently be configured.

Monitoring separates completed from incomplete or in-progress syncs. For each object type, a completed sync reports attempted rows and how many succeeded or failed. The total is only the rows that changed and needed resynchronization since the previous sync, not the total population of that object. Operators can download a CSV containing a sample of up to 100 failures for one object type and sync. That sample is not evidence that all failures are included, and the page does not define retry policy, backoff, recovery, alerting, ordering, atomicity across object types, deletion behavior, a success SLA, or a proof that Salesforce committed and exposed every successful row.

## Synchronized object model

The integration synchronizes these Metronome record families into Salesforce objects:

| Family | Documented records and useful boundaries |
| --- | --- |
| Identity and catalog | Credit types, customers, customer ingest aliases, and rate cards. Customer records can look up the associated Salesforce account; every listed object carries the Metronome environment name. |
| Commercial terms and balances | Contracts carry customer and rate-card lookups, inclusive start and exclusive end times, and usage-statement frequency. Commits or credits carry customer and contract lookups, type, priority, access dates, total amount, current balance, total cost, and cost basis. The current-balance description includes burn-down from the current draft invoice. |
| Invoices and dimensions | Invoice and invoice-line records include draft and finalized data, identities and lookups, service-period bounds, totals, status or line details, and product attribution. Separate association objects connect invoice lines to pricing dimensions and invoicing groups, whose key/value records are also synchronized. |

The invoice table enumerates `Draft`, `Finalized`, and `Void` as status values even though the surrounding prose says the synchronized invoice and line-item objects include draft and finalized invoices. The page does not resolve whether void invoices are synchronized, retained after a transition, or merely represented by the field's value set. It also does not define row deletion or archival semantics, referential ordering, partial-object updates, number precision, currency units, timezone rendering beyond UTC field descriptions, or Salesforce field-length and schema-migration behavior.

The synchronized invoice and balance fields are CRM-facing replicas, not evidence that an invoice was finalized downstream, delivered to a billing provider, paid, settled, taxed, posted to revenue, or reconciled. Dedicated invoice, balance, export, and reconciliation authorities continue to own those outcomes.

## Existing authority separation

[[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]] describes a worked architecture in which a Salesforce integration creates a Metronome customer and contract, then warehouse data is compared across systems. That Salesforce-to-Metronome provisioning statement is a different direction from this page's Metronome-to-Salesforce daily sync. Neither page establishes that one connector is bidirectional or that its provisioning and synchronization actions share identifiers, timing, retries, or reconciliation guarantees.

The customer list and retrieval authorities own their API response shapes, nullable Salesforce account mapping, filters, and read-consistency unknowns. This assigned guide owns package installation, Census workspace setup, Salesforce destination authorization, customer-scope selection, daily cadence, monitoring, and the listed Salesforce object fields.

## Related

- Company: [[metronome]]
- External systems: Salesforce and Census
- Concepts: [[metronome-integrations]], [[metronome-reporting-and-analytics]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-products-and-rate-cards]]
- Customer authorities: [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-customers-get-a-customer]], [[source-metronome-api-reference-customers-list-customers]]
- Reconciliation authority: [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]]

## Raw Sources

- [[raw/metronome/integrations/platform-integrations/sfdc-integration-2026-07-13|2026-07-13 snapshot - Salesforce package and Census setup, daily sync operations, monitoring, and Salesforce object fields]]