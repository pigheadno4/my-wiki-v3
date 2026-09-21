<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/wells-flat/pricing-fees/
createTime: '2025-04-01T23:41:03.510Z'
updateTime: '2025-04-01T23:41:03.531Z'
---



# Pricing and Fees


## Transaction fees


**NOTE**
 Braintree will not charge any fees for PayPal transactions; only [PayPal's processing fees](https://www.paypal.com/webapps/mpp/merchant-fees) apply.

 

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Fees can be broken down into the following categories:


- **Discount rate**: Percentage we take from each transaction
- **Per transaction fee**: Static dollar amount deducted from each transaction
- **Braintree processing fees**: Discount rate and per transaction fees, combined
- **Chargeback fee**: Fixed fee charged by the processing bank that manages the chargeback
- **Cross border fee**: Percentage we take from each transaction on cards issued outside the US

Braintree’s processing and cross border fees are only applied to **successful transactions** and are deducted from your daily disbursements. Verifications, declines, gateway rejections, and voids will not incur fees.

If you use your own [American Express account](/braintree/articles/wells-flat/transactions/accepted-payment-methods#special-note-on-american-express), we will charge a per transaction fee on top of whatever fees that you pay Amex directly.


### Braintree processing fee rates

We do not display your processing fees in the Control Panel, but you can find your processing fee rates in the **Pricing Schedule** on your statements. To access your statements:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the top navigation
- Click the**Statements**tab
- Click the**View Statement**button located to the right of**Merchant Statements**
- Open any statement for the merchant account you'd like to view your processing fee rates for by clicking the**PDF**link

Within the **Pricing Schedule** section of your statement, you'll find your fee rates for **discount**, **cross border**, **per-transaction**, and **chargeback** fees.


### Transaction-level fees

If you would like to view the Braintree fees assessed at the transaction level, you can run a [Transaction-Level Fee report](/braintree/articles/control-panel/reporting/transaction-level-fee-report). This report is also helpful for [reconciliation](/braintree/articles/wells-flat/statements-reconciliation#reconciliation).


## Standard rounding

When calculating percentage-based fees, we round to the nearest unit if there is a remainder. This means that we round fees up or down based on the 3rd decimal digit. Rounding is done at the transaction level, so if you manually multiply your fees by the total settled sales for a given month, there may be a slight discrepancy between the calculated value and the fee details listed on your statement.

If the third decimal of a calculated fee is between 0 and 4, rounding down will be applied. Conversely, if the third decimal is between 5 to 9, rounding up will be applied. The table below demonstrates examples of how we use standard rounding for the fee calculations.

| Calculated Fee | Fee After Rounding |
| --- | --- |
| $1.158 | $1.16 |
| $1.143 | $1.14 |


## Refunds

Braintree transaction fees will not be returned for refunded transactions. This means that if you issue a full or partial refund to a buyer, or refund a donation to a donor, we won't charge additional fees to make the refund but the processing fees that you originally paid will not be returned to you.


## Chargebacks, retrievals, and pre-arbitrations

The bank that manages the chargeback or pre-arbitration will charge a non-refundable $15 fee regardless of whether you win the dispute. This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time. [More information on chargebacks.](/braintree/articles/wells-flat/chargebacks-retrievals-prearbs)

