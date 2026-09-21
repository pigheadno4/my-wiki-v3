<!-- Source URL: https://developer.paypal.com/braintree/articles/chase/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/chase/pricing-fees/
createTime: '2025-04-02T00:11:52.290Z'
updateTime: '2025-04-02T00:11:52.304Z'
---



# Pricing and Fees


## Transaction fees

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Depending on your [pricing model](#pricing-models), interchange fees might not apply.


- **Discount rate**: Percentage we take from each transaction
- **Per transaction fee**: Static dollar amount deducted from each transaction
- **Paymentech processing fees**: Discount rate and per transaction fees, combined
- **Interchange fees**: Variable fees assessed by the card issuing bank
- **Chargeback fee**: Fixed fee charged by the processing bank that manages the chargeback

All fees are deducted from your daily disbursements, and are only applied to **successful sale transactions**. Fees are not applied to refunds, verifications, declines, gateway rejections, or voids. Your Paymentech processing fees will also be included in reporting via [Chase Paymentech Online](https://www.chasepaymentech.com/merchant_log_in.html).


**IMPORTANT**
 If you use your own American Express account, you will not be charged for that transaction at our discount rate. You will be charged Braintree’s per transaction fee on top of both interchange fees and any fees charged by Amex directly.

 


## Pricing models

Your pricing model was determined when you originally signed up for an account. [Contact us](/braintree/help/feeHelp) if you have questions about which pricing model applies to your account.


### Blended

Blended pricing offers fixed rates, which makes it easier to accurately forecast your payment processing costs. The blended model is composed of our Braintree processing fees. Depending on your account setup, you may have different rates for debit cards and credit cards.


### IC+

IC+ pricing consists of the Braintree processing fees and interchange fees. Because interchange fees are variable and are not set by Braintree, it can be harder to predict the exact amount you’ll be charged. The specific fees that are applied to each transaction depend primarily on card type, but include a number of other factors such as the type of merchant, cost of sale, processing technology, region, and more.


### Reporting

Chase manages all of your reporting directly. They offer 125+ customizable reports via Paymentech Online. Find more information about Chase reporting in our [Chase Reporting and Reconciliation article](/braintree/articles/chase/reporting-reconciliation).


## Chargebacks, retrievals, and pre-arbitrations

Regardless of whether you win a [chargeback or pre-arbitration](/braintree/articles/risk-and-security/chargebacks-retrievals/overview), you will be charged a $15 non-refundable chargeback fee. This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time.

