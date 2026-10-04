---
title: "Braintree Australia Statements"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/statements"
raw_files:
  - "braintree/articles/au/statements-2026-09-16.md"
tags: [braintree, australia, statements, reconciliation, reporting]
---

## Overview

This 2026-09-16 snapshot of Braintree's Australia statements article describes the monthly merchant statement as a reconciliation tool, explains where a user with the **View Statements** role permission can find it in the Control Panel, and routes readers through its summary and detailed sections. It is an Australia-specific Braintree documentation snapshot, not evidence of current bank policy, current pricing or surcharge rules, a particular deposit arriving, a stated settlement currency, or equivalence with another region's or processor's statement.

## Key takeaways

- The summary page covers the past month's disbursements, processing and fees. Its Disbursement Summary combines gross sales, refunds, credits and fees with the net amount described as disbursed for that statement period; the document does not independently prove receipt by the merchant's bank.
- Braintree Fee Details distinguishes transaction fees from billable-event fees. **Quantity** and **Total Billed** can differ because a fee may be created before it is billed to the account, and one transaction can incur more than one billable-event fee.
- The Pricing Schedule identifies the merchant account's pricing model and listed fee categories. For this Australia article, GST is described as 10% on most goods and services consumed in Australia and as assessed on applied Braintree fees, plus pass-through fees when the account uses an IC ++ pricing model; the GST amount is included in the statement's **Total Fees** value.
- Some detail is account- or pricing-dependent: the Kount section may be absent depending on pricing setup. Use the captured sections below for the document's disbursement, refund, chargeback, Kount and Cost of Acceptance breakdowns rather than treating this page as current operational, bank or regulatory authority.

## Detail locators

- **Locating your statement** — lines 32–40; Control Panel path and required role permission.
- **Statement summary page** — lines 42–104; Disbursement Summary, Processing Snapshot, fee timing and categories, multi-fee warning, and Pricing Schedule.
- **Goods and Services Tax (GST) Details** — lines 107–111; Australia and IC ++ qualifications and Total Fees placement.
- **Disbursement, Refund and Chargeback Details** — lines 114–126; statement-period breakdown descriptions.
- **Kount Fee Details** — lines 129–131; pricing-dependent presence.
- **Cost of Acceptance Details** — lines 134–136; captured calculation purpose and external regulation link.

## Related

- [[braintree]]
- [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/au/statements-2026-09-16|Braintree Australia Statements (2026-09-16)]]
