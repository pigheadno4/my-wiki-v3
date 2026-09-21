<!-- Source URL: https://developer.paypal.com/braintree/articles/apac/statements-reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Statements and Reconciliation
slug: /articles/apac/statements-reconciliation/
createTime: '2025-04-01T22:56:33.336Z'
updateTime: '2025-04-01T22:56:33.358Z'
---



# Statements and Reconciliation


## Statements

Statements for the previous month are made available on the 4th of each month. To access your statements:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Statements**tab


**NOTE**
 If you are unable to access or do not see the **Reports** page in the navigation bar, you'll want to make sure that your user’s role has the View Statements [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-view-statements) enabled.

 


### Disbursement Summary

The Disbursement Summary section of your statement is a quick way to view your gross sales, refunds, and chargeback credits and debits.


### Processing Summary

The Processing Summary shows the number of sales, refunds, and chargeback credits and debits you processed.


### Fee Details

The Fee Details section breaks down the different fees that were charged to your account and identifies the quantity for each. You’ll also find any credits to your account for refunds.


- **Discount**: Total volume of Braintree fees that were applied based on your discount rate
- **Discount Credits**: Total volume of Braintree fees that were returned to you (if applicable)
- **Chargeback Fee**: Total fees assessed for chargebacks processed
- **Auth Fees***: Total amount of authorization fees assessed from the previous month, which you'll see debited from the first disbursement in the Daily Disbursement Details on your statement
- **Other**: Any billing refunds and adjustments that are applied

*The cutoff date for calculating authorization fees is 2:45am HKT on the second to last day of the month. Authorizations that occur after this time will be billed the following month.


### Daily Disbursement Details

All amounts in the Daily Disbursement Details are listed in your [settlement currency](/braintree/articles/get-started/currencies).


- **Disbursement Date**: Date that funds were deposited into your account — generally 2-3 days after the transaction creation date, and 1 day before the settlement date listed in the[APAC Transaction Detail Report](#downloading-the-apac-transaction-detail-report)
- **Number of Transactions**: Total number of settled transactions on a given day
- **Gross Sales**: Total dollar amount processed on a given day
- **Refunds**: Total amount refunded
- **Chargeback Credits**: Amount credited due to disputes won
- **Chargeback Debits**: Amount debited due to disputes received
- **Total Disbursed***: Total amount deposited into your bank account

* If the amount debited is greater than the amount credited for a given disbursement date, the Total Disbursed will be listed as 0, and the negative balance will roll into the following day.


## Reconciliation

Most of our merchants reconcile by comparing the information in the APAC Transaction Detail Report — which is generated daily — to the deposits they see in their bank accounts.

The funding descriptor on your deposits should read something similar to:

GIRO MISCELLANEOUS MISC C/A - SCB CARD STS PYT


### Downloading the APAC Transaction Detail Report

The APAC Transaction Detail Report lists all the transactions and chargebacks in each settlement batch. The transactions are organized by **settlement date** and have all transaction details listed – including currency, card type, and associated fees. For reconciliation purposes, pull the APAC Transaction Detail Report for the same date that funds were disbursed to your bank account.

Only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the APAC Transaction Detail Report. To run this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**APAC Transaction Detail Report**, click the**Run Report**button
- Make your date selections and click the**Run APAC Transaction Detail Report**button
- Click the**Download**link to download the report


### Daily reconciliation

Once you’ve downloaded the APAC Transaction Detail Report, you’ll be able to reconcile your sale and chargeback amounts with the deposits in your account. If you subtract the sum of your fees and chargeback amounts from the sum of your settlement amounts, the result should match your deposit.

It is important to note that the Fees column in your APAC Transaction Detail Report is only for transaction fees. This column does not include authorization fees or chargeback fees; as a result, the fee value for any chargeback on this report will always be zero. You can calculate your chargeback fees by multiplying the number of chargebacks on the report by the [flat chargeback fee for your currency](/braintree/articles/apac/chargebacks-retrievals-prearbs#chargeback-fees). You can also find your total chargeback fees listed on your [monthly statement](#statements).


**NOTE**
 If you are reconciling the 1st disbursement of the month, make sure to subtract your authorization fees, as those are debited from your disbursement at the beginning of each month. You’ll find the total amount of authorization fees debited in the **Auth Fees** column of your monthly [statement](#statements).

 

