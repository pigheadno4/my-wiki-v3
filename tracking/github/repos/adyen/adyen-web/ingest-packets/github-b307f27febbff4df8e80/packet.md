# GitHub ingest packet

- Repository: `adyen/adyen-web`
- Work item: `github-b307f27febbff4df8e80`
- Snapshot: `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/manifest.json`
- Recommended mode: `delta`
- Review priority: `high`

## `@adyen/adyen-web`

- Version: `6.41.1` -> `6.42.0`
- Recommendation: `delta` / `high`
- Unchanged retained files: `208`

### Required reading

- `raw/github/adyen/adyen-web/releases/adyen-web/6.42.0/2026-08-09/manifest.json`
- `raw/github/adyen/adyen-web/releases/adyen-web/6.42.0/2026-08-09/release-notes.md`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/package.json`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/Dropin/components/DropinComponent.tsx`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/Dropin/types.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/Dropin/utils/paymentMethodsAnalytics.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/ThreeDS2/callSubmit3DS2Fingerprint.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/ThreeDS2/components/Challenge/DoChallenge3DS2.tsx`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/ThreeDS2/components/Challenge/PrepareChallenge3DS2.tsx`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/ThreeDS2/components/Challenge/types.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/ThreeDS2/constants.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/components/ThreeDS2/types.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/core/Analytics/events/AnalyticsInfoEvent.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/files/packages/lib/src/core/ProcessResponse/PaymentAction/actionTypes.ts`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/manifest.json`
- `raw/github/adyen/adyen-web/snapshots/2026-08-09-c98ea8a/manifest.json`
- `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.1--6.42.0/comparison.json`
- `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.1--6.42.0/comparison.md`
- `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.1--6.42.0/diff.patch`

### Upstream changes

- `modified` `.github/workflows/e2e-tests.yml`: `intentional-policy-exclusion`
- `modified` `.github/workflows/release-snapshot.yml`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/playwright.config.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/a11y/card/card.contextualTexts.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/a11y/customCard/expiryDate/customCard.regular.expiryDatePolicies.optional.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/a11y/customCard/expiryDate/customCard.separate.expiryDatePolicies.optional.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/e2e/card/legacyInputMode/card.legacyInputMode.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/ui/card/binLookup/branding/branding.reset.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/ui/card/binLookup/panLength/panLength.focus.regular.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/ui/card/binLookup/plcc/plcc.noluhn.nodate.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/ui/card/branding/card.branding.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/ui/card/expiryDate/card.expiryDatePolicies.optional.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/ui/customCard/binLookup/branding/customCard.dualBranding.reset.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/e2e-playwright/tests/ui/customCard/binLookup/branding/customCard.singleBranding.reset.spec.ts`: `intentional-policy-exclusion`
- `modified` `packages/lib/.size-limit.cjs`: `intentional-policy-exclusion`
- `modified` `packages/lib/CHANGELOG.md`: `intentional-policy-exclusion`
- `modified` `packages/lib/package.json`: `retained-evidence`
- `modified` `packages/lib/src/components/Card/Card.test.tsx`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/Dropin/Dropin.test.ts`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/Dropin/components/DropinComponent.tsx`: `retained-evidence`
- `modified` `packages/lib/src/components/Dropin/types.ts`: `retained-evidence`
- `added` `packages/lib/src/components/Dropin/utils/paymentMethodsAnalytics.test.ts`: `intentional-policy-exclusion`
- `added` `packages/lib/src/components/Dropin/utils/paymentMethodsAnalytics.ts`: `retained-evidence`
- `modified` `packages/lib/src/components/ThreeDS2/callSubmit3DS2Fingerprint.ts`: `retained-evidence`
- `added` `packages/lib/src/components/ThreeDS2/components/Challenge/DoChallenge3DS2.test.tsx`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/ThreeDS2/components/Challenge/DoChallenge3DS2.tsx`: `retained-evidence`
- `modified` `packages/lib/src/components/ThreeDS2/components/Challenge/PrepareChallenge3DS2.test.tsx`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/ThreeDS2/components/Challenge/PrepareChallenge3DS2.tsx`: `retained-evidence`
- `modified` `packages/lib/src/components/ThreeDS2/components/Challenge/types.ts`: `retained-evidence`
- `modified` `packages/lib/src/components/ThreeDS2/constants.ts`: `retained-evidence`
- `modified` `packages/lib/src/components/ThreeDS2/types.ts`: `retained-evidence`
- `modified` `packages/lib/src/components/internal/Address/Address.test.tsx`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/internal/Address/Address.tsx`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/internal/Address/validate.formats.ts`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/internal/Address/validate.test.ts`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/internal/Address/validate.ts`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/components/internal/IFrame/Iframe.tsx`: `intentional-policy-exclusion`
- `modified` `packages/lib/src/core/Analytics/events/AnalyticsInfoEvent.ts`: `retained-evidence`
- `modified` `packages/lib/src/core/ProcessResponse/PaymentAction/actionTypes.ts`: `retained-evidence`
- `modified` `packages/lib/src/utils/Formatters/types.ts`: `intentional-policy-exclusion`
- `modified` `packages/playground/package.json`: `intentional-policy-exclusion`
- `modified` `yarn.lock`: `intentional-policy-exclusion`
