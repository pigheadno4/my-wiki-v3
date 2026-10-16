# Fixed queries — Platforms onboarding components

## Q1 — purpose, scope, and what must not be inferred

**Query:** Which onboarding resources do these components cover, for what entity versions, and does completion verify a user or payout account?

**Answer:** The prebuilt platform UI covers transfer-instrument bank-account configuration and management for legal entities created with LEM API v3 or v4. It can create the resource and display verification statuses/errors, but covers only some API-only onboarding steps; other API calls remain necessary. A `complete` event indicates interaction/submission, not Adyen verification approval, capability activation, completed payout or bank receipt. Hosted-onboarding users may also manage submitted data through the embedded platform UI. Raw: `raw/adyen/docs/platforms/onboard-users/components/2026-09-15.md:17-35,57-75,564-603`. Canonical route: `[[source-adyen-docs-platforms-onboard-users-components]]` → `[[adyen-platforms]]`.

## Q2 — central capability, prerequisites, and warnings

**Query:** What setup, consent, session-scope, environment and sensitive-data conditions must the platform preserve?

**Answer:** An Adyen for Platforms integration, LEM API key, supported language/browser and prerequisite onboarding steps are called out. The platform server uses its API key to create a Session authentication token scoped by `allowOrigin` (HTTPS on live), `product: onboarding`, the legal entity with the contractual relationship and bank-account ownership, and `transferInstrumentConfiguration`/`transferInstrumentManagement` roles. Configuration lets the user permit instant bank verification or upload documents; US/CA instant verification has an `openBankingPartnerConfigId` parameter. The frontend uses `@adyen/kyc-components`, `test`/`live` environment, root legal-entity ID and token-refresh callback. Management can remove accounts immediately. The sample callback exposes bank details and is not a consent or verification record; inspect the actual status separately. Library features vary by selected version. Raw: `raw/adyen/docs/platforms/onboard-users/components/2026-09-15.md:35-53,57-75,98-113,141-161,174-204,564-603`. Canonical route: `[[source-adyen-docs-platforms-onboard-users-components]]` → `[[adyen-platforms]]`.
