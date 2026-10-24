---
title: "Adyen setup PayPal for marketplaces"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/setup-paypal-marketplaces"
raw_files:
  - "adyen/docs/payment-methods/paypal/setup-paypal-marketplaces/2026-09-15.md"
tags: [adyen, paypal, marketplaces, platforms, setup]
---

## Overview

This 2026-09-15 Adyen guide describes how a **marketplace operator** sets up PayPal to let its marketplace users accept online PayPal payments. It requires a marketplace in the modern Adyen for Platforms integration and expressly excludes Classic Platforms. The page describes PayPal and Adyen account setup, permissions, integration, testing and live preparation; it does not document onboarding each seller, prove current regional eligibility or confirm a payment outcome. [[adyen]] [[adyen-platforms]]

## Key takeaways

- For testing, create a PayPal developer account and associated **business** and **personal** sandbox accounts to simulate merchant and shopper roles. The marketplace account is a separate PayPal account: coordinate with the Adyen contact for its details and referral URL, then use that URL to give Adyen permission to access it. Adyen configures PayPal in Customer Area after that access step; a configuration notification precedes the marketplace's payment integration. No account creation or permission grant was performed by this source ingest.
- The marketplace integration includes split-payment data and the `paypalRisk` fields specified by its PayPal account manager, with Web Drop-in or Web Components as linked implementation routes. The page does not specify a single universal risk-field set or prove that a split, capture or settlement occurred.
- The captured page lists EU-registered marketplace PayPal **settlement** currencies as AUD, CAD, CHF, CZK, DKK, EUR, GBP, HKD, JPY, NOK, NZD, PLN, SEK, SGD and USD. It labels settlement-currency support for Australia, New Zealand, UK and US marketplaces as "Coming soon"; that dated statement does not establish present support or exclusion. It does not state that any listed currency is available for every merchant or payment.
- Sandbox testing uses the business account as merchant and personal account as shopper; test payment status can be inspected in Adyen Customer Area. Live operation separately requires live PayPal business and marketplace accounts, a repeated marketplace referral/Adyen-access step, and Adyen configuration in **live** Customer Area. The source recommends a generic company email for the live business account because that address appears on PayPal shopper receipts. Sandbox status and live setup instructions are not live authorization, capture, settlement or payout proof.
- For disputes, PayPal tells Adyen of a disputed payment but Adyen does not know which marketplace seller it belongs to; the marketplace must map, review and defend disputes for sellers using its own business logic, with a limited response period. Refunds must go through Adyen's live Customer Area or API; the page explicitly warns that issuing them in the PayPal portal causes reconciliation discrepancies.

## Detail locators

- Four-stage setup outline, current Platforms prerequisite, Classic exclusion and dated EU/other-region settlement-currency scope: raw lines 19–53.
- Developer and sandbox account roles: raw lines 55–68. Marketplace account/referral/permission sequence: raw lines 70–78. Adyen configuration before integration, splits, risk fields, and Web implementation routes: raw lines 80–97.
- Sandbox testing/status and distinct live business/marketplace account setup: raw lines 99–127. Seller-dispute ownership and response limit: raw lines 129–140. Adyen-only refund route and PayPal-portal warning: raw lines 142–146.

## Related

- [[adyen-platforms]] — modern Platforms and marketplace context.
- [[adyen-online-payments]] — Web PayPal integration context.
- [[source-adyen-docs-payment-methods-paypal]] — wallet overview and channel routes; do not infer these setup steps establish payment-method enablement.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/setup-paypal-marketplaces/2026-09-15|PayPal marketplace setup guide, captured 2026-09-15]]
