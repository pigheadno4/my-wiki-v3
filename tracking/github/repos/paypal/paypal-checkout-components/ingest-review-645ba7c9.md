# Review: @paypal/checkout-components@5.0.433

Operator record; work-items.json remains state authority. User separately approved delta ingest and the same focused-reading exception for 5.0.433 only. No extension to 5.0.434; no commit/push approval.

## Evidence and grounding

Work item `github-645ba7c91bcd94bdb64e`: `5.0.432` / `e4c6f20d6bd1f6b1c7cc812a6b89e9a180146478` to `5.0.433` / `e5f517b7311d4e358b546bf796b67560195e4995`; released September 4, collected September 20, 2026.

Complete authored Buttons component and package JSON read; new changelog entry and release/comparison metadata reviewed against cumulative wiki history. Both 214-file snapshot manifests parsed, hashes/sizes checked; 210 unchanged files byte-equal. Packet Markdown/snapshot and comparison Markdown/patch hashes verified. Separate upstream release notes are unavailable.

The new changelog is an added entry plus byte-identical prior history. Package JSON differs only in version. Removing the single added aria-label line from 5.0.432 reproduces the entire 5.0.433 component, which also equals the 5.0.431 component. Generated bundles differ in bytes; both contain four aria-label occurrences and neither contains Payment Button. No semantic equivalence or deployed-bundle claim. The generated bundle, cumulative upstream history and large diff were not semantically reread in full under the approved exception. Raw files, registry and immutable packet unchanged.

Grounding under `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e5f517b/files/`:

- `CHANGELOG.md:3`: `Revert "Fix duplicate PayPal announcement for screen readers via distinct ifr…"`.
- `src/zoid/buttons/component.jsx:243`: ``title: `${FUNDING_BRAND_LABEL.PAYPAL}${fundingSource}`,``.
- Same component, line 244: `role: "presentation",`.
- `package.json:3`: `"version": "5.0.433",`.

## Checklist

- [x] Focused reading, grounding and mechanical checks.
- [x] Concept audit/update before source: existing PayPal Checkout concept; no new concept required.
- [x] Cumulative source and changelog, preserving earlier history.
- [x] Company update; source_count remains 177.
- [x] Reciprocal concept references.
- [x] Cross-company comparison decision: not warranted.
- [x] Version/contradiction check: label specific to 5.0.432; rollback rationale unknown; no bundle/runtime claim.
- [x] Provider index.
- [x] Provider/root logs.
- [x] Validation and completion of this item only.

## Completion

Five touched content/log pages pass wiki validation; root-log/provider-index links verified separately. GitHub validator passes with 113 snapshots, 98 releases, 55 comparisons and 112 work items. `git diff --check` passes. CLI returned `ingested` for this delta item; 5.0.434 remains awaiting approval. No commit or push.
