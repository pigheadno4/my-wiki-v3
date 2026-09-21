<!-- Source URL: https://developer.paypal.com/braintree/articles/moneris/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/moneris/pricing-fees/
createTime: '2025-04-02T01:31:28.037Z'
updateTime: '2025-04-02T01:31:28.051Z'
---



# Pricing and Fees


## Transaction fees

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Fees can be broken down into the following categories:


- **Per transaction fee**: Static dollar amount deducted from each transaction
- **Discount rate**: The percentage we take from each transaction
- **Braintree processing fees**: Discount rate and per transaction fees, combined
- **Interchange fees**: Variable fees assessed by the card issuing bank
- **Chargeback fee**: Fixed fee charged by the processing banks that manage the chargeback

Depending on your [pricing model](#pricing-models), interchange fees may be charged separately or included in your Braintree processing fees.

Braintree’s discount rate is only applied to successful transactions and is deducted from your daily disbursements. The per transaction fee will be applied to **all** transactions, including refunds, authorizations (excluding $0 auths), voids, and gateway rejections.


## Pricing models

Your pricing model was determined when you originally signed up for an account. [Contact us](/braintree/help/feeHelp) if you have questions about which pricing model applies to your account.


### Blended

Blended pricing offers fixed rates, which makes it easier to accurately forecast your payment processing costs. The blended model is composed of the discount rate and per transaction fee.


### Interchange plus (IC+)

IC+ pricing is composed of the Braintree processing fees and interchange fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. The specific fees that are applied to each transaction depend primarily on card brand, but include a number of other factors such as card type, region, and more.


## Refunds and voids

Braintree's per transaction fee is applied to all refunds, and the original transaction fees will not be returned on refunded transactions.

Issuing a void will also incur our per transaction fee, but the fees associated with voids will be returned to you at the beginning of the following month. You’ll want to keep this in mind when [reconciling your transactions](/braintree/articles/moneris/reconciliation#refunds-and-voids).


## Chargebacks, retrievals, and pre-arbitrations

Regardless of whether you win a [chargeback or pre-arbitration](/braintree/articles/risk-and-security/chargebacks-retrievals/overview), you will be charged a non-refundable chargeback fee. This fee only applies to chargebacks and pre-arbs; retrievals do not incur a fee at this time.


## Reporting

Moneris will mail your statements to the business address on file 3 to 5 business days after the beginning of each month. If you have not processed any transactions, you will not be issued a statement.

For more details on your transaction processing, you can access your [Settlement Batch Summary](/braintree/articles/control-panel/reporting/settlement-batch-summary) and [Transaction Summary](/braintree/articles/control-panel/reporting/transaction-summary) in the Braintree Control Panel at any time.

