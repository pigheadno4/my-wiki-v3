<!-- Source URL: https://developer.paypal.com/braintree/articles/apac/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/apac/pricing-fees/
createTime: '2025-04-01T23:20:34.884Z'
updateTime: '2025-04-01T23:20:34.899Z'
---



# Pricing and Fees


## Transaction fees

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Depending on your [pricing model](#pricing-models), interchange and scheme fees may be bundled into your rates, so it’s possible you will not see them listed in your reports.


- **Ad valorem**: Percentage we take from each transaction
- **Per transaction fee**: Static monetary amount deducted from each transaction
- **Chargeback fee**: Fixed fee charged by the processing banks that manage the chargeback
- **Interchange fees**: Variable fees assessed by the card issuing bank
- **Scheme fees**: Variable fees assessed by the card associations (e.g. Visa and Mastercard)

All fees are deducted from your disbursements prior to being deposited in your bank account. Braintree’s per transaction fee is applied to **all** authorizations (approved and declined), verifications, voids, and gateway rejections. The ad valorem percentage rate applies to settled transactions. Refunds do not incur any fees.


## Pricing models

Your pricing model was determined when you originally signed up for an account. [Contact us](/braintree/help/feeHelp) if you have questions about which pricing model applies to your account.


### Blended

Blended pricing offers fixed rates, which makes it easier to accurately forecast your payment processing costs. The blended model consists of an ad valorem percentage rate and per transaction fee.

Depending on your account setup, your rates may vary based on the type of payment method used and the currency the transaction is presented in.


### IC++

IC++ pricing consists of an ad valorem percentage rate, per transaction fee, interchange fees, and scheme fees. Scheme and interchange fee rates are not managed by Braintree — they are variable and determined by Visa/Mastercard and issuing banks. The specific fees applied to each transaction depend primarily on card type, but they include a number of other factors such as the type of merchant, currency presented, cost of sale, processing technology, region, and more.


**IMPORTANT**
 Multi-currency transactions on the IC++ model will incur an additional 1% fee for conversion.

 


## Reporting

Once you begin processing, we’ll generate an APAC Transaction Detail Report each day transactions are settled. This report is usually generated about 3 business days after the transaction date and includes the following details:


- All transactions settled in each batch
- The fees associated with each transaction
- All chargebacks, including case numbers and chargeback amounts

See our [Statements and Reconciliation article](/braintree/articles/apac/statements-reconciliation#reconciliation) for more information on this report.


## Refunds and credits

No fees are incurred when processing refunds and credits. Voids, however, will incur a separate per transaction fee.

In the case of a full refund, all but the per transaction fee will be credited back to you. [Contact us](/braintree/help/feeHelp) if you are unsure of your per transaction fee rate.


## Chargebacks, retrievals, and pre-arbitrations

Regardless of whether you win a [chargeback or pre-arbitration](/braintree/articles/apac/chargebacks-retrievals-prearbs), you will be charged a nonrefundable flat fee, which is determined by your settlement currency.


- 30 SGD
- 160 HKD
- 90 MYR

This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time.

