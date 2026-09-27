---
title: "Braintree Control Panel Grant API Report (Beta)"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/grant-api-report"
raw_files:
  - "braintree/articles/control-panel/reporting/grant-api-report-2026-09-16.md"
tags: [braintree, control-panel, reporting, grant-api, oauth, beta]
---

## Overview

This collected Braintree article documents the beta Grant API report in the Control Panel. The report summarizes transaction count and transaction volume for each visible recipient, grouped by currency, while the article separately qualifies the Grant API as being in limited release.

## Key takeaways

- The page labels the report as **Beta** and says the Grant API is currently in limited release. The 2026-09-16 snapshot does not establish current or general availability.
- The report provides transaction count and transaction volume for each recipient, grouped by currency. A recipient appears only after consenting through the OAuth flow, so absence from the report is not evidence that no recipient or Grant API activity exists.
- The article places report execution in the Control Panel under **Reports**, where the user selects a date range and runs the Grant API Summary. It does not document the separate API operations for granting or revoking payment-method access.

## Detail locators

- Beta title and limited-release availability qualification: `# Grant API Report (Beta) > **AVAILABILITY**`, lines 14-18.
- Report measures, per-recipient and currency grouping, and OAuth-consent visibility condition: `# Grant API Report (Beta)`, line 22.
- Control Panel navigation and date-range execution steps: `## Running a Grant API report`, lines 25-34.

## Evidence boundary

> [!warning] Limited-release beta report, not complete Grant API or reconciliation evidence
> This article documents a Control Panel summary and its OAuth-consent visibility condition. It does not establish report freshness, export behavior, reconciliation completeness, underlying transaction types, API grant/revoke behavior, or current broad availability.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Separate Grant API operation route: [[source-braintree-payment-method-grant-node]]
- Separate Grant API notification route: [[source-braintree-webhooks-grant-api-node]]

## Related raw API references

- [[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16|Braintree OAuth overview]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/grant-api-report-2026-09-16|Braintree Grant API Report (Beta) article]] - complete collected page covering limited-release status, report measures and grouping, OAuth-consent visibility, and Control Panel execution steps
