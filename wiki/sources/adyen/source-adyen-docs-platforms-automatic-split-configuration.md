---
title: "Adyen for Platforms automatic split configuration"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/automatic-split-configuration"
raw_files:
  - "adyen/docs/platforms/automatic-split-configuration/2026-09-15.md"
tags: [adyen, platforms, automatic-splits, split-configuration, balance-accounts]
---

## Overview

This Adyen for Platforms page explains automatic transaction splitting for a platform that processes its users' transactions through stores. A split-configuration profile contains rules with matching conditions and split logic; linking the profile to a user's store lets Adyen apply that logic to transactions processed through the store. The page describes configuration and expected booking behavior, not an executed payment, merchant-of-record assignment, settlement, or payout. [[adyen]] [[adyen-platforms]] [[adyen-automatic-split-configuration]]

## Key takeaways

- Create a profile with at least one rule in Customer Area or through the Management API, then link it to the user's store. A matching rule specifies amounts for the platform's liable balance account and the user's balance account. Currency, payment method, funding source, and shopper interaction are required condition dimensions in this page; card region is optional, while card usage type is described here as a pilot not available to all platforms.
- All of a rule's conditions must match. If multiple rules match, Adyen selects by priority: currency, payment method or variant, card usage type, card region, funding source, then shopper interaction. Within a priority, the more specific rule prevails. The examples illustrate this selection; one scenario's explanatory wording calls the selected funding-source rule a payment-method comparison, so use the stated hierarchy rather than that wording as the rule.
- Split logic can assign platform commission, transaction fees, and optional additional commission; it also includes refund and chargeback amounts/costs, post-conversion remainder, surcharge and tip. The in-person DCC markup allocation is explicitly pilot-only. Transaction fees can be booked to the liable or user balance account, together or separately. The page does not provide the detailed fee-type schema or prove any particular downstream booking.
- A catch-all rule with all conditions set to ANY is recommended. If no specific rule matches without one, the transaction is booked to the platform's liable balance account by default. More broadly, absent profile or per-request split instructions, the page says transaction amounts and fees default to that liable account. Split instructions in an individual payment, capture, or refund request override the automatic split for that request.
- Automatic split amounts use the transaction currency's maximum decimal precision and half-to-even rounding. Fixed commission is in minor units; variable commission is in basis points. By default, variable commission uses the total payment amount including tip and surcharge; Support can configure a choice to exclude either or both. That choice affects variable Commission and Additional commission in the profiles.
- At capture, Adyen checks the profile again, recalculates splits if the captured amount differs from authorization, and uses a profile updated between authorization and capture. Capture-request split instructions override it. Configuration text and examples do not establish actual capture, balance transfer, or financial outcome.

## Detail locators

- Raw lines 15–33: store/profile setup, liable-account default and profile-rule concept.
- Raw lines 35–75: condition and split-logic tables, card-usage and DCC pilots, catch-all fallback and request override.
- Raw lines 77–96: matching-rule granularity and priority order; lines 98–185 contain illustrative scenarios, with a wording inconsistency at lines 138–146.
- Raw lines 187–224: currency precision and half-to-even rounding, including tie examples.
- Raw lines 226–256: commission basis, Support-configured tip/surcharge inclusion and illustrative calculation.
- Raw lines 258–262: capture amount recalculation, profile reevaluation and capture-request override.

## Related

- [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] — separate profile-creation and store-linking guide, with enablement, roles and API examples.
- [[adyen-platforms]] — platform/user and balance-account context.

## Raw Sources

- [[raw/adyen/docs/platforms/automatic-split-configuration/2026-09-15|Automatic split configuration, fetched 2026-09-15]]
