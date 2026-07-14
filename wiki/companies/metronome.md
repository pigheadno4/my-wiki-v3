---
title: "Metronome"
type: company
tags: [metronome, stripe, usage-based-billing]
source_count: 2
---

## Overview

Metronome is maintained as an independent provider capsule related to [[stripe]]. Its documentation covers usage-based pricing and packaging along with invoicing options spanning Stripe, cloud marketplaces, and ERP workflows.

## Documented billing models

- Pay as you go charges customers in arrears for actual usage.
- Enterprise models can include prepaid or postpaid commitments, negotiated discounts, one-time charges, and renewals.
- Hybrid subscriptions combine recurring revenue with usage-based components.
- Prepaid credit models allow upfront purchases, with auto-recharge or gated access after depletion.

The current source is a navigation overview. Detailed APIs, object models, event handling, and calculation rules require dedicated sources.

## Invoicing options

- Native Stripe invoicing can use Stripe Tax, dunning, and other Stripe product-suite capabilities.
- Marketplace invoicing automates metering and invoice creation for AWS, Azure, and GCP.
- ERP invoicing includes out-of-the-box and custom integrations for collection, book-closing, and revenue workflows.

## Knowledge status

- Collected documentation pages: 225
- Ingested source summaries: 2
- Documentation pages pending ingest: 223

## Sources

- [[source-metronome-guides-get-started-home]] — documentation entry point and four pricing/packaging routes
- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options

## Related

- [[metronome-index]] — provider catalog and coverage
- [[metronome-log]] — collection and future ingest history
- [[stripe-index]] — related Stripe catalog
- [[metronome-usage-based-billing]] — platform-specific billing concept
- [[metronome-invoicing]] — platform-specific invoicing options
