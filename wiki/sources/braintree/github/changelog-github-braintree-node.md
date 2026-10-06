---
title: "GitHub changelog: braintree/braintree_node"
type: source
date_ingested: 2026-10-06
original_format: github-repo
raw_files:
  - "github/braintree/braintree_node/snapshots/2026-10-06-deb5227/manifest.json"
  - "github/braintree/braintree_node/snapshots/2026-08-09-7a9270a/manifest.json"
tags: [braintree, node-js-sdk, server-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_node`. Cumulative implementation knowledge belongs in [[source-github-braintree-node]] and the linked immutable snapshots.

## `braintree@3.40.0` (2026-09-23)

| Repository / Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree/braintree_node` / `braintree` | `3.39.0` | `3.40.0` | `deb5227f1c4824b1f622115caf2ba4302134d375` | Full additive, focused reading |

**Important findings:** Broad path-traversal hardening with the shared `^[A-Za-z0-9_-]+$` ID/token allowlist; new `achType` transaction search with same-day/standard enum values; announced refund `surchargeAmount` support. Source additionally guards TestingGateway operations and confirms unchanged Address/Dispute callers inherit stricter validation.

**Developer or merchant impact:** Affected path-based calls reject invalid identifiers locally with `NotFoundError` before contacting the gateway. Audit custom IDs and error handling; do not sanitize identifiers into different identities. ACH search is not ACH enablement or a settlement guarantee.

**Migration action:** Review affected identifier inputs and optional search/refund use. Node/npm requirements and dependencies are unchanged. The refund options forwarding path already exists at `3.39.0`; the announcement does not establish new forwarding code or live acceptance of the field.

**Updated source sections:** New full additive `3.40.0` section; path security, ACH search, refund announcement/implementation boundary and preserved runtime knowledge; Server SDK concept, company, provider index and logs. All older source and ledger findings remain.

**Evidence boundary:** 20 changed retained files and 150 unchanged; 21 upstream paths excluded by capsule policy. Focused reading fully covers changed implementation and affected prior code/dependencies; snapshot inventories and unchanged cumulative history checked mechanically. Empty upstream release-note body; repository changelog and exact source are authoritative here. No upstream tests or live payments executed. Node and Ruby package identities must remain repository-qualified.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_node/releases/braintree/3.40.0/2026-10-06/manifest.json`
- Empty release notes: `raw/github/braintree/braintree_node/releases/braintree/3.40.0/2026-10-06/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/manifest.json`
- Comparison: `tracking/github/repos/braintree/braintree_node/comparisons/braintree/3.39.0--3.40.0/comparison.md`
- Comparison manifest: `tracking/github/repos/braintree/braintree_node/comparisons/braintree/3.39.0--3.40.0/comparison.json`
- Changelog: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/CHANGELOG.md`
- Path helper: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/util.js`
- ACH search: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/transaction_search.js`
- Refund and transaction guards: `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/lib/braintree/transaction_gateway.js`

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
