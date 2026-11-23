---
title: "GitHub changelog: stripe/ai"
type: source
date_ingested: 2026-08-13
date_updated: 2026-11-23
original_format: github-repo
raw_files:
  - "github/stripe/ai/snapshots/2026-11-22-1bb4869/manifest.json"
  - "github/stripe/ai/snapshots/2026-08-13-1953b6c/manifest.json"
tags: [stripe, ai, llm, mcp, agent-toolkit, token-billing, changelog, github-repository]
---

## Overview

Package-qualified retained history for `stripe/ai`. The repository has multiple independently versioned packages and no single repository semantic version. Cumulative implementation knowledge belongs in [[source-github-ai]].

## Full Additive Ingest: `default-branch@1bb4869` (2026-11-23)

- From `1953b6cce7344d880a054c42b8dd21ca3e50ebd5` to `1bb486909cc36ce608181c2af62c4716ba9cd7c7` on `main`; target collected 2026-11-22. This exact ref does not identify a package version.
- Repository focus moved from shipping agent toolkits, a local MCP bridge and LLM metering packages to maintaining skills, hosted-MCP plugin configuration, and benchmarks. The November README deprecates five packages without further updates, including security fixes. Plugin manifest versions are independent of one another. Skills expand documented integration planning, Connect, Apps, project and agent payment workflows.
- The [snapshot](../../../../raw/github/stripe/ai/snapshots/2026-11-22-1bb4869/manifest.json) retains 95 files: 35 added to the retained set, 35 modified and 25 unchanged. Of 147 August-only retained files, 121 are confirmed as upstream deletions in the path-scoped [comparison](../../../../tracking/github/repos/stripe/ai/comparisons/default-branch/1953b6c--1bb4869/comparison.json); 26 are not confirmed as deletions. These are not whole-tree counts.
- All current retained files and relevant August source were read; inventories, duplicated diff, and unchanged historical files were verified mechanically. August history remains intact. This ingest did not run a hosted endpoint, CLI, hook, payment or benchmark.

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
