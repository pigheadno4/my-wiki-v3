# GitHub ingest packet

- Repository: `paypal/paypal-android`
- Work item: `github-fce7ee241c398cc73695`
- Snapshot: `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/manifest.json`
- Recommended mode: `delta`
- Review priority: `high`

## `paypal-android`

- Version: `3.0.0` -> `3.1.0`
- Recommendation: `delta` / `high`
- Unchanged retained files: `260`

### Required reading

- `raw/github/paypal/paypal-android/releases/paypal-android/3.1.0/2026-10-16/manifest.json`
- `raw/github/paypal/paypal-android/releases/paypal-android/3.1.0/2026-10-16/release-notes.md`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/Demo/src/main/java/com/paypal/android/api/model/UserActionSelected.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/manifest.json`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CHANGELOG.md`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/api/CorePayments.api`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/src/main/java/com/paypal/android/corepayments/api/CreateShopperSessionWithAppSwitchEligibilityAPI.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/src/main/java/com/paypal/android/corepayments/model/CreateShopperSessionWithAppSwitchEligibilityModels.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/src/main/java/com/paypal/android/corepayments/model/CreateShopperSessionWithAppSwitchEligibilityParams.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/src/main/java/com/paypal/android/corepayments/model/TokenType.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/api/model/serialization/OrderModels.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/customenvironment/DemoEnvironmentSettings.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/customenvironment/SettingsView.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/customenvironment/SettingsViewModel.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/models/OrderRequest.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/ui/paypal/PayPalCheckoutViewModel.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/ui/vaultcard/VaultCardViewModel.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/usecase/CreateOrderUseCase.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/FraudProtection/src/main/java/com/paypal/android/fraudprotection/PayPalDataCollector.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/PayPalPayments/src/main/java/com/paypal/android/paypalpayments/PayPalClient.kt`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/version.properties`
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/manifest.json`
- `tracking/github/repos/paypal/paypal-android/comparisons/paypal-android/3.0.0--3.1.0/comparison.json`
- `tracking/github/repos/paypal/paypal-android/comparisons/paypal-android/3.0.0--3.1.0/comparison.md`
- `tracking/github/repos/paypal/paypal-android/comparisons/paypal-android/3.0.0--3.1.0/diff.patch`

### Files absent from current snapshot

Snapshot absence is not proof of upstream deletion. `not-listed` refers only to the supplied upstream change inventory.

- `Demo/src/main/java/com/paypal/android/api/model/UserActionSelected.kt`: `upstream-deletion`; upstream: `deleted`

### Upstream changes

- `modified` `CHANGELOG.md`: `retained-evidence` (snapshot-file)
- `modified` `CorePayments/api/CorePayments.api`: `retained-evidence` (snapshot-file)
- `modified` `CorePayments/src/main/java/com/paypal/android/corepayments/api/CreateShopperSessionWithAppSwitchEligibilityAPI.kt`: `retained-evidence` (snapshot-file)
- `modified` `CorePayments/src/main/java/com/paypal/android/corepayments/model/CreateShopperSessionWithAppSwitchEligibilityModels.kt`: `retained-evidence` (snapshot-file)
- `modified` `CorePayments/src/main/java/com/paypal/android/corepayments/model/CreateShopperSessionWithAppSwitchEligibilityParams.kt`: `retained-evidence` (snapshot-file)
- `modified` `CorePayments/src/main/java/com/paypal/android/corepayments/model/TokenType.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/androidTest/java/com/paypal/android/CardApproveOrderTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/androidTest/java/com/paypal/android/CardVaultTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/androidTest/java/com/paypal/android/PayPalCheckoutTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/androidTest/java/com/paypal/android/PayPalVaultTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/androidTest/java/com/paypal/android/robots/DemoRobot.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Demo/src/androidTest/java/com/paypal/android/uishared/enums/ReturnToAppStrategyOption.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/debug/java/com/paypal/android/customenvironment/CustomEnvironmentRepository.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `deleted` `Demo/src/main/java/com/paypal/android/api/model/UserActionSelected.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/api/model/serialization/OrderModels.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/customenvironment/DemoEnvironmentSettings.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/customenvironment/SettingsView.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/customenvironment/SettingsViewModel.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/models/OrderRequest.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/ui/paypal/PayPalCheckoutViewModel.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/ui/vaultcard/VaultCardViewModel.kt`: `retained-evidence` (snapshot-file)
- `modified` `Demo/src/main/java/com/paypal/android/usecase/CreateOrderUseCase.kt`: `retained-evidence` (snapshot-file)
- `added` `Docs/README.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/android-migrate-v2-to-v3.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/getting-started/android-concepts-and-responsibilities.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/getting-started/android-install-and-setup.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/getting-started/android-which-guide-do-i-use.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/integration-guides/android-card-acdc.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/integration-guides/android-payment-buttons.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/integration-guides/android-paypal-checkout.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Docs/integration-guides/android-troubleshooting.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `FraudProtection/libs/android-magnessdk-5.5.1.jar`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `FraudProtection/src/debug/java/com/paypal/android/fraudprotection/CoreConfigMagnesExt.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `FraudProtection/src/main/java/com/paypal/android/fraudprotection/PayPalDataCollector.kt`: `retained-evidence` (snapshot-file)
- `modified` `FraudProtection/src/release/java/com/paypal/android/fraudprotection/CoreConfigMagnesExt.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `FraudProtection/src/test/java/com/paypal/android/fraudprotection/PayPalDataCollectorUnitTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `PayPalPayments/src/main/java/com/paypal/android/paypalpayments/PayPalClient.kt`: `retained-evidence` (snapshot-file)
- `modified` `version.properties`: `retained-evidence` (snapshot-file)
