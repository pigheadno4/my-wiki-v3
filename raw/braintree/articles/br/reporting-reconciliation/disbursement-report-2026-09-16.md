<!-- Source URL: https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/disbursement-report -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Disbursement Report
slug: /articles/br/reporting-reconciliation/disbursement-report/
createTime: '2025-04-01T23:14:27.264Z'
updateTime: '2025-04-01T23:14:27.303Z'
---



# Disbursement Report


## Document Version 1.1

[Changelog](#changelog)


## Report Definition

To reconcile your daily deposits from PayPal and Braintree with your system of records to clear your receivables, you will need to use the Disbursement Report. This report will contain both summarized and event-level detail of every payment event that impacted a deposit from PayPal and Braintree to your deposit bank account.


## Report format

The Disbursement Report contains 4 sections:


- Header
- Summary
- Detail
- Footer


### Header

The **Header** section will contain report configuration and status information. This is where you will find information like the timezone of the data in the report, or report name.


### Summary

The **Summary** section will contain summarized data about the disbursement batches from the reporting period. Each disbursement batch will appear as a line-item in this section and will have information like the total amount disbursed per merchant account, the transfer ID of the disbursement, and the bank account to which the funds were disbursed.


### Detail

The **Detail** section will contain line-item detail for all the disbursement impacting events (e.g. transactions, disputes, etc.).


### Footer

This section will provide data that can be used to verify that the number of records ingested into your system matches the number of records in the file. It will also include the total number of files generated for the day and the sequence number of the files within that set.


## How to Use the Report


### Reconciling deposit amount to funding account in PayPal

Below are the steps to reconcile the line-item deposit records from PayPal on your bank statement with the Disbursement Report:


- Match each deposit amount from PayPal on your bank statement with the amounts found in theNet Disbursed Amountcolumns of the**Summary**section of the Disbursement Report
- Locate theFunding Accountfor each deposit line-item in the**Summary**section. For Brazil, this value will always be a PayPal Account Number because both PayPal Wallet and Credit/Debit Card transactions are disbursed through a PayPal account.
- Use the values found in theFunding Accountcolumn of the**Summary**section for each line-item deposit to identify the rows in the**Detail**section that belong to each deposit.
- Sum the values found inNet Disbursedcolumn for each group of rows filtered byFunding Account.The sum for each group will match the amounts found in the**Summary**sections

Once you have confirmed that all the disbursement impacting items (e.g. transactions, disputes, etc) are present in the report, you can begin reconciling the items by Record Type as outlined in the following sections.


### Reconciling standard sales and refunds

To reconcile standard sales and refunds records that have been disbursed to your bank account, follow the below methodology:


- Locate records whereRecord Typeis eitherSaleorRefund.
- With theSaleandRefundrecords selected, iterate through the set using theRecord IDfield to locate theTransaction ID, and ingest the following data at a minimum:
- Disbursement Date– The date the installment was disbursed
- Transfer ID– The unique ID include in the descriptor on the bank transfer. Summing all theNet Disburseditems in the disbursement report byTransfer IDwill equal the deposit amount in your bank account.
- Net Disbursed– The amount of the installment net fees, in disbursement currency, that was included in the deposit.




### Reconciling installments

To reconcile the installments that have been disbursed to your bank account, follow the below methodology:


- Locate records whereRecord Type=**installments**andRecord Subtype=**disbursements**.
- With the installment disbursement records selected, iterate through the installments using theRecord IDfield to locate theInstallment ID, and ingest the following data at a minimum:
- Disbursement Date– The date the installment was disbursed
- Transfer ID– The unique ID include in the descriptor on the bank transfer. Summing all theNet Disburseditems in the disbursement report byTransfer IDwill equal the deposit amount in your bank account.
- Net Disbursed– The amount of installment net fees, in disbursement currency, that was included in the deposit.


- Locate records whereRecord Type=**Installments**andRecord Subtype=**Adjustments**, and repeat step 2, but for the adjustment records in your system of record.


### Reconciling disputes

To reconcile disputes that have impacted your disbursement, follow the below methodology:


- Locate records whereRecord Type=**Dispute**.
- With the dispute records selected, iterate through disputes using theDispute IDcolumn to identify the dispute.
- Match the value in theNet Disbursedcolumn with the disputed amount.
- IfRecord Subtype=**Chargeback**then the dispute should have a status of**Lost**and should be a negative amount
- IfRecord Subtype=**Chargeback reversal**then the dispute should have a status of**Won**and be a positive amount




## Data dictionaries for Disbursement Report sections


### Report Header Data Dictionary

| Field Name | Description |
| --- | --- |
| RH | RH is short for "Report Header." All rows in the Header section will have the value**RH**in theRHcolumn to indicate the rows belong to the Header section. |
| Report name | The name of the Report. |
| Report status | Status of the report. Will be either:**success**or**Error** |
| Report generated | The date the report was generated. Will be formatted YYYY-MM-DD |
| Hierarchy | The business level hierarchy for the data captured in the report |
| Timezone | The timezone for which the report was generated |


### Report Summary Data Dictionary

| Field Name | Description |
| --- | --- |
| RS | RS is short for "Report Summary." All rows in the Summary section will have the value**RS**in theRScolumn to indicate the rows belong to the Summary section. |
| Transfer ID(s) | The unique PayPal generated value that identifies the disbursement transfer in the PayPal system. Can be used to identify to which transfer a disbursement batch belongs |
| Bank account | The last 4 digits of the bank account that the transfer |
| Currency | Indicates the disbursement currencies |
| Net disbursed amount | Total amount disbursed for each currency that is included in the report. This will equal the amounts found inCurrent disbursement amountandPrevious failed disbursement amount |
| Current disbursement amount | The total amount being disbursed in this reporting period |
| Previous failed disbursement amount | If the previous disbursement failed and was included in the current day's disbursement, its amount will be found here. |
| Previous transfer ID(s) | Transfer ID associated with each disbursed amount. If there are multiple Transfer ID for the records then they will be comma separated. |


### Report Detail Data Dictionary

| Field Name | Description |
| --- | --- |
| RD | RD is short for "Report Detail." All rows in the Detail section will have the value**RD**in theRDcolumn to indicate the rows belong to the Summary section. |
| Record ID | ID of the money movement item. |
| PayPal transaction ID | The PayPal transaction ID. Only populated for PayPal Wallet transactions |
| Record type | The type of the money movement item. |
| Record sub-type | The subtype of the money movement item. |
| Merchant account ID | The Braintree Merchant Account ID that was used to process the transaction |
| Account name | The business name stored on the account in PayPal |
| PayPal account ID | The account number of the PayPal account |
| Created at | The datetime of creation of the money movement object |
| Settlement date | The date on which the money movement event settled. This will only be populated for sales and refunds |
| Disbursement date | The date the money movement was disbursed |
| Transaction currency | The ISO currency code for the transaction currency |
| Gross transaction amount | The gross amount for the transaction in transaction currency |
| Gross transaction fees | The gross fee amount in transaction currency |
| Net transaction amount | The amount in transaction currency net transaction fees |
| Settlement currency | The ISO currency code for the settlement currency |
| Gross settlement amount | The gross amount for the transaction in settlement currency |
| Gross settlement fees | The gross fee amount in settlement currency |
| Net disbursed amount | The amount in settlement currency net settlement fees |
| Exchange rate | The exchange rate of the transaction if there is a difference between presentment and settlement currencies |
| Tax amount | Merchant generated value passed at time of transaction |
| Tax exempt | Merchant generated value passed at time of transaction |
| Transfer ID | The Transfer ID to which the disbursed item belongs |
| Currency conversion record ID | The record ID of the currency conversion in PayPal |
| Dispute ID | The ID of the dispute in the Braintree gateway |
| Order ID | Merchant generated value passed at time of transaction |
| Purchase order number | Merchant generated value passed at time transaction |
| PayPal custom field | Merchant generated value passed at time of transaction. Only applicable for PayPal Wallet and Credit transactions |
| Original record ID | The ID of the original transaction. For**Refund**record types, this value will be the original Sale Transaction ID |
| Acquirer reference number | The Transaction ID from the acquirer |
| Payment instrument type | The type of payment instrument used by the customer for the transaction |
| Payment instrument sub-type | The subtype of the payment instrument used by the customer for the transaction |
| Payment method token | The token value that represents the payment method in the Braintree vault |
| Number of installments | The total number of installments to which the installment belongs to. |
| Installment number | The sequence number of the installment |
| Bank account | The last 4 digits of the bank account that the transfer |


### Footer Data dictionary

| Field Name | Description |
| --- | --- |
| RF | RF is short for "Report Footer." All rows in the Footer section will have the value**RF**in theRFcolumn to indicate the rows belong to the Summary section. |
| Total files | The number of files that were generated for the day |
| File number | The sequence number of the file |
| Total records | The total number of records in the the Detail report |


## Record types and subtypes

| Record Type | Record Subtype |
| --- | --- |
| Adjustment​ | (null)​ PayPal receivables​ PayPal Credit adjustment​ Account correction​ |
| Hold​ | Temporary holds​ Account holds​ |
| Funds transfer​ | (null)​ Recoupment​ Receivables financing​ |
| Currency conversion​ | Conversion from​ Conversion to​ Balance conversion​ |
| Payout​ | ​ |
| Payout refund​ | ​ |
| Payout reversal​ | ​ |
| Return - ACH return​ | UnAuth returns​ General returns​ |
| Other ​ | Payment sent​ Payment received​ Payment reversal​ Donation​ ACH reversal​ Blocked payments​ |
| Partner fees​ | Partner Tax​ (null)​ |
| Failed disbursement​ | ACH reversal​ |
| Sale​ | (null)​ Installment​ |
| Refund​ | Referenced ​ Non-referenced​ |
| Dispute​ | Retrieval​ Chargeback​ Pre-arbitration​ Chargeback reversal​ |
| Installment​ | Disbursements​ Refund adjustments​ |
| Add money​ | (null)​ Credit card deposit​ PayPal Credit deposit​ PayPal payables​ Incentive deposit​ |
| Withdraw money​ | (null)​ Non-bank withdrawal​ Credit card withdrawal​ |
| Fees​ | Chargeback fees​ Resolution fees​ Withdrawal fees​ Payout fees​ Fee reversal​ Fee refund​ Monthly fees​ |
| Bonus​ | (null)​ Cash bonus​ Referral bonus​ Warranty bonus​ Protection bonus​ |
| Reversal​ | Account hold reversals​ Temporary hold reversals​ Incentive reversal​ |


## Payment instrument types and subtypes

| Payment Instrument | Payment Instrument Subtype |
| --- | --- |
| Credit card​ | Visa Mastercard​ American Express Discover Hipercard Elo Union Pay |
| Debit card​ | Visa Mastercard​ American Express Discover Hipercard Elo Union Pay |
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
| 1.1 | 04-27-2021 | Changed "Presentment" fields to "Transaction" |

