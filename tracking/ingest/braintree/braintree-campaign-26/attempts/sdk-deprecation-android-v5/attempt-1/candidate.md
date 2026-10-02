---
title: "Braintree Android Client SDK Deprecation Policy (v5)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/client-sdk/deprecation-policy/android/v5"
raw_files:
  - "braintree/docs/guides/client-sdk/deprecation-policy/android/v5-2026-09-16.md"
tags: [braintree, android, client-sdk, deprecation, sdk-lifecycle, semantic-versioning]
---

## Overview

This historical Braintree website-policy snapshot explains semantic-versioning, release-time platform-support, and version-monitoring expectations for the Android client SDK. It is a policy and navigation source, not evidence of the SDK's current supported Android versions, current major-version status, feature parity, or deprecation dates.

## Key takeaways

- Braintree recommends regular integration updates and updating the client SDK version at least once a year.
- The page says Braintree follows semantic versioning for client SDK updates. When an update requires code changes to existing integrations, Braintree increases the major version to signal that an integration will likely need changes to work with the newest version. Adding or dropping support for a mobile OS or browser version, and security changes, are given as examples; the page qualifies that Braintree tries to add such support without a new major version, but sufficiently large changes could still be breaking.
- Platform-support decisions are based on regular review of widely used browsers and OS versions. The active Android SDK major version is described as supporting the most widely used Android versions at the time of its release. The API level 21+ statement is presented only as the page's example and must not be treated as a current support floor.
- SDK major-version statuses can change over time. The page identifies each client SDK's README as the place containing status and deprecation dates and says those statuses are updated as new major versions are released. It also warns that unforeseen circumstances may require exceptions. This retained webpage does not contain the status-category definitions or a current version-status table.
- Braintree recommends watching the SDK on GitHub for version news and says it may occasionally contact merchants about upcoming changes that require an update. GitHub repository and changelog evidence remains a separate ingest authority.

## Detail locators

- Regular-update and annual client-SDK guidance: policy note, lines 17-18.
- Semantic versioning, major-version signal, examples, and breaking-change qualification: `## Overview`, lines 21-33.
- Release-time platform-support policy and the API level 21+ example: `### Platform support`, lines 36-40.
- Status-change diagram, per-SDK README lookup, and exception qualification: `## Status categories`, lines 43-56.
- GitHub watching, possible merchant contact, migration, reference, repository, changelog, and server-policy routes: `## Tips for following SDK versions` and `### See Also`, lines 59-73.

## Evidence limitations

> [!warning] Historical policy is not a current support matrix
> The page was collected on 2026-09-16, while its embedded metadata reports an update time of 2025-04-02. Its support statement is conditioned on the Android versions widely used at the time an active major version was released, and API level 21+ is introduced as an example. Do not infer current Android support, current SDK status, version parity, a deprecation deadline, or runtime availability from this snapshot. The captured body names status categories and links a diagram but does not include the category definitions; version-specific README and GitHub evidence must be retained separately.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/client-sdk/deprecation-policy/android/v5-2026-09-16|Braintree Android Client SDK Deprecation Policy (v5)]] - complete collected website-policy snapshot for semantic versioning, release-time platform support, status lookup and monitoring routes
