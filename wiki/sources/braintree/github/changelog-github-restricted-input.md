---
title: "GitHub changelog: braintree/restricted-input"
type: source
date_ingested: 2026-08-30
original_format: github-repo
raw_files:
  - "github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/manifest.json"
  - "github/braintree/restricted-input/snapshots/2026-08-30-79053ef/manifest.json"
tags: [braintree, restricted-input, input-formatting, changelog, github-repository]
---

## Overview

Commit-qualified history for `braintree/restricted-input`. Durable implementation knowledge belongs in [[source-github-restricted-input]]; this page separates the exact retained transition from package-version statements found inside the repository.

## `default-branch@8dcc6ea` (2026-03-04)

| Ref | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `main` | `79053ef3a0843d2c68a167a4830159bb787f6fb1` (`package.json` 4.1.3) | `default-branch@8dcc6ea` (`package.json` 4.2.0) | `8dcc6ea9e6cea44eef2b02fbc3f7569a602fa089` | Full |

**Retained transition:** Thirteen selected files change. Source changes modernize TypeScript imports, lint annotations, formatting, and compiler settings without changing the retained public constructor or the `getUnformattedValue()`, `setPattern()`, and static `supportsFormatting()` APIs.

**Dependency and tooling impact:** The runtime browser-detection dependency moves from `^1.17.2` to `^2.1.1`. Development moves from WebdriverIO to Playwright integration tests, updates Node and TypeScript-era tooling, and includes tests in the TypeScript project configuration.

**Behavior assessment:** The repository changelog documents no intentional formatter behavior change for `4.2.0`. Browser classification remains a delegated evidence gap because the dependency implementation is not retained, and excluded tests do not prove cross-browser parity.

**Migration action:** No application migration is documented. Consumers should retest platform detection, Samsung fallback behavior, input-method handling, paste, autofill, and caret preservation before upgrading across the browser-detection major boundary.

**Identity boundary:** This is a commit comparison, not a package release record. The ending source says `4.2.0`, but the Git tag history is not reliable enough to use as the repository's version authority.

**Updated source sections:** Evidence and identity boundary; event and selection handling; platform strategies; `4.1.3` to `4.2.0` transition; historical behavior.

**Evidence:**

- Current snapshot: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/manifest.json`
- Prior snapshot: `raw/github/braintree/restricted-input/snapshots/2026-08-30-79053ef/manifest.json`
- Comparison: `tracking/github/repos/braintree/restricted-input/comparisons/default-branch/79053ef--8dcc6ea/comparison.json`
- Patch: `tracking/github/repos/braintree/restricted-input/comparisons/default-branch/79053ef--8dcc6ea/diff.patch`
- Current changelog: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/CHANGELOG.md`
- Current package metadata: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/package.json`

## Retained Package-History Statements

- `4.1.4` records workflow fixes only.
- `4.1.3` through `4.1.0` record workflow, script, formatting-tool, and dependency maintenance.
- `4.0.3` fixes iOS Safari focus-time pattern changes and restores a removed public formatting-support method.
- `4.0.1` fixes Samsung-browser date input; `3.0.5` and `3.0.4` address macOS Safari keyboard-layout and input-source behavior.
- `3.0.3` fixes duplicate Android Chrome paste input, `3.0.2` improves server-side rendering safety, and `3.0.0` adds TypeScript types with a private-method break.
- `2.1.0` adds the paste callback. The v2 and v1 history records preset-value formatting, browser detection, autofill, keyboard, paste, selection, WebView, and legacy-browser fixes.

These are statements from the changelog retained at `8dcc6ea`; only the `79053ef` to `8dcc6ea` boundary has a byte-level comparison in this wiki.

## Related

- [[source-github-restricted-input]] - cumulative implementation knowledge and evidence boundaries
- [[payment-input-formatting]] - generic formatting model
- [[braintree]] - company and repository catalog
