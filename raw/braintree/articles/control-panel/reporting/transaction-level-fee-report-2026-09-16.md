<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/reporting/transaction-level-fee-report -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Transaction-Level Fee Report
slug: /articles/control-panel/reporting/transaction-level-fee-report/
createTime: '2025-04-02T01:10:37.185Z'
updateTime: '2025-04-02T01:10:37.202Z'
---



# Transaction-Level Fee Report


**AVAILABILITY**
 The Transaction-Level Fee report is available by default to US and Australia based merchants on IC+, and to US, Australia, and Brazil based merchants on flat rate or blended pricing models.

 

The Transaction-Level Fee report provides detailed information about your transactions and the fees associated with them. The details provided in the report depend on whether you have an [IC+ pricing model](#ic+-pricing-models), or a [flat rate or blended model](#flat-rate-and-blended-pricing-models). [Contact us](/braintree/help) if you're unsure of your pricing model.

Payment methods supported by the Transaction-Level Fee report:


- Credit and Debit Cards
- Venmo Accounts
- Apple Pay
- Google Pay


## Running a Transaction-Level Fee report

Only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Transaction-Level Fee report. To run this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Transaction-Level Fee Report**, click the**Run Report**button
- Select the desired merchant account and date range
- Click the**Run Transaction-Level Fee Report**button
- Click the**Download**link next to the report you would like to view


**NOTE**
 American Express transactions processed directly through Amex and all PayPal transactions will not be included in this report.

 


## Flat rate and blended pricing models

The Transaction-Level Fee report for flat rate and blended merchants contains the actual Braintree fees charged for each transaction as defined by your pricing agreement. Data for an individual transaction will become available in this report 3 calendar days after the settled amount is disbursed into your bank account.

This report can give you deeper insight into the following:


- Cost of Braintree fees per transaction
- Reconciliation at a transaction-level
- Card types typically used by your customers
- Regions your customers typically reside in
- Cost trends across time periods, card types, card brands, etc.


## IC+ pricing models


**IMPORTANT**
 The Transaction-Level Fee report for merchants on an IC+ pricing model contains interchange fee estimates and should not be used for reconciliation. [Learn more about interchange estimates for IC+ merchants.](#interchange-fee-estimates)

 

The Transaction-Level Fee report for merchants on an IC+ pricing model will contain:


- Transactions by type (e.g. sale or credit)
- Estimated interchange rate and fee charged for each sale transaction
- Estimated interchange rate and fee refunded for each credit or refund
- Discount rate and fee charged for each sale transaction
- Discount rate and fee refunded for each credit or refund

For IC+ merchants, data for an individual transaction will become available in this report 5 calendar days after the settled amount is disbursed into your bank account.


**NOTE**
 If you elect to accept Venmo through a merchant account that is priced as IC+, the Venmo transaction will be included in your IC+ Transaction Level Fee Report.

 

This report can help IC+ merchants gain a better understanding of:


- Interchange pricing tiers
- Cost of Braintree fees per transaction
- Card types typically used by your customers
- Regions your customers typically reside in
- Cost trends across time periods, card types, card brands, etc.


### Interchange fee estimates

The Transaction-Level Fee report includes estimated interchange fee rates for each transaction. After a transaction is processed, these estimated values are often adjusted through a process known as reclassification, and the actual per-transaction interchange fees are passed on to you in a consolidated sum at the end of the month. As a result, exact transaction-level fee assessments for interchange are not available.

The estimated interchange fees listed in this report should be used for general reference and identifying trends – not for reconciliation.

