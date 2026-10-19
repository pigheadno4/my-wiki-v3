---
title: "Adyen Issuing KYC verification analytics"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/kyc-insights"
raw_files:
  - "adyen/docs/issuing/kyc-insights/2026-09-15.md"
tags: [adyen, issuing, kyc, onboarding, analytics]
---

## Overview

Adyen's KYC verification analytics dashboard guide (captured 2026-09-15) describes balance-platform onboarding and verification metrics in Customer Area. It is an aggregate trend view; the guide points to an account holder's KYC summary and timeline for individual verification detail. Access requires one of three specified platform user roles: Manage account holders and legal entities, Generate Balance Platform reports, or Download Balance Platform reports. In Customer Area, the route is Analytics > KYC verification analytics. [[adyen-issuing]] [[adyen]]

## Key takeaways

- The **Overview** tab presents account-holder onboarding status as of the selected date, verification attempts, first-attempt success rate, and median verification time. The **Errors** tab counts account holders with verification errors and breaks them down by category. The page says the dashboard updates daily at 3:00 AM CET and supports location, legal-entity-type, integration-type and custom-date filters; a filtered view can be shared with organization members who have a required role. See raw lines 27–47.
- **Cohort and status rules:** Number of account holders covers those who started onboarding in the selected date range, filtered by **creation date**, not completion date. Statuses are in review, verified, unsuccessful, or rejected. Verified means all capability verification statuses are valid, but further verification can change that status. Unsuccessful includes invalid capability status and unresolved verification errors; Classic Platforms upgrades are initially assigned unsuccessful until KYC and capability requirements are met. Rejected means at least one capability verification status is rejected. See raw line 59.
- **Metric definitions:** A verification attempt is counted whenever the account holder submits KYC information, whether or not it succeeds. First-attempt success rate divides account holders verified on the first attempt by all who started onboarding, including those who have not submitted yet or encountered errors. Median verification time runs from account-holder creation and first capability request until all KYC checks pass and capability statuses are valid, including time to communicate and resolve errors. See raw lines 60–62.
- **Error interpretation:** An account holder can have multiple error types, so category counts can exceed unique affected account holders. Error data remains visible after resolution and uses the account holder's creation date, not error occurrence or resolution date. The category table covers organization, individual, sole proprietorship, bank, business line, missing data, contract, general, data-review, and signatory issues. See raw lines 64–86.
- The use cases propose monitoring bottlenecks, troubleshooting errors and comparing interventions or markets. Such dashboard patterns may suggest where to investigate; they do not establish a causal improvement, present-day eligibility, or transaction readiness. See raw lines 88–134.

## Detail locators

- Role gate, Customer Area path, tabs, daily update and filters: raw lines 27–47.
- Exact Overview metric definitions and status qualifications: raw lines 53–62.
- Error category definitions and historical retention: raw lines 64–86.
- Examples for monitoring, troubleshooting, comparing interventions and markets: raw lines 88–134.

## Related

- [[adyen-issuing]] — Issuing concept.
- [[adyen-platforms]] — platform and balance-platform context.

## Raw Sources

- [[raw/adyen/docs/issuing/kyc-insights/2026-09-15|KYC verification insights, captured 2026-09-15]]
