---
title: "Adyen Getting paid"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/getting-paid"
raw_files:
  - "adyen/docs/account/getting-paid/2026-09-15.md"
tags: [adyen, merchant-settlement, payouts, payable-batch]
---

## Overview

This Adyen account guide describes how funds from transactions Adyen processes for a merchant are assigned to payable batches and sent to the merchant's payout account **separately for each merchant account**. It concerns merchant settlement, routed through [[adyen-sales-day-payout]]; [[adyen-payouts]] covers the distinct legacy Payout API for paying other recipients. The guide was last modified in 2020 and captured in 2026; it does not establish current account eligibility or an individual bank receipt. See [[adyen]].

## Key takeaways

- The selected payout model assigns processed transactions to a payable batch. The **Payable balance** is described as the most up-to-date view of the current batch. The batch closes according to payout frequency; **if its balance is positive at close, Adyen instructs payout**. The instruction is a separate event from funds arriving at the bank.
- Both models pay on a **net** basis: sales for the period less transaction costs, refunds, chargebacks and other adjustments such as balance transfers. **Sales day payout**, described as the default, groups a whole sales day into one batch regardless of whether the scheme or payment method has transferred funds to Adyen. **Pass-through payout** can spread a sales day over several batches as those funds arrive. The captured guide says pass-through is the only available model in Africa, Brazil and Turkey; verify current regional configuration before applying it.
- Payout currency depends on the acquiring connection's country, and like-for-like settlement is offered only when that currency is also a supported settlement currency for the payment method. Frequency is configured per merchant account. The guide says bank arrival **may take up to two days depending on currencies and banks**, while currency-specific bank holidays can stop payout processing or Adyen's receipt of funds and shift timing. This is guidance, not a guaranteed arrival time.
- At batch close, Adyen creates a **Settlement details report** about credited/debited transactions and associated costs. Customer Area payout viewing requires one of the listed viewing roles; changing model or frequency requires **Change payout schedule** or **Merchant admin**. Changing the payout destination account follows a separate bank-account-details route.

## Detail locators

- Merchant-account separation, payable-batch close and net calculation: pinned raw lines 19–27.
- Currency and like-for-like qualification: pinned raw lines 29–33.
- Sales-day versus pass-through models and regional exception: pinned raw lines 35–43.
- Frequency, bank arrival and holiday effects: pinned raw lines 45–61.
- Net deductions, Settlement details report and payout-view roles/steps: pinned raw lines 63–99.
- Model/frequency change roles and Customer Area steps: pinned raw lines 101–123.

## Related

- [[adyen-sales-day-payout]] — merchant settlement and payable-batch concept.
- [[adyen-payouts]] — separate recipient disbursement API concept.
- [[adyen-reporting]] — report-level evidence boundary.

## Raw Sources

- [[raw/adyen/docs/account/getting-paid/2026-09-15|Adyen Getting paid, captured 2026-09-15]]
