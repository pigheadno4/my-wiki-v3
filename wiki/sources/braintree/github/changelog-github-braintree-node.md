---
title: "GitHub changelog: braintree/braintree_node"
type: source
date_ingested: 2026-08-09
original_format: github-repo
raw_files:
  - "github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/manifest.json"
tags: [braintree, node-js-sdk, server-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_node`. Cumulative implementation knowledge belongs in [[source-github-braintree-node]] and the linked immutable snapshots.

## `braintree@3.39.0` (2026-08-06)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree` | Initial baseline | `3.39.0` | `7a9270aaf31eb87819add64a768652243f90007c` | Full |

**Important findings:** Added invalid-format and excessive-length PayPal email validation codes; added `ThreeDSecurePassThruNetwork` and pass-through `network` fields on transactions, customers, and card verifications; added `preferredPaymentMethodToken` to client-token generation.

**Developer or merchant impact:** Server integrations can pass network-specific 3DS authentication data and request client-token context for a preferred vaulted payment method. PayPal email validation failures can now be handled through explicit gateway codes.

**Migration action:** No mandatory migration is documented. Treat the fields as optional additions and confirm client-side support and merchant eligibility before exposing a related checkout experience.

**Updated source sections:** Evidence boundary; client tokens and vaulting; PayPal and Venmo; cards and 3DS; exact release findings; Braintree company and provider index.

**Evidence boundary:** This is the first retained Braintree Node baseline, so no prior exact-SHA comparison exists. The upstream release-note record has no body; patch findings come from the retained repository changelog. Broader checkout and server behavior in the source page is cumulative `3.39.0` implementation knowledge, not a list of changes introduced by this release.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_node/releases/braintree/3.39.0/2026-08-09/manifest.json`
- Empty release-notes record: `raw/github/braintree/braintree_node/releases/braintree/3.39.0/2026-08-09/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/manifest.json`
- Repository changelog: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/CHANGELOG.md`
- Client-token implementation: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/client_token_gateway.js`
- 3DS network enum: `raw/github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/files/lib/braintree/three_d_secure_pass_thru_network.js`
