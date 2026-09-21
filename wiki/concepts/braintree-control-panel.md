---
title: "Braintree Control Panel"
type: concept
category: technology
tags: [braintree, control-panel, gateway-administration, sandbox, production, reporting]
---

## Braintree Control Panel

The Braintree Control Panel is the user interface for administering a Braintree gateway. Most functions can also be automated through the API, but the overview identifies payment-method enablement, fraud and recurring-billing configuration, email-receipt enablement, webhooks, users and roles, custom fields, and processing-credential access as tasks that must be completed in the Control Panel. [[source-braintree-control-panel-overview]]

## Dashboard and environment boundaries

The Dashboard provides sales and transaction volume, totals, averages, and routes to statements, summaries, and other reports. Successful transactions are expected to appear the day after settlement, but the Dashboard is for general sales patterns rather than reconciliation, and Braintree Marketplace transactions are excluded from its daily-sales graphs.

Sandbox and Production use mutually exclusive Control Panel environments that do not interact and may have different login credentials. Use the dedicated reporting documentation for reconciliation and the specific administration guides for task-level behavior. [[source-braintree-control-panel-overview]]

## Sources

- [[source-braintree-control-panel-overview]] — Control Panel purpose, administration categories, Dashboard limitations, and Sandbox/Production isolation
