---
title: "Braintree Wells IC Level 2 and 3 Processing"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/transactions/level-2-and-3-processing"
raw_files:
  - "braintree/articles/wells-ic/transactions/level-2-and-3-processing-2026-09-16.md"
tags: [braintree, wells-ic, level-2, level-3, commercial-cards, interchange]
---

## Overview

This collected Braintree article in the Wells IC route explains Level 1, Level 2 and Level 3 transaction-data processing for certain Mastercard and Visa cards. It presents Level 1 as the default and higher levels as specific-use-case options, primarily for business-to-business transactions, with merchant and card eligibility conditions. This snapshot is not evidence of current eligibility, account enablement, a particular rate, or policy for Wells Flat, another processor, bank, pricing model or region.

## Key takeaways

- Level 1 requires the least transaction information and is the default level at which Braintree passes transactions. Level 2 and Level 3 add transaction or line-item data for qualified higher-level processing.
- The article says Level 2 and 3 processing is appropriate only for specific use cases: travel and entertainment businesses are not eligible, the processing is intended primarily for business-to-business transactions, and the merchant's Tax ID must be stored in the Braintree Control Panel. For Visa, corporate and purchasing cards are eligible; for Mastercard, the article says any commercial cards are eligible. Merchants are directed to contact Braintree for complete eligibility information.
- Supplying Level 2 and 3 data can enable eligible merchants to receive lower interchange rates set by Visa and Mastercard, and can give purchasing businesses more detailed expense information. This is a qualified potential benefit, not a promised discount or an account-specific pricing schedule.
- Settlement and funding timing is stated to be the same for all card-transaction levels. The statement does not prove settlement, funding or a bank deposit for any transaction.
- Level 2 requires submission of data for the transaction's tax-exempt status, tax amount and purchase-order number; Level 3 adds merchant, invoice, tax and line-item data. Use the raw locators and linked developer-document routes for the complete field lists and integration setup rather than treating these examples as the full schema.

> [!warning] Processor, account and snapshot scope
> The page is captured under Braintree's Wells IC article path, but its body does not establish that the same eligibility, pricing effect or policy applies to Wells Flat, another merchant account, bank, processor, pricing model or region. The raw was fetched on 2026-09-16 and carries page metadata dated 2025-04-02; confirm current eligibility and account configuration with Braintree.

## Related implementation qualification

A separately collected Node.js reference says that adding Level 2/3 data through `submitForSettlement()` requires internal approval, overrides Level 2/3 data supplied in the sale request, and should be done through either the sale request or settlement submission rather than both. That operation-specific qualification is documented at [[source-braintree-transaction-submit-for-settlement-node]]; this Wells IC article itself provides only the general setup route.

## Detail locators

- Level definitions and Level 1 default: introductory paragraphs, lines 14-18.
- Business-use, Tax ID and Visa/Mastercard card-eligibility conditions plus the contact route: `## Availability`, lines 21-32.
- Qualified interchange and purchaser-expense benefits: `## Benefits`, lines 35-39.
- Same settlement and funding timeline across levels: `## Settlement and funding timeline`, lines 42-44.
- Level 2 example fields and complete-list route: `## Level 2 data`, lines 47-49.
- Level 3 example fields and complete-list route: `## Level 3 data`, lines 52-54.
- Transaction API setup route: `## Setup`, lines 57-59.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Node settlement-submission route: [[source-braintree-transaction-submit-for-settlement-node]]

## Raw Sources

- [[raw/braintree/articles/wells-ic/transactions/level-2-and-3-processing-2026-09-16|Braintree Wells IC Level 2 and 3 Processing article]] - complete collected page covering level definitions, eligibility, qualified benefits, settlement timing, field-list routes and setup navigation
