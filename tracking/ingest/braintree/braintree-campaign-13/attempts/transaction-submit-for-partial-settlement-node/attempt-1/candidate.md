---
title: "Braintree Transaction Submit for Partial Settlement (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/submit-for-partial-settlement/node"
raw_files:
  - "braintree/docs/reference/request/transaction/submit-for-partial-settlement/node-2026-09-16.md"
  - "braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16.md"
tags: [braintree, node-js, transactions, partial-settlement, paypal, venmo]
---

## Overview

This Braintree Node.js request reference documents `gateway.transaction.submitForPartialSettlement()` for settling multiple partial amounts against one authorization. It describes a parent authorization for the order and a separate child transaction for each settled portion, with callback and Promise examples and qualified refund guidance.

## Key takeaways

- The primary page marks multiple partial settlements as available only for PayPal and Venmo transactions. Its procedure says not to submit the parent authorization for settlement through the ordinary option or call, then to make a separate partial-settlement call for each portion with the authorized transaction and amount. The method name missing from one collected instruction line is not reconstructed.
- Each partial settlement creates a child transaction with the original transaction's details and the amount specified in that partial-settlement call. The page says the parent and child then move through lifecycle states, but the collected state names and transition symbols are missing; this entry does not reconstruct them.
- The page lists conditions for a later parent transition and says no more settlements can be created after that transition, but the target state and several condition qualifiers are absent from the collected rendering. Use the exact raw locator to inspect this damaged section rather than inferring statuses.
- After a transaction has been submitted for partial settlement, refunds can be issued only against child transactions and only up to the amount settled on each child. The corresponding transaction must be fully settled, but the required state name is missing from the collected text.
- The Control Panel links the parent authorization and settlement child records; the parent shows its children under Settlement Information, while each child shows its parent as authorization information.

> [!warning] Availability conflict
> The primary partial-settlement page says availability is only for PayPal and Venmo transactions. The fully read [[source-braintree-transaction-submit-for-settlement-node|Submit for Settlement source]] and its raw page additionally route some credit-card transactions for select merchants to multiple partial settlements. These statements do not establish one universal current eligibility rule; verify payment-method and merchant availability with Braintree rather than generalizing either scope.

## Detail locators

- PayPal/Venmo availability, parent-authorization pattern, ordinary-settlement prohibition, separate-call guidance, and missing method rendering: `# Transaction: Submit For Partial Settlement`, lines 15-25.
- Callback and Promise `gateway.transaction.submitForPartialSettlement()` examples and success/error result access: `### Callback` and `### Promise`, lines 30-63.
- Child-transaction creation, damaged parent/child statuses and transitions, transition conditions, and no-further-settlement restriction: `## Transaction settlement`, lines 65-76.
- Child-only refund scope, per-child amount ceiling, fully-settled prerequisite, and missing required state: `## Refunds`, lines 79-84.
- Parent/child Control Panel links: `## Control Panel visibility`, lines 87-91.
- Conflicting select-merchant credit-card availability route: [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Braintree Node.js Submit for Settlement reference]], `## Examples > ### Specifying settlement amount`, line 32.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Ordinary settlement submission and availability conflict: [[source-braintree-transaction-submit-for-settlement-node]]
- Related refund operation: [[source-braintree-transaction-refund-node]]
- Related void operation: [[source-braintree-transaction-void-node]]

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/submit-for-partial-settlement/node-2026-09-16|Braintree Node.js submit-for-partial-settlement reference]] - complete primary page covering PayPal/Venmo availability, parent/child behavior, damaged lifecycle rendering, refund restrictions, and Control Panel links
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Braintree Node.js submit-for-settlement reference]] - complete supplemental page used for the conflicting select-merchant credit-card availability statement at line 32
