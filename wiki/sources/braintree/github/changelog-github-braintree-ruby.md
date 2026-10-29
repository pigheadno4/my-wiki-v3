---
title: "GitHub changelog: braintree/braintree_ruby"
type: source
date_ingested: 2026-08-23
date_updated: 2026-10-29
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/manifest.json"
  - "github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/manifest.json"
  - "github/braintree/braintree_ruby/snapshots/2026-08-23-1217992/manifest.json"
tags: [braintree, ruby-sdk, server-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_ruby`. Cumulative implementation knowledge belongs in [[source-github-braintree-ruby]] and the linked immutable snapshots.

## `braintree@4.42.0` (ingested 2026-10-29)

- Ruby gem, SHA `647f4bb8a45a869cb4d664077d28287881d299b1`, from `4.41.0`; approved delta with focused reading, preserving all older knowledge. Manifest October 19 timestamp is tag/commit-derived; no GitHub Release-note body.
- Adds `Transaction.reverse`/`reverse!` and gateway equivalents: validated ID, optional `api_request_key`, one reverse endpoint. Gateway chooses void or full refund; no local fallback or partial-refund amount. Ordinary result versus bang resource/validation exception behavior is preserved.
- Adds Mastercard external-vault link ID to card/customer signatures and previous link ID to transaction and declared verification signatures. Verification create does not invoke that signature validator. Existing response readers and generic payment-method signatures are not new features. Six error constants cover reversal availability and external-vault validation.
- Integration action: use reversal only with gateway eligibility/error handling; retain explicit refund for amount-specific refunds. Confirm external-vault product requirements separately rather than inferring them from SDK fields. No runtime, merchant enablement or payment execution claim.
- Seven modified/194 unchanged retained files, 17 upstream dispositions (seven retained/ten excluded specs), no gaps/unclassified changes. Changed source, comparison, affected prior code and cumulative history read; inventories/unchanged history mechanically checked. Concept, source, company, catalog and logs updated without changing source_count.

Evidence:
- `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-647f4bb/manifest.json`
- `raw/github/braintree/braintree_ruby/releases/braintree/4.42.0/2026-10-29/manifest.json` - adjacent empty release-notes.md
- `tracking/github/repos/braintree/braintree_ruby/comparisons/braintree/4.41.0--4.42.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-braintree-ruby]] - source paths, five located quotes and detailed limits

## `braintree@4.41.0` (ingested 2026-10-29)

- Ruby SDK, SHA f3d70148cb0a68e8a20160b9a8e4e01e7d79d1df, from4.40.0. Manifest September16 timestamp is tag/commit-derived, not GitHub release publication; upstream release-note body absent. Approved additive full override with focused reading; all4.40.0 history retained.
- Adds preferred_payment_method_token to client-token generation, shallow-copying options and remapping to payment_method_id; symbol key wins if both forms exist. Closes the recorded Ruby option gap, not proof of frontend returning-buyer support or token authorization.
- Extends the existing stringifying ASCII path allowlist across15 gateway classes and a customer association-filter input. Invalid affected paths raise ArgumentError before HTTP; body IDs are not universally covered. Some old lowercase-only checks become broader, not uniformly stricter character sets. No all-path security/exploit guarantee or sanitization advice.
- GET/DELETE start forwarding query hashes through an unchanged non-encoding helper; no automatic existing-query merge. Adds ACH search same_day/standard and explicitly allowed refund surcharge_amount. Runtime, README/gemspec, webhook and merchant eligibility boundaries remain unchanged; no gateway/Ruby/payment execution.
- 201 current/201 prior files,21 modified/180 unchanged; all402 size/SHA-256/Git IDs pass. Upstream46=21 retained+25 exclusions; no gaps/unclassified changes. Full assignment210; changed retained files and affected prior code/cumulative history read, manifests/unchanged evidence mechanically checked under approval. Raw changelog retains1308 prior lines with6 inserted. Concept first, cumulative source/company/index/logs updated, source_count unchanged. No commit/push.

Evidence:
- `raw/github/braintree/braintree_ruby/snapshots/2026-10-29-f3d7014/manifest.json`
- `raw/github/braintree/braintree_ruby/releases/braintree/4.41.0/2026-10-29/manifest.json` - adjacent empty release-notes.md
- `tracking/github/repos/braintree/braintree_ruby/comparisons/braintree/4.40.0--4.41.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-braintree-ruby]] - precise source paths, five located quotes and behavior boundaries

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
