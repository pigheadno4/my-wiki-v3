---
title: "Adyen Capital user application and interface guidelines"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/user-interface"
raw_files:
  - "adyen/docs/capital/user-interface/2026-09-15.md"
tags: [adyen, capital, platforms, user-interface, consent, compliance]
---

## Overview

This Capital user-application and interface guideline (last modified 2023-12-12; captured 2026-09-15) states what Adyen says platforms must present for agreed financial services and Capital offers, terms, consent and ongoing information. It expressly says it is not legal advice. Its “must” language is dated Adyen guidance, not current legal certification, a platform's approval, a user's valid consent, an accepted grant or funding proof. See [[adyen]], [[adyen-capital]] and [[adyen-platforms]].

## Key takeaways

- **General interface and identity:** The page calls for an interface to request agreed financial services, supply Adyen-required KYC data, present agreements/disclosures/fees, obtain informed acceptance from an authorized legal representative, keep accepted agreements accessible, and provide free ongoing product/account information. It forbids preselected confirmation options, says the platform must not present itself as a bank, and calls for Adyen-provider disclosure. Hosted onboarding places KYC fields and terms with Adyen; components may embed certain requirements, so implementation paths differ. The page also specifies security measures for Capital access. Its consent procedure states only a natural person who is an Authorized Signatory can give consent to Adyen, and evidence of obtained consents must be retained.
- **Capital offer and terms:** The Capital row names Adyen Capital User Terms and Adyen's Privacy Statement. Offer UI should identify financing contract type, present Adyen-provided dynamic/static offer fields and a maximum repayment period, and show that the user requests Capital before an offer. The guide calls for KYC submission, offer amount, total repayment, percentage, fee and any alternative repayment method, with Terms of Service visible and acceptance captured. It says Capital user terms need acceptance one time and updates communicated; the separate How Capital works guide says grant Terms of Service must be accepted for each new grant, even after earlier business-financing acceptance. Do not use the one-time user-terms sentence to waive grant-specific acceptance.
- **Country-specific presentation:** The Capital fee must appear as an annual interest rate in Canada. For Ireland, the page gives a provider wording for all products and requires specified credit-reporting notices, Capital balance/offer-validity information and a tick-box consent before the user becomes bound by a Capital contract. The UK-only payment-processing row is separate from Capital. These are dated country/product conditions, not universal disclosure text or current legal advice.
- **Ongoing insights versus outcome:** The interface should show Capital balance, repayment requirements, repaid funds and term, and inform users about disbursement and repayment; the page points to grant GET and Capital/Transfer webhooks for data. Displaying a financing offer, accepted-looking screen, grant details or repayment progress does not independently prove grant disbursement, a bank receipt, debt balance or final repayment.

## Detail locators

- Legal-advice boundary, general UI, hosted/components variation and authorized representative consent language: pinned raw lines 15–43.
- Product-specific terms and Capital display, Canada and Ireland requirements: pinned raw lines 45–79.
- Offer, KYC, relevant terms and acceptance example: pinned raw lines 81–136.
- Capital insights, API/webhooks and access security: pinned raw lines 138–166.
- Customer disclosure/consent procedure, Authorized Signatory and evidence retention: pinned raw lines 168–202.
- Separate per-grant Terms acceptance in linked How Capital works raw: raw/adyen/docs/capital/how-capital-works/2026-09-15.md lines 90–100.

## Related

- [[adyen-capital]] — main Capital concept and reciprocal source route.
- [[adyen-platforms]] — platform context.

## Raw Sources

- [[raw/adyen/docs/capital/user-interface/2026-09-15|Adyen Capital user-interface guidance, captured 2026-09-15]]
