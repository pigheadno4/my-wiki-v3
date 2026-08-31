---
title: "GitHub: braintree/uuid"
type: source
date_ingested: 2026-08-31
original_format: github-repo
raw_files:
  - "github/braintree/uuid/snapshots/2026-08-31-d134a2c/manifest.json"
tags: [braintree, uuid, javascript, web-crypto, secure-random, github-repository]
---

## Overview

`@braintree/uuid@2.0.0` is the first retained exact-SHA baseline for Braintree's small CommonJS UUID v4 utility. Braintree describes it as shared by its JavaScript SDK ecosystem; the retained implementation exposes one zero-argument function that returns a UUID string.

This package generates identifiers only. It does not create a payment resource, provide idempotency semantics, tokenize payment data, establish merchant or buyer eligibility, or process a transaction.

## Baseline and Package Boundary

The retained package resolves to tag `v2.0.0` at SHA `d134a2ca93d12705a76ff036baeba568016f9b13`, dated 2026-01-20. Its package entry point is `index.js`, its declaration exposes `uuid(): string`, and its manifest declares only development dependencies.

The README names `braintree-web`, `braintree-web-drop-in`, and `framebus` as consumers. Exact consumer behavior remains version-qualified: retained `braintree-web@3.144.0` pins `@braintree/uuid@2.0.0`, while retained `braintree-web-drop-in@1.47.0` pins `@braintree/uuid@1.0.1` and therefore cannot inherit this v2 implementation.

## UUID Generation

The exported function follows this sequence:

1. If global `crypto.randomUUID` exists, call it and return its result.
2. If that call is unavailable or throws, use global `crypto.getRandomValues` to fill 16 bytes.
3. Set the UUID version nibble to v4 and the variant bits on the random bytes, then render the conventional hyphenated hexadecimal form.
4. If neither secure API is available, throw `@braintree/uuid: No secure random source available`.

There is no `Math.random()` fallback. The module also does not import Node's `crypto` module; the runtime must expose a compatible global `crypto` API.

## Grounding Excerpts

> "A simple node js implementation of uuid v4 for use with Braintree's JS based SDKs."
>
> `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/README.md:3`

> "return crypto.randomUUID();"
>
> `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/index.js:7`

> "crypto.getRandomValues(bytes);"
>
> `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/index.js:16`

> "throw new Error('@braintree/uuid: No secure random source available');"
>
> `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/index.js:33`

## Release and Evidence Boundaries

The repository changelog describes `2.0.0` as an update to a "robust v4 implementation" and also records development-tool and repository Node-version updates. No exact v1 snapshot or comparison is retained, so the prior generation algorithm and the precise compatibility impact of upgrading from `1.0.1` are not established by this source.

The release record has no upstream release-note body. Tests and tooling are excluded from the capsule, so this evidence establishes implementation structure but not observed cross-browser or Node-version compatibility.

> [!warning] License metadata conflict
> The retained `LICENSE` contains the MIT License, while `package.json` declares `"license": "ISC"`. Preserve both source-scoped statements; this repository evidence does not resolve which metadata governs a distributed package artifact.

## Related

- [[changelog-github-uuid]] - package-qualified release ledger
- [[braintree-web-sdk]] - modular browser SDK that pins UUID `2.0.0` in the retained release
- [[braintree-web-drop-in]] - prebuilt UI that pins UUID `1.0.1` in the retained release
- [[braintree]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/manifest.json`
- Release manifest: `raw/github/braintree/uuid/releases/uuid/2.0.0/2026-08-31/manifest.json`
- Release notes: `raw/github/braintree/uuid/releases/uuid/2.0.0/2026-08-31/release-notes.md` (upstream body unavailable)
- Repository changelog: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/CHANGELOG.md`
- README: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/README.md`
- Runtime implementation: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/index.js`
- Type declaration: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/index.d.ts`
- Package metadata: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/package.json`
- License: `raw/github/braintree/uuid/snapshots/2026-08-31-d134a2c/files/LICENSE`
