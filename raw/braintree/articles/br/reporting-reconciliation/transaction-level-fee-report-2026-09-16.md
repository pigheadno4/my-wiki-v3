<!-- Source URL: https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/transaction-level-fee-report -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Brazil Transaction-Level Fee Report
slug: /articles/br/reporting-reconciliation/transaction-level-fee-report/
createTime: '2025-04-01T22:18:34.212Z'
updateTime: '2025-04-01T22:18:34.234Z'
---



# Brazil Transaction-Level Fee Report


## Document Version 1.0

[Changelog](#changelog)


## Report Definition

The Transaction-Level Fee report provides detailed information about your transactions and the fees associated with them. The details provided in the report depend on whether you have an IC+ pricing model, or a flat rate or blended model. Contact us if you're unsure of your pricing model. Payment methods supported by the Transaction-Level Fee report:


- Credit and Debit Cards
- Venmo Accounts
- Apple Pay
- Google Pay

In Brazil, the report will also contain:


- [Installments](#installments)
- [Funds Anticipation Fees](#funds-anticipation)

For more information about running this report, [visit our Transaction-Level Fee report page](/braintree/articles/control-panel/reporting/transaction-level-fee-report).


### Installments

In Brazil, merchants can offer customers the ability to pay for transactions in installments. This is supported for Visa and Mastercard credit cards, and PayPal Wallet transactions. [Learn more about the installments capability](/braintree/articles/br/payment-capabilities).

Installments will be assessed fees individually for the below fee types:


- Discount Fees
- Pre-defined Funds Anticipation Fees


#### Reconciling Fees for Installment Disbursements

To reconcile the fees for installments that have been disbursed to your bank account, follow the below steps:


- Locate records whereRecord Type=**Installment**andRecord Subtype=**Disbursements**.
- With the installment disbursement records selected, iterate through the installments using theTransaction IDfield to locate the ID of the installment.
- For each installment record, you will use the following columns to gain insight into the fees netted from the disbursed installment:
- Discount– The rate of the charged charged by PayPal for the installment
- Per Transaction Fee– The fee charged for each transaction for the installment
- Funds Anticipation Rate– If Pre-defined Funds Anticipation was used to accelerate the funding of the installment, the Funds Anticipation fee rate will be populated in this column.
- Braintree Total Amount– This is the total discount fee, which equals: (DiscountXSettlement Amount)+Per Transaction Fee
- Total Fee Amount– This will be the total fee amount that was charged for the installment. It will be theBraintree Total Amount+ (Funds Anticipation RateXSettlement Amount)




#### Reconciling Fees for Installment Adjustments

When a transaction with installments is refunded, the discount fees for each installment may also be refunded. This is dependent on your pricing agreement with PayPal. Only fully refunded transactions with installments will have refunded fees associated with it.

If a transaction with installments is refunded, the refund amount is equally divided over the number of installments. The refunds are shown in reporting as: Record Type = **Installment** and Record Subtype = **Adjustment**.

Follow the below methodology to reconcile fees associated with installment adjustments caused by refunds:


- Locate records whereRecord Type=**Installment**andRecord Subtype=**Adjustment**.
- With the installment disbursement records selected, iterate through the installments using theTransaction IDfield to locate the ID of the installment.
- For each installment record, you will use the following columns to gain insight into the fee credits associated with the installment adjustment:
- Discount Credit– The rate of the PayPal fee charged for the installment
- Per Transaction Fee Credit– The portion of the per transaction fee charged to the installment
- Funds Anticipation Rate Credit– If pre or post defined fund anticipation was used to accelerate the funding of the installment, the Funds Anticipation fee rate will be populated here.
- Braintree Total Amount– This is the total discount fee, which equals: (Discount CreditXOriginal Sale Amount)+Per Transaction Fee Credit
- Total Fee Amount– This will be the total fee amount that was charged for the installment. It will be:Discount Fee+Per Transaction Fee+Funds Anticipation Fee(which equals:Original Sale AmountXFunds Anticipation Fee Credit)



For both installment disbursement and adjustments that appear in the Transaction Level Fee Report, the Total Fee Amount for the installment should be equal to the Net Settlement Fees for the same line item in the [Disbursement Report](/braintree/articles/br/reporting-reconciliation/disbursement-report).


### Funds Anticipation

In Brazil, credit card transactions take 30 days to disburse by default. Merchants can opt to pay a certain rate-based fee to have their credit card transactions paid out sooner than 30 days. This feature is called Funds Anticipation.

Braintree and PayPal support **Pre-defined Funds Anticipation** that allows merchants to have all credit card transactions be paid out earlier than 30 days at an agreed upon schedule and Funds Anticipation rate (e.g. all credit card transactions will be paid out in 15 days as opposed to 30, and each transaction will be assessed an additional rate-based Fund Anticipation fee).

These fees will apply to standard credit card transactions and transactions with installments.

To see the rate applied to a sale or refund, with or without installments, look to the Funds Anticipation Rate and Funds Anticipation Rate Credit column to obtain the rate assessed to the transaction. Multiply the transaction or installment amount to obtain the fee that will be assessed for Funds Anticipation.


## Record types and subtypes

| Record Type | Record Subtype |
| --- | --- |
| Sale​ | Installment​​ (null) |
| Refund​ | Referenced ​ Non-referenced​ |
| Installment​ | Adjustment (null) |


## Payment instrument types and subtypes

| Payment Instrument | Payment Instrument Subtype |
| --- | --- |
| Credit card​ | Visa Mastercard​ American Express Discover Hipercard ELO Union Pay |
| Venmo | Venmo Wallet​ |
| Apple Pay​ | Visa Mastercard​ American Express Discover |
| Google Pay | Visa Mastercard​ American Express Discover |
| Samsung Pay | Visa Mastercard​ American Express Discover |
| Bank Account | US Personal Account US Business Account Others |


## Changelog

| Document Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 02-18-2021 | Initial Version |

