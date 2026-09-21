<!-- Source URL: https://developer.paypal.com/braintree/articles/nab/statements-reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Statements and Reconciliation
slug: /articles/nab/statements-reconciliation/
createTime: '2025-04-02T01:33:23.486Z'
updateTime: '2025-05-19T08:29:30.190Z'
---



# Statements and Reconciliation


## Statements

NAB generates two monthly statements: the **Transact Statement**, which provides information on your per transaction fee processing, and the **Merchant Statement**, which covers all other merchant service and interchange fees.

NAB Merchant Statements are made available in the Control Panel by the 9th of each month. To access your statements:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Statements**tab

If you are unable to access or do not see the **Reports** page in the navigation bar, you'll want to make sure that your user's role has the View Statements [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-view-statements) enabled.


**NOTE**
 Transact Statements are not currently provided in the Control Panel. [Contact us](/braintree/help/Reconciling) if you need access to a Transact Statement.

 


### Merchant Statements

Keep in mind, some of the following sections may or may not be included in your Merchant Statement, depending on your [pricing model](/braintree/articles/nab/pricing-fees#pricing-models).


#### Fee settlement summary

This section lists the total amount of fees you were charged for that month, including any Goods and Services Tax (GST).


#### Transaction fees and charges

If you’re on the IC+ pricing model, this section will have breakdowns for the service fees organized by card brand, as well as the total amount charged in Card Issuer Fees.

If you have the blended pricing model, you’ll see the total value of transactions processed, your standard service fee pricing rate, and then the total amount charged based on that rate, including GST.


#### Credit card interchange category

This section only applies to those on the IC+ pricing model. Here, you’ll find a breakdown of the card issuer fees listed in the [Transaction fees & charges](#transaction-fees-and-charges) section. Each fee is broken down by its interchange category, and includes the number of transactions, the total value of the transactions charged, the pricing rate for that fee, and the total amount debited.

The total of this section should be equal to the Card Issuer Fees row found in the Transaction fees & charges section.


#### Daily transaction settlement summary

The monthly trend compares your net sales for each day that month. This gives you an idea of how many sales you processed on each given day throughout the month. The days are based off of the transaction settlement time. If you use a bank other than NAB for your business banking account you’ll want to keep the settlement delay in mind when looking at these.


#### Monthly trend

The monthly trend allows you to compare your net sales — both the number of transactions and the total dollar amount — for each month.


#### Card product summary

This section categorizes your transaction count and total sales by card type. It also takes into consideration refunds, reversals, and deposits.


#### Store summary

If you have multiple [merchant account IDs](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id), this section will give you a breakdown of the number of transactions as well as your net sales for each ID.


## Reconciliation

The best way to reconcile your debits and deposits is to compare the [Settlement Batch Summary Report](/braintree/articles/control-panel/reporting/settlement-batch-summary#running-a-settlement-batch-summary) — which is generated daily — with your bank statements.

The Settlement Batch Summary Report is organized by settlement date. If you use NAB for your business banking account, settled funds should be deposited the next day. If you use a different bank for your business account, there may be an additional delay between the settlement date and the day the corresponding deposit hits your account. You’ll want to keep this delay in mind when running the report.

Once you’ve downloaded the Settlement Batch Summary Report, you’ll be able to compare it to the deposits on your bank statement. Because your fees are debited at the end of the month, the deposits in your account are the gross transaction amount. This means that they should match the settlement batch exactly.


### Fee reconciliation

Fees are deducted on a monthly basis on the last business day of every month. This includes chargeback fees, merchant service and interchange percentages, and per transaction fees.

If you’d like to take a look at how much you paid in fees for a given month, you can find that information on your Merchant and Transact statements. To reconcile your fees, compare the fees assessed in your Merchant and Transact statements to the fee debit from your bank account each month.

If you are having trouble reconciling your account, [Contact us](/braintree/help/Reconciling) for assistance.

