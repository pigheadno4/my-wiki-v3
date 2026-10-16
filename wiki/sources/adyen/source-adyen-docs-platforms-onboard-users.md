---
title: "Adyen Platforms onboard and verify users"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users"
raw_files:
  - "adyen/docs/platforms/onboard-users/2026-09-15.md"
tags: [adyen, platforms, onboarding, verification, hosted-onboarding]
---

## Overview

This Adyen for Platforms overview (last modified 2024-03-04; captured 2026-09-15) compares hosted and API-only user onboarding. Required verification information depends on a user's legal-entity type and operating country, and collection timing depends on verification type. After Adyen receives information, its verification process starts; submission and UI completion do not themselves prove approval, an allowed capability or payment/payout execution. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Route selection:** Hosted onboarding sends users to an Adyen page. Onboarding on invite has the platform request an account holder in Customer Area and Adyen create the required resources; a Customer Area link uses SMS authentication, while the View Verification Status component can create a link and display status. API-initiated hosted onboarding instead has the platform create resources and a link through the Legal Entity Management and Configuration APIs, then redirect the user. API-only onboarding uses the platform's own UI and API submissions; an optional Onboarding component can create the relevant resource from entered data. These are alternative integration routes, not interchangeable account identities.
- **Invite resources and gating:** The invite flow names account holder, balance account, business line and legal entities as separate resources. Although it also lists payment methods and stores, the guide says those are created only after the receivePayments capability is allowed, and are visible in Customer Area only after verification completes. Its default payment-method list depends on the user's legal-entity registration country; it is dated orientation, not a promise of any method for a particular user.
- **API-initiated obligations:** For an LEM API-generated link, the page directs configuration of relevant PCI questionnaires, redirect handling and a server to receive verification-status/results updates. It does not establish PCI compliance or verification approval. The page's general Requirements section states no extra preparation for an Adyen for Platforms integration, but API-initiated and API-only paths still require their stated API work.
- **Conditional hosted features:** The guide lists organization, individual, sole proprietorship and trusts only in Australia/New Zealand, plus a dated hosted-onboarding country list. Instant bank verification is limited by location and entity type. ID-document autofill, guided organization decision-maker roles and decision-maker invitation are limited to onboarding v3 or v4; Latin-character ID documents are required for autofill. A decision-maker's invitation requests their own information and is not proof that they completed verification.
- This overview does not specify Terms of Service acceptance or consent mechanics; use the separate linked onboarding/terms evidence for those questions. Its country, bank-verification and payment-method lists are historical source claims, not current eligibility. Account holder, legal entity, balance account and capability remain distinct.

## Detail locators

- Verification inputs/timing, route definitions and baseline requirement: pinned raw lines 19-28.
- Hosted variants, invite account-holder request, SMS/component link and API-initiated resource/link creation: pinned raw lines 30-62.
- Invite resource list, receivePayments condition and dated payment-method list: pinned raw lines 64-101.
- LEM-link PCI/redirect/status handling and LEM/Configuration API requirements: pinned raw lines 103-121.
- Hosted country list and entity/region-specific instant-bank verification: pinned raw lines 123-198.
- v3/v4 ID autofill, guided decision-maker and invitation qualifications: pinned raw lines 206-237; API-only route and optional component: 239-243.

## Related

- [[adyen-platforms]] — platform onboarding concept and reciprocal source route.
- [[source-adyen-docs-platforms-onboard-users-customize-hosted-onboarding]] — theme, locale and link settings for hosted onboarding.
- [[source-adyen-docs-platforms-onboard-users-terms-of-service]] — separate terms and acceptance evidence.
- [[source-adyen-docs-platforms-verification-overview]] — separate capability and verification-state evidence.

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/2026-09-15|Adyen Onboard and verify users, captured 2026-09-15]]
