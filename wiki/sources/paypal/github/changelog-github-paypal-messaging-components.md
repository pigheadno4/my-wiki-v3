---
title: "GitHub changelog: paypal/paypal-messaging-components"
type: source
date_ingested: 2026-08-29
date_updated: 2026-09-20
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/manifest.json"
  - "github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/manifest.json"
  - "github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/manifest.json"
  - "github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/manifest.json"
tags: [paypal, pay-later, paypal-credit, messaging, changelog, github-repository]
---

## Overview

Package-qualified release history for `paypal/paypal-messaging-components`. Durable implementation behavior belongs in [[source-github-paypal-messaging-components]]; this page records version transitions and their evidence.

## `@paypal/messaging-components@1.97.0` (2026-09-17)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/messaging-components` | `1.96.0` | `1.97.0` | `39769bc09150879c1e85d3f5ae27a516279f652a` | Full additive, approved focused reading |

**Important findings:** Replaces the `view-edit-fi` page-type enum with `view-edit-funding-instrument`; introduces inline disclosure state and iframe presentation for flagged modal content; forwards link URLs to native-webview click callbacks; adds ES/IT borrowing-cost warning copy and layout adjustments; changes v2 default text size from 14px to 12px.

**Developer or merchant impact:** The removed page-type value now warns and resolves to undefined, without aliasing or throwing in that branch. Apple Wallet-named modal JSONs opt into inline disclosures through string `"true"`; any supplied view with the flag activates array-link interception. The supplemental component supplies a Back button and iframe, not merchant Apple Pay checkout or native-host implementation. ES/IT changes are presentation evidence, not legal-compliance or eligibility proof.

**Migration action:** Replace the old page-type string where used. Explicit v2 text size 14 remains accepted. Check narrow banners, inline-link accessibility wording and host disclosure behavior in runtime QA; source inspection is not evidence that those checks passed. The URL formatter rewrites selected HTTPS PayPal origins but returns other URLs unchanged, so do not treat it as a rejection allowlist. Package dependencies are unchanged.

**Updated source sections:** added `1.97.0` page type, disclosures and layout; updated latest/version-qualified navigation, Pay Later concept, company, provider index and logs. Preserved the `1.95.1` baseline and `1.96.0` section.

**Evidence boundary:** 2 added, 55 modified, zero removed and 653 unchanged retained files. User approved full mode after manual review found an incompatible enum change missed by the packet's public-API classifier. The focused-reading exception remains specific to this item: changed implementation/content and affected prior versions fully read; unchanged inventories/history hash-verified. Two separately approved exact-SHA supplemental files close the disclosure-component gap without modifying the snapshot or future policy. The stylesheet aggregation file, upstream tests and distributions remain excluded; no build, runtime, screen-reader, visual or deployed-behavior proof is claimed.

**Evidence:**

- Release record: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.97.0/2026-09-20/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.97.0/2026-09-20/release-notes.md`
- Snapshot: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.96.0--1.97.0/comparison.json`
- Comparison detail: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.96.0--1.97.0/comparison.md`
- Page-type validation: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/library/zoid/message/validation.js`
- Inline links: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/components/modal/v2/parts/InlineLinks.jsx`
- Supplement: `raw/github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/manifest.json`
- Disclosure component: `raw/github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/files/src/components/modal/v2/parts/Disclosure.jsx`
- Disclosure stylesheet: `raw/github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/files/src/components/modal/v2/styles/components/_disclosure.scss`
- Attachment: `tracking/github/repos/paypal/paypal-messaging-components/evidence-attachments/github-d20af06106d6d3e9a2b7/attachment.json`
- Review: `tracking/github/repos/paypal/paypal-messaging-components/ingest-review-d20af061.md`

## `@paypal/messaging-components@1.96.0` (2026-09-03)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/messaging-components` | `1.95.1` | `1.96.0` | `a682a8d6689f308155da4cca9521265d9e156b03` | Delta, approved focused reading |

**Important findings:** Calculator input-error relationships and empty-US-input labeling; localized loading announcements and busy state; decorative shimmers hidden from assistive technology; financing-plan headings; a PayPal/PayPal Credit logo text alternative in the legacy renderer. Adds US Apple Wallet-named Pay Monthly/Pay in 4 modal JSONs and v2 demonstration fixtures. Changes v2 flex height from `100%` to `100vh`.

**Developer or merchant impact:** More explicit accessibility semantics in authored source, not independently verified screen-reader behavior. Apple modal copy describes single-use virtual-card financing, not a merchant Apple Pay API or eligibility change. V2 fixture content is development evidence, not live product/market availability.

**Migration action:** No merchant API migration identified. Runtime dependencies remain unchanged; `jest-image-snapshot` changes from `^6.5.2` to an exact development pin `6.5.2`. Standalone demo guidance adds `features=useRenderV2Message`; supporting demo/test scripts are policy-excluded and were not run.

**Updated source sections:** added `1.96.0` accessibility/content delta and version-qualified use; updated Pay Later concept, PayPal company, provider index and logs. Prior `1.95.1` knowledge preserved.

**Evidence boundary:** 41 added, 25 modified, zero removed and 642 unchanged retained files. User-approved exception for this item: changed implementation/content and prior affected versions read fully; manifests and unchanged changelog history checked mechanically. No claim of complete upstream-repository reading, CSS visual parity, runtime testing or deployed behavior. At the time of this ingest, `1.97.0` remained queued; its subsequent ingest is recorded separately above.

**Evidence:**

- Release record: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.96.0/2026-09-20/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.96.0/2026-09-20/release-notes.md`
- Snapshot: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.95.1--1.96.0/comparison.md`
- Comparison manifest: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.95.1--1.96.0/comparison.json`
- Calculator: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/components/modal/v2/parts/Calculator.jsx`
- Logo text alternative: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/server/message/index.jsx`
- Apple modal: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/content/modals/US/PL2GO/apple_wallet_short_term.json`
- Review: `tracking/github/repos/paypal/paypal-messaging-components/ingest-review-c9338f57.md`

## `@paypal/messaging-components@1.95.1` (2026-08-25)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/messaging-components` | Initial baseline | `1.95.1` | `2bdaf940cdb0dcd29a8a3bc992eea975798d6d00` | Full |

**Important findings:** Established the first policy-controlled full baseline for the web Messaging Components runtime. The release filters qualifying offers before term sorting, validates numeric payment counts, makes country-specific sort direction explicit, preserves default APR disclaimer fallback, and guards modal event delivery when the target window is absent.

**Developer or merchant impact:** The changes make long-term offer ordering and disclaimer selection deterministic for already-returned offers and reduce a modal event failure. They do not alter or prove upstream buyer qualification, merchant enablement, or country availability.

**Migration action:** No API migration is identified. Consumers should keep package and combined-SDK versions separate: `@paypal/sdk-release@5.0.569` records Messaging Components `1.94.0`, while this independently released package baseline is `1.95.1`.

**Updated source sections:** merchant integration surface; message and modal lifecycle; rendering and style contracts; `1.95.1` offer processing; Pay Later concept and PayPal company summary.

**Evidence boundary:** This is an initial baseline with no prior managed snapshot comparison. The retained capsule excludes tests, and source-level Venmo logo rendering is not Venmo checkout or Pay Later eligibility evidence.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.95.1/2026-08-28/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.95.1/2026-08-28/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/manifest.json`
- Package manifest: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/package.json`
- Upstream changelog: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/CHANGELOG.md`
- Offer terms table: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/components/modal/v2/parts/TermsTable.jsx`
