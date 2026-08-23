---
title: "GitHub changelog: braintree/braintree_ruby"
type: source
date_ingested: 2026-08-23
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/manifest.json"
tags: [braintree, ruby-sdk, server-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_ruby`. Cumulative implementation knowledge belongs in [[source-github-braintree-ruby]] and the linked immutable snapshots.

## `braintree@4.40.0` (2026-08-05)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree` | Initial baseline | `4.40.0` | `1217992763cc13f33dbd8b6c51ad2ae058ddd2a8` | Full |

**Important findings:** Added PayPal account email validation codes `92963` and `92964`; added `network` to 3DS pass-through data across transactions, cards, customers, payment methods, and card verifications with Eftpos, Mastercard, and Visa constants; fixed path traversal in Address and Dispute gateway request IDs.

**Developer or merchant impact:** Applications can handle malformed PayPal email data with explicit codes and transport network-qualified 3DS evidence. The ID allowlist is a security hardening change for applications that pass external identifiers into affected gateway methods.

**Migration action:** No mandatory migration is documented. Upgrade to active 4.x for security coverage, do not transform rejected IDs to bypass validation, and confirm client-side 3DS support and merchant eligibility before exposing related checkout behavior.

**Updated source sections:** Shared server concept; evidence boundary; cards and 3DS; webhooks, errors, and security; exact release findings; Braintree company and provider index.

**Evidence boundary:** This is the first retained Braintree Ruby baseline, so no prior exact-SHA comparison exists. The upstream release-note record has no body; patch findings come from the retained repository changelog. Broader server behavior in the source page is cumulative `4.40.0` implementation knowledge, not a list of changes introduced by this release.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_ruby/releases/braintree/4.40.0/2026-08-23/manifest.json`
- Empty release-notes record: `raw/github/braintree/braintree_ruby/releases/braintree/4.40.0/2026-08-23/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/manifest.json`
- Repository changelog: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/CHANGELOG.md`
- Address path validation: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/address_gateway.rb`
- Dispute path validation: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/dispute_gateway.rb`
- 3DS network constants: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/three_d_secure_pass_thru.rb`
- Validation codes: `raw/github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/files/lib/braintree/error_codes.rb`
