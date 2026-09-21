<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-af/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/aib-af/transactions/settlement-funding-timeline/
createTime: '2025-04-01T22:39:35.947Z'
updateTime: '2025-04-01T22:39:35.965Z'
---



# Settlement and Funding Timeline

After a transaction is settled, funds will pass through your merchant account to your bank account.


## Credit cards


**NOTE**
 {" "} There is an additional delay of 10 business days before you will see your first deposit. After your first deposit, the regular funding schedule outlined below will apply.

 

Credit card transactions are divided into settlement batches and sent to the processing bank to confirm settlement. The settlement batch cut-off time for your account is 6pm Central Time (US), and can't be changed. Any transactions submitted for settlement after that time will be included in the next settlement batch.

Once a transaction has successfully settled, AIB will disburse the funds to your account. You should see the funds deposited in your bank account based on the following schedule:


- **Visa/Mastercard/Discover/Maestro**: 2-3 business days after transaction has settled
- **American Express**: 2-8 business days after transaction has settled*

*In our experience, Amex transactions are disbursed according to this schedule. Because Amex sets their own settlement batch cutoff times and handles your disbursements directly, you’ll need to contact them for details.

By default, funds are disbursed every weekday, excluding bank holidays. On weekends and bank holidays, funds will be sent to your bank account the following business day. It typically takes an additional business day before you see the funds in your account.

We also offer the ability to disburse funds weekly or monthly instead of daily. [Contact us](/braintree/help) to set up a custom funding schedule.


## Apple Pay and Google Pay

All [Apple Pay and Google Pay](/braintree/articles/aib-af/transactions/accepted-payment-methods#alternative-payment-methods) transactions will be processed and disbursed alongside your credit card transactions.


## PayPal

PayPal manages the disbursement of funds separately from your Braintree-managed account and there are [different funding options available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

