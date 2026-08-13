---
title: "GitHub changelog: stripe/ai"
type: source
date_ingested: 2026-08-13
date_updated: 2026-08-13
original_format: github-repo
raw_files:
  - "github/stripe/ai/snapshots/2026-08-13-1953b6c/manifest.json"
tags: [stripe, ai, llm, mcp, agent-toolkit, token-billing, changelog, github-repository]
---

## Overview

Package-qualified retained history for `stripe/ai`. The repository has multiple independently versioned packages and no single repository semantic version. Cumulative implementation knowledge belongs in [[source-github-ai]].

## Initial Baseline — Change Set `1953b6c` (2026-08-13)

| Component | Retained version/ref | SHA | Ingest mode |
| --- | --- | --- | --- |
| `@stripe/ai-sdk` | `0.1.3` | `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` | Full |
| `@stripe/token-meter` | `0.1.0` | `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` | Full |
| `@stripe/mcp` | `0.3.3` | `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` | Full |
| `@stripe/agent-toolkit` | `0.9.1` | `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` | Full |
| `stripe-agent-toolkit` | `0.7.0` | `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` | Full |
| skills, provider manifests, benchmarks | `default-branch@1953b6c` (`main`) | `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` | Full |

**Baseline established:** LLM proxy and native metering paths; Stripe Billing v2 token events; remote/local MCP architecture; TypeScript and Python framework adapters; Stripe-authored agent skills and provider manifests; integration benchmark methodology and examples.

**Important boundaries:** Token billing is private preview at this SHA. The Stripe AI SDK proxy rejects tool calling. Native meter delivery is fire-and-forget. TypeScript toolkit `0.9.1` requires asynchronous remote MCP initialization and has no direct API fallback. Examples and references contain contradictions that are preserved in the cumulative source.

**Future comparison rule:** Compare the exact default-branch SHA and each package-qualified version independently. A package version change can use delta ingest when the retained source remains structurally valid; a major package transition, architecture change, or materially changed skills/benchmark corpus requires a full additive ingest. Never label a default-branch SHA as a package release.

**Evidence:**

- [Snapshot manifest](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/manifest.json)
- [Repository README](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/README.md)
- [AI SDK package](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/ai-sdk/package.json)
- [Token meter package](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/llm/token-meter/package.json)
- [MCP package](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/tools/modelcontextprotocol/package.json)
- [TypeScript toolkit package](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/tools/typescript/package.json)
- [Python toolkit package](../../../../raw/github/stripe/ai/snapshots/2026-08-13-1953b6c/files/tools/python/pyproject.toml)
