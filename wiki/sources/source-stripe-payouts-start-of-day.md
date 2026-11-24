---
title: "Stripe — Customized Start of Day"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payouts/customized-start-of-day"
raw_files:
  - "stripe-payouts-customized-start-of-day-2026-11-07.md"
  - "stripe-payouts-start-of-day-2026.md"
tags: [stripe, payouts, start-of-day, timezone, apac, reconciliation]
---

## Summary

Customized start of day sets the local-day cutoff Stripe uses to group payments into automatic payouts for reconciliation. The Singapore example groups payments across successive midnight SGT cutoffs or successive 06:00 SGT cutoffs, depending on the configured start time.

## Default cutoff and availability

- The November 7, 2026 guide describes the default as midnight in the user's time zone, with exceptions for some APAC users. Stripe usually allows a local cutoff between midnight and morning.
- The direct guide lists AU, HK, ID, IN, JP, MY, NZ, PH, SG and TH. It also offers an email request to join the preview. The form leaves the geographic scope, eligibility and access decisions unspecified.
- A connected account without access to the full Stripe Dashboard or under platform control uses the platform's cutoff. Stripe links to the [Connect customized start-of-day guide](https://docs.stripe.com/connect/customized-start-of-day) for platform customization in certain countries. That companion guide lists AU, HK, ID, IN, JP, MY, NZ, SG and TH and documents a private preview for US connected accounts. The scope of that preview is specific to connected accounts.

## Dashboard setup and effect on payout grouping

1. Open **Settings** → **Linked accounts and payouts** → [**Settlement and transfer rules**](https://dashboard.stripe.com/settings/settlement).
2. In **Start of day**, select the preferred cutoff. The change takes effect at the new cutoff. Changing the cutoff at 07:00 SGT to 00:00 SGT takes 17 hours in Stripe's example.

Each original transaction retains the payout settings and timing in effect when it was created. In Stripe's example, USD 500 each attributed to UTC Monday and Tuesday keep their original grouping and process the following Monday and Tuesday after a Wednesday change to Singapore time. New payments after the change use the new settings. In the New York illustration, a daily automatic payout with four-business-day timing groups Monday's midnight-to-midnight ET sales into one payout that arrives before the end of Friday. Those assumptions govern the timing illustration.

## May 2026 capture

The May 11, 2026 guide described the default as UTC midnight with some APAC exceptions and listed the same direct markets. It said Express and Custom accounts used one common cutoff chosen by the platform. It directed users to **Settings** → **Business** → **Bank accounts and currencies** → **Start of day**. Both captures describe the effective-time and original-transaction payout rules.

## Related Pages

- [[stripe-payouts]] — automatic payouts and reconciliation
- [[stripe]] — provider overview

## Raw Sources

- [[raw/stripe-payouts-customized-start-of-day-2026-11-07]] — full November 7 capture
- [[stripe-payouts-start-of-day-2026]] — full May 11 capture with two Dashboard screenshots
