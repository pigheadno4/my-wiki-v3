---
title: "GitHub changelog: braintree/graphql-api"
type: source
date_ingested: 2026-08-11
date_updated: 2026-10-23
original_format: github-repo
raw_files:
  - "github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/manifest.json"
  - "github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/manifest.json"
tags: [braintree, graphql, api-specification, changelog, github-repository]
---

## Overview

Commit-qualified schema history for `braintree/graphql-api`. Cumulative API-contract knowledge belongs in [[source-github-graphql-api]] and the linked immutable snapshot.

## `default-branch@9f76e60` (2026-10-20)

| Ref | From | To | Ingest mode |
| --- | --- | --- | --- |
| `master` | `3a89f427466a0a978dbfcfd953913f4e76c3264a` | `9f76e60580da00f6740a20692d0b5ea2f313d93e` | Full additive override; approved focused reading |

**Ingested:** 2026-10-23. Full mode is justified by removed inputs and response nullability, overriding the script's contained-file delta recommendation. The prior baseline remains unchanged below; no semantic SDK release is invented.

### New changelog milestones since the baseline

| Changelog date | Retained change and impact |
| --- | --- |
| 2026-08-11 | Adds BLIK Pay Later, OXXO Pay and PIX International local-payment/search enum entries; inventory is not eligibility or SDK support |
| 2026-08-13 | Removes merchant-account search `id: SearchValueInput`; adds `merchantAccountId: SearchTextValueInput`, the account token with broader text filters |
| 2026-09-15 | Expands `ExternalProcessor`; names do not prove connector enablement |
| 2026-09-30 | Replaces both PayPal experience-profile shipping booleans with `shippingPreference`; adds transaction customer first/last name and US e-commerce card refund-surcharge attribution |
| 2026-10-06 | Adds 3DS lookup `deviceId`; subscription response `paymentMethodId` becomes nullable; formally deprecates Boleto/Samsung enum entries and Venmo top-level `userName` |
| 2026-10-20 | Adds Smart Authentication skip status; deprecates the Adaptive Authentication value in favor of it |

**Migration:** Choose explicit buyer-selected, merchant-locked or no-address shipping behavior; the schema supplies neither a default nor a universal conversion from the old booleans. Remove old input fields from generated clients/requests. Audit merchant-account filter name/type and returned subscription null handling. Subscription creation still requires `paymentMethodId: ID!`. Refund `surchargeAmount` is included in, not added to, the total; preserve non-negative/US/e-commerce-credit-card qualifiers. `deviceId` differs from CardinalCommerce `dfReferenceId`, and a skipped 3DS status does not prove authentication, liability shift or payment success.

**Additional description changes:** OAuth requirements are now stated for generic charge, vault, reversal, verification and legacy-ID conversion operations. They are not newly added operation signatures or proof of a new enforcement date. Many legacy fields only gain dated deprecation descriptions. Boleto/Samsung/Venmo prose already warned of deprecation in the old schema; do not infer a newly discontinued flow. The Smart/Adaptive status note's 2026-10-20 announcement differs from its since-2026-10-01 annotation; neither establishes production rollout timing. Returning-buyer View/Edit mutations were already in the baseline.

**Scope/verification:** Three current files / 615,078 bytes; two modified and one unchanged. Both three-file snapshots verified by size/SHA-256/Git blob ID. The full patch reconstructs all new files exactly; the original raw changelog remains an exact suffix with 48 inserted lines. Read changed current definitions and affected prior definitions in full (71 current blocks including one new enum), new notes, README and cumulative wiki history; unchanged schema/history, generated manifests/diff and inventories checked mechanically under explicit approval. No claim to a full schema reread, deployed API availability or payment execution.

**Updated knowledge:** Existing [[braintree-payment-platform]], [[paypal-braintree-integration]] and [[braintree-3d-secure]] concepts before source edits; cumulative source/changelog, company, index and logs. Source count unchanged; no cross-provider comparison warranted. Earlier `3a89f42` facts and evidence links preserved.

### `9f76e60` evidence

- [Snapshot manifest](../../../../raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/manifest.json) and [exact schema](../../../../raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/schema.graphql)
- [[raw/github/braintree/graphql-api/snapshots/2026-10-23-9f76e60/files/CHANGELOG|Changelog milestones]]
- [Comparison](../../../../tracking/github/repos/braintree/graphql-api/comparisons/default-branch/3a89f42--9f76e60/comparison.json) and [retained patch](../../../../tracking/github/repos/braintree/graphql-api/comparisons/default-branch/3a89f42--9f76e60/diff.patch)
- [[source-github-graphql-api]] - version-qualified contracts, examples and five grounding excerpts

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
