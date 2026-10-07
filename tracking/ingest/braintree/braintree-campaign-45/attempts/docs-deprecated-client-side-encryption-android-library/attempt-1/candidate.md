---
title: "Braintree Deprecated Client-Side Encryption Android Library"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/android-library"
raw_files:
  - "braintree/docs/deprecated/client-side-encryption/android-library-2026-09-16.md"
tags: [braintree, android, deprecated, client-side-encryption]
---

## Overview

This 2026-09-16 Braintree website snapshot documents the deprecated Android client-side encryption library. It lists a versioned jar and an Android library-project installation path, then provides source, example, issue-tracker, and quick-start routes. This is historical website documentation, not evidence of current Android SDK or GitHub support.

## Key takeaways

- Braintree explicitly marks the integration method deprecated and directs readers to its SDK upgrade guidance.
- The page offers an `encryption-2.0.0.jar` download and an Android library-project route for SDK r6 or higher; the latter assumes Eclipse and describes importing and attaching the Braintree Android library project.
- The quick-start example constructs `com.braintreegateway.encryption.Braintree` with a placeholder client-side-encryption key and separately encrypts a card number, CVV, and expiration date. It is an example only: the page does not document merchant-server handoff, gateway processing, or any payment outcome.

## Detail locators

- Deprecation notice and SDK-upgrade route: raw lines 17-18.
- Installation choices: `## Installation`, raw lines 21-23.
- Versioned jar download and displayed SHA1: `### Jar file`, raw lines 24-26.
- SDK r6-or-higher Android library-project route, Eclipse assumption, and project-linking steps: `### Android library project (SDK r6 or higher)`, raw lines 27-37.
- Source-code archives: `### Source code`, raw lines 40-42.
- Integration-example archives: `## Integration examples`, raw lines 43-45.
- Support and GitHub issue routes: `## Bugs`, raw lines 46-48.
- Example key initialization and field-by-field encryption: `## Quick start example`, raw lines 49-54.

## Related

- [[braintree]]
- [[braintree-android-sdk]] - current modular Android SDK concept with separately versioned website and GitHub evidence boundaries
- [[source-braintree-upgrade]] - upgrade route linked by this deprecated page

## Raw Sources

- [[raw/braintree/docs/deprecated/client-side-encryption/android-library-2026-09-16|Braintree deprecated client-side encryption Android library (2026-09-16 snapshot)]]
