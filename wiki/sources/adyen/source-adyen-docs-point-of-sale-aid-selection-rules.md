---
title: "Adyen Docs: POS card application selection rules"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/aid-selection-rules"
raw_files:
  - "adyen/docs/point-of-sale/aid-selection-rules/2026-09-15.md"
tags: [adyen, point-of-sale, card-application-selection, co-badged-cards, least-cost-routing]
---

## Overview

This Adyen POS guide explains how a payment terminal selects a card application or network when a presented card supports more than one. It covers automatic checks and priority rules, configurable least-cost considerations, and the shopper's manual **Card options** choice for a transaction. The stated integration scope is Terminal API with payment terminals or a standalone solution. Its 2025-modified, 2026-09-15-captured rules do not prove current scheme availability, account configuration, regional compliance, exact fees, or the network chosen for a particular payment. [[adyen]] [[adyen-terminal-api]] [[co-badged-cards]]

## Key takeaways

- The page's examples include co-badged local/global schemes, credit/debit combo cards, and US debit cards with global and back-of-card debit networks. In this guide, an **application** means a selectable payment method/network on a multi-application card; it does not supply AID values, BIN tables, or a merchant API parameter for forcing a brand. See **Card application selection**, pinned raw lines 15–25.
- For Terminal API or standalone terminals, automatic selection checks terminal support for the application and transaction type plus current network availability. Rules from the payment request can narrow the path: the guide's installment example selects a credit application for a combo card. Scheme-compliance and least-cost rules are also considered. It says automatic selection aims to avoid an unnecessary shopper choice screen, not that a particular network always wins. See **Requirements / Automatic application selection**, pinned raw lines 27–49.
- Adyen describes different interchange/scheme-fee structures, with illustrative fixed-versus-percentage examples; it says some automatic rule priorities can be customized for merchant cost, PIN verification, or whether a manual-selection screen appears. Compliance-dependent and unsupported-feature rules cannot be changed. The Customer Area route is **Devices > Device settings > Payment features > Card application selection**, and changes require Support or an account manager. A displayed rule priority is not evidence of actual merchant pricing or transaction routing. See **Least cost routing / Customizing application selection rules**, pinned raw lines 51–74.
- The guide says shoppers must be able to prevent automatic selection for a particular transaction; it also describes EEA-issued co-badged cardholder choice when both brands are supported. Its stated terminal software floor for the EEA choice path is **1.109**. This is the page's dated compliance description, not a legal conclusion or proof of a terminal's current software or merchant obligations. The existing [[co-badged-cards]] applicability summary lists in-person France and Germany. That narrower generic summary and this Adyen page's EEA-issued/both-brands wording have not been reconciled; neither is a universal current-law map here. See **Requirements / Manually selecting an application**, pinned raw lines 32–33 and 76–84.
- To choose manually, the shopper selects **Card options** while the payable amount is shown, presents the card, selects a brand, and may need to present the card again. If the card is presented without selecting **Card options**, the page says the default brand continues. The guide notes manual selection can also matter for offline payments when a local application cannot process offline and a global one can; it does not establish offline eligibility for a given transaction. See pinned raw lines 84–96.
- This page concerns physical payment terminals and standalone operation. It does not specify Mobile POS, online checkout, hardware model, cardholder verification outcome, SCA, AID/BIN payload, store-specific enablement, or successful authorization. Its PIN mention is an optional rule-customization consideration, not a general PIN-bypass rule. See complete pinned raw lines 15–100.

## Detail locators

- **Card application selection / Requirements** (pinned raw lines 15–33) — multi-application card categories, integrated/standalone scope and EEA software condition.
- **Automatic application selection** (pinned raw lines 35–49) — terminal, transaction-type and network-availability checks; request, compliance and least-cost rules.
- **Least cost routing** (pinned raw lines 51–62) — fee-comparison rationale and illustrative USD fixed/percentage examples.
- **Customizing application selection rules** (pinned raw lines 64–74) — Customer Area priority display, immutable rule classes, custom reasons and Support route.
- **Manually selecting an application** (pinned raw lines 76–96) — page-stated EEA shopper-choice condition, Card options sequence, default choice and offline example.
- **See also** (pinned raw lines 98–100) — separate cardholder-verification guide.

## Related

- [[adyen-terminal-api]] — primary integrated POS payment and terminal-message route.
- [[adyen-standalone-terminals]] — standalone terminal context.
- [[adyen-payment-terminals]] — physical-device context; this guide gives no model-specific instructions.
- [[co-badged-cards]] — cross-provider cardholder network-choice concept; reconcile regional scope separately.

## Related raw API references

These are navigation links in the guide, not additional behavior reviewed for this entry:

- Co-badged cards compliance — https://docs.adyen.com/online-payments/co-badged-cards-compliance
- Cardholder verification methods — https://docs.adyen.com/point-of-sale/cardholder-verification-methods

## Raw Sources

- [[raw/adyen/docs/point-of-sale/aid-selection-rules/2026-09-15|Adyen POS card application selection guide, fetched 2026-09-15]]
