# Adyen iOS Serial Ingest - 2026-11-07

## Authorization and Order

User approved notes-only delta 5.26.0 first, followed by full additive 5.27.0 with focused reading, preserving all history. No commit/push is authorized. Process one item to completion and validation before claiming the next; unrelated shared-file changes remain untouched.

## 5.26.0 Notes Revision: Grounding Before Edits

Claimed github-03f5682f5c6d30579f8c as delta. Exact SHA da347498d07b843e5af3f9eb871376514ffdf38c and 689 retained files are unchanged. Read complete cumulative source/changelog, old/new release notes and new release record; parsed the complete structured snapshot manifest and verified every retained file's size, SHA-256 and Git blob identity. Required reading consists of these five assigned paths; no changed implementation is inferred from the inventory.

Three verbatim anchors:

1. `This is the **last release available through CocoaPods**.` - original raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/release-notes.md:6 (excerpt).
2. `> **iPhone Duo**` - revised raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-11-07/release-notes.md:2.
3. `> * This release supports **iPhone Duo**.` - same revised notes, line 4.

Full old/new comparison shows removal of the CocoaPods paragraph and its heading qualifier, with all implementation highlights unchanged. Concept audit: existing adyen-ios-sdk owns the distribution contradiction; add a dated clarification there first. No new source/concept/cross-company comparison or source-count change is warranted. Do not ingest the 5.27.0 source claims as part of this notes-only unit.

## 5.27.0 Grounding Before This Version's Edits

Claimed github-2e39da6002199c52091d as full only after the notes delta passed five-page wiki validation, baseline-preservation/locator/whitespace checks and completed ingested/delta. Effective full assignment: 698 paths / 2,680,926 bytes after the notes correction expanded cumulative context.

Read all 13 modified retained files completely (including README and podspec), complete cumulative source/changelog, release record/notes, retained diff and affected prior implementations. Read the retained FormItemView/FormValueItemView dependencies and affected FormTextItemView accessibility/reset sections. Mechanically verify unchanged files, generated inventories and duplicated diff/reference content under the approved focused-reading exception; do not claim a full upstream-tree read. Prior/current 1,378 file sizes, SHA-256 and Git blob identities pass; 13 changed / 676 unchanged, all 7,780 upstream dispositions reconcile (13 retained, 7,767 excluded), no packet gaps or unclassified changes.

Five verbatim anchors in snapshot 2026-11-07-15167f6/files, except the release-note quote:

1. `switchControl.accessibilityLabel = item.title` - Adyen/UI/Form/Items/Toggle/FormToggleItemView.swift:39.
2. `public var accessibilityInputFormat: String? {` - Adyen/UI/Form/Items/Value/Validatable/FormValidatableValueItemView.swift:19; enclosing type is AdyenInternal SPI, not a new merchant payment API.
3. `guard isEnabled, isUserInteractionEnabled else { return false }` - Adyen/UI/Views/SubmitButton.swift:126.
4. `roiWidthConstraint.constant = max(0, min(bounds.width, bounds.height) - (padding * 2))` - AdyenCardScanner/Sources/CardScannerOverlayView.swift:103.
5. `This is the **last release available through CocoaPods**.` - raw/github/adyen/adyen-ios/releases/adyen-ios/5.27.0/2026-11-07/release-notes.md:5 (excerpt).

Concept audit: extend existing adyen-ios-sdk first; retain prior architecture, all dated correction history and independent dependency/wrapper boundaries. No new concept or cross-company comparison is warranted.

## Progress

- 5.26.0 notes revision: concept-first edits validated; ingested/delta before claiming the second item. All original source/changelog lines remain in order; exact evidence locators pass.
- 5.27.0: full additive concept-first promotion complete, five-page wiki validation passes, item completed ingested/full after the first item's terminal state. Prior source/changelog history remains in order (latest-navigation pointer updated); exact evidence locators and provider-index/root-log links/placeholders pass. Scoped whitespace checks pass.
- Publication: not authorized.

## Self-Review and Counts

Reviewed new source/ledger/concept claims against the changed implementations: SPI property is not presented as a merchant API; format-label construction is distinguished from CVC sanitization; submit activation is bounded by enabled/interactive state, not a duplicate-payment guarantee; scanner changes are not measured performance/recognition claims. Current distribution wording is separated from original dated statements and registry availability. No device/VoiceOver, Xcode, package-install, compliance or payment execution is claimed.

Both items are ingested in the approved serial order. All original source/changelog content remains except the updated latest-navigation pointer; all prior implementation facts and raw captures are preserved. Company source_count stays 3206. Reconciled distinct ingested repository/release identities to 30: previous 27 plus the two already-ingested Android releases and this new iOS release. The notes revision adds no release identity. Historical company checkpoint explicitly labeled by date rather than left as stale latest guidance.

Only wiki/tracking work changed during these ingests. The preceding repair's test results remain in notes-revision-repair-2026-11-07.md: focused 150-test suite passes; full suite 829/834 with four baseline registry mismatches and one unresolved full-suite-only Stripe test discrepancy. No further code change or claim that the full suite is green. Final offline GitHub validation reports exactly the same 13 unrelated historical errors, no Adyen iOS/notes-revision errors and zero pending items. Scoped wiki/link/raw/history/count/whitespace checks pass. Publication remains a separate approval gate; no commit/push performed.
