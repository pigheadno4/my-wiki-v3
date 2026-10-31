---
title: "GitHub changelog: Metronome-Industries/metronome-node"
type: source
date_ingested: 2026-08-12
date_updated: 2026-10-31
original_format: github-repo
raw_files:
  - "github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/manifest.json"
  - "github/metronome/metronome-node/snapshots/2026-08-12-f8ac112/manifest.json"
tags: [metronome, node-js, typescript, server-sdk, changelog, github-repository]
---

## Overview

Package-qualified release ledger for `Metronome-Industries/metronome-node`. Cumulative implementation knowledge belongs in [[source-github-metronome-node]]; this page records what changed and preserves historical upgrade boundaries.

## `@metronome/sdk@3.11.0` (2026-10-27)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@metronome/sdk` | `3.10.0` | `3.11.0` | `5e8d4ac4659f9378f2341e4e18f89274908523ed` | Full additive |

**Ingested:** 2026-10-31, work item `github-255c5762c0ce5e6af973`. Explicit user-approved full override of the generated delta recommendation, with focused reading. All `3.10.0` knowledge and raw history remain retained.

**Breaking changes:** V1/V2 contract lists now return cursor pages, not `ContractListResponse`; traverse with async iteration or manual page methods and update type imports. Required response timestamps add `anchor_date` for recurring commits/credits and `created_at` for subscriptions. MCP server source/install instructions are removed; the release notes preserve existing published versions, without runtime availability proof.

**Additional source finding:** Stripe collection-method unions drop `auto_charge_payment_intent` and `manually_charge_payment_intent`; only automatic charging and send-invoice values remain on the affected customer/billing-config surfaces. Tax-provider text loses its former PaymentIntent-only qualifier. Neither change establishes service retirement, eligibility or a change to separate threshold payment gates.

**New billing surface:** quantity/spend balance access, invoice quantity-consumption attribution, optional credit creation time, subscription renaming/product custom fields/custom unit, pricing-unit create/archive, prepaid-threshold commit duration/rate/rollover, composite-spend inclusion, package `CUSTOM_DATE` schedules and historical-commit invoice inclusion. Manual ledger `uniqueness_key` rejects duplicates with `409`; do not expect successful replay.

**Notifications and discovery:** new V2 offset lifecycle controls and system-type discovery; system publishing toggles through `notifications.offset.edit`, not a nonexistent system-edit method. Contract and offset lists use body `cursor`, while the newly added contract-level named-schedule list uses body `next_page`. System list is not auto-paginated. Threshold types add quantity/access and combined percentage scope. Custom-field changes do not emit credit/commit/contract edit events.

**Corrections and constraints:** stale Payments API-index section removed; V2 edit docs correct edit-versus-contract ID wording while details remain optional. Display-name-only metric update becomes typed. Usage docs clarify UTC-midnight/day-span bounds and 200 total grouped filter values. The earlier Web Fetch migration is retained, not newly introduced here.

**Updated knowledge:** cumulative source, six existing concepts (integrations, customers/contracts, credits/commits, products/rate cards, billable metrics, alerts/notifications), company, provider index and logs. No new source/concept or cross-company comparison. Package source/types/docstrings do not prove tenant enablement, runtime delivery, payment or reconciliation.

**Evidence:**

- Release manifest: `raw/github/metronome/metronome-node/releases/sdk/3.11.0/2026-10-31/manifest.json`
- Release notes: `raw/github/metronome/metronome-node/releases/sdk/3.11.0/2026-10-31/release-notes.md`
- Snapshot manifest: `raw/github/metronome/metronome-node/snapshots/2026-10-31-5e8d4ac/manifest.json`
- Comparison: `tracking/github/repos/metronome/metronome-node/comparisons/sdk/3.10.0--3.11.0/comparison.md`
- Comparison manifest: `tracking/github/repos/metronome/metronome-node/comparisons/sdk/3.10.0--3.11.0/comparison.json`
- Cumulative implementation and exact raw-file routes: [[source-github-metronome-node]]

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
