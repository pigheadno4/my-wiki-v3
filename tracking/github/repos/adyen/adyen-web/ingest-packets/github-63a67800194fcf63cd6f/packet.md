# GitHub ingest packet

- Repository: `adyen/adyen-web`
- Work item: `github-63a67800194fcf63cd6f`
- Snapshot: `raw/github/adyen/adyen-web/snapshots/2026-11-08-6ccc03f/manifest.json`
- Recommended mode: `delta`
- Review priority: `high`

## `@adyen/adyen-web`

- Version: `6.48.0` -> `6.48.1`
- Recommendation: `delta` / `high`
- Unchanged retained files: `220`

### Required reading

- `raw/github/adyen/adyen-web/releases/adyen-web/6.48.1/2026-11-08/manifest.json`
- `raw/github/adyen/adyen-web/releases/adyen-web/6.48.1/2026-11-08/release-notes.md`
- `raw/github/adyen/adyen-web/snapshots/2026-11-08-6ccc03f/files/package.json`
- `raw/github/adyen/adyen-web/snapshots/2026-11-08-6ccc03f/files/packages/lib/package.json`
- `raw/github/adyen/adyen-web/snapshots/2026-11-08-6ccc03f/manifest.json`
- `raw/github/adyen/adyen-web/snapshots/2026-11-08-a05c118/manifest.json`
- `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.48.0--6.48.1/comparison.json`
- `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.48.0--6.48.1/comparison.md`
- `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.48.0--6.48.1/diff.patch`

### Upstream changes

- `modified` `.github/workflows/.size-limit.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/automated-a11y.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/automated-visual.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/e2e-dist-tests.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/e2e-tests.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/gh-release.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/npm-publish.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/release-notifications.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/release-snapshot.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/release.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/sonarcloud.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/strict-typescript.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/unit-tests.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/update-screenshots.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `.github/workflows/validate-locales.yml`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `package.json`: `retained-evidence` (snapshot-file)
- `modified` `packages/e2e-playwright/package.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/.storybook/preview.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/CHANGELOG.md`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `packages/lib/config/rollup.size.js`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/config/setupTests.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/jest.config.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/package.json`: `retained-evidence` (snapshot-file)
- `modified` `packages/lib/src/components/AfterPay/AfterPay.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/Boleto/Boleto.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/Iris/Iris.test.tsx`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/Iris/Iris.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/Iris/components/IrisComponent.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/Iris/utils.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/Iris/utils.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/PayTo/PayTo.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/RatePay/RatePay.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/RatePay/RatePayDirectDebit.test.ts`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `packages/lib/src/components/UPI/UPI.scss`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/UPI/UPI.test.tsx`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/UPI/UPI.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/internal/Await/Await.test.tsx`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/internal/QRLoader/QRLoader.scss`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/internal/QRLoader/QRLoader.test.tsx`: `intentional-policy-exclusion` (excluded-category:tests)
- `modified` `packages/lib/src/components/internal/QRLoader/QRLoader.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `packages/lib/src/components/internal/QRLoader/components/QRBrandLogos.test.tsx`: `intentional-policy-exclusion` (excluded-category:tests)
- `added` `packages/lib/src/components/internal/QRLoader/components/QRBrandLogos.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/internal/QRLoader/components/QRLoaderPendingState.tsx`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/internal/QRLoader/types.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/src/components/internal/SecuredFields/lib/constants.ts`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/lib/storybook/public/mockServiceWorker.js`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/playground/package.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/package.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/ar.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/bg-BG.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/ca-ES.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/cs-CZ.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/da-DK.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/de-DE.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/el-GR.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/en-US.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/es-ES.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/et-EE.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/fi-FI.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/fr-FR.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/hr-HR.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/hu-HU.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/is-IS.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/it-IT.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/ja-JP.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/ko-KR.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/lt-LT.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/lv-LV.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/nl-NL.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/no-NO.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/pl-PL.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/pt-BR.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/pt-PT.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/ro-RO.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/ru-RU.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/sk-SK.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/sl-SI.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/sv-SE.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/zh-CN.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `packages/server/translations/zh-TW.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `yarn.lock`: `intentional-policy-exclusion` (outside-capsule-policy)
