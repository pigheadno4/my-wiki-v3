---
title: "Agentic Commerce"
type: concept
category: trend
tags: [agentic-commerce, ai, conversational-commerce, shopping-assistants, llm, payments]
---

## Definition

**Agentic commerce** is a shopping paradigm where AI agents — rather than human users clicking through a UI — discover products, manage carts, and complete purchases on behalf of customers. Instead of navigating a website, a customer tells an AI assistant what they want in natural language, and the agent autonomously executes the transaction.

This is distinct from simple product recommendation AI: agentic commerce involves the AI actually *taking actions* (adding to cart, placing orders, making payments) with varying degrees of human oversight.

## Why It Matters

Agentic commerce represents a fundamental shift in how checkout friction is eliminated:

- **Conversational UX**: buyers express intent in natural language rather than navigating UI flows
- **Cross-platform reach**: a single AI assistant (ChatGPT, Gemini, Claude) can shop across many merchants simultaneously
- **Supervised vs autonomous**: ranges from AI-suggested actions that humans approve to fully autonomous purchasing
- **New merchant distribution channel**: merchants who integrate agentic-ready infrastructure can be discovered and sold through AI platforms they didn't build

## Two Integration Patterns

### Inbound (Make your store AI-accessible)

Merchants expose their product catalog and cart/order APIs to AI shopping assistants. The AI queries the merchant's infrastructure to search products, check inventory, and place orders directly into the merchant's OMS.

**PayPal implementation**: Store Sync — product catalog integration + cart operations API.

### Outbound (Accept payments via AI assistants)

Merchants minimally adapt their existing payment stack to accept transactions initiated by AI platforms. The payment provider (PayPal) handles security, identity, and compatibility across different AI platforms.

**PayPal implementation**: Agent Ready — Braintree-only; uses the **Agentic Commerce Protocol (ACP)**, an OpenAI open standard with 3 specs: product feed, agentic checkout, delegated payment. Flow: ChatGPT app calls `window.openai.requestCheckout()` → OpenAI obtains one-time Braintree nonce via delegated payment → MCP server `complete_checkout` tool receives nonce → merchant calls `gateway.transaction.sale({payment_method_nonce: token})`. Transactions tagged with `facilitator_details.oauth_application_name = "ChatGPT"` for tracking.

## Key Technical Challenges

- **Authentication & authorization**: how does an AI agent prove it's acting on behalf of an authorized human buyer?
- **Idempotency**: AI agents may retry; payment APIs must handle duplicate prevention
- **Scope limiting**: agents must not over-spend; platforms need spending controls and confirmation flows
- **Audit trail**: who authorized what, when — especially for autonomous purchasing
- **Merchant discovery**: how does an AI know which merchants support agentic transactions?

## Current State (2026)

- **Early/gated access**: PayPal's agentic commerce requires merchant application (form-based access request)
- **Store Sync eligibility (very restricted)**: US-only, USD-only, physical goods only, must already use Orders v2
- **Partner ecosystem**: Wix, Cymbio, BigCommerce, Feedonomics, Shopware are early integration partners
- **Supervised dominant**: most implementations still require human confirmation before purchase
- **MCP adoption**: Model Context Protocol (Anthropic) emerging as a standard for exposing merchant APIs to AI agents

> [!info] Evolving — eligibility expanding: Store Sync is currently limited to US merchants selling physical goods in USD via Orders v2. These constraints are likely to relax as the product matures.
> [!info] Evolving: Agentic commerce infrastructure is nascent as of 2026. Standards, auth patterns, and merchant tooling are all actively developing. Treat specific integration details as subject to change.

## PayPal AI Developer Tools (3 paths)

| Path | Product | Use case |
| --- | --- | --- |
| Custom AI assistant | **Agent toolkit** | Build AI agents for payment workflows, subscriptions, disputes, invoicing, customer support |
| LLM platform integration | **LLM integration + MCP server** | Enable ChatGPT, Claude, and other LLMs to interact with PayPal services |
| AI-powered shopping | **Agentic commerce** (Store Sync + Agent Ready) | Make products discoverable through AI shopping surfaces |

All PayPal AI agents operate within PCI-compliant environment. MCP (Model Context Protocol) server is available as a quickstart for LLM integrations.

## Open Standards

- **[[ucp]]** (Universal Commerce Protocol): open standard for agentic commerce interoperability — checkout, identity linking (OAuth 2.0), order tracking, payment token exchange. Stripe is a UCP Tech Council member.
- **[[acp]]** (Agentic Commerce Protocol): co-built by Stripe, OpenAI, and Meta. 5 capabilities: agentic checkout, cart/feed, delegate payment (token exchange), delegate authentication (OAuth 2.0), orders/webhooks. Used by ChatGPT.
- **MPP** (Machine Payments Protocol): Stripe's multi-network protocol for machine-to-machine payments (fiat + crypto).
- **x402**: HTTP payment protocol for Base/USDC machine payments.

## Related Concepts

See [[ai-developer-tools]] for AI tools that help *developers build* payment integrations (MCP servers, agent skills, LLM SDKs) — distinct from AI agents acting as buyers.

## Key Players

- [[paypal]] — Store Sync + Agent Ready products
- [[stripe]] — **Agentic Commerce Suite (ACS)**: catalog feed (v2 `ProductCatalogImport` API) + `checkout.session.completed` fulfillment + order approval/customization hooks. See [[stripe-agentic-commerce]].
- **Shopify** — building agentic checkout integrations
- **OpenAI** (ChatGPT) — shopping agent platform
- **Anthropic** (MCP) — protocol enabling AI agents to call external APIs

## Sources

- [[source-paypal-agentic-commerce]] — PayPal Store Sync and Agent Ready overview
- [[source-paypal-agent-ready]] — Agent Ready technical guide: ACP specs, ChatGPT integration, MCP tool, allowance validation, transaction tracking
- [[source-paypal-store-sync-product-catalog]] — Store Sync integration: product feed specs, Cart API, response handling, use cases
- [[source-paypal-store-sync-api-spec]] — Cart API OpenAPI spec v1.2.0: all 4 endpoints, PayPalCart schema, ValidationIssue contexts
- [[source-stripe-agentic-commerce-for-sellers]] — Stripe ACS: catalog feed upload (v2 API), order fulfillment, order approval hook, checkout customization hook
