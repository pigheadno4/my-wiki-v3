---
title: "GitHub changelog: braintree/web-sdk-github-actions"
type: source
date_ingested: 2026-09-29
original_format: github-repo
raw_files:
  - "github/braintree/web-sdk-github-actions/snapshots/2026-09-29-e9c8ae9/manifest.json"
  - "github/braintree/web-sdk-github-actions/supplements/2026-09-29-e9c8ae9-d8cf7fde/manifest.json"
tags: [braintree, developer-tooling, github-actions, release-engineering, changelog, github-repository]
---

## Overview

Commit-qualified history for `braintree/web-sdk-github-actions`. Durable implementation knowledge and caveats belong in [[source-github-web-sdk-github-actions]]. This ledger does not assign semantic versions to the repository or represent downstream SDK releases.

## `default-branch@e9c8ae9` (2026-09-10)

| Ref | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `main` | Initial baseline | `default-branch@e9c8ae9` | `e9c8ae99ae5365f91f8e5372ae2d9d2dc7a427e0` | Full |

Collected and ingested 2026-09-29, work item `github-4776aefdf1eeb1056827`. Fully read 28 retained files plus manifests and attachment; the root operations log alone used the user's focused-context exception. No prior exact-SHA baseline exists, so these are retained capabilities, not newly introduced features.

**Baseline:** Composite actions cover Git/Node setup, version and changelog preparation, optional release PR creation, npm publication, release-note extraction and Confluence forwarding. Reusable workflows cover CI, PR/Jira validation, stale cleanup and release operations.

**Operational impact:** Consumers must distinguish preparation from publication, verify their chosen workflow/action revisions and permissions, and account for branch pushes, PRs, published artifacts and deletion-capable cleanup. Prerelease controls in the composite are not all exposed by wrapper workflows. This baseline does not establish checkout or merchant eligibility.

**Caveats:** README merge/tag/full-pipeline claims exceed the retained authored implementation. The separate dry-release workflow transfers only a version string, not the bumped files, and lacks the claimed release-notes step. Change detection has a confirmed shell syntax error. Release-note shell interpolation, mutable Jira helper checkout, hardcoded Jira runner and older pinned helper revisions remain explicit limitations. Generated bundles and delegated runtime were not verified.

**Migration:** No previous retained version and no measured migration diff. Do not replace an existing release process based solely on this baseline. Future comparisons must preserve these findings and tie any claimed fix to exact retained evidence.

**Updated sections:** Initial source, [[braintree-sdk-release-automation]], company catalog, provider index and operations logs. No payment concept or cross-provider comparison changed.

## Raw Sources

- [Snapshot](../../../../raw/github/braintree/web-sdk-github-actions/snapshots/2026-09-29-e9c8ae9/manifest.json)
- [Same-SHA supplement](../../../../raw/github/braintree/web-sdk-github-actions/supplements/2026-09-29-e9c8ae9-d8cf7fde/manifest.json)
