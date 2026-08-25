---
title: "GitHub: adyen/adyen-sdk-automation"
type: source
date_ingested: 2026-08-25
date_updated: 2026-08-25
original_format: github-repo
raw_files:
  - "github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/manifest.json"
  - "github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/manifest.json"
tags: [adyen, sdk-automation, openapi, code-generation, release-engineering, github-repository]
---

## Overview

`adyen/adyen-sdk-automation` is Adyen's Gradle Kotlin DSL factory for generating code into `Adyen/adyen-*-api-library` repositories. This initial full ingest records `default-branch@2f180b9`, exact SHA `2f180b958babc6bbd6f0b6b73d7e4c6feefe256e`, committed on 2026-08-24 and collected on 2026-08-25.

Repository: <https://github.com/Adyen/adyen-sdk-automation>

## Evidence Boundary

- Findings are commit-qualified. This repository does not establish a package version for any generated SDK.
- The retained evidence contains 38 configured source files plus a four-file exact-SHA workflow supplement. Tests, fixtures, two CI script tests, and the Gradle wrapper binary are excluded.
- This repository owns generation configuration and release-support automation. Java, Python, .NET, Go, Node.js, PHP, and Ruby SDKs retain independent release and behavior histories.
- A service in the generator registry proves a configured generation input at this commit, not merchant eligibility, API enablement, production availability, or complete behavior parity among languages.
- The repository clones `Adyen/adyen-openapi` at execution time. The exact schema commit used by a particular generated SDK change belongs in that generation's provenance log or downstream pull request, not this static snapshot.

## Grounding Excerpts

> "This is a set of Gradle build scripts to generate code for `Adyen/adyen-*-api-library` repositories."
>
> `raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/README.md:5`

> "Shared logic goes into `buildSrc`. Subprojects can extend and customize predefined tasks via the type-safe `SdkAutomationExtension` or reconfiguration (`tasks.named`)."
>
> `raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/README.md:56`

> "Release notes are produced only when validation passes; on failure, the validation report records the blocking reasons."
>
> `raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/README.md:111`

> "The commit history of this PR reflects the `adyen-openapi` commits that have been applied."
>
> `raw/github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/files/.github/workflows/gradle.yml:183`

## Repository Architecture

The root build acquires specifications and shared Gradle conventions define generation behavior. Seven language subprojects provide target-specific generator versions, configuration, templates, naming, and copy/deployment tasks:

| Project | OpenAPI Generator | Notable retained configuration |
| --- | --- | --- |
| Java | `7.11.0` | Jersey 3, Jakarta imports, Terminal-specific generation |
| Python | `7.13.0` | Python client model and service deployment |
| .NET | `7.16.0` | `net8.0`, `generichost`, nullable references |
| Go | `6.5.0` | Go model and service deployment |
| Node | `7.13.0` | TypeScript models/services; restricted webhook and Terminal outputs |
| PHP | `6.0.1` | PHP models/services and small-service handling |
| Ruby | `7.13.0` | Custom `AdyenRubyCodegen` and single-quote escaping lambda |

The repository does not contain the complete generated SDKs. Each language task clones its target `Adyen/adyen-<language>-api-library` repository and writes generated output into that checkout.

## Specification Preparation

The `specs` task shallow-clones `Adyen/adyen-openapi` and processes top-level JSON specifications. `SpecProcessor` forces the `openapi` field to `3.0.0` and copies `x-methodName` into `operationId`; webhook and notification specifications without paths skip the operation transformation.

Shared conventions distinguish multi-tag services from small services that use one generic `General` tag. Small-service preparation renames that tag to the API name. Webhook preparation adds `x-webhook-root` once to the payload model so generated handlers can deserialize webhook roots. A separate task can derive a Checkout payment-method class and transaction-variant table from the schema.

## Configured API Inventory

At this commit, the central service list includes:

- Checkout v72; Payout, Recurring, and classic Payment v68; BIN Lookup v54;
- POS Mobile v68, Payments App v1, Disputes v30, Stored Value v46, and Document Collector v1;
- Terminal API v1, limited by configuration to Java and Node;
- Management v3 and Balance Control v1;
- Legal Entity Management v4, Balance Platform v2, Transfers v4, Data Protection v1, Session Authentication v1, and Capital v1;
- configuration, ACS, report, transfer, transaction, management, dispute, negative-balance-warning, balance, tokenization, and relayed-authorization webhook specifications.

This inventory is useful for tracing generated model origins. Detailed non-checkout API questions still require the exact downstream SDK source or a focused clone because generator configuration alone does not retain generated models or runtime transport.

## Generation Workflow

The supplemented `Update SDKs` GitHub workflow runs on pushes to `main` and supports manual project/service selection. Its classifier skips documentation, test-only source, and test-dependency-only changes; a missing base commit, generator source/configuration change, or ambiguous change regenerates as the safe fallback.

The workflow expands the selected languages and services into a non-fail-fast matrix. Each matrix job:

1. checks out this repository and the target API library;
2. copies the target project's generator version into shared build configuration;
3. runs the service task only if that service applies to the language;
4. invokes the downstream repository's formatting action when present;
5. checks whether generated files changed;
6. records OpenAPI, automation, and prior library SHAs in `sdk-generation-log/<service>.json`; and
7. creates a service-specific pull request with an OpenAPI-qualified commit message.

The workflow uses concurrency cancellation per ref and pinned action commits. The retained pull-request sanity workflow only verifies that Gradle can configure all tasks; it does not prove generated output correctness or downstream SDK tests.

## Release-Note Factory

The repository contains a Factory skill and droid that accept one of seven language names plus optional baseline and target refs. The canonical source is always `Adyen/adyen-<language>-api-library`; arbitrary repository URLs and local checkout paths are rejected.

The skill controls argument validation, output paths, overwrite authorization, delegation, and final artifact checks. The droid temporarily clones the full downstream repository, resolves refs, inventories public API and dependency changes, associates pull requests and contributors, composes release notes, and writes both `RELEASE_NOTES.md` and `RELEASE_NOTES_VALIDATION.md`.

A reported success requires validation to pass and both output files to satisfy the contract. Failure must remain failure rather than being repaired or inferred by the caller. The retained instructions include a hardcoded Java regression fixture for `v38.3.0..v39.0.0`; that fixture is validation scaffolding, not the current Java SDK release range.

## Version and Query Guidance

Use [[changelog-github-adyen-sdk-automation]] to determine which automation commit is retained. For a question such as why a field differs between Node and PHP, first inspect this page for generator/spec-processing differences, then inspect the package-qualified source and changelog for each downstream SDK. The automation baseline cannot replace those language-specific sources.

Future default-branch updates should compare exact commits. A bounded generator, service-version, workflow, or release-note change can use delta ingest. A broad service-registry, generation architecture, language-target, or provenance change should use additive full ingest while preserving this baseline.

## Related

- Company: [[adyen]]
- Concept: [[adyen-sdk-automation]]
- Downstream examples: [[adyen-node-api-library]], [[adyen-php-api-library]]
- History: [[changelog-github-adyen-sdk-automation]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/manifest.json) - exact-SHA capsule inventory and hashes
- [Workflow supplement](../../../../raw/github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/manifest.json) - exact-SHA production scripts and workflows
- [README](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/README.md) - generation commands and release-note workflow
- [Shared conventions](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/buildSrc/src/main/kotlin/adyen.sdk-automation-conventions.gradle.kts) - services, transformations, tasks, and deployment
- [Specification processor](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/buildSrc/src/main/kotlin/com/adyen/sdk/SpecProcessor.kt) - OpenAPI and operation transformation
- [Generation workflow](../../../../raw/github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/files/.github/workflows/gradle.yml) - trigger, matrix, provenance log, and pull-request lifecycle
- [Generation classifier](../../../../raw/github/adyen/adyen-sdk-automation/supplements/2026-08-25-2f180b9-23c1cfdf/files/.github/scripts/should_generate.py) - regeneration decision rules
- [Release-note skill](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/.factory/skills/release-notes-generation/SKILL.md) - validation and delegation contract
- [Release-note droid](../../../../raw/github/adyen/adyen-sdk-automation/snapshots/2026-08-25-2f180b9/files/.factory/droids/release-notes-generation-droid.md) - repository analysis and artifact contract
