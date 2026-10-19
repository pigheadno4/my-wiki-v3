# C21 worker queries — onboard users

Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-onboard-users]] → [[raw/adyen/docs/issuing/onboard-users/2026-09-15]].

## Q1. How does this page route user onboarding, and what determines the required information?

The user's legal-entity type and operating country determine which verification information to collect (raw line 19). Hosted onboarding sends users to an Adyen-hosted page while the platform makes resource-creation/customization API calls (raw lines 21, 36–42). API-only onboarding uses the platform's own UI and Legal Entity Management/Configuration API submissions; optional embedded components create relevant resources from user input (raw lines 22, 160–164). Adyen says verification starts automatically after it receives the information (raw line 24). The v4 section says issuing cards requires a business line with `service: issuing` and an industry code (raw lines 166–172).

## Q2. What limits, evidence requests, or contradictions qualify this route?

The hosted-country list is specific to the captured page (raw lines 44–86), and instant bank verification applies only to listed country and legal-entity-type combinations (raw lines 88–119). ID autofill and decision-maker features require onboarding v3 or v4, and ID autofill supports Latin-character documents only (raw lines 127–158). Adyen says source-of-funds verification applies to Issuing and Business Accounts, with additional documents possibly requested by funding type (raw lines 174–189). For Adyen-processed funds, prose names `sourceOfFunds.adyenProcessedFunds` but the table names `businessLines.adyenProcessedFunds`; this snapshot leaves the path conflict unresolved (raw lines 187, 193). None of these instructions proves a user passed verification or a card became active.
