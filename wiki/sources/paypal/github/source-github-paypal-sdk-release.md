---
title: "GitHub: paypal/paypal-sdk-release"
type: source
date_ingested: 2026-08-21
date_updated: 2026-10-04
original_format: github-repo
raw_files:
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-27aa46b/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-da10cb8/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-2e5394c/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-627d37c/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-7f58511/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-8924d8f/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-5f04b0c/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-7597acd/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-f0dd88b/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-3a1548a/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-10-04-0fcbea2/manifest.json"
  - "github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/manifest.json"
tags: [paypal, javascript-sdk, release-automation, dependency-manifest, github-repository]
---

## Overview

`paypal/paypal-sdk-release` is the assembly and release repository for a combined PayPal and Braintree browser SDK bundle. This cumulative page starts with package-qualified baseline `@paypal/sdk-release@5.0.569` at exact SHA `71e5116c56355a60bc8af337720116047d4d6ab8`.

Repository: <https://github.com/paypal/paypal-sdk-release>

Latest locally ingested assembly in this history: `@paypal/sdk-release@5.0.580` (released 2026-09-29, ingested 2026-10-04). It pins Checkout `5.0.436`, Messaging `1.98.0` and Common `1.0.62`; the other nine direct pins match baseline `5.0.569`. Each intermediate version remains below and in [[changelog-github-paypal-sdk-release]]. This is not a live upstream-latest or deployed-traffic assertion.

## Evidence boundary

- This repository proves which direct component package versions were assembled by `@paypal/sdk-release@5.0.569` and how that assembly is upgraded, published, and deployed. It does not prove that every component is enabled for a merchant, region, buyer, or transaction.
- Component implementation behavior remains owned by independently collected repositories such as [[source-github-paypal-checkout-components]], [[source-github-paypal-sdk-logos]], and [[source-github-paypal-js]]. Do not transfer behavior between their package versions merely because they appear in this release manifest.
- Upstream provides no GitHub release notes for tag `v5.0.569`. The initial baseline therefore comes from the complete retained capsule rather than a release-note narrative.
- The policy capsule excludes the large transitive `package-lock.json` and embedded CDN tarballs. Direct dependencies are retained in `package.json`; exact transitive dependency or packaged-artifact questions require a supplement pinned to this SHA.

## Grounding excerpts

> "Wrapper module to test and release combined client SDK modules for PayPal and Braintree."
>
> `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/README.md:14`

> "Unified SDK wrapper module for tests, shared build config, and deploy."
>
> `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/package.json:4`

> "Error: Only @paypal packages are allowed."
>
> `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/deploy.yml:45-47`

> "Ensure SVGs have been published on CDN"
>
> `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/publish.yml:32-33`

> `return setupSDK(components);`
>
> `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/index.js:3-6`

## Release assembly at `5.0.569`

The package manifest pins twelve direct PayPal components:

| Component | Version | Assembly role |
| --- | --- | --- |
| `@paypal/checkout-components` | `5.0.428` | Checkout presentation and browser runtime |
| `@paypal/messaging-components` | `1.94.0` | Pay Later and promotional messaging |
| `@paypal/applepay-components` | `1.8.2` | Apple Pay browser component |
| `@paypal/googlepay-components` | `1.3.5` | Google Pay browser component |
| `@paypal/card-components` | `1.0.59` | Card component runtime |
| `@paypal/common-components` | `1.0.60` | Shared component behavior |
| `@paypal/example-components` | `1.0.28` | Example component package |
| `@paypal/funding-components` | `1.0.32` | Funding presentation components |
| `@paypal/identity-components` | `5.0.14` | Identity component package |
| `@paypal/legal-components` | `1.2.2` | Legal presentation components |
| `@paypal/muse-components` | `1.3.98` | Muse component package |
| `@paypal/sdk-client` | `4.0.204` | SDK setup runtime used by the wrapper entry point |

The entry point imports `setupSDK` from `@paypal/sdk-client/src` and delegates its `components` argument to that function. The retained function accepts `namespace` and a misspelled `verison` parameter but does not use either parameter. This is source-level wrapper behavior, not a documented merchant API contract.

## Assembly update: `@paypal/sdk-release@5.0.570`

Released 2026-08-25; delta-ingested 2026-10-04 at SHA `0fcbea21c0ee4fb63c0c5ed6441eb51ff33832f8`, after `5.0.569`.

| Direct component | At `5.0.569` | At `5.0.570` |
| --- | --- | --- |
| `@paypal/checkout-components` | `5.0.428` | `5.0.431` |
| `@paypal/messaging-components` | `1.94.0` | `1.95.1` |

All ten other direct pins, development dependencies, scripts and engine requirements are unchanged. Only `package.json` changes within the eleven-file retained capsule; the wrapper, README and workflows are byte-identical. This is assembly evidence, not a new merchant API or proof of enabled/deployed component behavior. No GitHub release notes are available. Excluded lockfile/CDN-artifact changes remain outside the implementation evidence boundary.

Grounding in `raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-0fcbea2/files/package.json`: line 3 `"version": "5.0.570",`; line 70 `"@paypal/checkout-components": "5.0.431",`; line 76 `"@paypal/messaging-components": "1.95.1",`; line 78 `"@paypal/sdk-client": "4.0.204"`.

Evidence: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-0fcbea2/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-0fcbea2/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.570/2026-10-04/manifest.json), [note record](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.570/2026-10-04/release-notes.md), [comparison](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.569--5.0.570/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.569--5.0.570/diff.patch). Older assembly knowledge remains above; release history is in [[changelog-github-paypal-sdk-release]].

Comparison identity and hashes for `5.0.570`: [comparison manifest](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.569--5.0.570/comparison.json).

## Assembly update: `@paypal/sdk-release@5.0.571`

Released 2026-08-31; delta ingest 2026-10-04 after `5.0.570`, SHA `3a1548a1efda9e86a49c9bfe459e07917c14ece4`. All twelve direct component pins remain unchanged; the retained package edit is version-only.  Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.570 -> 5.0.571](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.570--5.0.571/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.570--5.0.571/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.570--5.0.571/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.572`

Released 2026-09-01; delta ingest 2026-10-04 after `5.0.571`, SHA `f0dd88b1e8e7d9b86fbe406501c7fc04b1903761`. Checkout Components advances `5.0.431` -> `5.0.432`; the other eleven direct pins remain unchanged.  Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.571 -> 5.0.572](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.571--5.0.572/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.571--5.0.572/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.571--5.0.572/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.573`

Released 2026-09-07; delta ingest 2026-10-04 after `5.0.572`, SHA `7597acd9ddb49fa50c9948252768401a987c4fb8`. Checkout Components `5.0.432` -> `5.0.433`; Messaging Components `1.95.1` -> `1.96.0`; other ten direct pins unchanged.  Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.572 -> 5.0.573](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.572--5.0.573/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.572--5.0.573/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.572--5.0.573/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.574`

Released 2026-09-09; delta ingest 2026-10-04 after `5.0.573`, SHA `5f04b0c4743893851fa6465a4ed14179d5024fbc`. Checkout Components `5.0.433` -> `5.0.434`; the other eleven direct pins remain unchanged.  Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.573 -> 5.0.574](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.573--5.0.574/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.573--5.0.574/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.573--5.0.574/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.575`

Released 2026-09-14; delta ingest 2026-10-04 after `5.0.574`, SHA `8924d8f8be85332d841d8a4dd527a0b1871996bd`. All twelve direct pins remain unchanged; the retained package edit is version-only.  Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.574 -> 5.0.575](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.574--5.0.575/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.574--5.0.575/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.574--5.0.575/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.576`

Released 2026-09-14; delta ingest 2026-10-04 after `5.0.575`, SHA `7f58511a2151384f823163b30699ec20adad1c61`. All twelve direct pins remain unchanged; the retained package edit is version-only.  Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.575 -> 5.0.576](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.575--5.0.576/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.575--5.0.576/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.575--5.0.576/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.577`

Released 2026-09-21; delta ingest 2026-10-04 after `5.0.576`, SHA `627d37cee3a23ba7b256eeff8f3e9ca425208465`. Checkout Components `5.0.434` -> `5.0.435`; Messaging Components `1.96.0` -> `1.97.0`; other ten direct pins unchanged.  Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.576 -> 5.0.577](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.576--5.0.577/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.576--5.0.577/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.576--5.0.577/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.578`

Released 2026-09-22; delta ingest 2026-10-04 after `5.0.577`, SHA `2e5394ce06e946b5e51b2aa34f201ecc9b5c5e48`. Common Components `1.0.60` -> `1.0.61`; the other eleven direct pins remain unchanged. Common Components implementation is absent from this capsule; its behavioral delta requires independent exact-version evidence. Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.577 -> 5.0.578](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.577--5.0.578/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.577--5.0.578/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.577--5.0.578/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.579`

Released 2026-09-28; delta ingest 2026-10-04 after `5.0.578`, SHA `da10cb8de5930be798cf44881a175c3c521326c2`. Common Components `1.0.61` -> `1.0.62`; Messaging Components `1.97.0` -> `1.98.0`; other ten direct pins unchanged. Common Components behavior requires independent exact-version evidence; Messaging behavior remains owned by [[source-github-paypal-messaging-components]]. Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.578 -> 5.0.579](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.578--5.0.579/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.578--5.0.579/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.578--5.0.579/diff.patch). Earlier version knowledge is preserved.

## Assembly update: `@paypal/sdk-release@5.0.580`

Released 2026-09-29; delta ingest 2026-10-04 after `5.0.579`, SHA `27aa46b6623c9b20a74d5c58ce060be25be68dc4`. Checkout Components `5.0.435` -> `5.0.436`; the other eleven direct pins remain unchanged. Common remains `1.0.62`, Messaging remains `1.98.0`. Only `package.json` differs in the retained eleven-file capsule; the other ten files, development dependencies, scripts and engine requirements are unchanged. No GitHub release notes or merchant migration are established. Excluded lockfile/CDN changes remain an evidence gap.

Exact package and release evidence appears under Raw Sources; comparison: [5.0.579 -> 5.0.580](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.579--5.0.580/comparison.json), [details](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.579--5.0.580/comparison.md), [patch](tracking/github/repos/paypal/paypal-sdk-release/comparisons/sdk-release/5.0.579--5.0.580/diff.patch). Earlier version knowledge is preserved.

## Upgrade, publish, and deployment flow

The README exposes add, upgrade, remove, release, and activation operations. It explicitly warns that release triggers npm publication and production deployment, while activation moves a published version into traffic and supports selecting a prior version for rollback.

> [!warning] Upstream activation contradiction
> The README instructs operators to run `npm run activate` and `npm run activate x.x.x`, but the retained `package.json` defines no `activate` script. The capsule therefore establishes the documented operational intent, not an executable activation command at `5.0.569`; live operational tooling may exist outside the retained repository evidence.

The scheduled deployment workflow runs each Monday at `19:00` UTC and can also be dispatched manually. It reinstalls dependencies, optionally upgrades one filtered package, rejects filters outside the `@paypal/` namespace, pins `@krakenjs/zoid` during the scheduled upgrade, and invokes the package release command with npm credentials.

Separate workflows provide:

- pull-request and main-branch validation through `npm test`;
- a release dry run;
- manual dependency upgrade without the scheduled Zoid rejection;
- lockfile regeneration and commit; and
- manual npm publication after checking that SDK logo assets are available on the PayPal CDN.

The logo check reads the resolved `@paypal/sdk-logos` version from the lockfile and requests `paypal-default.svg` from the corresponding versioned CDN directory. Because the lockfile is outside this capsule, the exact logo version used by `5.0.569` is an explicit evidence gap.

## Version-qualified use

Use this repository first when a question asks which component versions formed a specific PayPal SDK release or how PayPal's release assembly was promoted. Then consult the independently versioned component source and changelog for implementation details. At initial baseline ingestion, the `5.0.569` manifest pinned Checkout Components `5.0.428`, while the then-local checkout-components source ended at `5.0.425`; that older snapshot did not establish behavior introduced in `5.0.426` through `5.0.428`. This is historical collection context, not the current endpoint of the independently maintained component history.

For future `@paypal/sdk-release` updates, compare `package.json` first. A component-version change identifies which independent repository may need recollection, but it does not itself establish the component's implementation delta.

## Related

- Company: [[paypal]]
- Concept: [[paypal-checkout]]
- Release history: [[changelog-github-paypal-sdk-release]]
- Checkout runtime: [[source-github-paypal-checkout-components]]
- JS loader and React wrappers: [[source-github-paypal-js]]
- SDK artwork: [[source-github-paypal-sdk-logos]]

## Raw Sources

- `5.0.580`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-27aa46b/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-27aa46b/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.580/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.580/2026-10-04/release-notes.md).
- `5.0.579`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-da10cb8/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-da10cb8/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.579/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.579/2026-10-04/release-notes.md).
- `5.0.578`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-2e5394c/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-2e5394c/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.578/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.578/2026-10-04/release-notes.md).
- `5.0.577`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-627d37c/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-627d37c/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.577/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.577/2026-10-04/release-notes.md).
- `5.0.576`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-7f58511/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-7f58511/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.576/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.576/2026-10-04/release-notes.md).
- `5.0.575`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-8924d8f/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-8924d8f/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.575/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.575/2026-10-04/release-notes.md).
- `5.0.574`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-5f04b0c/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-5f04b0c/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.574/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.574/2026-10-04/release-notes.md).
- `5.0.573`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-7597acd/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-7597acd/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.573/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.573/2026-10-04/release-notes.md).
- `5.0.572`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-f0dd88b/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-f0dd88b/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.572/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.572/2026-10-04/release-notes.md).
- `5.0.571`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-3a1548a/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-3a1548a/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.571/2026-10-04/manifest.json), [notes](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.571/2026-10-04/release-notes.md).
- `5.0.570`: [snapshot](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-0fcbea2/manifest.json), [package](raw/github/paypal/paypal-sdk-release/snapshots/2026-10-04-0fcbea2/files/package.json), [release](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.570/2026-10-04/manifest.json), [note record](raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.570/2026-10-04/release-notes.md).
- Snapshot manifest: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/manifest.json`
- Release manifest: `raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.569/2026-08-21/manifest.json`
- Release-note record: `raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.569/2026-08-21/release-notes.md`
- Package manifest: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/package.json`
- README: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/README.md`
- Wrapper entry point: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/index.js`
- Deployment workflow: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/deploy.yml`
- Publication workflow: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/publish.yml`
