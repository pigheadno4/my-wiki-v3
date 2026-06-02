---
title: "PayPal Agent Toolkit — Quickstart Guide"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "paypal-agent-toolkit-quickstart-2025.md"
  - "paypal-agent-tools-reference-2025.md"
  - "paypal-llm-integration-quickstart-2025.md"
  - "paypal-mcp-quickstart-2025.md"
  - "paypal-agent-prompt-best-practices-2025.md"
tags: [paypal, ai, agent-toolkit, mcp, langchain, crewai, openai, vercel, bedrock]
---

## Summary

Quickstart guide for integrating PayPal APIs into AI agent workflows. Supports 6 frameworks (Amazon Bedrock, CrewAI, LangChain, MCP, OpenAI Agents SDK, Vercel AI SDK) in TypeScript and Python. Includes 6 commerce agent types, full code samples, and Next.js frontend integration.

## Key Takeaways

- **TypeScript package**: `@paypal/agent-toolkit` (`npm install @paypal/agent-toolkit`)
- **Python package**: `paypal-agent-toolkit` (`pip install paypal-agent-toolkit`)
- **Python prerequisite**: Python 3.11+
- **TypeScript prerequisite**: Node.js 18+
- **`ALL_TOOLS_ENABLED`**: Bedrock-only constant for enabling all tools at once
- **`Context(sandbox=True)`** (Python) / `context: { sandbox: true }` (TypeScript) — always use for testing
- **MCP**: configure with `npx -y @paypal/mcp --tools=all`; needs `PAYPAL_ACCESS_TOKEN` + `PAYPAL_ENVIRONMENT` (SANDBOX/PRODUCTION)
- **Granular actions config**: `orders.create/get/capture`, `invoices.create/list/send`, `disputes.list/get`, `subscriptions`, `shipment`, etc.

## 6 Supported Frameworks

| Framework | Language | Import path |
| --- | --- | --- |
| Amazon Bedrock | TypeScript | `@paypal/agent-toolkit/bedrock` |
| CrewAI | Python | `paypal_agent_toolkit.crewai.toolkit` |
| LangChain | Python | `paypal_agent_toolkit.langchain.toolkit` |
| MCP | TypeScript/any | `npx -y @paypal/mcp` |
| OpenAI Agents SDK | Python | `paypal_agent_toolkit.openai.toolkit` |
| Vercel AI SDK | TypeScript | `@paypal/agent-toolkit/ai-sdk` |

## MCP Configuration

```json
{
  "mcpServers": {
    "paypal": {
      "command": "npx",
      "args": ["-y", "@paypal/mcp", "--tools=all"],
      "env": {
        "PAYPAL_ACCESS_TOKEN": "YOUR_TOKEN",
        "PAYPAL_ENVIRONMENT": "SANDBOX"
      }
    }
  }
}
```

Add to `~/Claude/claude_desktop_config.json` for Claude Desktop.

## 6 Commerce Agent Types

| Agent | Key capabilities |
| --- | --- |
| Customer support | Product Q&A, order status, shipping policies, troubleshooting |
| Product recommendation | Taste/brewing preferences, complementary products, pattern tracking |
| Order processing | Checkout guidance, address validation, inventory, shipping estimates |
| Shipping | Generate/print labels, tracking, returns label generation |
| Returns & exchanges | Return requests, refunds/store credits, feedback collection |
| Subscription management | Sign-ups, pause/resume, frequency changes, cancellations |

## Best Practices

- Always use sandbox for initial testing
- Never hard-code credentials; use env vars
- Define system prompts to control agent behavior
- Implement error handling

## Frontend: Next.js Integration

4-step: create Next.js project → chat interface (`app/page.tsx`) → API route (`app/api/chat/route.ts` with Vercel AI SDK) → `npm run dev`

## Related Pages

- [[paypal]] — company page
- [[agentic-commerce]] — agentic commerce concept
- [[source-paypal-ai-developer-tools]] — AI developer tools overview

## Raw Sources

- [[paypal-agent-toolkit-quickstart-2025]] — full 681-line agent toolkit quickstart: 6 frameworks, Python + TypeScript setup, MCP config, 6 commerce agent types, Next.js frontend
- [[paypal-agent-prompt-best-practices-2025]] — Prompt best practices: action first, be specific, break into subtasks, "Think step-by-step" for analytics, NEVER embed PII/card numbers (toolkit rejects + PCI DSS); 9 multistep workflow examples (invoice, order+shipping, subscription, disputes, product, QR invoice, fix invoice, reconcile, cancel subscription)
- [[paypal-mcp-quickstart-2025]] — MCP server quickstart: local (npx -y @paypal/mcp) vs remote (mcp.sandbox.paypal.com / mcp.paypal.com); 2 transports (SSE /sse, Streamable HTTP /http); Bearer token auth; troubleshoot: rm -rf ~/.mcp-auth; 3 workflow screenshots
- [[paypal-llm-integration-quickstart-2025]] — LLM integration: Anthropic (POST /v1/messages, anthropic-beta: mcp-client-2025-04-04, model claude-sonnet-4-20250514, mcp_servers[].authorization_token) + OpenAI (POST /v1/responses, gpt-4.1, tools[].type=mcp, require_approval: never); both connect to `https://mcp.paypal.com/sse`
- [[paypal-agent-tools-reference-2025]] — Agent tools reference: 30 tools across 7 categories (catalog/disputes/invoices/payments/reporting/shipment/subscriptions); remote MCP server adds 3 gift-card-only tools (search_product/create_cart/checkout_cart) via `mcp-remote https://mcp.paypal.com/sse` with x-feature-flags: commerce:true header
