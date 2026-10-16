---
title: "Adyen Platforms KYC verification insights"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/kyc-insights"
raw_files:
  - "adyen/docs/platforms/kyc-insights/2026-09-15.md"
tags: [adyen, platforms, kyc, analytics]
---

## Overview

This 2026-09-15 Adyen page describes the **KYC verification analytics** dashboard for aggregate onboarding and verification trends on a balance platform. It is a Customer Area analytics view, not an individual account holder's definitive verification record; the page routes a specific holder to its KYC summary and timeline. Dashboard data, examples and trends do not prove a particular user's current capability, legal-entity status, account eligibility, payment or payout. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Access requires **one of** the listed Customer Area roles: Manage account holders and legal entities, Generate Balance Platform reports, or Download Balance Platform reports. The path is Analytics → KYC verification analytics. A selected filter view can be shared only with people in the organization who have a required role; this is not a public or unrestricted PII route.
- The **Overview** tab presents account-holder onboarding status on a **selected date**, including attempts, first-attempt success rate and median verification time. The **Errors** tab counts holders who faced verification errors and groups error types. Dashboard data are updated daily at **3:00 AM CET**. Filters include location, legal-entity type, integration type and custom date range; compare like cohorts before interpreting changes.
- The account-holder count uses holders who **started onboarding** within the selected date range and is grouped by the **holder's creation date**, not verification-completion date. Its categories are in review, verified, unsuccessful and rejected. In this metric, verified means all capability verification statuses are valid at that point; the page says a verified holder can later change status if additional verification is required. A Classic Platforms-to-Adyen for Platforms upgrade is initially classified unsuccessful until its KYC information is verified. None of these dashboard labels alone proves permission to use a particular product or a live financial outcome.
- A verification attempt counts a KYC-information submission **whether successful or not**. The first-attempt success rate divides first-attempt-verified holders by **all holders who started onboarding**, including some not yet submitted or with errors. Median verification time spans account-holder creation and first capability request until checks pass and capability statuses are valid, including error-notification and remedy time. Do not compare these metrics as if they share the same denominator or event date.
- **Errors** are historical and remain visible after resolution. A holder can have multiple error types, so category totals may exceed unique affected holders. Error-category names cover organization, individual, sole-proprietorship, bank, business line, missing data, contracts, general issues, data review and signatory. These aggregates help diagnose onboarding friction but do not by themselves identify a current root cause for an individual holder.
- The use cases suggest monitoring, troubleshooting and comparing interventions by date/location/integration type. They present analytical hypotheses and possible improvement signals, not verified causal effects or a guarantee that changing an onboarding flow resolves KYC.

## Detail locators

- Dashboard purpose, individual-holder route, access roles, two tabs, refresh and filters: pinned raw lines 15–47.
- Overview metric definitions, status/time/denominator and Classic-upgrade qualification: pinned raw lines 49–62.
- Error categories, overlapping counts and historical persistence: pinned raw lines 64–86.
- Monitoring, troubleshooting, interventions and comparisons as illustrative use cases: pinned raw lines 88–134.

## Related

- [[adyen-platforms]] — provider Platforms hub; dashboard analytics do not replace holder-level verification and capability records.
- [[source-adyen-docs-platforms-manage-account-holders]] — holder-level KYC summary/timeline route; separate source.

## Raw Sources

- [[raw/adyen/docs/platforms/kyc-insights/2026-09-15|Adyen KYC verification insights, captured 2026-09-15]]
