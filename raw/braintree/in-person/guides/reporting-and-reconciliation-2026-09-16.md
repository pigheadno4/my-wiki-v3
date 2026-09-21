<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/reporting-and-reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reporting and Reconciliation
slug: /in-person/guides/reporting-and-reconciliation/
createTime: '2024-11-20T19:03:24.515Z'
updateTime: '2025-01-21T10:38:30.976Z'
---



# Reporting and Reconciliation

There are many ways to reconcile your payments with Braintree, here are some of the tools available to you


## Transaction Lifecycle

For more information about the transaction lifecycle and the definitions of important transaction status' see the [Braintree transaction lifecycle](/braintree/articles/get-started/transaction-lifecycle/). For additional documentation on status definitions within the Braintree platform see these [docs here](/braintree/docs/reference/general/statuses/).


### In-Store Transaction Settlement Timelines:

Braintree offers a pass through payout model where we disburse settled funds to our merchants as we receive them from the card schemes (ex: Visa, Mastercard, Discover, AMEX, etc...). Typically this happens **T+2** ( transaction date plus 2 business days ), however, this can vary by card scheme. See the below example of a typical [settlement funding timeline](/braintree/articles/wells-ic/transactions/settlement-funding-timeline/).

**NOTE**
This can vary due to a number of factors including day of the week (since banks are closed on Saturday and Sunday in the US), the below is just an example of the happy path

| **Request Type** | **Action** | **Day** |
| [requestCharge](/braintree/in-person/guides/making-a-transaction/#initializing-the-reader-for-charging) | Cardholder funds are authorized + capture initiated | Monday |
| Funds Settlement | Braintree Settlement Job runs (not merchant initiated) | Monday |
| Processor transfers funds to Braintree | Braintree receives funds | Tuesday |
| Braintree initiates disbursement | Braintree initiates disbursement of funds to the merchant | Tuesday |
| Merchant Deposit | Merchant receives funds from Braintree to their configured bank account | Wednesday |

For more information on this topic [follow this link](/braintree/articles/wells-ic/transactions/settlement-funding-timeline), or discuss with your Solutions Engineer or Integration Engineer.


### AMEX External Settlement

If you are using your own AMEX SE# to process AMEX transactions through Braintree, this means that you will receive your fund disbursements directly from AMEX for AMEX card transactions. Settlement and funding timelines may vary, more information [here](/braintree/articles/wells-ic/transactions/settlement-funding-timeline#american-express).


## General Information on Braintree Settlement Reporting

You can find more information regarding Braintree's settlement reporting functionality [here](/braintree/articles/control-panel/reporting/settlement-batch-summary).


## Using the Order ID field to reconcile with Braintree settlement reports

The orderId API field is important for reporting and reconciliation. It allows the Point of Sale application to pass a unique transaction identifier which can be used to link sale reporting from the Point of Sale to the settlement reporting produced by Braintree. Whatever information is passed in the orderId field via the API will be displayed in Braintree's settlement reporting. For more information about orderId or other API input fields see our [API reference documentation](/braintree/graphql/reference/#Input--InStoreTransactionInput).

Typically, we would expect a POS System generated sales order number or identifier would be passed in this field, however, you can concatenate by stringing multiple values together including a store identifier, terminal identifier or any other useful information for your reporting/reconciliation.

**NOTE**
See above linked documentation for character limits of the orderId field


## Configuring Custom Fields for In-Store Reporting

If you require more granular custom data from your Point of Sale to be searchable within the Braintree control panel other than the orderId, it's recommended that you create [Custom Fields](/braintree/articles/control-panel/custom-fields/) within the merchant account to suit your needs. Store and pass back fields can be searched by the value passed inside. You can optionally create any number of custom fields to suit your business logic or specific in-store use case.

For example, creating "Store ID", "Terminal ID", and "Cashier ID" custom fields and passing in the data from your application at the time of each transaction would allow you to search for transactions created by a specific cashier or store from within the Braintree control panel.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/reporting-and-reconciliation.png)**NOTE**
If your application is optionally specifying Custom Fields in the API, they must be configured on the merchant account prior to creating a transaction, or it will fail.


## Sample Braintree Reports

Below you will find a sample Braintree Daily Transactions Report, Daily Disbursement Report and Daily Disputes Report. These sample reports are designed to be generic based on the typical merchant set up and may look slightly different depending on the [account structure](/braintree/in-person/get-started-1/account-structure/) you decide to implement with Braintree.

[4KBstandard_transaction_report_sample.csv](/braintree/files/standard_transaction_report_sample.csv)This is a sample "Daily Transactions Report" [1KBdisbursement_report_sample.csv](/braintree/files/disbursement_report_sample.csv)This is a sample "Daily Disbursement Report" [22KBdisputes_report_sample.csv](/braintree/files/sample_disputes_report.csv)This is a sample "Daily Disputes Report"

[Receipt Printing API](/braintree/in-person/guides/receipt-printing-api/)[Testing Your Integration](/braintree/in-person/guides/testing-your-integration/)