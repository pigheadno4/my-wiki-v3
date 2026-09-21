<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-bf/statements-reporting -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Statements and Reporting
slug: /articles/aib-bf/statements-reporting/
createTime: '2025-04-02T00:15:34.275Z'
updateTime: '2025-04-02T00:15:34.293Z'
---



# Statements and Reporting


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


- A key for important terms and column headers


### Summary page

The summary page will include some or all of the sections outlined below. We recommend having your statement available for reference when reading this guide.


#### Disbursement Summary

The Disbursement Summary section of your statement is a quick way to view your gross sales along with any refunds, credits, or fees, as well as the net amount that was disbursed to your bank account for that statement period.


#### Processing Snapshot

The Processing Snapshot shows the number of transactions, chargebacks, and refunds you processed. It also shows your average transaction amount and allows you to celebrate your best day of gross sales for that period.


#### Braintree Fee Details

The Braintree Fee Details section breaks down the different fees that were charged to your account and identifies the quantity for each. You’ll also find any credits to your account for full refunds (if applicable), chargebacks you have won, and promotions that were applied to your fee calculations.


- **Discount***: Total volume of Visa, Mastercard, Maestro, and Discover transactions, along with the Braintree fees that were applied based on your[discount rate](/braintree/articles/aib-bf/pricing-fees)
- **Discount Credits**: Total volume of refunds for Visa, Mastercard, Maestro, and Discover transactions, along with the Braintree fees that were returned to you
- **Multi-Currency Fee**: Total volume of transactions affected by the multi-currency fee and the amount charged
- **American Express Discount***: Total volume of Amex transactions along with the discount rate fees
- **American Express Discount Credits**: Total volume of Amex refunds along with the Braintree fees that were returned to you
- **Per Transaction Fee**: Total number of all transactions, regardless of card type, along with the[per transaction fee](/braintree/articles/aib-bf/pricing-fees)that was assessed for those transactions
- **Per Transaction Fee Credits**: Total number of refund transactions, regardless of card type, along with the[per transaction fees](/braintree/articles/aib-bf/pricing-fees)that were returned to you (if applicable)
- **Kount Fees**: Total number of Kount inquiries and the amount charged – will not show for merchants who negotiated Kount costs as a part of their per transaction fees

* The sum of the quantities in the**Discount**and**American Express Discount**rows should be equal to your**Gross Sales**found in the [Disbursement Summary](#disbursement-summary).


**IMPORTANT**
 We do not account for value-added tax (VAT), so you won’t see it listed on your statement. Merchants are responsible for covering VAT independently.

 


#### Kount Fee Details

The Kount Fee Details outlines the date, number of Kount requests, and total Kount fees you accrued throughout the month. Depending on your pricing setup, your statement may not include this section.


#### Pricing Schedule

The Pricing Schedule identifies the [fee structure](/braintree/articles/aib-bf/pricing-fees) for your merchant account, which includes the discount rate, per transaction fee, and multi-currency fee (if applicable). It also displays the [chargeback fee](/braintree/articles/aib-bf/pricing-fees#chargebacks,-retrievals,-and-pre-arbitrations).


#### Promotion Usages

If you are enrolled in one of our promotional programs, this section will display the details of that promotion. It includes the name of the promotion, the processing limit, the amount you have accrued towards the limit, and—when applicable—the date that the limit was reached and the promotion was completed.


## Transaction Fee Report


**AVAILABILITY**
 Currently, this report cannot be retrieved through the API

 

The Transaction Fee Report will be available at the beginning of each month. Only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Transaction Fee Report in the Control Panel. To see the report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Statements**tab
- Under the**Merchant Statements**section, click the**View Statements**button
- Locate the appropriate merchant account, and click the**Transaction Fee Report**link next to the month you're interested in

Here are the columns that merchants most frequently have questions about when reviewing this report:


- **Settlement Amount**: The transaction amount before any fees are deducted
- **Interchange Amount**: The total monetary value of the various interchange fees, both static and percentages, that were assessed for the transaction
- **Scheme Amount**: The total monetary value of the various scheme fees, both static and percentages, that were assessed for the transaction
- **Total Fee Amount**: The total fees assessed on the transaction, including the Interchange Amount and all Braintree fees; does not include chargeback fees or scheme fees assessed for chargebacks

This report does not include chargebacks, chargeback fees, scheme fees assessed for chargebacks, refunds, or returned refund fees, so it isn’t designed exclusively for reconciliation purposes.


**NOTE**
 For merchants on the [blended pricing model](/braintree/articles/aib-bf/pricing-fees#blended), the interchange rate is incorporated into your fixed rate. We list interchange rates separately on your Transaction Fee Report for your general reference only.

 

