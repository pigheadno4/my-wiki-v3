# Braintree Node Checkout-Focused Capsule Design

**Date:** 2026-08-09
**Status:** Approved
**Repository:** `braintree/braintree_node`
**Package:** `braintree`

## Purpose

Collect the official Braintree Node server SDK as immutable, package-qualified GitHub evidence for checkout implementation and version queries. The first ingest must establish detailed knowledge for gateway configuration, client-token generation, transactions, payment methods, vault operations, cards, PayPal, Venmo, subscriptions, refunds, 3D Secure, validation, and checkout-relevant webhooks.

Other server domains remain discoverable as inventory without receiving the same semantic depth. Collection does not prove merchant enablement, regional availability, gateway configuration, or production eligibility.

## Approved Evidence Boundary

Design discovery found `braintree@3.39.0` as the latest stable semantic tag. Its runtime contains 164 files under `lib/` totaling approximately 321 KB. The tag resolves to exact commit `7a9270aaf31eb87819add64a768652243f90007c`; collection must resolve and verify the tag again at run time.

### Included

- Complete `lib/` runtime so public exports, shared transport, request serialization, response models, validation codes, and gateway dependencies remain source-complete.
- `index.js` and `package.json` for package identity and public entry-point evidence.
- `README.md` and `CHANGELOG.md` for installation, supported major-line status, migration context, and release findings.
- `SECURITY.md` and `LICENSE` for security reporting and evidence provenance.

### Excluded

- `test/` and test fixtures;
- package lockfiles;
- CI, build, lint, formatting, editor, Docker, and release tooling;
- generated dependencies, Git metadata, and local environment files.

The exported `lib/braintree/test_values/` constants are runtime API evidence used for sandbox integration; they are not repository test fixtures and remain included.

## Registry Design

Enable the existing tier-2 registry entry and add one stable major-version track:

```toml
[[repos.version_tracks]]
selector = "package:braintree@3"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
pinned_versions = ["3.39.0"]
```

Use one root-package capsule:

```toml
[[repos.capsules]]
id = "braintree-node-checkout-source"
adapter = "npm-tracked-source-v1"
focus_packages = ["braintree"]
dependency_scope = "internal-runtime-closure"
changed_path_policy = "policy-bounded"
default_required_roots = ["lib"]
default_generated_target_paths = []
include_paths = ["README.md", "CHANGELOG.md", "SECURITY.md", "LICENSE", "index.js"]
excluded_categories = ["tests", "fixtures"]
secret_detector = "text-secrets-v1"
max_file_bytes = 512000
max_capsule_files = 220
max_capsule_utf8_bytes = 1500000
max_packet_files = 260
max_packet_utf8_bytes = 2000000
```

The registry stores stable policy only. Versions, SHAs, collection dates, comparisons, failures, and ingest state remain in generated tracking files.

## Collection and Comparison Flow

1. Validate the registry and run a dry collection for `braintree/braintree_node` to verify release discovery without publication.
2. Resolve the highest configured stable `braintree@3` release and verify package identity against the semantic tag.
3. Before requesting publication approval, run the capsule resolver against that exact tag in temporary storage to select, hash, UTF-8 validate, budget-check, and secret-scan the approved runtime capsule. The generic release dry-run currently stops after tag verification.
4. On explicit approval for real collection, publish the exact-SHA snapshot, release record, and full-review packet.
5. Stop at `awaiting_approval`; collection never starts ingest or edits wiki knowledge.
6. For future checks, compare each newer stable release with the highest retained version. Unchanged checks publish no work item.

The initial baseline is recommended as `full`. Later major changes, broad checkout behavior, public API incompatibility, security changes with unbounded impact, or capsule-policy changes also require full review. A contained, fully classified update may be recommended as delta.

## Ingest Contract

After separate user approval, ingest one exact-SHA work item serially and read every required path in full. Create one cumulative source page and one package-qualified changelog under `wiki/sources/braintree/github/`.

Deep synthesis covers:

- credentials, environments, HTTP behavior, and `BraintreeGateway` construction;
- client-token generation and client/server authorization boundaries;
- transaction sale, authorize, submit-for-settlement, void, refund, and search flows;
- customers, payment methods, nonces, cards, vault behavior, and verification;
- PayPal, Venmo, local methods, subscriptions/plans, 3D Secure, validation, and relevant webhooks;
- sandbox runtime test values exposed by the package.

Disputes, merchant onboarding, OAuth partner operations, document upload, settlement reporting, and unrelated administration APIs receive an inventory and evidence boundary only. A later detailed query can use the retained runtime or request an approved supplement if required evidence is absent.

## Validation and Success Criteria

- Registry and GitHub collection validators pass.
- Dry run identifies `braintree@3.39.0` without publishing raw evidence or a work item.
- Temporary exact-tag resolution proves the selected capsule remains within reviewed file and byte budgets and contains no secret findings.
- Real collection, when separately approved, stops at `awaiting_approval` with no wiki edits.
- The initial packet recommends full ingest and contains no unclassified retained changes or evidence gaps.
- Existing accepted snapshots and unrelated workspace files remain untouched.
