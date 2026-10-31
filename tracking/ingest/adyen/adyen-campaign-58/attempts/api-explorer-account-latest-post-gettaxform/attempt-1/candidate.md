---
title: "Adyen Account API v6: Get a tax form"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/getTaxForm"
raw_files:
  - "adyen/api-explorer/Account/latest/post/getTaxForm/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, tax-forms, us]
---

## Overview

This Account API Explorer snapshot, captured 2026-09-15 under `Account/latest`, documents POST `/getTaxForm` on the displayed Account v6 test server. It describes generating a tax form for account holders operating in the US, identified by Classic `accountHolderCode`. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request-body table requires `accountHolderCode`, `formType` and integer `year` in YYYY format. It offers `1099-K` as a form-type example and shows year `2020` only in a request example; neither is a universal type requirement or proof of an available form for that year (raw lines 14–30).
- The documented 200 response may include Base64 binary `content`, `contentType`, validation `invalidFields`, a request `pspReference` and `resultCode`; all top-level response fields are marked optional in the table (raw lines 33–49). The page does not show a successful response example or a decoded form.
- This endpoint page states US operating scope but does not specify tax eligibility thresholds or filing/delivery rules. The separate [[source-adyen-docs-classic-platforms-tax-forms]] guide supplies dated Classic 1099-K threshold context and a server-side retrieval, decode and delivery flow. Do not infer current tax rules, a particular holder's eligibility, form issuance, filing, or delivery from this API snapshot.
- Error headings list 400 malformed/unreadable request, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. No specific permission name appears; the 400/403 example codes are generic examples, not an exhaustive error contract (raw lines 52–140).

## Detail locators

- Purpose, displayed test server and required request properties: raw lines 5–19; request example: raw lines 21–30.
- 200 response schema, including Base64 `content`, `contentType`, validation-field shape, request reference and result code: raw lines 31–49.
- Error categories and optional error-body fields: raw lines 52–114; 400 and 403 examples: raw lines 116–140. The generic error body's `pspReference` description mentions a payment; this is a tax-form endpoint, and that wording does not establish a payment.

## Related

- [[adyen-classic-platforms]] — Classic account-holder context and reciprocal source route.
- [[source-adyen-docs-classic-platforms-tax-forms]] — separate Classic 1099-K guide with historical threshold and retrieval/delivery conditions.
- [[adyen-platforms]] — newer balance-platform model with separate tax-form guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/getTaxForm/2026-09-15|Account API Explorer POST getTaxForm, captured 2026-09-15]]
