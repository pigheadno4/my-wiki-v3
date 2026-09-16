# Braintree Web 3.145.0 delta-ingest reading checkpoint

Updated: 2026-09-16. Work item: `github-16166784785e0ab99eae`.
User approved high-priority delta ingest, superseding the earlier full choice.
This is an operator checkpoint, not a generated
status file, ingestion receipt, or canonical wiki source.

## Identity and boundary

- Snapshot: `raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/manifest.json`
- SHA: `732ed094354d650605e678d98246ce6332952ad3`
- Manifest SHA-256: `863e9abf381f3ad45d86eec66a6a607d9f14ec089fdfbe1cfd0a7fd3bc6e78be`
- Retained snapshot: 332 files, 2,191,272 bytes. Delta scope: 29 added/modified
  files; 303 byte-identical files do not require rereading.
- Packet/history evidence remains assigned. The original packet is immutable.
- User explicitly approved a one-item exception: fully review retained-source
  changes and mechanically validate excluded-file dispositions instead of
  reading excluded test/lockfile diffs. No permanent rule or packet change.
- Approved, claimed, and completed as delta through the CLI; state is ingested.

## Workflow checklist

- [x] Finish packet/history review and extract grounding quotes under the approved exception.
- [x] Concept audit and justified concept updates before source edits (three existing concepts; no new page).
- [x] Add 3.145.0 knowledge to cumulative source and changelog, preserving history.
- [x] Update company page; preserve correct source count.
- [x] Confirm concept coverage and reciprocal factual citations.
- [x] Assess whether any substantive comparison is warranted (release comparison in source/changelog; no new cross-provider comparison warranted).
- [x] Check contradictions against existing wiki knowledge (qualify older wrapper and SDK evidence by version; no new contradiction identified).
- [x] Update Braintree index only as appropriate.
- [x] Append provider/root log entries without changing unrelated entries.
- [x] Validate touched wiki pages and GitHub evidence; complete the work item.

## Confirmed full reads in the 2026-09-16 turn

Current source and changelog were both read end-to-end before raw reading:

- `wiki/sources/braintree/github/source-github-braintree-web.md`
- `wiki/sources/braintree/github/changelog-github-braintree-web.md`
- `raw/github/braintree/braintree-web/releases/braintree-web/3.145.0/2026-09-15/release-notes.md`

Under the current snapshot's `files/`, exactly 119 files were fully read:

1. Every file whose manifest `size <= 1100`: 115 files. This deterministic
   selector identifies the completed set against the pinned manifest above.
2. `src/lib/create-deferred-client.js`
3. `src/lib/frame-service/external/frame-service.js`
4. `src/data-collector/fraudnet.js`
5. `src/fastlane/fastlane.js`

Subsequent bounded full reads completed all remaining changed files:

- `.storybook/stories/Venmo/Venmo.stories.ts`
- `.storybook/stories/branded_payments/venmo/VenmoIntegration.ts`
- `CHANGELOG.md` (sequential ranges 1-400, 401-1000, 1001-1600,
  1601-2200, 2201-EOF)
- `package.json`
- `src/data-collector/index.js`
- `src/local-payment/external/local-payment.js`
- `src/paypal-checkout-v6/paypal-checkout-v6.js`
- `src/paypal-checkout/paypal-checkout.js`
- `src/venmo/external/venmo-desktop.js`
- `src/venmo/internal/index.js`
- `src/venmo/internal/ui-elements/back-view.js`
- `src/venmo/internal/ui-elements/card-container.js`
- `src/venmo/internal/ui-elements/close-icon.js`
- `src/venmo/internal/ui-elements/error-view.js`
- `src/venmo/internal/ui-elements/front-view.js`
- `src/venmo/internal/ui-elements/modal-backdrop.js`
- `src/venmo/internal/ui-elements/modal.js`
- `src/venmo/internal/ui-elements/qr-code-view.js`
- `src/venmo/shared/events.js`
- `src/venmo/venmo.js`

The other changed files are covered by the 119-file read above. Unchanged
`src/lib/convert-to-braintree-error.js` and `src/lib/assets.js` were also read
to verify delegated error/loader behavior.

Packet Markdown and comparison Markdown were read fully. Metadata and retained
patch review are complete as detailed below. The 15,951-line upstream patch
includes excluded lockfile and test diffs, handled under the explicit one-item
exception, not counted as full semantic reads. Earlier truncated output was
not counted; retained portions were subsequently read in bounded ranges.

## Source-grounded findings promoted to the wiki

### Review completion and grounding gate

All 29 changed raw files and all their retained-source patch sections are fully
read. Remaining retained patch ranges completed: 20-74, 140-170,
13477-13766, 13767-14017, 14018-14263, 14264-14380. The earlier complete
12141-13476 range covers the other retained implementation changes.
Release manifest, comparison JSON, packet metadata/classifications, and both
snapshot inventories/exclusions reviewed. SHA-256 and Git blob hashes checked
mechanically for all 330 prior and 332 current files; 303 unchanged metadata
rows are exactly identical. All 47 patch paths reconcile to 29 retained and
18 excluded dispositions (13 test/mock paths and five outside-policy paths).
Global collection validation passed before approval. Hash verification is not
claimed as a semantic read of unchanged source or excluded diff contents.

Grounding quotes, relative to the current snapshot's files directory:

1. `src/lib/create-deferred-client.js:41`: `return loadClientScript(src, true);`
2. `src/paypal-checkout-v6/paypal-checkout-v6.js:2719`:
   `if (account.details && account.details.implicitlyVaultedPaymentMethodToken) {`
3. `src/venmo/venmo.js:136`:
   `return Promise.reject(new BraintreeError(errors.VENMO_ECD_DISABLED));`
4. `src/fastlane/fastlane.js:58`:
   `convertToBraintreeError(err, errors.FASTLANE_SDK_LOAD_ERROR)`

- Deferred client: existing client returns directly. When loading is needed,
  any first load rejection triggers one forced reload, not only errors identified
  as suspend-related. Recovery analytics follows successful client creation.
  Final script-load error retains `details.originalError` and a failure-kind label.
- Shared frame service: delayed visibility listener installation (500 ms),
  suspend/resume callbacks, and delayed close check (1000 ms). Resume requires
  prior backgrounding; cleanup removes listeners/timeouts. PopupBridge bypasses
  the normal open path. This is not automatic payment completion or popup reopening.
- Fraudnet: failure emits enriched analytics when a client exists and returns
  null. Do not infer whole DataCollector success; read its caller completely.
- Fastlane: the catch wraps loader/initialization-chain errors. Existing
  BraintreeError instances pass through unchanged; other errors become
  FASTLANE_SDK_LOAD_ERROR with details.originalError. The delegated SDK is not
  evidence collected in this repository.
- Shared helpers preserve existing iframe, browser, and legacy module behavior;
  do not describe unchanged code as new in 3.145.0 without comparison evidence.
- PayPal Checkout v6 now distinguishes billing-token-only vaulting from
  checkout-with-vault with an order/payment identifier. The latter requires a
  payer identifier and sends billingAgreementToken with checkout fields.
  implicitlyVaultedPaymentMethodToken is copied only when the gateway supplies
  it in account.details; it is not a guaranteed result of the upgrade.
- Venmo desktop address flags are rejected with VENMO_ECD_DISABLED when ECD
  is disabled. The modern paymentMethodUsage mutation forwards truthy flags
  under paysheetDetails; the legacy QR mutation does not. payerInfo is backend
  output, not a promise of address availability.
- Venmo QR UI now uses the qrcode dependency, custom fonts, a rescan action,
  and separate rescan/error-view analytics. QR generation validates HTTPS and
  the venmo.com hostname. Completion still depends on context polling.
- Popup recovered analytics in non-v6 PayPal and LocalPayment occur before
  tokenization; they are not proof of payment success. Shared close detection
  is not automatic payment resumption or popup reopening.

## Completion

The CLI recorded `ingested` on 2026-09-16. Seven typed wiki pages passed
`validate_wiki.py`; the nine-file run reported only existing missing YAML
frontmatter conventions in `wiki/braintree-index.md` and `wiki/log.md`, with
no other issues. Scoped `git diff --check` passed. GitHub collection validation
passed for 108 snapshots, 93 release records, 49 comparisons and 107 work items.
No hosted payment flows were executed. No commit or push performed.

Next step: review and commit only this work's approved files, preserving
unrelated concurrent edits and existing version history.
