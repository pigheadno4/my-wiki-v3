# C24 Marketplace KYC insights retrieval checks

## Q1 — Where is the KYC analytics dashboard and what does it measure?

A user with one of the three specified account-holder or Balance Platform report roles opens **Analytics > KYC verification analytics** in Customer Area (raw lines 27–38). Overview summarizes selected-date onboarding status, verification attempts and speed; Errors groups affected holders and error categories. The view refreshes daily at 3:00 AM CET and supports location, legal-entity, integration-type and date filters (raw lines 40–47). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-kyc-insights]] → [[raw/adyen/docs/marketplaces/kyc-insights/2026-09-15]].

## Q2 — Why can these figures mislead if read as current individual verification?

Cohorts are grouped by holder creation date, not completion or error date; verified can later change, and Classic-upgraded holders initially appear unsuccessful until KYC verification (raw lines 57–59, 74–76). First-attempt success uses all starters as denominator, including non-submitters, while median time includes error notification and remediation (raw lines 60–62). Error categories can double-count a holder and resolved errors remain visible historically (raw lines 68–72). Use the separate holder KYC summary/timeline for a specific case (raw line 25). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-kyc-insights]] → [[raw/adyen/docs/marketplaces/kyc-insights/2026-09-15]].
