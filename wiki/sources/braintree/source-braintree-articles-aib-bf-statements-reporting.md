---
title: "Braintree AIB BF Statements and Reporting"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/statements-reporting"
raw_files:
  - "braintree/articles/aib-bf/statements-reporting-2026-09-16.md"
tags: [braintree, aib-bf, statements, reporting, transaction-fees, reconciliation]
---

## Overview

This collected [[braintree]] AIB BF article describes Control Panel statements and a monthly Transaction Fee Report. It covers statement access and sections, account-pricing information, report permissions, report columns and reconciliation limitations. The AIB BF label is preserved from the captured route; the article itself does not expand that label, name a processor or region, or establish current bank policy.

## Key takeaways

- Statements are available in the Control Panel under **Reports** → **Statements**. Users who cannot access or see **Reports** are directed to check for the **View Statements** role permission.
- A statement includes a summary page, detailed disbursement, refund and chargeback breakdowns, and a key. The summary page contains some or all documented sections; fee and pricing details depend on the merchant account and pricing setup.
- The statement does not account for VAT, so VAT is not listed and merchants are responsible for covering it independently.
- The Transaction Fee Report is available at the beginning of each month in the Control Panel to users with the **Create, Run, and Download Reports** role permission. The captured article says the report cannot currently be retrieved through the API.
- The Transaction Fee Report excludes chargebacks, related chargeback and scheme fees, refunds and returned refund fees, so it is not designed exclusively for reconciliation. For blended pricing, separately listed interchange rates are for general reference because interchange is incorporated into the fixed rate.

> [!warning] Scope and authority boundary
> This is a Braintree-hosted AIB BF snapshot collected on 2026-09-16, not the AIB AF variant or independent evidence of current bank policy, account eligibility, regional availability, pricing or report behavior. The linked role-permission and pricing pages were not read for this entry; their links provide navigation, not proof that the target pages agree with this snapshot.

## Detail locators

- Statement access path and **View Statements** permission: `## Statements`, raw lines 17–28.
- Statement contents and the conditional summary-page scope: `## Statements` and `### Summary page`, raw lines 32–47.
- Disbursement, processing, Braintree fee, Kount, pricing-schedule and promotion sections: `### Summary page`, raw lines 50–95.
- VAT exclusion and merchant responsibility: `### Braintree Fee Details > IMPORTANT`, raw lines 77–78.
- Transaction Fee Report API limitation, monthly timing, permission and Control Panel access flow: `## Transaction Fee Report`, raw lines 98–113.
- Report column definitions, chargeback/refund exclusions, reconciliation limitation and blended-pricing qualification: `## Transaction Fee Report`, raw lines 115–127.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Supporting concept: [[braintree-control-panel]]
- The captured page links to role-permission and AIB BF pricing material; those unread targets are navigation only for this entry.

## Raw Sources

- [[raw/braintree/articles/aib-bf/statements-reporting-2026-09-16|Braintree AIB BF Statements and Reporting article]] - complete collected snapshot covering statements, account-dependent sections, VAT treatment, the monthly Transaction Fee Report, permissions and reconciliation limits
