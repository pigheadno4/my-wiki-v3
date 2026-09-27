---
title: "Braintree Control Panel 1099-K Reporting"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/1099-k"
raw_files:
  - "braintree/articles/control-panel/reporting/1099-k-2026-09-16.md"
tags: [braintree, control-panel, reporting, tax-forms, 1099-k]
---

## Overview

This collected Braintree article documents qualified 1099-K availability, Control Panel access, delivery fallback and total-calculation boundaries. It says Braintree may be able to provide the form depending on account setup and business location; it does not establish universal eligibility or current support.

## Key takeaways

- When applicable, Braintree makes the 1099-K available online in the Control Panel. Access requires the user's role to have the `View Statements` permission; the Account Admin role includes that permission by default.
- The previous year's statement is generated at the end of January and remains available until at least October 15. If it is unavailable in the Control Panel, a US Braintree Direct merchant that processed transactions during the previous tax year is told that Braintree will send it by email or postal mail.
- Monthly and yearly totals use gross sales volume and do not include credits, refunds or chargebacks. Incorrect information is routed to Braintree for a corrected form.
- PayPal transactions are excluded from the 1099-K Braintree provides and receive a separate PayPal 1099-K. Aggregated Amex transactions are included in Braintree monthly totals; merchants with their own direct Amex account receive a separate Amex 1099-K for those transactions.

> [!warning] Eligibility and snapshot boundary
> The article qualifies provision by account setup, business location and applicability. The Control Panel delivery fallback is narrower: it names US Braintree Direct merchants that processed transactions in the previous tax year. The raw was fetched on 2026-09-16 and carries page metadata dated 2025-04-01; these dates preserve provenance and do not establish current eligibility, availability, deadlines or tax requirements.

## Detail locators

- Qualified provision, Control Panel availability and paper-copy support route: `# 1099-K`, line 16.
- `View Statements` permission and Control Panel download path: `## Viewing your 1099-K in the Control Panel`, lines 21-29.
- Prior-year generation, at-least-October-15 availability and US Braintree Direct delivery fallback: `## Viewing your 1099-K in the Control Panel`, lines 31-35.
- Gross-sales calculation, excluded adjustments and correction route: `## Reconciling 1099-K totals`, lines 40-44.
- Separate PayPal form and aggregated-versus-direct Amex treatment: `### PayPal transactions` and `### American Express transactions`, lines 47-54.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/1099-k-2026-09-16|Braintree Control Panel 1099-K article]] - complete collected page covering qualified form availability, access permission, delivery timing and fallback, gross-sales totals, and separate PayPal and Amex treatment
