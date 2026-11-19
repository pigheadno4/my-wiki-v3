# PayPal iOS Collection Review - 2026-11-15

## Release and Newer-Major Guard

- Approved scope: recheck, newer-major guard and findings before ingestion.
- Registry tracks stable package-qualified majors `paypal-ios@2` and `paypal-ios@3`; no registry change was made.
- Future collection found `paypal-ios@3.2.0`, published 2026-11-02T19:55:38Z, at exact SHA `7eb8f7b7f9162e8f8114abae7f5dba9b525eae64`.
- Independent live semantic-tag inspection found stable majors 0, 1, 2 and 3. The newest stable tag is 3.2.0; no stable v4 or higher was found.
- Prior ingested release remains `paypal-ios@3.1.1`, SHA `de98414f5cf74dc3db2239a4828b4760ef391d20`, wiki last-ingest date 2026-10-16.
- Collected work item `github-a24ad729631b9a2aa48d` is awaiting approval; no approved mode or ingest claim.

## Preliminary Findings

Complete retained 3.2.0 release notes, Package.swift and PayPal.podspec were read, along with prior source context and packet navigation. This is not yet a full semantic review of every changed source file or the missing Venmo implementation.

- Release notes announce the new VenmoPayments module: VenmoClient completion and async-throws start methods, handleReturnURL, result orderID/payerID, VenmoError and cancellation helper. Their claimed app-versus-Safari routing remains release-note intent until the full implementation is reviewed; Android behavior is not assumed to apply.
- Package.swift adds a VenmoPayments library and CorePayments-dependent target with its privacy resource. Podspec adds the parallel PayPal/VenmoPayments subspec. Both still declare iOS 16; Swift package tool version and pod Swift version are 5.9. Package installation/build and published artifact availability were not tested.
- This supersedes no-native-Venmo claims only for the new version after ingestion; prior v1/v2/3.0/3.1 evidence must remain version-qualified history. Source/API presence is not merchant enablement, geographic availability, settlement or tested device behavior.

## Missing Exact-Release Evidence

The base snapshot retains 18 modified files and 144 unchanged files, but excludes the entire new Sources/VenmoPayments module, its new demo folder and changed demo Info.plist. The packet has empty automated gap arrays because these are policy exclusions; that does not establish semantic sufficiency.

Recommend collecting these ten text files as an immutable supplement at **3.2.0 SHA `7eb8f7b7f9162e8f8114abae7f5dba9b525eae64`**, attaching them to the existing item, and sharing findings before requesting full additive ingestion:

```text
Sources/VenmoPayments/CoreEnvironment+Venmo.swift
Sources/VenmoPayments/PrivacyInfo.xcprivacy
Sources/VenmoPayments/VenmoCheckoutRequest.swift
Sources/VenmoPayments/VenmoCheckoutResult.swift
Sources/VenmoPayments/VenmoClient.swift
Sources/VenmoPayments/VenmoError.swift
Demo/Demo/VenmoPayments/VenmoPaymentState.swift
Demo/Demo/VenmoPayments/VenmoPaymentsView.swift
Demo/Demo/VenmoPayments/VenmoViewModel.swift
Demo/Demo/Info.plist
```

Script recommendation is delta/high priority. Operator recommendation is full additive after supplement review, because a new payment flow is a full-mode signal. This is not an executed mode override or ingestion approval. Accepted evidence, tests exclusion and future registry scope remain unchanged.

## Separate Later Documentation Boundary

Live main is `f557131331147694b5bd9c27b023571ad667e78e`, seven commits ahead of 3.2.0, merged 2026-11-12. The live API changed-path inventory identifies four documentation-only endpoint changes:

```text
Guides/README.md
Guides/getting-started/install-and-setup.md
Guides/getting-started/which-guide-do-i-use.md
Guides/integration-guides/venmo-checkout.md
```

These are metadata-preview findings only. Guide bodies were not collected/read, and commit titles cannot establish their requirements. Do not mix this later main documentation into the released 3.2.0 snapshot or infer merchant/app-version eligibility from titles. A separately approved four-file main-SHA collection/review can follow; no collect-ref or supplement for this boundary was run.

## Integrity and Approval Boundary

- Current snapshot: 162 files / 382,507 bytes. Prior snapshot: 162 files / 378,154 bytes. All 324 file sizes, SHA-256 and Git blob IDs pass; release notes, packet/snapshot and comparison hashes pass.
- All 43 upstream release paths have recorded dispositions: 18 retained and 25 excluded. Classification completeness is not proof that the missing payment implementation has been reviewed.
- Offline collection validation reports the same 13 unrelated historical structural errors and one pending item; none reference PayPal iOS. Global validation is not clean. Scoped whitespace and receipt-link checks pass.
- Original snapshot policy and prior history were preserved. No wiki edit, supplement collection, approval/claim, ingestion, build/test, device/browser/payment execution, commit or push was performed.
- Next gate: user approval for the exact ten-file release-SHA supplement. Full ingestion remains a later gate; all earlier history must be preserved.

## References

- [3.2.0 release](https://github.com/paypal/paypal-ios/releases/tag/3.2.0)
- [Release snapshot](../../../../../raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/manifest.json)
- [Review packet](ingest-packets/github-a24ad729631b9a2aa48d/packet.md)
- [Release comparison](comparisons/paypal-ios/3.1.1--3.2.0/comparison.md)
- [Later documentation comparison](https://github.com/paypal/paypal-ios/compare/7eb8f7b7f9162e8f8114abae7f5dba9b525eae64...f557131331147694b5bd9c27b023571ad667e78e)

## Approved Supplement Review

This section supersedes the earlier pending-supplement stage only. The user approved collecting the ten listed files, not ingestion. All ten were collected at exact release SHA `7eb8f7b7f9162e8f8114abae7f5dba9b525eae64` and read completely. Their total size is 24,339 bytes; file sizes, SHA-256 hashes and Git blob IDs pass. The original snapshot is unchanged.

- [Supplement manifest](../../../../../raw/github/paypal/paypal-ios/supplements/2026-11-15-7eb8f7b-763917b6/manifest.json)
- [Canonical evidence attachment](evidence-attachments/github-a24ad729631b9a2aa48d/attachment.json), linked to the existing awaiting-approval item.

### Implementation Findings

- `VenmoClient(config:)` exposes completion and async-throws `start(orderID:)` methods. It opens the HTTPS `/go/web/paypal?channel=in-app&token=...` URL with universal-links-only disabled. The installed-app check supplies analytics; it does not select the route. Production and sandbox hosts are `account.venmo.com` and `account.ext.live.venmo.com`. This client does not implement an ASWebAuthenticationSession flow.
- Unlike the Android launch-result API, successful URL opening does not resolve the iOS checkout result. The same retained client must receive `handleReturnURL(_:)`. Completion delivery is guarded once per start and dispatched to the main queue. Dismissal without a return URL has no automatic completion, timeout or cancellation path here; the async continuation can remain pending. The demo's state reset is not cancellation of the pending SDK flow.
- Return parsing recognizes `canceled=true`, or `approved=true` plus nonempty `token` and exact-key `PayerID`. Cancellation takes precedence. The client does not validate the return scheme/host/path or correlate the returned token with the started order. It consumes its pending callback before parsing, so forwarding an unrelated URL can terminate that pending attempt. Merchants should validate expected returns before forwarding, correlate the order and verify payment server-side. A single callback slot is not concurrent-checkout coordination.
- UpdateClientConfig is awaited with funding source `venmo`; failures are caught and checkout continues. This is not the Android failure-handling boundary. An approved return supplies order/payer data, not capture or settlement confirmation.
- `VenmoCheckoutRequest` declares `appSwitchIfEligible` and `currency`, with a web-authentication-session comment, but the collected client accepts only an order ID and never consumes this struct. Do not document these fields as working routing/currency controls or infer a web-session implementation from the unused error helper.
- The SwiftUI demo keeps the client in its view model and forwards `.onOpenURL`. It creates an order through the sample server with `payment_source.venmo`, return/cancel URLs and an app-switch context whose source is `NATIVE_APP`, then starts checkout and separately authorizes/captures through that server. It uses the created order ID for completion, without an explicit comparison to the parsed return token. This demonstrates integration order, not production payment verification.
- Demo Info.plist includes the Venmo query scheme and the sample app's return scheme. Project/entitlement wiring was not collected. The privacy manifest is a declaration, not runtime/compliance validation. No device, build, transaction, account-eligibility or geographic-availability testing was performed.

### Remaining Boundary

The ten-file exact-release implementation gap is closed. Later main-branch guides remain separate and were not collected. Registry policy, original snapshots, packets and all cumulative wiki history are unchanged. The work item remains `awaiting_approval`, with no approved mode or ingest claim. Recommend full additive ingestion of `paypal-ios@3.2.0` including this attachment, preserving every earlier version; that requires separate user approval.
