---
title: "Adyen Classic Platforms: manage account-holder risk with Score"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/identify-account-holder-risk/review-and-manage"
raw_files:
  - "adyen/docs/classic-platforms/identify-account-holder-risk/review-and-manage/2026-09-15.md"
tags: [adyen, classic-platforms, risk, score]
---

## Overview

This Classic Adyen for Platforms Score guide (last modified 2020-12-22; captured 2026-09-15) describes Customer Area review of linked account-holder identities, risk scores and signals, followed by role-gated manual or configured actions. Score must first be enabled for the platform through an Adyen Account Manager, who assigns required Customer Area roles. The page directs new implementations to a separate newer integration guide; its Classic Score workflow does not establish current product availability or that a particular risk action, refund or payout occurred. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- **Merchant MarketPlace** can view case management and risk signals. **Merchant Marketplace Risk** adds identity actions, including disabling payouts, suspending account holders, refunding transactions, adding values to a high-risk list and marking signals false positive. **Merchant Marketplace Risk Admin** adds Score settings, custom signals, automated actions, signal weights, trusted identities, linked-identifier exclusion and bulk high-risk-list edits.
- The case dashboard groups account holders into identities with scores and sorts highest risk first by default; users can filter and review signals on the full identity or account-holder Score tab. A false-positive dismissal lifts a signal for the whole identity; dismissing all signals resets its risk score. Trusting an identity prevents a known trusted identity from appearing in case management.
- Manual action boundaries matter: transaction refunds are possible **only after an account is suspended**; high-risk-list KYC values should come only from **confirmed fraudulent** account holders. Excluding a linked KYC identifier breaks the identity link and **cannot be undone**. This permanent action requires the Risk Admin role and confirmation.
- Admins can change signal impact, create custom transaction/KYC signals, bulk-upload KYC values, and configure automation for high-risk lists/custom signals. The documented automated choices are **No action**, **Bump KYC tier**, or **Disable payouts**; the manual refund and suspension actions are not listed as automation choices. The Automated actions log shows actions taken for accounts.
- The page describes Customer Area controls and possible effects, not an API contract or a verified fraud finding. A risk score or disabled-payout setting is not proof of payment, settlement, payout, reversal or bank receipt.

## Detail locators

- Raw lines 19–29 set Classic scope, Score enablement and three role tiers.
- Raw lines 31–57 describe case management, identity-level review and navigation.
- Raw lines 59–93 define manual identity actions, false-positive dismissal and permanent KYC-link exclusion.
- Raw lines 95–145 cover admin Score settings, risk-signal weights and custom signal examples.
- Raw lines 146–179 give automated-action choices, log route and high-risk-list CSV upload.

## Related

- [[adyen-classic-platforms]] — Classic platform model.
- [[adyen]] — provider context.
- [[adyen-platforms]] — separate current Platforms model.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/identify-account-holder-risk/review-and-manage/2026-09-15|Adyen Classic Platforms Score risk management, captured 2026-09-15]]
