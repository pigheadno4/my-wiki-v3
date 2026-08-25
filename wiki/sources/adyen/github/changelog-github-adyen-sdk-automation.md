---
title: "GitHub changelog: adyen/adyen-sdk-automation"
type: source
date_ingested: 2026-08-25
date_updated: 2026-08-25
original_format: github-repo
raw_files:
  - "github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/manifest.json"
  - "github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/manifest.json"
tags: [adyen, sdk-automation, openapi, code-generation, changelog, github-repository]
---

## Overview

Commit-qualified retained history for `adyen/adyen-sdk-automation`. Durable generation architecture and query guidance belong in [[source-github-adyen-sdk-automation]].

## Initial Baseline - `default-branch@2f180b9` (2026-08-24)

| Ref | SHA | Collection date | Ingest mode |
| --- | --- | --- | --- |
| `main` | `2f180b958babc6bbd6f0b6b73d7e4c6feefe256e` | 2026-08-25 | Full |

**Baseline established:** Gradle Kotlin DSL generation for seven Adyen API libraries; OpenAPI acquisition and preprocessing; centrally versioned services and webhooks; language-specific generator configuration; generated-code deployment; generation-impact classification; language/service matrix execution; service-specific pull requests and provenance logs; and validated Factory release-note generation.

**Head commit context:** the exact commit is a merge titled `Merge pull request #151 from Adyen/add-release-generator-droid`. The retained tree contains the release-note skill and droid, but this initial baseline does not attribute every wider generator behavior to that pull request.

**Evidence supplement:** the baseline snapshot's generic CI exclusion omitted production automation files. Exact-SHA supplement `2026-08-25-2f180b9-23c1cfdf` retains the generation classifier, matrix resolver, update workflow, and pull-request sanity workflow. Their two script test files remain excluded.

**Identity note:** this repository is tracked by default-branch commit, not semantic package version. Generated SDK versions and releases remain package-qualified in their own repositories; an automation SHA must not be presented as a Java, Node, PHP, or other SDK release.

**Future comparison rule:** compare each newly discovered `main` SHA against this retained commit. Use delta ingest for bounded and fully classified service-version, generator configuration, workflow, or release-note changes. Use additive full ingest for broad service inventory, code-generation architecture, supported-language, provenance, or trust-boundary changes. Preserve older findings in the cumulative source page.

## Evidence

- [Snapshot manifest](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/manifest.json)
- [Workflow supplement](../../../../raw/github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/manifest.json)
- [README](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/README.md)
- [Generation workflow](../../../../raw/github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/files/.github/workflows/gradle.yml)
