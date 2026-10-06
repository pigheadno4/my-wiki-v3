---
title: "Braintree In-Person Offline Transactions Guide"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/offline-transactions"
raw_files:
  - "braintree/in-person/guides/offline-transactions-2026-09-16.md"
tags: [braintree, in-person, offline-transactions, store-and-forward, card-reader, reconciliation]
---

## Overview

This collected Braintree In-Person guide describes offline transaction processing, also called Store & Forward (SAF): a supported reader captures and stores transaction data while it cannot reach the internet, then automatically uploads stored transactions to Braintree after reconnecting. It documents reader/POS network and certificate setup, reader-local initiation, status polling, retention and reconciliation behavior. This is snapshot-scoped provider guidance, not proof of current availability, merchant-account enablement, reader compatibility, successful authorization, settlement or funding.

## Key takeaways

- Offline capture is not a final payment outcome. Polling the context ID against the reader reports whether the reader collected card details for offline storage; after upload, the POS must poll the Braintree cloud endpoint for the final transaction status. A successful capture or upload therefore does not by itself establish authorization, settlement or funding.
- The merchant bears the risk of a stored transaction later being declined or refused and not funded. Braintree allows any amount to be sent to the reader in an offline session, so the POS or calling application is responsible for enforcing merchant-chosen floor limits and any session-level count or amount controls.
- The documented setup requires the reader and POS to share a local network, use static IP addresses and establish mutual TLS with certificates for both sides. The page recommends Store & Forward starting with reader firmware 5.0.0 because of critical improvements, but does not establish that every device, account or environment is eligible.
- Offline requests go to the reader's own GraphQL endpoint and include `deferredAuthorization: true`; the guide says request inputs such as `merchantAccountId`, custom fields and shopper statement descriptors are not validated at reader level. Invalid values can fail only after forwarding, leaving the merchant unfunded.
- Stored transactions may remain on the reader for up to five days before erasure; reconnection triggers automatic upload. After successful upload, a context ID is queryable for 24 hours, so the guide calls for at-least-daily reconciliation and storing the returned transaction ID and status in the POS database. A unique `orderId` is an additional query route that the page says does not expire.

## Detail locators

- Reader/POS topology, static-IP and mutual-TLS prerequisites: raw lines 45–64. Certificate creation, verification and reader provisioning details: raw lines 67–135.
- Reader endpoint, port, POS certificate, idempotency header and charge/refund request examples: raw lines 138–157. The examples are request illustrations, not execution guarantees or exact-current schema authority.
- Reader-local versus cloud-final status polling, firmware-qualified response fields and example responses: raw lines 160–175. Cancellation behavior: raw lines 176–180.
- Reader storage, upload, query and invalid-input expiry rules: raw lines 181–199. Daily reconciliation, Sandbox endpoint, `orderId` lookup and firmware-5.1.0-qualified vault/retry route: raw lines 203–215.
- The page's collected list of reader interactions supported offline and its reader-endpoint condition: raw lines 218–243. Treat this as the captured website list, not current account, environment or hardware enablement proof.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/in-person/guides/offline-transactions-2026-09-16|Braintree In-Person Offline Transactions (fetched 2026-09-16)]]
