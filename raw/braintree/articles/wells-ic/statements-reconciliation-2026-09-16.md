<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-ic/statements-reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: IC+ Statements and Reconciliation
slug: /articles/wells-ic/statements-reconciliation/
createTime: '2025-04-02T00:51:53.426Z'
updateTime: '2025-05-16T12:13:39.972Z'
---



# IC+ Statements and Reconciliation


**NOTE**
 If you are using [Braintree Marketplace](/braintree/articles/guides/braintree-marketplace/overview), your statements will look different. See the [Braintree Marketplace statements and reconciliation guide](/braintree/articles/wells-ic/braintree-marketplace-statements-reconciliation) to learn more.

 


## Statements

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

The Disbursement Summary section of your statement is a quick way to view your gross sales along with any refunds, credits, or fees. It also displays the net amount that you received that month, which is referred to as the Net Disbursed.


#### Processing Snapshot

The Processing Snapshot shows the number of transactions, chargebacks, and refunds you processed. It also shows your average transaction amount and allows you to celebrate your best day of gross sales for that period.


#### Fee Details

With the IC+ pricing model, you’ll be charged two sets of fees—the interchange fees that come directly from the card associations (also referred to as pass-through fees), and Braintree fees. The details of these fees are broken out into sections on your statement’s summary page.

Both your interchange fees and Braintree fees will be debited on the third business day of the following month in two separate withdrawals. [Learn more about the different types of fees.](/braintree/articles/wells-ic/pricing-fees)


##### Braintree Fee Details

The Braintree Fee Details section breaks down the different fees that were charged to your account and identifies the quantity for each. You’ll also find any credits to your account for full refunds, chargebacks you have won, and promotions that were applied to your fee calculations.

If you are using Braintree’s aggregated Amex account:
- TheDiscountrow will display the total volume of Visa, Mastercard, JCB, and Discover transactions, along with the Braintree fees that were applied based on your[discount rate](/braintree/articles/wells-ic/pricing-fees#braintree-processing-fees)
- TheAmerican Express Discountrow will display the total volume of Amex transactions along with the discount rate fees
- The sum of the quantities in theDiscountandAmerican Express Discountrows should be equal to yourGross Salesfound in the Disbursement Summary
- ThePer Transaction Feerow will display the total number of all transactions, regardless of card type, along with the[per transaction fee](/braintree/articles/wells-ic/pricing-fees#braintree-processing-fees)that was assessed for those transactions
- TheKount Feesrow will display the total number of Kount inquiries and the amount charged – it will not show for merchants who negotiated Kount costs as a part of their per transaction fees

If you are using your own Amex account:
- TheDiscountrow will display the total volume of Visa, Mastercard, JCB, and Discover transactions, along with the Braintree fees that were applied based on your[discount rate](/braintree/articles/wells-ic/pricing-fees#braintree-processing-fees)
- ThePer Transaction Feerow will include Visa, Mastercard, JCB, and Discover transactions, along with the associated fees
- TheAmerican Express Transaction Feerow will include Amex transactions, along with the associated Braintree fees; for information on the additional fees that Amex charges you, you’ll need to contact them directly
- TheKount Feesrow will display the total number of Kount inquiries and the amount charged – it will not show for merchants who negotiated Kount costs as a part of their per transaction fees


##### Pass-Through Fee Details

Interchange fees encompass all of the various processing fees set by Visa, Mastercard, Amex and Discover. We pass these fees on directly to you, which is why we refer to them as pass-through fees.

This section of the statement displays total volume by card type and the associated interchange fees. These fees are consolidated on your statement, but actually represent various smaller fees. The breakdown of each specific fee will be available by the end of the third business day of the following month in the Pass-Through Fee Report, which can be found in the Control Panel. To access the Pass-Through Fee Report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Statements**tab
- Select the**Pass-Through Fee Report**for the desired month

Interchange fees are billed based on when the transaction [settled](/braintree/articles/get-started/transaction-lifecycle#settled), while Braintree fees are billed based on when the transaction was **disbursed**. As a result, the total sales volume that you see in this section does not align with the Gross Sales in the Disbursement Summary on your statement.


##### Kount Fee Details

If your Kount fees are charged per Kount request, your statement will include a Kount Fee Details section. This section outlines the date, number of Kount requests, and total amount debited. If your Kount fees are included in your per transaction fee rate, your statement will not include this section.


#### Pricing Schedule

The Pricing Schedule identifies the [Braintree processing fees](/braintree/articles/wells-ic/pricing-fees#braintree-processing-fees) for your merchant account. This includes the discount rate and the per transaction fee, as well as the [chargeback fee](/braintree/articles/wells-ic/pricing-fees#chargebacks,-retrievals,-and-pre-arbitrations). Interchange fees are not included in this section.


## Reconciliation


### Disbursement Details

Most of our merchants reconcile by comparing the Disbursement Details—which can be found on the second page of your Braintree statement—to the deposits they see in their bank accounts. In this section of your statement, the Date column reflects when we **disbursed** the funds to your bank. These funds should be reflected on your bank statement within 1-2 business days of the disbursement date. The Total Disbursed column will match the deposit you see on your bank statement.

If you are using Braintree’s aggregated Amex account, the Total Disbursed value will include Visa, Mastercard, Discover, JCB, and Amex transactions.

If you have your own Amex account, Amex handles the disbursements directly. As a result, the funds from your Amex transactions will not be included in the Total Disbursed amount found on your Braintree statement.


### Disbursement Summary report

If you would like to see transactions from a particular day’s disbursement, or your gross sales and credits grouped by card type, you can use the Disbursement Summary in the Control Panel.

Only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Disbursement Summary. To run this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Disbursement Summary**, click the**Run Report**button
- Select the desired merchant account and date range
- Click the**Run Disbursement Summary**button
- To download a report that shows you the totals for each day grouped by card type, click the**Download .Csv**button
- To see all transactions from a specific day, click the**View Transactions**link next to the desired day




**NOTE**
 The Disbursement Summary does not include transaction fees and will not display Amex transactions for merchants with their own Amex account.

 


### Dispute Report

You can reconcile disputes with your Braintree statement by using the Disbursement Date column of the [Disputes Financial Impact Report](/braintree/articles/wells-ic/chargebacks-retrievals-prearbs#dispute-reports). Here you will find the exact date that disbursed funds were credited or debited from your account.


### Transaction search

If you would like to review transactions that were disbursed across multiple days, it is best to search for the transactions. To do this:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Above the date section, uncheck the box next toCreation date range
- Check the box next toDisbursed date range
- Select your desired date range
- Click the**Search**button

[Contact us](/braintree/help/Reconciling) if you have any questions about this process.


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

