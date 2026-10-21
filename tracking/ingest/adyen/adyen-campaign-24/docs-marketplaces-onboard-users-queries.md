# docs-marketplaces-onboard-users — attempt 1 retrieval checks

## Q1. What are the Marketplace user-onboarding routes and their prerequisites?

User legal-entity type and operating country determine required data, while verification type determines collection timing; Adyen starts checks after receiving the information (raw lines 19–25). Hosted onboarding uses an Adyen page plus marketplace LEM/Configuration API resource calls and includes Terms acceptance (raw lines 31–50). API-only onboarding uses a marketplace-built UI and LEM/Configuration API submissions; optional components can create a relevant resource from user-entered data (raw lines 168–172). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-onboard-users]] → [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15]].

## Q2. Does hosted onboarding or instant bank verification apply to every user, and does UI completion prove KYC?

No. Hosted onboarding lists Organization, Individual, Sole proprietorship and Australia/New Zealand-only Trusts (raw lines 39–44), plus its own dated operating-country list (raw lines 52–94). Instant bank verification has a narrower country-and-entity matrix (raw lines 96–127). ID autofill and decision-maker guidance/invites require onboarding v3/v4, with Latin-character ID documents for autofill (raw lines 135–166). The page’s base-integration “no additional requirements” wording (raw line 29) does not erase collection/submission of verification data (raw lines 19–25); an onboarding action is not approval or enabled-capability evidence. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-onboard-users]] → [[raw/adyen/docs/marketplaces/onboard-users/2026-09-15]].
