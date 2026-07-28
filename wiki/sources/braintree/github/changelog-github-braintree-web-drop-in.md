---
title: "GitHub changelog: braintree/braintree-web-drop-in"
type: source
date_ingested: 2026-07-28
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/manifest.json"
tags: [braintree, drop-in, javascript-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-web-drop-in`. Cumulative implementation knowledge belongs in [[source-github-braintree-web-drop-in]] and the linked immutable snapshots.

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
