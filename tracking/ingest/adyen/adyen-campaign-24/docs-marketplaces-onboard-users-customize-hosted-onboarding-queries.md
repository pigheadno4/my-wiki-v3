# docs-marketplaces-onboard-users-customize-hosted-onboarding — attempt 1 retrieval checks

## Q1. How is a Marketplace hosted-onboarding theme prepared and used?

For Adyen for Platforms or Issuing, API-initiated hosted onboarding needs LEM credentials, while Customer Area theme create/edit requires the named theme and balance-platform roles (raw lines 29–37). The company-account theme can set branding and page assets, then its saved theme ID is passed to POST `/legalEntities/{id}/onboardingLinks` to create an onboarding link (raw lines 39–70); locale and action settings are supplied on that link request (raw lines 124–176). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-onboard-users-customize-hosted-onboarding]] → [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15]].

## Q2. What do settings, test-bank fixtures and the debug report establish or expose?

Settings govern available hosted-page actions and defaults, not verification or payout outcomes (raw lines 158–176). The instant-bank credentials are explicitly for the **test environment** (raw lines 178–204). The debug UI is on by default for support/engineering; its report contains sensitive legal-entity, task, setting and capability information, and the page directs minimal sharing only with the team or Adyen Support (raw lines 206–227). A theme/link, test action or displayed task status does not prove KYC approval or enabled capabilities. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-onboard-users-customize-hosted-onboarding]] → [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15]].
