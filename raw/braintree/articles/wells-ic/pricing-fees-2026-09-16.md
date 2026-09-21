<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-ic/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: IC+ Pricing and Fees
slug: /articles/wells-ic/pricing-fees/
createTime: '2025-04-01T21:43:15.868Z'
updateTime: '2025-04-01T21:43:15.886Z'
---



# IC+ Pricing and Fees


## Transaction Fees


**NOTE**
 We will not charge any fees for PayPal transactions; only [PayPal's processing fees](https://www.paypal.com/webapps/mpp/merchant-fees) apply.

 

If you’ve received a link to this article, you are on our interchange-plus, or IC+, pricing model. With IC+ pricing, you’ll be charged two sets of fees:


- The interchange fees that come directly from the card associations and issuing banks
- Fees from Braintree

Fees for any given month are assessed on the third business day of the following month. We'll issue two separate debits - one for Braintree fees and another for interchange fees.

Braintree’s processing fee is only applied to **successful sale transactions**. It is not applied to refunds, verifications, declines, gateway rejections, or voids. Interchange fees may be applied to any transaction, however.


### Transaction-level fees

If you would like view fees assessed at the transaction level, you can run a Transaction-Level Fee report. While this report is helpful for identifying trends, Braintree fees, and interchange pricing tiers, this report contains amounts based on estimated interchange rates and should not be used for reconciliation. [Learn more about the Transaction-Level Fee report.](/braintree/articles/control-panel/reporting/transaction-level-fee-report)


### Interchange

Interchange fees encompass all of the various processing fees set by Visa, Mastercard, Amex and Discover. We pass these fees on directly to you, which is why we often refer to them as pass-through fees.

The specific fees that are applied to each transaction depend primarily on card type, along with a number of other factors including the type of merchant, cost of sale, processing technology, region, and more.

The breakdown of each specific fee will be available by the end of the third business day of the following month in the [Pass-Through Fee Report](/braintree/articles/wells-ic/statements-reconciliation#pass-through-fee-details).


### Braintree processing fees

Braintree’s processing fee is composed of two parts: the discount rate, which is the percentage we take from each transaction, and the per transaction fee, which is the static dollar amount deducted from each transaction.

If you use your own [Amex account](/braintree/articles/wells-ic/transactions/accepted-payment-methods#special-note-on-american-express), we will charge a per transaction fee on top of any interchange fees and whatever fees that you pay Amex directly.

We do not display your processing fees in the Control Panel, but you can [download a statement](/braintree/articles/wells-ic/statements-reconciliation#pricing-schedule) to find your specific discount rate and per transaction fee.


#### Rounding down


**NOTE**
 While we round down if there is a remainder value past the penny, this may not apply to interchange fees.

 

When calculating fees, we round down if there is a remainder value past the penny. These are calculated on the transaction level, so if you manually multiply your fees by the **total** settled sales for a given month, there may be a slight discrepancy between the calculated value and the fee details listed on your statement.

As a result of rounding down, we often charge slightly less than your discount rate!


### Refunds and credits

Braintree transaction fees will not be returned for refunded transactions. This means that if you issue a full or partial refund to a buyer, or refund a donation to a donor, we won't charge additional fees to make the refund but the processing fees that you originally paid will not be returned to you.


### Chargebacks, retrievals, and pre-arbitrations

The bank that manages the chargeback or pre-arbitration will charge a non-refundable $15 fee regardless of whether you win the dispute. This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time. [More information on chargebacks.](/braintree/articles/wells-ic/chargebacks-retrievals-prearbs)

