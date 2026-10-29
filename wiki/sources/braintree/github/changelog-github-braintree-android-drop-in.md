---
title: "GitHub changelog: braintree/braintree-android-drop-in"
type: source
date_ingested: 2026-08-13
date_updated: 2026-10-29
original_format: github-repo
raw_files:
  - "github/braintree/braintree-android-drop-in/snapshots/2026-10-29-55fc0bd/manifest.json"
  - "github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/manifest.json"
  - "github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json"
tags: [braintree, android, mobile-sdk, drop-in, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-android-drop-in`. Cumulative implementation knowledge belongs in [[source-github-braintree-android-drop-in]] and the linked immutable snapshots.

## `default-branch@55fc0bd` (2026-10-20; ingested 2026-10-29)

Approved delta from `72c05861a0e903e19bc9baca8bc0740b0b1ed57c` to `55fc0bd3a43299af800a5d94a71f8c9853069818`. Default-branch tooling evidence only; stable `drop-in@6.17.0` and development `6.17.1-SNAPSHOT` identity remain distinct.

**Changes:** root Dokka buildscript/plugin declarations converge on 1.9.20; root and library doc-plugin configurations add jsoup 1.23.1/freemarker 2.3.35. Two old root publishing classpath entries are removed, not the remaining publishing plugin. Library test-only JUnit moves 4.13 -> 4.13.2. No globally forced dependency versions or verified resolved dependency graph is claimed.

**Unchanged:** Braintree modules 4.50.0, card form 5.4.0, AGP 7.2.2, Kotlin 1.7.10, API levels 34/21/35, version code 110 and 6.17.1-SNAPSHOT. No changes to payment code, public APIs, demos, README or raw changelog. No Android/build/doc-generation/device/payment execution or all-vulnerabilities-fixed claim.

**Policy qualification:** tooling maintenance occurs after the README's unchanged no-updates date; it does not establish revised lifecycle dates or renewed support. Reciprocal contradiction qualification recorded in the cumulative source and Android concept. All earlier release/ref history is preserved.

**Scope:** two changed/163 unchanged files in each 165-file capsule; all 330 size/SHA-256/Git blob identities verified. Both changed files and affected prior files, comparisons and cumulative wiki history read under approved focused reading; manifests/unchanged inventories mechanically checked and relevant shared sections read. All two upstream changes retained; no exclusions/gaps/unclassified changes. Existing concept first, then source/changelog/company/index/logs; source_count unchanged. No commit or push.

**Evidence:** [snapshot](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-29-55fc0bd/manifest.json), [root build](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-29-55fc0bd/files/build.gradle), [library build](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-29-55fc0bd/files/Drop-In/build.gradle), [comparison](../../../../tracking/github/repos/braintree/braintree-android-drop-in/comparisons/default-branch/72c0586--55fc0bd/comparison.json) and [patch](../../../../tracking/github/repos/braintree/braintree-android-drop-in/comparisons/default-branch/72c0586--55fc0bd/diff.patch). Five located excerpts are in [[source-github-braintree-android-drop-in]].

## `default-branch@72c0586` (2026-04-23; ingested 2026-10-20)

Approved delta from release SHA `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7` to `72c05861a0e903e19bc9baca8bc0740b0b1ed57c`. This is commit-qualified documentation/build evidence, not a new stable package release; `drop-in@6.17.0` remains the release baseline.

**Findings:** README adds deprecation on 2026-09-01, unsupported status on 2027-09-01, no updates after deprecation, one year of processing support and possible processing suspension once unsupported. It recommends the separate modular SDK. Corrects the invalid June 31, 2025 certificate warning to March 30, 2026 for Drop-in 5.4.2 through 6.15.0, with a 6.16.0+ upgrade instruction. Historical Inactive/future-tense wording is not a support extension after the scheduled date. Source and concept carry the contradiction callout.

**Metadata, not payment behavior:** project version becomes `6.17.1-SNAPSHOT`, version code 110; stable README dependency remains 6.17.0. Braintree module pin stays 4.50.0 and API levels stay 34/21/35. No changed payment implementation, public API, demo logic or changelog at this boundary. The old v5-to-v6 Drop-in migration guide is not a new modular replacement guide.

**Evidence caveat:** Git changes only README.md/build.gradle; packet stored hashes additionally differ for the migration guide because of prior local credential redaction and a trailing newline. That guide has the same upstream blob. Preserve these distinctions; do not infer credential rotation or migration changes. Raw remains immutable; credentials are not quoted in wiki prose.

**Reading and updates:** approved focused reading of all three assigned changed documents, affected prior files, complete cumulative source/changelog and comparison; mechanical manifest/hash verification plus relevant shared-page context. Both 165-file snapshots verified (330 stored hashes/sizes). Concept updated first; source/changelog, company, index and logs updated without adding sources or replacing any 6.17.0 history. No cross-company comparison, Android build, dependency resolution, app-switch or payment execution.

**Evidence:** [new snapshot](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/manifest.json), [prior snapshot](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json), [comparison](../../../../tracking/github/repos/braintree/braintree-android-drop-in/comparisons/default-branch/da8a702--72c0586/comparison.json) and [upstream patch](../../../../tracking/github/repos/braintree/braintree-android-drop-in/comparisons/default-branch/da8a702--72c0586/diff.patch). Exact documents and grounding excerpts are linked in [[source-github-braintree-android-drop-in]].

## `drop-in@6.17.0` (2025-04-21)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `drop-in` | Initial baseline | `6.17.0` | `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7` | Full |

**Exact release change:** All pinned `braintree_android` modules move to `4.50.0`. No new payment method or public Drop-in flow is documented for `6.17.0`.

**Developer or merchant impact:** This release remains on the Braintree Android v4 dependency line, requires API 21+, and should be used instead of pre-`6.16.0` builds affected by the repository's 2025 certificate warning. Do not infer behavior from the independently retained `braintree-android@5.30.0` modular source.

**Migration action:** Treat `6.17.0` as the first exact-SHA Android Drop-in baseline. Before moving the underlying modular SDK or adopting v5 behavior, verify a compatible Drop-in release or replace the prebuilt UI with a modular integration.

**Updated source sections:** Version and dependency boundary; launch and server handoff; payment methods and eligibility; vaulting; 3D Secure and risk data; redirect handling; release findings.

**Evidence boundary:** No prior exact-SHA Android Drop-in snapshot exists in the wiki. Historical repository changelog entries provide context but are not retained source comparisons.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/manifest.json`
- Release notes: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json`
- Repository changelog: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/CHANGELOG.md`
- Root build metadata: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/build.gradle`
- Library build metadata: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/Drop-In/build.gradle`
