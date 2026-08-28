---
title: "GitHub changelog: stripe/stripe-apps"
type: source
date_ingested: 2026-08-28
date_updated: 2026-08-28
original_format: github-repo
raw_files:
  - "github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/manifest.json"
tags: [stripe, stripe-apps, dashboard, ui-extensions, app-manifest, changelog, github-repository]
---

## Overview

Commit-qualified retained history for `stripe/stripe-apps`. Durable platform, schema, and example knowledge belongs in [[source-github-stripe-apps]]. The repository does not expose a meaningful semantic release identity, and its root changelog delegates SDK releases to `@stripe/ui-extension-sdk` on npm.

## Initial Baseline — `default-branch@9b14b71` (2026-08-21)

| Repository | Branch | Schema package metadata | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `stripe/stripe-apps` | `main` | `@stripe/app-manifest-schema@0.0.0` | `9b14b71be496ca299401b3303b572856fd19baf4` | Full |

**Baseline established:** standard and local app-manifest schemas; the separate extension-manifest schema; distribution, API-access, sandbox, CSP, permission, and viewport configuration; and the complete retained Pizzazz Loyalty full-page example with typed routing, Dashboard UI components, settings, roles, and local state patterns.

**Important boundaries:** the example is entirely mock-backed and proves no live Stripe API or payment behavior. Permission enums do not establish merchant eligibility. The example manifest does not satisfy the retained standard schema literally, and the repository-level changelog does not provide `@stripe/ui-extension-sdk` release details.

**Version identity:** `0.0.0` is placeholder schema package metadata, not a released repository version. The durable identity is `default-branch@9b14b71` at the exact SHA above.

**Collection strategy:** this repository uses a bounded `commit-tree-v1` capsule containing root guidance, manifest schemas, and the current full-page example source. Tests, fixtures, lockfiles, generated/decorative assets, and workflows are excluded from routine ingest.

**Future comparison rule:** compare a newly collected `main` SHA against `9b14b71be496ca299401b3303b572856fd19baf4`. Use delta ingest for bounded, classified schema, example, or documentation changes. Use additive full ingest for a new manifest model, broad UI-extension architecture change, incompatible permission/access model, major payment-behavior addition, missing prior evidence, or capsule-policy change. Preserve this baseline and its contradictions in the cumulative source.

## Evidence

- [Snapshot manifest](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/manifest.json)
- [Root README](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/README.md)
- [Repository changelog](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/CHANGELOG.md)
- [Standard manifest schema](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/schema/stripe-app.schema.json)
- [Extension manifest schema](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/schema/stripe-app.schema.yaml)
- [Full-page example manifest](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/stripe-app.json)
- [Full-page mock API](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/src/data/api.ts)
