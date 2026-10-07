---
title: "Braintree Deprecated Client-Side Encryption for Windows Phone"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/windows-phone"
raw_files:
  - "braintree/docs/deprecated/client-side-encryption/windows-phone-2026-09-16.md"
tags: [braintree, windows-phone, client-side-encryption, deprecated]
---

## Overview

This 2026-09-16 Braintree website snapshot documents a deprecated Windows Phone client-side-encryption library. It provides a short class-library installation path, GitHub source and example navigation, and a .NET quick-start example that constructs `Braintree` with a placeholder client-side-encryption key and encrypts card-number, CVV, and expiration-date strings separately. This is historical client-library evidence, not evidence of current SDK, Windows Phone, or GitHub-repository support.

## Key takeaways

- The page explicitly marks the integration method deprecated and links to Braintree SDK upgrade guidance; it should not be treated as a current integration recommendation.
- The documented class-library path says to clone the linked source, import the Braintree Windows Phone class library into the solution, add it as a project dependency, and reference it. The page does not name a library release, package version, Windows Phone version, .NET runtime, or build prerequisite.
- The quick-start snippet instantiates `Braintree` with the placeholder string `your-client-side-encryption-key`, then calls `Encrypt` separately for literal card-number, CVV, and expiration-date strings. It does not show a merchant-server handoff, a gateway request, error handling, or any payment operation.

## Material limitations

- The GitHub repository, archive, issue-tracker, and examples URLs are unread navigation targets. Their appearance in this Braintree website snapshot does not establish current repository ownership, availability, branch contents, release status, compatibility, or maintenance.
- The code is an example, not proof of secure production handling, PCI scope or compliance, successful encryption, tokenization, authorization, Vault storage, transaction processing, settlement, or any other payment outcome.

## Detail locators

- Deprecation notice and linked SDK-upgrade route: raw lines 17-18.
- Installation orientation and Windows Phone class-library steps: `## Installation`, raw lines 21-29.
- GitHub source archive navigation: `### Source code`, raw lines 32-34.
- Separate GitHub integration-example navigation: `## Integration examples`, raw lines 35-37.
- Support and GitHub issue-tracker navigation: `## Bugs`, raw lines 38-40.
- .NET quick-start example and placeholder client-side-encryption key: `## Quick start example`, raw lines 41-48.

## Related

- [[braintree]]
- [[braintree-payment-platform]] - provider-level route for Braintree product and integration evidence
- [[source-braintree-upgrade]] - upgrade route linked by this deprecated page; consult that separately retained source for its contents

## Raw Sources

- [[raw/braintree/docs/deprecated/client-side-encryption/windows-phone-2026-09-16|Braintree deprecated client-side encryption for Windows Phone (2026-09-16 snapshot)]]
