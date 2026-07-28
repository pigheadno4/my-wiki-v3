---
title: "Metronome Invoicing"
type: concept
category: technology
tags: [metronome, invoicing, stripe, marketplaces, erp]
---

## Definition

Metronome presents invoicing as a set of distribution-channel options rather than one mandatory delivery path. Its overview identifies native Stripe invoicing, marketplace invoicing for AWS, Azure, and GCP, and ERP-oriented invoicing and revenue workflows.

## Invoicing options

| Option | Documented scope |
| --- | --- |
| Stripe Invoicing | Native Stripe integration that can use Stripe Tax, dunning, and other Stripe product-suite capabilities. |
| Marketplace Invoicing | Out-of-the-box metering and invoice creation for AWS, Azure, and GCP marketplaces, covering all Metronome charge types without a third-party integrator. |
| ERP Invoicing | Out-of-the-box and custom ERP integrations for collection, book-closing, and revenue workflows; the overview highlights NetSuite as a native option. |

## Selection model

The overview emphasizes optionality: organizations can use simpler integrated invoicing, marketplace distribution, or ERP systems according to their contracting and revenue-process needs. It does not define invoice objects, lifecycle states, synchronization details, or integration setup; those require the linked dedicated guides.

## Event-based invoice preview

Metronome exposes `POST /v1/customers/{customer_id}/previewEvents` to calculate draft invoices from supplied usage events and the customer's current contract configuration before those events are processed. The request can replace historical usage or merge with it, and the response returns draft invoice records with totals and line items. Contracts using SQL billable metrics are excluded from this preview capability.

## Related

- Company: [[metronome]]
- Usage-billing context: [[metronome-usage-based-billing]]
- Related platform: [[stripe]]

## Sources

- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-api-reference-invoices-preview-events]] — draft-invoice previews calculated from proposed usage events
