# Adyen iOS Recheck - 2026-11-07

## Boundary and Result

User approved a recheck and findings before ingestion. No approve/claim/complete-ingest command, wiki edit, registry/budget/code change, commit or push was performed. Existing source/changelog/concept remain unchanged; last ingest stays 2026-10-15 at adyen-ios@5.26.0.

Online releases and exact Git tags identify 5.27.0 as the latest stable release. The 6.0.0-alpha.1 prerelease remains excluded by the existing major-5 stable policy; no untracked newer stable major was reported. Sources: https://github.com/Adyen/adyen-ios/releases and https://github.com/Adyen/adyen-ios/releases/tag/5.27.0.

Initial command permission review timed out before execution; the authorized retry ran. Routine future collection discovered a revised 5.26.0 note and 5.27.0, then stopped on the note-revision queue inconsistency described below. The existing exact-release command successfully collected 5.27.0 without changing policy.

## Collected 5.27.0

- Package: adyen-ios@5.27.0; released 2026-10-30T12:46:05Z.
- Exact SHA: 15167f660094853d204dc6cd25a068eddf1bc2b2.
- Work item: github-2e39da6002199c52091d, awaiting_approval, approved_mode null.
- Snapshot: raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/manifest.json.
- Release: raw/github/adyen/adyen-ios/releases/adyen-ios/5.27.0/2026-11-07/manifest.json and release-notes.md in that directory.
- Comparison: tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.26.0--5.27.0/comparison.json, comparison.md and diff.patch.
- Packet: tracking/github/repos/adyen/adyen-ios/ingest-packets/github-2e39da6002199c52091d/packet.json and packet.md.
- Current snapshot: 689 files / 2,136,123 bytes, 13 modified and 676 unchanged; no added/removed retained files. Prior snapshot: 689 files / 2,136,434 bytes.
- All 7,780 upstream dispositions reconcile: 13 retained, 7,767 intentional exclusions. No packet gaps or unclassified changes.
- Collection-time required reading: 22 paths / 619,549 bytes. Pure full-mode preflight (no state promotion) validates 698 paths / 2,677,239 bytes.

## Findings Before Ingestion

1. Store-payment toggle uses the native UISwitch as the labeled accessibility element, with the separate text label excluded. Removes the previous VoiceOver-status-dependent switch/container swapping. This is accessible presentation/activation wiring, not a change to server token storage or consent ownership.
2. Expiry/CVC format text is retained while editing, validating and resetting. Shared FormValidatableValueItemView assembles title, expected input format and the currently shown validation error. The new accessibilityInputFormat property is on an AdyenInternal SPI type, not a newly advertised merchant payment API. Expiry initialization also retains supplied localization parameters.
3. Card logo collection disables selection and, on iOS 15+, focus. Logo images receive an accessibility label and image trait. Billing-address and modal-toolbar titles acquire the header trait; the modal cancel button gets a localized cancel label even when a custom image is used.
4. Source-derived finding beyond the five release highlights: SubmitButton.accessibilityActivate checks enabled/user-interaction state, then dispatches touchUpInside. Loading already disables the control. This is code-level activation behavior, not proof of a successful VoiceOver/device/payment test.
5. Source-derived finding beyond the release highlights: CardScannerOverlayView creates its region-of-interest constraints once, updates a retained width constraint and clamps width with max(0, min(bounds.width, bounds.height) - 24). It updates the constraint before super.layoutSubviews and then publishes roiFrame. Do not infer measured performance or recognition-accuracy improvements.
6. The 5.27.0 release note now identifies this release as the final CocoaPods release, with future distribution through SPM/Carthage. Same-tag README still includes CocoaPods installation and Adyen.podspec bumps to 5.27.0. This is not proof that 5.27.0 is unavailable through CocoaPods or that published artifacts were installed. README minimums remain iOS 12, Xcode 15 and Swift 5.7. No retained Session/Apple Pay orchestration change or delegated dependency bump was found in this comparison.

## Revised 5.26.0 Notes and Queue Blocker

Original notes remain immutable at raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/release-notes.md. New notes were retained at the corresponding 2026-11-07 path, at the same da347498d07b843e5af3f9eb871376514ffdf38c SHA. Only the heading and CocoaPods notice change: the notice formerly attached to 5.26.0 is removed, while the iPhone Duo and implementation highlights remain. The notice now appears in 5.27.0. Preserve this dated correction rather than erase the former source claim.

Routine collector output: errors=["work-item state requires all applicable comparisons"], release_ids=["adyen-ios@5.26.0", "adyen-ios@5.27.0"]. Its state=ingested field refers to the existing accepted item and is not success for the new revision or 5.27.0 collection.

The draft revision packet is tracking/github/repos/adyen/adyen-ios/ingest-packets/github-03f5682f5c6d30579f8c/packet.json (plus Markdown), notes-only, from/to 5.26.0, same SHA, 689 unchanged files and an empty comparison_manifest. It has no persisted work item and must not be approved or described as queued.

Root-cause inspection: _publish_comparison_and_change in scripts/collect_github_repos.py intentionally omits a code comparison for a release-notes revision, while scripts/github_work_items.py:_validate_work_item rejects any populated from_version without a comparison at the later lifecycle boundary. Thus evidence publication succeeds before queue persistence fails. No fabricated comparison, weakened validation, manual queue mutation, deletion of accepted evidence or code patch was attempted. A bounded notes-revision repair and regression test need separate approval.

## Verification and Recommendation

- All 1,378 prior/current retained files pass size, SHA-256 and Git blob identity checks. Full-mode preflight validates packet/snapshot identities without approval or ingest state changes. Collection policies, original evidence and wiki pages are unchanged.
- Review covers the complete retained-code diff, release-note comparison, relevant README/distribution sections, complete changed toggle/validation/submit/scanner implementations and generated metadata/disposition inventories mechanically. The very large generated excluded-path inventory is not a claimed complete semantic reading of every assigned file or upstream repository. Approved ingest reading remains a separate gate.
- Pure transport optimization seeded 689 verified prior blobs only into the second collector's temporary Git object store to avoid redundant lazy fetches. An earlier seeding attempt stopped when the first collector closed its temporary clone. No retained file, selected scope or collector code was changed. No process remains running.
- Offline validation reports 14 structural errors: the existing 13 unrelated historical errors plus this new draft revision packet having no queue item. There is one pending item, 5.27.0. No error targets the 5.27.0 packet/snapshot. Do not call the complete collection globally clean.
- Script recommends full/high for 5.27.0; its security-keyword heuristic is not an independently established security advisory. Recommend retaining full additive mode for the shared form/activation changes, with separately approved focused reading of changed authored code and affected prior dependencies, mechanical checks of unchanged files/manifests, and preservation of all older history.

Next: approve a bounded repair/test for notes-only revision queueing, then review/regenerate that revision from retained evidence. Recommend notes-only delta for the revised 5.26.0 documentation first, followed by full additive 5.27.0 after separate ingest approval. No Swift/Xcode build, installation, device/VoiceOver or payment test was run.

Follow-up (separately approved repair): the notes-only queueing issue is repaired and the original draft packet was regenerated byte-identically from retained evidence, then atomically queued awaiting_approval with approved_mode null. No ingest or publication occurred. See notes-revision-repair-2026-11-07.md for regression proof, exact identities, updated validation and the remaining approval gate. Earlier blocker observations above record the original collection outcome, not the current queue state.
