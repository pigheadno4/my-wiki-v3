---
title: "Adyen Adobe Commerce payment-method setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/set-up-the-payment-methods-in-adobe-commerce"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/set-up-the-payment-methods-in-adobe-commerce/2026-09-15.md"
tags: [adyen, adobe-commerce, payment-methods, checkout-configuration]
---

## Overview

This Adyen webpage describes configuring payment methods and their checkout presentation in the Adobe Commerce plugin's admin panel. A method must first be added in Adyen Customer Area, then enabled in Adobe Commerce to render it in checkout. The page's configuration descriptions do not establish current merchant eligibility, successful payment, capture or settlement. See [[adyen]] and [[adyen-magento2]]. The retained [[source-github-adyen-magento2]] is a separate exact-version repository baseline; this webpage does not pin a plugin release.

## Key takeaways

- The general **Payment methods enabled** setting retrieves methods already added in Customer Area. Availability and rendering remain method- and account-dependent. For card checkout, the guide says **Visa support requires both showing and requiring the holder-name field**. Installments are limited by country/region and need per-card rules when enabled.
- Alternative-method settings include a gift-card refund strategy for mixed-method payments, a configurable country used to determine methods shown (defaulting to shopper billing address), locale, Boleto settings and Apple Pay domain-association download. Headless gift cards have extra steps in the linked headless guide. These are configuration choices, not proof of a specific refund allocation or available method in a live checkout.
- Online checkout return-path fields differ from **headless** Payment Origin URL, Payment Return URL and Customer Success Redirect Path. If the headless frontend origin differs from the Adobe Commerce base URL, set the origin where the 3D Secure Component loads. A success redirect path or Order Increment ID parameter is navigation configuration, not payment confirmation.
- Express module settings include placement options and Apple Pay button color. For **PayPal Express**, PayPal Business and Adobe Commerce phone-number requirements must agree; a mismatch can prevent order creation. For HUF PayPal transactions, the guide says transaction and line-item amounts must round to whole amounts and add up, or PayPal may reject the transaction after Adyen rounding causes a discrepancy.
- **Admin orders** are separate paths. Pay by Link requires Customer Area link-creation permissions and remains unfinished until the shopper follows the link and pays; the guide says plugin cron closes unfinished orders. MOTO requires a MOTO merchant account and related Client/API keys with Test or Live mode selection. Neither setup creates a paid order by itself.
- **Giving** is described as enabled by default, using active Customer Area campaigns and fixed-amount or round-up post-checkout donations; a shopper choice would charge the same method used for the original transaction. The page routes stored payment methods to a separate tokenization guide and gives testing/go-live links. It states no capture configuration, token-consent contract or live donation outcome.

## Detail locators

- Customer Area prerequisite and plugin enablement: pinned raw lines 19–37.
- Card holder-name, installments and alternative-method settings: pinned raw lines 39–76.
- Online versus headless return/origin fields: pinned raw lines 78–96.
- Express placement, PayPal phone mismatch and HUF amounts: pinned raw lines 98–121.
- In-person/admin order, Pay by Link permissions and MOTO account/credential steps: pinned raw lines 123–185.
- Giving defaults/campaigns, separate tokenization route and test/go-live pointers: pinned raw lines 187–213.

## Related

- [[adyen-magento2]] — Adobe Commerce plugin concept and version boundary.
- [[source-adyen-docs-plugins-adobe-commerce-headless-integration]] — headless checkout route for separate gift-card steps.
- [[source-github-adyen-magento2]] — independently versioned implementation evidence.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/set-up-the-payment-methods-in-adobe-commerce/2026-09-15|Adyen payment-method setup guide, captured 2026-09-15]]
