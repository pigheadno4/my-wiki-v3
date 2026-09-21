---
title: "Braintree Control Panel Overview"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/overview"
raw_files:
  - "braintree/articles/control-panel/overview-2026-09-16.md"
tags: [braintree, control-panel, dashboard, sandbox, production, reporting]
---

## Overview

The Braintree Control Panel is the user interface for administering a Braintree gateway. Although developers can automate most Control Panel functions through the API, the page identifies gateway setup and administration tasks that must be performed in the Control Panel, including enabling payment methods, configuring fraud and recurring-billing options, managing users and roles, creating webhooks and custom fields, and accessing processing credentials.

## Key takeaways

- The Dashboard gives a quick look at sales volume, transaction volume, totals, and averages, and offers quick actions to view merchant statements, transaction summaries, and other reports. Braintree says successful transactions can be expected to appear there the day after settlement.
- The Dashboard is intended for general sales-pattern visibility, not reconciliation; the page directs reconciliation work to Braintree reporting tools. Braintree Marketplace transactions are excluded from the Dashboard graphs' daily sales totals.
- Sandbox and Production have separate Control Panels for testing and live activity. They are mutually exclusive, do not interact, and may use different login credentials.

## Detail locators

- Control-Panel-only administration categories: `# Overview`, task list.
- Dashboard metrics, next-day post-settlement appearance, and reconciliation warning: `## Dashboard`, first paragraph.
- Marketplace exclusion: `## Dashboard`, note.
- Sandbox/Production links and isolation: `## Environments`.

## Related

- Company: [[braintree]]
- Concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/control-panel/overview-2026-09-16|Braintree Control Panel overview]] — complete collected overview covering administrative purpose, Dashboard boundaries, and environment isolation
