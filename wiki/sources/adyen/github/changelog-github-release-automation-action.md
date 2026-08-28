---
title: "GitHub changelog: adyen/release-automation-action"
type: source
date_ingested: 2026-08-28
date_updated: 2026-08-28
original_format: github-repo
raw_files:
  - "github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/manifest.json"
tags: [adyen, release-automation, github-actions, semantic-versioning, changelog, github-repository]
---

## Overview

Commit-qualified retained history for `adyen/release-automation-action`. Durable release behavior, limits, and query guidance belong in [[source-github-release-automation-action]].

## Initial Baseline - `default-branch@9675ced` (2026-05-29)

| Ref | SHA | Repository version | Collection date | Ingest mode |
| --- | --- | --- | --- | --- |
| `main` | `9675cedc9efe9d0b5563bd7dd0f8ef88f26ad03b` | `1.4.0` | 2026-08-28 | Full |

**Baseline established:** merged-pull-request discovery since `v<current-version>`; label-based patch, minor, and major selection; prerelease start, increment, and completion; version-file replacement; release pull-request creation; optional auto-merge; GitHub release creation; and run-summary output.

**Operational impact:** adopters can standardize release proposals and GitHub releases around repository labels and a checked-in `VERSION` file. Correct behavior still depends on branch protection, repository settings, token permissions, consumer version-file structure, and the bounded GitHub comparison result.

**Retained limits:** comparison fetches at most 100 commits, five associated pull requests per commit, and five labels per pull request. Changelog output is limited to sorted pull-request numbers. Label normalization replaces only the first space, and semantic-version input is parsed without a complete validation gate.

**Identity note:** repository metadata reports `1.4.0`, but this work item is tracked as default-branch commit evidence rather than a package release. The README usage example references `v1.3.0` and is not treated as the latest version selector.

**Ownership boundary:** this action does not own Adyen checkout behavior, merchant eligibility, downstream SDK APIs, or `adyen-sdk-automation` generation history.

**Future comparison rule:** compare a newly discovered `main` SHA with this exact commit. A fully classified documentation or bounded action-input change can use delta ingest. Broad changes to version calculation, GitHub queries, permissions, pull-request creation, or release publication require additive full ingest.

## Evidence

- [Snapshot manifest](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/manifest.json)
- [README](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/README.md)
- [Action definition](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/action.yml)
- [Release implementation](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/src/release.ts)
