<!-- Source URL: https://developer.paypal.com/braintree/articles/au/reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reconciliation
slug: /articles/au/reconciliation/
createTime: '2025-04-01T23:49:48.968Z'
updateTime: '2025-04-01T23:49:48.994Z'
---



# Reconciliation

We provide you with a monthly merchant statement and multiple reports for reconciling disbursements
to your bank account. This guide outlines where to locate those tools and how to best utilize them
for reconciliation.
## Statement reconciliation

Your best tool for reconciliation is your monthly merchant statement. [Learn more about the information available in your statement.](/braintree/articles/au/statements)


### Disbursement Details

Most of our merchants reconcile by comparing the Disbursement Details section to the deposits they see in their bank accounts. In this section of your statement, the Date column reflects when we disbursed the funds to your bank. If you use NAB for your business banking account, settled funds should be deposited the same day. If you use a different bank for your business account, funds should be reflected on your bank statement within 1-2 business days of the disbursement date. The Total Disbursed column will match the deposit you see on your bank statement.


### Braintree Fee Details

To reconcile the individual transaction and billable event fees listed in the [Braintree Fee Details](/braintree/articles/au/statements#braintree-fee-details) section of your merchant statement with processed transactions, you must download a [Transaction-Level Fee report](/braintree/articles/control-panel/reporting/transaction-level-fee-report) from the Control Panel. When downloading this report, be sure to select the same date range as the merchant statement you are reconciling against.

Your Transaction-Level Fee report includes a Creation Date column, which lists the date that the fee in question was created. For transaction fees and most billable event fees, this is the date the associated transaction was initiated; for declines, this is the date when the decline was first created. We use this date to determine the value listed in the Quantity column in your Braintree Fee Details table.


#### Reconciling billable event fees

[Billable event fees](/braintree/articles/au/statements#billable-event-fees) are the individual fees applied to declines, refunds, verifications, and two-step authorizations. Because there can be a delay between when a billable event fee is created and actually billed, you will need to reconcile the Quantity and Total Billed values for each billable event separately with the Transaction-Level Fee report.


##### Authorizations

Your Transaction-Level Fee report will include a column for Auth Type, identifying whether a transaction was authorized and submitted for settlement in a combined single step (indicated with a 1) or if the transaction was authorized and settled in separate actions (indicated with a 2). One-step authorizations only incur transaction fees; two-step authorizations will incur an authorization billable event fee in addition to the transaction fees.

To reconcile the Quantity value for two-step authorization events:


- Filter theCreated Datecolumn to only dates within the statement period
- Filter theAuth Typecolumn to2
- The number of rows left will be equal the number of authorization fees that were created in the statement time period

To reconcile the Total Billed value for two-step authorization events:


- Filter theAuth Fee Billed Dateto only dates within the statement period
- Filter theAuth Typecolumn to2
- The number of rows left will be equal the number of authorization fees you were billed for in the statement time period

If you authorize a transaction at the end of the month, and it does not settle until the next statement period, you could see a transaction on the Transaction-Level Fee report that has an authorization fee but no settlement date. When you run this report the next month, the now-settled transaction will have values populated in all of the appropriate columns.


##### Refunds

Refund fees are applied to each transaction refund that you process. No other billable event fees are assessed for processing a refund.

To reconcile the Quantity value for refund events:


- Filter theCreated Datecolumn to only dates within the statement period
- Filter theTransaction Typecolumn tocredit
- The number of rows left will be equal the number of refund fees that were created in the statement time period

To reconcile the Total Billed value for refund events:


- Filter theDisbursement Dateto only dates within the statement period
- Filter theTransaction Typecolumn tocredit
- The number of rows left will be equal the number of refund fees you were billed for in the statement time period


##### Declines

Decline fees are charged for every processor declined transaction. If the transaction also went through a two-step authorization before being declined, it will have both authorization and decline fees assigned to it.

To reconcile the Quantity value for decline events:


- Filter theCreated Datecolumn to only dates within the statement period
- Filter out any blank cells from theDeclined Feecolumn
- The number of rows left will be equal the number of decline fees that were created in the statement time period

To reconcile the Total Billed value for decline events:


- Filter theDeclined Fee Billed Dateto only dates within the statement period
- Filter out any blank cells from theDeclined Feecolumn
- The number of rows left will be equal the number of refund fees you were billed for in the statement time period


##### Verifications

Verification fees are applied to every card verification and are not listed on your Transaction-Level Fee report. You can reconcile the Total Billed value for verification fees by running a [Verification Search](/braintree/articles/control-panel/search#verifications) in the Control Panel for the same date range as your merchant statement:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Vault**in the navigation bar
- Click on the**Verifications**tab
- Uncheck all**Status**types exceptVerified
- Define any other desired parameters and click the**Search**button
- To download a CSV, click the**Download**button


## Additional reconciliation tools

In addition to your statement, we provide a Disbursement Summary Report and a Disputes Report that can assist you in the reconciliation process.


### Disbursement Summary report

If you would like to see individual transactions from a particular day’s disbursement, or see your gross sales and credits grouped by card type, you can use the Disbursement Summary in the Control Panel. Keep in mind that it can take 1-3 business days after the disbursement for the Disbursement Summary to become available, and only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access this report in the Control Panel.

While disbursements typically take 1-2 business days to reach your bank account, this timeframe can vary. As a result, it’s best to match the amount of the deposit on your bank statement with the **Total Disbursed** amount in the [Disbursement Details section](#disbursement-details) on your Braintree statement. Once you determine Braintree’s disbursement date, you can use that to pull the corresponding Disbursement Summary.


**NOTE**
 The Disbursement Summary does not include transaction fees.

 

To find your Disbursement Summary:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Disbursement Summary**, click the**Run Report**button
- Select the desired merchant account and date range
- Click the**Run Disbursement Summary**button
- To download a report that shows you the totals for each day grouped by card type, click the**Download .Csv**button
- To see all transactions from a specific day, click the**View Transactions**link next to the desired day




### Advanced search

You can reconcile your billable events (declines, authorizations, verifications, and refunds) with specific transactions or verifications from the statement period by performing [advanced searches](/braintree/articles/control-panel/search#advanced-search-options) in the Control Panel. The type of advanced search you run will depend on the types of event you want to reconcile. [Contact us](/braintree/help/Reconciling) with questions.


### Dispute Report

Users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Dispute Report in the Control Panel. To access the report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Dispute Report**, click the**Run Report**button

This report lists every dispute within a given date range, along with important details such as the status of the dispute or the payment method type used for the disputed transaction. All disputes with the status of Open or Won will also include a value in the Disbursement Date column, indicating when disputed funds were credited or debited from your bank account. Use the Dispute Report when running a chargeback analysis or alongside your statement for reconciliation purposes.

