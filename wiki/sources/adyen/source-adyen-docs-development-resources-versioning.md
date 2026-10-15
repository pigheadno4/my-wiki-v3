---
title: "Adyen API and Server-side Library Versioning"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/versioning"
raw_files:
  - "adyen/docs/development-resources/versioning/2026-09-15.md"
tags: [adyen, api-versioning, server-side-libraries, compatibility, deprecation]
---

## Overview

Adyen's versioning guide explains how API versions and server-side API library versions are identified and changed. This is a 2026-09-15 documentation snapshot with page metadata last modified 2022-01-18. It describes versioning policy, not current endpoint availability or a particular library release.

## Key takeaways

- Each Adyen API has its own version. For direct server calls, the API URL contains a `v` or `V` plus an integer; for server-side libraries, release notes identify included API versions. A library's package version is separate from the API versions it wraps. Check the API Explorer and relevant release notes when selecting a version.
- Adyen says breaking or incompatible API changes receive a new API version, while backward-compatible changes are implemented in all versions. The compatibility classification depends on API type: Payment, Recurring, Payout and BinLookup are listed as classic; the guide calls other APIs new. Adding a response-body field is non-breaking for a new API but breaking for a classic API. Use the two change tables for other cases rather than applying one rule to every API.
- The non-breaking table classifies **documentation deprecation** of a request or response field as non-breaking for both types. That classification does not say the field was removed: the breaking table separately lists field removal as breaking. The guide also says an API version can be introduced without visible consumer changes, and version numbers can be skipped.
- The guide recommends upgrading and checking release notes, but says existing API versions can continue to be used until an integration is ready to upgrade. This dated statement is a policy description, not proof that a specific old version remains available now.
- Server-side API libraries use MAJOR.MINOR.PATCH semantic versioning: major for breaking changes to older endpoint usage such as declarations or parameters, minor for new non-breaking features, and patch for bug fixes. The guide recommends checking the library's GitHub releases when upgrading; it does not establish the behavior or support status of any specific release.

## Detail locators

- `### Checking the API version` — URL suffix, per-API versions, library release notes, and API Explorer lookup.
- `### New vs classic APIs`, `### Non-breaking changes`, `### Breaking changes` — API categories and the full change-classification tables.
- `### New API version without changes`, `### Upgrading to a new API version` — version-number gaps, upgrade recommendation, and release-note route.
- `## Server-side libraries` through `### Upgrading to a new version of a server-side library` — package version versus API version and semantic version meanings.

## Related

- Company: [[adyen]]
- SDK generation and release provenance: [[adyen-sdk-automation]]
- Version-qualified library baselines: [[adyen-node-api-library]], [[adyen-php-api-library]]
- Server-side library directory: [[source-adyen-docs-development-resources-libraries]]

## Raw Sources

- [[raw/adyen/docs/development-resources/versioning/2026-09-15|2026-09-15 Adyen versioning snapshot]]
