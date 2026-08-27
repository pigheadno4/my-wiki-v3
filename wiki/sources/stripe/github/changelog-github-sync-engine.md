---
title: "GitHub changelog: stripe/sync-engine"
type: source
date_ingested: 2026-08-27
date_updated: 2026-08-27
original_format: github-repo
raw_files:
  - "github/stripe/sync-engine/snapshots/2026-08-26-93321ab/manifest.json"
tags: [stripe, sync-engine, data-pipeline, postgres, temporal, changelog, github-repository]
---

## Overview

Commit-qualified retained history for `stripe/sync-engine`. Durable architecture and implementation knowledge belongs in [[source-github-sync-engine]]. The workspace package version is recorded as metadata and must not be treated as a repository release without a matching retained tag.

## Initial Baseline — `default-branch@93321ab` (2026-08-20)

| Repository | Branch | Workspace version | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `stripe/sync-engine` | `dev` | `0.2.5` | `93321ab3644d5460213725abe0595247c403eb46` | Full |

**Baseline established:** OpenAPI-driven Stripe catalog discovery; account-qualified records; concurrent, resumable backfill; Events API, verified-webhook, and WebSocket live paths; connector protocol; PostgreSQL projection and staleness-gated writes; state migrations; and Temporal-managed setup, backfill, live synchronization, reconciliation, and teardown.

**Important boundaries:** the repository describes itself as under active development and redirects active work to `stripe/sync-engine-fork`. It is intended for trusted internal deployment, exposes an unauthenticated `/internal/query` endpoint, and does not establish production support or merchant eligibility. Several design documents are stale relative to implementation.

**Version identity:** `0.2.5` comes from retained workspace metadata. Because this work item follows the `dev` default branch at an exact SHA and contains no retained matching release tag, its durable identity is `default-branch@93321ab`, not `sync-engine@0.2.5`.

**Collection strategy:** this repository uses a bounded `commit-tree-v1` operational capsule. The snapshot retained 162 selected files and assigned 105 evidence and context paths to the approved full ingest. Tests and unrelated files are excluded from the baseline but can be collected through a targeted supplement if a future query requires them.

**Future comparison rule:** compare a newly collected default-branch SHA against `93321ab3644d5460213725abe0595247c403eb46`. Use delta ingest for bounded, fully classified connector, schema, workflow, security, or documentation changes. Use additive full ingest for a major architecture or trust-boundary change, a new release identity, missing prior evidence, or capsule-policy change. Preserve this baseline and earlier-version findings in the cumulative source.

## Evidence

- [Snapshot manifest](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/manifest.json)
- [README](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/README.md)
- [Repository changelog](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/CHANGELOG.md)
- [Workspace package manifest](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/package.json)
- [Engine architecture](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/docs/engine/ARCHITECTURE.md)
- [Service lifecycle implementation](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/apps/service/src/temporal/workflows/pipeline-lifecycle.ts)
