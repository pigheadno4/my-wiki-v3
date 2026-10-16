# GitHub ingest packet

- Repository: `paypal/paypal-ios`
- Work item: `github-5cce6532a34ea07a94ef`
- Snapshot: `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/manifest.json`
- Recommended mode: `delta`
- Review priority: `high`

## `paypal-ios`

- Version: `3.0.0` -> `3.1.0`
- Recommendation: `delta` / `high`
- Unchanged retained files: `151`

### Required reading

- `raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.0/2026-10-16/manifest.json`
- `raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.0/2026-10-16/release-notes.md`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/CHANGELOG.md`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Package.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/PayPal.podspec`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/README.md`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/CorePayments/PayPalCoreConstants.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/CorePayments/UIApplication+URLOpener.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionVariables.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/Models/PayPalCheckoutAnalyticsData+Analytics.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/Models/PayPalUserAction.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/PayPalClient.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/manifest.json`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/manifest.json`
- `tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.0.0--3.1.0/comparison.json`
- `tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.0.0--3.1.0/comparison.md`
- `tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.0.0--3.1.0/diff.patch`

### Upstream changes

- `modified` `.github/workflows/release.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.gitignore`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `CHANGELOG.md`: `retained-evidence` (snapshot-file)
- `modified` `Demo/Demo.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/Demo/Info.plist`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/Info.plist`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/_CodeSignature/CodeDirectory`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/_CodeSignature/CodeRequirements`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/_CodeSignature/CodeRequirements-1`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/_CodeSignature/CodeResources`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/_CodeSignature/CodeSignature`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/MagnesCryptoUtil.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/MagnesSystemConfigUtils.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/PPRiskMagnes-Swift.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/PPRiskMagnes.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Info.plist`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.abi.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.private.swiftinterface`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.swiftdoc`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.swiftinterface`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/module.modulemap`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/PPRiskMagnes`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/PrivacyInfo.xcprivacy`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Headers/MagnesCryptoUtil.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Headers/MagnesSystemConfigUtils.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Headers/PPRiskMagnes-Swift.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Headers/PPRiskMagnes.h`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Info.plist`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios-simulator.abi.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios-simulator.private.swiftinterface`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios-simulator.swiftdoc`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios-simulator.swiftinterface`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/x86_64-apple-ios-simulator.abi.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/x86_64-apple-ios-simulator.private.swiftinterface`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/x86_64-apple-ios-simulator.swiftdoc`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/x86_64-apple-ios-simulator.swiftinterface`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/Modules/module.modulemap`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/PPRiskMagnes`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/PrivacyInfo.xcprivacy`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Frameworks/XCFrameworks/PPRiskMagnes.xcframework/ios-arm64_x86_64-simulator/PPRiskMagnes.framework/_CodeSignature/CodeResources`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/README.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/getting-started/concepts-and-responsibilities.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/getting-started/install-and-setup.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/getting-started/which-guide-do-i-use.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/integration-guides/card-acdc.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/integration-guides/payment-buttons.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/integration-guides/paypal-checkout.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/integration-guides/troubleshooting.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Guides/migrate-v2-to-v3.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Package.swift`: `retained-evidence` (snapshot-file)
- `modified` `PayPal.podspec`: `retained-evidence` (snapshot-file)
- `modified` `PayPal.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `README.md`: `retained-evidence` (snapshot-file)
- `modified` `SampleApps/SPMTest/SPMTest.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Sources/CorePayments/PayPalCoreConstants.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/UIApplication+URLOpener.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/APIRequests/CreateShopperSessionVariables.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/Models/PayPalCheckoutAnalyticsData+Analytics.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/Models/PayPalUserAction.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/PayPalClient.swift`: `retained-evidence` (snapshot-file)
- `modified` `UnitTests/PayPalPaymentsTests/CreateShopperSessionAPI_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/PayPalPaymentsTests/PayPalWebCheckoutClient_CreateSession_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/TestShared/MockCreateShopperSessionAPI.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
