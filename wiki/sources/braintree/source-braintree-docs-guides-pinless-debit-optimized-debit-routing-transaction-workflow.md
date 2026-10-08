---
title: "Braintree PINless Debit Optimized Routing Transaction Workflow"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/transaction-workflow"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/transaction-workflow-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, refunds]
---

## Overview

This 2026-09-16 snapshot of Braintree's unversioned transaction-workflow page describes routing for a transaction found ineligible for PINless debit and the refund route for a sale originally sent over a PINless debit network. [[braintree]] [[braintree-payment-methods]]

## Key takeaways

- The page says Braintree checks whether a transaction is eligible for PINless debit; when it is ineligible, the transaction goes through Visa or Mastercard.
- For a refund of a sale transaction, the page says the refund is sent on the same PINless debit network used for the original sale. If that refund is unsuccessful, Braintree says it automatically retries the refund through Visa/Mastercard.
- The automatic-retry statement is specifically about an unsuccessful refund after same-network routing. It does not establish a retry rule for an initial sale, a successful refund, or other transaction types.
- This short workflow snapshot does not supply eligibility criteria, account enablement, exact network selection, API or SDK instructions, client/server responsibility, or environment-specific behavior, and it is not proof of current availability or any individual authorization, refund, settlement or funding outcome.

## Detail locators

- Initial transaction eligibility check and Visa-or-Mastercard fallback: `## Transaction workflow`, raw line 16.
- Same-network refund routing and unsuccessful-refund retry through Visa/Mastercard: `### Refund experience`, raw line 21.
- Workflow diagram asset: raw line 18.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Related integration route: [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-integration]]
- Related eligibility route: [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-eligibility]]
- Related test and go-live route: [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-test-and-go-live]]

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/transaction-workflow-2026-09-16|Braintree PINless Debit optimized routing transaction workflow (2026-09-16 snapshot)]]
