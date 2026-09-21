<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-af/reconciliation-lr -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reconciliation (LR)
slug: /articles/aib-af/reconciliation-lr/
createTime: '2025-04-02T01:07:28.010Z'
updateTime: '2025-04-02T01:07:28.044Z'
---



# Reconciliation (LR)


## General reconciliation

For general reconciliation, compare the information in the **Funding Totals** section of your [AIB Merchant Statement](/braintree/articles/aib-af/statements#funding-totals) to the deposits you see in your bank account. This is where details of all bank transfers completed within the billing period are, along with the text that will appear on your bank statements for each disbursement.


## Transaction-level reconciliation

Use the Transaction Fee Report to reconcile your daily deposits for your Braintree AIB funded accounts with your system of records and to clear your receivables. This report contains both summarized and event-level details (including fees) of every payment event that impacted a deposit from your AIB funded Braintree account to your deposit bank account.


## Sample files


### Net settlement sample files

[Sample net settlement AIB Transaction Fee Report](/braintree/files/sampleNetMerchant_020412386_2022-04-29.csv)


### Gross settlement sample files

For Gross settlement reconciliation you will need to test two files:

[Sample gross settlement file (daily credit)](/braintree/files/sampleGrossMerchant_020274043_disbursements_2022-04-29.csv)

[Sample gross settlement file (fee debit)](/braintree/files/sampleGrossMerchant_020274043_disbursements_2022-05-13.csv)


### Transaction-level fee report format

The Transaction Fee Report contains 3 record categories:


- Gateway Transaction Records
- Accounting Based Records
- Summary Records


#### Gateway Transaction Records

The Gateway Transaction Records contain line-item details for all transaction events in the gateway impacting disbursement (e.g., transactions, disputes, etc.).


#### Accounting Based Records

The Accounting Based Records contain line-item details for accounting records, such as Fees and Adjustments that are assessed at a MID level and impact disbursements (e.g., 3DS Fees, Network Registration Fees).


#### Summary

The Summary Record contains summarized data about each disbursement in the reporting period. Each disbursement appears as a line-item in this section and will have information about the total amount disbursed per MID and the transfer ID of the disbursement.


### How to Use the Report


#### Reconciling deposit amount to the reported amounts

To reconcile the line-item deposit records on your bank statement with the AIB Transaction Fee Report:


- Using the Transfer ID, match each deposit amount from AIB on your bank statement with the amounts found in the Net Disbursed columns of the Summary Records of the Transaction Fee Report
- Locate the “Transaction Disbursement Key” for each deposit line-item
- Use Transaction Disbursement Key for each deposit to identify the rows that belong to each deposit
- For each unique Transaction Disbursement Key:
- Add the Settlement amount for each row and truncate the total to two decimals (do not round)
- Add the Total Fee Amount for each row (For Gateway Transaction Records, only add if the “Transaction Fee Debit Date” = “Settlement Date”) and truncate the total to two decimals (do not round)
- Add the Chargeback Amount for each row and truncate the total to two decimals (do not round)


- The sum for each group will match the amounts found in the corresponding "Summary" sections
- Add all the amounts in the summary row to calculate the “Net Disbursed” for each Transaction Disbursement Key

Once you have confirmed that all the disbursement impacting items (e.g., transactions, disputes, etc.) are present in the report, reconcile the items by Record Type as outlined in the following sections.


#### Reconciling standard sales and refunds

To reconcile standard sales and refunds records that have been disbursed to your bank account:


- Locate records where Record Type is eitherSaleorRefund.
- With the sale and refund records selected, iterate through the set to locate the Transaction ID, and ingest the following data at a minimum:
- Disbursement Date- The date the installment was disbursed
- Transaction Disbursement Key- The unique ID for each bank transfer
- Net Disbursed- The net amount deposited in your bank, as part of the disbursement, in disbursement currency.




**NOTE**
 For merchants in net settlement, this will be net of fees. Merchants in gross settlement should refer to the [Reconciling Fees (gross settlement)](/braintree/articles/aib-af/reconciliation-lr#reconciling-fees-(gross-settlement)) section.

 


#### Reconciling disputes

To reconcile disputes that have impacted your disbursement:


- Locate records whereRecord Type = Dispute
- With the dispute records selected, iterate through disputes using theChargeback Case Numbercolumn to identify the dispute
- Match the value in theNet Disbursedcolumn with the disputed amount


#### Reconciling fees (gross settlement)

To reconcile processing fees that have impacted your disbursement:


- Locate records where the record type isFee, and the record subtype isProcessing Fees
- Iterate through the records selected using theTransaction ID, and ingest the following data at a minimum:
- Disbursement Date- The date the installment was disbursed
- Transaction Disbursement Key- The unique ID for each bank transfer
- Net Disbursed- The fees assessed for the transaction, in disbursement currency, that was included in the deposit


- Match the value in the Net Disbursed column with the fees assessed for each transaction and mark as paid


### Data dictionary for Report Records

| Field Name | Can be null? | Description |
| --- | --- | --- |
| Merchant Account ID | Yes | The Braintree Merchant Account used to process the transaction. Mandatory for sales and refunds. |
| Transaction ID | Yes | The Braintree transaction ID. Mandatory for sales and refunds. |
| Transaction Type | Yes | The type of transaction, will be one of the following: sale, credit, chargeback_won, chargeback_opened Empty for Accounting Based Records and Summary |
| Original transaction ID | Yes | The transactions ID of the sale transaction that was refunded. Mandatory for refunds. |
| MID | No | The acquirer merchant ID. |
| Transaction Currency | Yes | The currency the customer was charged in. Also known as presentment currency. |
| Transaction Amount | Yes | The amount the customer was charged in the transaction currency. |
| Settlement Currency | Yes | The currency Braintree settled the transaction in. |
| Settlement Amount | Yes | The amount of the settlement in the in the settlement currency. |
| Exchange Rate | Yes | The exchange rate between the Transaction Currency and the Settlement Currency. |
| Settlement Date | Yes | The date on which the transaction settled. |
| Transaction Disbursement Date | Yes | The date on which the transaction was disbursed to merchant's bank account. |
| Card Brand | Yes | Brand of the credit or debit card used for the transaction. |
| Card Type Group | Yes | Type of credit card product, only populated for EMEA region. Possible values: Consumer Debit, Commercial, Consumer Credit. |
| Region Relation | Yes | Interchange qualification region (EMEA only). Possible values: Inter-region, Intra-region, Domestic. |
| Interchange Description | Yes | Description of the interchange category. |
| Interchange Fee Currency | Yes | Currency for the interchange charge. |
| Total Interchange Fee Amount | Yes | Total Interchange charge for the transaction. |
| Scheme Fee Currency | Yes | Currency for the scheme fee charge. |
| Total Scheme Fee Amount | Yes | Total Scheme fee charge for the transaction. |
| Order ID | Yes | Order ID for the transaction. Populated by the merchant. |
| Acquirer Reference Number | Yes | The acquirer transaction ID. |
| Transfer ID | No | A value corresponding to the deposit that will appear on the merchant's bank statement. |
| Chargeback Case Number | Yes | The acquirer case number for the chargeback. |
| Chargeback Currency | Yes | The currency for the amount being charged back. |
| Chargeback Amount | Yes | The amount of the chargeback. |
| Discount Fee | Yes | The fee from the acquirer. |
| Total Fee Amount | Yes | The Total amount of fees charged. |
| Total Fee Currency | Yes | The currency for the fees charged. |
| Transaction Fee Debit Date | Yes | The date on which the fee was debited for the transaction. |
| Original Transaction Order ID | Yes | The order ID of the original sale transaction. Only populated for refunds. |
| Record Type | No | The type of payment action that the row contains data for. Refer to Transaction Types and Subtypes section. |
| Record Subtype | Yes | The subtype of the payment action that the row contains data for. This will be "null" for "sale" record types. Refer to the Transaction Types and Subtypes section. |
| Transaction Disbursement Key | No | A unique number identifying each deposit to merchant's bank account. |
| Net Disbursed | No | This is the corresponding value for a particular record included in the disbursement/debit. Refer to the specific section on gross or net settlement to understand your specific case. |


### Record types and Subtypes

| Record Category | Record Type | Record Subtype | Description |
| --- | --- | --- | --- |
| Gateway transaction records | Sale | (null) | Payments received. |
|  | Refund | (null) | Refunds to customers. |
|  | Dispute | Chargeback | A disputed transaction. |
|  | Dispute | Chargeback reversal | A chargeback that is reversed after won. |
| Accounting based records | Adjustments | Merchant Credit | Miscellaneous credit applied to account. |
|  | Adjustments | Reserved Funds Released | Used when PayPal instructs AIB to pay money to a merchant on an ad hoc basis. |
|  | Adjustments | Alternative Payment Processing | Used for cross MID matching (e.g. to clear the negative balance on an MID based on the processing volume of another MID). |
|  | Adjustments | Pre-edit adjustments | Transactions that after settlement, are rejected by schemes. |
|  | Failed disbursement | (null) | When bank deposits fail, payment corresponding to the failed deposit is reported under this type. |
|  | Dispute | Grouped Chargeback | Used for Diners &amp; JCB Chargebacks &amp; claims with no original transaction (CWOT). CWOT may happen if transactions are over 6 months old for example. |
|  | Add funds | Manual Invoice Collection (Neg Bal) | Funds added against an account due to a negative balance. |
|  | Add funds | (null) | Used to credit large amounts to a MID as a manual, one-time transfer when the need arises. |
|  | Fees | Authorization Fees | Authorization Fee is applied/charged; monthly fee is the default timing. |
|  | Fees | Enhanced Authorization Fee | Fee is applied/charged; monthly fee is the default timing. |
|  | Fees | Excessive Chargebacks Fee | Scheme fee that is passed through when merchants' ratio goes over the acceptable threshold. |
|  | Fees | Chargeback Fees | Monthly fee for all chargeback handling fees. |
|  | Fees | Mastercard Network Fees | MasterCard annual registration fees. |
|  | Fees | Manual Invoiced Fees | This subtype will be used in cases in which Braintree cannot debit fees directly. |
|  | Fees | MASTERCARD DAF Scheme Fee | Scheme's chargeback fee (MasterCard all chargebacks). |
|  | Fees | MASTERCARD Dispute Administration Fee | Scheme's chargeback fee (MasterCard all chargebacks). |
|  | Fees | VISA CNP Fraud CBK Scheme Fee | Scheme's chargeback fee (Visa Fraud only). |
|  | Fees | PCI Fee | Payment Card Industry Fee (Generally not applicable). |
|  | Fees | 3DS Scheme Fee | Scheme fee for 3DS |
|  | Fees | Marketplace Fees | Fee for marketplace services |
|  | Fees | Processing Fees | Corresponding processing fee charges for gross settlement merchants. |
| Summary records | Summary | (null) | This indicates the deposit/charge summary row. This will reconcile to the bank deposit. |

