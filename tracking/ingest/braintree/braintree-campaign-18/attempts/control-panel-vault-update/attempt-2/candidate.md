---
title: "Braintree Control Panel: Update Customer Information"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/vault/update"
raw_files:
  - "braintree/articles/control-panel/vault/update-2026-09-16.md"
tags: [braintree, control-panel, vault, customers, payment-methods, addresses]
---

## Overview

This collected Braintree article documents updating an existing customer record in the Control Panel Vault. It covers customer details, payment methods and addresses, while routing high-volume customer updates to the API; it does not document an API or SDK update operation.

## Key takeaways

- After customer information has been stored in the Vault, a Control Panel user can find the customer through search, open the customer ID, and edit customer details, payment methods or addresses. The article describes the Control Panel as practical for one or two customers and recommends the API when many customers need updates.
- Updating credit-card numbers in the Control Panel may affect the business's PCI-compliance scope. Braintree also strongly recommends selecting `Verify card` during a payment-method update; this collected guidance does not determine a merchant's actual compliance scope or prove a successful verification.
- Adding a new payment method to a Vault record does not automatically change existing subscriptions. The article directs the user to update the subscription itself, keeping the Vault payment-method update distinct from subscription mutation.
- A customer Vault record can contain up to 50 addresses. Billing addresses are stored with the record and associated with one or more payment methods, while shipping addresses are selected per transaction. The article provides separate Control Panel routes for editing an associated billing address, adding one for an existing payment method, or selecting another saved address.
- Those billing-address actions do not trigger the gateway's AVS rules; verifying a new billing address requires re-verifying the stored card with the new billing information. Updating an existing customer address is reflected in payment methods already using it as their billing address.
- A shipping address on a specific transaction cannot be updated after that transaction is created. Customer addresses may still be added or updated for use as shipping addresses on future transactions.

> [!warning] Collected Control Panel and lifecycle boundaries
> This 2026-09-16 snapshot documents Control Panel actions, not equivalent API behavior or current availability. Preserve the page's qualified PCI warning, do not treat `Verify card` selection as proof of verification success, and keep Vault payment-method changes, existing-subscription updates, AVS checks and transaction-specific shipping addresses as separate effects.

## Detail locators

- Editable customer-information categories and API recommendation for high-volume updates: `# Update Customer Information`, lines 16-23.
- Payment-method PCI warning, existing-subscription boundary and card-verification recommendation: `## Payment methods`, lines 26-34.
- Per-customer address limit and billing-versus-shipping identity: `## Addresses`, lines 39-45.
- Billing-address update categories and the no-AVS/re-verification boundary: `### Billing address`, lines 48-54; `#### Editing a billing address` through `#### Selecting a different billing address`, lines 59-106.
- Shared existing-address propagation: `### Billing address > NOTE`, lines 109-110.
- Shipping-address choices and existing-transaction versus future-transaction boundary: `### Shipping address`, lines 115-126.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- API/SDK context: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/articles/control-panel/search-2026-09-16|Braintree Control Panel Search]] - unread navigation-only route for finding the Vault customer; not used as factual evidence here
- [[raw/braintree/docs/guides/customers/node-2026-09-16|Braintree Customers guide for Node.js]] - unread navigation-only route for the recommended high-volume API approach; not used as factual evidence here
- [[raw/braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16|Braintree PCI Compliance article]] - unread navigation-only authority for the qualified PCI-scope warning; not used as factual evidence here
- [[raw/braintree/articles/guides/recurring-billing/subscriptions-2026-09-16|Braintree Subscriptions article]] - unread navigation-only route for updating a subscription's payment method; not used as factual evidence here
- [[raw/braintree/articles/control-panel/vault/card-verification-2026-09-16|Braintree Control Panel Card Verification article]] - unread navigation-only route for re-verifying a card with new billing information; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/vault/update-2026-09-16|Braintree Control Panel Update Customer Information article]] - complete collected page covering Vault customer, payment-method and address updates plus PCI, subscription, AVS and transaction-shipping boundaries
