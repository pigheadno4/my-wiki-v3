---
title: "GitHub: paypal/paypal-rest-api-specifications"
type: source
date_ingested: 2026-04-16
date_updated: 2026-08-11
original_format: github-repo
raw_files:
  - "github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/manifest.json"
  - "github-paypal-rest-api-specs.md"
tags: [paypal, openapi, api-spec, orders, payments, payouts, subscriptions, disputes, invoicing, vault, webhooks, github-repository]
---

## Overview

`paypal/paypal-rest-api-specifications` is PayPal's machine-readable REST contract repository. The reviewed baseline is the 16-file, 3,415,255-byte capsule at exact commit `90e8041ffe02d80c452d2b476bedd59a8d219bdc`. It contains 13 OpenAPI specifications plus the repository README, license, and package metadata.

The exact SHA and all 13 specification bytes match the legacy April 2026 collection. This full ingest therefore replaces a shallow summary with a canonical, fully reviewed baseline; it does not represent a newly released API change. Repository package metadata reports `@paypal/paypal-rest-api-specifications@1.2.0` and Apache-2.0 licensing.

Repository: <https://github.com/paypal/paypal-rest-api-specifications>

## Evidence Boundary

- The specifications are authoritative for retained endpoint paths, request and response shapes, required fields, enums, and declared API versions at exact SHA `90e8041`.
- A schema branch, enum, or operation proves that it exists in this contract. It does not establish merchant enablement, buyer eligibility, regional availability, production rollout, or a client SDK surface.
- Most files declare OpenAPI 3.0.3. Orders and Payments declare OpenAPI 3.0.4, correcting the legacy summary that described all 13 files as 3.0.3.
- The README's captured `npm run` output names package `1.0.0`, while the retained `package.json` is `1.2.0`. Use `package.json` for the reviewed package identity and treat the README output as stale generated text.
- Checkout-related domains are retained in detail below. Disputes, Invoicing, Payouts, Reporting, Partner Referrals, and the legacy Payment Experience API are summarized at a rough navigation level; use their exact raw specifications for field-level questions.

## Grounding Excerpts

> "This repository contains the specification files for PayPal REST APIs."
>
> `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/README.md:3`

> "This allows both humans and machines to discover the capabilities of an API without needing to first read documentation or understand the implementation."
>
> `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/README.md:47`

> `"summary": "Find a list of eligible payment methods."`
>
> `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/openapi/payments_payment_v2.json:2013`

> `"summary": "Create a setup token"`
>
> `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/openapi/vault_payment_tokens_v3.json:619`

> `"summary": "Verify webhook signature"`
>
> `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/openapi/notifications_webhooks_v1.json:469`

## API Contract Inventory

| API | Declared version | Operations | Checkout relevance |
| --- | --- | ---: | --- |
| Subscriptions | 1.8 | 16 | Detailed: plan and subscription lifecycle |
| Catalog Products | 1.0 | 4 | Detailed: product create/list/get/patch |
| Orders | 2.32 | 9 | Detailed: create, confirm, patch, authorize, capture, and order tracking |
| Disputes | 1.11 | 15 | Rough: dispute lifecycle and response actions |
| Partner Referrals | 2.5 | 2 | Detailed for connected-merchant onboarding and feature grants |
| Invoices | 2.6 | 22 | Rough: invoice, payment/refund record, template, and accounting-sync operations |
| Webhooks Management | 1.11 | 16 | Detailed: registration, lookup, verification, event retrieval, resend, and simulation |
| Payment Experience | 1.3 | 6 | Rough historical web-profile CRUD |
| Payments | 2.12 | 8 | Detailed: authorization, capture, reauthorization, void, refund, and method eligibility |
| Payouts | 1.9 | 4 | Rough: batch creation/retrieval and unclaimed-item cancellation |
| Transaction Search | 1.9 | 2 | Rough: transactions and balances |
| Shipment Tracking | 1.9 | 5 | Detailed: batch/single add, list, get, update, and cancel |
| Payment Method Tokens | 3.4 | 6 | Detailed: setup-token and payment-token lifecycle |

## Orders and Payment Sources

Orders 2.32 defines create, get, patch, confirm-payment-source, authorize, capture, add tracking, update/cancel tracking, and order-update callback operations. Its order statuses are `CREATED`, `SAVED`, `APPROVED`, `VOIDED`, `COMPLETED`, and `PAYER_ACTION_REQUIRED`; intent is `CAPTURE` or `AUTHORIZE`.

The request contract includes PayPal, Venmo, cards, Apple Pay, Google Pay, token, Bancontact, BLIK, EPS, Giropay, iDEAL, MyBank, P24, Sofort, Trustly, and crypto branches. Their presence is a server-contract inventory, not an availability matrix. Payment-source-specific experience contexts carry return/cancel URLs, shipping preferences, user action, app-switch state, and callback configuration.

Orders separates stored-card credential fields from Vault usage patterns. `stored_credential` requires `payment_initiator` and `payment_type`; values include `ONE_TIME`, `RECURRING`, and `UNSCHEDULED`, with optional `usage` values `FIRST`, `SUBSEQUENT`, or `DERIVED`. `usage_pattern` belongs to the Payment Method Tokens wallet contract, not this Orders stored-credential object.

## Payments and Eligibility

Payments 2.12 covers authorization retrieval/capture/reauthorization/void, capture retrieval/refund, refund retrieval, and `POST /v2/payments/find-eligible-methods`. The eligibility request can describe one-time, recurring, vault-with-payment, or vault-without-payment flows. Its method enum includes PayPal, Venmo, PayPal Credit, and PayPal Pay Later; the response can return eligibility and payment tokens.

Authorization, capture, and refund models preserve distinct state machines. Capture statuses include `COMPLETED`, `DECLINED`, `PARTIALLY_REFUNDED`, `PENDING`, `REFUNDED`, and `FAILED`; refund statuses include `CANCELLED`, `FAILED`, `PENDING`, and `COMPLETED`. Idempotency and partner headers are endpoint-specific and must be taken from the exact operation contract.

## Vault Contract

Payment Method Tokens 3.4 exposes create/list/get/delete payment tokens plus create/get setup tokens. The payment-source union includes cards, PayPal, Venmo, and Apple Pay. Setup-token statuses are `CREATED`, `PAYER_ACTION_REQUIRED`, `APPROVED`, `VAULTED`, and `TOKENIZED`.

Wallet `usage_pattern` values cover immediate, deferred, recurring, threshold, unscheduled, subscription, and installment pre/postpaid modes. The schema also carries `usage_type` (`MERCHANT` or `PLATFORM`) and `customer_type` (`CONSUMER` or `BUSINESS`). These fields describe the retained contract but do not resolve the wiki's documented product-eligibility and rollout contradictions for Venmo vault-without-purchase.

## Subscriptions and Catalog

Subscriptions 1.8 contains plan create/list/get/patch/activate/deactivate/pricing-update operations and subscription create/get/patch/revise/suspend/cancel/activate/outstanding-balance capture/transaction-list operations. Catalog Products 1.0 independently owns product create/list/get/patch. The legacy source incorrectly grouped product CRUD inside the Subscriptions specification.

Plans support trial and regular billing cycles, fixed and tiered pricing structures, taxes, setup fees, payment preferences, and quantity handling. Subscription status values are `APPROVAL_PENDING`, `APPROVED`, `ACTIVE`, `SUSPENDED`, `CANCELLED`, and `EXPIRED`.

## Webhooks and Tracking

Webhooks Management 1.11 covers webhook and lookup CRUD, subscribed and available event types, event listing/retrieval/resend, event simulation, and signature verification. Signature verification requires transmission metadata, certificate URL, webhook ID, and the webhook event, and returns `SUCCESS` or `FAILURE`.

Shipment Tracking 1.9 supports batch and single tracking submission, list/get, and update or cancellation. The tracker contract carries transaction ID, tracking number, status, carrier, shipment direction, uploader, buyer notification, and links. Orders also has order-scoped tracking operations; callers should choose the API boundary that matches their transaction workflow.

## Other API Families

- Disputes 1.11 exposes 15 operations covering list/get/patch and evidence, appeal, accept, adjudicate, require evidence, escalate, message, offers, return acknowledgement, and supporting information.
- Partner Referrals 2.5 creates and retrieves onboarding referrals. Its contract includes API-integration methods, products, capabilities, and REST feature grants, but not proof that a referred merchant receives them.
- Invoices 2.6 covers draft/send/remind/cancel, externally recorded payments and refunds, QR codes, search, templates, and accounting connections.
- Payouts 1.9 creates and retrieves batches/items and cancels only unclaimed items. Recipient wallet values include PayPal and Venmo.
- Transaction Search 1.9 lists transactions and balances; it is reporting evidence, not payment execution.
- Payment Experience 1.3 manages legacy web experience profiles and is retained as historical contract evidence.

## Code Generation and Repository Tooling

The repository includes Redocly preview/bundle commands, Redocly and Spectral linting, OpenAPI Generator validation, and Java or TypeScript/Node code generation. Generated clients remain downstream artifacts; their behavior and release identity must be reviewed in their own repositories.

## Related

- Company: [[paypal]]
- Checkout: [[paypal-checkout]]
- Vault: [[paypal-vault]]
- Subscriptions: [[paypal-subscriptions]]
- Payouts: [[paypal-payouts]]
- Disputes: [[disputes]]
- Server SDK: [[source-github-paypal-typescript-server-sdk]]
- Request examples: [[source-github-postman-collections]]
- History: [[changelog-github-paypal-rest-api-specifications]]

## Raw Sources

- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/manifest.json` - 16-file exact-SHA capsule manifest.
- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/openapi/` - all 13 reviewed OpenAPI specifications.
- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/README.md` - repository purpose, specification inventory, linting, and code generation.
- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/package.json` - package `1.2.0`, scripts, and dependencies.
- `raw/github-paypal-rest-api-specs.md` - legacy collection stub retained as historical raw evidence.
