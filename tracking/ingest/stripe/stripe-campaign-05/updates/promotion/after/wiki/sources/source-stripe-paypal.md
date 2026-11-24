---
title: "Stripe: PayPal Payments (via Stripe)"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/paypal"
raw_files:
  - "stripe-payments-paypal-2026-11-07.md"
  - "stripe-paypal-2025.md"
tags: [stripe, wallets, paypal, europe, eur, gbp, usd, recurring, connect, marketplace, seller-protection, 180-day-refunds]
---

## Overview

The May 7 and November 7, 2026 guides describe the Stripe-processed PayPal wallet (`paypal`) for buyers worldwide and Stripe accounts in the 30 listed European countries. Merchants outside the stated business locations or opting to process through their own PayPal account can review the distinct [[source-stripe-paypal-custom-payment-method|PayPal custom payment method]]. See May lines 8–22 and 52–85 and November lines 9–23 and 53–86.

- **Business locations.** AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI and SK. The listed scope includes Switzerland, the UK, Liechtenstein and Norway.
- **Presentment.** EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD and SGD. PayPal has no separate minimum charge. Stripe's general minimum and maximum charge amounts still apply.

## Customer flow and merchant activation

After selecting PayPal, the customer is redirected to PayPal, signs in, chooses wallet balance, a linked card or bank account, or buy now, pay later, and authorizes the payment. Both introductions describe a redirect back to the merchant's site after successful authorization. The flow captions label a customer return visit to the merchant's site optional. Stripe separately notifies the merchant immediately of payment success or failure. Standard payout timing applies independently of payment confirmation.

The guides list Checkout, Payment Links, Elements, Subscriptions and Invoicing. The normal route is enabling PayPal from the Dashboard for dynamic display and following the PayPal go-live activation guide. Recurring payments can require separate approval. See May lines 26–42, 87–112 and 126–130, November lines 27–43, 88–112 and 137–141, [[source-stripe-paypal-activate]] and [[source-stripe-paypal-set-up-future-payments]].

## Connect for online marketplaces

Connect support is limited to online marketplaces that collect payments and pay out to sub-accounts or service providers. Platforms that enable onboarded businesses to accept payments directly are excluded. Destination charges and separate charges and transfers are supported. Direct charges and `on_behalf_of` are unsupported.

The November guide tells eligible marketplaces to open **Payment method settings** in the Dashboard, select **Request access** next to PayPal and complete the form. Stripe and PayPal review each request, which can take several weeks. The marketplace can check progress in Payment method settings. Once approved, it receives instructions for connecting its PayPal account. November says the marketplace does not need to enable PayPal in connected-account payment method configurations because direct charges and `on_behalf_of` are unsupported. The May guide described email progress updates and status in Payment method settings. November retains status tracking and does not repeat the email wording. See May lines 114–124 and November lines 114–135.

## Refunds, disputes and reporting

Full or partial refunds can be initiated in the Stripe Dashboard or API within 180 days of the original payment. If settlement is to Stripe, refunds draw from available Stripe funds. If settlement is to PayPal, refunds use the PayPal balance or another funding source available in that PayPal account. See May lines 140–144 and November lines 151–155.

Submit dispute evidence in the Stripe Dashboard. For dispute types where PayPal offers direct customer contact, use the PayPal Dashboard for that contact. PayPal's Seller Protection applies to eligible transactions, with examples including unauthorized payments and claims of non-receipt. Separate program and dispute criteria govern eligibility. PayPal fees appear in **Less fees** in the Stripe Balance and Balance Activity reports and are excluded from Stripe's tax invoice. Access PayPal's fee documents through its Dashboard. The guides also say certain businesses need PayPal pre-approval under its Acceptable Use Policy in addition to Stripe's restrictions. See May lines 132–160 and November lines 143–171.

## Related Pages

- [[stripe-wallets]] — Wallet methods and PayPal integration context
- [[source-stripe-paypal-custom-payment-method]] — PayPal through a merchant's own account via a custom payment method
- [[source-stripe-paypal-activate]] — Standard PayPal go-live setup
- [[source-stripe-paypal-disputes]] — PayPal dispute operations
- [[source-stripe-paypal-settlement]] — Settlement preference and reporting
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-paypal-2026-11-07|November 7, 2026 Stripe-processed PayPal]] — Full overview with marketplace request and review details
- [[raw/stripe-paypal-2025|May 7, 2026 Stripe-processed PayPal]] — Earlier full overview, with five captured flow diagrams
