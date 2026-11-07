# GitHub ingest packet

- Repository: `adyen/adyen-react-native`
- Work item: `github-01b194e7c644e7ff1f60`
- Snapshot: `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/manifest.json`
- Recommended mode: `delta`
- Review priority: `high`

## `@adyen/react-native`

- Version: `2.13.0` -> `2.14.0`
- Recommendation: `delta` / `high`
- Unchanged retained files: `293`

### Required reading

- `raw/github/adyen/adyen-react-native/releases/react-native/2.14.0/2026-11-07/manifest.json`
- `raw/github/adyen/adyen-react-native/releases/react-native/2.14.0/2026-11-07/release-notes.md`
- `raw/github/adyen/adyen-react-native/snapshots/2026-10-21-68acfa3/manifest.json`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/README.md`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/adyen-react-native.podspec`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/android/build.gradle`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/android/dependencies.gradle`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/android/gradle.properties`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/docs/Compatibility.md`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/docs/Customization.md`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/ios/Components/ApplePay/ApplePayModule.swift`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/ios/Views/CardView/CardComponentViewProxy.swift`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/src/components/CardView.tsx`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/src/core/configurations/ApplePayConfiguration.ts`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/src/plugin/setKotlinGradlePlugin.ts`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/src/plugin/withAdyenAndroid.ts`
- `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/manifest.json`
- `tracking/github/repos/adyen/adyen-react-native/comparisons/react-native/2.13.0--2.14.0/comparison.json`
- `tracking/github/repos/adyen/adyen-react-native/comparisons/react-native/2.13.0--2.14.0/comparison.md`
- `tracking/github/repos/adyen/adyen-react-native/comparisons/react-native/2.13.0--2.14.0/diff.patch`

### Upstream changes

- `modified` `.gitattributes`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `.github/workflows/android_agp9_build.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/e2e_test.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/pr_check.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/public_api_check.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/run_sonar.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.husky/pre-commit`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `README.md`: `retained-evidence` (snapshot-file)
- `modified` `adyen-react-native.podspec`: `retained-evidence` (snapshot-file)
- `modified` `android/build.gradle`: `retained-evidence` (snapshot-file)
- `modified` `android/dependencies.gradle`: `retained-evidence` (snapshot-file)
- `modified` `android/gradle.properties`: `retained-evidence` (snapshot-file)
- `modified` `api-extractor.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `docs/Compatibility.md`: `retained-evidence` (snapshot-file)
- `modified` `docs/Customization.md`: `retained-evidence` (snapshot-file)
- `added` `e2e-tests/scripts/configure-android-toolchain.js`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/scripts/configure-expo-app.js`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/scripts/resolve_rn_cli_version.sh`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `e2e-tests/scripts/setup.sh`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `etc/api/adyen-react-native.api.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/android/build.gradle`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/ios/AdyenExampleTests/Modules/CardComponentViewProxyLayoutTests.swift`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `example/ios/Podfile.lock`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `ios/Components/ApplePay/ApplePayModule.swift`: `retained-evidence` (snapshot-file)
- `modified` `ios/Views/CardView/CardComponentViewProxy.swift`: `retained-evidence` (snapshot-file)
- `modified` `scripts/__tests__/api-report-summary.test.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `scripts/__tests__/configure-android-toolchain.test.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `scripts/__tests__/post-api-report-comment.test.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `scripts/api-report-summary.js`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `scripts/post-api-report-comment.js`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/components/CardView.tsx`: `retained-evidence` (snapshot-file)
- `modified` `src/core/configurations/ApplePayConfiguration.ts`: `retained-evidence` (snapshot-file)
- `added` `src/plugin/__tests__/setKotlinGradlePlugin.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `src/plugin/setKotlinGradlePlugin.ts`: `retained-evidence` (snapshot-file)
- `modified` `src/plugin/withAdyenAndroid.ts`: `retained-evidence` (snapshot-file)
- `modified` `yarn.lock`: `intentional-policy-exclusion` (outside-capsule-policy)
