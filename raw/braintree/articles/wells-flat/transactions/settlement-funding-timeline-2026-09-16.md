<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/wells-flat/transactions/settlement-funding-timeline/
createTime: '2025-04-01T23:05:34.585Z'
updateTime: '2025-04-01T23:05:34.611Z'
---



# Settlement and Funding Timeline

After a transaction is settled, funds will pass through your merchant account to your bank account. Because you are using Braintree Direct, we manage funding for you. If you have questions about or issues with your funding, [Contact us](/braintree/help/Reconciling).


## Credit cards


**NOTE**
 The following information applies to all credit cards except American Express. [Learn more about settlement and funding for Amex transactions.](#american-express)

 

Credit card transactions are divided into settlement batches and sent to the processor several times a day to confirm settlement. Transactions submitted for settlement after 5pm CT (US) will be included in the next day's settlements.

Once we receive confirmation from the processor that a transaction has successfully settled, we will disburse the funds to your account. You should see the funds deposited in your bank account 2 business days after the associated transactions have settled.

Funds are disbursed every weekday, excluding bank holidays, in which case they're sent the next business day.


### American Express

American Express transactions are divided into settlement batches separate from other credit card transactions. If you're using our Braintree aggregated American Express setup, the final settlement batch is sent to the processor at 4PM CT (US) each day; any transactions submitted for settlement after this time will be included in the next day's settlements. You should see the funds from these transactions disbursed into your account within 2-5 business days.


**NOTE**
 The 4PM settlement batch cutoff time is not impacted by daylight savings time. As such, between first Sunday in November and the second Sunday in March, the final settlement batch will actually run at 3PM CT (US).

 

If you have your own account through Amex and are not using our Braintree aggregated Amex setup, these transactions will be funded and deposited by Amex directly. Because Amex sets their own settlement batch cutoff times and handles your disbursements in this case, you’ll need to contact them with any questions.


### Special note on gateway-only accounts

If your [merchant account](/braintree/articles/get-started/overview#merchant-account) is through another provider and you only use the Braintree gateway for processing, you'll have one settlement batch per day with a cut-off time of 6am CDT/CST (US). [Contact us](/braintree/help) if you're unsure whether or not you are gateway-only.


### Disbursement Information

You can view disbursement details for a settled transaction in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Disbursement Information**section to view the**Disbursement Date**and**Settlement Amount**

Keep in mind, the disbursement date represents the date that the money was sent to your bank account and won’t necessarily align with the date that the funds appear in your bank account. Learn how to [reconcile these deposits](/braintree/articles/wells-flat/statements-reconciliation).


## Apple Pay and Google Pay

All Apple Pay and Google Pay transactions will be processed and disbursed alongside your credit card transactions.


## PayPal

PayPal manages the disbursement of funds separately from your Braintree-managed account, and [different funding options are available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

