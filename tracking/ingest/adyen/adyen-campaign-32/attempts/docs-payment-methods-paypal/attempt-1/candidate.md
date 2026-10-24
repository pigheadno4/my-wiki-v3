---
title: "Adyen PayPal payment-method overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal"
raw_files:
  - "adyen/docs/payment-methods/paypal/2026-09-15.md"
tags: [adyen, paypal, venmo, wallets, online-payments]
---

## Overview

This [[adyen]] payment-method overview describes PayPal wallet payments, a separate Venmo option within the PayPal Web Component/Drop-in, channel-specific direct versus redirect flows, conditional feature support, PayPal risk-data obligations, and links to channel guides. Its “International”/“Multiple” PayPal table labels and child links are broad overview metadata, not proof of a merchant's enabled countries, currencies, features, or completed payment. [[adyen-online-payments]]

## Key takeaways

- The PayPal row calls it a **wallet**, labels the flow **Direct**, and marks recurring, refunds, several partial/multiple refund and capture variants, and chargebacks with checkmarks; several cells say “See note” without a clearly corresponding PayPal-specific note in this page. The channel section narrows the flow: **Web is direct**, while **iOS/Android require redirect**. Do not treat the overview checkmarks as unconstrained capture/refund entitlement or an actual transaction result. See raw lines 23–27 and 55–87.
- The PayPal Web Component can be configured for **express checkout**. For Web Drop-in/Components, the page dates PayPal and PayPal Credit Smart Payment Buttons to **v3.7.0+** and PayPal Pay Later to **v5.12.0+**, limited here to AU, FR, DE, IT, ES, UK, and US with local currencies. These are guide version/region claims, not current account or shopper availability. It recommends the latest Checkout API version without giving a minimum API version. See raw lines 29–31 and 55–87.
- **Venmo is a narrower, distinct option:** Web Drop-in/Web Component **v5.42.0+**, exclusively inside the PayPal Component; by default it appears only when both merchant and shopper are in the US, and it can be disabled. Its table says Direct (Web), US, USD, **no recurring**, and marks refunds/capture/chargebacks with notes. Multiple partial captures and partial refunds require additional Adyen configuration; payments are captured immediately after authorization by default; Venmo handles all chargebacks directly. Do not import the broader PayPal table's recurring or geography labels into Venmo. See raw lines 33–53.
- PayPal requires merchants in **specific verticals and marketplaces** to provide transaction-context risk data through `additionalData.paypalRisk`. The page directs merchants to ask their PayPal account manager which fields, if any, apply. This is conditional, not a universal field list or proof of PayPal account approval. See raw lines 89–93.
- The Web, iOS, Android, API-only, and Pay by Link entries are navigation to separate guides. This overview does not supply their requests, redirects/returns, billing-agreement consent, capture execution, or settlement procedure. See raw lines 95–125.

## Detail locators

- PayPal capability matrix and ambiguous “See note” cells: raw lines 23–27.
- Express Web route, Venmo versions/default/notes: raw lines 29–53.
- Channel and Smart Payment Button version/region scopes: raw lines 55–87.
- Conditional `paypalRisk` and child-guide menu: raw lines 89–125.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/2026-09-15|Adyen PayPal overview snapshot]]
