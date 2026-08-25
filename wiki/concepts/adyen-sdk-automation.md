---
title: "Adyen SDK Automation"
type: concept
category: technology
tags: [adyen, sdk-automation, openapi, code-generation, release-engineering]
---

## Adyen SDK Automation

Adyen SDK Automation is the generation and release-support factory behind Adyen's Java, Python, .NET, Go, Node.js, PHP, and Ruby API libraries. It clones Adyen OpenAPI specifications, applies generator-oriented transformations, runs language-specific OpenAPI Generator configurations, and deploys generated services and models into independently versioned SDK repositories.

It is not a merchant checkout SDK. It explains where generated API clients, models, service versions, and some release artifacts come from; runtime behavior and supported public interfaces must still be verified in the exact downstream SDK release.

## Current baseline

The retained baseline is `default-branch@2f180b9` at exact SHA `2f180b958babc6bbd6f0b6b73d7e4c6feefe256e`, collected on 2026-08-25. This is commit-qualified repository evidence rather than a package release.

The central service registry includes Checkout v72, classic Payment, Payout, and Recurring v68, Terminal API v1 for Java and Node, Management v3, platform APIs, and multiple webhook specifications. These entries establish generator inputs at this commit; they do not prove merchant eligibility, production availability, or that every generated language library exposes identical behavior.

## Generation lifecycle

The root build clones `Adyen/adyen-openapi`, rewrites specifications to OpenAPI `3.0.0`, and maps `x-methodName` to `operationId`. Shared Gradle conventions register one generation task per applicable service, rename the generic tag used by small services, and inject `x-webhook-root` for webhook model generation.

Each language project supplies its own generator version, templates, output mapping, and compatibility choices. The retained versions range from OpenAPI Generator `6.0.1` for PHP and `6.5.0` for Go to `7.11.0`-`7.16.0` for Java, Node, Python, Ruby, and .NET. Generator-version differences are therefore part of the evidence when comparing generated SDK shape.

## Continuous generation and provenance

The retained GitHub workflow runs on `main` pushes or manual dispatch. It resolves a language-and-service matrix, skips changes classified as documentation or test-only, clones the selected downstream SDK, generates and formats one service, and opens a service-specific pull request only when files changed.

For each changed service it writes a generation log containing the OpenAPI commit SHA, automation commit SHA, target library SHA, project, service, and generation time. This supports provenance analysis across repositories, but the generated SDK repository remains the owner of its release history.

## Release-note tooling

The repository also contains a Factory skill and droid for evidence-backed release notes across all seven languages. The caller supplies a language and optional version range; the droid clones the canonical downstream repository, inventories changes, writes `RELEASE_NOTES.md` and a validation report, and reports success only after validation passes.

These instructions describe a release-analysis workflow, not retained release notes for every downstream SDK. A version-specific query must search the corresponding SDK source and changelog page, then collect a focused supplement or clone the upstream repository when the required code is outside the retained capsule.

## Query boundary

- Use this page for generator ownership, supported generation targets, service-version inputs, language-specific generator configuration, CI orchestration, and release-note workflow.
- Use [[adyen-node-api-library]] or [[adyen-php-api-library]] for retained server-SDK runtime behavior.
- Use the corresponding downstream repository history for a language/version comparison; do not treat an automation commit as a downstream package release.
- Use official product documentation and merchant configuration evidence for eligibility and current API guidance.

## Related

- [[source-github-adyen-sdk-automation]] - cumulative exact-commit source evidence
- [[changelog-github-adyen-sdk-automation]] - commit-qualified automation history
- [[adyen-node-api-library]] - retained Node.js API Library behavior
- [[adyen-php-api-library]] - retained PHP API Library behavior
- [[adyen]] - company and knowledge-status page
