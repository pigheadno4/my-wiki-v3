<!-- Source URL: https://developer.paypal.com/braintree/articles/nab/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/nab/pricing-fees/
createTime: '2025-04-01T23:28:33.991Z'
updateTime: '2025-04-01T23:28:34.012Z'
---



# Pricing and Fees


## Transaction fees

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Depending on your [pricing model](#pricing-models), you may or may not see separate interchange and scheme fees.


- **Merchant service fee**: Percentage we take from each transaction
- **Per transaction fee**: Static monetary amount deducted from each transaction
- **Chargeback fee**: Fixed fee charged by the processing banks that manage the chargeback
- **Interchange and scheme fees**: Variable fees assessed by the card-issuing bank
- **GST**: Goods and Services Tax
- **Multi-currency transaction fee**: Percentage charged per-transaction for any accounts set up for multiple currencies

Braintree’s per transaction fee is applied to **all** authorizations. This includes verifications, failed transactions, and refunds.

Fees are deducted on a monthly basis by our partner bank, NAB, on the last business day of every month. This includes chargeback fees, merchant service and interchange percentages, and per transaction fees.


## Multi-currency fees

Outside of the multi-currency transaction fee, there are no additional fees for accepting currencies other than AUD. The 8 major currencies will settle in a like-for-like format (e.g. a transaction presented in USD will settle in USD, and not be converted to AUD prior to settlement). The major currencies are:


- USD
- CAD
- EUR
- HKD
- JPY
- NZD
- SGD
- GBP

When funds that have been deposited in your account as one of the 8 major currencies are withdrawn/transferred, the amount will be converted to AUD, and a $20 AUD fee will be charged by NAB for that day's disbursement.

All other currencies are considered minor currencies, and will automatically convert to AUD prior to settlement at a daily conversion rate determined by Visa/Mastercard.


## Pricing models

Your pricing model was determined when you originally signed up for an account. [Contact us](/braintree/help/feeHelp) if you have questions about which pricing model applies to your account.


### Blended

Blended pricing offers fixed rates, which makes it easier to accurately forecast your payment processing costs. The blended model consists of a merchant service fee and per transaction fee.

Depending on your account setup, your rates may vary based on the type of payment method used and the currency the transaction is presented in.

When processing a refund on the blended pricing model, you will be charged an additional per transaction fee, but you will be refunded the merchant service fee that was assessed at the time of the original transaction.


### Interchange plus (IC+)

IC+ pricing consists of a merchant service fee, a per transaction fee, and interchange and scheme fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. The specific fees applied to each transaction depend primarily on card type, but include a number of other factors such as the type of merchant, cost of sale, processing technology, region, and more.

When processing a refund, you will be charged an additional per transaction fee, but you will be refunded the merchant service fee and interchange fees that were assessed at the time of the original transaction.


## Funding fees

When funds are transferred/withdrawn from transactions charged in any of the [8 major currencies](#multi-currency-fees), NAB will automatically convert funds from those transactions to AUD and charge a $20 AUD fee per transfer/withdrawal. This is not a Braintree-related or -controlled fee.


## Reporting

You can access your [Settlement Batch Summary](/braintree/articles/control-panel/reporting/settlement-batch-summary), [Transaction Summary](/braintree/articles/control-panel/reporting/transaction-summary), and [NAB Merchant Statement](/braintree/articles/nab/statements-reconciliation#statements) in the Control Panel.


## Chargebacks and pre-arbitrations

A flat rate chargeback fee – which was determined when you signed your pricing agreement – is assessed for both chargebacks and pre-arbitrations. Chargeback fees are only applied if you lose or accept the dispute or allow it to expire. Chargeback fees are debited as applicable throughout the month alongside Braintree's monthly processing fees, and will be clearly displayed as a separate debit from any other fees or refunds.

