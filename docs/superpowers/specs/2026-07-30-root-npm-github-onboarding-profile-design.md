# Root npm GitHub Onboarding Profile Design

**Date:** 2026-07-30
**Profile:** Root npm package
**Validation pilot:** `stripe/stripe-js` (`@stripe/stripe-js`)
**Status:** Approved design

## Goal

Define one reusable onboarding profile for repositories that publish a single npm package from the repository root. Validate the profile by onboarding `stripe/stripe-js` as the sixth executable GitHub repository.

The profile establishes a useful major-version baseline without backfilling every historical release, then retains every future stable release in the current major. Future repositories that satisfy the profile contract reuse this design and its implementation plan; they do not require repository-specific design documents.

Collection must create immutable raw evidence and review packets only. It must not edit wiki knowledge or begin ingest automatically.

## Profile Contract

A repository can reuse this profile when all of these conditions hold:

- one focus npm package is declared by the root `package.json`;
- stable releases use deterministic semantic-version tags;
- the package name and version at each selected tag match the package-qualified release identity;
- public implementation, declarations, documentation, and examples can be expressed as bounded repository-relative roots;
- generated output, dependencies, tests, and fixtures can be excluded without losing the public source of truth; and
- the existing `npm-tracked-source-v1` adapter can classify changed public evidence without repository-specific code.

Reuse requires only:

1. a reviewed registry row with package-qualified version tracks, bounded roots, exclusions, and budgets;
2. focused registry coverage for that row;
3. a smoke collection and offline validation; and
4. user review of each generated ingest packet.

The registry row and generated packet are the repository-specific onboarding record. Do not create another design or implementation plan when the repository conforms to this contract.

A new or amended design is required only when observed evidence shows a different adapter family, multiple independently versioned packages, ambiguous or non-semantic tags, generated-only public sources, an unbounded evidence layout, or another material exception to this profile.

## Stripe JS Pilot Retention

Configure two package-qualified tracks:

| Track | Backfill | Future |
| --- | --- | --- |
| `package:@stripe/stripe-js@8` | latest stable | none |
| `package:@stripe/stripe-js@9` | latest stable | all stable |

The initial collection therefore retains the latest stable v8 release and latest stable v9 release. It processes v8 first, followed by the v8-to-v9 transition. Later runs retain each stable v9 release newer than the highest accepted v9 version.

Prereleases are excluded. The collector must resolve exact upstream tags and package manifests; it must not infer a release from an incomplete or ambiguous tag.

## Stripe JS Pilot Capsule

Reuse `npm-tracked-source-v1` with `@stripe/stripe-js` as the only focus package. The package lives at the repository root, so no Stripe-specific adapter is required.

The bounded capsule includes:

- `src/` for the script loader and side-effect behavior;
- `types/` for the public Stripe.js, Elements, and API declarations;
- `pure/` for the side-effect-free package entrypoint;
- `examples/parcel/src/` and `examples/rollup/src/` for reviewed integration examples; and
- standard repository context such as `README.md`, `LICENSE`, and `package.json`.

Tests, fixtures, example lockfiles and build configuration, dependencies, the generated `lib/` tree, distribution artifacts, and unrelated repository automation are excluded as required roots. Exact tracked files referenced by public package fields such as `main`, `module`, `types`, or `exports` remain eligible because they are package entrypoint evidence.

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

## Stripe JS Knowledge Boundary

`@stripe/stripe-js` is a loader and TypeScript declaration package for Stripe-hosted Stripe.js. Package release evidence can establish loader behavior, package entrypoints, TypeScript surfaces, and pinned Stripe.js generation. It cannot by itself prove the runtime availability of every feature served from `js.stripe.com`.

The eventual cumulative source page and changelog must preserve that boundary and use package-qualified versions. Runtime feature claims require corroborating Stripe documentation or other direct runtime evidence.

## Profile Implementation And Pilot Flow

1. Implement any profile-level test coverage needed to prove a root npm package is handled by the existing adapter without repository-specific code.
2. Add the Stripe JS version tracks and bounded capsule to its existing registry row, then enable the repository.
3. Add focused registry coverage for the exact tracks, capsule roots, exclusions, and budgets.
4. Run the existing registry, capsule, release, collector, packet, and validation tests.
5. Run `collect --repo stripe/stripe-js --mode backfill`.
6. Validate the generated snapshots, releases, comparisons, work items, packets, hashes, and status offline.
7. Stop with the generated work items in `awaiting_approval`.
8. Review each packet with the user.
9. After approval, ingest the v8 baseline first and the v9 transition second, reading every required path in full and processing one work item at a time.

After the pilot passes, onboard another conforming root npm repository by adding and testing its registry policy, then running its smoke collection. Do not reopen profile design unless the smoke collection exposes a profile-contract violation.

No source page, changelog, company page, concept page, index, or log is created during collection.

## Stripe JS Expected Wiki Targets

Approved serial ingest will use:

- `wiki/sources/stripe/github/source-github-stripe-js.md`
- `wiki/sources/stripe/github/changelog-github-stripe-js.md`
- `wiki/companies/stripe.md`
- affected Stripe concept pages
- `wiki/stripe-index.md`
- `wiki/stripe-log.md`

The source page remains cumulative and retains both v8 and v9 findings. The changelog records package-qualified transitions and links to immutable raw evidence.

## Validation And Success Criteria

The profile implementation and Stripe JS pilot are successful when:

- tests demonstrate that a conforming root npm package needs no repository-specific adapter;
- registry validation accepts the enabled repository;
- focused and full automated tests pass;
- latest stable v8 and v9 releases resolve deterministically;
- each accepted SHA produces one immutable bounded snapshot;
- each package release has a separate immutable release record;
- the v8-to-v9 comparison and review packets contain no unclassified changes or blocking evidence gaps;
- `validate_github_collection.py` passes; and
- no wiki file is changed before explicit ingest approval.

If upstream layout or tag behavior violates these assumptions, collection must fail without publishing partial evidence. The policy is then revised from observed upstream evidence before retrying.

The profile is ready for reuse only after the Stripe JS pilot reaches `awaiting_approval` with valid immutable evidence and review packets. Wiki ingest is not required to prove that collection onboarding can be reused, although Stripe JS ingest still follows the normal serial approval workflow.
