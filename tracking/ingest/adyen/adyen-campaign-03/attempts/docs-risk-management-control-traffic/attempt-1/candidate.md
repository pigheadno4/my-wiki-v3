---
title: "Adyen Docs: Control traffic"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/control-traffic"
raw_files:
  - "adyen/docs/risk-management/control-traffic/2026-09-15.md"
tags: [adyen, risk-management, protect, control-traffic, fraud]
---

## Overview

This [[adyen]] guide explains control traffic: a very small, randomly selected set of transactions that the page says are settled regardless of their risk evaluation and placed in a separate dataset. Merchants can inspect what risk rules would have done to identify false positives and confirm true positives when evaluating a risk profile. The 2026-09-15 snapshot describes selection exclusions, Customer Area access, and a manual-review boundary; it gives no numeric sampling rate or issuer-authorization rule. See [[adyen-risk-management]].

## Key takeaways

- The guide says selected control-traffic transactions are settled regardless of their risk evaluation, and some may be fraudulent. Reviewing triggered rules and later disputes can help assess whether a risk profile would have blocked a good or fraudulent transaction; the page presents this as a basis for possible risk-setting changes.
- The page excludes transactions of **EUR 2,000 or more**, transactions refused several times in a row, payment methods not included in risk evaluation, and transactions with properties in block or trust lists. It also excludes transactions that trigger a custom rule labeled **Legal**, **Business**, or **Block list**; labeling custom rules requires Protect premium. The page gives no numeric threshold for repeated refusals.
- Control traffic is excluded from manual review. Even when premium features and case-management settings are enabled and matched, a control-traffic transaction cannot be sent to case management.
- An online payments integration is required. The guide calls for **View payments** to look up control-traffic status; changing risk setup requires **Merchant change risk settings** or **Risk admin**. In the **live Customer Area**, merchants can filter the Payment list for Control Traffic = Yes or inspect a payment's risk score page for the control-traffic label.

## Detail locators

- **Purpose and requirements, raw lines 19–32** — false/true-positive analysis, online integration, and distinct lookup versus risk-change roles.
- **How it works and possible impact, raw lines 34–44** — small random selection, stated settlement treatment, separate dataset, and possible fraudulent transactions.
- **Exclusions, raw lines 46–54** — amount, repeated refusals, payment-method risk inclusion, lists, and labeled premium custom rules.
- **Case management, raw lines 56–60** — exclusion from manual review even if premium case-management settings match.
- **Find control traffic, raw lines 62–81** — live Customer Area list filter and single-payment label route.

## Related

- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-configure-your-risk-profile]]
- [[source-adyen-docs-risk-management-case-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/control-traffic/2026-09-15|Adyen control traffic guide (2026-09-15 snapshot)]]
