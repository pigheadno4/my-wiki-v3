---
title: "Adyen Marketplace financial-product notifications and reporting"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/compliance-financial-products/reporting-to-adyen"
raw_files:
  - "adyen/docs/marketplaces/compliance-financial-products/reporting-to-adyen/2026-09-15.md"
tags: [adyen, marketplaces, financial-products, compliance, reporting]
---

## Overview

This [[adyen]] Marketplace financial-products compliance-guideline page, last modified 2024-01-10 and captured 2026-09-15, describes when a marketplace offering financial products is asked to notify Adyen and submit daily or periodic reports. The page expressly says it is not legal advice. Its timing, channels and region/product conditions are dated Adyen guidance, not proof of present legal duties, current policy or any platform's reporting performance. See [[adyen-financial-products]] and [[adyen-platforms]].

## Key takeaways

- **Event notification:** The page says platforms must notify Adyen immediately, defined as within 1–2 business days, for Security, Regulatory or Legal Complaints through a dedicated template. It sends unresolved user support, unauthorized credentials/fraud, disputed unauthorized payments or statement errors, material incidents/breaches and material user non-compliance through normal support lines. If a qualifying notification is made through an API request, such as account block/termination, the page says no additional reporting is needed. See pinned raw lines 23–37.
- **Daily reports are service-qualified:** For relevant events, the page asks for daily Accounts/Issuing fraud incident or dispute counts and reason codes/descriptions, via Disputes API or an email channel communicated by Adyen. It lists a separate Issuing-only report for blocked/stolen/lost/damaged cards, with instrument ID, scheme status and marketplace action. Do not apply the Issuing report to a platform without Issuing. See pinned raw lines 39–52.
- **Quarterly complaint reporting:** To the extent applicable law does not prohibit it, the marketplace is asked to report Adyen-product user complaints each quarter using Adyen's template. The reporting period starts when its first user is onboarded live. Listed fields include receipt/acknowledgement/resolution dates, status and upheld/not-upheld determination, user/entity/country, product/category and resolution steps. The page gives 10 January, 10 April, 10 July and 10 October deadlines and a named complaints mailbox. These are page-snapshot instructions, not proof of submission. See pinned raw lines 54–96.
- **UK and Ireland addition:** The section asks for vulnerable-user totals, four-driver category counts and outcomes of specific support requests with the same quarterly deadlines, plus annual sharing of patterns that may warrant Adyen attention. It also says only total figures for vulnerable users are required, leaving the intended granularity of support-request outcomes less clear; do not infer that identifiable user-level vulnerability files must be sent. The region qualifier applies to this addition, not all marketplaces. See pinned raw lines 98–112.

## Detail locators

- Dated source, financial-products scope and legal-advice disclaimer: pinned raw lines 15–21.
- Complaint and support notification triggers/channels, API-request exception: pinned raw lines 23–37.
- Accounts/Issuing fraud and Issuing-only card reporting: pinned raw lines 39–52.
- Quarterly Adyen-product complaint fields, live-start trigger, recipient and dates: pinned raw lines 54–96.
- UK/Ireland vulnerable-user counts, outcome wording, totals qualifier and annual patterns: pinned raw lines 98–112.

## Related

- [[adyen-financial-products]] — reciprocal financial-products concept.
- [[source-adyen-docs-platforms-compliance-financial-products-reporting-to-adyen]] — same dated guidance under the Platforms path.
- [[source-adyen-docs-marketplaces-compliance-financial-products-vulnerable-users]] — separate UK/Ireland staff support and factual-recording guidance.

## Raw Sources

- [[raw/adyen/docs/marketplaces/compliance-financial-products/reporting-to-adyen/2026-09-15|Marketplace reporting-to-Adyen guidance, captured 2026-09-15]]
