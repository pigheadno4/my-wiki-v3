---
title: "PayPal Agent Ready"
type: source
date_ingested: 2026-04-18
original_format: webpage
raw_files:
  - "paypal-agent-ready-2025.md"
tags: [paypal, agentic-commerce, agent-ready, braintree, chatgpt, acp, mcp]
---

## Summary

Technical guide for PayPal's Agent Ready product — enabling existing Braintree merchants to accept payments through AI platforms (initially ChatGPT) using the OpenAI Agentic Commerce Protocol (ACP).

## Key Takeaways

- **Agent Ready = Braintree only** — uses Braintree SDK + GraphQL, not PayPal Orders API
- **ACP**: OpenAI-developed open standard with 3 specs: product feed (OpenAI ↔ Merchant), agentic checkout (OpenAI ↔ Merchant), delegated payment (OpenAI ↔ PSP)
- **Payment token**: one-time-use Braintree nonce received via MCP `complete_checkout` tool — use exactly like any Braintree `payment_method_nonce`
- **Amounts in cents**: `requestCheckout()` totals use cents (e.g. `330` = $3.30)
- **Supported methods now**: `card`, `applepay`, `googlepay` — `paypal_wallet` and `venmo_wallet` coming soon
- **Transaction tracking**: `transaction.facilitator_details.oauth_application_name` = `"ChatGPT"`

## ACP Specifications

| Spec | Description | Parties |
| --- | --- | --- |
| Product feed | Merchant exposes catalog for AI discovery | OpenAI ↔ Merchant |
| Agentic checkout | AI creates checkout sessions and completes orders | OpenAI ↔ Merchant |
| Delegated payment | AI platform obtains one-time payment token from PSP | OpenAI ↔ PSP (Braintree) |

## Integration Flow (ChatGPT App)

1. ChatGPT app widget calls `window.openai.requestCheckout(checkoutRequest)` with Braintree as provider
2. OpenAI requests delegated payment token from Braintree using allowance fields
3. Braintree issues one-time nonce token
4. OpenAI calls MCP server `complete_checkout` tool with `payment_data.token`
5. Merchant server calls `gateway.transaction.sale({payment_method_nonce: token})`

## `requestCheckout()` Key Parameters

```javascript
{
  id: checkoutSessionId,
  payment_provider: {
    provider: "braintree",
    merchant_id: "your_braintree_merchant_id",
    supported_payment_methods: ["card", "applepay", "googlepay"]
  },
  status: "ready_for_payment",
  currency: "USD",
  totals: [{ type: "total", amount: 330 }], // cents
  payment_mode: "live"  // or "test"
}
```

## MCP `complete_checkout` Tool

```python
token = payment_data.token  # Braintree nonce
result = gateway.transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": token,
    "options": {"submit_for_settlement": True}
})
```

## Allowance Validation (4 fields Braintree checks)

| Field | Validation | Error code |
| --- | --- | --- |
| `merchant_id` | Must match Braintree public merchant ID | 91565 |
| `max_amount` | Must be ≥ transaction amount | 915266 |
| `currency` | Must match merchant's configured currency | 915267 |
| `expires_at` | Token must not be expired | 91565 |

## Transaction Tracking

```bash
transaction.facilitator_details.oauth_application_name  # "ChatGPT"
transaction.facilitator_details.oauth_application_client_id
```

Search via Braintree Control Panel (filter by `facilitator_details.oauth_application_name`) or GraphQL (`facilitatorOAuthApplicationClientId: { is: "ChatGPT" }`).

## Test Setup

1. Enable ChatGPT developer mode: Settings → Apps → Advanced Settings
2. Register app: Settings → Apps → Create App → enter MCP server URL
3. Use `payment_mode: "test"` for test cards

## Related Pages

- [[paypal]] — company page
- [[agentic-commerce]] — agentic commerce concept
- [[source-paypal-agentic-commerce]] — Store Sync + Agent Ready overview
- [[source-paypal-store-sync-product-catalog]] — Store Sync product catalog integration

## Raw Sources

- [[paypal-agent-ready-2025]] — full Agent Ready guide: ACP specs, ChatGPT app integration, MCP server implementation, allowance validation, transaction tracking
