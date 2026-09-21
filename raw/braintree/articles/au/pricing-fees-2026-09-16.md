<!-- Source URL: https://developer.paypal.com/braintree/articles/au/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/au/pricing-fees/
createTime: '2025-04-01T22:41:00.249Z'
updateTime: '2025-04-01T22:41:00.269Z'
---



# Pricing and Fees

Your account setup will determine both your pricing and the types of fees you face when processing transactions through Braintree. If you have any questions about your setup, [Contact us](/braintree/help/feeHelp) for assistance.


## Fees

There are two different types of fees that you may see: transaction fees and billable event fees.


### Transaction fees

Transaction fees are applied to individual settled transactions and will vary based on your pricing model. These fees can be broken down into the following categories:


- **Per transaction fee**: Fixed fee amount deducted from each authorization
- **Cross border fee**: Percentage we take from each transaction made using a card that was issued outside of the country where your business is located
- **Kount fee**: Fixed fee charged for each Kount inquiry
- **Chargeback fee**: Fixed fee charged by the processing bank that is managing the chargeback
- **Interchange fees**: Variable fees assessed by the card issuing bank
- **Merchant service fee**: Percentage we take from each settled transaction
- **Braintree processing fee**: Merchant service fee and per transaction fee, combined
- **Pass-through fees**: Processing fees set by Visa, Mastercard, Amex, and Discover that we pass on directly to you

The per transaction fee is applied to **all** authorizations. This includes verifications, failed transactions, voids, and refunds. If you use your own [American Express account](/braintree/articles/au/transactions/accepted-payment-methods#american-express), we will charge a per transaction fee on top of the fees that you pay Amex directly.


### Billable event fees

Billable event fees are the individual fees applied to every decline, refund, two-step authorization, and card verification. Unlike transaction fees, multiple billable event fees can be applied to the same transaction. [Learn more.](/braintree/articles/au/statements#billable-event-fees)


## Pricing models

Your pricing model was determined when you originally signed up for an account. [Contact us](/braintree/help/feeHelp) if you have questions about which pricing model applies to your account.


### IC+

IC+ pricing consists of the Braintree processing fees and interchange fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. The specific fees applied to each transaction vary primarily by card brand, but can also be affected by a number of other factors such as card type, region, and more.

Fees are deducted on a monthly basis on the last business day of every month.


### IC++

IC++ pricing consists of the Braintree processing fees, interchange fees, scheme fees, and pass-through fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. Similar to interchange fees, scheme fees are variable and are not determined by Braintree. The specific fees applied to each transaction vary primarily by card type, but can also be affected by a number of other factors such as your type of business, cost of sale, processing technology, region, and more.

Fees are deducted on a monthly basis on the last business day of every month.


## Chargebacks, retrievals, and pre-arbitrations

A flat rate chargeback fee – which was determined when you signed your pricing agreement – is assessed for both chargebacks and pre-arbitrations; retrievals do not result in a fee at this time. [Learn more about chargebacks.](/braintree/articles/au/chargebacks-retrievals-prearbs)

