---
title: "GitHub changelog: braintree/uuid"
type: source
date_ingested: 2026-08-31
original_format: github-repo
raw_files:
  - "github/braintree/uuid/snapshots/2026-08-31-d134a2c/manifest.json"
tags: [braintree, uuid, javascript, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/uuid`. Cumulative implementation knowledge belongs in [[source-github-uuid]] and the linked immutable snapshot.

## `@braintree/uuid@2.0.0` (2026-01-20)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@braintree/uuid` | Initial baseline | `2.0.0` | `d134a2ca93d12705a76ff036baeba568016f9b13` | Full |

**Exact release change:** The retained implementation first uses global `crypto.randomUUID()`, falls back to `crypto.getRandomValues()` with explicit v4 and variant bit setting, and throws when neither secure random API is available. The repository changelog describes this as a robust v4 update and separately records Jest, Prettier, and repository Node-version updates.

**Developer impact:** Consumers receive a UUID string from the same zero-argument CommonJS export, but their runtime must provide a compatible global secure-random API. There is no insecure `Math.random()` fallback.

**Migration action:** Before upgrading a browser, WebView, or Node integration, verify that its supported runtimes expose global `crypto.randomUUID` or `crypto.getRandomValues`, and handle or prevent the explicit no-secure-source error. The retained evidence does not include an exact v1 implementation, so it cannot define a complete `1.0.1` to `2.0.0` behavioral diff.

**Updated source sections:** Baseline and package boundary; UUID generation; release and evidence boundaries.

**Evidence boundary:** This is the first retained exact-SHA baseline. Upstream release notes are unavailable, tests are excluded, and there is no comparison manifest or exact v1 snapshot.

**Evidence:**

- Release manifest: `raw/github/braintree/uuid/releases/uuid/2.0.0/2026-08-31/manifest.json`
- Release notes: `raw/github/braintree/uuid/releases/uuid/2.0.0/2026-08-31/release-notes.md`
- Snapshot manifest: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/manifest.json`
- Repository changelog: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/CHANGELOG.md`
- Runtime implementation: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/index.js`
- Type declaration: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/index.d.ts`
- Package metadata: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/package.json`

## Earlier Version Context

- `1.0.1` records development-dependency updates.
- `1.0.0` records development-dependency updates and a repository Node-version move to v18.

These are retained changelog statements only. Separate exact release snapshots are not present, and the Node entries do not establish a package `engines` requirement.
