---
title: "GitHub changelog: Metronome-Industries/terraform-provider-metronome"
type: source
date_ingested: 2026-08-15
original_format: github-repo
raw_files:
  - "github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/manifest.json"
tags: [metronome, terraform, provider, experimental, changelog, github-repository]
---

## Overview

Package-qualified release ledger for `Metronome-Industries/terraform-provider-metronome`. Cumulative implementation knowledge belongs in [[source-github-terraform-provider-metronome]]; this page records release changes and preserves the boundary between generic provider machinery and registered Metronome Terraform capabilities.

## `terraform-provider-metronome@0.1.0-alpha.3` (2026-06-01)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `terraform-provider-metronome` | Initial retained baseline | `0.1.0-alpha.3` | `f06da6d6afee448e9fe9bad77d213cf6159d11f8` | Full |

**Important findings:** The release notes add schema-description support for per-resource API permissions and semantic-equivalence checks for dynamic validators. They also list fixes for dynamic values, JSON encoding, patch serialization, data-source IDs, nested nulls, float planning, and generated collection handling.

**Developer impact:** These changes improve generic generated-provider machinery, but the exact `0.1.0-alpha.3` implementation registers zero resources and zero data sources. There is no usable Metronome Terraform management surface to migrate to in this retained baseline.

**Migration action:** Do not use this experimental release in production. Existing prerelease evaluators should keep credentials in environment variables where possible, verify Terraform CLI 1.0 or later, and reassess the exact registration surface before adopting any future version.

**Evidence boundary:** This is the first retained exact-SHA release, so no prior snapshot comparison exists. The upstream changelog includes `alpha.2` and `alpha.1`, but they are navigation history rather than independently collected implementation baselines. Generic changelog entries about resources or data sources do not override the empty registration lists in the exact source.

**Future comparison rule:** Compare package-qualified versions and exact snapshot fingerprints. Any first registered Metronome resource or data source, production-readiness change, authentication/schema incompatibility, or broad generated-surface change requires full additive ingest. A contained internal correction may use delta ingest only when every retained change is classified and the registration surface is explicitly rechecked.

**Evidence:**

- Release manifest: `raw/github/metronome/terraform-provider-metronome/releases/terraform-provider-metronome/0.1.0-alpha.3/2026-08-15/manifest.json`
- Release notes: `raw/github/metronome/terraform-provider-metronome/releases/terraform-provider-metronome/0.1.0-alpha.3/2026-08-15/release-notes.md`
- Snapshot manifest: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/manifest.json`
- Repository changelog: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/CHANGELOG.md`
- Provider registration: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/internal/provider.go`

## Earlier Prerelease Navigation

- `0.1.0-alpha.2` (2025-06-09) records a generic API-generation change described as inferring all services.
- `0.1.0-alpha.1` (2025-06-02) records API and SDK Studio updates, environment-property support, a private-production-repository build fix, and a Terraform CLI 1.12 compatibility dependency update.

These entries come from the cumulative changelog. They are not full ingests of those tags and cannot prove the exact resources, data sources, provider schema, or runtime behavior present in either historical release.
