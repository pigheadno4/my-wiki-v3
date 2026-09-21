<!-- Source URL: https://developer.paypal.com/braintree/articles/au/statements -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Statements
slug: /articles/au/statements/
createTime: '2025-04-01T22:51:52.156Z'
updateTime: '2025-04-01T22:51:52.175Z'
---



# Statements

Your monthly merchant statement is your best tool for [reconciliation](/braintree/articles/au/reconciliation). The statement includes the following details:


- A summary page
- Detailed breakdowns of your:
- Disbursements
- Refunds
- Chargebacks
- Fees


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

The Disbursement Summary section of your statement is a quick way to view your gross sales along with any refunds, credits, or fees, as well as the net amount that was disbursed to your bank account for that statement period.


### Processing Snapshot

The Processing Snapshot shows the total volume of transactions, chargebacks, and refunds you processed. It also shows your average transaction amount and allows you to celebrate your best day of gross sales for that period.


### Braintree Fee Details

The Braintree Fee Details section outlines the fees and credits applied to your account in a detailed table with the following columns:


- Type: The type of fee or credit applied
- Quantity: The number of fees or credits that were created in the statement period
- Total Billed: The number of fees or credits that were billed to your account in the statement period
- Cost: The total amount credited or debited from your account, based on the value listed in theTotal Billedcolumn

The values in the Quantity and Total Billed columns will not always match, especially for [billable event fees](#billable-event-fees). There can be a delay between when a fee is created and when it is billed (applied) to your account. [Learn more about how to reconcile this table with your Transaction-Level Fee report.](/braintree/articles/au/reconciliation#braintree-fee-details)


#### Fee types

The types of Braintree fees – or credited fees – applied to your account fall into two categories: transaction fees and billable event fees.


##### Transaction fees

Transaction fees are the fees – or credited fees – that are applied to individual settled transactions:


- Merchant Service Fee: The[merchant service fee rate](/braintree/articles/au/pricing-fees)applied to each card transaction
- Per Transaction Fee: The[per transaction fee](/braintree/articles/au/pricing-fees)assessed on all transactions, regardless of card type
- Per Transaction Fee Credits: The[per transaction fees](/braintree/articles/au/pricing-fees)returned to you (if applicable) for refunded transactions, regardless of card type


##### Billable event fees

Billable event fees are charged for individual billable events:


- Authorization Fees: The authorization fee applied to each two-step authorization;[learn more about authorization types](/braintree/articles/au/reconciliation#authorizations)
- Decline Fees: The decline fee applied to each declined transaction
- Verification Fees: The verification fee applied to each card verification attempt
- Refund Fees: The refund fee applied to each refunded transaction


**NOTE**
 A single transaction can incur more than one billable event fee. For example, a card transaction that went through verification and was later refunded will be charged both a verification fee and a refund fee.

 


### Pricing Schedule

The Pricing Schedule identifies the [pricing model](/braintree/articles/au/pricing-fees) for your merchant account, merchant service fee, per transaction fee, billable event fees, and chargeback fee.


## Goods and Services Tax (GST) Details

The Goods and Services Tax (GST) is a 10% tax on most goods and services consumed in Australia. This tax is assessed on the total Braintree fees – and pass-through fees if you're on an IC ++ pricing model – that were applied during the statement period.

The Goods and Services Tax (GST) Details section outlines both the fee amount used to calculate this tax and the tax amount itself. Your GST amount is included in the **Total Fees** value at the top of your statement.


## Disbursement Details

The Disbursement Details section lists your daily disbursement amounts, organized by the dates when we disbursed the funds to your bank. This section incorporates all the transactions in each disbursement amount, along with gross sales, chargeback credit and debit amounts, and transaction refund amounts.


## Refund Details

The Refund Details section lists the number of refunds issued per day, along with the amounts credited (if any) for the refunded amounts.


## Chargeback Details

This section provides more information on the chargebacks you won or lost, such as the number of chargebacks and the total amount of money collected for chargebacks, including fees.


## Kount Fee Details

The Kount Fee Details section outlines the date, number of Kount requests, and total Kount fees you accrued throughout the month. Depending on your pricing setup, your statement may not include this section.


## Cost of Acceptance Details

The Cost of Acceptance (COA) Details calculates the average cost you incurred by processing transactions of each card type. You can then use this COA calculation to determine the maximum amount you can surcharge your customers for card transactions. Learn more information about surcharging regulations on the [Reserve Bank of Australia’s website](http://www.rba.gov.au/payments-and-infrastructure/review-of-card-payments-regulation/q-and-a/card-payments-regulation-qa-conclusions-paper.html).

