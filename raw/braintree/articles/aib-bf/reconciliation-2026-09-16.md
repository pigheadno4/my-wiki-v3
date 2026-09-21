<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-bf/reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reconciliation
slug: /articles/aib-bf/reconciliation/
createTime: '2025-04-01T22:25:15.108Z'
updateTime: '2025-04-01T22:25:15.133Z'
---



# Reconciliation

Most of our merchants reconcile by comparing the Disbursement Details – which can be found on the second page of your Braintree statement – to the deposits they see in their bank accounts.

If you’re looking for more granular information, some merchants like to reconcile down to the transaction by [calculating their own per transaction fees](/braintree/articles/aib-bf/reconciliation#calculating-fees-on-a-transaction-level).


**IMPORTANT**
 While the [Dashboard](/braintree/articles/control-panel/overview#dashboard) and the [Settlement Batch Summary](/braintree/articles/control-panel/reporting/settlement-batch-summary) can be helpful tools, they should not be used for reconciliation purposes.

 


## Disbursement Details

In the **Disbursement Details** – which can be found on the second page of your Braintree statement – the Date column reflects when we disbursed the funds to your bank. Depending on how long your bank takes to manage incoming deposits, these funds should be reflected on your bank statement within 1-3 business days of the disbursement date.

The **Disbursement Details** also show you a breakdown of the fees applied to each disbursement, and the Total Disbursed column will match the deposit you see on your bank statement.


## Disbursement Summary report

If you would like to see individual transactions from a particular day’s disbursement, or see your gross sales and credits grouped by card type, you can use the Disbursement Summary in the Control Panel. Keep in mind that it can take 1-3 business days after the disbursement for the Disbursement Summary to become available, and only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access this report in the Control Panel.

While disbursements typically take 1-3 business days to reach your bank account, this time frame can vary. As a result, it’s best to match the amount of the deposit on your bank statement with the **Total Disbursed** amount in the [Disbursement Details](#disbursement-details) on your Braintree statement. Once you determine Braintree’s disbursement date, you can use that to pull the corresponding Disbursement Summary.


**NOTE**
 The Disbursement Summary does not include transaction fees.

 


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Disbursement Summary**, click the**Run Report**button
- Select the desired merchant account and date range
- Click the**Run Disbursement Summary**button
- To download a report that shows you the totals for each day grouped by card type, click the**Download .Csv**button
- To see all transactions from a specific day, click the**View Transactions**link next to the desired day



If you would like to review transactions that were disbursed across multiple days, it is best to run a transaction search by following the steps in the next section.


## Reconciling disputes

You can reconcile disputes with your Braintree statement by using the Disbursement Date column of the [Disputes Financial Impact Report](/braintree/articles/aib-bf/chargebacks-retrievals-prearbs#dispute-reports). Here you will find the exact date that disbursed funds were credited or debited from your account.


## Calculating fees on a transaction level

You can calculate the fees for individual transactions by performing a transaction search:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll down to the date range section
- Uncheck the box next to**Creation date range**
- Check the box next to**Disbursed date range**located below the date range section
- Choose your desired date range
- Click the**Search**button
- On the results page, click the**Download**button
- Open the CSV file in the spreadsheet program of your choice

From here, you can create additional columns for your transaction fees. To find your specific transaction fees, look at the [Pricing Schedule](/braintree/articles/aib-bf/statements-reporting#pricing-schedule) on your statement. Make sure to [round down](/braintree/articles/aib-bf/pricing-fees#rounding-down), and then apply the fees to your individual transactions.


**NOTE**
 You can also view all fees assessed and deducted from specific sale transactions within the [Transaction Fee Report](/braintree/articles/aib-bf/statements-reporting#transaction-fee-report). This report is available at the beginning of each month.

 

[Contact us](/braintree/help/feeHelp) if you have any questions about this process.

