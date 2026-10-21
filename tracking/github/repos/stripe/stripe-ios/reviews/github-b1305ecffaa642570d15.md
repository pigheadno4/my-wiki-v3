# Stripe iOS 26.15.0 ingest review

- Work item: `github-b1305ecffaa642570d15`.
- Exact SHA: `19c1d05439595535f0722e67e4847aece4faf4b2`.
- User-approved full additive ingest, serially after terminal completion of 26.14.0; all historical knowledge preserved.
- Same explicit focused-reading authorization for both releases: changed implementation, affected prior code, supplemental source, release notes and cumulative wiki history; unchanged source/history, generated inventories and duplicated diff verified mechanically. No whole-repository/fresh unchanged-source reading claim.
- Both 300-file snapshots verified by hash/size; 27 modifications and 273 unchanged files. Effective full list: 319 paths. 180 upstream changes: 27 retained, 153 intentional policy exclusions.
- Eight-file canonical supplement attachment verified: result type, localized card-preview forwarding, Identity image helper/uploaders/native coordinator, sheet resolver/presentation helper.
- Concept audit: existing stripe-ios-sdk and stripe-crypto-onramp updated first. No new broad concept or cross-company comparison.
- Grounding excerpts in cumulative source: plural KYC signature; deferred completeWithoutConfirmingIntent return; server-livemode uploader flag; document placeholder selection; resolver initialization. Exact quote strings checked against raw.
- Important qualifications: remaining ordinary Radar API is not removed; test image substitution does not prove zero camera/metadata/PII handling; final funding formatter, placeholder binary assets, concrete containers/factory, backend KYC and transport internals remain excluded. Device override is compiled out at this SHA despite nearby comment. No SDK/device/payment execution.
- Historical changelog: 2226 -> 2241 lines, 15 inserted, zero removed; six retrospective Identity lines are not newly introduced 26.15.0 functionality. All old wiki sections/references preserved.
- Validation result: six touched schema-bearing wiki pages pass validate_wiki; both linked attachments and collection index pass; exact raw grounding quote strings and historical section/raw-reference preservation pass; provider index has one current 26.15.0 entry per relevant page and source_count stays 666. git diff --check passes. Global GitHub validation reports only the same twelve unrelated historical packet-budget errors, no Stripe iOS error. Provider index has no YAML frontmatter by existing convention; its entries were checked separately rather than changing that unrelated convention.
