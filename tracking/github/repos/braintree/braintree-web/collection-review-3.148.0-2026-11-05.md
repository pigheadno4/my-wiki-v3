# Braintree Web 3.148.0 Collection Review

## Published Tracking Refresh

The preceding approved unchanged Braintree v6 sample check was published separately as `db1927c44a9e148bfc9ed7f6a34a35c02ea59a2b`; origin/main matched that full SHA after push. Only the two generated collection-index files were committed using an isolated index. Other sessions' staged/unstaged work was preserved.

## New Collection

- Repository: `braintree/braintree-web`; package `braintree-web@3.148.0`, released 2026-11-02, collected 2026-11-05.
- Prior release `3.147.0`, SHA `f3357c49c7b71f079d031c3ddf89cdfe444f6511`; current SHA `0b989560481a1274a8fda27e426f6297d3bde552`.
- Work item `github-b0a5af655a25673da0cb` is `awaiting_approval`; approved_mode null. No ingestion or wiki-source edit.
- Snapshot `raw/github/braintree/braintree-web/snapshots/2026-11-05-0b98956/manifest.json`: 333 files / 2,239,903 bytes. Twenty modified, 313 unchanged; no additions/removals. Prior: 333 files / 2,232,384 bytes.
- Packet `ingest-packets/github-b0a5af655a25673da0cb/packet.json`: delta/high, reasons contained minor, dependency change, payment review signal; 29 required paths / 759,728 bytes at review time; zero reported gaps/unclassified changes. Recommendation does not authorize ingest.
- Existing selectors include the stable-major guard; no registry/rule/budget edits were needed.

## Findings Before Ingestion

Release notes, complete comparison Markdown/patch and targeted current implementation were reviewed; this is not yet a full assigned-file ingestion read. Test/lockfile diff excerpts in the generated comparison are not complete retained test/dependency source or proof of executed upstream tests.

1. **PayPal v6 teardown:** now waits for client and frame-service promises, invokes frame-service teardown and sends analytics. The retained frame-service implementation closes its frame and removes its dispatch iframe. Storybook adds teardown controls, including cleanup of both initial-vault and saved-method edit instances. This is lifecycle cleanup, not a browser-tested guarantee that all hosted SDK resources are destroyed. A rejected prerequisite promise still prevents the completion callback.
2. **Optional shopper session metadata:** public create documentation adds `shopperSessionId`; `_initialize` records truthy values and new checkout/vault/messages/saved-method SDK instances can forward the value to `window.paypal.createInstance`. It is not a payment token, authenticated buyer identity or settlement result.
3. **Important load-order/shared-state caveat:** storage is module-wide and guarded by the exact `window.paypal` object. `_initialize` records the value before a later SDK load can create/replace that object. The getter then returns undefined, and another wrapper can overwrite the shared ID. Existing or in-flight instances return before the ID-forwarding branch; no new per-instance update call is introduced. Treat the release-note forwarding statement as conditional and test fresh-load, preloaded-SDK and multi-wrapper cases before adoption.
4. **Instant Verification:** `startPayment` strips only the exact trailing literal `?customer_id=` from a string authorization fingerprint before the redirect's `at` query value. The regex is `/\?customer_id=$/`; nonstrings are returned unchanged. This is not general query stripping, JWT validation or customer authorization.
5. **Dependency:** direct `credit-card-type` pin changes 10.2.0 -> 10.3.1. Dependency implementation was not collected in this capsule; no specific recognition/security behavior is inferred from the version bump alone.

## Helper-Only Check

Executed only the inspected module-level setter/getter fragment in a Node VM with a stub `window`, no imports, browser, hosted SDK, network or payment calls:

- Record `shopperSessionId = A` while `window.paypal` is absent; replace `window.paypal` with an object; getter returns undefined.
- Record A then B against the same SDK object; getter returns B.

This confirms helper semantics, not an end-to-end browser reproduction. No raw or upstream source was modified.

## Verification

- All 666 prior/current retained file sizes, SHA-256 and Git blob IDs pass.
- Packet Markdown, comparison Markdown/patch digests pass; original evidence unchanged.
- Fresh offline validation retains exactly the same 13 unrelated structural errors (six historical packet-budget failures and their six invalid-packet consequences, plus the Adyen PHP changelog omission). No error for this repository/item; one pending item, this release. Whitespace check passes. No project code/rules/registry edits, so no new unit-suite run is warranted for this collection-only review.

Next: obtain separate approval for delta ingestion with focused reading, preserving all 3.147.0 and earlier history. The new raw/packet/index/review changes remain local and uncommitted.
