# PayPal TypeScript Server SDK Capsule Design

**Date:** 2026-08-09
**Status:** Approved
**Repository:** `paypal/PayPal-TypeScript-Server-SDK`
**Package:** `@paypal/paypal-server-sdk`
**Initial releases:** `2.3.0`, `2.4.0`

## Purpose

Migrate the existing manually selected PayPal TypeScript Server SDK evidence into the version-qualified GitHub pipeline and establish complete runtime/model coverage for deep implementation and version-comparison queries. Preserve the legacy review rather than replacing it, then collect canonical package releases `2.3.0` and `2.4.0` as separate exact-SHA work items.

Collection does not prove merchant eligibility, regional availability, product enablement, API rollout, or production configuration. Controller and model presence proves only the retained package contract at the identified release.

## Existing Evidence and Identity Boundary

The wiki currently retains 16 selected files from commit `ff27fa8e18cccad1daf180fe98d3cf0ed5ed3c5b` and describes package `@paypal/paypal-server-sdk@2.3.0`. The official semantic tag `2.3.0` resolves to `b37cec58f2cdeecf5b9b7a7c15131cc5f4fff712`, while tag `2.4.0` resolves to `dbdbdd06f18a06d633c66bbc27d7d7a54283e1a3`.

The legacy commit and canonical `2.3.0` tag are distinct evidence identities. The collection and eventual cumulative source page must preserve that distinction and must not claim the old 16-file review is a complete tag snapshot.

Repository discovery on 2026-08-09 found `2.4.0` as the latest stable tag. The collector must re-resolve and verify every tag and package version at execution time.

## Approved Evidence Boundary

### Included

- Complete `src/` TypeScript source, including client configuration, authentication, transport integration, controllers, errors, 365 model files, schema definitions, and public exports.
- `doc/controllers/` references for Orders, Payments, Vault, Subscriptions, and Transaction Search.
- `README.md`, `CHANGELOG.md`, `package.json`, and `LICENSE` for package identity, initialization, supported APIs, release context, and provenance.

This boundary contains approximately 395 files and 2 MB per release. It supports detailed queries about controller signatures, headers, request and response models, serialization schemas, OAuth client behavior, exports, API errors, and exact `2.3.0` to `2.4.0` changes.

### Excluded

- `test/`, tests, and fixtures;
- generated `doc/models/` pages, because the complete TypeScript model source is retained;
- generated build output under `dist/`;
- CI, editor, lint, formatting, code-generation, release, and build tooling;
- lockfiles, dependencies, Git metadata, and local environment files.

An excluded generated model page is not evidence that the corresponding API model is absent. Model behavior must be grounded in the retained `src/models/` implementation and schema references.

## Version Policy

Enable the existing tier-2 registry row with one package-qualified major-version track:

```toml
[[repos.version_tracks]]
selector = "package:@paypal/paypal-server-sdk@2"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
pinned_versions = ["2.3.0", "2.4.0"]
```

`latest-stable` plus the two explicit pins selects only the approved historical baseline and current release during backfill. Future collection retains every stable release newer than the highest accepted v2 release. A future major version requires a separately reviewed track and full-ingest decision.

## Capsule Policy

Use the standard root-package NPM adapter:

```toml
[[repos.capsules]]
id = "paypal-typescript-server-sdk-source"
adapter = "npm-tracked-source-v1"
focus_packages = ["@paypal/paypal-server-sdk"]
dependency_scope = "internal-runtime-closure"
changed_path_policy = "policy-bounded"
default_required_roots = ["src", "doc/controllers"]
default_generated_target_paths = ["dist/"]
include_paths = [
  "CHANGELOG.md",
  "LICENSE",
  "README.md",
]
excluded_categories = ["tests", "fixtures"]
secret_detector = "text-secrets-v1"
max_file_bytes = 512000
max_capsule_files = 430
max_capsule_utf8_bytes = 3000000
max_packet_files = 500
max_packet_utf8_bytes = 4000000
```

The package manifest is resolved automatically by the NPM adapter and must match each selected release version. The generated `dist/` target is declared for public-export validation but is not retained as duplicate source evidence.

Budgets provide modest headroom above the reviewed release layout. A missing required path, secret finding, unsafe path, package/tag mismatch, or budget overflow stops for manual review; collection must not silently truncate or increase limits.

## Collection and Comparison Flow

1. Add focused registry tests for identity, version pins, future policy, source root, controller documentation, exclusions, and budgets.
2. Enable the registry row and run offline registry/collection validation.
3. Run a dry backfill to verify tag discovery and package identities without publishing evidence.
4. Resolve both exact tags through the capsule policy in temporary storage and confirm file counts, byte counts, hashes, UTF-8 validity, secret scan, and budgets.
5. Run real backfill collection. It may collect both releases in one collection operation, but it publishes separate exact-SHA snapshots, package release records, comparisons, packets, and work items.
6. Review both packet files and every required path before requesting ingest approval.
7. Stop with both work items at `awaiting_approval`; collection never edits wiki knowledge or begins ingest.

The collector comparison between canonical `2.3.0` and `2.4.0` is authoritative for release-delta classification. Discovery found 155 changed repository files overall and 58 changed files inside the approved capsule boundary. Upstream `CHANGELOG.md` does not describe a `2.4.0` section, so implementation evidence is required to characterize that release.

## Serial Ingest Contract

Ingest remains strictly one work item at a time:

1. Review and explicitly approve canonical `@paypal/paypal-server-sdk@2.3.0` for full ingest.
2. Read the complete approved `2.3.0` capsule and preserve the legacy `ff27fa8` findings as earlier partial evidence.
3. Complete and validate the `2.3.0` ingest before claiming the next item.
4. Review the complete `2.3.0` to `2.4.0` packet and explicitly approve its evidence-driven full or delta mode.
5. Ingest `2.4.0` by adding version-qualified findings and history; never refresh away `2.3.0` knowledge.

The canonical output is one cumulative source page plus one separate package-qualified changelog under `wiki/sources/paypal/github/`. The source page owns durable controller, client, model, header, compatibility, and evidence-boundary findings. The changelog owns release identities, exact SHAs, impact, migration notes, updated source sections, comparisons, and raw links.

## Expected `2.4.0` Review Areas

The comparison review must examine, without presupposing merchant impact:

- the new exported `ProcessingInstruction` model;
- Orders request, response, confirmation, and authorization model changes;
- Transaction Search controller and documentation changes;
- controller-reference expansions across all five API groups;
- schema-description and optionality corrections across shared models; and
- package metadata, Node compatibility, exports, and dependency changes.

The changelog omission itself is an evidence-quality finding, not proof that `2.4.0` lacks meaningful behavior changes.

## Validation and Success Criteria

- Registry, release-discovery, capsule, packet, work-item, and GitHub collection tests pass.
- Dry run discovers exactly the pinned `2.3.0` and `2.4.0` releases for initial backfill without publishing raw evidence.
- Temporary capsule resolution stays within reviewed file and byte budgets and reports no secret findings.
- Real collection publishes two immutable exact-SHA work items and stops at `awaiting_approval` with no wiki edits.
- Canonical `2.3.0` and legacy `ff27fa8` identities remain distinct and queryable.
- The `2.4.0` comparison contains no unclassified retained changes or unexplained evidence gaps.
- Existing accepted snapshots, generated tracking outside this repository, and unrelated workspace files remain untouched.
