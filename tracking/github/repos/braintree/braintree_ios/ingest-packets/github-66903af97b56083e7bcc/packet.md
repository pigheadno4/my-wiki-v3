# GitHub ingest packet

- Repository: `braintree/braintree_ios`
- Work item: `github-66903af97b56083e7bcc`
- Snapshot: `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `braintree-ios`

- Version: `7.12.0` -> `7.13.0`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `277`

### Required reading

- `raw/github/braintree/braintree_ios/releases/braintree-ios/7.13.0/2026-10-04/manifest.json`
- `raw/github/braintree/braintree_ios/releases/braintree-ios/7.13.0/2026-10-04/release-notes.md`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Braintree.podspec`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/CHANGELOG.md`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Demo/Application/Features/ApplePayView.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Package.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/README.md`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeCore/BTCoreConstants.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeCore/BTHTTP.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeCore/Info.plist`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeCore/UIApplication+BackgroundTaskManaging.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreePayPal/BTPayPalClient.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreePayPal/BTPayPalError.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeUIComponents/CardFields/CVVField/CVVFieldViewModel.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeUIComponents/CardFields/CardNumberField/CardNumberFieldValidator.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/Sources/BraintreeUIComponents/CardFields/Shared/CardBrand.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/files/V7_MIGRATION.md`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/manifest.json`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/files/Sources/BraintreeCore/Analytics/BackgroundTaskManaging.swift`
- `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/manifest.json`
- `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.12.0--7.13.0/comparison.json`
- `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.12.0--7.13.0/comparison.md`
- `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.12.0--7.13.0/diff.patch`

### Files absent from current snapshot

Snapshot absence is not proof of upstream deletion. `not-listed` refers only to the supplied upstream change inventory.

- `Sources/BraintreeCore/Analytics/BackgroundTaskManaging.swift`: `upstream-deletion`; upstream: `deleted`

### Upstream changes

- `modified` `Braintree.podspec`: `retained-evidence` (snapshot-file)
- `modified` `Braintree.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `CHANGELOG.md`: `retained-evidence` (snapshot-file)
- `modified` `CLAUDE.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/Application/Features/ApplePayView.swift`: `retained-evidence` (snapshot-file)
- `modified` `Demo/Application/Supporting Files/Braintree-Demo-Info.plist`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/Demo.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Package.swift`: `retained-evidence` (snapshot-file)
- `modified` `Podfile`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Podfile.lock`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `README.md`: `retained-evidence` (snapshot-file)
- `modified` `SampleApps/CarthageTest/CarthageTest.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Sources/BraintreeCore/Analytics/BackgroundTaskManaging.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreeCore/BTCoreConstants.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreeCore/BTHTTP.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreeCore/Info.plist`: `retained-evidence` (snapshot-file)
- `added` `Sources/BraintreeCore/UIApplication+BackgroundTaskManaging.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreePayPal/BTPayPalClient.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreePayPal/BTPayPalError.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreeUIComponents/CardFields/CVVField/CVVFieldViewModel.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreeUIComponents/CardFields/CardNumberField/CardNumberFieldValidator.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/BraintreeUIComponents/CardFields/Shared/CardBrand.swift`: `retained-evidence` (snapshot-file)
- `deleted` `UnitTests/BraintreeCoreTests/Analytics/MockBackgroundTaskManager.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/BraintreeCoreTests/BTHTTP_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/BraintreeCoreTests/BTWebAuthenticationSession_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/BraintreePayPalTests/BTPayPalClient_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/BraintreeTestShared/MockAPIClient.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UnitTests/BraintreeTestShared/MockBackgroundTaskManager.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/BraintreeUIComponentsTests/CardNumberFieldValidatorTests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `V7_MIGRATION.md`: `retained-evidence` (snapshot-file)
