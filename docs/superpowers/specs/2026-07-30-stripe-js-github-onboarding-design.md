# Stripe JS GitHub Onboarding Design

**Date:** 2026-07-30
**Repository:** `stripe/stripe-js`
**Package:** `@stripe/stripe-js`
**Status:** Approved design

## Goal

Onboard `stripe/stripe-js` as the sixth executable GitHub repository using the existing release-driven collection pipeline. Establish a useful major-version baseline without backfilling every historical release, then retain every future stable release in the current major.

Collection must create immutable raw evidence and review packets only. It must not edit wiki knowledge or begin ingest automatically.

## Release Retention

Configure two package-qualified tracks:

| Track | Backfill | Future |
| --- | --- | --- |
| `package:@stripe/stripe-js@8` | latest stable | none |
| `package:@stripe/stripe-js@9` | latest stable | all stable |

The initial collection therefore retains the latest stable v8 release and latest stable v9 release. It processes v8 first, followed by the v8-to-v9 transition. Later runs retain each stable v9 release newer than the highest accepted v9 version.

Prereleases are excluded. The collector must resolve exact upstream tags and package manifests; it must not infer a release from an incomplete or ambiguous tag.

## Source Capsule

Reuse `npm-tracked-source-v1` with `@stripe/stripe-js` as the only focus package. The package lives at the repository root, so no Stripe-specific adapter is required.

The bounded capsule includes:

- `src/` for the script loader and side-effect behavior;
- `types/` for the public Stripe.js, Elements, and API declarations;
- `pure/` for the side-effect-free package entrypoint;
- `examples/parcel/src/` and `examples/rollup/src/` for reviewed integration examples; and
- standard repository context such as `README.md`, `LICENSE`, and `package.json`.

Tests, fixtures, example lockfiles and build configuration, dependencies, generated `lib/` output, distribution artifacts, and unrelated repository automation are excluded.

The initial limits are:

| Limit | Value |
| --- | ---: |
| Per file | 512,000 bytes |
| Snapshot files | 160 |
| Snapshot UTF-8 content | 2,000,000 bytes |
| Packet files | 200 |
| Packet UTF-8 content | 2,500,000 bytes |

The retained v9.12.1 source, type, pure-entrypoint, and example-source roots contain approximately 67 files before standard context, leaving capacity for normal growth without permitting a full-repository snapshot. These budgets remain hard failure boundaries. A budget failure stops collection for policy review; it does not silently truncate accepted evidence.

Changed files in later releases remain policy-bounded. A changed public source, type declaration, entrypoint, documentation file, or example must be classified into the packet. Unclassified changes or evidence gaps block delta approval.

## Knowledge Boundary

`@stripe/stripe-js` is a loader and TypeScript declaration package for Stripe-hosted Stripe.js. Package release evidence can establish loader behavior, package entrypoints, TypeScript surfaces, and pinned Stripe.js generation. It cannot by itself prove the runtime availability of every feature served from `js.stripe.com`.

The eventual cumulative source page and changelog must preserve that boundary and use package-qualified versions. Runtime feature claims require corroborating Stripe documentation or other direct runtime evidence.

## Collection And Ingest Flow

1. Add the two version tracks and one bounded capsule to the existing registry row, then enable the repository.
2. Add focused registry coverage for the exact tracks, capsule roots, exclusions, and budgets.
3. Run the existing registry, capsule, release, collector, packet, and validation tests.
4. Run `collect --repo stripe/stripe-js --mode backfill`.
5. Validate the generated snapshots, releases, comparisons, work items, packets, hashes, and status offline.
6. Stop with the generated work items in `awaiting_approval`.
7. Review each packet with the user.
8. After approval, ingest the v8 baseline first and the v9 transition second, reading every required path in full and processing one work item at a time.

No source page, changelog, company page, concept page, index, or log is created during collection.

## Expected Wiki Targets

Approved serial ingest will use:

- `wiki/sources/stripe/github/source-github-stripe-js.md`
- `wiki/sources/stripe/github/changelog-github-stripe-js.md`
- `wiki/companies/stripe.md`
- affected Stripe concept pages
- `wiki/stripe-index.md`
- `wiki/stripe-log.md`

The source page remains cumulative and retains both v8 and v9 findings. The changelog records package-qualified transitions and links to immutable raw evidence.

## Validation And Success Criteria

The onboarding is successful when:

- registry validation accepts the enabled repository;
- focused and full automated tests pass;
- latest stable v8 and v9 releases resolve deterministically;
- each accepted SHA produces one immutable bounded snapshot;
- each package release has a separate immutable release record;
- the v8-to-v9 comparison and review packets contain no unclassified changes or blocking evidence gaps;
- `validate_github_collection.py` passes; and
- no wiki file is changed before explicit ingest approval.

If upstream layout or tag behavior violates these assumptions, collection must fail without publishing partial evidence. The policy is then revised from observed upstream evidence before retrying.
