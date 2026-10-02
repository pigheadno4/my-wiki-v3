---
title: "Braintree iOS Client SDK Deprecation Policy (v7 Route)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/client-sdk/deprecation-policy/ios/v7"
raw_files:
  - "braintree/docs/guides/client-sdk/deprecation-policy/ios/v7-2026-09-16.md"
tags: [braintree, ios, client-sdk, deprecation, sdk-lifecycle, semantic-versioning]
---

## Overview

This collected Braintree website policy describes client-SDK major-version changes, lifecycle categories, and an iOS platform-support rule on the documentation's iOS v7 route. It is historical policy evidence, not a current support matrix or evidence that iOS SDK v7 currently has any particular lifecycle status.

## Key takeaways

- Braintree recommends regular integration updates and updating the client SDK version at least once a year.
- Braintree says client-SDK updates follow semantic versioning. When an update requires code changes to an existing integration, Braintree increases the major version to indicate that the integration will likely need changes to work with the newest version. The listed examples are adding or dropping support for an OS or browser version and security updates or changes; the policy says Braintree tries to make such support changes without a new major version, but sufficiently large changes could be breaking.
- For the active major version of the Braintree iOS SDK, the collected policy states a minimum of the most recent iOS version and the two previous versions. This is a relative policy statement in the snapshot; the parenthetical iOS 14/13/12 values are only the page's example, not a current support claim.
- The policy defines four lifecycle categories. `Active` is the single most-current, fully supported version and receives new features. `Inactive` begins when a deprecation date is assigned and receives only security updates. `Deprecated` receives no updates; processing is stated to continue for one year after the deprecation date, with immediate-upgrade guidance to avoid disruption. `Unsupported` receives neither developer nor Braintree Support support, and processing can be suspended at any time.
- The policy points to each client SDK's README for major-version statuses and deprecation dates, recommends watching the SDK on GitHub, and says Braintree may occasionally contact merchants about upcoming changes that require an SDK update. It also qualifies the lifecycle categories by allowing unforeseen exceptions that Braintree says it will try to communicate.

## Detail locators

- Annual client-SDK update recommendation: policy note, lines 17-18.
- Semantic versioning, major-version signal, example causes and breaking-change qualification: `## Overview`, lines 23-35.
- Relative iOS platform-support rule: `### Platform support`, lines 38-42.
- `Active`, `Inactive`, `Deprecated` and `Unsupported` meanings and development states: `## Status categories`, lines 45-54.
- README status/date route, lifecycle diagram and exception qualification: `## Status categories`, lines 56-60.
- GitHub watching recommendation and possible merchant contact: `## Tips for following SDK versions`, lines 65-69.

## Evidence limitations

> [!warning] Historical policy is not current iOS support evidence
> This page was collected on 2026-09-16 and does not identify the then-current or currently active iOS SDK major version, assign a status to v7, or provide a version-specific deprecation date. Do not infer current iOS-version support, current SDK support, or current release status from the `/ios/v7` URL, the policy's relative platform rule, its illustrative OS-version example, or collection success. Consult current, separately retained README and release authority for version-specific status; do not merge those GitHub findings into this website-policy snapshot.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-ios-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/client-sdk/deprecation-policy/ios/v7-2026-09-16|Braintree iOS Client SDK Deprecation Policy (v7 route)]] - complete collected policy for semantic-version changes, iOS platform-support scope, lifecycle categories and status lookup routes
