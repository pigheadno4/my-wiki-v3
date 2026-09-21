<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/statements-reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Statements and Reconciliation
slug: /articles/wells-flat/statements-reconciliation/
createTime: '2025-04-02T01:27:02.275Z'
updateTime: '2025-04-02T01:27:02.298Z'
---



# Statements and Reconciliation


**NOTE**
 If you are using [Braintree Marketplace](/braintree/articles/guides/braintree-marketplace/overview), your statements will look different. See the [Braintree Marketplace statements and reconciliation guide](/braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation) to learn more.

 


## Statements

Your Braintree statement is a snapshot of your settled transactions, Braintree processing fees, and deposits sent to your account. You can use it for reconciliation purposes or to evaluate your transaction activity.

Statements are available in the Control Panel. To access your statements:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Statements**tab


**NOTE**
 If you are unable to access or do not see the **Reports** page in the navigation bar, you'll want to make sure that your user’s role has the View Statements [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-view-statements) enabled.

 

The statement includes:


- A summary page
- Detailed breakdowns of your
- Disbursements
- Refunds
- Chargebacks
- U.S. bank account transactions
- Venmo transactions


- A key for important terms and column headers


**NOTE**
 Your statement will only include a detailed breakdown of your U.S. bank account transactions and Venmo transactions if you have enabled those payment methods.

 


### Summary page

The summary page will include some or all of the sections outlined below.


#### Disbursement Summary

The Disbursement Summary section of your statement is a quick way to view your gross sales along with any refunds, credits, or fees, and the net amount that was disbursed to your bank account for that statement period.


#### Processing Snapshot

The Processing Snapshot shows the number of transactions, chargebacks, and refunds you processed. It also shows your average transaction amount and allows you to celebrate your best day of gross sales for that period.


#### Braintree Fee Details

The Braintree Fee Details section breaks down the different fees that were charged to your account and identifies the quantity for each. You’ll also find any credits to your account for full refunds (if applicable), chargebacks you have won, and promotions that were applied to your fee calculations.


##### If you are using Braintree’s aggregated Amex account:


- TheDiscountrow will display the total volume of Visa, Mastercard, JCB, and Discover transactions, along with the Braintree fees that were applied based on your[discount rate](/braintree/articles/wells-flat/pricing-fees)
- TheAmerican Express Discountrow will display the total volume of Amex transactions along with the discount rate fees
- The sum of the quantities in theDiscountandAmerican Express Discountrows should be equal to yourGross Salesfound in the[Disbursement Summary](#disbursement-summary)
- The Per Transaction Fee row will display the total number of all transactions, regardless of card type, along with the[per transaction fee](/braintree/articles/wells-flat/pricing-fees)that was assessed for those transactions


##### If you are using your own Amex account:


- TheDiscountrow will display the total volume of Visa, Mastercard, JCB, and Discover transactions, along with the Braintree fees that were applied based on your[discount rate](/braintree/articles/wells-flat/pricing-fees)
- ThePer Transaction Feerow will include Visa, Mastercard, JCB, and Discover transactions, along with the associated fees
- TheAmerican Express Transaction Feerow will include Amex transactions, along with the associated Braintree fees; for information on the additional fees that Amex charges you, you’ll need to contact them directly


#### Pricing Schedule

The Pricing Schedule identifies the [fee structure](/braintree/articles/wells-flat/pricing-fees) for your merchant account, which includes the discount, cross border fee, chargeback fee, and per transaction fee rates. It also displays the [chargeback fee rate](/braintree/articles/wells-flat/pricing-fees#chargebacks,-retrievals,-and-pre-arbitrations).


#### Promotion Usages

If you are enrolled in one of our promotional programs, this section will display the details of that promotion. It includes the name of the promotion, the processing limit, the amount you have accrued towards the limit, and—when applicable—the date that the limit was reached and the promotion was completed.


## Reconciliation

Most of our merchants reconcile by comparing their Disbursement Details—which can be found on the second page of your Braintree statement—to the deposits they see in their bank accounts.

If you’re looking for more granular information, some merchants like to reconcile down to the transaction by calculating their own per transaction fees.


**IMPORTANT**
 While the [Dashboard](/braintree/articles/control-panel/overview#dashboard) and the [Settlement Batch Summary](/braintree/articles/control-panel/reporting/settlement-batch-summary) can be helpful tools for quickly assessing processing activity in your account, they should not be used for reconciliation purposes.

 


### Disbursement Details

In the Disbursement Details — which can be found on the second page of your Braintree statement — the Date column reflects when we disbursed the funds to your bank. The Total Disbursed column will match the deposit you see on your bank statement.


**NOTE**
 The disbursement date reflects the date that the funds were sent to your account – not the date that they'll be available in your account. Funds should be reflected on your bank statement within 1-2 business days of the disbursement date.

 

If you are using Braintree’s aggregated Amex account, the Total Disbursed value will include Visa, Mastercard, Discover, JCB, and Amex transactions.

If you have your own Amex account, Amex handles the disbursements directly. As a result, the funds from your Amex transactions will not be included in the Total Disbursed amount found on your Braintree statement.


### Disbursement Summary report

If you would like to see transactions from a particular day’s disbursement, or see your gross sales and credits grouped by card type, you can use the Disbursement Summary in the Control Panel.


**NOTE**
 The Disbursement Summary does not include transaction fees and will not display Amex transactions for merchants with their own Amex account.

 

Only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Disbursement Summary. To run this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Disbursement Summary**, click the**Run Report**button
- Select the desired merchant account and date range
- Click the**Run Disbursement Summary**button
- To download a report that shows you the totals for each day grouped by card type, click the**Download .Csv**button
- To see all transactions from a specific day, click the**View Transactions**link next to the desired day




### Dispute Report

You can reconcile disputes with your Braintree statement by using the Disbursement Date column of the [Disputes Financial Impact Report](/braintree/articles/wells-flat/chargebacks-retrievals-prearbs#dispute-reports). Here you will find the exact date that disbursed funds were credited or debited from your account.

[Contact us](/braintree/help/Reconciling) if you have any questions about this process.


### Transaction-level reconciliation

You can review the Braintree fees assessed at the transaction level by [running a Transaction-Level Fee report](/braintree/articles/control-panel/reporting/transaction-level-fee-report#running-a-transaction-level-fee-report). This report contains the actual Braintree fees charged for each transaction.


## Multi-currency reconciliation


**NOTE**
 This section applies to merchants that have multi-currency merchant accounts. For more information on the difference between accepting multiple currencies and having a multi-currency merchant account, see our support article on [currencies](/braintree/articles/get-started/currencies).

 

During the disbursement process, we will convert all of your transactions to USD without charging any additional conversion fees. The funds will be deposited into your bank account in USD, which will be reflected on your Braintree statement. The reconciliation process doesn’t differ from what we have outlined above: you can compare the Disbursement Details—which can be found on the second page of your Braintree statement—to the deposits you see in your bank account.

The exchange rate is determined at the time the transaction is [authorized](/braintree/articles/get-started/transaction-lifecycle#authorized) and applied when the transaction is disbursed. As a result, transactions within a single disbursement may have varying exchange rates. You can find the individual exchange rate for each transaction. To do this:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click the**Download**button at the top of the page
- Open the CSV file in the spreadsheet program of your choice

The exchange rate for any given transaction will be listed in the Settlement Currency Exchange Rate column.

