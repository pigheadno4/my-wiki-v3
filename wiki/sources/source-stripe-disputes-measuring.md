---
title: "Stripe — Measuring Disputes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/measuring"
raw_files:
  - "stripe-disputes-measuring-2026-11-07.md"
  - "stripe-disputes-measuring-2026.md"
tags: [stripe, disputes, dispute-rate, dispute-activity, monitoring, radar, early-fraud-warnings]
---

## Summary

The May 10 and November 7, 2026 captures distinguish dispute activity by dispute date from dispute rate by original charge date, each using successful payments as its denominator. The guide explains network monitoring, charge-cohort analysis, conditional predicted activity, and early fraud warnings (EFWs). The captures do not establish a specific account's live metrics, program placement, fine, Radar access, or alert. See [[disputes]]. [May capture](../../raw/stripe-disputes-measuring-2026.md#L8-L49); [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L9-L50)

## Two metrics

| Metric | Numerator and cohort | Denominator | Use |
| --- | --- | --- | --- |
| Dispute activity | Disputes received by **dispute date** in the period | Successful payments in that period | Card-network dispute and fraud monitoring programs |
| Dispute rate | Disputes associated with successful payments by **original charge date** in the period | Successful payments charged in that period | Identify problematic payments and fraud patterns |

The captured example has 1,000 successful payments processed in a week and 10 disputes received in that week; only three disputes relate to that week's payments. Activity is 10/1,000 = **1%**; rate for the payment cohort is 3/1,000 = **0.3%**. The other seven disputes came from earlier payments. This is an illustration, not an account calculation. [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L9-L19); [May capture](../../raw/stripe-disputes-measuring-2026.md#L8-L18)

The guide locates dispute activity under Dashboard Analytics. It labels the dispute-rate Dashboard route `dashboard.stripe.com/radar` as **Radar for Fraud Teams** in May and **Radar** in November. This is a captured UI-label change, not evidence of changed calculation or entitlement. [May capture](../../raw/stripe-disputes-measuring-2026.md#L20-L30); [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L21-L31)

## Monitoring and time window

The guide calls dispute activity above **0.75%** excessive as an industry standard, while a sudden spike or steep upward trend can trigger program placement before 0.75%. Card networks set their own monitoring thresholds; prolonged excess (usually multiple months) might lead to fines. The guide says all disputes count whether won or lost. These statements are not a universal numeric placement threshold, actual account placement, or an assessed fine. [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L21-L23); [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L33-L37)

Because cardholders can dispute up to 120 days after payment **and sometimes later**, a charge-date dispute rate can change for dates under 120 days old, and the capture gives no guaranteed finality at day 120. [May capture](../../raw/stripe-disputes-measuring-2026.md#L29); [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L30)

## Predicted dispute activity

**In some cases**, Stripe says its AI models can predict possible future excessive dispute activity; **if that happens**, Stripe says it will alert the account. It cannot predict which individual payments will be disputed, and the predicted rate remains uncertain as further disputes arrive. A particular account's prediction or alert is not established here. [May capture](../../raw/stripe-disputes-measuring-2026.md#L38-L43); [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L39-L44)

## Early fraud warnings and VAMP

EFWs are issuer-generated suspected-fraud messages on Visa, Mastercard, and JCB. They may give an opportunity to refund before a fraud dispute, but a refund is not guaranteed to prevent one. Networks also use EFWs as a fraud metric; Visa counts them toward identification in its VAMP monitoring program. An EFW is not itself a formal dispute, and the captures do not establish automatic dispute conversion. [May capture](../../raw/stripe-disputes-measuring-2026.md#L45-L49); [November capture](../../raw/stripe-disputes-measuring-2026-11-07.md#L46-L50)

## Related Pages

- [[disputes]] — concept page with reciprocal measuring route
- [[stripe-high-risk-merchant-lists]] — related card-network monitoring context
- [[source-stripe-disputes-how-disputes-work]] — dispute timing and EFW details

## Raw Sources

- [[raw/stripe-disputes-measuring-2026-11-07|November 7, 2026 measuring disputes capture]] — same-URL webpage text (60 lines)
- [[raw/stripe-disputes-measuring-2026|May 10, 2026 measuring disputes capture]] — historical webpage text (59 lines; three chart images)
