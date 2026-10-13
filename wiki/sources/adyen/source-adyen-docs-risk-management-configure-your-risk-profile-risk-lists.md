---
title: "Adyen Docs: Risk lists"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/configure-your-risk-profile/risk-lists"
raw_files:
  - "adyen/docs/risk-management/configure-your-risk-profile/risk-lists/2026-09-15.md"
tags: [adyen, risk-management, risk-lists, referrals, fraud]
---

## Overview

This [[adyen]] guide describes risk lists, also called block and allow lists or referrals, for using known shopper, card, and bank details in transaction risk decisions. Lists can draw on Adyen, merchant, or third-party data. This 2026-09-15 documentation snapshot describes configuration and editing in Customer Area and the Referrals API; it does not establish a particular merchant account's settings or a payment outcome. See [[adyen-risk-management]].

## Key takeaways

- The guide requires an online payments integration with risk management enabled and a Customer Area user with **Manage referral lists** or **Risk admin**. Default block and allow lists are available; **custom risk lists require premium features**. Shopper name, email, and IP details are masked by default, and viewing unmasked details requires **Merchant view PII**. Users without that PII role are directed to the Fraud control widget to edit lists.
- Risk lists are maintained at the company-account level by default and can be configured separately for merchant accounts in risk settings. The listed default payment-method scope is credit and debit cards, SEPA Direct Debit, and PayPal; other payment methods must be added in risk settings to include them in risk evaluation. Configuration can differ by risk profile.
- A payment request must include the field used by a configured list for that list to trigger; for example, an email list needs `shopperEmail`. The default-list table covers card or bank data and shopper attributes. The **Adyen global referral list** is a distinct option: when enabled in risk settings, a match to scheme-reported stolen or fraudulent card or bank details is blocked before authorization, while its entries are not visible in the merchant block list. Do not extend that before-authorization behavior to every risk list.
- Customer Area editing routes include a single item, CSV upload for most lists, and a transaction's Fraud control widget; the Referrals API can automate list uploads. Widget attributes vary by payment method.

## Detail locators

- **Requirements, raw lines 21–30** — integration, Customer Area roles, custom-list premium condition, and masked PII access.
- **How it works, raw lines 32–40** — company versus merchant scope, default payment methods, profile-specific configuration, and payment-request field matching.
- **Default risk lists, raw lines 42–60** — card, bank, and shopper list types and the global referral list's before-authorization effect and visibility limit.
- **View and edit risk lists, raw lines 62–114** — Customer Area navigation, single-item and CSV editing, PII limitation, and Referrals API route.
- **Fraud control widget, raw lines 118–135** — transaction-specific editing and payment-method-dependent attributes.

## Related

- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/configure-your-risk-profile/risk-lists/2026-09-15|Adyen risk lists guide (2026-09-15 snapshot)]]
