<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-bf/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/aib-bf/transactions/settlement-funding-timeline/
createTime: '2025-04-02T00:57:22.972Z'
updateTime: '2025-04-02T00:57:22.987Z'
---



# Settlement and Funding Timeline


## Credit cards


**NOTE**
 The following information applies to all credit cards except American Express. [Learn more about settlement and funding for Amex transactions.](#american-express)

 

Credit card transactions are divided into settlement batches and sent to the processing bank to confirm settlement. The settlement batch cut-off time for your account is 6pm Central Time (US), and can't be changed. Any transactions submitted for settlement after that time will be included in the next settlement batch.

Once a transaction has successfully settled, we will disburse the funds to your account. You should see the funds deposited in your bank account 2-3 business days after the associated transactions have settled.

By default, funds are paid out every weekday, excluding bank holidays. On weekends and bank holidays, funds will be sent to your bank account the following business day.


### American Express

American Express transactions are divided into settlement batches separate from other credit card transactions. If you're using our Braintree aggregated American Express setup, the final settlement batch is sent to the processor at 4PM Central Time (US) each day; any transactions submitted for settlement after this time will be included in the next day's settlements. You should see the funds from these transactions disbursed into your account within 2-8 business days.


**NOTE**
 The 4PM settlement batch cutoff time is not impacted by daylight savings time. As such, between the second Sunday in March and the first Sunday in November, the final settlement batch will actually run at 3PM Central Time (US).

 

If you have your own account through Amex and are not using our Braintree aggregated Amex setup, these transactions will be funded and deposited by Amex directly. Because Amex sets their own settlement batch cutoff times and handles your disbursements in this case, you’ll need to contact them with any questions.


### Payout information

You can view the payout details for a settled transaction in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Disbursement Information**section to view the Disbursement Date and Settlement Amount

Keep in mind, the Disbursement Date in the Control Panel represents the date that the money was paid out to your bank account; it typically takes an additional business day before you see the funds in your account.


## Apple Pay and Google Pay

All [Apple Pay and Google Pay](/braintree/articles/aib-bf/transactions/accepted-payment-methods#alternative-payment-methods) transactions will be processed and disbursed alongside your credit card transactions.


## PayPal

PayPal manages the disbursement of funds separately from your Braintree-managed account and there are [different funding options available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

