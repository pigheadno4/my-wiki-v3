# PayPal Checkout Components Exact-Ref Collection Review - 2026-11-09

## Collected Boundary

- Repository: `paypal/paypal-checkout-components`.
- From: `dcd6abfc340371666a0428d7292a2cab32c2bbca`.
- To: `f2c422afd638eb3f7e4c8a46b3a998ddbad0fc75`, identified as `default-branch@f2c422a`.
- Work item: `github-9a387d85474ea0fe16cd`, `awaiting_approval`; no approved ingest mode.
- Packet: `tracking/github/repos/paypal/paypal-checkout-components/ingest-packets/github-9a387d85474ea0fe16cd/packet.json` and sibling `packet.md`.
- Current immutable snapshot: `raw/github/paypal/paypal-checkout-components/snapshots/2026-11-09-f2c422a/manifest.json`.
- This is unreleased default-branch evidence, not a new package release. Latest accepted stable identity remains `@paypal/checkout-components@5.0.438`.

## Confirmed Source Findings

The complete old and new `src/interface/hosted-buttons.js` and `src/lib/security.js`, plus the prior `src/interface/button.js`, were read. The helper is identical across the two snapshots.

1. Hosted Buttons now exports `allowIframe` using the existing lazy protected-export pattern already used by the Buttons entry. This addresses the missing `paypal.allowIframe()` export when only `components=hosted-buttons` is loaded.
2. `protectedExport` exposes the helper only when `isPayPalDomain()` is true; otherwise it returns `undefined`. This is not a new public merchant integration API or permission for arbitrary-origin iframe checkout.
3. The helper itself rejects calls outside a PayPal domain. Within its supported context, it returns true when popups are unsupported or the parent component window is same-domain; otherwise it returns false. External dependency implementations and browser behavior were not runtime-tested.
4. Two added test files are recorded as excluded under existing tests policy. They were not collected as source evidence or executed. No registry policy was changed.

## Snapshot-Selection Caveat

The generated packet lists `vite.config.js` as removed because it was retained as changed-release evidence in the prior snapshot but is not selected in the new capsule. It is NOT an upstream deletion.

The exact ending Git tree still contains `vite.config.js` with blob ID `da7523b49c4835c2b3f79933a7e22ae6e05317f3`, size 2,118 bytes, identical to the prior manifest. The prior complete file was read and configures Vitest. The generated exact-ref patch contains only the Hosted Buttons implementation change. During ingestion, preserve prior Vite knowledge and describe this as a selection-only omission, not a removal or migration requirement. Accepted raw evidence and generated packets were not manually altered.

[Exact ending tree metadata](https://api.github.com/repos/paypal/paypal-checkout-components/git/trees/f2c422afd638eb3f7e4c8a46b3a998ddbad0fc75)

## Validation

- Collector completed without errors and stopped at `awaiting_approval`.
- All 427 retained files across both manifests passed byte-size, SHA-256 and Git blob ID verification.
- The only changed common retained path is `src/interface/hosted-buttons.js`; the only prior-only retained path is the unchanged upstream `vite.config.js` noted above.
- Packet Markdown, linked snapshot, comparison Markdown and patch hashes passed.
- Offline collection validation reports one pending work item and the same 13 unrelated historical structural errors. None reference this repository or work item. Global validation is not clean.
- No wiki ingestion, approval/claim, commit or push was performed.

## Recommendation and Next Gate

Recommend delta ingestion of `default-branch@f2c422a`, preserving all previous release/ref history and explicitly carrying the selection caveat above. This is a contained export repair; no helper behavior or security restriction changed. User approval is required before ingesting. Packet-required reading and the normal ingest/concept audit remain required; this review does not authorize a reading exception.
