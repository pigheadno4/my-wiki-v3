<!-- Source URL: https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reconciliation
slug: /articles/br/reporting-reconciliation/reconciliation/
createTime: '2025-04-02T01:13:04.932Z'
updateTime: '2025-04-02T01:13:04.953Z'
---



# Reconciliation

We provide you with a monthly merchant statement and multiple reports for reconciling disbursements to your bank account. This guide outlines where to locate those tools and how to best utilize them for reconciliation.


## Statement reconciliation

Your best tool for reconciliation is your monthly merchant statement. [Learn more about the information available in your statement.](/braintree/articles/br/reporting-reconciliation/statements)


### Disbursement Details

Most of our merchants reconcile by comparing the **Disbursement Details** section to the deposits they see in their bank accounts. In this section of your statement, the Date column reflects when we disbursed the funds to your PayPal account, which are then swept into your bank. If you use the batch settlement feature, funds that settle Monday through Thursday should be deposited into your bank the same day; funds settled on Fridays will be swept on the following Monday. Once swept, funds should be reflected on your bank statement within 1-2 business days.


**NOTE**
 The Total Disbursed column will match the deposit you see in your PayPal account, however due the to the fact that some of your settled funds may be sent to your partnering bank for the purposes of debt repayment, you must use to the [Unified Disbursement Report](/braintree/articles/br/reporting-reconciliation/disbursement-report) to reliably reconcile the deposits to your bank account.

 


## Additional reconciliation tools

In addition to your statement, we provide a Disbursement Summary Report and a Disputes Report that can assist you in the reconciliation process.


### Unified Disbursement Report

PayPal provides a disbursement report that will include both PayPal and Braintree processed transactions in a single report. This report will detail all disbursement impacting events, including sales, refunds, installments, disputes, and fees. Additionally, the report makes it possible to reconcile multiple Braintree accounts that may settle into a single PayPal account and get disbursed together. [Learn more about how to use the Unified Disbursement Report](/braintree/articles/br/reporting-reconciliation/disbursement-report).


### Disbursement Summary report

If you would like to see individual transactions from a particular day’s disbursement, or see your gross sales and credits grouped by card type, you can use the Disbursement Summary in the Control Panel. Keep in mind that it can take 1-3 business days after the disbursement for the Disbursement Summary to become available, and only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access this report in the Control Panel.

While disbursements typically take a few business days to reach your bank account, this timeframe can vary. As a result, it’s best to match the amount of the deposit on your bank statement with the Total Disbursed amount in the [Disbursement Details section](#disbursement-details) on your Braintree statement. Once you determine Braintree’s disbursement date, you can use that to pull the corresponding Disbursement Summary.


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




### Dispute Report

You can reconcile disputes with your Braintree statement by using the Disbursement Date column of the [Disputes Financial Impact Report](/braintree/articles/br/chargebacks-retrievals-prearbs#disputes-financial-impact-report). Here you will find the exact date that disbursed funds were credited or debited from your account.

