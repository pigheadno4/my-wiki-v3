---
title: "Stripe — Identifying Potential Fraud"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/prevention/identifying-fraud"
raw_files:
  - "stripe-disputes-prevention-identifying-fraud-2026-11-07.md"
  - "stripe-disputes-identifying-fraud-2026.md"
tags: [stripe, fraud, disputes, fraud-indicators, card-testing, shipping, digital-goods, donations]
---

## Overview

Stripe's guide lists possible payment-fraud indicators and merchant review steps for physical shipping, digital goods, and donations. The merchant has purchase and fulfillment context that can help evaluate a suspicious payment. Individual implicit signals do not establish fraud; several together can raise concern. An early fraud warning is an external indicator, while the listed patterns are reasons to investigate. This dated documentation cannot prove that any specific customer or payment is fraudulent. See [[stripe]] and [[disputes]]. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Identifying potential fraud|Guide]]

The 2026-05-10 capture names Radar for Fraud Teams for automatic review of elevated-risk card payments. The 2026-11-07 capture conditions that automatic review on whether **the merchant's Radar plan supports the feature**. It does not identify every qualifying plan. The guide suggests additional review or block rules based on merchant context, but says its recommendations cannot eliminate disputes or fraud. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Identifying potential fraud|Plan-qualified review]] [[raw/stripe-disputes-identifying-fraud-2026#Identifying potential fraud|Earlier wording]]

## Common indicators

The guide suggests reviewing likely false or inconsistent contact details, scripted communications, unusually large orders, and clusters of attempts sharing cards, shipping addresses, IP addresses, names, or similar card numbers. A successful payment following separate failed-card attempts may carry greater fraud risk. Requests to split an order across cards with unshared verified billing details, process a payment manually, overcharge and pay a third party, or refund outside the card network are also listed as signals. These patterns should be assessed together with declined payments and ordinary customer context, not treated as conclusive proof. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Common types of fraud indicators|Indicator list]]

## Shipping physical goods

The guide recommends closer review when billing and shipping addresses differ, while expressly saying that difference alone does not indicate fraud (a gift is one example). For a matching address on a US, Canada, or UK credit card, it advises checking postal and street-address verification. Other review cues include a post-order address change, rush delivery, an unusual card-origin/shipping-country combination, high-cost overnight shipping, international or high-risk destinations, and freight forwarders. It says not to use a customer's “preferred shipper” or pay a third-party shipper on that customer's behalf. A 24–48 hour delay is suggested for high-value, non-verified-address, or first-time-customer shipments; it is not a universal hold period. If a billing postal code was verified, check that shipping-label generation did not change it. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Shipping physical goods|Shipping guidance]]

Shipping data is generally unnecessary to accept a payment, and Stripe generally cannot see the address a customer gives the merchant. Supplying the shipping address when creating a payment can improve Stripe's fraud detection. The page does not say address data guarantees a fraud decision or payment acceptance. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Shipping physical goods|Shipping-data qualification]]

## Digital goods and donations

For digital products or services, the guide suggests collecting and verifying CVC and address details, considering rejection when CVC or postal-code checks fail, and reviewing bursts of purchases, similar accounts, unexpected activity changes, IP/email/usage logs, and actual service use. Review rules are suggested for some patterns; these are risk checks, not a judgment about every customer sharing a detail. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Digital goods or services|Digital-goods guidance]]

For a very large donation from an unknown person, it suggests scrutiny and considering a refund if the donor cannot be verified. Fraudulent actors **sometimes** make a large donation and then request a partial refund to test a stolen card's credit limit. If a donor reports a mistaken amount and asks for the difference back, the guide says a full refund **might be prudent**; the pattern is a suspicion, not proof, and a full refund is a case-specific option. Rapid declines across different cards can suggest card testing; when it looks like testing, the guide suggests considering checkout delay or CAPTCHA. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Donations or crowdfunding|Donation guidance]]

## Marking suspected fraud

The assigned guide states that a payment can be marked fraudulent through the Stripe API or Dashboard and points to the separate Radar risk-evaluation guidance for instructions. It does not itself specify an API field, refund state, or guarantee that reporting changes the outcome. See [[source-stripe-radar-risk-evaluation]] for the separately sourced workflow. [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07#Mark a payment as fraudulent|Fraud-reporting locator]]

## Related

- [[disputes]] — dispute and fraud context
- [[source-stripe-disputes-fraud-types]] — types of fraud
- [[source-stripe-disputes-card-testing]] — card-testing prevention
- [[source-stripe-radar-risk-evaluation]] — separate risk-feedback workflow

## Raw Sources

- [[raw/stripe-disputes-prevention-identifying-fraud-2026-11-07|Stripe fraud-indicator guide, captured 2026-11-07]]
- [[raw/stripe-disputes-identifying-fraud-2026|Stripe fraud-indicator guide, captured 2026-05-10]]
