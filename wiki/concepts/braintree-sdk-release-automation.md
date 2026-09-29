---
title: "Braintree SDK Release Automation"
type: concept
category: technology
tags: [braintree, developer-tooling, github-actions, release-engineering]
---

## Overview

`braintree/web-sdk-github-actions` provides reusable engineering workflows and composite actions for CI, release preparation, npm publication, GitHub release notes, PR validation, repository cleanup and Confluence documentation. It is not a payment SDK and does not establish merchant eligibility or checkout behavior. The first retained baseline is `default-branch@e9c8ae9`, collected on 2026-09-29. [[source-github-web-sdk-github-actions]]

## Release Boundaries

The retained TypeScript prepares a version/changelog commit, pushes a release branch and optionally opens a PR. It does not merge or tag that PR. The retained release-pipeline workflow contains CI and a version-bump action call; publication is a separate workflow. Prerelease level and feature-tag controls belong to the composite action, not every wrapper workflow. [[source-github-web-sdk-github-actions]]

> [!warning] Contradiction
> README claims of a complete merge/tag/publish pipeline and side-effect-free dry run exceed the retained implementation. The standalone dry-release workflow does not transfer bumped package files to its publish job, and its description includes release notes although no such job is present. The change-detection workflow also contains an unmatched shell `fi`, confirmed by syntax-only checking. Do not copy these workflows as a verified release recipe.

## Evidence And Query Use

The capsule retains authored source and workflow configuration, not generated `dist/` bundles. Several internal action calls pin an older SHA, while the Jira workflow checks out mutable `main`. Those delegated implementations were not verified by this baseline. Query exact source and [[changelog-github-web-sdk-github-actions]] together; an automation commit is not a downstream SDK release.

## Related

- [[source-github-web-sdk-github-actions]] - exact-SHA contracts, side effects and limitations
- [[changelog-github-web-sdk-github-actions]] - commit-qualified history
- [[braintree]] - company catalog
