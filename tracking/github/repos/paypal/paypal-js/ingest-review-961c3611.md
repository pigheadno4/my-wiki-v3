# PayPal JS approved full-ingest checkpoint

Operator review notes and completion record. Generated work-items.json remains
the lifecycle authority; this file is not a substitute for reading raw evidence.

## Authorization and scope

- User approved full, additive ingest in this conversation on 2026-09-19.
- Work item: `github-961c3611b36c6341ad56`.
- SHA: `abc4c8331a64e91d90a6eec911b635f36c0f273f`.
- Packages: `@paypal/paypal-js@11.0.1 -> 11.1.0` and
  `@paypal/react-paypal-js@10.4.1 -> 10.5.0`.
- Full override reason: required `fundingSource` changes public approval-data
  types. Keep the immutable collection-time delta recommendation unchanged.
- Preserve earlier versions. Work inline and serially. No commit or push
  authorized for this item.
- CLI full approval and serial claim completed after the approved focused read.
  CLI complete-ingest subsequently marked the item ingested after validation.

## Workflow checklist

1. Complete: approved focused reading and five grounding quotes below.
2. Complete: updated existing paypal-checkout, paypal-apm, and
   paypal-expanded-checkout before editing the source. No new concept needed.
3. Complete: additive cumulative source and separate changelog; package-qualified
   history retained, with React examples and explicit runtime evidence limits.
4. Complete: company update; existing source keeps source_count at 177.
5. Complete: all three updated concepts cite the source, which links back.
6. Complete: no substantive cross-company comparison; no comparison page added.
7. Complete: client eligibility example/type contradiction mirrored in checkout
   concept and source/changelog; previous callback warning preserved.
8. Complete: provider index entries updated; no root catalog change needed.
9. Complete: provider log entry and concise root log entry added.
10. Complete: seven content pages passed validate_wiki; navigation checked
    separately; collection validator passed before and after complete-ingest.

## Reading boundary

The effective full-mode expansion was 180 paths totaling 1,692,178 bytes,
including 157 snapshot files. No registry reading selector is configured.
Recompute with `ingest_required_reading(root, item, mode="full")` from
`scripts/collect_github_repos.py` and check identities before resuming.
Hash verification is not a semantic full read.

### Completed reads carried forward from this conversation

- Entire cumulative source (736 lines) and changelog (469 lines), through their
  2026-09-13 state. Reread if either has subsequently changed.
- Current packet Markdown and both release-note Markdown files.
- Core package comparison `11.0.1--11.1.0/diff.patch` (385 lines).
- Current evidence attachment JSON.
- Snapshot paths below, relative to
  `raw/github/paypal/paypal-js/snapshots/2026-09-19-abc4c83/files/`:
  - `packages/paypal-js/types/v6/components/base-component.d.ts`
  - `packages/paypal-js/types/v6/components/paypal-legacy-billing-agreements.d.ts`
  - `packages/paypal-js/types/v6/components/paypal-subscriptions.d.ts`
  - `packages/react-paypal-js/src/v6/components/LPMOneTimePaymentButton.tsx`
  - `packages/react-paypal-js/src/v6/components/LPMPaymentProvider.tsx`
  - `packages/react-paypal-js/src/v6/components/PayPalCardNameField.tsx`
  - `packages/react-paypal-js/src/v6/config/lpmRegistry.ts`
  - `packages/react-paypal-js/src/v6/hooks/useLPMOneTimePaymentSession.ts`
  - `packages/react-paypal-js/src/v6/hooks/useVenmoOneTimePaymentSession.ts`
  - `packages/react-paypal-js/src/v6/hooks/usePayPalCardFieldsOneTimePaymentSession.ts`
  - `packages/react-paypal-js/src/v6/lpmExports.ts`
- All six supplement source files under
  `raw/github/paypal/paypal-js/supplements/2026-09-19-abc4c83-f8243778/files/`.
  The last outstanding file, `shared/code.ts`, was read end-to-end in ranges
  1-380, 381-760, and 761-1120 (EOF at line 1103).
- Supplement manifest JSON, read completely after `shared/code.ts`.
- Both current package comparison Markdown files, read on continuation.
- Additional snapshot paths fully read on continuation, relative to the same
  snapshot `files/` directory:
  - `packages/paypal-js/types/v6/components/constants.d.ts`
  - `packages/paypal-js/types/v6/components/card-fields.d.ts`
  - `packages/paypal-js/types/v6/components/find-eligible-methods.d.ts`
  - `packages/paypal-js/types/v6/components/lpm-payments.d.ts`
  - `packages/paypal-js/types/v6/components/paypal-payments.d.ts`
  - `packages/paypal-js/types/v6/index.d.ts`
  - `packages/react-paypal-js/src/v6/types/sdkWebComponents.ts`
  - `packages/react-paypal-js/src/v6/index.ts`
  - `packages/react-paypal-js/package.json`
  - `packages/react-paypal-js/rollup.config.js`

### Additional completed reads

- Both package CHANGELOG.md files, core package.json, and the complete React
  README.md (2669 lines, read through EOF in six contiguous ranges).
- Prior snapshot core rollup.config.js; both release manifests; both comparison
  JSON files; packet JSON (all metadata, package fields, retained evidence and
  upstream changes, with equality checked before deduplicating identical arrays).
- Current snapshot manifest: all metadata and excluded entries, then all file
  entries in ranges [0:80] and [80:].

### Approved item-specific reading scope

Manifest hash comparison on continuation confirmed 24 new/changed retained
files (332,255 bytes) and 133 unchanged files (895,397 bytes). Both generated
OpenAPI declaration files are unchanged, totaling 464,307 bytes. These counts
describe snapshot files, not the broader 180-path effective reading list.

The user approved the focused scope and then requested continuation: every
changed retained file plus relevant dependencies, examples, release records,
and history, with complete reads of each selected file and full additive wiki
output. This is an explicit exception for this SHA work item, not a permanent
registry or workflow-policy change. The CLI default full expansion remains
180 paths; do not claim every unchanged path was reread. Unchanged generated
schemas and unrelated unchanged implementation remain retained for queries.
The immutable snapshot and collection-time packet remain untouched.

Completed on continuation: all 3782 lines of the React comparison patch, in
four contiguous ranges; prior manifest metadata and differing entries, with
133 identical file entries and all exclusions verified against the fully read
current manifest. A truncated whole-manifest output was not used as a full read.

Additional complete current-snapshot dependency reads (package-relative):
- Core: src/v6/index.ts, src/utils.ts, types/v6/components/venmo-payments.d.ts.
- React: src/v6/components/PayPalProvider.tsx, PayPalCardFieldsProvider.tsx,
  PayPalCardField.tsx, VenmoOneTimePaymentButton.tsx.
- React: src/v6/context/PayPalProviderContext.tsx, PayPalDispatchContext.tsx,
  PayPalCardFieldsProviderContext.tsx.
- React: src/v6/hooks/useEligibleMethods.ts, usePayPal.ts, usePayPalDispatch.ts,
  useError.ts, useIsMounted.ts, useIsomorphicLayoutEffect.ts,
  usePayPalCardFields.ts, usePayPalCardFieldsSavePaymentSession.ts.
- React: src/v6/utils.ts, src/v6/types/index.ts, ProviderEnums.ts.

All 24 added/modified current retained files are covered by the completed reads.
The current source and changelog still match the previously read tracked files.

## Grounding quotes

Locations below are relative to the current snapshot files/ directory.
1. `packages/paypal-js/types/v6/components/base-component.d.ts:11`:
   `fundingSource: FundingSource;`
2. `packages/react-paypal-js/CHANGELOG.md:7`:
   `Added new PayPalCardNameField component to use with Card Fields`
3. `packages/react-paypal-js/CHANGELOG.md:8`:
   `Add React wrappers for all 50 v6 SDK Local Payment Methods (LPMs)`
4. `packages/react-paypal-js/src/v6/hooks/useLPMOneTimePaymentSession.ts:172`:
   `Session fields are merchant-collected inputs resolved on the`
   Context at 172-174 explicitly assigns session fields to the second argument.
5. `packages/react-paypal-js/src/v6/hooks/useVenmoOneTimePaymentSession.ts:19`:
   `` `sandboxSupport` is a temporary Venmo sandbox-testing flag that the JS SDK will ``

## Review observations to retain

These are review notes, not canonical ingested claims. Ground the final source
in exact raw links and quotes after the reading gate is complete.

- Core approval-data types require `fundingSource`; manually constructed typed
  data and mocks may need changes, but callbacks need not consume the field.
- React adds LPM wrappers/hooks and card name field support. Core LPM types
  existed earlier; do not describe this as the first core LPM capability.
- LPM eligibility is checked by examples, not automatically by the generic
  button/hook. Loading state is not transaction-level double-click protection.
- `shared/code.ts` card examples inspect `submitResponse.state` before a
  separate backend capture. Resolved `submit()` alone is not capture proof.
- Several examples parse JSON or await `fetch()` and log success without
  checking `response.ok` or capture status. Preserve the distinction between
  illustrative snippets and production-ready server verification.
- Card vault examples log a setup token as saved; do not equate this with
  independently verified durable vault completion.
- Venmo sandbox support in a React hook is not proof of native SDK support,
  merchant eligibility, or production availability.
- Hosted runtime behavior and runnable integration success remain untested.

## Validation and next step

- validate_wiki: seven touched content pages passed with no issues.
- Initial invocation including paypal-index.md and log.md reported missing
  frontmatter. These names are exempt in the validator's normal whole-wiki
  route; no schema or validator change was made. Separate navigation checks
  passed on both pages, with no placeholders or unresolved wikilinks.
- All 110 relative evidence links in the source/changelog resolve; each has
  exactly one entry in the provider index.
- validate_github_collection passed after completion: 109 snapshots, 95 release
  records, 51 comparisons, 108 work items; no structural errors.
- Focused git diff --check passed. Reviewed diff preserves prior release
  sections; only current metadata, overview, package table, and related links
  replace earlier lines.
- No payment runtime, published-package build/compiler, or bundle-size test.

The user subsequently approved a scoped commit of this completed ingest.
Exclude unrelated Braintree, BYD, rule, and script changes; stage only this
item's hunks in shared wiki navigation. Push remains unauthorized.
