# GitHub ingest packet

- Repository: `stripe/stripe-react-native`
- Work item: `github-e889941d7b5280b9c509`
- Snapshot: `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `@stripe/stripe-react-native`

- Version: `0.83.0` -> `0.84.0`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `234`

### Required reading

- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.84.0/2026-10-29/manifest.json`
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.84.0/2026-10-29/release-notes.md`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-0f28895/manifest.json`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/CHANGELOG.md`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/MIGRATING.md`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/README.md`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/android/gradle.properties`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/android/src/main/java/com/reactnativestripesdk/PaymentSheetManager.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/android/src/main/java/com/reactnativestripesdk/checkout/CheckoutConfigurationMapper.kt`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/ios/Checkout/CheckoutConfigurationMapper.swift`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/package.json`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/checkout/createCheckout.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/components/CheckoutCurrencySelectorElementView.tsx`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/components/CheckoutPaymentElementView.tsx`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/connect/EmbeddedComponent.tsx`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/hooks/useCheckout.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/index.tsx`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/plugin/withStripe.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/types/Checkout.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/src/types/index.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/files/stripe-react-native.podspec`
- `raw/github/stripe/stripe-react-native/snapshots/2026-10-29-33ef1ee/manifest.json`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.83.0--0.84.0/comparison.json`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.83.0--0.84.0/comparison.md`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.83.0--0.84.0/diff.patch`

### Upstream changes

- `modified` `CHANGELOG.md`: `retained-evidence` (snapshot-file)
- `modified` `CONTRIBUTING.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `MIGRATING.md`: `retained-evidence` (snapshot-file)
- `modified` `README.md`: `retained-evidence` (snapshot-file)
- `modified` `android/gradle.properties`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/PaymentSheetManager.kt`: `retained-evidence` (snapshot-file)
- `modified` `android/src/main/java/com/reactnativestripesdk/checkout/CheckoutConfigurationMapper.kt`: `retained-evidence` (snapshot-file)
- `added` `android/src/test/java/com/reactnativestripesdk/PaymentSheetCallbackTest.kt`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `android/src/test/java/com/reactnativestripesdk/PaymentSheetManagerHostTest.kt`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `android/src/test/java/com/reactnativestripesdk/checkout/ShippingAddressAppearanceMapperTest.kt`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `bitrise.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/android-only/paymentsheet-customFlow-canceled.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/checkout-confirmation.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/checkout-mutations.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `e2e-tests/checkout-shipping-address.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/checkout.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/helpers/checkout-card.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `e2e-tests/helpers/checkout-open-card.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/helpers/checkout-shipping.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `etc/stripe-react-native.api.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/ios/Podfile.lock`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/package.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/src/screens/Checkout/CheckoutCartScreen.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/src/screens/Checkout/playgroundConfig.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/yarn.lock`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `ios/Checkout/CheckoutConfigurationMapper.swift`: `retained-evidence` (snapshot-file)
- `modified` `ios/Tests/CheckoutConfigurationMapperTests.swift`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `ios/Tests/ShippingAddressAppearanceMapperTests.swift`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `package.json`: `retained-evidence` (snapshot-file)
- `modified` `scripts/test-expo-project`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `scripts/update-expo-plugins.js`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/checkout/createCheckout.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/components/CheckoutCurrencySelectorElementView.tsx`: `retained-evidence` (snapshot-file)
- `modified` `src/components/CheckoutPaymentElementView.tsx`: `retained-evidence` (snapshot-file)
- `modified` `src/connect/EmbeddedComponent.tsx`: `retained-evidence` (snapshot-file)
- `modified` `src/connect/__tests__/EmbeddedComponent.test.tsx`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `src/connect/analytics/__tests__/ComponentAnalyticsClient.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `src/hooks/useCheckout.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/index.tsx`: `retained-evidence` (snapshot-file)
- `modified` `src/plugin/__tests__/withStripe-test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `src/plugin/withStripe.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/types/Checkout.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/types/index.ts`: `retained-evidence` (snapshot-file)
- `modified` `stripe-react-native.podspec`: `retained-evidence` (snapshot-file)
- `modified` `stripe_spm.rb`: `intentional-policy-exclusion` (outside-capsule-policy)
