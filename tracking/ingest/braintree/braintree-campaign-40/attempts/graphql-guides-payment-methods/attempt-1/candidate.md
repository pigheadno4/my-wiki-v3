---
title: "Braintree GraphQL Payment Methods Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/payment_methods"
raw_files:
  - "braintree/graphql/guides/payment_methods-2026-09-16.md"
tags: [braintree, graphql, payment-methods, vault, verification]
---

## Overview

This [[braintree]] website guide describes the GraphQL `PaymentMethod` object and the server-side GraphQL operations for vaulting, verifying, updating, finding, searching and deleting payment methods. A payment method represents transactable payment information, belongs to a customer, and exposes an ID that can be retained for later transaction creation. This is a collected website/API guide, not evidence about an SDK package, GitHub implementation, current merchant enablement or successful payment execution.

## Key takeaways

- The guide treats a client-obtained nonce as the ID of a GraphQL `PaymentMethod` whose `usage` is `SINGLE_USE`. A successful `vaultPaymentMethod` call consumes that ID and returns a new `MULTI_USE` payment-method ID for the same underlying information. Methods that support verification are verified automatically before storage; a failed or declined verification leaves the payment method unstored while verification detail may remain available in the partial GraphQL response.
- Single-use payment methods expire after three hours. Charging, authorizing, capturing and vaulting are listed as consuming actions, and an already-consumed ID cannot then be vaulted. Some methods are not vaultable: the guide's example is a PayPal authorization that grants permission for only one charge.
- A vaulted method may be associated with a supplied `customerId`; it cannot later be transferred to another customer. If no `customerId` is supplied, the documented default is creation of an empty customer associated with the newly vaulted method. Verification can be directed to a merchant account through `verification.merchantAccountId`.
- Update support is limited here to the billing address, cardholder name or expiration date of multi-use credit-card payment methods. The three documented update mutations verify by default; `verification.skip: true` updates without verification and returns a null verification field.
- `deletePaymentMethodFromVault` removes a multi-use method irreversibly. Storing the same underlying method again requires obtaining and vaulting a new single-use method, producing a new ID. For Venmo, deleting the last duplicate vaulted method for an underlying account also removes the customer's merchant connection in Venmo; a customer can independently remove that connection, which automatically removes the vaulted method and can be surfaced by the named revocation webhook.

## Detail locators

- Object identity, customer ownership and stored-ID purpose: `Payment Methods`, lines 14–16.
- Nonce-to-`SINGLE_USE` interpretation: `Obtain A Single-Use Payment Method (Nonce)`, lines 19–25.
- Vault mutation, verification fields and single-use-to-multi-use transition: `Vaulting The Payment Method`, lines 28–139.
- Displayed sandbox endpoint and `Braintree-Version: 2019-01-01` header are part of the cURL example at lines 79–94; they are example context, not a guide-wide environment or version guarantee.
- Customer association defaults and transfer restriction: `Customers`, lines 144–148.
- Vault failures, partial GraphQL failure shape and verification history pagination: `Error Handling`, lines 151–207.
- Consumption actions, three-hour expiry and non-vaultable method example: lines 210–227.
- Multi-use verification mutation and response fields: `Verify`, lines 230–290.
- Credit-card update mutations and skip-verification behavior: `Update` and `Skipping Verification`, lines 292–521.
- Node lookup and customer-based search schemas/examples: `Find`, lines 524–560, and `Search`, lines 562–669.
- Irreversible deletion, not-found behavior and Venmo connection effects: `Delete`, lines 672–718.

## Related

- [[braintree-payment-methods]] — provider-level payment-method and eligibility hub; this source is the distinct GraphQL object and lifecycle route.

## Raw Sources

- [[raw/braintree/graphql/guides/payment_methods-2026-09-16|Braintree GraphQL Payment Methods guide (2026-09-16)]]
