---
title: "Provide tax forms (US only) | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/us-tax-forms"
raw_files:
  - "adyen/docs/platforms/us-tax-forms/2026-09-15.md"
tags: [adyen, platforms, us, tax-forms, reporting]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms page describes Adyen's US 1099-K filing for users to whom Adyen pays out directly and the platform's retrieval and PDF-delivery route for generated forms. See [[adyen-platforms]] for the platform route. The page title/description also mention 1099-NEC, but the body gives only 1099-K criteria and retrieval; do not infer a 1099-NEC procedure from it. Its tax-year threshold and availability statements are dated source claims, not current tax advice, evidence of a filing, or proof a form was delivered.

## Key takeaways

- The captured page says Adyen files 1099-K with the IRS for US-based users it pays out directly, with some state filing too. For tax year 2025, it states a federal threshold of **USD 20,000 gross processed volume and 200 transactions combined per calendar year**, with state thresholds varying. Gross processed volume is before fees, chargebacks and refunds; `splits.type=TopUp` transactions are excluded. But a later sentence says a form is generated when the volume **or** transaction threshold is met. The page does not resolve this AND/OR conflict; neither wording should be selected as the controlling trigger for a filing decision. The criteria are historical and scoped to the named year and direct-payout relationship. [Raw: lines 21–28, 34]
- Adyen says it makes prior-year forms available in the third week of January (example: 2025 forms in January 2026). The page separately says 1099-K generation depends on a volume or transaction threshold and that no form is available below it; that **or** wording conflicts with the **and** formulation for 2025 above. The platform can retrieve available forms through Customer Area or API and distribute PDF copies to its users. Availability or retrieval instructions do not prove that Adyen filed a specific form or that the platform delivered it. [Raw: lines 30–34]
- Customer Area download requires `Download tax form` plus either `Balance platform admin` or `Balance platform base`; the path starts under the merchant account where the account holder processes, then the account-holder overview. API retrieval for tax year 2022 or later requires a Balance Platform API key and `Download Tax Form via Tax Api` role. These are distinct credential routes. [Raw: lines 36–61]
- API use sends `GET /accountHolders/{id}/taxForms` with account-holder ID, required `formType=US1099k` and `year=YYYY`; `legalEntity` is shown without a required mark and identifies the relevant legal entity when supplied. The response contains Base64-encoded PDF content; the platform decodes and provides a PDF copy to the user. The page asks the platform to show a user button/link that triggers retrieval for that account holder. The sample request/response is illustrative and does not itself show a real user's form. [Raw: lines 52–95]
- The linked electronic-delivery-consent guide covers paperless delivery separately. A tax form's generation, Customer Area access, API response, user consent and final delivery are separate steps; this page alone does not establish consent or delivery. [Raw: lines 30–34, 95–99]

## Detail locators

- US direct-payout scope, 2025 federal/state threshold, gross basis and TopUp exclusion: raw lines 15–28.
- Prior-year availability, threshold gate and platform PDF distribution: raw lines 30–34.
- Customer Area roles and account-holder navigation: raw lines 36–50.
- API key/role, endpoint, parameters, Base64 response and PDF-delivery steps: raw lines 52–95.
- Separate paperless-consent guide: raw lines 97–99.

## Related

- [[adyen-platforms]] — platform model and evidence boundary
- [Paperless tax-form delivery consent](https://docs.adyen.com/platforms/us-tax-forms-edelivery-consent) — separate consent route
- [IRS](https://www.irs.gov/) — current US tax authority

## Raw Sources

- [[raw/adyen/docs/platforms/us-tax-forms/2026-09-15|Adyen Platforms US tax forms — collected 2026-09-15]]
