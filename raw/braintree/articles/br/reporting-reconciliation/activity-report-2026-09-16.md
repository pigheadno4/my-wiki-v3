<!-- Source URL: https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/activity-report -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Activity Report
slug: /articles/br/reporting-reconciliation/activity-report/
createTime: '2025-04-02T00:27:55.661Z'
updateTime: '2025-04-02T00:27:55.695Z'
---



# Activity Report


## Document Version 1.1

[Changelog](#changelog)


## Report Definition

The Activity Report is a daily report that contains all transactions that were Submitted for Settlement or Settlement Declined from the previous processing day. The purpose of this report is to provide projected disbursement dates and total transaction fees for all transactions to aid in forecasting receivables from PayPal. By saving the projected disbursement dates for all transactions in your system of record, you will be able to more easily track transactions that will be disbursed in the future. For merchants who offer installments, this report will also capture any adjustments to future installment disbursement that may occur due to credit card disputes or refunds.

For merchants who process credit cards (with or without installments), this report will contain the Projected Disbursement Date for the following type of transactions:


- Credit card sale and refund transactions
- Debit card sale and refund transactions
- Newly created installment transactions
- Adjustments to installments


## Obtaining projected disbursement dates

In Brazil, card-based transactions can take anywhere from 2 to 30 days to be disbursed depending on the card type. The default disbursement is 30 days, however a feature called Predefined Funds Anticipation allows merchants to pay a premium to accelerate the funding of credit card based transactions. For more information about this feature [visit this page](/braintree/articles/br/reporting-reconciliation/transaction-level-fee-report#funds-anticipation).

| Card Type | Disbursement Date |
| --- | --- |
| Credit Cards | 30 days |
| Debit Cards | 2 days |

Whether you opt to pay for Predefined Funds Anticipation or not, it will be important to obtain and store the projected disbursement dates for all transactions and installments in your system of record so that you can track your receivables and forecast future disbursements.


### Standard sale and refund transactions

To obtain the projected disbursement date for a standard sale or refund transaction, follow the below steps:


- Filter the report onRecord Type=**Sale**or**Refund**
- Use the values in found in theRecord IDcolumn to match the IDs of transaction sales and refunds in your system of records
- Save the value found in theProjected Disbursement Datacolumn along with the transaction in your system


### Sale transactions with installments

When a sale transaction is created and submitted for settlement with installments, the transaction response object will contain the following data for each installment:


- Installment ID
- Installment Amount

When the installments are initially created, the Projected Disbursement Date will be NULL and will be populated within twelve hours.

Installment records should be stored separately from standard sale transactions in your system of record because they will be paid out over time, so tracking them individually will be required in order to reconcile PayPal’s data with your system of record, and with your deposit bank account.


#### Steps to locate installment projected disbursement dates


- Select all records whereRecord Type=InstallmentandRecord Subtypeis empty.
- Once the installment records are filtered to just those that represent newly created installments, iterate through the set using the**Record ID**column to identify the installment ID for which the record pertains to.
- Locate the**Projected Disbursement Date**field, add this date to your system of record, and save it with the installment record.


## Installment adjustments

The amount of an installment can be affected by two types of payment events:


- Full and partial refunds
- Full and partial disputes

Whenever a transaction with installments is refunded or has a dispute that has Lost associated with it, every installment will have its amount adjusted equally.

Additionally, adjustments can occur on both installments previously disbursed as well as installments that are to be disbursed in the future.

In the case an adjustment is made to an installment that has previously been disbursed, the adjustment amount will be netted out of the next disbursement, so it’s important to track the installment adjustments as they are created so that you can reconcile the installment disbursements with both your deposit account and your system of record.


#### Types of installment adjustments


##### Refunds

In the case of refunds, each installment will be reduced by the amount of the refund divided by the number of installments.


##### Disputes

Dispute adjustments are typically negative adjustments and will reduce installment amounts. In some cases, disputes can be reversed, resulting in a positive adjustment.


#### Steps to locate information in the Activity Report

In order to maintain your system of records for installments, you will need to save installment adjustment records separately.


- To isolate the installment adjustment records, select all records withRecord Type=InstallmentandRecord Subtype=Adjustmentfrom the Daily Activity Report
- Iterate through the installment adjustment records, using theRecord IDfield to identify the installment ID and save the following fields:
- Settlement Amount– This will be used to obtain the amount of the adjustment. Add this value to the installment amount in your system of record to obtain the new amount for the installment.
- Installment Disbursed
- If**TRUE**then the installment’s adjustment amount will be netted from a future disbursement whose date can be obtained from theProjected Disbursement Datefield. Installment adjustments for previously disbursed installments should be tracked as separate objects in your system of record because they will have their own money movement event, and will need to be reconciled using the Disbursement Report.
- If**FALSE**then only future disbursed installments will be affected. In this case, the installment adjustment will have the same projected disbursement date as the installment.


- Projected Disbursement Date– This is the date the adjustment amount will be netted from a future disbursement
- Reason– This is the reason for the adjustment. The reason will either be a**refund**or**dispute**.
- Adjuster ID– This is the ID of the object in your system that caused the installments to be adjusted.
- WhenReason=**refund**theAdjuster IDwill be the ID of the refund in your system.
- WhenReason=**dispute**theAdjuster IDwill be the ID of the dispute in your system.






## Data dictionary of Activity Report

| Field Name | Description |
| --- | --- |
| Merchant Account ID | The Merchant Account ID that was used to process the transaction |
| Record Type | The type of object in the Braintree gateway. Either: - Sale - Refund - Installment |
| Record Subtype | The subtype of the object in the Braintree gateway: - Adjustment (this is populated for installment objects where the row is describing an adjustment to an existing installment) |
| Record ID | The ID of the object in the Braintree gateway. - For Sale and Refund record types, the ID will be theTransaction IDfor the sale or credit transaction. - For Installment record types, the ID will be theInstallment ID |
| Status | The status of the transaction |
| Presentment Currency | The presentment currency of the transaction |
| Presentment Amount | The amount in presentment currency |
| Tax Amount | The amount passed by the merchant in theTax Amountfield of the API |
| Settlement Currency | The currency used to settle the transaction |
| Settlement Amount | The amount of the Braintree object. - For Sale and Refund records, theSettlement Amountwill be the amount of the transaction. - For Installment records (non-adjustments), this will be the initial amount of the installment - For Installment records where theRecord SubtypeisAdjustment, theSettlement Amountwill be theAdjustment Amount. |
| Effective Date | The date scope of the report. - For Sale and Refund record types, this will be theSubmitted for Settlementdate - For Installment record types (non-adjustment) this will be the date the installment was created. - For Installment record types with theRecord SubtypeofAdjustment,the date will be the creation date of the installment adjustment. |
| Order ID | The merchant populated order ID value |
| Purchase Order Number | A Level 2 data field that can be used to store a purchase order identification value. |
| Payment Instrument Type | The payment instrument that was used to create the transaction |
| Payment Instrument Subtype | The subtype of the payment instrument where applicable. For credit cards, this will be the brand of the credit card that was used to create the installment transaction. |
| Card Type | The type of credit card used, either: - Credit - Debit - Unknown |
| Customer ID | The ID of the customer in the Braintree gateway |
| Installment Disbursed | A Boolean that indicates whether the installment that's being adjusted has been disbursed previously |
| Projected Disbursement Date | The projected disbursement date of the installment adjustment. Only populated for installment adjustments where installments that have previously been disbursed. |
| Number of Installments | The total number of installments in the installment plan. |
| Installment Number | The sequence number of the installment |
| Reason | The reason the adjustment occurred, either: - Refund - Dispute |
| Adjuster ID | The ID of the adjusting object. - WhenReasonisRefundthe adjuster ID will be the refund ID. - WhenReasonisDisputethe adjuster ID will be the dispute ID. |
| Total Fee Amount | The total fee that will be assessed on the transaction upon disbursement |


## Record types and subtypes

| Record Type | Record Subtype |
| --- | --- |
| Sale​ | Installment​​ (null) |
| Refund​ | Referenced ​ Non-referenced​ |
| Installment​ | Adjustment (null) |


## Payment instrument types and subtypes

| Payment Instrument | Payment Instrument Subtype |
| --- | --- |
| Credit Card​ | Visa Mastercard​ American Express Discover Hipercard Elo Union Pay |
| Debit Card​ | Visa Mastercard​ American Express Discover Hipercard Elo Union Pay |
| PayPal​ | PayPal Wallet​ PayPal Credit |
| Venmo | Venmo Wallet​ |
| Apple Pay​ | Visa Mastercard​ American Express Discover |
| Google Pay | Visa Mastercard​ American Express Discover |
| Samsung Pay | Visa Mastercard​ American Express Discover |
| Bank Account | US Personal Account US Business Account Others |
| Local Payment Methods | OXXO iDeal Bancontact Sofort eps Grabpay MyBank giropay Przelewy24 Verkkopankki Blik |
| Others | Partner Tax |


## Changelog

| Document Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 02-18-2021 | Initial Version |
| 1.1 | 04-27-2021 | Added "Total Fee Amount" Column |

