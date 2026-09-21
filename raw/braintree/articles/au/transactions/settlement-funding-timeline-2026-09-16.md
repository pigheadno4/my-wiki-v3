<!-- Source URL: https://developer.paypal.com/braintree/articles/au/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/au/transactions/settlement-funding-timeline/
createTime: '2025-04-01T23:10:38.291Z'
updateTime: '2025-04-01T23:10:38.305Z'
---



# Settlement and Funding Timeline

After a transaction is settled, funds will pass through your merchant account to your bank account. Because you are using Braintree Direct, we manage funding for you. If you have questions about or issues with your funding, [Contact us](/braintree/help/Reconciling).


## Credit cards

Credit card transactions are divided into settlement batches and sent to the processor several times a day to confirm settlement. The final settlement batch cut-off time for your account is 8pm AET, and can't be changed. Any transactions submitted for settlement after that time will be included in the next day’s settlement batch.

Once we receive confirmation from the processor that a transaction has successfully settled, we will disburse the funds to your account. You should see the funds deposited in your bank account based on the following schedule:


- **Visa/Mastercard**: 1-3 business days after transaction has been submitted for settlement
- **American Express**: 2-8 business days after transaction has been submitted for settlement*

*In our experience, Amex transactions are typically disbursed according to this schedule. Because American Express sets their own settlement batch cutoff times and handles your disbursements directly, you'll need to contact them for details.


### Disbursement information

You can view disbursement details for a settled transaction in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Disbursement Information**section to view the Disbursement Date and Settlement Amount

Keep in mind, the disbursement date represents the date that the money was sent to your bank account and won’t necessarily align with the date that the funds appear in your bank account. [Learn how to reconcile these deposits.](/braintree/articles/au/reconciliation#disbursement-summary-report)


## Apple Pay and Google Pay

All Apple Pay and Google Pay transactions will be processed and disbursed alongside your credit card transactions.


## PayPal

PayPal manages the disbursement of funds separately from your other Braintree transactions, and [different funding options are available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

