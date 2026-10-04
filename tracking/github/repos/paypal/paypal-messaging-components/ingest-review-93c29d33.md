# Messaging Components 1.98.0 ingest review

- Item: `github-93c29d339b648ea8820e`.
- Approved scope: additive full ingest, inline, with focused reading. Changed implementation/content and affected prior code must be read completely; unchanged inventories and cumulative history may be checked mechanically.
- Exact release: `@paypal/messaging-components@1.98.0`, SHA `a639ec71494d3278684f5896017a426ed1fbfcd1`.
- Prior release: `1.97.0`, SHA `39769bc09150879c1e85d3f5ae27a516279f652a`.
- Commit/push: not authorized for this ingestion.

## Checklist

- [x] Read complete existing cumulative source and changelog.
- [x] Verify current/prior snapshot files, packet and comparison hashes.
- [x] Read release, comparison and all changed current implementation/content; check unchanged cumulative changelog history mechanically.
- [x] Read affected prior implementation and necessary dependencies; extract 3-5 exact grounding quotes.
- [x] Audit/update concepts before editing the source.
- [x] Add version-qualified source and separate changelog history, preserving older sections.
- [x] Update company, provider index and logs; check contradictions and scope.
- [x] Validate touched wiki pages and collection.
- [x] Complete the serial work item and verify terminal state.

## Reading Progress

The two existing wiki pages have been read completely. No new wiki claims have been published. Collection-time recommendation is full because the capsule budget policy changed; this is not itself proof of an incompatible payment API change.

### Mechanical Checks

- All 710 prior and 726 current retained files pass size and SHA-256 checks.
- Packet Markdown, current snapshot manifest, release notes, comparison Markdown and comparison patch match their recorded hashes.
- Collection validator passes: 167 snapshots, 153 release records, 110 comparisons, 167 work items, no structural errors. Registry/receipt diff whitespace check passes. These structural checks do not close the semantic-reading or ingest gates.
- The cumulative changelog section beginning at `## [1.97.0]` is byte-identical across both releases: SHA-256 `74ed62341201a3b1db524e20d2c0f31f58ad94f5028ee4cda32aed40efaeca8a`. The new 1.98.0 section was read completely. The unchanged `# Changelog` header is outside that section; an initial whole-file suffix assertion was too strict because the new release is inserted after that header, not before it.
- Release manifest and release notes read completely. Packet JSON identities and semantic fields and Markdown preamble/reading list reviewed; all 2,957 upstream dispositions mechanically reconciled with the Markdown inventory: 149 retained changes and 2,808 intentional policy exclusions, no gaps or unclassified changes. Deleted excluded paths use `old_path`, not the empty `new_path`; the initial inventory assertion was corrected accordingly. Comparison Markdown and the entire 303,634-character patch were read end-to-end. Hash verification is not semantic reading.

### Complete Raw Reads So Far

Current base: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/`.
Prior base: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/`.
The following nine paths were read completely in both bases:

- `src/components/modal/v2/lib/locale.js`
- `src/components/modal/v2/lib/utils.js`
- `src/components/modal/v2/parts/BodyContent.jsx`
- `src/components/modal/v2/parts/Calculator.jsx`
- `src/components/modal/v2/parts/OfferCard.jsx`
- `src/components/modal/v2/parts/TermsTable.jsx`
- `src/components/modal/v2/parts/views/LongTerm/Content.jsx`
- `src/components/modal/v2/parts/views/ProductList/Content.jsx`
- `src/components/modal/v2/parts/views/ShortTerm/Content.jsx`

These four French modal paths were also read completely in both bases:

- `content/modals/FR/long_term.json`
- `content/modals/FR/product_list.json`
- `content/modals/FR/short_term.json`
- `content/modals/FR/short_term_en.json`

Initial current-only reads (affected prior versions have since been read where they exist):

- `content/modals/CA/long_term.json`
- `content/modals/CA/long_term_fr.json`
- `content/modals/CA/long_term_xo_fr.json`
- `content/modals/CA/product_list.json`
- `content/modals/CA/product_list_fr.json`
- `content/modals/CA/short_term.json`
- `content/modals/CA/short_term_fr.json`
- `content/modals/CA/short_term_xo.json`
- `content/modals/CA/short_term_xo_fr.json`
- `content/offers/CA/long_term.json`
- `content/offers/CA/long_term_fr.json`
- `content/offers/CA/long_term_xo.json`
- `content/offers/CA/long_term_xo_fr.json`

Reading is now complete under the approved focused exception: all 148 changed current files other than the cumulative changelog, its complete new release section, and all 132 modified prior files other than the mechanically verified changelog history. The initial lists above document the first reads; the remaining 122 current files were read in contiguous chunks covering all 378,473 characters, and 119 remaining prior files in contiguous chunks covering all 357,470 characters. No claim of full upstream-repository reading is made.

CLI approval and serial claim succeeded for this item only, in `full` mode. The effective assignment expands to 497 paths. The user-approved focused exception covers unchanged files in that expansion by manifest/hash verification; changed files outside the original selector list were also fully read. No other GitHub item was approved or ingesting at claim time.

### Initial Grounding And Findings

These findings were extracted from the initial complete modal reads. Subsequent current/prior and comparison reading below closes the then-open server-dispatch and history questions:

- Current `src/components/modal/v2/lib/utils.js:101`: `} else if (!e.shiftKey && document.activeElement === tabArray[tabArray.length - 1]) {`. Prior source lacks the `!e.shiftKey` guard. This corrects the forward-wrap branch; it is not proof of complete keyboard or screen-reader accessibility.
- Current `src/components/modal/v2/parts/BodyContent.jsx:93`: `const countryClassName = country?.toLowerCase();`. That class is now appended to the modal content container; stylesheet behavior remains unverified.
- Current `content/modals/FR/short_term_en.json:49`: `"creditWarning": "Caution! A credit costs money and must be repaid.",`. Long-term, short-term and product-list views now conditionally render supplied credit-warning content.
- Canadian amount display changes from French `$ CAD` to `$ CA`, and English `$<value>` to `$<value> CAD`; language is passed from the calculator through TermsTable to OfferCard. These locale-selection branches existed before; do not describe Canadian localization as entirely new.
- French modal disclosures remove explicit French-PayPal-account-required wording and revise links/provider wording. This is version-qualified authored copy, not independent proof of changed eligibility or legal compliance.
- Canadian long-term/product-list content is present in the current snapshot. Current disclosures explicitly qualify availability by merchant/consumer eligibility. Prior comparison and server dispatch still need reading before describing the precise release delta.

### Completed Grounding And Findings

- Fourth quote, current `src/server/locale/CA/mutations/index.js:11-12`: `case 'PLLT_MQ_GZ':` / `return longTermQ[type];`. The corresponding prior dispatcher lacked the long-term branches. Canadian localization itself already existed.
- Fifth quote, current `src/server/message/mediaQueries.js:222`: ``return `.message__disclaimer > span.multi:first-of-type { white-space: normal; }`;``. This new helper is distinct from the existing `disclaimerWrap`, whose implementation changes in this release.
- Canadian long-term EN/FR message dispatch, new modal/product-list content and XO offer content expand presentment; qualifying-offer filtering and term sorting remain unchanged. Currency formatting and regional-rate wording are version-qualified authored presentation, not current eligibility or legal guidance.
- FR, AT and DE message JSONs add credit warnings; mutations put the `large` disclaimer first. New AT/DE text CSS preserves the extra cross-border account disclaimer styling. FR modal views conditionally render supplied credit warnings.
- Layout changes and forward-Tab guard are implementation evidence only. Country-class insertion does not prove a specific modal color. Removed French account-required copy does not prove relaxed eligibility. No public API or dependency change was detected; Puppeteer is already `^25.3.0` in the prior package.

### Output And Remaining Verification

Updated Pay Later concept before source promotion, then cumulative source/changelog, company, provider catalog and both logs. No new concept/source/comparison page needed; source_count stays 177. Old helper and localization behavior remain explicitly version-qualified rather than overwritten; no factual contradiction requires a new callout. Validate exact grounding, historical preservation and touched-page/collection contracts before completing this serial item. Commit/push remain outside this approval.

### Validation Results

- `validate_wiki.py`: five typed touched pages pass. The initial seven-path invocation flags the pre-existing untyped `wiki/paypal-index.md` and `wiki/log.md`; their established formats are retained, with catalog uniqueness and link/evidence checks performed separately.
- `validate_github_collection.py`: 167 snapshots, 153 release records, 110 comparisons and 167 work items pass with no structural errors before terminal completion.
- All five new grounding excerpts match their exact raw line numbers. All exact raw/tracking evidence paths resolve. Company source_count remains 177; provider/company catalog entries each remain unique.
- Historical preservation checked against HEAD: all old source implementation/version sections from Merchant Integration Surface to Version-Qualified Use are byte-preserved; the entire old changelog from `1.97.0` onward is byte-preserved.
- Scoped diff whitespace check passes. No runtime tests performed. No commit/push.

### Completion

`complete-ingest` returned `ingested` for `github-93c29d339b648ea8820e` in approved full mode. The terminal collection validator also passes (167 snapshots, 153 releases, 110 comparisons, 167 work items). No subsequent item claimed. Next step: review the scoped collection/ingest changes for a separately authorized commit, preserving unrelated session changes; push is not authorized.
