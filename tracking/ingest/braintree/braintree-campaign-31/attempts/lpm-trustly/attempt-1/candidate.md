---
title: "Braintree Trustly Local Payment Method"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/trustly"
raw_files:
  - "braintree/docs/guides/local-payment-methods/trustly-2026-09-16.md"
tags: [braintree, local-payment-methods, trustly, bank-payments, graphql, webhooks]
---

## Overview

This collected Braintree guide describes Trustly as a Local Payment Method through which consumers initiate payments directly from their bank accounts. It is a retrieval route for the guide's European collection purpose, PayPal business-account prerequisite, exact buyer/seller/currency applicability table, non-instant transaction handling, server-side GraphQL direction, required outcome webhooks and sandbox simulation behavior. The 2026-09-16 snapshot does not establish current availability, merchant enablement, buyer or bank eligibility, production execution, settlement or funding.

## Key takeaways

- The guide says Trustly integrates with banks to collect funds locally across Europe, offers real-time reconciliation through its proprietary account integrations, supports merchant checkout natively and is optimized for most devices. These statements describe the collected page, not universal device support or account-specific eligibility.
- Processing Local Payment Methods requires a valid PayPal business account created, verified and linked in the Braintree Control Panel. The applicability table identifies the payment type as `trustly` and gives the captured buyer countries, seller-country exclusions, country-specific `EUR`, `DKK`, `GBP`, `NOK` and `SEK` mappings, and a `0.01 EUR` minimum that depends on the bank; use the exact table locator rather than generalizing those snapshot values.
- Trustly is explicitly non-instant. The page recommends shipping only after the transaction status reports success, says there is no capture call, and says Braintree associates a transaction for the merchant only after receiving confirmation that payment settled. Consumer initiation, an approval interaction or a notification should not be treated as independent proof of settlement or funding.
- The page directs the server side to GraphQL to create a local-payment transaction. This unversioned guide does not provide a complete client integration or a client SDK version, so it should not be used to infer a uniform client/server implementation contract.
- A webhook integration is required. The guide describes webhooks as confirmation of successful payment and notification of expiry, and shows funded and expired example payloads. The funded payload's transaction fields and `settled` status are illustrative example values, not a guarantee for every event or proof that a particular live payment funded.
- In sandbox, the guide says the approval URL opens a modal for simulating successful, expired or unapproved outcomes. Its stated 2-3 minute webhook timing and associated-transaction update apply to selecting the successful-payment simulation in that sandbox flow; they are not production timing or real-payment evidence.

## Evidence boundaries

> [!warning] Non-instant fulfillment boundary
> Trustly is non-instant in this guide. Do not ship from initiation, approval presentation or an assumed webhook schedule; follow the page's recommendation to wait for success on transaction status, while separately recognizing that the snapshot itself is not execution evidence.

> [!warning] Transaction, event, settlement and funding
> The guide says Braintree associates the merchant transaction after settlement confirmation and separately requires success/expiry webhooks. Keep transaction creation, webhook delivery, an example `settled` field and actual settlement or funding distinct; the example payload does not prove a specific payment outcome.

> [!warning] Environment and applicability scope
> The simulated outcomes and 2-3 minute webhook statement are sandbox-specific. The country, currency and bank-dependent minimum table is snapshot evidence and does not prove current method availability, merchant enablement, buyer eligibility or production behavior.

## Detail locators

- Trustly bank-payment identity, Europe collection scope, real-time reconciliation statement, merchant-checkout support and device optimization: `### Overview`, line 19.
- PayPal business-account creation, verification and Control Panel linking prerequisite: `### Overview`, line 22.
- Exact payment type, buyer countries, seller-country exclusions, country-to-currency mappings and bank-dependent minimum: `### Overview`, lines 24-26.
- Non-instant classification and shipping recommendation: note under `### Overview`, lines 29-30.
- No-capture behavior and transaction association after settlement confirmation: `### Capturing Non-Instant Transaction`, lines 33-35.
- Sandbox approval modal, three simulated outcomes, successful-simulation webhook timing and Payment Context update: note under `### Capturing Non-Instant Transaction`, lines 36-37.
- Server-side GraphQL transaction-creation direction: `### Server Side with GraphQL`, lines 40-44.
- Required webhook integration and successful-versus-expired notification purposes: `### Configure webhooks`, lines 47-49.
- Illustrative funded webhook fields and `settled` example status: `### Configure webhooks` and first `### JSON`, lines 51-68.
- Illustrative expired webhook fields and linked Local Payment Method webhook reference: second `### JSON`, lines 69-79.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Local-method family guide: [[source-braintree-payment-methods-local-payment-methods]]
- Notification concept: [[braintree-webhooks]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/trustly-2026-09-16|Braintree Trustly guide]] - complete collected page covering method purpose, applicability, non-instant transaction handling, GraphQL direction, webhook requirements and sandbox simulation
