<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/braintree-marketplace-statements-reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Braintree Marketplace Statements and Reconciliation
slug: /articles/wells-flat/braintree-marketplace-statements-reconciliation/
createTime: '2025-04-01T23:53:07.187Z'
updateTime: '2025-04-01T23:53:07.210Z'
---



# Braintree Marketplace Statements and Reconciliation


**NOTE**
 If you are not using [Braintree Marketplace](/braintree/articles/guides/braintree-marketplace/overview), your statements will look different. See [Statements and Reconciliation](/braintree/articles/wells-flat/statements-reconciliation) for the standard statements and reconciliation guide.

 


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
- Master merchant disbursement
- Escrow (if applicable)
- Refunds
- Chargebacks
- Sub-merchant disbursements


- A key for important terms and column headers


### Summary page

The summary page will include some or all of the sections outlined below.


#### Master Merchant Summary

The Master Merchant Summary section of your statement is a quick way to view your gross [service fees](/braintree/articles/guides/braintree-marketplace/processing#service-fees) along with any refunds, credits, or fees, and the net amount that was disbursed to your master merchant bank account for that statement period.


#### Braintree Fee Details

The Braintree Fee Details section breaks down the different fees that were charged to your account and identifies the quantity for each. You’ll also find any credits to your account for full refunds, chargebacks you have won, and promotions that were applied to your fee calculations.


- TheDiscountrow will display the total volume of Visa, Mastercard, JCB, and Discover transactions, along with the Braintree fees that were applied based on your discount rate
- TheAmerican Express Discountrow will display the total volume of Amex transactions along with the discount rate fees
- ThePer Transaction Feerow will display the total number of all transactions, regardless of card type, along with the per transaction fee that was assessed for those transactions


#### Pricing Schedule

The Pricing Schedule identifies the [fee structure](/braintree/articles/wells-flat/pricing-fees) for your merchant account, which includes the discount rate and the per transaction fee. It also displays the [chargeback fee](/braintree/articles/wells-flat/pricing-fees#chargebacks,-retrievals,-and-pre-arbitrations).


## Reconciliation

Most Braintree Marketplace merchants reconcile by comparing the Master Merchant Disbursement Details—which can be found on the second page of your Braintree statement—to the deposits they see in their bank accounts. If you’re looking for more granular information, you can reconcile down to the transaction by [calculating your own per transaction fees](#calculating-fees-on-a-transaction-level).

To help your individual sub-merchants reconcile, you should use the [Disbursement Summary or an advanced transaction search](#sub-merchant-reconciliation).

**IMPORTANT**
While the [Dashboard](/braintree/articles/control-panel/overview#dashboard) can be a helpful tool for quickly assessing processing activity in your account, it should not be used for reconciliation purposes.


### Master merchant reconciliation

The Master Merchant Disbursement Details—which can be found on the second page of your Braintree statement—displays the gross service fees that you collected from your sub-merchants. It calculates any refunds, chargebacks, or fee credits, along with Braintree’s fees, to determine the Total Disbursed to your master merchant bank account.

The Date column reflects when we disbursed the funds to your bank. These funds should be reflected on your bank statement within 1-2 business days of the disbursement date. The Total Disbursed column will match the deposit you see on your bank statement.


### Sub-merchant reconciliation

Your Braintree statement displays the total revenue for all sub-merchants, so you’ll need to use alternative tools in order to help an individual sub-merchant reconcile.

**NOTE**
Remember, sub-merchants don’t pay Braintree transaction fees, so they won’t need to take those into consideration when reconciling. Sub-merchants will receive the full amount of the gross sales less any [service fees](/braintree/articles/guides/braintree-marketplace/processing#service-fees) that you have designated.


#### For multiple sub-merchants

To help multiple sub-merchants reconcile, search for transactions filtered by disbursed date:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Choose either**All Sub-merchant Accounts**, or enter the desired sub-merchants
- Above the date section, uncheck the box next toCreation date range
- Check the box next toDisbursed date range
- Select your desired date range
- Click the**Search**button
- Click the**Download**button at the top of the page
- Open the CSV file in the spreadsheet program of your choice

From there, you can categorize the report by the Merchant Account and Disbursement Date. The Amount Submitted For Settlement minus the Service Fee will equal the amount that was disbursed to the sub-merchant for that transaction. If you add up the disbursed amounts for all of the transactions on a given disbursement date for a specific sub-merchant, this should match what that sub-merchant sees deposited into their bank account.


#### For a specific sub-merchant

To help a specific sub-merchant reconcile, use the Disbursement Summary and add your own service fees. Only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Disbursement Summary. To run this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Scroll to the**Transactions**section
- Next to**Disbursement Summary**, click the**Run Report**button
- Select the desired merchant account and date range
- Click the**Run Disbursement Summary**button
- Click the**Download .Csv**button at the top of the page
- Open the CSV file in the spreadsheet program of your choice

The report will be separated by card type so you’ll need to use the totals from each day. Service fees are not included in the Disbursement Summary so you will also need to add those to the spreadsheet, then subtract them from the values found in the Total Amount column. This calculated value should match what that sub-merchant sees deposited into their bank account.


### Calculating fees on a transaction level

You can calculate the Braintree fees for individual transactions using a transaction search:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Uncheck the box next toCreation date range
- Check the box next toDisbursed date range
- Select your desired date range
- Click the**Search**button
- Click the**Download**button at the top of the page
- Open the CSV file in the spreadsheet program of your choice

From here, you can create additional columns for your transaction fees.

To find your specific transaction fees, look at the [Pricing Schedule](#pricing-schedule) on your statement. Make sure to [round down](/braintree/articles/wells-flat/pricing-fees#rounding-down), and then apply the fees to your individual transactions.

To find the exact amount we disbursed to your master merchant bank account for each transaction, subtract the total Braintree fees you have calculated from the Service Fee.

[Contact us](/braintree/help/Reconciling) if you have any questions about this process.

