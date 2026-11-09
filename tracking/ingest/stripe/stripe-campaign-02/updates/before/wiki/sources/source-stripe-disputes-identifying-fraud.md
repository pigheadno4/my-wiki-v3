---
title: "Stripe — Identifying Potential Fraud"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-identifying-fraud-2026.md"
tags: [stripe, fraud, disputes, fraud-indicators, card-testing, shipping, digital-goods, donations]
---

## Summary

Practical fraud identification guide: common indicators, shipping fraud signals, digital goods risks, donation fraud, and how to mark payments as fraudulent.

## Common Fraud Indicators

- False info: fake email/phone patterns (e.g. `asdkf12495@freemail.example.com`)
- Inconsistent customer details across purchases (same email, different name)
- Scripted communication — search the phrase in quotes to see if used elsewhere
- Unusually large/expensive orders or multiples of same item
- Payment patterns: same card + different shipping, many cards + same shipping, same card + same IP, rapid different-card failures → successful payment = high risk
- Red flag requests: split payment across unverified cards, manual processing (to use your IP), overcharge + pay third-party, refund outside card network

## Shipping Physical Goods

- Shipping ≠ billing address: scrutinize more carefully; check postal code + street verification for US/CA/UK cards
- Watch for post-order address change requests
- Rush/overnight delivery (fraudsters want goods before card reported stolen)
- Card country mismatch with shipping country
- Never use "preferred shipper" or pay third-party shipping company on customer's behalf
- 24–48hr delay for high-value / first-time / unverified-address orders
- USPS postal code autocorrect exploit: verify the shipping label shows the billing postal code
- Extra care for freight forwarders

## Digital Goods

- Spam/rapid purchases, multiple accounts with same email or card
- Rapid charges to same email → add to review queue via review rule
- Unexpected account activity spikes
- Collect CVC + postal + street address; consider rejecting CVC/postal code failures

## Donations / Crowdfunding

- Scrutinize large donations from unknown individuals
- "I made a mistake, please refund the difference" → tests credit limit → refund the entire donation instead
- Rapid declined payments with different cards = card testing

## Mark as Fraudulent

Via Dashboard → payment → Refund → Fraudulent, or API `fraud_details.user_report = 'fraudulent'`. See [[source-stripe-radar-risk-evaluation]].

## Related Pages

- [[disputes]] — concept page (updated with fraud identification indicators)
- [[source-stripe-disputes-fraud-types]] — 7 fraud type categories
- [[source-stripe-disputes-card-testing]] — card testing prevention

## Raw Sources

- [[stripe-disputes-identifying-fraud-2026]] — verbatim fraud identification guide
