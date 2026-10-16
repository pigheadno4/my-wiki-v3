---
title: "Adyen Pass-through payout"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/pass-through-payout"
raw_files:
  - "adyen/docs/account/pass-through-payout/2026-09-15.md"
tags: [adyen, pass-through-payout, merchant-settlement, payable-batch, reconciliation]
---

## Overview

This Adyen page describes **Pass-through payout** for a merchant account's sales proceeds: funds enter a payable batch as card schemes or payment methods send them to Adyen, then the batch closes according to the merchant's payout frequency for payout. It is a merchant-settlement model, not an API for sending money to a separate recipient. The page was last modified in 2020 and captured 2026-09-15; its example and timing statements do not prove a particular payout reached a bank. See [[adyen]] and [[adyen-sales-day-payout]].

## Key takeaways

- **Variable timing and batch grain:** Funds received for one sales day depend on scheme/payment-method settlement timelines and may be paid across several payout batches. The page explicitly says day-total reconciliation is not supported and automated reconciliation is required because one sales day can be spread over several days. Conversely, one payout can contain funds from several sales days.
- **Assignment and payout:** A sale is assigned to a payable batch when the scheme or method sends funds to Adyen; the batch closes according to the account's payout frequency, then Adyen describes payout to the merchant. Its daily-frequency January 1 sales example spanning January 2–7 is illustrative, not a universal delay or guaranteed bank-receipt schedule. The page does not state a fixed cutoff, payout currency, or eligibility rule; retrieve those from the relevant account configuration and linked getting-paid guide.
- **Adjustments and balance:** Refunds, chargebacks and other adjustments are added to the payable batch as they occur. The linked Payable balance is the route for current-batch information. A balance or batch assignment is not a final bank outcome.
- **Holiday qualification:** For a currency, a bank holiday on the capture day, payout day, or between them delays payout under this model. The page says scheme/method settlement timelines can be delayed by one or more days. Apply the actual currency/calendar and account conditions before estimating timing.

## Detail locators

- Lines 15–24: model definition and prohibition on day-total reconciliation.
- `## How it works`, lines 26–30: scheme/method receipt to payable batch, payout frequency and illustrative multi-batch example.
- `### Adjustments`, lines 34–38: refund/chargeback additions and Payable-balance route.
- `## Bank holidays`, lines 40–46: currency-specific capture-to-payout holiday delays.
- `## See also`, lines 48–53: links to payout-account details, sales-day payout, Settlement details and Payable balance; their details are separate evidence.

## Related

- [[adyen-sales-day-payout]] — reciprocal concept covering both merchant-settlement models.
- [[adyen-reporting]] — separate reconciliation/reporting context.
- [[source-adyen-docs-account-getting-paid]] — broader merchant payout frequency and bank-holiday guidance.
- [[source-adyen-docs-account-sales-day-payout]] — contrasting sales-day merchant-settlement model.

## Raw Sources

- [[raw/adyen/docs/account/pass-through-payout/2026-09-15|Pass-through payout, captured 2026-09-15]]
