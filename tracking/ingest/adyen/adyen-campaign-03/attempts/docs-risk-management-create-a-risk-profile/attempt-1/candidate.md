---
title: "Adyen Create and Assign Risk Profiles"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/create-a-risk-profile"
raw_files:
  - "adyen/docs/risk-management/create-a-risk-profile/2026-09-15.md"
tags: [adyen, protect, risk-management, risk-profiles, merchant-accounts]
---

## Overview

This Adyen Protect guide explains how a company-account user creates a risk profile, assigns it to merchant accounts, and optionally selects a different profile for an individual online payment. A profile holds risk rules and settings that govern which risk rules apply to payments on a merchant account.

## Key takeaways

- The guide assumes an online-payments integration, enabled/configured risk management, and a Customer Area user with either **Merchant change risk settings** or **Risk admin** role. It says a default profile is available when risk management is first configured. Company-account users create and configure profiles, then assign a profile to one or more merchant accounts. In-person risk-profile creation has separate considerations.
- The profile's available controls depend on Protect basic versus premium features enabled in risk settings. The guide's tier table places custom lists and rules, machine-learning fraud detection, experiments, profile/rule analytics, and case management in premium. The table is a snapshot of documented capabilities, not evidence that a merchant has premium enabled.
- To create an additional profile in Customer Area, the user names it and selects an existing profile as its template, then configures its rules. Merchant-account assignment is a separate action under the profile's **Merchant accounts** settings.
- For a specific payment, the merchant can override its merchant account's assigned profile by sending the desired profile's unique reference as `riskData.profileReference` in a Checkout `/sessions` or `/payments` request. If the request omits this reference, the merchant account's default profile applies. The sample request values are examples; this page does not establish a payment's risk decision or authorization outcome.

## Detail locators

- Opening and `## Requirements` (raw lines 15–34): profile purpose, Protect/risk-setting prerequisites, company versus merchant account roles, Customer Area roles, premium limit, and in-person route.
- `## Risk profile` (raw lines 36–50): basic/premium feature comparison.
- `## Create a risk profile` (raw lines 52–67): company-account Customer Area creation, template selection, and later configuration/assignment routes.
- `## Assign a risk profile to a merchant account` (raw lines 69–78): merchant-account selection and save action.
- `## Assign a risk profile to a payment` (raw lines 80–146): default-versus-override rule, profile reference lookup, `riskData.profileReference`, and example `/sessions` and `/payments` requests.

## Related

- Company: [[adyen]]
- Concept: [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/create-a-risk-profile/2026-09-15|2026-09-15 Adyen risk-profile creation and assignment guide]]
