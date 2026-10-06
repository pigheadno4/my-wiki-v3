---
title: "Braintree Account Onboarding API Data Dictionary"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/application-uploader/paypal-uob-api-data-dictionary"
raw_files:
  - "braintree/articles/guides/application-uploader/paypal-uob-api-data-dictionary-2026-09-16.md"
tags: [braintree, account-onboarding, application-data, underwriting, branded-solution]
---

## Overview

This collected [[braintree|Braintree]] webpage is the landing page for the Account Onboarding API Data Dictionary used to prepare the type and format of data for creating many account applications through the onboarding API. The page limits the API to select merchants. It is the Account Onboarding API dictionary route, not the separate PayPal Intake data-dictionary route.

## Key takeaways

- The webpage says the dictionary defines expected application information, acceptable values, and formatting, but those row-level definitions are in linked CSV downloads that were not collected or read for this entry. The page itself therefore does not establish a complete row-level field list, exact CSV column keys, enums, formats, requiredness, validation rules, or a current API schema.
- The general dictionary is organized into Create Account Input, business, stakeholder, funding, ACH, discount-program-registration, and American Express sections. For the Branded solution, the page directs readers to a separate dictionary because only a subset of application data is needed; it specifically says ACH, Discount Program, and American Express information are not needed for that solution.
- Business and stakeholder information is described as serving underwriting and setup of features such as PayPal, Venmo, and Hyperwallet. If people beyond beneficial owners or authorized signers should participate in vetting and review, the page requires at least one Point of Contact; it also requires stakeholder information for any beneficial owner with more than 25% ownership.

## Evidence boundaries

> [!warning] Application data is not approval
> This page describes information for creating applications and says some information is used in underwriting. It does not establish that submitting an application approves a biller, activates an account, enables a feature, processes a payment, or executes a payout.

> [!warning] Linked CSV contents were not read
> The two downloadable dictionaries are navigation targets only in this evidence set. Do not infer the downloads' complete row-level field lists, exact CSV column keys, enums, formats, requiredness, validation rules, or current availability from this landing page.

## Detail locators

- Select-merchant availability and dictionary purpose: opening text, raw lines 17-24.
- General and Branded-solution CSV download navigation: opening text, raw lines 26-34.
- Seven section names and the Branded-solution exclusions: opening text, raw lines 36-49.
- Create Account Input nesting and business-information purpose: `## Create Account Input` and `## Business information`, raw lines 54-63.
- Stakeholder roles, primary-contact treatment, and the greater-than-25%-ownership condition: `## Stakeholder information`, raw lines 66-74.
- Funding, ACH, discount-program-registration, and American Express section purposes: corresponding headings, raw lines 79-96.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Account-onboarding integration guide: [[source-braintree-graphql-integration-guides-account-onboarding]]

## Related raw API references

- [Account Onboarding Data Dictionary CSV](https://developer.paypal.com/braintree/files/uob-api-data-dictionary.csv) - linked download; not collected or read for this entry, navigation only.
- [PayPal Branded Solution Data Dictionary CSV](https://developer.paypal.com/braintree/files/uob-api-branded-data-dictionary.csv) - linked download; not collected or read for this entry, navigation only.

## Raw Sources

- [[raw/braintree/articles/guides/application-uploader/paypal-uob-api-data-dictionary-2026-09-16|Braintree Account Onboarding API Data Dictionary]] - fully read 2026-09-16 webpage snapshot covering select-merchant availability, dictionary purpose, section roles, Branded-solution qualifications, and download navigation
