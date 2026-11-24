---
title: "Stripe Terminal: Configure On-Reader Tips (Fleet)"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/fleet/tipping"
raw_files:
  - "stripe-terminal-tipping-config-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, tipping]
---

## Summary

The 2026-05-01 [[stripe]] Terminal fleet guide covers on-reader tip settings through the Dashboard and the Configuration API. The 2026-11-07 base capture links to separate Dashboard and API variants.

## Key Details

**Tip modes in May**. The reader displays three suggestions before the customer presents a payment method. Smart tips switch between three percentages and three fixed amounts based on the pre-tip amount. The other modes display three percentage suggestions or three fixed amounts.

**Dashboard in May**. From a location’s details or the Manage locations page, open its configuration and edit or override **Tipping**. Choose the mode and currency, enter the suggestions, then select **Review**, **Confirm** and **Apply changes**. In this Dashboard section, Stripe says it applies the settings on the reader within 10 minutes.

**API in May**. Create or update a Configuration object with tipping settings keyed by currency. The USD example uses `tipping: { usd: { percentages: [...], fixed_amounts: [...], smart_tip_threshold: 1000 } }`. The separate on-reader guide explains that this example shows fixed amounts below USD 10 and percentages at or above USD 10. It also requires the same configuration keys for each currency in a multicurrency Configuration.

## Related

- [[source-stripe-terminal-on-reader-tipping]] — detailed threshold, multicurrency and reader-specific timing. The separate guide says BBPOS WisePad 3 receives updates when it connects to the POS application, and BBPOS WisePOS E can take up to five minutes.
- [[source-stripe-terminal-configurations]] — account defaults and location overrides for Terminal configurations
- [[stripe-terminal-tipping]] — SDK-level tipping behavior and on-receipt tipping

## Raw Sources

- [[raw/stripe-terminal-tipping-config-2025|Stripe Terminal fleet tipping guide captured 2026-05-01]]

## Related raw API references

- [[raw/stripe-terminal-fleet-tipping-2026-11-07|Stripe Terminal fleet tipping Dashboard and API index captured 2026-11-07]]
