# Stripe PHP Broad Public API Capsule Design

**Date:** 2026-08-14
**Status:** Approved design; pending written-spec review
**Repository:** `stripe/stripe-php`
**Release identity:** `stripe-php`
**Composer package:** `stripe/stripe-php`

## Purpose

Collect one immutable, package-qualified baseline for Stripe's official PHP server SDK. The source must support detailed checkout and payment implementation questions while retaining enough public runtime code for rough queries across other Stripe API domains.

The initial baseline is one exact stable release from the newest stable major. Runtime discovery on 2026-08-14 identified `stripe-php@21.2.0` as the newest stable v21 release for Composer package `stripe/stripe-php`; stable `21.1.0` and `21.1.1` are superseded baseline candidates, while alpha and beta tags are excluded. Collection must re-resolve the stable tag and exact SHA at runtime rather than trusting discovery state.

## Approved Evidence Boundary

### Included

- All public runtime PHP code under `lib/`, including:
  - the client, request, transport, retry, telemetry, exception, pagination, collection, object-conversion, and configuration layers;
  - V1 and V2 event parsing and webhook-signature handling;
  - OAuth and Connect context support;
  - generated resource classes, service classes, and service-parameter classes across every retained API domain;
  - checkout-relevant resources and services for Checkout Sessions, PaymentIntents, SetupIntents, PaymentMethods, Customers, Payment Links, Refunds, Events, Subscriptions, Invoices, and related billing objects.
- Root package and provenance files needed to understand installation, compatibility, initialization, versioning, and release history: `README.md`, `CHANGELOG.md`, `composer.json`, `init.php`, `LICENSE`, and existing API/SDK version marker files.
- The exact stable GitHub release record and release notes produced by the collector.

### Excluded

- All unit, integration, generated, and fixture tests;
- CI configuration, release automation, code-formatting configuration, static-analysis configuration, and local development scripts;
- generated HTML/API documentation and website output;
- examples or fixtures whose only purpose is testing the repository itself;
- binary assets, dependency vendor trees, caches, lockfiles, and local environment files;
- alpha, beta, release-candidate, private-preview, and other prerelease tags.

Generated runtime resource and service classes under `lib/` are public SDK evidence and must not be classified as generated documentation or discarded merely because they are code-generated.

## Version Policy

Use one package-qualified release track:

```toml
[[repos.version_tracks]]
selector = "package:stripe-php@21"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
pinned_versions = ["21.2.0"]
```

The initial collection contains exactly `stripe-php@21.2.0`. It does not backfill `21.0.0`, `21.1.0`, `21.1.1`, major 20, or any earlier release. Future collection selects every newer stable `21.x` release. A later major requires an explicit reviewed track update because Stripe PHP majors can represent API-version, typing, compatibility, or runtime boundaries.

## Capsule Policy

Use the existing `tagged-tree-v1` adapter because one semantic Git tag identifies one package release and the repository is not an NPM workspace.

The capsule should use `lib` as its required runtime root and explicit root metadata paths. It must retain the complete public runtime tree rather than an allowlist of selected products.

Before setting final file and byte budgets, implementation performs a non-publishing exact-tag inventory in temporary storage. Final registry limits must be based on the measured `21.2.0` capsule plus a small, explicit allowance for ordinary stable-minor growth. If the measured capsule exceeds collector hard limits or makes a serial full ingest impractical, implementation stops for policy review. It must not silently omit API domains, weaken secret checks, classify public runtime as navigation-only, or increase hard limits without review.

Required safety controls remain:

- path safety and symlink rejection;
- UTF-8 validation for retained text;
- per-file and aggregate size limits;
- text-secret scanning;
- deterministic retained/excluded classification;
- immutable exact-SHA publication only after all checks pass.

## Collection Flow

1. Resolve the newest stable major and exact `21.2.0` tag from the official repository; represent it as release identity `stripe-php@21.2.0` and reject prereleases.
2. Inventory the exact tag in temporary storage and measure all approved root metadata plus `lib/**/*.php`.
3. Review the measured file count, byte count, largest file, and excluded categories. Stop if the broad capsule cannot meet the existing serial-ingest and safety contract.
4. Add the reviewed package track, tagged-tree capsule, exact include roots, exclusions, and measured budgets to `tracking/github/repo-registry.toml`.
5. Add focused registry/capsule tests, run the offline validator, and run a collector dry-run. Dry-run publishes no raw evidence or work item.
6. Run real collection only after policy checks pass. Publish one exact-SHA snapshot, one release record, and one review packet.
7. Stop at `awaiting_approval`. Collection does not approve, claim ingest, or edit wiki knowledge.

No previous-major comparison is created during this baseline. Future stable releases compare against the highest retained stable `21.x` release.

## Ingest Contract

After separate user approval, ingest exactly one SHA work item. Read the cumulative source and changelog if they exist, then read both packet files, the release record and notes, the snapshot manifest, and every assigned retained file in full before writing wiki content.

Create:

```text
wiki/sources/stripe/github/source-github-stripe-php.md
wiki/sources/stripe/github/changelog-github-stripe-php.md
```

The cumulative source provides deep treatment of:

- installation, PHP runtime requirements, Composer/autoload behavior, and package version identity;
- client and service architecture;
- HTTP transport, timeouts, retries, idempotency, request options, API-version pinning, telemetry, errors, and pagination;
- webhook signature verification and V1/V2 event parsing boundaries;
- Checkout Sessions, PaymentIntents, SetupIntents, PaymentMethods, Customers, Payment Links, refunds, subscriptions, invoices, and billing flows.

Other API domains receive a concise public-surface catalog grounded in their retained resource and service classes. Their presence proves that the versioned SDK exposes those classes and methods; it does not prove merchant eligibility, product availability, account enablement, or complete business semantics.

The source must keep `stripe-php` independent from `stripe-node`. Cross-language comparisons may cite both cumulative sources, but neither repository's version or behavior may be attributed to the other.

## Full and Delta Rules

The initial baseline is recommended as `full`.

Later stable releases may use `delta` when every retained change is classified and the change is bounded to generated fields or methods, documentation, typing, or contained transport behavior. Use additive `full` ingest for:

- a new major or pinned Stripe API-version boundary;
- PHP runtime compatibility changes;
- broad client, service, transport, retry, authentication, webhook, or event architecture changes;
- incompatible public method or parameter changes;
- missing prior evidence, unbounded security impact, or capsule-policy changes.

Full ingest adds the new version's knowledge to the cumulative source and preserves validated older-version findings. It never refreshes the source to latest-only content.

## Validation and Success Criteria

- Discovery resolves `stripe-php@21.2.0` as the newest stable v21 release for Composer package `stripe/stripe-php` and excludes all prereleases.
- The temporary broad inventory contains all approved public runtime PHP files and root metadata with no tests, unsafe paths, secret findings, or unclassified retained files.
- Measured budgets are reviewed before publication and remain compatible with complete serial ingest.
- Registry/capsule tests and `python3 scripts/validate_github_collection.py` pass.
- Dry-run publishes no raw snapshot, release record, work item, or wiki edit.
- Real collection publishes one immutable exact-SHA baseline and stops at `awaiting_approval`.
- The initial review packet recommends `full`, has no unresolved evidence gaps, and lists every retained file as required reading.
- Existing accepted evidence and unrelated workspace files remain untouched.

## Explicit Non-Goals

- No previous-major baseline or v20-to-v21 comparison in this cycle.
- No prerelease or private-preview package collection.
- No automatic wiki ingest.
- No cross-language Stripe PHP versus Stripe Node comparison page during baseline collection.
- No weakening of the one-source, full-read, serial-ingest rule to accommodate capsule size.
