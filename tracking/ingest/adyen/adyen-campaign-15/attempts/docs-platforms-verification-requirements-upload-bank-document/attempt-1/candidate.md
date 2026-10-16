---
title: "Adyen Hosted Onboarding bank-document upload"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-requirements/upload-bank-document"
raw_files:
  - "adyen/docs/platforms/verification-requirements/upload-bank-document/2026-09-15.md"
tags: [adyen, platforms, hosted-onboarding, bank-verification]
---

## Overview

This 2026-09-15 Adyen for Platforms page explains the **Hosted Onboarding bank-document upload** when automatic bank-account verification is not possible. It describes document checks and immediate upload feedback, not final bank-account or legal-entity verification. The page labels automated document checks **limited availability** in Australia, France, the United Kingdom and the United States at capture time and says processes/documentation may change. It does not establish current country eligibility, enabled account features, payout readiness or bank receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Before upload, the bank document should display the **bank account holder's name matching the legal-entity name on record**, account number or IBAN, issue date within the previous **12 months** subject to stated exceptions, and evidence it was bank-issued. Accepted formats are PDF (preferred), JPEG/JPG and PNG, **one file at a time**, up to **4 MB**. The separate bank-document requirements page owns full details, including special conditions for checks and deposit forms.
- The page lists bank statements, agreements, deposit slips/forms, online-banking screenshots, official bank letters, checks, French RIBs, Greek TAMIEYTHPIO and Singapore passbooks as document types. This document-type list must not be read as expanding the four-country **automated-check availability** notice. Screenshots can omit an issue date under the FAQ but must clearly show the account number/IBAN, name and bank name/logo. Other date exceptions also apply by document type.
- In Hosted Onboarding, the user uploads at the bank-account step. The automated system returns document feedback in seconds: passing the check prompts **review and submit**; a warning permits **Replace document** or **Use this document** for manual Adyen review. If classification is inconclusive, the review team handles it and contacts the user if needed. Upload acceptance and the ability to continue are not a final verification decision or payout permission.
- The troubleshooting table covers blur, cropping, wrong type, age and size. The page rejects card photos, ATM/terminal records, third-party bookkeeping documents, unclear bank-origin evidence, missing or illegible identifying fields, edited/digitally altered files and poor-quality images. Follow the Hosted Onboarding flow for sensitive bank data; this page does not define a separate consent process or authorize sending documents outside it.
- This is a provider snapshot of the **Hosted Onboarding** experience, with no specified API or onboarding-version equivalence. Refer to the linked requirements guide for detailed document criteria and the user's actual verification status for outcome, rather than treating fast automated feedback as compliance proof.

## Detail locators

- Limited-availability notice and fallback from automatic account verification: pinned raw lines 15–24.
- Document identity, date, bank-origin, format and size conditions: pinned raw lines 26–39.
- Accepted types and special-document link: pinned raw lines 41–55.
- Hosted upload path, automated feedback, manual-review option: pinned raw lines 57–79.
- Quality/security exclusions, manual classification and screenshot FAQ: pinned raw lines 81–129.

## Related

- [[adyen-platforms]] — Platforms onboarding and verification context.
- [[source-adyen-docs-platforms-verification-requirements-document-requirements]] — separate detailed bank-document requirements route, not substituted by this upload-flow summary.

## Raw Sources

- [[raw/adyen/docs/platforms/verification-requirements/upload-bank-document/2026-09-15|Adyen Hosted Onboarding bank-document upload, captured 2026-09-15]]
