---
title: "PayPal Collection and Ingest Log"
type: log
tags: [paypal, github-repository, operations]
---

> PayPal-specific collection and ingest history. The root [[log]] keeps a concise cross-provider chronology.

## [2026-07-23] ingest | paypal/paypal-js coordinated `10.0.0` transition

- Approved and processed work item `github-bd7fe849961b5c6b9964` in full mode.
- Read and hash-verified the 171-file, 1,206,475-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-4bd05ab/manifest.json`; 89 tests were excluded and stories remained eligible.
- Ingested `@paypal/paypal-js@10.0.0` and `@paypal/react-paypal-js@10.0.0` as separate package releases sharing SHA `4bd05aba2f3263f0ea4694140dc71dfe1dd5b429`.
- Added the required v6 `environment` migration to [[paypal-checkout]], [[source-github-paypal-js]], and [[changelog-github-paypal-js]] while preserving all v8 and v9 knowledge.
- Kept the evidence boundary explicit: the release changes environment selection, not payment functionality, and does not establish a change to the separate Braintree provider.

## [2026-07-23] ingest | paypal/paypal-js v9 major transition

- Approved and processed work item `github-aa80084a50abf57e06d7` in full mode.
- Read and hash-verified the 198-file, 1,250,862-byte exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-31eb658/manifest.json`; 96 tests were excluded and stories remained eligible.
- Ingested `@paypal/paypal-js@9.8.0` and `@paypal/react-paypal-js@9.3.0` as separate package releases sharing SHA `31eb658ac885a490d38ef34e471c069b0c6e49cb`.
- Added v9 component, provider, eligibility, Card Fields, Google Pay, and Braintree knowledge to [[source-github-paypal-js]] and [[changelog-github-paypal-js]] without removing either v8 baseline.
- Created [[paypal-braintree-integration]] and updated [[paypal-checkout]], [[paypal-expanded-checkout]], [[paypal-google-pay]], and [[paypal-vault]].
- Corrected [[source-github-paypal-js-v6]]: v9 `PayPalProvider` does not automatically call `findEligibleMethods()`.

## [2026-07-23] ingest | paypal/paypal-js `@paypal/react-paypal-js@8.9.2`

- Approved and processed work item `github-b11f1f62c66a78b84806` in full mode.
- Read and hash-verified the 101-file exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-77487d6/manifest.json`; 36 tests were excluded and integration stories were retained.
- Updated [[paypal-expanded-checkout]] with React Card Fields callback-freshness behavior.
- Added the React v8 baseline to [[source-github-paypal-js]] and [[changelog-github-paypal-js]].
- Recorded the dependency move to `@paypal/paypal-js ^9.0.0` without marking that core package release as ingested.

## [2026-07-23] ingest | paypal/paypal-js `@paypal/paypal-js@8.4.2`

- Approved and processed work item `github-8416828e1141b2d896ea` in full mode.
- Read the exact-SHA capsule at `raw/github/paypal/paypal-js/snapshots/2026-07-22-702863f/manifest.json`, its 100 assigned files, and the package release notes.
- Updated [[paypal-checkout]] with package-qualified historical v6 evidence.
- Moved the cumulative source authority to `wiki/sources/paypal/github/source-github-paypal-js.md`.
- Created [[changelog-github-paypal-js]] as the separate release ledger.
- Recorded `@paypal/react-paypal-js@8.9.1` only as collateral repository context; no React release was ingested.
- Preserved the legacy v8 and later v6/v9 source pages as historical supporting evidence.
