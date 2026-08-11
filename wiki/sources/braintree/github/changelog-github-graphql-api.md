---
title: "GitHub changelog: braintree/graphql-api"
type: source
date_ingested: 2026-08-11
original_format: github-repo
raw_files:
  - "github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/manifest.json"
tags: [braintree, graphql, api-specification, changelog, github-repository]
---

## Overview

Commit-qualified schema history for `braintree/graphql-api`. Cumulative API-contract knowledge belongs in [[source-github-graphql-api]] and the linked immutable snapshot.

## `default-branch@3a89f42` (2026-08-04)

| Ref | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `master` | Initial baseline | `default-branch@3a89f42` | `3a89f427466a0a978dbfcfd953913f4e76c3264a` | Full |

**Latest exact change:** Added `MerchantAccountCapabilities`, `MerchantAccountType`, the `deprecatedSince` directive, additional card-brand enum values, and merchant-account `accountType`, `capabilities`, and `supportsPublicDescriptors` fields.

**Recent recurring-billing milestones:** April through July 2026 added plan, add-on, discount, subscription create/update/cancel/search/charge operations, lifecycle records, proration controls, template deletion, and direct top-level search queries.

**Checkout history retained in the baseline:** Dedicated PayPal and Venmo authorization, charge, setup, tokenization, and vault operations; Venmo payment contexts; partial capture; client tokens; 3D Secure lookup and pass-through fields; transaction idempotency and lifecycle operations.

**Developer or merchant impact:** The exact schema can ground generated-client and direct GraphQL field questions. New schema fields remain optional contract additions unless their nullability or documentation says otherwise. Merchant availability and client-SDK support require separate evidence.

**Migration action:** No repository-wide migration is documented for the retained commit. Integrations using the deprecated nested `search` query should move to the corresponding top-level search fields. Consumers should regenerate or validate clients when adopting newly exposed schema fields.

**Evidence boundary:** This is the first retained exact-SHA baseline, so no prior snapshot comparison exists. The source page describes cumulative behavior present at this commit; it does not attribute all current operations to the 2026-08-04 change.

**Evidence:**

- Snapshot manifest: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/manifest.json`
- Exact schema: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql`
- Full upstream history: `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/CHANGELOG.md`
