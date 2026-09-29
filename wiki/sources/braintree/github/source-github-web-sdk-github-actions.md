---
title: "GitHub: braintree/web-sdk-github-actions"
type: source
date_ingested: 2026-09-29
original_format: github-repo
raw_files:
  - "github/braintree/web-sdk-github-actions/snapshots/2026-09-29-e9c8ae9/manifest.json"
  - "github/braintree/web-sdk-github-actions/supplements/2026-09-29-e9c8ae9-d8cf7fde/manifest.json"
tags: [braintree, developer-tooling, github-actions, release-engineering, github-repository]
---

## Overview

Engineering automation for Braintree web SDK repositories, retained at `default-branch@e9c8ae9` on `main`, exact SHA `e9c8ae99ae5365f91f8e5372ae2d9d2dc7a427e0`. The commit is dated 2026-09-10 and was collected on 2026-09-29. This is a commit baseline, not a semantic package release or proof of a downstream SDK release.

The evidence comprises 18 snapshot files and a same-SHA supplement with nine workflows plus the lockfile: 28 files, 76,720 bytes. Generated bundles are outside the retained capsule. The source describes authored implementation and wiring, not a successfully executed release.

## Key Takeaways

- Release preparation, publication and GitHub release creation are separate responsibilities despite broader README wording.
- The version-bump action exposes normal and prerelease controls, a calculation-only TypeScript path and optional automatic PR creation. Its enclosing action still performs setup and local branch operations in dry-run mode.
- Reusable workflows cover CI, semantic PR titles, optional Jira references, stale cleanup and release operations; the retained change-detection shell block fails syntax checking.
- Internal calls frequently pin a different commit. Reading current authored source does not verify those older implementations or the excluded executable bundles.
- This repository provides no merchant-facing payment API, checkout integration, account eligibility or transaction-processing evidence.

## Grounding Quotes

Locations below are relative to the snapshot `files/` directory unless marked supplement:

- `README.md:36`: "Validate CHANGELOG, bump npm version, create release branch + PR, merge, and tag."
- `src/release-pr.ts:20`: "We don't wait on the merge, and we don't tag here. Tagging happens on merge."
- `actions/version-bump/action.yml`, description: "Bump version + CHANGELOG on a throwaway branch and open a release PR into the base branch"
- `src/validate-changelog.ts`, failure text: "UNRELEASED section not found in CHANGELOG.md"
- Supplement `.github/workflows/release-dry-run.yml:3`: "Dry runs steps of: CI, version_bump, npm publication, Github release notes"

## Details

### Version And Changelog Preparation

The composite `actions/version-bump/action.yml` takes `version-type`, `github-token`, `base-branch` (default `main`), optional `feature-tag`, optional `prerelease-level`, `dry-run` (default false), and `create-pr` (default true). It fetches history and checks out `release-bump-$GITHUB_RUN_ID` from `origin/$BASE_BRANCH`, validates `CHANGELOG.md`, invokes the bundled bump script, and conditionally invokes the release-PR script.

The corresponding authored `src/bump-version.ts` accepts prerelease identifiers `alpha`, `beta` and `rc`. An explicit level must be `premajor`, `preminor`, `prepatch` or `prerelease` and is rejected with a non-prerelease version type. Otherwise an existing prerelease advances via `prerelease`; a stable version starts via `preminor`. A feature tag appends to the prerelease identifier. Normal execution runs `npm version --no-git-tag-version`, replaces a line starting `## UNRELEASED` with the new version and UTC date, then stages package.json, package-lock.json and CHANGELOG.md and commits. The validation regex is looser than the replacement regex; passing validation alone does not guarantee a heading replacement.

`src/release-pr.ts` pushes the branch before deciding whether to create a PR. Only the exact string `false` disables PR creation; it still pushes the branch and prints manual-PR guidance. Otherwise it calls `octokit.rest.pulls.create`, returns the PR URL and stops. It does not merge, wait for merge, or create a tag. Its comment assigns tagging/deployment to a separate workflow but does not identify or prove that consumer workflow.

### Publication And Release Notes

`actions/npm-publish/action.yml` calls setup-node and runs `npm publish --provenance`, adding `--dry-run` when requested and supplying the token through `NODE_AUTH_TOKEN`. The release-notes action reads the package version, invokes the bundled extractor and conditionally runs `gh release create`.

The authored extractor selects the body between the first and second `## ` headings in CHANGELOG.md, or the remaining file after the first heading. It does not match that heading to the package version or reject an UNRELEASED first section. Extracted notes are interpolated directly into the shell command's double-quoted `--notes` argument: arbitrary quotes, backticks or shell expansions in notes are not safely isolated by this construction. This is a static risk, not a reproduced exploit or evidence that a particular release was affected.

The supplemental `publish.yml` accepts an explicit `ref` and checks it out separately for npm publication and GitHub release creation. The latter job depends on npm publication. It declares `id-token: write` for publication and `contents: write` for the release job; it contains no CI job. The separate `release-pipeline.yml` contains only CI and version-bump jobs, with contents/pull-request write permissions on the latter. Its required npm token is not consumed by a publication job there.

### Dry-Run Differences And Documentation Conflicts

> [!warning] Contradiction
> README describes version-bump as merging/tagging and release-pipeline as CI through npm and GitHub publication. The retained authored PR script stops after branch/PR creation, and the retained pipeline contains only CI and a pinned version-bump action call. Preserve this distinction rather than treating the README as an end-to-end release guarantee.

- In `src/bump-version.ts`, dry-run calculates with `semver.inc` and skips package/changelog modification and commit. The enclosing composite action still performs setup, fetch and `git checkout -B`; "no changes" is not a whole-action guarantee.
- The separate `release-dry-run.yml` uses inline `npm version --no-git-tag-version`, not that TypeScript calculation-only path. The version string passes to the publish job only for its summary; the job performs a fresh checkout with no transfer of bumped package files. It therefore does not demonstrate publication of the calculated candidate artifact.
- That dry-release workflow's description and README include release notes, but no release-notes job is present. It also does not expose the composite action's feature-tag or explicit prerelease-level inputs.
- Several called actions are pinned to `d08e2700fb9ffdfe87200621e25ad63e47014941`, not this collected commit. These observations establish workflow wiring and current authored-source distinctions, not the exact runtime of those delegated older actions.

### CI, PR Checks And Cleanup

| Surface | Retained contract and limitations |
| --- | --- |
| CI | Caller-supplied lint/test commands, skipped when empty; configurable runner and node-version file. Commands are executed as workflow shell, not treated as untrusted data. |
| Semantic PR title | Configurable conventional-commit types, scopes and ignore labels; delegated to a pinned external action. |
| Jira check | Skips bots, `no-jira` labels, drafts and an empty pattern. Authored helper tests PR body against a JavaScript RegExp. The job hardcodes `gh-2-core-ubuntu-latest` despite a configurable runner elsewhere, and checks out this repository's mutable `main` to run a bundle. |
| File-change check | Intended to distinguish markdown-only changes. At supplement line 34 its opening `if` is part of a comment, leaving an unmatched `fi`. `bash -n` on the exact run block fails; no operational `src_changed` result is established. |
| Stale cleanup | Defaults: PR/issues stale after 14 days then close after 7; branches stale after 21 then delete after 7. Configures open-PR branch protection and regex `^(main\|gh-pages\|release)$`; PR label exemption defaults to `dependencies`. These are consequential delegated actions, not read-only checks. |
| Script validation | Workflow configures typecheck, build and a dirty-`dist/` failure check. Its existence does not establish a successful run or source/bundle equivalence. |

### Toolchain And Documentation Adapter

The repository is a private npm package with no semantic version field. `.nvmrc` selects Node 24; TypeScript is strict CommonJS targeting ES2022, while `build.mjs` bundles all source entrypoints except `utils.ts` using esbuild targeting Node 24. The lock retains TypeScript 5.9.3, esbuild 0.25.12 and semver 7.8.1. The setup-node action at this commit installs global npm without a version pin and optionally runs `npm ci`; it is not a fully pinned runtime environment.

The Confluence composite forwards source, account credentials, page/space/parent identifiers, write-page-id and dry-run options to `adrmachado-public/confluence-md@patches-v0.2.2`, then exposes page URL/ID, version, updated and created outputs. These are wrapper contracts; the external implementation and actual publication behavior are not retained.

## Evidence Gaps And History

This is the first retained baseline; there is no earlier snapshot comparison and no claim that these capabilities first appeared in this commit. Five generated `dist/` bundles are excluded. Older pinned internal actions, external actions, mutable Jira helper execution, consumer workflows, live permissions and successful publication remain unverified. No dependency installation, upstream build/test suite, release workflow or payment flow was executed. Only the change-check shell syntax was locally tested.

Future exact-commit changes belong in [[changelog-github-web-sdk-github-actions]] and are additive here. Do not project this repository's automation onto a particular Braintree Web package without checking that package's own workflow revision.

## Related

- Companies: [[braintree]]
- Concepts: [[braintree-sdk-release-automation]]
- History: [[changelog-github-web-sdk-github-actions]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/braintree/web-sdk-github-actions/snapshots/2026-09-29-e9c8ae9/manifest.json) - 18-file authored-source capsule
- [Snapshot README](../../../../raw/github/braintree/web-sdk-github-actions/snapshots/2026-09-29-e9c8ae9/files/README.md) - documented interfaces and retained contradictions
- [Version bump source](../../../../raw/github/braintree/web-sdk-github-actions/snapshots/2026-09-29-e9c8ae9/files/src/bump-version.ts) and [PR source](../../../../raw/github/braintree/web-sdk-github-actions/snapshots/2026-09-29-e9c8ae9/files/src/release-pr.ts)
- [Supplement manifest](../../../../raw/github/braintree/web-sdk-github-actions/supplements/2026-09-29-e9c8ae9-d8cf7fde/manifest.json) - same-SHA nine workflows and package-lock.json
- [Release pipeline](../../../../raw/github/braintree/web-sdk-github-actions/supplements/2026-09-29-e9c8ae9-d8cf7fde/files/.github/workflows/release-pipeline.yml), [dry release](../../../../raw/github/braintree/web-sdk-github-actions/supplements/2026-09-29-e9c8ae9-d8cf7fde/files/.github/workflows/release-dry-run.yml) and [change detection](../../../../raw/github/braintree/web-sdk-github-actions/supplements/2026-09-29-e9c8ae9-d8cf7fde/files/.github/workflows/check-files-changed.yml)
