# Review: @paypal/checkout-components@5.0.432

Operator checkpoint; generated work-items.json remains state authority.

## Scope and authorization

User approved delta ingest, then a one-time focused-reading exception for this item only: full authored component and package-manifest reads, new changelog entry review, mechanical checks of generated bundle changes and unchanged history. Raw evidence, registry and packet are unchanged. This is not a claim to have semantically read the entire bundle, cumulative upstream changelog or 1.6 MB patch.

Work item: `github-ac14a515ca3bffb44e18`. Transition: `5.0.431` / `9bb1162373b4dd96d5a3196dbfab41990f606bb7` to `5.0.432` / `e4c6f20d6bd1f6b1c7cc812a6b89e9a180146478`. Released September 1; collected September 20, 2026.

## Evidence and grounding

Read cumulative wiki source and changelog, complete current `src/zoid/buttons/component.jsx` and `package.json`, release manifest (notes unavailable), packet Markdown, comparison metadata and authored diff. Parsed packet JSON and snapshot manifests; verified SHA-256/size for all 214 files in each snapshot, all 210 unchanged files byte-equal, packet Markdown/snapshot hashes and comparison Markdown/patch hashes.

The new upstream changelog is exactly a six-line prefix followed by the unchanged prior body. Package JSON differs only by version. Removing the added aria-label line makes the current authored component byte-identical to the prior component. Generated bundle bytes differ; both bundles contain four `aria-label` occurrences and neither contains `Payment Button` or `allowpaymentrequest`. No bundle semantic-equivalence, deployed-build or screen-reader test claim. A general character-diff attempt was stopped due to excessive runtime and replaced by bounded hash/literal checks.

Grounding, under `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e4c6f20/files/`:

- `CHANGELOG.md:3`: "Fix duplicate PayPal announcement for screen readers via distinct iframe aria-label".
- `src/zoid/buttons/component.jsx:244`: `"aria-label": "Payment Button",`
- Same component, line 245: `role: "presentation",`
- `package.json:3`: `"version": "5.0.432",`

## Checklist

- [x] Approved focused reading and grounding; hash and history verification.
- [x] Concept audit/update before source edit: existing PayPal Checkout concept; no new concept warranted.
- [x] Cumulative source and separate changelog, preserving old versions.
- [x] Company update; source count unchanged at 177.
- [x] Reciprocal concept references checked.
- [x] Cross-company comparison decision: not warranted.
- [x] Contradiction/version-boundary check: distinct from older title fix; source versus bundle boundary explicit; later releases remain queued.
- [x] Provider index update.
- [x] Provider and root log entries.
- [x] Validate and complete this item only.

## Verification

- Five touched content/log pages pass `validate_wiki.py`; provider-index/root-log links checked separately.
- GitHub validator: 113 snapshots, 98 releases, 55 comparisons, 112 work items; no structural errors.
- `git diff --check` passes. CLI completion returned `ingested` for this delta item on September 20, 2026. No commit/push; later two releases remain awaiting approval.
