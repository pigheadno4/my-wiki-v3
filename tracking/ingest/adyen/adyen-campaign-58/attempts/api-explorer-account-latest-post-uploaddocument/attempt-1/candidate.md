---
title: "Adyen Account API v6 POST /uploadDocument"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/uploadDocument"
raw_files:
  - "adyen/api-explorer/Account/latest/post/uploadDocument/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, documents, verification]
---

## Overview

This captured Classic Account API v6 `POST /uploadDocument` reference submits a document for an account holder for use during Adyen's verification process. Submission and an API response are distinct from a completed or approved KYC check. The listed server is `https://cal-test.adyen.com/cal/services/Account/v6`. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request schema requires `documentContent` as a Base64-encoded string and a `documentDetail` object containing required `documentType`. `accountHolderCode`, `filename`, `description`, and the other link codes are marked optional in the table; do not infer that the sample's `accountHolderCode` makes it unconditionally required. See raw lines 14–42.
- The document type enum covers bank statement, company registration screening (v5+), constitutional document, passport, and front/back ID card and driving licence types. ID-card front/back and driving-licence front/back are described as paired submissions for usability. The `DRIVING_LICENCE_BACK` description mistakenly repeats `DRIVING_LICENCE_FRONT` twice, while the front description names both sides; preserve that source inconsistency rather than applying its literal repetition as a rule. See raw line 22.
- Link the document to the relevant Adyen-generated owner code where applicable. `bankAccountUUID` is required when a `BANK_STATEMENT` is submitted to verify a bank account. `shareholderCode` is required for a Business account holder's passport, ID-card or driving-licence document. `legalArrangementCode`, `legalArrangementEntityCode` and `signatoryCode` are listed as optional linkage fields, without additional conditional rules on this page. See raw lines 19–27.
- This operation page does not give file-size or accepted-format limits; it points to verification requirements. The related Classic document requirements source gives category-specific format and size rules, including separate ID, organization/legal-arrangement, and bank-evidence limits. Use [[source-adyen-docs-classic-platforms-verification-process-document-requirements]] for those conditions, rather than treating the sample `passport.png` as the complete format contract.
- `200` is labeled successful; `202` says processing was accepted but has **not completed**. Both response tables reuse an extensive account-holder schema with optional `verification`, `invalidFields`, `pspReference` and `resultCode`; they do not specify a document identifier or a re-upload/replace identity. A returned verification field or upload receipt is not a KYC approval guarantee. See raw lines 43–372.
- The page lists 400, 401, 403, 422 and 500 errors; 401 requires authentication and 403 indicates insufficient permissions. The 400/403 JSON examples are illustrative. See raw lines 375–463.

## Detail locators

- Purpose, TEST server, request body and example: raw lines 5–42.
- 200 response and account-holder/verification fields: raw lines 43–207.
- 202 incomplete-processing response and repeated fields: raw lines 210–372.
- Error tables and examples: raw lines 375–463.

## Related

- [[adyen-classic-platforms]] — Classic account-holder context.
- [[source-adyen-api-explorer-account-latest-overview]] — Account API v6 overview and authentication/version boundary.
- [[source-adyen-docs-classic-platforms-verification-process-document-requirements]] — separate Classic file format, quality, page-count and size requirements.
- [[source-adyen-docs-classic-platforms-verification-process-check-verification-results]] — verification result checks after submission.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/uploadDocument/2026-09-15|POST /uploadDocument, captured 2026-09-15]]
