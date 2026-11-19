# GitHub ingest packet

- Repository: `paypal/paypal-ios`
- Work item: `github-a24ad729631b9a2aa48d`
- Snapshot: `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/manifest.json`
- Recommended mode: `delta`
- Review priority: `high`

## `paypal-ios`

- Version: `3.1.1` -> `3.2.0`
- Recommendation: `delta` / `high`
- Unchanged retained files: `144`

### Required reading

- `raw/github/paypal/paypal-ios/releases/paypal-ios/3.2.0/2026-11-15/manifest.json`
- `raw/github/paypal/paypal-ios/releases/paypal-ios/3.2.0/2026-11-15/release-notes.md`
- `raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/manifest.json`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/CHANGELOG.md`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Demo/Demo/Models/CreateOrderParams.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Demo/Demo/SwiftUIComponents/FeatureSelectionView.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Package.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/PayPal.podspec`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CardPayments/CardClient.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CardPayments/CardError.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CorePayments/AnalyticsEventData.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CorePayments/Networking/AnalyticsService.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CorePayments/Networking/NetworkingError.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CorePayments/PayPalCheckoutAnalyticsData.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CorePayments/PayPalCoreConstants.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CorePayments/UIApplication+URLOpener.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/CorePayments/WebAuthenticationSession.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/PayPalPayments/Models/PayPalCheckoutAnalyticsData+Analytics.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/PayPalPayments/PayPalClient.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/PayPalPayments/PayPalError.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/files/Sources/PaymentButtons/PaymentButtonEdges.swift`
- `raw/github/paypal/paypal-ios/snapshots/2026-11-15-7eb8f7b/manifest.json`
- `tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.1.1--3.2.0/comparison.json`
- `tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.1.1--3.2.0/comparison.md`
- `tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.1.1--3.2.0/diff.patch`

### Upstream changes

- `modified` `CHANGELOG.md`: `retained-evidence` (snapshot-file)
- `modified` `Demo/Demo.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/Demo/Info.plist`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/Demo/Models/CreateOrderParams.swift`: `retained-evidence` (snapshot-file)
- `modified` `Demo/Demo/SwiftUIComponents/FeatureSelectionView.swift`: `retained-evidence` (snapshot-file)
- `added` `Demo/Demo/VenmoPayments/VenmoPaymentState.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Demo/Demo/VenmoPayments/VenmoPaymentsView.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Demo/Demo/VenmoPayments/VenmoViewModel.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Package.swift`: `retained-evidence` (snapshot-file)
- `modified` `PayPal.podspec`: `retained-evidence` (snapshot-file)
- `modified` `PayPal.xcodeproj/project.pbxproj`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `PayPal.xcodeproj/xcshareddata/xcschemes/UnitTests.xcscheme`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `PayPal.xcodeproj/xcshareddata/xcschemes/VenmoPayments.xcscheme`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `PayPal.xcodeproj/xcshareddata/xcschemes/VenmoPaymentsTests.xcscheme`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Sources/CardPayments/CardClient.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CardPayments/CardError.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/AnalyticsEventData.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/Networking/AnalyticsService.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/Networking/NetworkingError.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/PayPalCheckoutAnalyticsData.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/PayPalCoreConstants.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/UIApplication+URLOpener.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/CorePayments/WebAuthenticationSession.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/Models/PayPalCheckoutAnalyticsData+Analytics.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/PayPalClient.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PayPalPayments/PayPalError.swift`: `retained-evidence` (snapshot-file)
- `modified` `Sources/PaymentButtons/PaymentButtonEdges.swift`: `retained-evidence` (snapshot-file)
- `added` `Sources/VenmoPayments/CoreEnvironment+Venmo.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Sources/VenmoPayments/PrivacyInfo.xcprivacy`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Sources/VenmoPayments/VenmoCheckoutRequest.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Sources/VenmoPayments/VenmoCheckoutResult.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Sources/VenmoPayments/VenmoClient.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Sources/VenmoPayments/VenmoError.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/PayPalPaymentsTests/PayPalWebCheckoutClient_CreateSession_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/PaymentsCoreTests/AnalyticsEventData_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/PaymentsCoreTests/AnalyticsService_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/TestShared/MockURLOpener.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UnitTests/TestShared/MockWebAuthenticationSession.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UnitTests/VenmoPaymentsTests/CoreEnvironment+Venmo_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UnitTests/VenmoPaymentsTests/VenmoCheckoutRequest_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UnitTests/VenmoPaymentsTests/VenmoClient_CheckoutAppSwitch_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UnitTests/VenmoPaymentsTests/VenmoClient_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UnitTests/VenmoPaymentsTests/VenmoError_Tests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
