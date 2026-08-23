---
title: "GitHub: paypal/paypal-sdk-release"
type: source
date_ingested: 2026-08-21
original_format: github-repo
raw_files:
  - "github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/manifest.json"
tags: [paypal, javascript-sdk, release-automation, dependency-manifest, github-repository]
---

## Overview

`paypal/paypal-sdk-release` is the assembly and release repository for a combined PayPal and Braintree browser SDK bundle. This cumulative page starts with package-qualified baseline `@paypal/sdk-release@5.0.569` at exact SHA `71e5116c56355a60bc8af337720116047d4d6ab8`.

Repository: <https://github.com/paypal/paypal-sdk-release>

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

Use this repository first when a question asks which component versions formed a specific PayPal SDK release or how PayPal's release assembly was promoted. Then consult the independently versioned component source and changelog for implementation details. For example, this manifest pins Checkout Components `5.0.428`, while the current local checkout-components source page ends at `5.0.425`; behavior introduced only in `5.0.426` through `5.0.428` is not established by the older component snapshot.

For future `@paypal/sdk-release` updates, compare `package.json` first. A component-version change identifies which independent repository may need recollection, but it does not itself establish the component's implementation delta.

## Related

- Company: [[paypal]]
- Concept: [[paypal-checkout]]
- Release history: [[changelog-github-paypal-sdk-release]]
- Checkout runtime: [[source-github-paypal-checkout-components]]
- JS loader and React wrappers: [[source-github-paypal-js]]
- SDK artwork: [[source-github-paypal-sdk-logos]]

## Raw Sources

- Snapshot manifest: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/manifest.json`
- Release manifest: `raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.569/2026-08-21/manifest.json`
- Release-note record: `raw/github/paypal/paypal-sdk-release/releases/sdk-release/5.0.569/2026-08-21/release-notes.md`
- Package manifest: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/package.json`
- README: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/README.md`
- Wrapper entry point: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/index.js`
- Deployment workflow: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/deploy.yml`
- Publication workflow: `raw/github/paypal/paypal-sdk-release/snapshots/2026-08-21-71e5116/files/.github/workflows/publish.yml`
