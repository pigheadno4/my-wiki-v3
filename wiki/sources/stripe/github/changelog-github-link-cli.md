---
title: "GitHub changelog: stripe/link-cli"
type: source
date_ingested: 2026-08-15
date_updated: 2026-08-15
original_format: github-repo
raw_files:
  - "github/stripe/link-cli/snapshots/2026-08-15-d540389/manifest.json"
tags: [stripe, link, link-cli, agentic-commerce, financial-insights, changelog, github-repository]
---

## Overview

Package-qualified retained history for `stripe/link-cli`. Durable architecture and implementation knowledge belongs in [[source-github-link-cli]].

## Initial Baseline — `@stripe/link-cli@0.13.0` (2026-08-13)

| Package | Version | Tag | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@stripe/link-cli` | `0.13.0` | `@stripe/link-cli@0.13.0` | `d540389e030d0f475a6b85cd64ccaf978ff498ac` | Full |

**Baseline established:** OAuth device authorization and scope upgrades; Link payment-method and address access; approval-gated spend requests; virtual-card, SPT/MPP, and Link Pay Token paths; 3DS and other next actions; structured agent output; stdio and HTTP MCP; credential-file protections; outcome reporting; and read-only financial data commands.

**Release-specific changes:**

1. `0.13.0` exposes `balances`, `sources`, and `transactions` in the CLI and ships the `financial-insights` skill.
2. Interactive mode now surfaces duplicate spend-request error messaging so an existing matching request can be retrieved instead of recreated.

**Identity note:** the repository root and published CLI share the name `@stripe/link-cli`, but the package-qualified release is established by `packages/cli/package.json` and tag `@stripe/link-cli@0.13.0`. The internal `@stripe/link-sdk@1.0.0` package is private and does not have an independent retained public release in this work item.

> [!warning] Contradiction
> Both retained skill files declare frontmatter version `0.11.0`, although this work item is package release `@stripe/link-cli@0.13.0` and its notes say the financial-insights skill ships in `0.13.0`. Preserve these as separate identities: package release `0.13.0`, stale embedded skill metadata `0.11.0`.

**Collection strategy:** this repository uses a `tagged-tree-v1` capsule because the semantic tag maps to one CLI release while the repository root is private and does not expose a release-valid NPM workspace declaration in `package.json`. The capsule retains configured CLI, SDK, skill, and metadata paths and excludes tests and fixtures.

**Future comparison rule:** compare every stable package-qualified `@stripe/link-cli@0.x` release after `0.13.0` against the highest retained version. Use delta ingest for bounded, fully classified command, schema, payment-flow, skill, security, or documentation changes. Use additive full ingest for a major boundary, broad architecture or authorization change, incompatible payment behavior, missing prior evidence, or capsule-policy change. Preserve all older-version findings in the cumulative source.

## Evidence

- [Release record](../../../../raw/github/stripe/link-cli/releases/link-cli/0.13.0/2026-08-15/manifest.json)
- [Release notes](../../../../raw/github/stripe/link-cli/releases/link-cli/0.13.0/2026-08-15/release-notes.md)
- [Snapshot manifest](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/manifest.json)
- [CLI changelog](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/CHANGELOG.md)
- [CLI package manifest](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/package.json)
