---
title: "Stripe: Amazon Pay Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/amazon-pay"
raw_files:
  - "stripe-payments-amazon-pay-2026-11-07.md"
  - "stripe-amazon-pay-2025.md"
tags: [stripe, wallets, amazon-pay, worldwide, multi-currency, manual-capture, disputes, recurring, sepa, a-to-z-guarantee]
---

## Overview

Amazon Pay is a reusable wallet that lets customers check out with information held in their Amazon account. In the November 2026 overview, the customer signs in and authorizes on Amazon's hosted page; Stripe confirms after Amazon authorization and Amazon returns the customer to the merchant's success or confirmation page. The page labels confirmation immediate, access instant provisional, and settlement on the **standard payout schedule**. The return page alone does not independently prove a successful charge or an immediate payout. See [[stripe]], [[stripe-amazon-pay]], and [[stripe-wallets]] (new raw lines 5-15, 170-182; old raw lines 8-12, 24-38).

## Eligibility and currencies

- Customers worldwide may use Amazon Pay, while the November capture lists Stripe account locations AT, BE, CH, CY, DE, DK, ES, FR, GB, HU, IE, IT, LU, NL, PT, SE and US. It marks B2B and B2C and domestic and cross-border use, subject to account enablement (new raw lines 16-43; old raw lines 16-18, 56-76).
- The November account-location table permits the twelve listed presentment currencies—AUD, CHF, DKK, EUR, GBP, HKD, JPY, NOK, NZD, SEK, USD and ZAR—for the sixteen listed European locations, but **US accounts are USD only**. It gives minimum amounts of 0.50 USD, 0.50 GBP and 0.50 EUR, referring other currencies to Stripe's currency minima (new raw lines 40-51). The May prose says US is an exception to multi-currency support, but its adjacent table lists US with all twelve currencies (old raw lines 136-142). That older internal table/prose conflict is dated; November's explicit US row resolves it for this captured overview.
- November marks MCC **6051, cryptocurrency exchanges and wallets, prohibited** (new raw lines 22-30). Merchant or Connect support flags and a listed country do not establish a particular account's category eligibility or activation.
- Amazon Pay stores card credentials and the page lists US alternative methods including Amazon Store Card, installment products, Citi Flex Pay, Affirm and Shop with Points; listed European markets have SEPA Direct Debit (new raw lines 53-60; old raw lines 144-151). These are method examples, not a guarantee that each customer will see every option.

## Capabilities and product routes

The November matrix marks recurring, manual and partial capture, full and partial refunds, and full disputes supported; it marks extended/incremental/decremental/re-authorization, multicapture, overcapture and partial disputes unsupported (new raw lines 62-87). The 90-day refund limit and 240-day general dispute limit are filing/submission windows, not success or settlement windows.

November lists hosted and embedded Checkout, Payment Links, Payment Element, Express Checkout Element, in-app payments, Billing, Invoicing, Customer Portal, Radar and Connect, plus Checkout Sessions, PaymentIntents, PaymentIntents with `setup_future_usage`, SetupIntents and off-session payments. Payment Method Messaging Element, Managed Payments and Terminal are marked unsupported (new raw lines 145-169). The May page had a shorter product list and already stated recurring, Connect and manual capture support (old raw lines 32-50, 78-85). These product flags do not prove identical setup on every UI, unrestricted Connect configuration, live merchant activation, or an off-session payment outcome.

## Refund and dispute boundaries

- Full or partial refunds may be submitted within **90 days of the original payment**. Amazon Pay returns funds to the original form of payment; some non-card transactions may take **up to 14 calendar days to return a final status**. Track the Refund `status` and `refund.updated`/`refund.failed`; a failed refund returns money to the Stripe balance and requires another customer refund method (new raw lines 78-100). May phrased the 14-day interval as starting from purchase (old raw lines 107-111); November does not specify that origin, so do not carry it forward as a new clock.
- Customers have up to **240 calendar days from purchase** to file an Amazon Pay dispute. For a chargeback, evidence is **typically due within 10 calendar days** of dispute creation. An A-to-z Guarantee claim has **90 calendar days from purchase** to be filed and a **six-calendar-day** evidence response period; it incurs no dispute fee. Use the actual Dashboard deadline or Dispute `evidence_details.due_by`, not the typical interval (new raw lines 102-143). The May page stated a generic ten-day evidence period and described fee-free A-to-z claims without the separate six-day/90-day limits (old raw lines 113-134).
- Stripe withholds disputed amount and applicable fee; Amazon Pay decides within 90 calendar days after evidence submission. A merchant win returns amount and fee to the Stripe balance; a customer win makes the charge permanent. The November Dispute object has `payment_method_details.amazon_pay.dispute_type = claim` for an A-to-z claim (new raw lines 106-143). The old page used a less specific `dispute_type = claim` description (old raw line 132).

## Hosted authorization and identifiers

Amazon controls how long the customer has to complete its hosted checkout step; Stripe does not configure an authorization-session timeout for that step (new raw lines 170-182). This statement is about Amazon's hosted session, not a universal lifetime for every PaymentIntent or integration path. The November overview links to a separate accept-payment guide, but that route does not itself update any older path-specific example.

To obtain an Amazon Pay transaction ID, retrieve the PaymentIntent with `expand[]=latest_charge` and read `latest_charge.payment_method_details.amazon_pay.transaction_id`, or retrieve the referenced Charge. Without expansion, `latest_charge` is a Charge ID; the Amazon transaction ID might be absent if Amazon does not provide one. Stripe passes the merchant statement descriptor to Amazon, but Amazon and the funding source control its appearance on the customer statement (new raw lines 184-188).

## Detail locators

- November account/category/currency and alternative payment method details: new raw lines 16-60; May account/currency and alternative methods: old raw lines 14-85, 136-151.
- November capability, refund, disputes and product support: new raw lines 62-169; May refund/dispute baseline: old raw lines 107-134.
- November hosted checkout and Charge identifier: new raw lines 170-194.

## Raw Sources

- [[raw/stripe-payments-amazon-pay-2026-11-07|Amazon Pay overview — 2026-11-07 full capture]]
- [[raw/stripe-amazon-pay-2025|Amazon Pay overview — 2026-05-07 full capture (historical filename)]]
