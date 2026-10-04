---
title: "Braintree AIB AF Statements"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/statements"
raw_files:
  - "braintree/articles/aib-af/statements-2026-09-16.md"
tags: [braintree, aib-af, statements, control-panel, reporting, fees]
---

## Overview

This collected [[braintree]]-hosted article, filed under the AIB AF path, explains how to access monthly statements in the Control Panel and how the captured statement presents batch processing, merchant service charges, other applicable fees, and funding totals.

It is snapshot evidence for this AIB AF statement document, not AIB BF evidence, independent current bank policy, current account or regional eligibility, current pricing authority, or proof that a particular transfer reached a bank account. The article does not define the AF label or establish equivalence with another AIB account arrangement.

## Key takeaways

- The article says statements are available in the Control Panel by the ninth business day of each month and routes access through **Reports** to **Statements**. If a user cannot access the Merchant Statements page, it directs the user to check that their role has the **View Statements** permission.
- **Processing Details** is a batch-level summary for the statement billing period. Its fields cover sales as credits, refunds as debits, processed net amounts, presentment and funding currencies, and a settlement-currency net total; use the raw locator for the exact field meanings.
- **Merchant Service Charges** displays ad valorem and per-transaction fee information. Interchange fees are additionally shown when the merchant has an IC+ pricing agreement, and the interchange and scheme columns remain empty when those fees do not apply to the merchant's pricing model.
- A separate fee-charges portion lists applicable non-processing fees, such as chargeback fees, and is absent when there are no applicable fees. The snapshot's detailed fee fields, including its statement that its VAT columns are blank, remain at the raw locator rather than being generalized as current tax or pricing policy.
- **Funding Totals** reports bank transfers described as completed within the billing period and the text that will appear on the bank statement for the disbursement. This is statement-reporting content, not independent proof that any individual deposit arrived or was made available by a bank.

> [!warning] Captured AIB AF scope
> Keep the access timing, statement layout, pricing-agreement conditions, fee treatment and funding language within this captured AIB AF article. Do not transfer them to AIB BF, another processor or account arrangement, current regional/account eligibility, current bank policy, or a current pricing agreement.

> [!warning] Links and reported transfers
> Links to role permissions, Settlement Batch Summary and pricing pages are navigation routes, not evidence that those targets agree with this snapshot. A Funding Totals entry described as a completed bank transfer does not by itself prove bank receipt, availability, settlement of a specific transaction, or successful payment execution.

## Detail locators

- Monthly statement timing, Control Panel access path and **View Statements** permission: `# Statements`, raw lines 14-25.
- Batch-level processing purpose and exact date, sales, refund, currency and net-amount field meanings: `## Processing Details`, raw lines 30-46.
- Merchant Service Charges, IC+ interchange condition, field inventory and pricing-model-dependent empty columns: `### Merchant Service Charges`, raw lines 52-70.
- Applicable non-processing fee condition and exact fee/VAT field meanings: `### Fee charges`, raw lines 73-87.
- Completed-transfer detail and bank-statement-text purpose: `## Funding Totals`, raw lines 90-94.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General reporting route: [[source-braintree-control-panel-reporting-overview]]

## Raw Sources

- [[raw/braintree/articles/aib-af/statements-2026-09-16|Braintree AIB AF Statements]] - complete collected snapshot covering statement access, role permission, batch processing fields, pricing-qualified fees and funding-total reporting
