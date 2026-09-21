---
title: "Braintree Grant API Webhooks (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/grant-api/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/grant-api/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, grant-api, payment-methods]
---

## Overview

This Braintree Node.js reference documents Grant API webhook notifications for updates to, or revocation of, payment instruments that were previously granted to another Braintree merchant. It describes event conditions and payload categories; it does not document how to grant or revoke access.

## Key takeaways

- The page labels an update notification type as `granted_payment_instrument_update` when a payment instrument previously granted to another Braintree merchant is updated. It says the `kind` is `GrantorUpdatedGrantedPaymentMethod` or `RecipientUpdatedGrantedPaymentMethod`, depending on which side of the relationship receives the webhook.
- The `granted_payment_instrument_revoked` notification is triggered when the grantor revokes a previously granted payment instrument. This notification is evidence of that event, not an instruction or authorization to perform revocation.
- The attributes section covers notification identity and trigger time, Vault/payment-method references, the revoked payment-method object, owning and recipient merchant identifiers, updated-instrument nonce information, nonce-use state, and names of updated fields. The collected rendering concatenates these descriptions, so this source does not reconstruct field names or assign every category to a particular webhook kind; the separate Grant API webhook guide owns kind-specific attribute details.

## Detail locators

- Notification-kind purpose: `# Grant API > ### Notification kinds`, lines 17-21.
- Previously granted instrument update condition and grantor/recipient-side kind labels: `# Grant API > ### Notification kinds`, lines 23-36.
- Grantor revocation condition: `# Grant API > ### Notification kinds`, lines 37-39.
- Concatenated payload-category descriptions and separate kind-specific guide route: `# Grant API > ### Attributes`, lines 42-46.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree Node.js webhook parsing guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/payment-method/grant/node-2026-09-16|Braintree Node.js payment-method grant request]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/payment-method/revoke/node-2026-09-16|Braintree Node.js payment-method revoke request]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/response/payment-method/node-2026-09-16|Braintree Node.js PaymentMethod response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/grant-api/node-2026-09-16|Braintree Node.js Grant API webhook reference]] - complete collected page covering notification conditions, side-qualified update kinds, revocation notification scope, and broad payload categories
