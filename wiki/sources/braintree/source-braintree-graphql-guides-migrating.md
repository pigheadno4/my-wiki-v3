---
title: "Braintree GraphQL Server SDK Migration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/migrating"
raw_files:
  - "braintree/graphql/guides/migrating-2026-09-16.md"
tags: [braintree, graphql, migration, server-sdk, identifiers]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes a typical migration from a legacy Braintree server-SDK integration to the GraphQL API. Its central transition is from legacy IDs to GraphQL IDs, with a staged coexistence period and mappings for payment-method, transaction and raw-card concepts. It is website guidance, not a package-qualified legacy-SDK baseline, the exact commit-qualified GraphQL schema in [[source-github-graphql-api]], current merchant enablement, or evidence that a migration or payment operation succeeded.

## Key takeaways

- Legacy and GraphQL IDs identify the same Braintree entities, but their namespaces differ: different domain objects can share a legacy ID, whereas the guide says GraphQL IDs are unique across domains. The `idFromLegacyId` query therefore takes both a legacy ID and its `LegacyIdType`; a displayed `TRANSACTION` conversion is an example, not a universal type or result.
- The guide's typical migration stages local schema and integration changes: add a GraphQL-ID field alongside stored legacy IDs, build the GraphQL integration, prefer the GraphQL ID when present, and otherwise translate the legacy ID or read a supported server-SDK object's `graphql_id`. During rollout it directs callers to request and dual-write GraphQL `id` and `legacyId`, then back-fill after launch and stop requesting/writing `legacyId` only once the GraphQL integration is stable. This sequence is guidance from the snapshot, not proof that any database migration, rollback path or production launch is safe or complete.
- The captured server-side SDK route exposes already-translated `graphql_id` values on `CreditCardVerification`, `Customer`, `Dispute` and `Transaction`. Those values must not be passed through `idFromLegacyId` again. The guide does not establish this field for unlisted objects or every SDK language/version.
- A GraphQL ID's format is explicitly not a contract. Existing IDs remain unchanged, but new formats may differ; only the documented 1–256-character alphanumeric/dash/underscore bound is stated as safe to assume. Systems should not infer object type or other behavior from the displayed encoded example.
- Terminology and actions also change. SDK nonces map to GraphQL single-use payment methods, while SDK vaulted payment methods map to multi-use payment methods and the GraphQL `usage` field distinguishes them. SDK `sale` maps conceptually to GraphQL authorize or charge mutations, with capture available separately. For PCI-scoped merchants handling raw card details, the API accepts those details only through tokenization mutations; charging or vaulting then uses the resulting payment method. The Ruby sale and GraphQL charge snippets are examples, not guarantees for all payment methods, accounts, SDK versions or schema revisions.

> [!warning] Migration and evidence boundaries
> Introducing and back-filling identifiers changes local persistence, and prematurely ending the dual-write period can remove the rollback flexibility the guide is designed to preserve. Do not translate an already translated `graphql_id`, assume an identifier's format, or project example operation shapes onto the current schema. Confirm the applicable SDK version, object support, GraphQL schema and merchant/payment-method eligibility before a production migration.

## Detail locators

- Guide purpose and legacy-versus-GraphQL identity model: opening and `## Legacy vs. GraphQL IDs`, lines 16–25.
- Staged additional-field, fallback translation, dual-write, back-fill and cutover path: `## Migrating an Integration to Use the Braintree GraphQL API`, lines 28–39.
- Supported server-SDK objects whose `graphql_id` is already translated: `### Reading the graphql_id Field`, lines 42–44.
- `idFromLegacyId` input identity and displayed transaction example: `### Using the idFromLegacyId Query`, lines 47–77.
- Non-contract identifier format and stated length/character bound: `### GraphQL ID Format`, lines 81–85.
- Nonce/single-use and vaulted/multi-use terminology mapping: `### Nonces vs. single-use payment methods`, lines 93–102.
- SDK sale versus GraphQL authorize/charge/capture mapping and example snippets: `### Creating transactions`, lines 105–137.
- PCI-scope qualification and raw-payment-detail tokenization boundary: `### Accepting payment data directly`, lines 141–145.
- Exact commit-qualified GraphQL types, operations and schema constraints are separately retained via [[source-github-graphql-api]]; they must not be inferred from this website page's examples.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Exact commit-qualified schema: [[source-github-graphql-api]]
- Related payment-method terminology route: [[source-braintree-payment-method-nonces]]

## Raw Sources

- [[raw/braintree/graphql/guides/migrating-2026-09-16|Braintree GraphQL migration guide (2026-09-16)]]
