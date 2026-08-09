---
title: "GitHub changelog: paypal/paypal-sdk-logos"
type: source
date_ingested: 2026-08-09
original_format: github-repo
raw_files:
  - "github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/manifest.json"
  - "github-paypal-sdk-logos.md"
tags: [paypal, logos, svg, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal/paypal-sdk-logos`. Durable rendering behavior and implementation details belong in [[source-github-paypal-sdk-logos]]; this page records version transitions and their evidence.

## Repository baseline: `default-branch@4c39c1e` (2026-04-22)

| Identity | Package | Exact SHA | Ingest mode |
| --- | --- | --- | --- |
| `default-branch@4c39c1e` | `@paypal/sdk-logos@2.3.7` | `4c39c1ec50b15dde3af99b524fb24ec8aa9fa11b` | Full |

**Important change:** Established the first policy-controlled public-source capsule while preserving the legacy `2.3.3` generated-SVG evidence. The retained upstream changelog advances through four generated-CDN releases and records whitespace refinements for general logos, Venmo, and the PP monogram. Current source adds badge constants/components and the PayPal Credit rebrand logo identity compared with the retained `2.3.3` constants.

**Developer or merchant impact:** Consumers can target the versioned `2.3.7` CDN path and use the current inline/external rendering surface. Geometry changes may affect visual spacing. The repository does not establish merchant eligibility, payment-method availability, or permission to use protected marks.

**Migration action:** Pin CDN URLs to the intended package version, visually verify layouts affected by logo whitespace, and test requested color variants because unsupported colors fall back to `default`. Apply applicable PayPal and payment-brand usage requirements separately.

**Updated source sections:** rendering API; CDN and color behavior; current logo surface; version-qualified history; implementation and evidence boundaries.

**Evidence:**

- [Snapshot manifest](../../../../raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/manifest.json)
- [Upstream changelog](../../../../raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/CHANGELOG.md)
- [Current constants](../../../../raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/src/constants.js)
- [Rendering components](../../../../raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/src/lib/components.jsx)
- [CDN utility behavior](../../../../raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/src/lib/util.js)

### Included package sequence

| Version | Date | Retained upstream change |
| --- | --- | --- |
| `2.3.7` | 2026-04-22 | Removed PP-monogram whitespace and regenerated CDN packages |
| `2.3.6` | 2026-04-20 | Updated Venmo whitespace and regenerated CDN packages |
| `2.3.5` | 2026-04-17 | Removed or updated logo whitespace and regenerated CDN packages |
| `2.3.4` | 2026-04-16 | Regenerated CDN packages |
| `2.3.3` | 2026-04-03 | Historical generated-CDN baseline retained locally |

### Evidence boundary

This work item is a default-branch commit baseline, not a package release record. Package `2.3.7` is read from the pinned source manifest and changelog. Exact generated `2.3.7` CDN SVG files are outside the capsule; the exact generated `2.3.3` set remains available in the legacy raw collection.

## Historical baseline: `@paypal/sdk-logos@2.3.3` (2026-04-03)

The earlier wiki ingest retained commit `bb24f9b`, four source/reference files, and 117 generated SVGs. It established the versioned CDN filename convention, color constants, card/payment-method inventory, and principal rebrand families.

This history remains part of the cumulative source. The 2026-08-09 full ingest adds `2.3.7`; it does not refresh away or reinterpret the exact `2.3.3` assets.

**Evidence:**

- [Legacy collection stub](../../../../raw/github-paypal-sdk-logos.md)
- [Legacy constants](../../../../raw/github-paypal-sdk-logos/src/constants.js)
- [Legacy logo index](../../../../raw/github-paypal-sdk-logos/src/logos/index.js)
- Generated files: `raw/github-paypal-sdk-logos/cdn/2.3.3/`
