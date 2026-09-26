---
title: "Braintree Control Panel: Managing Authorizations"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/managing-authorizations"
raw_files:
  - "braintree/articles/control-panel/transactions/managing-authorizations-2026-09-16.md"
tags: [braintree, control-panel, transactions, authorizations, settlement, vault]
---

## Overview

This collected Braintree article routes merchants managing expiring payment authorizations to three gateway workflows: verify and store, repeated authorizations, and authorization adjustments. Although the page sits in the Control Panel Transactions documentation tree, its described actions are merchant integration and API/SDK operations; it does not document a Control Panel button or transaction-editing action.

## Key takeaways

- Authorization expiry timing varies by payment method. For credit or debit cards, Braintree recommends card verification before vaulting the payment method; the merchant then creates the transaction when ready to collect. This avoids maintaining an authorization but does not guarantee sufficient funds or an active account at that later time.
- Braintree does not recommend repeated authorizations as a standard workflow. The merchant must identify the payment-method type, apply its expiration timing, authorize without submitting for settlement, void within that window, reauthorize through the vaulted token as needed, and submit only the latest transaction for settlement. This requires merchant-side logic and can create duplicate pending transactions that confuse customers and restrict their available funds.
- Authorization adjustments are described for select merchants and processors. The article routes adjustments before settlement to the Auth Adjustment API and describes a final adjustment during settlement submission. Lower amounts trigger an attempted partial reversal; higher amounts trigger an attempted incremental authorization. If the issuer declines either adjustment, Braintree returns a validation error and the original transaction remains `Authorized`.
- The article limits adjustments to Visa and Mastercard and says Mastercard permits all merchant categories while Visa limits use to listed categories. Its regional availability statements conflict, so the collected page cannot establish one reliable region list without current confirmation from Braintree.
- The page also warns that authorization and capture can incur merchant fees in some markets. It separately says delaying settlement for shipped PayPal goods is unnecessary because of Seller Protection; follow the linked agreement and protection terms rather than treating that note as a universal settlement rule.

## Control Panel and API boundary

The documentation location is a Control Panel article, but the operative flows link to card verification, Vault storage, transaction sale, void, Auth Adjustment, and submit-for-settlement APIs or SDK references. Configuration screens, user permissions, API request shapes, and current merchant enablement are not established by this page.

## Availability warning

> [!warning] Conflicting regional statements in the collected page
> The pre-settlement adjustment section says the feature is available only in the US for Visa and Mastercard, while the later Availability section lists US, APAC, EU, and Australia for both brands. This source preserves both statements and does not resolve them. Confirm current merchant, processor, region, card-brand, and Visa merchant-category eligibility with Braintree before implementation.

## Detail locators

- Expiration premise and PayPal Seller Protection plus market-qualified fee notes: `# Managing Authorizations`, lines 16-22.
- Three workflow choices and post-authorization amount-adjustment route: `## Authorization options`, lines 27-35.
- Recommended verify-and-store steps, benefits, and later-funds/account limitations: `### Verify and store`, lines 38-60.
- Repeated-authorization warning, payment-method-specific timing logic, void/reauthorize/latest-settlement flow, and duplicate-pending consequence: `### Multiple authorizations`, lines 63-94.
- Pre-settlement Auth Adjustment API behavior, issuer-decline result, and US-only statement: `#### Authorization adjustments without settlement`, lines 108-118.
- Settlement-time final adjustment and required validation-error handling: `#### Authorization adjustments during settlement`, lines 125-131.
- Broader region list, card-brand and merchant-category eligibility, plus the full Visa category list: `#### Availability`, lines 134-156.
- Decline-response and success-tracking benefits: `#### Benefits`, lines 159-163.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Gateway/API operations: [[braintree-server-sdk]]
- Dedicated adjustment operation: [[source-braintree-transaction-adjust-authorization-node]]
- Settlement-submission operation: [[source-braintree-transaction-submit-for-settlement-node]]

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/managing-authorizations-2026-09-16|Braintree Managing Authorizations article]] - complete collected page covering authorization workflow options, timing, adjustment behavior, eligibility, and warnings
