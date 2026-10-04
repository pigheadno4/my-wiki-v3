# GitHub ingest packet

- Repository: `braintree/braintree_android`
- Work item: `github-50a0160c94669e522efa`
- Snapshot: `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/manifest.json`
- Recommended mode: `delta`
- Review priority: `normal`

## `braintree-android`

- Version: `5.32.0` -> `5.33.0`
- Recommendation: `delta` / `normal`
- Unchanged retained files: `382`

### Required reading

- `raw/github/braintree/braintree_android/releases/braintree-android/5.33.0/2026-10-04/manifest.json`
- `raw/github/braintree/braintree_android/releases/braintree-android/5.33.0/2026-10-04/release-notes.md`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/CHANGELOG.md`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/README.md`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/build.gradle`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/cardfields/CardFieldsViewModel.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardCvvField.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardExpirationField.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFieldBaseTextInputField.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFields.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFieldsController.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFieldsVisualTransformations.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardNumberField.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CvvHintPopup.kt`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/res/values/dimens.xml`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/UIComponents/src/main/res/values/strings_card_fields.xml`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/build.gradle`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/files/v5_MIGRATION_GUIDE.md`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/manifest.json`
- `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/manifest.json`
- `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/comparison.json`
- `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/comparison.md`
- `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/diff.patch`

### Upstream changes

- `modified` `CHANGELOG.md`: `retained-evidence` (snapshot-file)
- `deleted` `Demo/src/main/java/com/braintreepayments/demo/ComposeButtonsFragment.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `Demo/src/main/java/com/braintreepayments/demo/ComposeUIComponentsFragment.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/main/java/com/braintreepayments/demo/MainFragment.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/main/res/navigation/nav_graph.xml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `Demo/src/main/res/values/strings.xml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `LocalPayment/src/androidTest/java/com/braintreepayments/api/localpayment/LocalPaymentApiTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `LocalPayment/src/androidTest/java/com/braintreepayments/api/localpayment/LocalPaymentClientTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `README.md`: `retained-evidence` (snapshot-file)
- `modified` `UIComponents/build.gradle`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/androidTest/java/com/braintreepayments/api/uicomponents/compose/CardCvvFieldTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UIComponents/src/androidTest/java/com/braintreepayments/api/uicomponents/compose/CardExpirationFieldTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UIComponents/src/androidTest/java/com/braintreepayments/api/uicomponents/compose/CardFieldsFormTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UIComponents/src/androidTest/java/com/braintreepayments/api/uicomponents/compose/CardNumberFieldTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/cardfields/CardFieldsViewModel.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardCvvField.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardExpirationField.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFieldBaseTextInputField.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFields.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFieldsController.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardFieldsVisualTransformations.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CardNumberField.kt`: `retained-evidence` (snapshot-file)
- `added` `UIComponents/src/main/java/com/braintreepayments/api/uicomponents/compose/CvvHintPopup.kt`: `retained-evidence` (snapshot-file)
- `modified` `UIComponents/src/main/res/values/dimens.xml`: `retained-evidence` (snapshot-file)
- `modified` `UIComponents/src/main/res/values/strings_card_fields.xml`: `retained-evidence` (snapshot-file)
- `modified` `UIComponents/src/test/java/com/braintreepayments/api/uicomponents/cardfields/CardFieldsViewModelUnitTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UIComponents/src/test/java/com/braintreepayments/api/uicomponents/compose/CardFieldsControllerUnitTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UIComponents/src/test/java/com/braintreepayments/api/uicomponents/compose/CardFieldsUnitTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `UIComponents/src/test/java/com/braintreepayments/api/uicomponents/compose/CardFieldsVisualTransformationUnitTest.kt`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `build.gradle`: `retained-evidence` (snapshot-file)
- `modified` `gradle/libs.versions.toml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `v5_MIGRATION_GUIDE.md`: `retained-evidence` (snapshot-file)
