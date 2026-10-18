---
title: "Adyen Capital higher-amount user-data collection"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/collect-user-data"
raw_files:
  - "adyen/docs/capital/collect-user-data/2026-09-15.md"
tags: [adyen, capital, kyc, anacredit, financing]
---

## Overview

This 2026-09-15 Capital guide describes additional business KYC collection for certain legal entities when a selected financing offer or the new offer plus outstanding balance reaches a country-specific combined-financing threshold. It links the process to AnaCredit data collection. The instructions are for a Capital API integration; the page says UI components facilitate collection through Adyen-hosted onboarding. This dated guide does not prove a user's current country/entity eligibility, a verified capability, an approved offer or grant, legal compliance, disbursement or bank receipt. See [[adyen]], [[adyen-capital]] and [[adyen-platforms]].

## Key takeaways

- **Trigger and country grain:** The introduction says the selected offer or new offer plus existing outstanding balance “meets” a threshold, usually EUR 25,000 or equivalent; the later configuration-flow paragraph says Adyen requires data when total exposure “exceeds” the country/region threshold. Do not resolve that equality boundary from this page alone. Its table applies additional reporting to organizations from EUR 25,000 in Finland, France, Netherlands, Sweden, UK and US (local equivalent where shown), but lists Spain from EUR 3,000; Australia and Canada excluding Saskatchewan are marked not applicable. These are dated product/reporting conditions, not universal financing eligibility or current law.
- **Prerequisites and durable consequence:** The API path calls for a Capital-supporting Adyen for Platforms integration; Balance Platform Capital configuration and grant-initiation roles, a Legal Entity Management API key, getGrantOffers and receiveGrants account-holder capabilities, and Capital/configuration webhooks. The feature supports legal entities created with LEM API v3 or later. The guide says requesting a higher amount automatically assigns an additional-KYC risk level that is currently irreversible, so data is required before future grants even below the threshold. Required data must arrive before the offer expires or a new grant request is needed.
- **Collection routes:** After a selected offer and grant-configuration request, Adyen checks total exposure, signals an unresolved AnaCreditCapabilityRule and Reviewing grant status, and the platform gathers data. Hosted onboarding uses a one-time link for the main legal entity; the page gives four minutes to redirect, one click, one-hour access, and expiry on refresh. The hosted flow collects user submission, including separate parent-company legal entities where relevant. The API-only path reads account-holder capability problems, gathers required fields, PATCHes the main legal entity and, where relevant, creates and associates immediate/ultimate-parent legal entities. Its association PATCH replaces the whole array, so existing entries must be included. These are alternative integration paths, not proof of successful verification.
- **Resolution and status:** The page's API-only example distinguishes capability verification errors and remediation codes from grant action state. It says account-holder verification errors and grant-related actions must be resolved before approval; check account-holder verificationStatus valid/allowed true separately from grant AnaCreditCapabilityRule resolved true/status Approved through the respective webhooks or GETs. The examples are TEST payloads and do not establish a real offer, grant disbursement, final debt or bank credit. The errors table includes a noPossibleRemediation code for CNAE_NUMBER; do not assume every error is fixed by submitting another field.

## Detail locators

- Scope, selected/new-plus-outstanding threshold wording and API/component split: pinned raw lines 15–30.
- Roles, credentials, capabilities, webhooks, LEM version, irreversible risk level and link/offer expiry: pinned raw lines 32–61.
- Configure-grant exposure check and Reviewing/AnaCredit status: pinned raw lines 63–110 and 150–175.
- Hosted link and parent-company path: pinned raw lines 176–365; API-only capability errors and legal-entity field conditions: pinned raw lines 366–518.
- Parent-company create/associate and whole-array PATCH warning: pinned raw lines 755–1052.
- Verification-versus-grant status, country/organization thresholds and error/remediation table: pinned raw lines 1347–1513.

## Related

- [[adyen-capital]] — main Capital concept and reciprocal source route.
- [[adyen-platforms]] — platform account/capability context.

## Raw Sources

- [[raw/adyen/docs/capital/collect-user-data/2026-09-15|Adyen Capital higher-amount KYC guide, captured 2026-09-15]]
