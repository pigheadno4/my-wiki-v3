---
title: "Adyen Referrals API: automate submitting referrals"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/automate-submitting-referrals"
raw_files:
  - "adyen/docs/risk-management/automate-submitting-referrals/2026-09-15.md"
tags: [adyen, risk-management, referrals, risk-lists, api]
---

## Overview

This [[adyen]] guide describes using the Referrals API to upload referral details to block and trust lists for [[adyen-risk-management]]. It covers list scope, actions, prerequisites, rejected or skipped values, and examples for email, IP, shopper address, and payment-reference-derived details. The snapshot does not establish a merchant's live configuration or the outcome of a particular payment.

## Key takeaways

- Block and trust lists are maintained per company account by default. A request may use a merchant or company `accountCode`, but the referral is applied at company-account scope. This scope matters before using `block`, `trust`, or `delete`; the actions respectively block or allow payments associated with the detail, or remove the detail from the account. The page does not say a trust entry overrides every other risk rule or guarantees authorization.
- Supported referral-detail examples are email addresses, IP addresses, billing or shopper addresses, and details connected to a payment's PSP reference. The Referrals API cannot upload custom lists, and API uploads do not allow wildcards; the page says wildcards can be submitted in Customer Area.
- The API credential needs the `API referral lists management` role. For referral matches to trigger, the relevant block and trust lists must be enabled in the risk profile and a score configured for `block` and, where applicable, `trust`. Uploading a list entry alone is therefore not the complete risk configuration.
- Invalid referral values are skipped. The email, IP, and address examples also say entries already present can be skipped, with `skippedReferrals` identifying them in the response. For payment-reference-derived details, an already-present referral can be skipped, while the API request fails if a requested payment detail is absent from the payment identified by `pspReference`. Do not treat a sample `success: true` response as proof every submitted entry was accepted.
- The request examples use different structures: `referrals` with `shopperemail` or `shopperip`, `addressReferrals` with `shopperaddress`, and `paymentReferenceReferrals` with `paymentreference`. They target a `ca-test.adyen.com` endpoint; the guide links the Referrals API reference for details. These examples are test-environment illustrations, not a verified live endpoint or availability claim.

## Detail locators

- `# Automate submitting referrals`, raw lines 14–35 — API purpose, company-account list scope, supported details, custom-list and wildcard limits, and three actions.
- `## Requirements`, raw lines 37–59 — credential role and risk-profile list/score configuration.
- `## Add email address referrals`, raw lines 61–105 — `shopperemail` request, invalid and already-present skip behavior, and response.
- `## Add IP address referrals`, raw lines 107–151 — `shopperip` example, skipped value, and response.
- `## Add shopper address referrals`, raw lines 153–207 — `shopperaddress` payload and invalid country-code example.
- `## Add referrals based on the payment reference`, raw lines 209–258 — `paymentreference` payload, `pspReference` and requested detail types, skip behavior, and absent-detail request failure.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — provider risk-management concept and source routes.

## Raw Sources

- [[raw/adyen/docs/risk-management/automate-submitting-referrals/2026-09-15|Automate submitting referrals (2026-09-15 snapshot)]]
