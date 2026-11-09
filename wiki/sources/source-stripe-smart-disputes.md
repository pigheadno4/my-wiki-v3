---
title: "Stripe — Smart Disputes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/smart-disputes"
raw_files:
  - "stripe-disputes-smart-disputes-2026-11-07.md"
  - "stripe-disputes-smart-disputes-2026.md"
tags: [stripe, disputes, smart-disputes, ai, evidence, automation]
---

## Summary

Smart Disputes uses an AI rules engine to collect, compile, and submit evidence for **eligible card disputes**. Stripe charges a Smart Disputes fee only if the merchant wins; the issuer decides the outcome, so automation is no win guarantee. The 2026-11-07 guide adds test identifiers absent from the 2026-05-10 capture.

## How It Works

1. For a dispute Stripe determines eligible, it notifies the merchant by email and in the Dashboard.
2. The engine extracts relevant evidence from Stripe internal data, the merchant's transaction data, and cardholder data, tailoring a packet to the dispute reason.
3. If the merchant takes no action, Smart Disputes submits the pre-filled packet just before the dispute deadline. The merchant can instead counter manually or accept before the deadline, and can disable auto-submit in Dashboard dispute settings.

Eligibility considers dispute reason code, payment method, evidence availability, evidence relevance, and cost. Each packet uses data available to Stripe when generated; the merchant remains responsible for its accuracy and completeness. Stripe says the feature requires no additional integration work **if the merchant already uses Stripe**. These guide statements do not establish eligibility or enabled access for a particular account. See the 2026-11-07 raw guide lines 7–30 and the 2026-05-10 guide lines 6–30.

## Pricing and Outcome

The issuer makes the final decision. Stripe says there is no guarantee a Smart Disputes response wins, but it charges the **Smart Disputes fee only on a win**, with no such fee on a lost case. This statement concerns the Smart Disputes fee; it does not establish treatment of other applicable dispute fees. The guide links [Stripe pricing](https://stripe.com/pricing) and says to assess each dispute individually rather than treat the feature as professional advice. See the 2026-11-07 raw guide lines 32–36 and the 2026-05-10 guide lines 32–36.

## Testing

The 2026-11-07 guide says these identifiers create a **Smart Disputes eligible test dispute** (raw lines 38–46):

| Testing method | Value |
| --- | --- |
| Card number | `4000000001000043` |
| PaymentMethod | `pm_card_createAutoRepresentmentEligibleDispute` |
| Token | `tok_createAutoRepresentmentEligibleDispute` |

These are test-mode identifiers, not evidence of a production account's access, eligibility, automatic submission, or win. The 2026-05-10 raw ends at a bare `## Request access` heading (old line 38), without access criteria; the November Testing section does not establish that production access rules changed.

## Related Pages

- [[disputes]] — Stripe dispute concept and Smart Disputes route
- [[source-stripe-smart-disputes-setup]] — setup and API-specific status details
- [[source-stripe-disputes-prevention]] — dispute prevention overview

## Raw Sources

- [[raw/stripe-disputes-smart-disputes-2026-11-07|Smart Disputes guide, fetched 2026-11-07]]
- [[raw/stripe-disputes-smart-disputes-2026|Smart Disputes guide, fetched 2026-05-10]]
