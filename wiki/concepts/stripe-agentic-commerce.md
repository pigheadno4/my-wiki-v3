---
title: "Stripe Agentic Commerce Suite"
type: concept
category: technology
tags: [stripe, agentic-commerce, ai-agents, product-catalog, v2-api, catalog-feed]
---

## Overview

Stripe's **Agentic Commerce Suite (ACS)** lets sellers make products discoverable and accept payments across AI chat agents with a single integration. US only. Uses v2 API namespace.

## How It Works

1. **Catalog feed**: upload product data (CSV/TSV) via v2 `ProductCatalogImport` API → Stripe indexes products for AI agents
2. **AI agent discovers products**: agents query Stripe's indexed catalog
3. **Agent-initiated checkout**: Stripe handles the checkout flow; seller listens to `checkout.session.completed`

## Catalog Feed API (v2)

```js
stripe.v2.commerce.productCatalog.imports.create({ feed_type, mode: 'upsert' })
```

**Feed types**:

- `product` — full catalog (recommend daily)
- `inventory` — incremental stock updates
- `pricing` — incremental price updates

**Import flow**: create → presigned URL → `PUT` CSV (max 4 GB) → poll until terminal state (`succeeded`/`succeeded_with_errors`/`failed`)

**v2 webhooks**: `v2.commerce.product_catalog.imports.succeeded/succeeded_with_errors/failed` — retrieve full object via `related_object.url`

## Order Fulfillment

Listen to `checkout.session.completed`. Expand with `Stripe-Version: 2025-12-15.preview` to get all line items, taxes, and payment details in one call. SKU at `LineItems.Data[].price.external_reference`.

## Optional Hooks

**Order approval hook**: Stripe calls your endpoint before confirming payment; 4-second timeout; must be idempotent (424 on error, agents may retry); returns `approved`/`declined`.

**Checkout customization hook**: dynamic tax rates + shipping options returned to Stripe before checkout; same idempotency requirement.

## Manual Capture

Set in Dashboard; capture via `POST /v1/payment_intents/:id/capture` with `Stripe-Version: 2025-09-30.preview`.

## Custom Integration (Third-Party Processors)

For merchants using third-party processors, ACS uses a **reverse API** pattern — Stripe calls YOUR backend. Implement four hooks:

1. `POST /agentic/checkouts` — create checkout, return line items + fulfillment options + totals
2. `POST /agentic/checkouts/:id` — update checkout (shipping selection, address change); set `ready_for_payment`
3. `POST /agentic/checkouts/:id/confirm` — receive SPT + risk details; resolve SPT → charge via your processor → record payment
4. `GET /agentic/checkouts/:id` — return current checkout state

**Shared Payment Token (SPT)**: resolve via `POST /v1/shared_payment/granted_tokens/:id/resolve` → `agentic_token` or `dpan` credentials (number, exp, cryptogram, ECI). Stripe may use Mastercard Agent Pay or Visa Intelligent Commerce tokens.

**Record payment**: `POST /v1/payment_records/report_payment` with SPT ID, amount, outcome (`guaranteed`), `processor_details[type]=custom`.

**Checkout status enum**: `incomplete` | `ready_for_payment` | `requires_escalation` | `processing` | `completed` | `canceled`

## Agent-Side Integration (For AI Interfaces)

ACS also enables AI interfaces (agents) to embed commerce. Two modes:

- **Embedded** (full): Delegated Checkout API manages full checkout; Stripe handles routing, auth, retries, SPT creation
- **Redirect** (feed-only): ingest seller product catalogs via SFTP, handle checkout independently

**OCA (Orchestrated Commerce Agreement)**: required bilateral connection; only seller initiates; agent confirms via `POST /v2/orchestrated_commerce/agreements/:id/confirm`; v2 webhooks: `created`, `partially_confirmed`, `confirmed`, `terminated`

**SFTP product feed**: Stripe delivers seller catalogs to agent's SFTP server; `disable_checkout: true` = discovery only; SSH keys rotated every 365 days

**RequestedSession lifecycle**: Create → update fulfillment address → select shipping → collect PaymentMethod → confirm (with RadarSession or raw risk signals)

**424 retry**: Stripe returns 424 if seller API fails — retry transient errors

**Next actions**: `shared_payment.issued_token.requires_action` for Klarna/Affirm/3DS — provide `return_url` at confirm

**MPF warning**: agents with end-to-end checkout may have marketplace facilitator tax obligations

## MCP App Monetization

Stripe also supports adding checkout to **MCP apps** (Model Context Protocol hosts like ChatGPT and Claude) for one-time purchases, subscriptions, tips, and donations.

Two modes:

- **Redirect** (public): prebuilt Checkout page in new tab; 40+ payment methods, subscriptions, 3DS, promo codes, tax — all integrated
- **Instant Checkout** (OpenAI private beta): stays in chat; cards/Apple Pay/Google Pay/Link only; no subscriptions/3DS/saved payment methods natively

See [[source-stripe-mcp-monetize]] for the full feature comparison.

**Redirect integration**: register `buy-products` MCP tool → `stripe.checkout.sessions.create()` → return URL; client calls `app.openLink()`. Fulfillment via `checkout.session.completed` webhook.

**Instant Checkout integration**: requires Stripe profile + Network ID; client calls `window.openai.requestCheckout()` with SPT payment provider; `complete_checkout` MCP tool receives SPT → `stripe.paymentIntents.create({ shared_payment_granted_token: spt, confirm: true })`. Use `payment_mode: "test"` for sandbox.

## Relationship to Other Products

- [[agentic-commerce]] — industry-wide agentic commerce concept (PayPal Store Sync/Agent Ready, ACP protocol)
- [[stripe-off-session-payments]] — off-session payments API (related: recurring payments infrastructure)

## Sources

- [[source-stripe-agentic-commerce-for-sellers]] — seller integration guide: catalog feed upload, order fulfillment, hooks, manual capture
- [[source-stripe-agentic-commerce-custom-integration]] — custom integration (third-party processors): reverse API hooks, SPT resolve, payment recording
- [[source-stripe-mcp-monetize]] — MCP app monetization: Redirect vs Instant Checkout (OpenAI private beta) comparison
- [[source-stripe-mcp-accept-payment]] — MCP accept payment: full Redirect + Instant Checkout integration code, SPT + PaymentIntent, testing checklist
- [[source-stripe-agentic-commerce-for-agents]] — Agent integration: OCA lifecycle, SFTP feed, RequestedSession, payment methods, next actions, mobile, MPF warning
