---
title: "GitHub changelog: braintree/braintree-web-drop-in"
type: source
date_ingested: 2026-07-28
date_updated: 2026-09-20
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/manifest.json"
  - "github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/manifest.json"
tags: [braintree, drop-in, javascript-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-web-drop-in`. Cumulative implementation knowledge belongs in [[source-github-braintree-web-drop-in]] and the linked immutable snapshots.

## `braintree-web-drop-in@1.48.0` (2026-09-10)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-web-drop-in` | `1.47.0` | `1.48.0` | `5e6de786a463598b4583a657acbd5cafee72dbf9` | Delta |

**Important findings:** Card-label interpolation now converts `lastFour` to a number, stringifies it, takes its first four characters, and pads with zeros. `0012` and `0000` remain intact; overlong `123456` becomes `1234`; nonnumeric strings become `0NaN`. This is not strict digits-only validation. The enclosing view still uses `innerHTML`; other wallet label branches are unchanged.

**Developer or merchant impact:** A contained display-hardening update, not a new payment method or public API. Runtime dependencies remain unchanged, including `braintree-web@3.123.2` and `@braintree/uuid@1.0.1`. README CDN examples advance to `1.48.0`. Existing integration checks should include selected-card labels and leading zeros.

**History clarification:** The new cumulative upstream changelog adds "(where possible)" to the old `1.47.0` textContent statement. The original release history below and its immutable evidence are retained.

> [!warning] Contradiction: lifecycle evidence
> The September 10 release retains a README saying updates stop September 1, 2026, with unsupported status September 1, 2027. Do not infer a support extension or resolve the conflict from this release alone. [[source-github-braintree-web-drop-in]]

**Updated source sections:** Latest ingested boundary; card-label implementation and examples; lifecycle contradiction; immutable evidence navigation. Prior architecture and `1.47.0` findings remain intact.

**Evidence boundary:** All 13 assigned paths read fully; four retained files modified and 82 unchanged. Lockfile and unit tests remain policy-excluded as full files, but changed hunks are available in the comparison. Reviewed tests are not executed tests; no browser/payment validation or security advisory is established.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.48.0/2026-09-20/manifest.json`
- Notes: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.48.0/2026-09-20/release-notes.md`
- Snapshot: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/manifest.json`
- Comparison: `tracking/github/repos/braintree/braintree-web-drop-in/comparisons/braintree-web-drop-in/1.47.0--1.48.0/comparison.json`
- Diff: `tracking/github/repos/braintree/braintree-web-drop-in/comparisons/braintree-web-drop-in/1.47.0--1.48.0/diff.patch`
- Implementation: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/src/views/payment-method-view.js`
- README: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/README.md`
- Package: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/package.json`
- Upstream history: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/CHANGELOG.md`

## `braintree-web-drop-in@1.47.0` (2026-06-17)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-web-drop-in` | Initial baseline | `1.47.0` | `ec1c7c533c2e878545f2b25505c56b7e22dc1c17` | Full |

**Important findings:** The release tightens HTML escaping, replaces an error-message `innerHTML` assignment with `textContent`, adopts conventional commits, and announces scheduled deprecation on 2026-09-01 followed by unsupported status on 2027-09-01.

**Developer or merchant impact:** Existing integrations retain the prebuilt UI and nonce flow, but the repository directs merchants to migrate to the modular Braintree SDK before support milestones. Its notice says processing will be supported for one year after deprecation and may be suspended at any time after unsupported status. Custom translations and dynamic error text receive stronger output handling.

**Migration action:** Plan migration to Braintree Web rather than starting long-lived new Drop-in work. Do not assume separately collected `braintree-web@3.144.0` behavior is present: this release pins `braintree-web@3.123.2`.

**Updated source sections:** Initial architecture; payment methods; vaulted methods; 3D Secure and fraud data; localization; lifecycle and migration boundary.

**Evidence boundary:** This is the first retained Drop-in baseline, so no prior exact-SHA comparison exists. The full repository changelog provides historical context, while exact `1.47.0` changes come from the release notes and current source.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.47.0/2026-07-28/manifest.json`
- Release notes: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.47.0/2026-07-28/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/manifest.json`
- Repository changelog: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/CHANGELOG.md`
- README: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/README.md`
- Package manifest: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/package.json`
- Sanitizer: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/lib/sanitize-html.js`
