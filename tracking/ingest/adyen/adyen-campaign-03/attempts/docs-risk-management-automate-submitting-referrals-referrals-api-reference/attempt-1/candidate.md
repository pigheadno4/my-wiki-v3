---
title: "Adyen Referrals API Reference"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/automate-submitting-referrals/referrals-api-reference"
raw_files:
  - "adyen/docs/risk-management/automate-submitting-referrals/referrals-api-reference/2026-09-15.md"
tags: [adyen, risk-management, referrals, block-list, trust-list, api-reference]
---

## Overview

This Adyen Docs reference describes requests to upload referral values to block or trust lists or delete values from a list. It is scoped to a company account through `accountCode` and documents test-platform SOAP, JSON, and FORM endpoints; it directs live integrations to separate generic or custom live endpoints. See [[adyen]] and [[adyen-risk-management]]. The reference describes list-changing operations, not a general read/list CRUD API or proof that any resulting payment risk decision was made.

## Key takeaways

- The stated limit is 10 referrals per request and 10 requests per minute. Each request has one top-level `referralType` and one `action`: `block`, `trust`, or `delete`. Submitted values must match the chosen type. These actions modify list content, so `delete` must not be treated as a harmless lookup or dry run.
- Ordinary referral values use `referrals`/`referralContainer`. Address entries use `addressReferrals` with top-level `referralType: shopperaddress`; payment-derived entries use `paymentReferenceReferrals` with `referralType: paymentreference`. Both special arrays replace the ordinary container. Although the `referrals` table row bears a required marker, its own description says it does not apply to either special array; interpret requiredness by the selected branch.
- For `paymentReferenceReferrals`, provide the payment PSP reference and selected `referralTypes` to extract. The payment must contain each requested property or the request fails. The top-level `reason` is described as automatically generated to include that PSP reference for `paymentreference`, so it cannot be an arbitrary free-text reason in that branch.
- The address object has country and postal-code formats, with `stateOrProvince` required for US and Canadian addresses. The reference's field catalog and sample-value routes are at the raw locators below. Test endpoint presence does not establish live enablement, successful list mutation, or a later fraud decision.

## Detail locators

- Opening and `## Endpoints`, raw lines 14–44 — test/live distinction, request-rate limits, SOAP/WSDL route, JSON/FORM test upload URL, and live-endpoint navigation.
- `## Create upload referrals request`, raw lines 46–84 — action/type constraint, company-account scope, required and conditional payload fields, reason qualification, and referral-type catalog.
- `## referralContainer object`, raw lines 85–101 — ordinary item values and type matching.
- `## paymentReferenceReferrals object`, raw lines 102–122 — PSP-reference extraction, selected property list, and missing-property failure.
- `## shopperAddress object`, raw lines 123–140 — address list shape, country/postal formats, and US/Canada state requirement.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — provider risk and list-control concept.

## Raw Sources

- [[raw/adyen/docs/risk-management/automate-submitting-referrals/referrals-api-reference/2026-09-15|Adyen Docs — Referrals API reference (2026-09-15 snapshot)]]
