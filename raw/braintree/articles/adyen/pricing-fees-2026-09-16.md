<!-- Source URL: https://developer.paypal.com/braintree/articles/adyen/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/adyen/pricing-fees/
createTime: '2025-04-02T00:29:48.675Z'
updateTime: '2025-04-02T00:29:48.693Z'
---



# Pricing and Fees


## Transaction fees

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on.


- **Markup**: Percentage deducted from each transaction
- **Commission**: Assessed by Adyen and card brands on certain transactions – can be a percentage or a flat rate, and are most commonly seen on American Express transactions
- **Per transaction fee**: Static dollar amount deducted from each transaction
- **Interchange fees**: Variable fees assessed by the card issuing bank
- **Scheme fees**: Variable fees assessed by the card associations (e.g. Visa and Mastercard)
- **Chargeback fee**: Fixed fee charged by the processing bank that manages the chargeback

Markup, per transaction, interchange, and scheme fees are applied to all successful transactions. Refunds, verifications, voids, and gateway rejections are only charged the per transaction fee.

Fees are calculated and deducted with your payout. If your presentment and settlement currencies differ, the fees will be based on the converted settlement amount.


## American Express

By default, your account is set up to process American Express through Adyen’s aggregated Amex account. Instead of incurring our standard markup rate, American Express transactions are subject to a commission rate, which is determined by Adyen and Amex.

Alternatively, you can apply for your own account directly through Amex. If you choose this option, Amex will manage your funding, descriptors, and chargebacks. You will also need to contact them for any support related to your Amex transactions.


## Pricing model

The standard pricing model for Adyen merchants is our IC++ model. IC++ pricing consists of a markup (or commission, when appropriate) rate, per transaction fee, interchange fees, and scheme fees. Interchange and scheme fees are variable and are not determined by Braintree. Which specific fees are applied to each transaction depends primarily on the provided card type, but can also be influenced by a number of other factors – such as the type of merchant, cost of sale, processing technology, region, and more.


## Reporting


### Settlement Details Report

You can view all fees assessed and deducted from your transactions in the Settlement Details Report, which is generated upon [payout](/braintree/articles/adyen/transactions/settlement-funding-timeline). To find this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Settlement Details Report**, click the**Run Report**button


### Adyen invoice

Adyen will email an invoice around the third week of each month. It’s important to note that the totals listed in this invoice will not match the transaction information in the Settlement Details Report. Instead, the amounts shown on the Adyen invoice reflect all transactions settled between the first and last day of the invoice month – the Settlement Details Report covers transactions that have been paid to your account.


**NOTE**
 Ultimately, the invoice is intended to be a high level snapshot of a given month’s processing, and for that reason, it should not be used for reconciliation.

 


## Refunds and credits

Our standard per transaction fee will be charged for refunds and credits. The transaction fees assessed on the original charge will not be returned for refunded transactions.


## Chargebacks, retrievals, and pre-arbitrations

Regardless of whether you win a [chargeback or pre-arbitration](/braintree/articles/risk-and-security/chargebacks-retrievals/overview), you will be charged a non-refundable fee. This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time.

