---
title: "Stripe — Accept a Payment in MCP Apps"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-mcp-accept-payment-2026.md"
tags: [stripe, mcp, model-context-protocol, chatgpt, instant-checkout, spt, shared-payment-token, agentic-commerce]
---

## Summary

Full integration guide for both MCP payment modes: Redirect (Stripe-hosted Checkout) and Instant Checkout (ChatGPT-specific, OpenAI private beta). Covers MCP tool/resource registration, UI SDK, and payment processing.

## Redirect Mode

**Packages**: `@modelcontextprotocol/sdk`, `@modelcontextprotocol/ext-apps`, `@modelcontextprotocol/ext-apps/server`

**Flow**:
1. `server.registerTool("buy-products")` → `stripe.checkout.sessions.create()` → returns `checkoutSessionUrl` in `structuredContent`
2. `registerAppTool("list-products")` with `_meta: { ui: { resourceUri } }` → serves product picker UI
3. `registerAppResource()` → serves bundled HTML widget (can use React in production)
4. Client: `app.callServerTool({ name: "buy-products", ... })` → `app.openLink({ url })`
5. Fulfillment: listen to `checkout.session.completed` + `checkout.session.async_payment_succeeded`

## Instant Checkout Mode (OpenAI Private Beta)

**Prerequisites**: Stripe profile + Network ID + OpenAI authorization

**Flow**:
1. `registerAppTool("show-buy-product-widget")` → returns product details in `structuredContent`
2. Client calls `window.openai.requestCheckout({ id: checkoutSessionId, payment_provider: { provider: 'stripe', merchant_id: networkID }, ... })` — session ID format: `"${priceID}::${uuid}"`
3. Customer selects payment method → ChatGPT calls `complete_checkout` MCP tool with SPT
4. `stripe.paymentIntents.create({ shared_payment_granted_token: spt, confirm: true })`

**Testing**: `payment_mode: "test"` + test Network ID; remove before ChatGPT app review. Restricted API key with Payment Intents: Write for live mode.

## Related Pages

- [[stripe-agentic-commerce]] — concept page (updated with MCP integration patterns)
- [[source-stripe-mcp-monetize]] — overview/comparison page

## Raw Sources

- [[stripe-mcp-accept-payment-2026]] — verbatim MCP accept payment guide, both variants (614 lines)
