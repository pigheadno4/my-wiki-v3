---
title: "GitHub: paypal/paypal-rest-api-specifications"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-rest-api-specs.md"
tags: [paypal, openapi, api-spec, orders, payments, payouts, subscriptions, disputes, invoicing, vault, webhooks]
---

## Summary

PayPal's official OpenAPI 3.0.3 specification files for all PayPal REST APIs. These are the machine-readable API contracts — authoritative source for request/response schemas, endpoint paths, parameters, and error definitions. Can be used for code generation (Java, TypeScript/Node) or as deep-dive reference for any API query.

## Key Takeaways

- **13 OpenAPI specs** covering the full PayPal REST API surface
- **Format**: OpenAPI 3.0.3 (JSON)
- **Codegen**: `npm run codegen-java -- <spec.json> --artifact-id <name>` or `npm run codegen-typescript-node`
- **Best use**: authoritative schema reference for field-level detail, enum values, required fields, and error shapes not always in prose docs

## API Coverage

| API | Version | Key operations |
| --- | --- | --- |
| Orders | v2 | Create, confirm, show, update, authorize, capture, track |
| Payments | v2 | Authorize, reauthorize, void, capture, refund, show |
| Payouts | v1 | Create batch, show batch/item, cancel unclaimed item |
| Subscriptions | v1 | Products CRUD, Plans CRUD, Subscriptions full lifecycle |
| Disputes | v1 | List, show, message, offer, escalate, evidence, accept, appeal |
| Invoicing | v2 | Create/send/cancel invoice, QR, record payment, templates |
| Payment Method Tokens (Vault) | v3 | Setup tokens, payment tokens, customer management |
| Shipment Tracking | v1 | Add/update tracking, shipment details |
| Partner Referrals | v2 | Marketplace onboarding, partner referrals |
| Catalog Products | v1 | Product CRUD for subscriptions |
| Webhooks Management | v1 | Create/list/show/delete webhooks, event types |
| Transaction Search | v1 | Search transactions by date, amount, status |
| Payment Experience | v1 | Web experience profiles |

## Related Pages

- [[paypal]] — company page
- [[paypal-payouts]] — Payouts concept
- [[paypal-vault]] — Vault concept
- [[disputes]] — Disputes concept
- [[source-github-paypal-postman-collections]] — Postman collections with real request samples

## Raw Sources

- [[github-paypal-rest-api-specs]] — stub file pointing to detail directory with all 13 OpenAPI specs
