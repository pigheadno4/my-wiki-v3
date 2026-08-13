# Braintree GraphQL API Checkout Capsule Design

## Goal

Collect `braintree/graphql-api` as immutable commit-qualified evidence and ingest checkout knowledge deeply without expanding the wiki into full operational coverage of every GraphQL domain.

## Upstream Shape

The repository contains three root-level files:

- `schema.graphql`: the complete monolithic GraphQL schema
- `CHANGELOG.md`: chronological API changes
- `README.md`: repository purpose and documentation links

The schema cannot be split into a checkout-only raw artifact without modifying upstream evidence or risking omitted type dependencies.

## Collection Design

Enable the existing tier-1, monthly, commit-tracked registry entry and add one `commit-tree-v1` capsule. The capsule must collect all three files verbatim, pin them to the resolved default-branch SHA, and stop at `awaiting_approval` after producing the baseline packet.

The current commit-tree adapter requires each `default_required_roots` entry to be a directory. Extend its general path resolution so a required entry may identify either a directory prefix or an exact root-level file. Configure `schema.graphql` as the required source path and `CHANGELOG.md` plus `README.md` as required includes. This is a common compatibility improvement, not a Braintree-specific exception.

Use limits sized narrowly above the observed corpus: one file may be approximately 650 KB, the complete three-file capsule approximately 800 KB, and the packet approximately 1.5 MB across at most 15 paths. The path limit covers the current snapshot, existing wiki context, and a future full comparison with prior evidence. Tests and fixtures remain excluded even though none are currently present.

## Ingest Boundary

The baseline requires full ingest and complete serial reading of the cumulative source page, packet, `README.md`, `CHANGELOG.md`, and `schema.graphql`.

Deep coverage includes:

- transactions, authorizations, captures, settlements, refunds, and verifications
- payment methods and tokenization
- vault and customer payment-method behavior
- PayPal and Venmo GraphQL types and flows
- 3D Secure
- recurring billing subscriptions and plans

Other GraphQL domains receive only a high-level inventory and evidence pointers. The source page must distinguish schema capability from merchant eligibility, regional availability, and end-to-end product support.

Create one cumulative source page and one separate commit-qualified changelog under `wiki/sources/braintree/github/`. Future selected changes use default-branch comparisons and may use delta ingest only when every retained change is bounded and classified.

## Validation And Failure Handling

Add focused tests for exact-file required-path selection, missing required files, and preservation of existing directory behavior. Run the GitHub unit tests and `scripts/validate_github_collection.py` before collection.

Collection remains atomic. Any missing file, hash failure, secret finding, budget overflow, or invalid packet must publish no partial raw snapshot and must not enter ingest approval.

## Success Criteria

- The registry validates with `braintree/graphql-api` enabled.
- Existing directory-based capsules behave unchanged.
- One exact-SHA snapshot contains the three upstream files verbatim.
- The generated work item stops at `awaiting_approval` with a deterministic `full` recommendation.
- No wiki page is edited before packet review and explicit user approval.
