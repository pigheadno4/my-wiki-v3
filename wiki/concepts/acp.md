---
title: "Agentic Commerce Protocol (ACP)"
type: concept
category: standard
tags: [acp, agentic-commerce-protocol, open-standard, stripe, openai, meta, oauth, checkout, payment-token]
---

## Overview

The **Agentic Commerce Protocol (ACP)** is an open standard co-built by **Stripe, OpenAI, and Meta** that defines how AI agents interact with businesses to complete purchases on behalf of buyers. It enables a programmatic exchange between buyers, their AI agents, and sellers. Learn more at [agenticcommerce.dev](https://agenticcommerce.dev).

## Five Capabilities

| Capability | What it does |
| --- | --- |
| **Agentic checkout** | Create, update, and complete checkout sessions (cart, fulfillment, payment) |
| **Cart and feed** | Browse product catalogs and manage carts before checkout |
| **Delegate payment** | Payment token exchange between buyers, agents, and businesses |
| **Delegate authentication** | OAuth 2.0 — agents act on buyer's behalf with a business |
| **Orders and webhooks** | Lifecycle updates: order confirmation, shipping, delivery, refunds |

## Key Players

- **Stripe**: co-builder; implements ACP payment handlers and SPT exchange
- **OpenAI** (ChatGPT): co-builder; uses ACP for in-chat shopping
- **Meta**: co-builder

## Relationship to UCP

[[ucp]] (Universal Commerce Protocol) has broader scope (checkout, identity, order, payment token exchange across platforms). ACP is focused specifically on the buyer-agent-seller purchase flow. Both are open standards in the agentic commerce space.

## Sources

- [[source-stripe-acp]] — Stripe's ACP overview with capability list and specification links
