---
title: "GitHub changelog: braintree/braintree_php"
type: source
date_ingested: 2026-08-19
original_format: github-repo
raw_files:
  - "github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json"
tags: [braintree, php-sdk, server-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_php`. Cumulative implementation knowledge belongs in [[source-github-braintree-php]] and the linked immutable snapshots.

## `braintree_php@6.37.0` (2026-08-05)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree_php` | Initial baseline | `6.37.0` | `0f53ece38397c9fed05b94620634a5a23ef8ee48` | Full |

**Important findings:** Fixed path traversal in Address and Dispute gateway paths by rejecting path separators and relative segments; added PayPal account email validation codes `92963` and `92964`; added `preferredPaymentMethodToken` to client-token generation.

**Developer or merchant impact:** Applications receive explicit codes for malformed or excessively long PayPal email addresses. Server integrations can generate client-token context for a preferred vaulted payment method. The path validation is a security hardening change for applications that pass external IDs into affected gateway methods.

**Migration action:** No mandatory migration is documented. Upgrade to an active release for security coverage, avoid transforming rejected IDs to bypass validation, and treat the new client-token field as optional until the corresponding client experience is confirmed.

**Updated source sections:** Evidence boundary; client tokens, nonces, and vaulting; webhooks, errors, and security; exact release findings; Braintree company and provider index.

**Evidence boundary:** This is the first retained Braintree PHP baseline, so no prior exact-SHA comparison exists. The upstream release-note record has no body; patch findings come from the retained repository changelog. Broader server behavior in the source page is cumulative `6.37.0` implementation knowledge, not a list of changes introduced by this release.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_php/releases/braintree_php/6.37.0/2026-08-19/manifest.json`
- Empty release-notes record: `raw/github/braintree/braintree_php/releases/braintree_php/6.37.0/2026-08-19/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json`
- Repository changelog: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/CHANGELOG.md`
- Client-token implementation: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/ClientTokenGateway.php`
- Address path validation: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/AddressGateway.php`
- Dispute path validation: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/DisputeGateway.php`
- Validation codes: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/Error/Codes.php`
