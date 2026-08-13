---
title: "GitHub: paypal/postman-collections"
type: source
date_ingested: 2026-08-12
original_format: github-repo
raw_files:
  - "github/paypal/postman-collections/snapshots/2026-08-12-7f7240a/manifest.json"
tags: [paypal, postman, checkout, vault, subscriptions, partner-api, github-repository]
---

## Overview

`paypal/postman-collections` preserves three PayPal Postman collections and the TypeScript helper bundled into their scripts. The exact baseline reviewed here is commit `7f7240ab2d9417a55bf9c68355bf33bf64b1665c`: 43 Checkout Flow requests, 45 Partner API requests, and 116 Public API requests.

Repository: <https://github.com/paypal/postman-collections>

## Evidence boundary

- This repository is a backup of collections published in PayPal's Postman workspace. PayPal recommends forking the workspace; a direct JSON import falls out of sync and does not receive updates.
- Request bodies, scripts, and stored responses are exact-commit example evidence. They do not prove current endpoint behavior, merchant eligibility, regional availability, account enablement, or product access.
- [[source-github-paypal-rest-api-specifications]] remains the machine-readable API-contract authority. SDK repositories remain implementation authorities for their own package versions. Current product documentation and real API responses remain authoritative for current integration decisions.
- The helper library automates Postman testing. It is not a merchant production SDK, credential store, or production orchestration layer.
- Managed Account examples are explicitly limited release. Their presence must not be interpreted as general availability.

## Grounding excerpts

> "This repository maintains a backup of PayPal Postman Collections published on postman.com/paypal."
>
> `raw/github/paypal/postman-collections/snapshots/2026-08-12-7f7240a/files/README.md:3`

> "Although, this option is not recommended as your copy of collection will be out of sync and not receive updates."
>
> `raw/github/paypal/postman-collections/snapshots/2026-08-12-7f7240a/files/README.md:7`

> "For Expanded Checkout (Save Payment Methods) it includes examples for both Save During Purchase ... and Save for Purchase Later."
>
> `raw/github/paypal/postman-collections/snapshots/2026-08-12-7f7240a/files/Collections/PayPal_Checkout_Flows.json:5`

> "This type of update requires the buyer's consent."
>
> `raw/github/paypal/postman-collections/snapshots/2026-08-12-7f7240a/files/Collections/PayPal_Public_APIs.json:42065`

> "This collection provides access to key PayPal APIs tailored for platform and marketplace partners."
>
> `raw/github/paypal/postman-collections/snapshots/2026-08-12-7f7240a/files/Collections/PayPal_Partner_APIs.json:5`

## Checkout and saved-payment flows

The Checkout Flows collection is organized around executable multi-request sequences rather than a complete API catalog. Its 43 requests cover:

| Flow | Retained sequence |
| --- | --- |
| Save for purchase later | Create setup token, create payment token, create an Order using `vault_id`, then delete the token; card examples include non-3DS and 3DS paths |
| Save during purchase | Create an Order with `payment_source.*.attributes.vault.store_in_vault`, complete the payment, use the vaulted method for a later Order, then delete the token |
| Recurring revenue | Initial order and capture, tracking and refund examples, then a returning-buyer vaulted payment |
| PayPal and Expanded Checkout | Create, confirm payment source, authorize, capture authorization, get Order, and capture Order examples; card confirmation includes 3DS and non-3DS variants |
| FX and hosted links | Currency-exchange quote and Orders FX instruction examples, plus Payment Links and Buttons payment-resource creation |

These sequences clarify the difference between saving while completing a purchase and obtaining consent before a future purchase. They do not replace current Vault eligibility or stored-credential guidance. A few request labels are inconsistent with their folder context, so conclusions must follow the request body and endpoint rather than the name alone.

## Public API collection

The 116 Public API requests provide a broad runnable inventory: Authorization, Orders, Payments, Invoices, Subscriptions, Payouts, Webhooks, Shipping, Transaction Search, currency exchange, Disputes, Payment Method Tokens, Payment Resources, and limited-release managed-account onboarding.

Checkout-relevant details include the Orders create/get/update/authorize/capture lifecycle, Payments authorization/capture/refund operations, setup-token and payment-token management, and Payment Links resource create/list/get/replace/delete operations. The collection's stored response examples preserve success and failure vocabulary such as `ORDER_NOT_APPROVED`, `ORDER_ALREADY_CAPTURED`, `NOT_ENABLED_FOR_VAULT`, and `PAYER_ACTION_REQUIRED`; these are example outcomes at this commit, not an exhaustive current error contract.

The Subscriptions folder covers product and plan creation, plan activation/deactivation and pricing updates, plus subscription create, show, update, revise, suspend, activate, cancel, outstanding-balance capture, authorized-amount capture, and transaction listing. Revise is the consent-bearing operation for plan, quantity, shipping amount, or shipping-address changes. Lifecycle constraints in examples must be verified against current Subscriptions documentation before production use.

## Partner API collection

The 45 Partner requests separate connected-path partner operations from a limited-release managed path. Connected-path examples cover partner referrals, seller status and credentials, partner Checkout and Payments calls, Apple Pay wallet-domain registration, setup/payment tokens, billing-agreement migration, tracking, and webhooks.

Partner order and capture examples show partner attribution, connected-merchant context, `payment_instruction.disbursement_mode`, and platform-fee payloads. These examples establish request shape only. They do not establish that a partner or seller has a product, capability, or onboarding path enabled.

## Postman helper library

`paypal-postman-lib` bundles reusable collection scripts. `needsNewAccessToken()` refreshes only when a token is missing, expired, or belongs to another client, and avoids recursion on the token endpoint. `refreshAccessToken()` performs the client-credentials request and stores the token, expiry, and client ID in collection variables. Utilities detect Sandbox, retrieve `PayPal-Debug-Id`, encode JWT material, and create an unsigned PayPal auth assertion for a payer ID.

Keep client IDs and secrets in a private environment. The collection's variable defaults and scripts are test conveniences, not a recommendation to embed credentials or token management in browser code.

## Related

- [[changelog-github-postman-collections]] - commit-qualified repository history
- [[paypal-checkout]] - checkout lifecycle and client/server boundary
- [[paypal-vault]] - saved-payment and returning-buyer flows
- [[paypal-subscriptions]] - create, activate, and revise lifecycle
- [[paypal-payment-links]] - Payment Resources API boundary
- [[source-github-paypal-rest-api-specifications]] - API-contract authority
- [[paypal]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/paypal/postman-collections/snapshots/2026-08-12-7f7240a/manifest.json`
- Collections: `files/Collections/PayPal_Checkout_Flows.json`, `PayPal_Partner_APIs.json`, and `PayPal_Public_APIs.json`
- Repository guidance: `files/README.md`
- Helper library: `files/paypal-postman-lib/README.md`, `package.json`, and `src/*.ts`
