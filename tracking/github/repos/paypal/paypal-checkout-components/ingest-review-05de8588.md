# Checkout Components 5.0.436 ingest review

Date: 2026-10-04
Work item: `github-05de85883ddb6e597928`
SHA: `5b2afe08b007bd026083492b8242d65047b7d3b8`
Release: `@paypal/checkout-components@5.0.435` -> `@paypal/checkout-components@5.0.436`
Mode: user-approved delta, inline serial ingest.

## Reading authorization and evidence

The user approved the proposed item-specific focused-reading exception: read the changed authored implementation and affected prior code completely; mechanically check generated bundle evidence, manifest inventories and unchanged cumulative raw history. This does not authorize semantic claims from unread generated code or a whole-repository/full-assigned-reading claim.

- [x] Read the complete cumulative wiki source and changelog before writing, both complete Pay Later configurations and package manifests, release metadata, packet/comparison metadata and authored patch sections. Read the new raw changelog prefix fully; verified the complete prior raw changelog as an identical suffix.
- [x] Verify both complete manifest inventories and all 214 prior plus 214 current files by size, SHA-256 and Git blob ID. Current capsule: 1,511,791 bytes; prior: 1,511,531 bytes. Four retained modifications and 210 unchanged paths; no retained additions/removals. Packet Markdown, snapshot manifest, comparison Markdown and full comparison patch hashes match.
- [x] Review all five upstream dispositions. Generated `dist/test/button.js` remains intentionally excluded from the raw capsule; its comparison evidence is not test execution.
- [x] Grounding gate: current `src/funding/paylater/config.jsx:59`, `:60`, `:62`, `:65-66` supplies the Canadian variant, French language, changed label and later override. `CHANGELOG.md:3` records the release intent.
- [x] Mode review: bounded label substitution; package JSON changes only version. No dependency or public-export change, evidence gap or unclassified retained change. Delta remains appropriate.
- [x] Concept audit and updates before source writing: existing Pay Later and Checkout concepts updated; no new concept required.
- [x] Add cumulative source and chronological changelog sections, preserving prior knowledge.
- [x] Update company, provider index and logs; comparison/contradiction audit. No new source page, so source_count unchanged. No substantive cross-company comparison. Existing Canadian product tables concern documented offers, not this runtime label; no new cross-page contradiction identified. Prior accessibility/retry warnings remain untouched.
- [x] Focused validation, historical preservation and terminal completion. Six schema-bearing wiki pages pass validation; separate local Markdown/wikilink checks cover all eight touched wiki pages (818 wikilinks). All 11 historical version sections and all earlier changelog release entries are preserved verbatim. `git diff --check` passes. Pre-completion collection validation passes: 152 snapshots, 137 release records, 95 comparisons and 151 work items. Completion returns `ingested` at the approved SHA/mode.

## Findings and limits

The sole authored implementation edit changes the eligible `paylater` product's Canadian French label from `Payer en 4` to `Payer plus tard`. Independent later conditions can overwrite it: any eligible `payIn4` assigns `Pay in 4`, and the French-product branch assigns `Payer en plusieurs fois`. Both legacy and rebranded Logo branches and the `labelText` property call the helper. This is conditional presentation, not a new offer, eligibility rule, financing term or merchant API.

The retained generated bundle has one new `Payer plus tard` literal and no remaining `Payer en 4` literal, with the corresponding CA/fr condition and later override in bounded inspected context. It changes beyond a simple label substitution plus scoped-style-ID normalization; no full generated-code semantic equivalence is claimed. An expensive token comparison was interrupted; hash, count, bounded context and inventory checks completed independently. No generated code, upstream tests or payment flow were executed.

Separate upstream release notes are unavailable (empty immutable notes record, `notes_available: false`); the raw changelog records September 29 release intent. Raw and packet evidence remain immutable. No build, browser/payment test, commit or push for this item.

Post-completion `validate_github_collection.py` also passes with the same counts and no structural errors. Final `git diff --check` passes.
