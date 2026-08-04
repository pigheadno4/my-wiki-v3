# PayPal Server-Side Sample Collection Design

**Date:** 2026-08-04
**Status:** Approved design, pending written-spec review
**Repository:** `paypal-examples/paypal-sdk-server-side-integration`

## Purpose

Collect the PayPal JS SDK and backend-server sample as bounded, immutable GitHub evidence for future checkout queries. The evidence must preserve the browser-to-server contract for one-time checkout, Hosted Fields, client tokens, shipping changes, and subscription create, activate, and revise operations.

The repository is tracked by its default branch and exact commit SHA. It must not receive a fabricated package version.

## Approved Evidence Boundary

Design discovery resolved the upstream default branch to `5409a3b9c0b6d0049fc3be9386092759fd6a1d5c`, committed on 2023-09-28. Collection must resolve the branch again at run time; this design-time SHA is context, not a pinned target.

The design-time selected inventory contains 36 files totaling 101,281 bytes.

### Included

- `src/`: Fastify server, configuration, OAuth and client-token handling, Orders create/get/patch/capture, shipping data, and subscription create/activate/revise code.
- `public/`: PayPal Buttons, Hosted Fields, and subscription browser examples.
- `docs/`: migration guidance from client-side helpers to server-side operations.
- `README.md`, `example.env`, `package.json`, and `tsconfig.json` for setup, dependency, and configuration context.

### Excluded

- tests;
- `package-lock.json`;
- CI and GitHub workflow files;
- lint, formatting, editor, and Node-version tooling;
- generated output, dependencies, Git metadata, and real environment files.

The snapshot proves implementation present at one exact commit. It does not prove current product availability, merchant eligibility, regional support, certification, or production suitability.

## Registry Design

Enable the existing tier-1 registry entry with one `commit-tree-v1` capsule:

```toml
[[repos.capsules]]
id = "paypal-server-side-sample-source"
adapter = "commit-tree-v1"
source_id = "paypal-sdk-server-side-integration"
dependency_scope = "configured-repository-paths"
changed_path_policy = "policy-bounded"
default_required_roots = ["docs", "public", "src"]
include_paths = ["README.md", "example.env", "package.json", "tsconfig.json"]
excluded_categories = ["tests", "fixtures"]
secret_detector = "text-secrets-v1"
max_file_bytes = 512000
max_capsule_files = 50
max_capsule_utf8_bytes = 250000
max_packet_files = 60
max_packet_utf8_bytes = 500000
```

The registry stores stable policy only. Mutable SHAs, dates, failures, and work-item states remain in generated tracking files.

## Collection and Comparison Flow

1. Resolve the remote default branch to an exact full SHA.
2. Select only files allowed by the capsule and run secret scanning and budget checks.
3. Publish an immutable baseline snapshot and deterministic full-review packet.
4. Stop at `awaiting_approval`; collection never authorizes wiki ingest.
5. For later checks, compare selected path/hash evidence with the last accepted snapshot.
6. Skip unchanged or excluded-only changes. Publish a comparison and new work item only when selected evidence changes.

The initial baseline is always recommended as `full`. Later broad payment, authentication, server architecture, or subscription changes require full review; bounded changes may be recommended as delta.

## Ingest Contract

After explicit approval, ingest one work item serially: read every required path in full, verify hashes, report findings, and update the cumulative repository source plus a separate commit changelog. Preserve old commit-qualified findings when adding newer evidence.

Expected wiki coverage includes PayPal Checkout, Hosted Fields, Orders, authentication/client tokens, shipping updates, and Subscriptions. Documentation claims that conflict with implementation must be recorded as contradictions rather than silently reconciled.

## Validation and Success Criteria

- Registry and GitHub collection validators pass.
- The baseline snapshot contains only the approved 36-file class of evidence and no secrets.
- No release record or semantic package identity is created.
- The work item stops at `awaiting_approval` with no automatic wiki edits.
- Future unchanged checks create no snapshot or ingest item.
