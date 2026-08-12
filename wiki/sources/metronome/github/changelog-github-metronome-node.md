---
title: "GitHub changelog: Metronome-Industries/metronome-node"
type: source
date_ingested: 2026-08-12
original_format: github-repo
raw_files:
  - "github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/manifest.json"
tags: [metronome, node-js, typescript, server-sdk, changelog, github-repository]
---

## Overview

Package-qualified release ledger for `Metronome-Industries/metronome-node`. Cumulative implementation knowledge belongs in [[source-github-metronome-node]]; this page records what changed and preserves historical upgrade boundaries.

## `@metronome/sdk@3.10.0` (2026-07-23)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@metronome/sdk` | Initial retained baseline | `3.10.0` | `f8ac11210fbca9616a220e82ea82ac1d340ea2df` | Full |

**Important findings:** Added `add_credit_type_conversions` to rate-card updates, `cost_basis` to commit responses, and `applicable_contract_ids` to customer-commit edits; removed `supersede` from contract transition typing; documented daily recurring commits and updated embeddable-dashboard documentation.

**Developer impact:** Integrations can add custom pricing-unit conversions while editing a rate card and can read commit cost basis. Customer-level commit edits can change contract applicability where allowed. Code that supplied the removed transition field must follow the current generated type and product guidance.

**Migration action:** No mandatory migration is documented. Treat the additions as optional and confirm account configuration before using them. Do not infer a replacement behavior for removed `supersede` from the release note alone.

**Evidence boundary:** This is the first retained package release, so no prior exact-SHA comparison exists. Release notes are dated 2026-07-22 while GitHub records the release publication on 2026-07-23. Broader SDK behavior in the cumulative source is implementation present at `3.10.0`, not functionality introduced by this release.

**Evidence:**

- Release manifest: `raw/github/metronome/metronome-node/releases/sdk/3.10.0/2026-08-12/manifest.json`
- Release notes: `raw/github/metronome/metronome-node/releases/sdk/3.10.0/2026-08-12/release-notes.md`
- Snapshot manifest: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/manifest.json`
- Repository changelog: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/CHANGELOG.md`
- Rate-card update type: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/v1/contracts/rate-cards/rate-cards.ts`
- Commit model and edit type: `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/shared.ts` and `raw/github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/files/src/resources/v2/contracts.ts`

## Retained Major-Version History

- `3.7.0` removed deprecated `/payments/*` endpoints and changed create/edit contract responses to return contract data.
- `3.0.0` removed deprecated MCP tool schemes and made code mode the supported invocation path.
- `1.0.0` moved the SDK to built-in Web Fetch with zero runtime dependencies and introduced the migration boundaries documented in `MIGRATION.md`.

These entries are historical navigation derived from the cumulative repository changelog. They are not independent full ingests of those releases and should not be used as exact old-version source snapshots.
