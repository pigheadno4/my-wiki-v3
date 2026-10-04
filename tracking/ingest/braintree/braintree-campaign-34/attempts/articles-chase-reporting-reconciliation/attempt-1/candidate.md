---
title: "Braintree Chase Reporting and Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/chase/reporting-reconciliation"
raw_files:
  - "braintree/articles/chase/reporting-reconciliation-2026-09-16.md"
tags: [braintree, chase, reporting, reconciliation, paymentech-online]
---

## Overview

This collected Braintree article covers reporting and reconciliation for merchants in its Chase banking partnership. Braintree says it does not generate statements for these merchants; instead, it routes them to Chase's Paymentech Online portal for customizable reporting and financial reports.

## Key takeaways

- Chase offers more than 125 customizable reporting tools in Paymentech Online, while Braintree does not generate statements for merchants in the documented Chase banking partnership.
- Chase reports expire after 6 to 16 months depending on report type, so the article suggests downloading them regularly to retain merchant records.
- For daily, weekly, and monthly reconciliation, the article recommends financial reports generated in Chase Paymentech Online. It names the **Deposit Activity Summary** (`FIN-0010`) and **Financial Activity Summary** (`FIN-0025`) as reports that include daily deposit amounts for settled transactions, chargebacks, fees, and administrative adjustments.

> [!warning] Retention and funding boundary
> Download needed Chase reports before their report-type-specific expiration window. The presence of daily deposit amounts in a report does not by itself prove that a particular transaction funded or that an individual deposit arrived.

## Detail locators

- Statement responsibility, Chase portal, and 125+ customizable reporting tools: `# Reporting`, raw line 16.
- Report expiration window and regular-download suggestion: `# Reporting`, raw line 18.
- Reconciliation cadence, named financial reports, and included activity categories: `# Reconciliation`, raw line 23.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/chase/reporting-reconciliation-2026-09-16|Braintree Chase reporting and reconciliation]] - complete collected snapshot for the Chase-partnership reporting route, retention window, and named reconciliation reports
