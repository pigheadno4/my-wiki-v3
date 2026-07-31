---
title: "Metronome Customers & Billing Overview"
type: source
date_ingested: 2026-07-31
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/overview"
raw_files:
  - "metronome/guides/customers-billing/overview-2026-07-13.md"
tags: [metronome, customers, billing, contracts, spend-controls, alerts]
---

## Overview

This landing page organizes Metronome's Customers & Billing documentation around customer lifecycle management, customer-facing billing experiences, fraud and entitlement controls, and notifications. It is a navigation map to more specific guides, not an API reference or an implementation contract for any listed capability.

## Key takeaways

- The customer-management area spans customer provisioning, contracts, ingest aliases, tiers and access, renewals, upsells, downgrades, and contract transitions.
- The customer-experience area points to API-powered usage, spend, and commitment dashboards; spending limits and payment gates; self-service billing controls; balance visibility; and usage and billing reports.
- The fraud-and-entitlements area groups spend thresholds and payment gates with product or feature access, unusual-usage and spend monitoring, and permission or availability controls.
- The notifications area covers threshold alerts, contract lifecycle monitoring, and webhook connections to existing notification systems.

## Documentation map

| Area | Topics named by the overview |
| --- | --- |
| Manage customers | Provisioning, customer objects, contracts, ingest aliases, lifecycle changes, tiers, product access, and renewals |
| Optimize customer experience | API-powered dashboards, spend controls, self-service controls, balance tracking, and reporting |
| Manage fraud and entitlements | Spend thresholds, payment gates, entitlement and access controls, and unusual-usage or spend monitoring |
| Set up notifications | Spend, usage, and commitment alerts; threshold actions; contract-state monitoring; and webhook integration |

The page's starting points are the customer-provisioning guide and customer-dashboard examples. Detailed behavior belongs to those linked guides and the relevant API and integration references.

## Scope and interpretation boundaries

> [!info] Navigation overview, not feature semantics
> Terms such as "fraud prevention," "entitlement controls," "automatically trigger actions," and "self-service billing management" are category labels on this landing page. The source supplies no request schemas, supported action types, enforcement ownership, monitoring algorithms, authorization model, latency, delivery guarantees, or failure behavior. In particular, it does not establish that a Metronome billing setting itself enforces application access or that every alert causes an automatic platform action.

The source also does not define contract transition rules, renewal automation, dashboard endpoints, report freshness, balance calculations, spend-threshold semantics, payment-gate lifecycles, webhook retry behavior, or permissions. Use dedicated customer, contract, invoicing, reporting, balance-threshold, alert, and webhook sources for those implementation details.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]], [[metronome-alerts-and-notifications]], [[metronome-webhooks]]
- Detailed context: [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]], [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]], [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]], [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/overview-2026-07-13|2026-07-13 snapshot — Customers & Billing documentation overview]]
