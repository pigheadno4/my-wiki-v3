---
title: "Adyen Marketplace US tax-form retrieval and distribution"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/us-tax-forms"
raw_files:
  - "adyen/docs/marketplaces/us-tax-forms/2026-09-15.md"
tags: [adyen, marketplaces, us, tax-forms, reporting]
---

## Overview

This 2026-09-15 Marketplace-path page describes Adyen's stated US 1099-K filing scope for users **to whom Adyen pays out directly** and the marketplace's routes to retrieve and distribute generated PDF forms. Its title and description also mention 1099-NEC, but the body supplies 1099-K criteria and retrieval only. Its tax-year thresholds and availability are dated source claims, not current tax advice or evidence that a particular form was filed, retrieved, consented to or delivered. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Direct-payout and tax-year scope:** The page says Adyen files 1099-K with the IRS for US-based users it pays out directly, and some states require filing. For **2025**, it states a federal threshold of **USD 20,000 gross processed volume and 200 transactions combined per calendar year**, while state thresholds vary. Gross volume is measured before fees, chargebacks and refunds; `splits.type=TopUp` transactions are excluded. A later sentence says Adyen only generates a form when the volume **or** transaction threshold is met. The page does not reconcile this **and/or** conflict; neither phrase should be treated as a resolved filing trigger.
- **Availability and user delivery:** Adyen says prior-tax-year forms become available in the third week of January, giving 2025 forms in January 2026 as an example. The marketplace can retrieve available forms in Customer Area or through the API and distribute a PDF copy. The text says no form is available below its threshold, but that statement inherits the unresolved threshold wording. Retrieval instructions do not prove actual filing or delivery.
- **Access routes:** Customer Area download requires **Download tax form** plus either **Balance platform admin** or **Balance platform base**, followed by selection of the processing merchant account and account holder. API retrieval covers tax years **2022 onward** and requires a Balance Platform API key with **Download Tax Form via Tax Api**. The guide says a user-facing button or link should trigger retrieval for that account holder.
- **API result:** `GET /accountHolders/{id}/taxForms` uses account-holder ID and required `formType=US1099k` and `year=YYYY`; `legalEntity` is shown as optional in the parameter table. The response contains Base64-encoded PDF content, which the marketplace decodes and provides to the user. Its TEST request and response are examples, not a real filing or delivery. A separately linked guide addresses paperless-delivery consent.

## Detail locators

- Direct-payout scope, dated 2025 threshold, gross basis and TopUp exclusion: pinned raw lines 15-28.
- Prior-year availability, threshold conflict and distribution: pinned raw lines 30-34.
- Customer Area roles/navigation and API credential/role: pinned raw lines 36-61.
- Endpoint, parameters, Base64 PDF response and provision to user: pinned raw lines 63-95.
- Separate paperless-delivery-consent route: pinned raw lines 97-99.

## Related

- [[adyen-platforms]] — main platform model and reciprocal source route.
- [[source-adyen-docs-platforms-us-tax-forms]] — separately captured Platforms-path counterpart.
- [[source-adyen-docs-marketplaces-us-tax-forms-edelivery-consent]] — paperless-delivery-consent guide, a distinct step.

## Raw Sources

- [[raw/adyen/docs/marketplaces/us-tax-forms/2026-09-15|Marketplace US tax forms page, captured 2026-09-15]]
