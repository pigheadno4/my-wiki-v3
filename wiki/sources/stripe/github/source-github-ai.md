---
title: "GitHub: stripe/ai"
type: source
date_ingested: 2026-08-13
date_updated: 2026-08-13
original_format: github-repo
raw_files:
  - "github/stripe/ai/snapshots/2026-08-13-1953b6c/manifest.json"
tags: [stripe, ai, llm, token-billing, usage-based-billing, mcp, agent-toolkit, agent-skills, benchmarks, github-repository]
---

## Overview

`stripe/ai` is Stripe's public implementation repository for AI-related payment tooling. The approved initial baseline is exact SHA `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` on `main`, collected on 2026-08-13. It combines LLM token-billing packages, the Stripe MCP bridge, TypeScript and Python agent toolkits, agent skills and plugin manifests, and Stripe integration benchmarks.

Repository: <https://github.com/stripe/ai>

## Evidence Boundary

- This page records behavior in the exact-SHA source capsule. It does not prove current upstream versions, private-preview access, merchant eligibility, or production enablement after the collection date.
- Package versions are independent and package-qualified. The repository itself has no single semantic version.
- The repository mixes product code, examples, skills, and benchmarks. Runtime source takes precedence when README or example claims conflict with implementation.
- The retained capsule excludes tests and lockfiles. It is sufficient for the public package surfaces and implementation paths summarized here, but a question requiring excluded internals may need a fresh clone and targeted source review.
- Benchmarks describe an evaluation method, not a product guarantee or a general comparison of payment providers.

## Grounding Excerpts

> "This repo is the one-stop shop for building AI-powered products and businesses on top of Stripe."
>
> `raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/README.md:5`

> "Stripe Billing for LLM Tokens is currently only available to organizations participating in the Billing for LLM Tokens Private Preview."
>
> `raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/README.md:7`

> "**Tool Calling**: Function calling and tool use aren't currently supported by the llm.stripe.com API"
>
> `raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/ai-sdk/provider/README.md:227`

> "Tools are fetched from `mcp.stripe.com`. If the server is unreachable, initialization fails with no fallback."
>
> `raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/tools/typescript/MIGRATION.md:26`

> "The score on an individual task is the best score of 3 runs. Failing runs due to observed infrastructure failures were discarded, and the best scoring run transcript was human reviewed by a Stripe engineer for run integrity."
>
> `raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/benchmarks/README.md:28`

## Package Baseline

| Package | Version at SHA | Role | Important boundary |
| --- | --- | --- | --- |
| `@stripe/ai-sdk` | `0.1.3` | Vercel AI SDK provider and meter | Private preview; provider proxies through `llm.stripe.com` |
| `@stripe/token-meter` | `0.1.0` | Meter native OpenAI, Anthropic, and Gemini usage | Fire-and-forget reporting can undercount when event delivery fails |
| `@stripe/mcp` | `0.3.3` | Local stdio bridge to Stripe's remote MCP | Tool availability follows API-key or RAK permissions |
| `@stripe/agent-toolkit` | `0.9.1` | TypeScript framework adapters | MCP-only architecture from `0.9.0`; async initialization required |
| `stripe-agent-toolkit` | `0.7.0` | Python framework adapters | Fetches remote MCP tools; lifecycle and network availability matter |

This table reports the ingested snapshot, not the latest packages currently published upstream.

## LLM Token Billing

### Stripe AI SDK provider

The provider routes Vercel AI SDK requests for OpenAI, Anthropic, and Google models through `https://llm.stripe.com`. A Stripe customer can be attributed at provider, model, or individual-request level, with the narrower request scope taking precedence.

Tool calling is rejected by both the v2 and v3 provider implementations. The provider README agrees, but its examples README lists tool calling as a feature and includes a tool-calling section. For this SHA, the implementation and provider README are authoritative: applications needing tools should use a native model SDK or another AI SDK provider and meter the resulting usage separately.

### Native and AI SDK meters

`@stripe/token-meter` extracts usage from OpenAI Chat, Responses, and Embeddings; Anthropic Messages; and Gemini GenerateContent responses, including streaming paths. The AI SDK meter provides equivalent wrappers for AI SDK v2 and v3. Native SDK ownership means model features such as tool/function calling can still be used independently of the Stripe proxy provider limitation.

Both meters send Stripe Billing v2 meter events. The default event is `token-billing-tokens`; the payload contains the Stripe customer, token count, normalized provider/model, and `input` or `output` token type.

The reporting path is intentionally fire-and-forget. It catches and logs Stripe failures without interrupting model generation. That protects request latency, but creates a billing-reliability boundary: production integrations need independent error monitoring, reconciliation, and a recovery strategy or failed event delivery can silently undercount usage.

## MCP and Agent Toolkits

The remote MCP endpoint is `https://mcp.stripe.com` and supports OAuth clients. The local `@stripe/mcp` package exposes a stdio bridge authenticated with a secret or restricted API key and can pass a connected account through `Stripe-Account`. A restricted key's permissions determine the exposed tools; integrations should use least privilege and should not assume a fixed tool catalog.

The TypeScript `@stripe/agent-toolkit` supports AI SDK, LangChain, OpenAI, and MCP adapters. Version `0.9.0+` replaced the older direct-API architecture with remote MCP tool discovery and execution, changed tool names to `snake_case`, removed action-list configuration, and removed metered-billing middleware. Initialization is asynchronous, remote MCP availability is mandatory, and clients must close the connection.

The Python `stripe-agent-toolkit` adapts remote Stripe MCP tools for OpenAI Agents, LangChain, CrewAI, and Strands. It has the same network and lifecycle boundary and supports Stripe account/customer context. Neither toolkit has a direct Stripe SDK fallback when the remote MCP service is unavailable.

The TypeScript README still demonstrates a synchronous constructor/get-tools pattern that conflicts with the migration guide and implementation. For `0.9.1`, use the awaited factory or explicitly await initialization, and close the toolkit when finished.

## Skills and Plugins

The repository carries Stripe-authored skills for best practices, Connect recommendations, Stripe Apps, documentation search, projects, directory navigation, and SDK/API upgrades. Provider manifests distribute these instructions to Claude, Codex, Cursor, Grok, Gemini, and Kiro environments. The skills are synchronized from Stripe documentation's `.well-known/skills` surface, so they are operational guidance rather than a separately versioned SDK.

The Connect guidance emphasizes Accounts v2 and explicit merchant decisions for Dashboard access, fee responsibility, and loss responsibility. A security reference elsewhere in the same snapshot still uses legacy Standard/Express/Custom terminology. Version-specific Connect advice should therefore follow the focused Accounts v2 skill and canonical Stripe documentation, while treating the legacy reference as an internal inconsistency.

Several skill references embed volatile current-version statements. Those values are evidence for this SHA only and must not be presented as the latest Stripe API or SDK versions without recollection.

## Integration Benchmarks

The benchmark corpus covers Checkout migration, embedded Checkout, partial payments, subscription flows, and SDK upgrades. Runs use a containerized agent harness with shell, editing, and computer-use tools; `search_stripe_documentation` is the only added Stripe documentation resource. Each task reports the best of three runs, discards observed infrastructure failures, and subjects the selected transcript to human integrity review.

These choices make the corpus useful for evaluating Stripe integration agents under its stated setup, but best-of-three selection and discarded failures must remain visible when interpreting scores. The benchmark solutions are implementation examples, not canonical product documentation.

## Related

- Company: [[stripe]]
- Concepts: [[ai-developer-tools]], [[stripe-usage-based-billing]]
- Documentation overview: [[source-stripe-building-with-ai]]
- History: [[changelog-github-ai]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/manifest.json) — exact-SHA capsule, selected/excluded inventory, and hashes
- [Repository README](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/README.md) — repository purpose and directory map
- [LLM overview](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/README.md) — preview status and provider-versus-meter selection
- [AI SDK provider README](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/ai-sdk/provider/README.md) — provider setup, attribution, and unsupported features
- [Provider v3 implementation](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/ai-sdk/provider/stripe-language-model-v3.ts) — request conversion and tool rejection
- [Token meter README](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/token-meter/README.md) — supported model SDKs and event shape
- [Meter event logging](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/token-meter/meter-event-logging.ts) — v2 event calls and failure handling
- [MCP README](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/tools/modelcontextprotocol/README.md) — local/remote configuration and permission boundary
- [TypeScript migration guide](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/tools/typescript/MIGRATION.md) — direct API to MCP transition
- [Python toolkit README](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/tools/python/README.md) — Python adapters and setup
- [Skills index](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/skills/README.md) — skill catalog and synchronization source
- [Benchmark methodology](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/benchmarks/README.md) — evaluation setup and scoring method
