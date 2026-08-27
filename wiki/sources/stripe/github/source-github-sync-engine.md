---
title: "GitHub: stripe/sync-engine"
type: source
date_ingested: 2026-08-27
date_updated: 2026-08-27
original_format: github-repo
raw_files:
  - "github/stripe/sync-engine/snapshots/2026-08-26-93321ab/manifest.json"
tags: [stripe, sync-engine, data-pipeline, postgres, temporal, webhooks, github-repository]
---

## Overview

`stripe/sync-engine` is an experimental framework for synchronizing Stripe API resources into Postgres. This initial full ingest records exact default-branch commit `93321ab3644d5460213725abe0595247c403eb46` on `dev`, committed on 2026-08-20 and collected on 2026-08-26. The workspace declares version `0.2.5`, but the retained identity is `default-branch@93321ab`; no matching release tag was collected.

Repository: <https://github.com/stripe/sync-engine>

## Evidence Boundary

- This is an operational data synchronization framework, not a checkout SDK or a source of merchant-facing payment eligibility.
- The README labels the project as under active development, recommends internal deployment, warns that access controls are not tight, and redirects active development to `stripe/sync-engine-fork`.
- The fork is a separate repository and evidence history. Its behavior is not merged into this source without an independent collection.
- The retained capsule contains 162 selected files. The approved full ingest read all 105 assigned evidence and wiki-context paths; excluded tests and unrelated files remain outside this baseline.
- Runtime source controls when retained architecture documents disagree with current code. Several documents describe archived, proposed, or older service behavior.

## Architecture

The repository is a TypeScript/pnpm workspace with two applications and reusable connector packages:

| Component | Role |
| --- | --- |
| `apps/engine` | Local engine, API, and CLI orchestration |
| `apps/service` | Long-running service and Temporal workflow orchestration |
| `packages/source-stripe` | Stripe catalog discovery, backfill, event, webhook, and WebSocket source behavior |
| `packages/destination-postgres` | PostgreSQL schema projection, writes, deletes, and connection support |
| `packages/state-postgres` | Pipeline state, cursor, and migration persistence |
| `packages/protocol` | Connector message protocol and NDJSON transport |
| `packages/util-postgres` | Shared SQL, upsert, SSL, and rate-limiting helpers |

The engine resolves source, destination, and state connectors, creates schemas, and runs source messages through filtering and destination execution. The service wraps setup, backfill, live synchronization, reconciliation, and teardown in Temporal activities and workflows.

## Stripe Source Discovery

The Stripe connector derives its catalog from an OpenAPI description and a resource registry. The catalog is wider than checkout and can include customers, products, prices, subscriptions, invoices, payment resources, and other supported Stripe objects.

Each configured Stripe account is represented explicitly. Persisted records use the composite identity `(id, _account_id)`, preventing identical Stripe object IDs from different accounts from sharing one destination row. Account metadata and configured account constraints are incorporated into discovery and synchronization.

An API version can be configured, but the current schema makes it optional and the connector can use its bundled fallback. Older documentation that says an API version is mandatory does not match this SHA.

## Backfill and State

Backfill uses time ranges and can subdivide them to process work concurrently. Cursor and sync state are persisted so a pipeline can resume rather than restart all retained work. Dependency transforms expand or reorder selected Stripe resources where their relationships require it, including list expansion and subscription-item handling.

The connector narrowly recognizes some product or entitlement errors as unsupported-resource conditions. Unknown failures remain stream errors rather than being silently treated as unavailable resources.

At the engine level, a failed destination stream is isolated: the stream error is emitted and other streams can continue. This improves partial progress but means pipeline-level completion must not be interpreted as proof that every stream succeeded. Operators need stream-error monitoring and reconciliation.

## Live Synchronization

The retained source supports multiple live paths:

- polling Stripe's Events API;
- receiving and verifying Stripe webhooks;
- WebSocket transport for service-managed delivery.

Webhook payloads are signature-verified before event processing. Event handling maps Stripe event objects back to catalog resources and emits updates or deletes. Network, `429`, and server-side failures use bounded retry behavior, including `Retry-After` handling where available.

These paths complement backfill. They do not remove the need for reconciliation because delayed, failed, unsupported, or out-of-order event processing can leave destination state incomplete.

## PostgreSQL Destination

The destination projects source schemas into PostgreSQL tables and generated columns. Writes are staleness-gated so an older object representation does not overwrite newer retained state. Deletes are hard deletes for the corresponding account-qualified record.

Schema setup and teardown are explicit operations. Teardown rejects protected schemas. State migrations are versioned, but the retained migration code has boundaries around legacy layouts and does not establish arbitrary split-schema migration support.

AWS and connection-string helpers provide database connection options. Their presence does not prove a production deployment topology or hosted operational support.

## Temporal Service Lifecycle

The service separates pipeline lifecycle work into setup, backfill, live synchronization, reconciliation, status updates, and teardown. The backfill loop repeatedly schedules bounded work until synchronization state indicates completion, while Temporal supplies durable workflow execution.

Retained service documentation is not fully synchronized with implementation. Endpoint names, state shapes, credential-store assumptions, and some workflow descriptions differ from current code. The source files under `apps/service/src` and current API schemas are authoritative for this commit.

## Security and Operational Limits

The engine API exposes `/internal/query` without an application authentication layer. The code assumes a trusted private network; exposing this endpoint publicly would cross the repository's stated trust boundary. The README's broader warning about limited access controls reinforces that this is not a hardened multi-tenant service as retained.

Other operational limits include:

- partial stream failure can coexist with progress in other streams;
- retries do not prove eventual success;
- reconciliation remains necessary after live processing;
- the active fork may contain newer behavior not represented here;
- no local source evidence establishes Stripe support, SLA, merchant entitlement, or production readiness.

## Documentation Drift

The retained documentation includes an archived Kafka/cloud design, a proposed event endpoint, older endpoint and state names, and credential-store descriptions that do not consistently match implementation. `docs/service/temporal.md` also differs from current Temporal code. These files remain useful design history, but query answers about current behavior at `93321ab` should prefer executable source and current schemas.

## Query Guidance

Use this source for detailed questions about the retained Stripe-to-Postgres architecture, connector protocol, backfill, live events, state, destination writes, and Temporal orchestration. For rough questions outside the retained capsule, clone the repository and inspect the relevant code. For current upstream behavior, collect a newer exact SHA and compare it with this baseline before updating conclusions.

## Related

- Company: [[stripe]]
- History: [[changelog-github-sync-engine]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/manifest.json) — exact-SHA capsule inventory and hashes
- [README](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/README.md) — project status, deployment, access-control, and fork boundaries
- [Repository changelog](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/CHANGELOG.md) — retained upstream change history
- [Engine implementation](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/apps/engine/src/lib/engine.ts) — connector orchestration
- [Pipeline implementation](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/apps/engine/src/lib/pipeline.ts) — source-to-destination processing
- [Engine API](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/apps/engine/src/api/app.ts) — internal query endpoint and API surface
- [Stripe catalog](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/packages/source-stripe/src/catalog.ts) — OpenAPI-driven discovery
- [Stripe list source](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/packages/source-stripe/src/src-list-api.ts) — backfill and pagination behavior
- [Stripe event source](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/packages/source-stripe/src/src-events-api.ts) — event polling
- [Stripe webhook source](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/packages/source-stripe/src/src-webhook.ts) — verified webhook ingestion
- [Retry implementation](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/packages/source-stripe/src/retry.ts) — retryable failures and delay handling
- [Postgres destination](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/packages/destination-postgres/src/index.ts) — destination operations
- [Postgres upsert helper](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/packages/util-postgres/src/upsert.ts) — staleness-gated writes
- [Pipeline lifecycle workflow](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/apps/service/src/temporal/workflows/pipeline-lifecycle.ts) — Temporal lifecycle orchestration
- [Backfill workflow](../../../../raw/github/stripe/sync-engine/snapshots/2026-08-26-93321ab/files/apps/service/src/temporal/workflows/pipeline-backfill.ts) — bounded backfill scheduling
