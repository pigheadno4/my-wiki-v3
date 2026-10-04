# Braintree Android 5.31.0 ingest review

- Item `github-d0228afe14f5b691e8b7`; approved delta from `braintree-android@5.30.0` to `braintree-android@5.31.0`; SHA `438d33ac42c92ca7489c3fec3b45d088a75a8361`.
- Explicit user-approved focused reading for this release only. Fully read changed implementation, affected prior client, README, build configuration, migration guide, release notes and patch, plus current source/changelog. Snapshot inventories and unchanged cumulative changelog history mechanically verified. Both 388-file snapshots passed every file hash; old changelog suffix identical.
- Packet: six modified retained files, 382 unchanged, no gaps/unclassified changes. Mechanically checked all 3,004 upstream dispositions: six retained and 2,998 policy exclusions, predominantly generated documentation; excluded files were not used as implementation proof.
- Additional existing retained files read fully: DEPENDENCIES.md and BraintreeCore/build.gradle. Browser Switch version discrepancy remains unresolved because gradle/libs.versions.toml is not retained. No supplement or policy change; raw immutable. Upstream build configuration not executed; credential literals not used or copied into synthesis.

## Grounding quotes
Snapshot `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/files/`:
- `PayPal/src/main/java/com/braintreepayments/api/paypal/PayPalInternalClient.kt`, sendRequest: `val requestBody = if (payPalRequest.enablePayPalAppSwitch && appLinkParam != null) {`
- Same file, appendDeviceInfo: `context.getSystemService(Context.ACTIVITY_SERVICE) as? ActivityManager ?: return requestBody`
- Same file, appendDeviceInfo: `put(PayPalRequest.DEVICE_MODEL_KEY, Build.MODEL)`
- `CHANGELOG.md`, 5.31.0: `Update Browser Switch version to 3.6.0`
- `DEPENDENCIES.md`, BraintreeCore table: "| `com.braintreepayments.api:browser-switch` | 3.5.1 |"

## Cycle
- [x] Read and grounding
- [x] Concept audit/update
- [x] Cumulative source and changelog
- [x] Company/count and reciprocal citations (292 sources unchanged; separate website C31 preserved)
- [x] Comparison/contradiction disposition (Browser Switch mismatch preserved in source, changelog and concept; no cross-company comparison)
- [x] Index/log
- [x] Validation/completion (five typed wiki pages; catalog/root-log links, count equality, unique navigation, history and verbatim quotes; global GitHub validator passes; item ingested)
