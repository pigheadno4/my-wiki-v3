---
title: "GitHub: adyen/release-automation-action"
type: source
date_ingested: 2026-08-28
date_updated: 2026-08-28
original_format: github-repo
raw_files:
  - "github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/manifest.json"
tags: [adyen, release-automation, github-actions, semantic-versioning, release-engineering, github-repository]
---

## Overview

`adyen/release-automation-action` is a reusable composite GitHub Action that proposes semantic versions, updates version files, opens release pull requests, and creates GitHub releases. This initial full ingest records `default-branch@9675ced`, exact SHA `9675cedc9efe9d0b5563bd7dd0f8ef88f26ad03b`, committed on 2026-05-29 and collected on 2026-08-28; the retained repository version is `1.4.0`.

Repository: <https://github.com/Adyen/release-automation-action>

## Evidence Boundary

- Findings are commit-qualified. The repository is tracked by its default branch, not as a package release.
- The retained capsule contains seven files: repository documentation, action configuration, package and version metadata, license, and the two TypeScript source files.
- The action automates repository releases. It does not implement checkout, payment processing, merchant configuration, or payment-method eligibility.
- `adyen/release-automation-action` is independent from `adyen/adyen-sdk-automation`. The latter owns OpenAPI-to-SDK generation and release-note analysis; this repository provides generic release orchestration for a consumer repository.
- Tests and workflow fixtures are excluded by capsule policy. The retained source establishes control flow, but not successful execution against every consumer repository configuration.

## Grounding Excerpts

> "Looks through all the merged PR's since the previous release"
>
> `raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/README.md:8`

> "Based on their labels (e.g. \"Breaking change\", \"Feature\", \"Fix\"), creates a new PR proposing which version to release next"
>
> `raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/README.md:9`

> "commits(first: 100)"
>
> `raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/src/release.ts:142`

> "const normalizedLabel = label.toLowerCase().replace(' ', '-')"
>
> `raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/src/release.ts:208`

> "if: inputs.github-release == 'true' || (github.event.pull_request.merged && contains(github.event.pull_request.labels.*.name, 'release'))"
>
> `raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/action.yml:89`

## Release Decision Flow

The action reads the consumer repository's current version from `VERSION` and compares `v<current-version>` with the configured development branch. It filters the comparison to commits associated with merged pull requests, deduplicates their numbers, sorts them numerically, and emits those numbers as the proposed changelog.

When unreleased commits exist, the default increment is patch. A `feature` label promotes the result to minor, while `breaking-change` immediately selects major. Label matching lowercases the label and replaces only the first space with a hyphen, so variants with multiple spaces or other punctuation are not guaranteed to match.

When no comparison base exists or the branch is not ahead, the action emits no increment. `nextVersion` then leaves the stable version unchanged unless prerelease mode requires a transition.

## Prerelease Behavior

The default prerelease separator is `-beta`:

- starting prerelease mode appends the separator to the newly calculated stable version;
- running prerelease mode again increments the numeric suffix, with a missing or nonnumeric suffix treated as zero before incrementing;
- disabling prerelease mode while a suffix is present returns the stable portion without another semantic increment.

The implementation requires a nonempty separator. It parses the three stable components with `parseInt` but does not explicitly validate a complete semantic version before calculating the result, so malformed consumer `VERSION` content is outside the dependable contract.

## Pull Request and Release Lifecycle

The composite action checks out the complete development-branch history with the supplied token, replaces the old version in `VERSION` and any configured version files, and creates a pull request on `promote/<develop-branch>`. The pull request carries the `release` label, a generated list of merged pull requests, and a full comparison link.

Auto-merge runs only when enabled and a pull request was newly created. A GitHub release is created either through the explicit `github-release` input or when a merged pull request carries the `release` label. A strict `major.minor.patch` regular expression marks a release as stable; all other version strings are published as prereleases.

The documented prerequisites include branch protection, permission for Actions to create pull requests, and either the default GitHub token or a repository-scoped personal access token. The README example still references action `v1.3.0`, while retained `VERSION` and `package.json` both report `1.4.0`; use exact refs or a reviewed release tag rather than copying that example version as current.

## Operational Limits and Caveats

- The GraphQL comparison requests at most 100 commits, five associated pull requests per commit, and five labels per pull request. Larger histories or heavily associated commits can be incomplete without direct upstream inspection.
- Changelog entries contain only deduplicated pull-request numbers; titles, authors, and labels are delegated to GitHub-generated release notes or later review.
- Version replacement uses a Perl text substitution across `VERSION` and configured files. The consumer must ensure the current version string appears only where replacement is intended.
- Creating release pull requests and enabling auto-merge depend on repository permissions, branch protection, and token behavior. Repository source does not prove those settings are active in a particular consumer.

## Version and Query Guidance

Use [[changelog-github-release-automation-action]] to identify the retained commit and future default-branch transitions. For questions about a downstream SDK release, inspect that SDK repository's source and changelog; this action can explain release mechanics but cannot establish what changed in the downstream product.

A bounded label, input, or release-step correction can use delta ingest. Changes to comparison scope, version calculation, token permissions, pull-request lifecycle, or release creation should trigger additive full ingest while preserving this baseline.

## Related

- Company: [[adyen]]
- Concept: [[adyen-sdk-automation]]
- Generation repository: [[source-github-adyen-sdk-automation]]
- History: [[changelog-github-release-automation-action]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/manifest.json) - exact-SHA capsule inventory and hashes
- [README](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/README.md) - purpose, prerequisites, usage, and development workflow
- [Action definition](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/action.yml) - inputs, version replacement, pull-request, auto-merge, and release steps
- [Release implementation](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/src/release.ts) - comparison, changelog, label, semantic-version, and prerelease behavior
- [Package metadata](../../../../raw/github/adyen/release-automation-action/snapshots/2026-08-28-9675ced/files/package.json) - retained repository version, runtime dependencies, and build commands
