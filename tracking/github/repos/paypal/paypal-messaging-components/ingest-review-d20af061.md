# Messaging Components 1.97.0 ingest review

Work item: `github-d20af06106d6d3e9a2b7`. Package: `@paypal/messaging-components@1.97.0`.
SHA: `39769bc09150879c1e85d3f5ae27a516279f652a`; prior `1.96.0` SHA: `a682a8d6689f308155da4cca9521265d9e156b03`.

## Approval and reading boundary

The user approved full additive ingest after review identified an incompatible `pageType` enum rename, overriding the immutable packet's delta recommendation. The user separately approved focused reading for this release: complete changed implementation/content and affected prior versions, with unchanged evidence and historical changelog verified mechanically. This is not a claim to have reread the entire repository or every unchanged current file.

All 57 changed retained paths were reviewed: 56 complete current files and the new CHANGELOG section, plus prior affected versions. Both cumulative wiki pages, release record/notes, comparison Markdown and complete patch were read. Structured packet/comparison inventories and excluded test/distribution inventories were inspected mechanically. The original packet has 49 required paths; full-mode expansion does not cancel the user's focused-reading exception.

The user also approved two exact-SHA supplementary files: `src/components/modal/v2/parts/Disclosure.jsx` and `src/components/modal/v2/styles/components/_disclosure.scss`. Both and their manifest were read completely. The canonical attachment is `tracking/github/repos/paypal/paypal-messaging-components/evidence-attachments/github-d20af06106d6d3e9a2b7/attachment.json`. It links `raw/github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/manifest.json`; original snapshot and future policy are unchanged.

Affected unchanged dependencies read include `src/library/zoid/message/component.js`, `src/server/v2/validateStyle.js`, and `src/utils/sdk.js`. The stylesheet aggregation file remains excluded; no build/runtime or stylesheet-wiring proof is claimed.

## Grounding excerpts

Paths below are relative to current snapshot `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/`, except the explicitly named supplement.

1. `src/library/zoid/message/validation.js`, pageType options: `'view-edit-funding-instrument'`. Prior equivalent: `'view-edit-fi'`; invalid options warn and return undefined.
2. `src/components/modal/v2/parts/InlineLinks.jsx`: `views.some(view => view?.meta?.useInlineDisclosure === 'true')`.
3. Supplement `Disclosure.jsx`: `<iframe className="disclosure-view__frame" src={url} title={backButtonLabel} />`.
4. `content/messages/IT/short_term_q.json`: `Attenzione! Prendere in prestito denaro comporta dei costi.`
5. `src/server/v2/validOptions.js`: `size: [Types.NUMBER, [12, 10, 11, 13, 14, 15, 16]],`.

## Integrity and dispositions

- All 708 prior and 710 current snapshot file hashes verified. Comparison: 2 added, 55 modified, 0 removed, 653 unchanged.
- Prior manifest SHA-256: `6d606e5a2262f85f26b494fefd0ffe818768c481c92f4dde2f69d7116c99b73e`.
- Current manifest SHA-256: `d9802c928f7e96ed56afae85d8fe6e3f4abfd380ddbbe05c1d0a40001af40349`.
- Historical CHANGELOG suffix from 1.96.0 onward is byte-identical. Packet Markdown, comparison Markdown, patch and release-note hashes verified.
- Supplement JSX SHA-256: `f9149611cbf7d6245f0b6a5c445d56043b521880ce545741bc0ae1ff9ecba6e0`.
- Supplement SCSS SHA-256: `3aab3113c5e54c536d46f9f6b4db5c4ff7e5284c8fbadc97f27243d8ddd42c15`.
- Upstream dispositions: 57 retained, 497 excluded tests, 116 excluded distribution files, 3 excluded implementation files. Two implementation gaps are addressed by the approved supplement; the style aggregation file remains outside the evidence boundary.
- Packet reports no public API changes, but manual review identifies the enum migration. Preserve the packet and explain the full-mode override; do not alter classifier policy in this ingest.
- Package manifest changes version only. Demo account changes are commented-example formatting, not newly enabled accounts.

## Checklist

- [x] Read evidence and extract grounding quotes under the approved exception.
- [x] Concept audit and concept-first update: existing Pay Later concept updated; no new product concept needed.
- [x] Add source and separate changelog; preserve older knowledge.
- [x] Update company without increasing source count: 177 retained.
- [x] Check concepts and cross-company comparison need: no new concept or comparison warranted.
- [x] Check version-qualified contradictions and evidence limits: old/new pageType explicitly distinguished; no availability or runtime claims; historical 1.96.0 queue note dated in changelog.
- [x] Update provider index.
- [x] Update provider and root logs.
- [x] Validate touched pages, evidence, links and historical preservation: five schema-bearing pages pass validate_wiki; links across all seven touched pages and 102 GitHub evidence references resolve; committed 1.95.1 core source sections/changelog preserved verbatim and 1.96.0 retained; catalogs unique; git diff --check passes. GitHub validator passes with 115 snapshots, 100 release records, 57 comparisons and 114 work items.
- [x] Complete only this work item: `github-d20af06106d6d3e9a2b7` is `ingested`, approved mode `full`, with linked immutable supplement. Post-completion GitHub validation passes.

No merchant eligibility, legal compliance, Apple Pay checkout enablement, browser accessibility, native-host presentation or deployed behavior is established by this source review. No commit or push is included.
