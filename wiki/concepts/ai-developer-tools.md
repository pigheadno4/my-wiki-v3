---
title: "AI Developer Tools for Payments"
type: concept
category: trend
tags: [ai, mcp, llm, agent-skills, developer-tools, stripe, paypal, agentic-commerce]
---

## Definition

AI developer tools for payments are platforms, SDKs, protocols, and integrations that help developers build payment integrations using AI assistance — LLMs, code agents, and AI-powered coding environments. Distinct from [[agentic-commerce]] (AI agents acting as buyers); this concept covers AI as the *developer's assistant*.

## Tool Categories

| Category | Description | Examples |
| --- | --- | --- |
| MCP servers | Expose payment API as tools callable by AI agents | Stripe MCP, PayPal MCP |
| Agent skills | Curated instructions for LLMs on best integration practices | Stripe agent skills, PayPal agent toolkit |
| LLM SDK integrations | Libraries connecting payment actions to LLM frameworks | PayPal agent toolkit (LangChain, CrewAI, etc.) |
| AI coding platform integrations | Pre-built payment support in vibe-coding platforms | Stripe on Base44/Replit/v0/Manus |
| IDE AI assistants | Payment-aware AI embedded in developer IDEs | Stripe VS Code AI Assistant |
| Plain text / llms.txt | Docs served as LLM-friendly markdown | Stripe `.md` URL suffix, `/llms.txt` |

## Platform Implementations

### Stripe

- **MCP server**: Interacts with Stripe API + searches docs knowledge base. Install: `docs.stripe.com/mcp`
- **Agent skills**: 3 skills covering integration best practices. Install via npx / Claude Code / Cursor:
  - `stripe-best-practices` — API selection, Connect (Accounts v2), billing, Treasury, security (keys/webhooks/OAuth), deprecated API migration
  - `stripe-projects` — new app/repo setup, Stripe Projects CLI bootstrapping
  - `upgrade-stripe` — API version + SDK upgrades
- **AI coding platforms**: Base44, Manus, Replit, v0 — pre-built Stripe integrations, no account needed; claimable sandboxes for platform builders
- **VS Code AI Assistant**: via Stripe VS Code extension; Copilot (`@stripe`) or standalone chat
- **Plain text docs**: add `.md` to any Stripe docs URL; `/llms.txt` follows emerging standard

See [[source-stripe-building-with-ai]].

### PayPal

- **MCP server**: Remote MCP hosted by PayPal; also supports local MCP setup. Integrates with Claude Desktop, Cursor, etc.
- **Agent toolkit**: 6 framework integrations (LangChain, CrewAI, OpenAI Agents SDK, Agno, Vercel AI, Google ADK); 30 tools across 7 categories (orders, products, subscriptions, invoicing, shipment, disputes, payouts)
- **LLM integration**: Anthropic + OpenAI SDKs; system prompt + tool schema injection pattern
- **Prompt best practices**: 5 principles — specify payment intent, include context, use structured responses, handle errors gracefully, scope permissions

See [[source-paypal-ai-developer-tools]], [[source-paypal-agent-toolkit]].

## Key Patterns

- **MCP (Model Context Protocol)**: Emerging standard for exposing APIs as callable tools for AI agents. Both PayPal and Stripe now have MCP servers
- **Agent skills / instructions**: Pre-written LLM instructions encoding integration best practices — reduces hallucination and improves code quality
- **llms.txt standard**: Emerging convention for making web content LLM-accessible (plain markdown, structured navigation)
- **Claimable sandboxes**: Test environments that AI platforms can provision for users without account creation (Stripe-specific)

## Open Questions

- How do PayPal and Stripe MCP server tool sets compare in breadth and quality?
- Which AI coding platforms support PayPal natively vs Stripe?
- How do agent skills from different providers differ in accuracy and coverage?

## Key Players

- [[stripe]] — MCP server, agent skills (Claude Code / Cursor / npx), VS Code AI assistant, claimable sandboxes
- [[paypal]] — MCP server (remote + local), agent toolkit (6 frameworks, 30 tools), LLM SDK integration, prompt best practices
