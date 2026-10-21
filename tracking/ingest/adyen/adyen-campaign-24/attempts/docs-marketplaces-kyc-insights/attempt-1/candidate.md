---
title: "Adyen Marketplace KYC verification insights"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/kyc-insights"
raw_files:
  - "adyen/docs/marketplaces/kyc-insights/2026-09-15.md"
tags: [adyen, marketplaces, kyc, analytics, onboarding]
---

## Overview

This 2026-09-15-modified Marketplace-route Adyen for Platforms guide describes the Customer Area **KYC verification analytics** dashboard for aggregate onboarding progress, speed and error trends on a balance platform. It points to a separate account-holder KYC summary/timeline for a specific user's verification process. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Customer Area access at **Analytics > KYC verification analytics** requires one of three roles: **Manage account holders and legal entities**, **Generate Balance Platform reports**, or **Download Balance Platform reports**. The dashboard refreshes daily at **3:00 AM CET**, and filter views may be shared only with colleagues who have a required role (raw lines 25–47). This is a dated dashboard snapshot, not live account-holder state.
- **Overview** shows account-holder onboarding status as of a selected date, attempts, verified counts and speed. **Errors** counts holders who faced verification errors and groups error categories (raw lines 40–43). Data can be filtered by location, legal entity type, integration type or custom date range (raw line 47).
- The account-holder cohort is filtered by **creation date**, not completion or error date. Its status total combines in-review, verified, unsuccessful and rejected holders. In-review means at least one capability is pending; verified requires all capability statuses valid but can later change; unsuccessful includes invalid capability checks, and an upgrade from Classic is initially counted unsuccessful until KYC is verified; rejected includes at least one rejected capability (raw lines 57–59, 74–76). These aggregate labels are not immutable individual approvals.
- Verification attempts count submissions whether successful or not. **First attempt success rate** divides holders verified on first attempt by all who started onboarding, including users who have not submitted information. **Median verification time** runs from holder creation and first capability request until all KYC checks pass and all capability statuses are valid, including notification and remediation time (raw lines 60–62).
- An account holder may face multiple error categories, so category totals can exceed unique affected holders. The Errors tab retains historical errors after resolution, and its holder count is also grouped by creation date (raw lines 64–76). A displayed error is therefore not proof of a currently unresolved error. The guide suggests comparing filtered cohorts or before/after interventions as analysis, not proof of causality (raw lines 122–134).

## Detail locators

- Dashboard purpose versus individual KYC route: raw lines 19–25. Role gate, UI path, tabs, refresh time and filters: raw lines 27–47.
- Overview cohort/status definitions, Classic migration exception and metric denominators/timing: raw lines 53–62. Error categories, duplicate-count and historical-error behavior: raw lines 64–86. Example intervention/comparison uses: raw lines 88–134.

## Related

- [[adyen-platforms]] — balance-platform and Marketplace route.
- [[source-adyen-docs-marketplaces-verification-overview-capabilities]] — capability statuses and allowed/enabled gates.
- [[adyen-classic-platforms]] — older Classic model mentioned in migration metric.

## Raw Sources

- [[raw/adyen/docs/marketplaces/kyc-insights/2026-09-15|Marketplace KYC insights, captured 2026-09-15]]
