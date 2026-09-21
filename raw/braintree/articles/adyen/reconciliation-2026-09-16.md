<!-- Source URL: https://developer.paypal.com/braintree/articles/adyen/reconciliation -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reconciliation
slug: /articles/adyen/reconciliation/
createTime: '2025-04-01T22:50:39.385Z'
updateTime: '2025-04-01T22:50:39.401Z'
---



# Reconciliation

The Settlement Details Report is your best tool for reconciliation. Other tools such as the
Settlement Batch Summary Report are informative, but will not be as valuable to you during the
reconciliation process.The Settlement Details Report is generated upon payout and is only available for users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports). To run a Settlement Details Report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Settlement Details Report**, click the**Run Report**button

The Settlement Details Report will list all of the transactions included in that bank deposit and will specify the gross and net settlement amounts for captures, refunds, and (if present) chargebacks. Fee totals and deposit corrections are also specified, as well as the amount transferred to your bank account.

The Type column identifies the individual sections within your Settlement Details Report. Each type falls under one of the four categories below.


## Merchant Payout

The **Merchant Payout** section is in a row near the bottom of the report and is one of the most helpful line items for reconciling deposits. This will show you how much Adyen has sent to your bank account, along with Adyen’s reference number that will appear on your bank statement. The amount in the **Net Debit** column should match the deposit in your bank account.

The information listed in the **Modification Reference** field is an Adyen payout reference number that can be used to quickly align your batches with the deposits in your account.


## Transaction Fees

The **Transaction Fees** section lists the period over which the fees were assessed, the total amount of fees assessed for that payout, and the currency they were assessed in.


## Corrections


### Deposit Correction

In some cases, Adyen will hold some of your processed payments as a reserve of funds on your account. There will be a **Deposit Correction** line near the bottom of the Settlement Details Report if any funds were debited from or credited to your reserve amount.

The Deposit Correction can also indicate if your deposit amount was adjusted to cover any outstanding fees. For example, if you agreed to a 1000-transaction monthly minimum at €0,10 per transaction, but do not process 1000 transactions, you would incur fees on the difference. Those fees would then be deducted from your deposit amount, rather than debited from your bank account separately.


### Invoice Deduction

At the end of every month, Adyen calculates the final invoice. If they find that they have charged too much or too little (e.g. due to tier pricing), they will list an **Invoice Deduction** line in the Settlement Details Report. This amount can be either a debit – if you were undercharged – or a credit – if you were overcharged.


### Balance Transfer

Adyen can adjust the amount paid out to your bank account by transferring funds between settlement batches. When this happens, you will see a **Balancetransfer** line in your Settlement Details Report. [Contact us](/braintree/help/Reconciling) for more information.


## Transaction details

These line items will make up the majority of the report and will break down fee deductions per transaction. Transactions can be identified by one of three types:


- Settled
- Refunded
- Chargeback

Many of these fields are straightforward, but it’s worth noting the following:


#### Merchant Account

This field will identify which [merchant account ID](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id) (MID) the transaction was processed with. If you are processing with more than one MID, you will have a separate report for each one.


#### Psp Reference

This is Adyen’s unique identifier for the transaction. If you need to contact them with any transaction issues, they will be able to locate the transaction using this number.


#### Merchant Reference

This is Braintree’s transaction ID. You can use this number to [search for transaction details](/braintree/articles/control-panel/search) in our Control Panel.


#### Modification Reference

This is an internal reference number for Adyen.


#### Gross Currency

This will indicate the presentment currency for the transaction.


#### Gross Debit (GC)

This field lists the gross amount for refunded transactions. If the transaction type is listed as Settled or Chargeback, this field will be blank.


#### Gross Credit (GC)

This field lists the gross transaction amount in the currency it was presented in for Settled and Chargeback transaction types. If the transaction type is listed as Refunded, this field will be blank.


#### Exchange Rate

This field notes what the currency conversion rate was when the funds for the transaction were sent to your account. If the settlement and presentment currencies were the same, the value will be 1.


#### Net Currency

This reflects the settlement currency for the transaction.


#### Net Debit (NC)

This reflects the amount debited from your account for refunded transactions, minus the fees listed in the Commission (NC), Markup (NC), Scheme Fees (NC), and Interchange (NC) columns. If the transaction type is listed as Settled or Chargeback, this field will be blank.


#### Net Credit

This reflects the amount paid out to your account for transactions in your settlement currency, minus the fees listed in the Commission (NC), Markup (NC), Scheme Fees (NC), and Interchange (NC) columns. If the transaction type is listed as Refunded, this field will be blank.


#### Commission (NC)

Adyen or card associations may charge a commission on certain transactions. This can be either a fixed rate or percentage, and does not always apply. You are most likely to see a value in this field for American Express transactions.


#### Payment Method Variant

This field indicates the type or card brand of the provided payment method.

