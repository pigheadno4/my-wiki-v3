# PayPal Android Collection Review - 2026-11-15

## Release and Newer-Major Guard

- User authorized recheck, newer-major verification and findings before ingestion.
- Registry tracks stable package-qualified majors `paypal-android@2` and `paypal-android@3`; no registry change was made.
- Routine future collection found `paypal-android@3.2.0`, published 2026-11-03T17:23:13Z, at `c5a36f034b0429b5c833b9e98ff24ef0ce52bd55`.
- Independent live semantic-tag inspection found stable majors 0, 1, 2 and 3, with 3.2.0 the newest stable tag. No stable v4 or higher was found. Main HEAD equals the 3.2.0 SHA, so no distinct later main checkpoint was found in this check.
- Prior ingested boundary remains `paypal-android@3.1.0`, SHA `d100313f2247b512cedf6080bb7b6ecaada26d42`, wiki date 2026-10-16.
- Work item `github-71f2e4bd6e83f068dc81` is `awaiting_approval`, not approved or claimed.

## Preliminary Findings Before Ingestion

Complete retained release notes, `Venmo/api/Venmo.api`, `Venmo/build.gradle`, `PayWithVenmoViewModel.kt` and `CreateVenmoOrderUseCase.kt` were read, along with packet/comparison navigation and prior cumulative source context. This is not yet a complete ingest read of every changed source file.

1. The new API surface declares `VenmoClient(Context, CoreConfig)`, coroutine and Java-compatible callback `start(Activity, orderId)` forms, and `finishStart(Intent)`.
2. Return variants include Success, Canceled, NoResult and Failure. Success exposes token, payer ID and an approved Boolean; a result name alone is not settlement proof.
3. The module build declares publication name `venmo-payments` and a CorePayments dependency. This establishes repository build/API intent, not independently verified artifact availability or merchant enablement.
4. The demo creates an Orders request with a Venmo payment source, return/cancel URLs and `appSwitchContext.source = NATIVE_APP`; the example uses USD 10.99. Its view model starts Venmo with the created order ID, processes return results, and offers a separate server completion/capture step with collected device data.
5. Earlier v2/v3.0/v3.1 statements about the absence of a native Venmo API remain historical facts for those versions. A later 3.2.0 section must qualify the new boundary, not erase earlier knowledge. Neither the API nor demo proves PayPal-only merchant eligibility, geographic availability, account enablement or tested device/payment behavior.

## Evidence Gap and Mode Recommendation

The current capsule retains Venmo API/build/manifest evidence but lacks `Venmo/src/main/java` among its required roots. All eight new Venmo implementation files are classified `intentional-policy-exclusion` / `outside-capsule-policy`, not retained. Both changed CoreEnvironment variants are also excluded. Automated `evidence_gaps` and `public_api_changes` arrays are empty, which does not override this manual evidence review or the demonstrably new API declarations.

The script recommends delta/high priority. Operator recommendation is **full additive** after missing implementation evidence is reviewed, because a new native payment flow is a full-mode signal under `rules/github-repos.md`. This is a recommendation only; no mode override or approval has been executed.

Recommended next approval is an immutable supplement at exact accepted SHA `c5a36f034b0429b5c833b9e98ff24ef0ce52bd55` for these ten text files, then attach/review before requesting full ingest approval:

```text
Venmo/src/main/java/com/paypal/android/venmo/VenmoClient.kt
Venmo/src/main/java/com/paypal/android/venmo/VenmoFinishStartResult.kt
Venmo/src/main/java/com/paypal/android/venmo/VenmoStartCallback.kt
Venmo/src/main/java/com/paypal/android/venmo/VenmoStartResult.kt
Venmo/src/main/java/com/paypal/android/venmo/analytics/VenmoAnalytics.kt
Venmo/src/main/java/com/paypal/android/venmo/analytics/VenmoCheckoutEvent.kt
Venmo/src/main/java/com/paypal/android/venmo/errors/VenmoError.kt
Venmo/src/main/java/com/paypal/android/venmo/errors/VenmoErrorCode.kt
CorePayments/src/debug/java/com/paypal/android/corepayments/CoreEnvironment.kt
CorePayments/src/release/java/com/paypal/android/corepayments/CoreEnvironment.kt
```

This supplement would not modify accepted snapshots or silently broaden future registry policy. A permanent Venmo-root addition for future releases is a separate policy decision. Additional gaps discovered from the complete supplemented implementation must be reported rather than inferred away.

## Integrity and Boundaries

- Current snapshot: 282 files / 709,337 bytes; 23 modified, five added and 254 unchanged retained files versus 3.1.0.
- All 559 prior/current retained file sizes, SHA-256 values and Git blob IDs pass. Packet Markdown, snapshot and comparison Markdown/patch hashes pass.
- All 44 upstream changed paths have recorded dispositions: 28 retained and 16 policy-excluded. Mechanical disposition completeness is not semantic sufficiency for the new Venmo flow.
- Offline collection validation reports the same 13 unrelated historical structural errors, none for this repository, and one pending work item. Global validation is not clean.
- No wiki ingestion, source/changelog edit, registry edit, supplement collection, commit or push was performed. Existing historical raw and wiki knowledge remain unchanged.

## Evidence

- [Release notes](https://github.com/paypal/paypal-android/releases/tag/3.2.0)
- [Current immutable snapshot](../../../../../raw/github/paypal/paypal-android/snapshots/2026-11-15-c5a36f0/manifest.json)
- [Review packet](ingest-packets/github-71f2e4bd6e83f068dc81/packet.md)
- [Comparison](comparisons/paypal-android/3.1.0--3.2.0/comparison.md)

## Approved Supplement Review - 2026-11-15

The user subsequently approved collection of the ten paths listed above at the same 3.2.0 SHA, with findings before full ingestion. That collection is complete. The earlier gap/proposed collection section records the pre-supplement state; it is not a claim that these files remain missing.

- Immutable supplement: `raw/github/paypal/paypal-android/supplements/2026-11-15-c5a36f0-23671a69/manifest.json`.
- Canonical attachment: `tracking/github/repos/paypal/paypal-android/evidence-attachments/github-71f2e4bd6e83f068dc81/attachment.json`, linked through `evidence_attachments` on the existing work item.
- All ten source files, the supplement manifest and attachment were read in full. Affected retained dependencies `ChromeCustomTabsClient.kt`, `UpdateClientConfigAPI.kt`, `DeviceInspector.kt`, the UpdateClientConfig GraphQL resource and Core manifest were also read fully. This is not yet a full read of the entire 3.2.0 ingest scope.

### Implementation Findings

1. **Browser-mediated launch:** `VenmoClient.start()` rejects a blank order ID, awaits an UpdateClientConfig call with funding source `venmo`, then opens the configured Venmo HTTPS URL with `channel=in-app` and `token=<orderId>` through `ChromeCustomTabsClient`. The helper uses `CustomTabsIntent.launchUrl`, without directly targeting the Venmo package. Downstream hosted/app-switch behavior is not established by this local launch code.
2. **Launch is not payment completion:** `VenmoStartResult.Success` means the Custom Tab launch returned successfully. A missing activity/browser produces a failure result. Server capture/settlement is not performed by this client; the separately read demo offers an explicit server completion step.
3. **Return parsing:** `finishStart()` reads `token`, `PayerID`, `approved` and `canceled` from intent data. Cancellation takes precedence if both status flags are true and does not require an order token. Approval needs nonempty token and payer ID, then returns Success with `approved=true`. Missing approval/cancellation becomes a malformed-status failure. These are parsed return values, not authenticated server payment state.
4. **NoResult documentation mismatch:** release notes describe NoResult for an unrelated intent. The implementation returns NoResult only when `intent.data` is null; an unrelated URI with data can instead yield Failure. Preserve this version-qualified discrepancy during ingestion.
5. **Return-validation boundary:** the complete method has no local scheme/host/path allowlist, saved-order correlation or server verification. It takes the caller-supplied Intent and stores no started-order state. Host routing/verified-link setup, expected-order correlation and server verification remain integration responsibilities. This is a static source boundary, not a reproduced exploit or a whole-application security assessment.
6. **Environment mapping:** production resolves to `https://account.venmo.com/go/web/paypal`; Sandbox resolves to `https://account.ext.live.venmo.com/go/web/paypal`. Debug additionally supports a CUSTOM override; the release variant does not. Do not substitute an inferred sandbox host or treat debug override support as a production capability.
7. **Configuration/exception boundary:** returned UpdateClientConfig success/failure is ignored, as the comment intends, but the call is awaited before the launch try/catch. That catch therefore does not guarantee conversion of every configuration/analytics exception into a Venmo failure result. The callback overload launches through its own scope and delivers normal results on Dispatchers.Main; no device/coroutine failure testing was performed.
8. **Analytics is not eligibility:** VenmoAnalytics reports events, order ID, `appSwitchEnabled=true` and installed-app telemetry. DeviceInspector checks `com.venmo` for this telemetry, but VenmoClient does not use that Boolean to gate launch. Neither telemetry nor this implementation proves account enablement, geographic availability or PayPal-only merchant eligibility.

The ten-file gap is now closed for this review. Known broader capsule omissions (for example, embedded binaries, excluded demo variants and external hosted behavior) are not silently promoted into evidence. No additional source collection is proposed at this point; deeper claims may still require separately approved evidence.

### Supplement Validation and Next Gate

- Ten files total 11,355 bytes. Each passed byte-size, SHA-256 and Git blob-ID verification; attachment identity and required-reading verification pass (12 attachment/read paths including manifests).
- Original snapshot and packet hashes remain intact; accepted evidence was not rewritten. Registry and cumulative wiki source/changelog are unchanged.
- Post-attachment offline validator retains the same 13 unrelated historical structural errors and one pending item, with no PayPal Android or attachment error. Global validation is not clean.
- Existing work item remains `awaiting_approval`, with no approved mode. Future capsule policy is unchanged; supplement attachment does not add a Venmo root for later release collections.
- Recommend **full additive ingestion of paypal-android@3.2.0 including this supplement**, preserving v3.1/v3.0/v2/v1 knowledge and recording the new payment flow, typed-result limits and return-validation cautions. Full-mode and any reading exception still require separate approval.
- No wiki ingestion, approval/claim, upstream build/test, browser/device/payment execution, commit or push was performed.
