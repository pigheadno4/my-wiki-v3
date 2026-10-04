# GitHub ingest packet

- Repository: `stripe/stripe-react-native`
- Work item: `github-9be7291cb2f1d1ffc9b4`
- Snapshot: `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `@stripe/stripe-react-native`

- Version: `0.79.0` -> `0.80.0`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `219`

### Required reading

- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.80.0/2026-10-04/manifest.json`
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.80.0/2026-10-04/release-notes.md`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-6bbf9d5/manifest.json`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/CHANGELOG.md`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/CollectBankAccountLauncherManager.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/FinancialConnectionsSheetManager.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/StripeSdkModule.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/StripeSdkPackage.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/checkout/CheckoutPaymentElementView.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/checkout/CheckoutPaymentElementViewManager.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/checkout/NativeCheckoutControllerInstance.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/android/src/main/java/com/reactnativestripesdk/utils/Mappers.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/ios/Checkout/CheckoutPaymentElementContainerView.swift`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/ios/Checkout/NativeCheckoutControllerInstance.swift`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/ios/FinancialConnections.swift`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/ios/NewArch/CheckoutPaymentElementViewComponentView.h`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/ios/NewArch/CheckoutPaymentElementViewComponentView.mm`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/ios/StripeSdkImpl.swift`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/package.json`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/src/checkout/createCheckout.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/src/components/CheckoutPaymentElementView.tsx`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/src/specs/NativeCheckoutPaymentElement.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/src/types/FinancialConnections.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/files/src/types/PaymentMethod.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-04-ce9c1bf/manifest.json`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.79.0--0.80.0/comparison.json`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.79.0--0.80.0/comparison.md`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.79.0--0.80.0/diff.patch`

### Upstream changes

- `modified` `CHANGELOG.md`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/CollectBankAccountLauncherManager.kt`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/FinancialConnectionsSheetManager.kt`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/StripeSdkModule.kt`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/StripeSdkPackage.kt`: `retained-evidence` (snapshot-file)
- `added` `android/src/main/java/com/reactnativestripesdk/checkout/CheckoutPaymentElementView.kt`: `retained-evidence` (snapshot-file)
- `added` `android/src/main/java/com/reactnativestripesdk/checkout/CheckoutPaymentElementViewManager.kt`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/checkout/NativeCheckoutControllerInstance.kt`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/utils/Mappers.kt`: `retained-evidence` (snapshot-file)
- `modified` `android/src/test/java/com/reactnativestripesdk/checkout/NativeCheckoutControllerInstanceTest.kt`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `android/src/test/java/com/reactnativestripesdk/mappers/MappersTest.kt`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `etc/stripe-react-native.api.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/ios/Podfile.lock`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/src/Config.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/src/screens/CollectBankAccountScreen.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `ios/Checkout/CheckoutPaymentElementContainerView.swift`: `retained-evidence` (snapshot-file)
- `modified` `ios/Checkout/NativeCheckoutControllerInstance.swift`: `retained-evidence` (snapshot-file)
- `modified` `ios/FinancialConnections.swift`: `retained-evidence` (snapshot-file)
- `added` `ios/NewArch/CheckoutPaymentElementViewComponentView.h`: `retained-evidence` (snapshot-file)
- `added` `ios/NewArch/CheckoutPaymentElementViewComponentView.mm`: `retained-evidence` (snapshot-file)
- `modified` `ios/StripeSdkImpl.swift`: `retained-evidence` (snapshot-file)
- `modified` `ios/Tests/MappersTests.swift`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `ios/Tests/NativeCheckoutControllerInstanceTests.swift`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `package.json`: `retained-evidence` (snapshot-file)
- `added` `src/checkout/__tests__/CheckoutPaymentElementView.test.tsx`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `src/checkout/createCheckout.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/components/CheckoutPaymentElementView.tsx`: `retained-evidence` (snapshot-file)
- `added` `src/specs/NativeCheckoutPaymentElement.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/types/FinancialConnections.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/types/PaymentMethod.ts`: `retained-evidence` (snapshot-file)
