---
title: "GitHub changelog: stripe/stripe-cli"
type: source
date_ingested: 2026-08-14
date_updated: 2026-08-14
original_format: github-repo
raw_files:
  - "github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/manifest.json"
tags: [stripe, stripe-cli, developer-tools, telemetry, changelog, github-repository]
---

## Overview

Package-qualified retained history for `stripe/stripe-cli`. Durable implementation knowledge belongs in [[source-github-stripe-cli]].

## Initial Baseline — `stripe-cli@1.50.0` (2026-08-13)

| Package | Version | Tag | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `stripe-cli` | `1.50.0` | `v1.50.0` | `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1` | Full |

**Baseline established:** direct and generated API commands, request controls and dry run, fixture execution, synthetic event triggers, webhook and thin-event listening/forwarding, OAuth and account contexts, request-log transport, and telemetry.

**Release-specific change:** the upstream notes contain one item: capture agent host and self-reported agent identifiers in telemetry. The baseline's other capabilities must not be attributed as newly introduced by `1.50.0`.

**Collection exception:** the immutable first snapshot includes 28 Go test files. Future capsules use the corrected policy that excludes Go tests; this policy reduction is not an upstream product change.

**Future comparison rule:** compare package-qualified stable releases against `stripe-cli@1.50.0`. Use delta ingest for bounded command, fixture, webhook, request, authentication, or telemetry changes with complete classified evidence. Use additive full ingest for a major version, broad architecture change, incompatible command or authentication behavior, missing prior evidence, or capsule-policy change. Preserve older-version findings in the cumulative source.

## Evidence

- [Release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/2026-08-14/manifest.json)
- [Release notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/2026-08-14/release-notes.md)
- [Snapshot manifest](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/manifest.json)
- [Telemetry implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/stripe/analytics_telemetry.go)
