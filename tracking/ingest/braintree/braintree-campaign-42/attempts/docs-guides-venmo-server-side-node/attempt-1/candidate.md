---
title: "Braintree Venmo Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/venmo/server-side/node"
raw_files:
  - "braintree/docs/guides/venmo/server-side/node-2026-09-16.md"
tags: [braintree, venmo, nodejs, server-side, vaulting, transactions]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] website guide describes the Node.js server-side steps for storing a client-supplied Venmo payment-method nonce in the Vault and creating a Venmo transaction from a nonce. The transaction route couples the nonce with client-collected device data, and a non-default Venmo business profile requires the same profile identifier used during client-side tokenization. See [[braintree-payment-methods]] for the provider-wide payment-method route.

## Key takeaways

- The Vault example calls `gateway.paymentMethod.create()` with a customer ID and the payment-method nonce received from the client. The page also says a Venmo account can be saved during a transaction, but the captured sentence that should name the applicable options is damaged; see **Vaulting the Venmo account** (lines 21-39).
- Deleting a vaulted Venmo payment method also deletes the customer's merchant connection in the Venmo app, except that duplicate vaulted methods for the same Venmo account delay connection deletion until the last method is deleted. A customer can independently delete the connection in Venmo, which automatically removes the method from the merchant Vault; the page routes that event to the `PaymentMethodRevokedByCustomer` webhook. See **Deleting a Vaulted Payment Method** (lines 40-44).
- The transaction examples call `gateway.transaction.sale()` with an amount, client nonce, `submitForSettlement: true`, and client-collected device data. The page says device data is required for transaction creation but not for customer or payment-method creation. These examples are request patterns, not proof of authorization, settlement or funding. See **Creating transactions** (lines 47-75).
- For a particular Venmo business profile, the server must pass the profile identifier associated with that profile, matching the identifier used during client-side tokenization. If it is omitted, the page says the transaction is associated with the default business profile. See **Specifying the business profile** (lines 78-112).
- The page routes multiple partial settlements of one authorization to the separate Venmo partial-settlement guide. For production transactions, it says the gateway requests a transactable token from a PayPal service; inability to obtain the token causes a gateway rejection with reason `token_issuance`, after which the page directs the integration to retry the transaction request. See **Settlement** and **Gateway rejections** (lines 122-132).

## Material boundaries

> [!warning] Snapshot, version and execution boundaries
> This retained website page is routed to Node.js but does not state an exact Node SDK package version. It does not establish current support, merchant enablement, profile eligibility, exact package behavior, successful vaulting, authorization, capture, settlement or funding. Client-side tokenization and device-data collection are separate prerequisites referenced by this server-side page.

> [!warning] Damaged vault-at-transaction condition
> The captured line 39 says a Venmo account can be saved to the Vault during a transaction "by usingwithor." The option names and conditions are missing from the capture, so this source cannot establish how transaction-time vaulting must be requested. Use the precise raw locator and do not reconstruct the missing fields.

- The page's retry direction is specific to its documented production `token_issuance` gateway rejection. It does not define a general retry policy or establish duplicate-safety for other failures.
- Deleting a vaulted Venmo payment method has the coupled merchant-connection effect described above, subject to the duplicate-method condition; customer-side revocation independently removes the method from the merchant Vault.

## Detail locators

- GraphQL alternative navigation: `# Server-Side Implementation`, raw line 18.
- Vault creation callback and Promise examples plus damaged transaction-time vaulting sentence: `## Vaulting the Venmo account`, raw lines 21-39.
- Merchant-connection deletion, duplicate-method condition, customer revocation and webhook route: `## Deleting a Vaulted Payment Method`, raw lines 40-44.
- Transaction callback and Promise examples and device-data scope: `## Creating transactions`, raw lines 47-75.
- Business-profile identifier coupling and default-profile fallback: `### Specifying the business profile`, raw lines 78-112.
- Repeated connection-removal guidance: `### Removing connections`, raw lines 115-119.
- Multiple partial-settlement navigation: `### Capturing multiple partial amounts against the same authorization`, raw lines 125-127.
- Production transactable-token request, `token_issuance` rejection and page-directed retry: `## Gateway rejections`, raw lines 128-132.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Server-side SDK boundary: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/payment-methods/node-2026-09-16|Braintree Node.js payment-method guide]] - unread navigation-only Vault route
- [[raw/braintree/docs/reference/general/webhooks/payment-method/node-2026-09-16|Braintree Node.js payment-method webhook reference]] - unread navigation-only revocation-event route
- [[raw/braintree/docs/guides/venmo/submit-for-partial-settlement/node-2026-09-16|Braintree Venmo partial-settlement guide for Node.js]] - unread navigation-only partial-settlement route
- [[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16|Braintree gateway-rejections article]] - unread navigation-only rejection reference

## Raw Sources

- [[raw/braintree/docs/guides/venmo/server-side/node-2026-09-16|Braintree Venmo server-side Node.js guide (captured 2026-09-16)]] - fully read pinned website snapshot covering Vault storage, connection deletion, transaction creation, profile selection, partial-settlement navigation and token-issuance rejection
