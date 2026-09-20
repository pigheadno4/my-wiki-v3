# Messaging Components 1.96.0 ingest review

- Item: `github-c9338f57d905235adf30`; approved delta, inline.
- Boundary: `@paypal/messaging-components@1.95.1` (`2bdaf940cdb0dcd29a8a3bc992eea975798d6d00`) to `1.96.0` (`a682a8d6689f308155da4cca9521265d9e156b03`).
- User explicitly approved focused reading for 1.96.0 only: complete changed implementation/content and prior affected versions, mechanical unchanged-history and manifest checks. No extension to 1.97.0, no raw/packet/registry changes, no commit/push authorization.

## Reading and grounding

Read all changed retained implementation/content, prior affected versions, package/demo documentation, release notes and current source/changelog. Reviewed packet Markdown and structured JSON classifications and the comparison; unchanged manifest inventories and historical changelog checked mechanically under the exception. The 57 changed content files include 39 new v2 fixture files and 18 modal-content files. No claim to have read the whole upstream repository or all unchanged snapshot files.

Current raw prefix: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/`.

- `src/components/modal/v2/parts/Calculator.jsx`: `aria-describedby={hasInputError ? 'purchase-amount-error' : undefined}`
- `src/components/modal/v2/parts/Calculator.jsx`: `loadingLabel = 'Loading financing options'`
- `src/components/modal/v2/parts/LoadingShimmer.jsx`: `<div id={index} className="accordion__container shimmer" aria-hidden="true">`
- `src/server/message/index.jsx`: `<span className="sr-only">{brandName}</span>`
- `content/messages/v2/README.md`: `representative CPS v2 message content fixtures` (development evidence, not live availability).

Mechanical checks: all 667 prior and 708 current snapshot entries hash/size verified; 642 unchanged hashes match; 41 added, 25 modified, zero removed. Packet Markdown, snapshot manifest, comparison Markdown/patch and release-note hashes match. Historical changelog body is unchanged. All 301 upstream changes have dispositions: 66 retained, 235 policy exclusions; no unclassified changes or packet evidence gaps.

Structured modal comparison confirms all 16 modified existing JSONs only add `content.calculator.loadingLabel`. New Apple long-term content is byte-identical to current PL2GO long-term content. Runtime dependencies unchanged; development dependency `jest-image-snapshot` is pinned from `^6.5.2` to `6.5.2` despite the packet's empty dependency_changes list.

## Checklist

- [x] Read evidence and extract grounding quotes under approved exception.
- [x] Concept audit and update before source edits.
- [x] Add cumulative source and changelog entry, preserve prior history.
- [x] Update company; retain source_count 177.
- [x] Check related concepts and comparison need.
- [x] Check contradictions and evidence limits.
- [x] Update provider index.
- [x] Update provider and root logs.
- [x] Validate touched pages, links, evidence and diff.
- [x] Complete only this work item; leave 1.97.0 awaiting approval.

Validation passed: five touched frontmatter pages; all seven touched wiki pages' wikilinks and raw/tracking paths; byte-preservation of prior source sections and the 1.95.1 changelog entry; `git diff --check`; GitHub validator before and after completion (115 snapshots, 100 release records, 57 comparisons, 114 work items). No runtime tests performed. No commit or push.

## Scope decisions

Existing Pay Later concept owns these facts; no new concept or cross-company comparison is needed. Keep Apple Wallet modal content separate from merchant Apple Pay APIs and eligibility. Keep v2 fixtures separate from production/legal claims. Changed modal SCSS, demo script and tests are policy-excluded: no visual-parity, reduced-motion, runnable-demo or runtime accessibility proof. No merchant API migration identified in retained evidence.
