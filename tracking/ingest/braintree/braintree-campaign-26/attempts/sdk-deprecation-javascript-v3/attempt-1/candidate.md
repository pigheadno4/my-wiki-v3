---
title: "Braintree JavaScript v3 Client SDK Deprecation Policy"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/client-sdk/deprecation-policy/javascript/v3"
raw_files:
  - "braintree/docs/guides/client-sdk/deprecation-policy/javascript/v3-2026-09-16.md"
tags: [braintree, javascript, client-sdk, deprecation, browser-support]
---

## Overview

This collected [[braintree]] website snapshot documents the JavaScript v3 client-SDK deprecation policy: semantic-versioning expectations, major-version browser policy, and the lifecycle from Active through Unsupported. It is historical policy evidence for [[braintree-web-sdk]], not proof of current SDK status, current browser support, merchant eligibility, or the behavior of any separately retained GitHub package version.

## Key takeaways

- Braintree recommends regular integration updates and updating the client SDK at least annually. This is guidance, not a stated hard requirement.
- The policy says integration-breaking changes increase the SDK major version and identifies browser/OS support changes and security changes as examples that can require a major release.
- In this snapshot, Active means the single current, fully supported major that receives features; Inactive begins when a deprecation date is assigned and receives only security updates; Deprecated receives no updates while processing is stated to continue for one year after the deprecation date; Unsupported receives neither developer nor Braintree Support support, and processing may be suspended at any time.
- The snapshot's platform section says the active JavaScript major supports the current and previous major versions of Chrome, Firefox, Safari, and Edge, and separately says it supports Internet Explorer 11. Treat those as snapshot-qualified historical statements, not current browser-support evidence.
- Braintree reserves the possibility of exceptions to the listed statuses and says it will try to communicate them. The policy directs readers to each client SDK README for major-version statuses and deprecation dates, so this page does not establish a particular JavaScript major's current status or dates.

## Detail locators

- **Overview** — semantic versioning, major-version breaking-change framing, browser/OS support changes, security changes, and the breaking-change qualification.
- **Platform support** — snapshot-qualified active-major browser rule and named desktop/mobile browser list.
- **Status categories** — Active, Inactive, Deprecated, and Unsupported definitions; feature/security-update treatment; processing timing; README status/date route; exception notice.
- **Tips for following SDK versions** — recommendation to watch the SDK GitHub repository and the possibility of direct notices about required updates.
- **See also** — migration guide, JavaScript GitHub repository, changelog, and the separate server-SDK deprecation policy.

## Related

- [[braintree-web-sdk]] — modular browser SDK concept and exact-version evidence boundaries.
- [[source-github-braintree-web]] — separately collected, versioned GitHub implementation evidence; do not infer package status or current support from this website snapshot.

## Raw Sources

- [[raw/braintree/docs/guides/client-sdk/deprecation-policy/javascript/v3-2026-09-16|Braintree JavaScript v3 client-SDK deprecation-policy snapshot]]
