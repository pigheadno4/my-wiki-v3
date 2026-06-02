---
title: "Stripe: Build on Stripe with AI"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-building-with-ai-2025.md"
  - "stripe-agent-skills-index-2025.md"
tags: [stripe, ai, mcp, agent-skills, llm, developer-tools, vscode]
---

## Summary

Stripe's AI developer tooling overview — MCP server, agent skills, AI coding platform integrations, plain text docs, and VS Code AI Assistant.

## Key Takeaways

- **Stripe MCP server**: exposes Stripe API as callable tools + knowledge base search for AI agents
- **Agent skills**: LLM instructions encoding Stripe integration best practices; 3 install methods
- **AI coding platforms**: Base44, Manus, Replit, v0 have pre-built Stripe integrations (no account needed); claimable sandboxes for builders
- **Plain text docs**: add `.md` to any Stripe docs URL; `/llms.txt` follows emerging standard
- **VS Code AI Assistant**: Stripe VS Code extension; Copilot (`@stripe`) or standalone chat

## Agent Skills Install Methods

| Method | Command |
| --- | --- |
| npx | `npx skills add https://docs.stripe.com --yes` |
| Claude Code | `claude /plugin install stripe@claude-plugins-official` |
| Cursor | Install Stripe plugin from Cursor marketplace |

> Note: manually added skills (npx) don't auto-update — pull updates manually.

## Agent Skills Catalog (3 skills)

| Skill name | Scope |
| --- | --- |
| `stripe-best-practices` | API selection (Checkout Sessions vs PaymentIntents), Connect (Accounts v2), billing/subscriptions, Treasury, Checkout/Payment Element, deprecated API migration, security (API keys, restricted keys, webhooks, OAuth). Files: SKILL.md + billing, connect, payments, security, treasury references |
| `stripe-projects` | New app/repo setup with Stripe Projects, stack provisioning, Projects CLI bootstrapping from coding agent |
| `upgrade-stripe` | Upgrading Stripe API versions and SDKs |

## Related Pages

- [[ai-developer-tools]] — AI developer tools for payments: MCP, agent skills, LLM integrations across platforms
- [[agentic-commerce]] — Agentic commerce: AI agents as buyers (distinct from AI as dev tool)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-building-with-ai-2025]] — Stripe AI developer tools: MCP server, agent skills (npx/Claude Code/Cursor), AI coding platforms, plain text docs, VS Code assistant
- [[stripe-agent-skills-index-2025]] — Stripe skills index: 3 skills (stripe-best-practices, stripe-projects, upgrade-stripe) with scope descriptions and file lists
