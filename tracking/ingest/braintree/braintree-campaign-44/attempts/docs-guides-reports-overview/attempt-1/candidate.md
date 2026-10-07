---
title: "Braintree Reports Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/reports/overview"
raw_files:
  - "braintree/docs/guides/reports/overview-2026-09-16.md"
tags: [braintree, reporting, api, webhooks, control-panel]
---

## Overview

This 2026-09-16 capture is the unversioned Braintree website overview that routes readers among reporting tools available through the API and additional reports described in Control Panel support articles. Its API-facing categories are settlement batch summaries, merchant-built custom reports, and reports assembled from webhook information. See [[braintree]], [[braintree-webhooks]], and [[braintree-control-panel]].

## Key takeaways

- Settlement Batch Summaries display total sales and credits for each batch for a particular date, with grouping by a custom-field value.
- The custom-report route is for merchant-built reporting over interactions with Braintree, including created transactions and customers; this overview supplies no query, field, export, or completeness contract.
- Webhook reporting starts only after webhook receipt is set up: the page describes collecting webhook information by trigger and uses subscription-cancellation notifications as an example report input.

## Scope boundary

This overview identifies report types and navigation routes, not a detailed API, SDK, webhook-delivery, or Control Panel contract. It does not specify an SDK language or version, client/server responsibility, required account type or Control Panel role, Sandbox-versus-Production behavior, webhook or report timing, or data-availability and completeness guarantees; follow the dedicated pages for those conditions, and do not treat this captured overview as current eligibility, configuration, delivery, report-generation, payment, settlement, disbursement, or funding proof.

## Detail locators

- API-versus-Control Panel reporting split: `# Overview`, line 16.
- Settlement Batch Summary purpose and custom-field grouping: `# Overview`, line 19.
- Custom-report purpose and transaction/customer scope: `# Overview`, line 20.
- Webhook setup condition, trigger-based collection, and subscription-cancellation example: `# Overview`, line 21.
- Control Panel reporting support route: `See also`, lines 23-26.

## Related

- [[braintree]]
- [[braintree-webhooks]]
- [[braintree-control-panel]]
- [[source-braintree-settlement-batch-summary-generate-node]]
- [[source-braintree-docs-guides-reports-custom-node]]
- [[source-braintree-docs-guides-reports-webhooks-node]]
- [[source-braintree-control-panel-reporting-overview]]

## Related raw API references

- [[raw/braintree/docs/reference/request/settlement-batch-summary/generate/node-2026-09-16|Settlement Batch Summary generate (Node.js)]] - unread navigation only; not used as factual authority here
- [[raw/braintree/docs/guides/reports/custom/node-2026-09-16|Custom Reports (Node.js)]] - unread navigation only; not used as factual authority here
- [[raw/braintree/docs/guides/reports/webhooks/node-2026-09-16|Webhook Reports (Node.js)]] - unread navigation only; not used as factual authority here
- [[raw/braintree/articles/control-panel/reporting/overview-2026-09-16|Control Panel reporting overview]] - unread navigation only; not used as factual authority here

## Raw Sources

- [[raw/braintree/docs/guides/reports/overview-2026-09-16|Braintree Reports Overview, captured 2026-09-16]]
