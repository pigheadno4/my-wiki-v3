---
title: "Braintree Server SDK Deprecation Policy"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/server-sdk-deprecation-policy"
raw_files:
  - "braintree/docs/reference/general/server-sdk-deprecation-policy-2026-09-16.md"
tags: [braintree, server-sdk, deprecation, sdk-lifecycle, semantic-versioning]
---

## Overview

This collected Braintree policy explains how server SDK major versions move through lifecycle categories and how semantic-version changes signal integration work. It provides maintenance and monitoring guidance, but it does not establish the current status of any particular language or SDK version.

## Key takeaways

- Braintree recommends regular integration updates and updating the server SDK version at least every two years.
- Braintree says its server SDK updates follow semantic versioning. When an update requires code changes to an existing integration, Braintree increases the SDK's major version to signal that the integration will likely need changes to work with the newest version. Examples and the qualification that some support changes may still become breaking changes are under `## Overview`.
- The policy defines four lifecycle categories. `Active` is the single most-current, fully supported version and receives new features. `Inactive` begins when a deprecation date is assigned and receives security updates but no new features. `Deprecated` versions receive no updates; processing is stated to continue for one year after the deprecation date, with immediate upgrade guidance to avoid disruption. `Unsupported` versions receive neither developer nor Braintree Support support, and processing can be suspended at any time.
- The README for each server SDK is identified as the location for major-version status and deprecation dates, with those entries updated as new major versions are released. Braintree also recommends watching the applicable SDK repository for version updates and says it may contact merchants about changes that require an SDK update.

## Detail locators

- Regular-update and two-year server-SDK guidance: policy note, lines 17-18.
- Semantic versioning, major-version signal and example causes of major updates: `## Overview`, lines 21-34.
- `Active`, `Inactive`, `Deprecated` and `Unsupported` definitions and development states: `## Status categories`, lines 37-44.
- Per-SDK README location for statuses and deprecation dates, plus exception qualification: `## Status categories`, lines 46-52.
- Repository watching and possible merchant contact: `## Tips for following SDK versions`, lines 55-59.

## Evidence limitations

> [!warning] Lifecycle policy is not a current support matrix
> This page was collected on 2026-09-16 and defines lifecycle categories without listing the current category of any specific SDK major version. Do not infer current support, a current recommended version, or a deprecation deadline from collection success or retained package versions. Check the applicable SDK's current README and release authority for version-specific status and dates. The policy also says unforeseen circumstances may require exceptions to the stated categories.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/server-sdk-deprecation-policy-2026-09-16|Braintree Server SDK Deprecation Policy]] - complete collected policy covering lifecycle categories, version-update guidance and current-status lookup routes
