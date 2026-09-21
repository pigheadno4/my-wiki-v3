<!-- Source URL: https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/statements -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Statements
slug: /articles/br/reporting-reconciliation/statements/
createTime: '2025-04-02T00:51:47.393Z'
updateTime: '2025-04-02T00:51:47.416Z'
---



# Statements

Your monthly merchant statement is your best tool for [reconciliation](/braintree/articles/br/reporting-reconciliation/reconciliation). The statement includes the following details:


- A summary page
- Detailed breakdowns of your:
- Fees
- Disbursements
- Refunds
- Chargebacks


- A key for important terms and column headers

In this article, we provide instructions on how to locate your statement in the Control Panel, along with a breakdown of each of the sections it contains.


## Locating your statement

Users with the View Statements [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-view-statements) can access monthly merchant statements in the Control Panel. To access your statements:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Statements**tab


## Statement summary page

The statement summary page includes information about your disbursements, processing, and fees from the past month. We've outlined what to expect in each section below; have your statement available for reference when reading this guide.


### Disbursement Summary

The Disbursement Summary section of your statement is a quick way to view your gross sales along with any refunds, credits, or fees, as well as the net amount that was disbursed to your PayPal account for that statement period.


### Processing Snapshot

The Processing Snapshot shows the total volume of transactions, chargebacks, and refunds you processed. It also shows your average transaction amount and allows you to celebrate your best day of gross sales for that period.


### Braintree Fee Details

The Braintree Fee Details section outlines the fees and credits applied to your account in a detailed table with the following columns:


- Type: The type of fee or credit applied
- Quantity: The number of fees or credits that were created in the statement period
- Cost: The amount credited or debited from your account in the statement period


##### Transaction fees

Transaction fees are the fees – or credited fees – that are applied to individual settled transactions:


- Discount: The percentage rate fee charged on your gross sales amount
- Per Transaction Fee: The flat per-transaction fee charged on all sales transactions
- Per Transaction Fee Credits: The quantity and total amount of transaction fees returned for full transaction refunds within the billing period


##### Pricing Schedule

The Pricing Schedule identifies the brand, credit/debit type, discount rate fee, per transaction fee, and chargeback fee.


## Disbursement Details

The Disbursement Details section lists your daily disbursement amounts, organized by the dates when we disbursed the funds to your PayPal account, which are then swept into your bank. This section incorporates all the transactions in each disbursement amount, along with gross sales, chargeback credit and debit amounts, and transaction refund amounts.


**NOTE**
 The Disbursement Date that you see in the [Disbursement Report](/braintree/articles/br/reporting-reconciliation/disbursement-report) is the date PayPal makes the payout to your bank account, and will be at least one day later than the Disbursement Date you see in the Braintree **Disbursement Details** section of your **Statement**.

 


### Refund Details

The Refund Details section lists the number of refunds issued per day, along with the amounts credited (if any) for the refunded amounts.


### Chargeback Details

This section provides more information on the chargebacks you won or lost, such as the number of chargebacks and the total amount of money collected for chargebacks, including fees.


## Pricing and fees


### Transaction fees


**NOTE**
 Braintree will not charge any fees for PayPal transactions; only [PayPal's processing fees](https://www.paypal.com/webapps/mpp/merchant-fees) apply.

 

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Fees can be broken down into the following categories:


- Discount rate: Percentage we take from each transaction
- Per transaction fee: Static dollar amount deducted from each transaction
- Braintree processing fees: Discount rate and per transaction fees, combined
- Chargeback fee: Fixed fee charged by the processing bank that manages the chargeback

Braintree’s processing fees are only applied to successful transactions and are deducted from your daily disbursements. Verifications, declines, gateway rejections, and voids will not incur fees.


#### Braintree processing fee rates

We do not display your processing fees in the Control Panel, but you can find your processing fee rates in the Pricing Schedule on your statements. To access your statements:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the top navigation
- Click the**Statements**tab
- Click the**View Statement**button located to the right of Merchant Statements
- Open any statement for the merchant account you'd like to view your processing fee rates for by clicking the PDF link

Within the Pricing Schedule section of your statement, you'll find your fee rates for discount, per-transaction, and chargeback fees.


#### Transaction-level fees

If you would like to view the Braintree fees assessed at the transaction level, you can run a [Transaction-Level Fee report](/braintree/articles/control-panel/reporting/transaction-level-fee-report). This report is also helpful for [reconciliation](/braintree/articles/br/reporting-reconciliation/reconciliation).


#### Rounding down

When calculating fees, we round down if there is a remainder value past the penny. These are calculated on the transaction level, so if you manually multiply your fees by the total settled sales for a given month, there may be a slight discrepancy between the calculated value and the fee details listed on your statement.

As a result of rounding down, we often charge slightly less than your discount rate!


### Refunds

You will not be charged any additional fees to issue refunds or credits.

Depending on the date you began processing with Braintree, we may credit back the Braintree processing fees that we charged for a transaction in the event that it is fully refunded. [Contact us](/braintree/help/feeHelp) with any questions regarding your setup.


### Chargebacks, retrievals, and pre-arbitrations

The bank that manages the chargeback or pre-arbitration will charge a non-refundable fee. This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time. [More information on chargebacks](/braintree/articles/br/chargebacks-retrievals-prearbs).

