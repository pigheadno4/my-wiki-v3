---
title: "Adyen Docs: Configure risk settings"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/configure-risk-settings"
raw_files:
  - "adyen/docs/risk-management/configure-risk-settings/2026-09-15.md"
tags: [adyen, protect, risk-management, customer-area, region]
---

## Overview

This Adyen Customer Area guide explains how a merchant configures [[adyen-risk-management|Protect]] risk settings. By default, settings are made on the company account and apply to every merchant account in that company; a specific merchant account can select **Override company settings**. The guide covers general, premium case-management, account, and live-only region settings.

## Key takeaways

- The stated prerequisites are an online-payments integration and a Customer Area user with **Merchant change risk settings** or **Risk admin**. Case-management and risk-based-authentication settings are relevant only when premium features are enabled.
- Selecting additional payment methods changes evaluation by risk lists and custom rules, with custom rules requiring premium. The page explicitly says this selection does **not** affect evaluation by machine-learning rules. Risk-based authentication is enabled by default with premium; the optional force-challenge setting requests a challenge rather than frictionless flow **only for transactions that qualify for risk-based authentication**.
- The general setting **Disable risk management** turns off Protect for the company; the page says risk management is otherwise on by default. Other account settings include excluding recurring transactions from risk evaluation, stopping use of the Adyen global referral block list, and maintaining lists per merchant account. Case-management settings can define actions after accept, reject, or expiry and a capture delay for reviewed payments.
- **Region configuration applies only in live.** Adyen says payments and risk checks use its EU data center by default. It recommends preparing ShopperDNA data in a selected region before switching payment requests to a location-based endpoint: `Storing data` replicates EU data, with 60 days recommended, then `Active` is selected and the regional endpoint used. These are recommended migration steps, not a claim that changing a setting instantly moves processing.
- Moving risk data to another region can have legal, privacy, or regulatory effects; Adyen says configuring the endpoint and risk region instructs it to change the existing setup and advises legal-team review. Region changes are subject to Support review and are **not applied immediately**. The page does not prove current merchant eligibility, account configuration, completion of replication, or transaction outcome.

## Detail locators

- **Requirements / Manage risk settings, raw lines 21–47** — integration and role prerequisites, premium-only settings, company navigation, merchant override, and category list.
- **General, raw lines 49–63** — premium toggle, payment-method selection scope, risk-based authentication and force-challenge condition, in-person risk option, and company-wide Protect disable action.
- **Case management / Account, raw lines 65–82** — case decision and capture-delay options, recurring exclusion, and risk-list controls.
- **Region configuration, raw lines 84–103** — live-only EU default, location-based endpoint, legal/privacy warning, recommended `Storing data` → 60-day replication → `Active` → endpoint sequence, and delayed Support review.
- **Next steps, raw lines 105–113** — risk profile creation, assignment, and configuration routes.

## Related

- [[adyen]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/configure-risk-settings/2026-09-15|Adyen Docs — Configure risk settings (2026-09-15)]]
