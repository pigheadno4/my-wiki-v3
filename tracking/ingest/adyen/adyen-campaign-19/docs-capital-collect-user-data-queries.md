# Capital higher-amount data collection — retrieval probes

## Q1 — Trigger and scope

**Query:** Does every Capital user need extra KYC at EUR 25,000, and is an exactly-at-threshold grant clearly covered?

**Expected answer:** No universal trigger follows. The captured API guide covers certain legal-entity types and selected-offer or new-offer-plus-outstanding exposure, with country/region thresholds. Its introduction says “meets,” while the configuration flow says “exceeds,” so it does not settle the equality case. The dated table lists organizations from EUR 25,000 in several countries, Spain from EUR 3,000, and Australia/Canada excluding Saskatchewan as not applicable. This is not current eligibility, legal advice or an approved grant.

**Raw locators:** lines 19–30, 63–75 and 1481–1498. **Canonical discovery route:** [[adyen-index]] → [[adyen-capital]] → [[source-adyen-docs-capital-collect-user-data]] → [[raw/adyen/docs/capital/collect-user-data/2026-09-15]].

## Q2 — Path, prerequisites and proof

**Query:** If extra data is required on an API-only Capital grant, what credentials, collection routes, states and warnings does the page describe, and does an Approved sample prove funding?

**Expected answer:** It describes Capital-supporting Platforms access, Capital configuration/initiation roles, LEM key, account-holder getGrantOffers/receiveGrants capabilities, webhooks and LEM v3+ legal entities. A higher-amount request imposes a currently irreversible extra-KYC risk level. Adyen signals unresolved AnaCreditCapabilityRule/Reviewing; hosted onboarding uses an expiring one-time main-entity link, while API-only reads capability problems, submits LEM data and handles parent-company entities/whole-array association PATCH where needed. Check account-holder capability validity/allowed state separately from resolved grant action/Approved status. Data must arrive before offer expiry; specific missing-data errors have remediation codes, including a noPossibleRemediation case. TEST examples and configuration/status alone do not prove disbursement or bank receipt.

**Raw locators:** lines 32–61, 95–175, 340–518, 755–1052, 1347–1479 and 1500–1513. **Canonical discovery route:** [[adyen-index]] → [[adyen-capital]] → [[source-adyen-docs-capital-collect-user-data]] → [[raw/adyen/docs/capital/collect-user-data/2026-09-15]].
