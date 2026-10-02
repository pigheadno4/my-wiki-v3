---
title: "Braintree Credit Cards Submit for Partial Settlement (Node.js)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/submit-for-partial-settlement/node"
raw_files:
  - "braintree/docs/guides/credit-cards/submit-for-partial-settlement/node-2026-09-16.md"
  - "braintree/docs/reference/request/transaction/submit-for-partial-settlement/node-2026-09-16.md"
  - "braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16.md"
tags: [braintree, node-js, credit-cards, transactions, partial-settlement, limited-release]
---

## Overview

This captured Braintree Node.js credit-card guide documents `gateway.transaction.submitForPartialSettlement()` for creating separate child settlement transactions against one parent authorization, such as portions of an order shipped separately. It is a server-side partial-settlement operation, not ordinary full settlement submission and not a refund operation. The page is snapshot documentation for [[braintree]] and [[braintree-server-sdk]]; it does not establish current feature availability, merchant eligibility, or successful authorization, settlement, refund, void, or payment execution.

## Key takeaways

- Multiple partial settlements are marked as a limited-release feature available only to select merchants. The guide applies when the sale was not submitted immediately through `options.submit_for_settlement`; the parent must be in `authorized` or `settlement_pending` status for a partial-settlement submission.
- The Node operation takes the parent authorization transaction ID and the amount for the new child settlement transaction. The amount must be greater than zero, and repeated calls may not cumulatively exceed the parent authorization unless the merchant's industry and processor support settlement adjustment.
- Each call creates a child transaction for the specified amount. The captured guide renders the parent as moving to `settlement_pending` and the child through `authorized` > `submitted_for_settlement` > `settling` > `settled`. It lists three ways the parent reaches `settled`: fully settled children totaling the authorized amount; an expired original authorization with one or more settled children; or more than 30 days in settlement pending. Once the parent is settled, no further settlements can be created against it.
- This guide says the feature supports most credit and debit card transactions, including those processed through Google Pay and Apple Pay, as well as PayPal and Venmo, but excludes American Express and Discover. The fully read request reference says multiple partial settlements are only available for PayPal and Venmo, while the ordinary-settlement reference says they are available for PayPal, Venmo, and some credit-card transactions for select merchants. These snapshot statements conflict and do not establish a universal or current eligibility rule.
- Refund and void rules are separate lifecycle operations after partial settlement. The guide says First Data merchants may refund child transactions only, while Chase merchants may also refund the parent; child refunds are capped at the child's settled amount, Chase parent refunds at the authorized parent amount, and refunds require a fully settled transaction in `settled` state. A parent in `settlement_pending` may not be voided.

> [!warning] Availability and execution boundary
> The collected pages disagree on payment-method scope, and the guide itself marks multiple partial settlements as limited release for select merchants. Confirm current merchant, processor, industry and payment-method eligibility with Braintree. A documented method call, example, status path or Control Panel label does not prove current enablement or a successful payment or settlement.

## Detail locators

- Limited-release/select-merchant qualification and explicit-submission context: `# Submit for Partial Settlement`, lines 18-22.
- Callback and Promise operation examples: `### Callback` and `### Promise`, lines 23-42.
- Parent-status prerequisite, required amount, positive-amount rule, cumulative ceiling and settlement-adjustment exception: `#### Arguments`, lines 47-55.
- Payment-method scope and American Express/Discover exclusions: `## Supported payment methods`, lines 58-65.
- Child creation, parent/child state paths, parent terminal conditions and no-further-settlement limit: `## Transaction settlement`, lines 66-77.
- Processor-qualified refund authority, amount caps, settled prerequisite and parent-void restriction: `## Refunds and voids`, lines 80-87.
- Parent/child labels and cross-links in the Control Panel: `## Control Panel visibility`, lines 90-94.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Ordinary settlement submission: [[source-braintree-transaction-submit-for-settlement-node]]
- Related refund operation: [[source-braintree-transaction-refund-node]]
- Related void operation: [[source-braintree-transaction-void-node]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/submit-for-partial-settlement/node-2026-09-16|Braintree Node.js submit-for-partial-settlement request reference]] - separate request-reference snapshot for the same operation; its damaged lifecycle labels do not negate the guide's separately rendered labels, and its PayPal/Venmo-only availability statement conflicts with the guide.
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Braintree Node.js submit-for-settlement request reference]] - ordinary settlement operation and the separate statement that multiple partial settlements support PayPal, Venmo and some credit-card transactions for select merchants.

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/submit-for-partial-settlement/node-2026-09-16|Braintree Credit Cards Submit for Partial Settlement Node.js guide (captured 2026-09-16)]] - complete assigned guide covering operation identity, prerequisites, amounts, payment-method scope, lifecycle effects, refunds, voids and Control Panel visibility
- [[raw/braintree/docs/reference/request/transaction/submit-for-partial-settlement/node-2026-09-16|Braintree Node.js submit-for-partial-settlement request reference (captured 2026-09-16)]] - complete related reference retained for operation and availability-conflict context
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Braintree Node.js submit-for-settlement request reference (captured 2026-09-16)]] - complete related ordinary-settlement reference retained for operation distinction and availability-conflict context
