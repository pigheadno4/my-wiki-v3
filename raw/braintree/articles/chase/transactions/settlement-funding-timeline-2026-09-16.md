<!-- Source URL: https://developer.paypal.com/braintree/articles/chase/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/chase/transactions/settlement-funding-timeline/
createTime: '2025-04-01T21:48:24.963Z'
updateTime: '2025-04-01T21:48:24.982Z'
---



# Settlement and Funding Timeline

After a transaction is settled, Chase will pass funds through your merchant account to your bank account. If you have questions about or issues with your funding, [Contact us](/braintree/help/Reconciling).


## Credit cards

Credit card transactions are divided into settlement batches and sent to the processor to confirm settlement. The cutoff time that determines which transactions are included in each settlement batch depends on your account setup and can't be changed. Any transactions submitted for settlement after a given cut-off time will be included in the next settlement batch.

Once Chase receives confirmation from the processor that a transaction has successfully settled, they will disburse the funds to your account. You should see the funds deposited in your bank account based on the following schedule:


- **Visa/Mastercard/Discover/Diners Club**: 2-3 business days after transaction has settled
- **American Express**: 2-5 business days after transaction has settled*

*In our experience, Amex transactions are disbursed according to this schedule. Because Amex sets their own settlement batch cutoff times and handles your disbursements directly, you’ll need to contact them for details.

The disbursement date for a specific transaction can be seen in [reporting](/braintree/articles/chase/reporting-reconciliation) via Chase Paymentech. Keep in mind, this represents the date that the money was sent to your bank account and won’t necessarily align with the date that the funds appear in your bank account. [Learn more about how to reconcile these deposits.](/braintree/articles/chase/reporting-reconciliation)


**NOTE**
 Funds are disbursed every weekday, excluding bank holidays, in which case they're sent the next business day.

 


## Apple Pay and Google Pay

All [Apple Pay and Google Pay](/braintree/articles/chase/transactions/accepted-payment-methods#alternative-payment-methods) transactions will be processed and disbursed alongside your credit card transactions.


## PayPal

PayPal manages the disbursement of funds separately from your Braintree-managed account, and [different funding options are available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

