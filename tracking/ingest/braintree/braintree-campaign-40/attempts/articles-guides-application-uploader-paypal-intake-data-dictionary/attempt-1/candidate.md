---
title: "Braintree PayPal Intake Data Dictionary"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/application-uploader/paypal-intake-data-dictionary"
raw_files:
  - "braintree/articles/guides/application-uploader/paypal-intake-data-dictionary-2026-09-16.md"
tags: [braintree, paypal, application-uploader, intake-api, onboarding, underwriting]
---

## Overview

This Braintree-hosted PayPal Intake Data Dictionary page routes bulk application data for the Intake API or Application Uploader. It identifies two accepted PayPal Intake input schemas, v1 and v2, plus a separate branded-solution dictionary and sample. The Application Uploader is stated to be available only to select merchants. This is an intake-dictionary landing page, not the PayPal UOB API contract, proof of merchant eligibility, successful submission, underwriting approval, account setup or feature enablement. See [[braintree]] and [[braintree-payment-platform]].

## Key takeaways

- Each dictionary row is described as defining expected information and details such as acceptable values and formatting. The captured webpage links the v1, v2 and branded-solution CSV dictionaries and samples but does not embed their field rows; use those linked artifacts for exact field names, requiredness, accepted values and formats rather than inferring constraints from this page or treating sample values as requirements.
- The seven named sections are Identifier, Business information, Owner information, Funding information, ACH information, Discount program registration information and American Express information. A unique identifier is expected per row or MID request to help prevent duplicate entries.
- Business and owner information supports underwriting and setup of features such as PayPal, Venmo and Hyperwallet. Owner information covers owners and authorized signers, with the first owner becoming the account's primary contact; treat these as sensitive personal and business data, and follow PayPal Account Management guidance for ownership requirements rather than copying sample identities into real submissions.
- Funding information is used to set up a biller's Funding profile and Hyperwallet account. ACH information sets up the biller's ACH payment method. American Express information uses the Service Establishment number for setup.
- ACH, discount-program registration and American Express sections are not required for branded solutions. Discount-program information is conditional on the biller being registered; for API use, `discountProgramRegistration.registered` need not be supplied because a value in `discountProgramRegistration.registrationIdentifier` implies `yes`.

## Detail locators

- Availability and bulk-intake purpose: raw lines 17-24.
- PayPal Intake v1/v2 dictionary and sample download routes: raw lines 26-40.
- Separate branded-solution dictionary and sample: raw lines 42-48.
- Seven section names and branded-solution exclusions: raw lines 50-59.
- Unique identifier purpose: raw lines 62-64.
- Business and owner information purposes, sensitive-person scope and primary-contact rule: raw lines 67-78.
- Funding and ACH purposes: raw lines 81-90.
- Conditional discount-program fields and API implication: raw lines 93-101.
- American Express purpose: raw lines 106-110.
- Sample-file navigation: raw lines 113-115.

## Related

- [[braintree]]
- [[braintree-payment-platform]]
- [[braintree-index]]

## Raw Sources

- [[raw/braintree/articles/guides/application-uploader/paypal-intake-data-dictionary-2026-09-16|PayPal Intake Data Dictionary (2026-09-16)]]
