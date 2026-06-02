---
title: "Stripe — Agentic Commerce Suite: For Agents"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-agentic-commerce-for-agents-2026.md"
tags: [stripe, agentic-commerce, oca, requested-session, sftp, delegated-checkout, spt, shared-payment-token, for-agents]
---

## Summary

Agent-side integration guide for ACS. Covers two modes (Embedded = full checkout via Delegated Checkout API; Redirect = feed ingestion only). Includes OCA lifecycle, SFTP product feed setup, RequestedSession management, payment collection, SPT next actions, and webhooks.

## Two Integration Modes

| Mode | What Stripe handles | Checkout |
| --- | --- | --- |
| **Embedded** | Full: routing, auth, retries, SPT creation | Via Delegated Checkout API (`RequestedSession`) |
| **Redirect** | Product feed delivery only | Agent handles independently |

## Agent Onboarding

1. Stripe account + profile
2. SFTP setup (host, port, user); Stripe generates SSH key pair (rotated every 365 days); upload `stripe-verification.txt` with challenge token
3. Optional: terms of service + privacy policy links for sellers
4. Verification (may require identity check)

## Orchestrated Commerce Agreement (OCA)

Required bilateral connection between agent and seller. Only seller can initiate.

**OCA API** (`Stripe-Version: 2026-04-22.preview`):
- Retrieve: `GET /v2/orchestrated_commerce/agreements/:id`
- Confirm: `POST /v2/orchestrated_commerce/agreements/:id/confirm`
- Terminate: `POST /v2/orchestrated_commerce/agreements/:id/terminate`
- Seller profile: `GET /v2/network/profiles/:seller_profile_id`

**OCA webhooks** (v2): `created`, `partially_confirmed` (→ agent confirms), `confirmed`, `terminated`

## Product Feed

Delivered to agent's SFTP server. `disable_checkout: true` = discovery only (redirect to seller); `false` = checkout supported via `RequestedSession`.

## RequestedSession Lifecycle (Embedded Mode)

```
Create → Update fulfillment address → Select shipping option → Collect PaymentMethod → Confirm (+ risk details)
```

API: `POST /v1/delegated_checkout/requested_sessions` with `seller_details[network_profile]`, `line_item_details[]`, currency.

**Risk details required at confirm**: RadarSession ID or raw signals (IP, user_agent, referrer, time_on_page).

**424 retry**: if seller API returns non-2xx, Stripe returns 424 — retry transient errors.

## Payment Methods (Embedded)

Cards (Mastercard Agent Pay / Visa IC), Link, Apple Pay, Google Pay, Klarna, Affirm (limited — agent can't interact with Affirm UI programmatically).

## Next Actions (SPT)

Listen for `shared_payment.issued_token.requires_action` → provide `return_url` at confirm → handle redirect (Klarna, Affirm, 3DS). After completion: `shared_payment.issued_token.active` → `delegated_checkout.requested_session.completed`.

## Mobile Integration

Use `sharedPaymentTokenSessionWithMode` instead of `mode` in PaymentSheet. `preparePaymentMethodHandler` confirms `RequestedSession` server-side.

## MPF Warning

Agents handling end-to-end checkout may have marketplace facilitator (MPF) tax obligations — consult tax advisor.

## RequestedSession Webhooks

`delegated_checkout.requested_session.created/updated/completed/expired` + `shared_payment.issued_token.requires_action/active`

## Related Pages

- [[stripe-agentic-commerce]] — concept page (updated with agent-side integration)
- [[source-stripe-agentic-commerce-for-sellers]] — seller-side integration

## Raw Sources

- [[stripe-agentic-commerce-for-agents-2026]] — verbatim agent integration guide, Embedded + Redirect modes (826 lines)
