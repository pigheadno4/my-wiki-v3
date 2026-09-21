<!-- Source URL: https://developer.paypal.com/braintree/articles/moneris/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/moneris/transactions/settlement-funding-timeline/
createTime: '2025-04-01T22:43:55.837Z'
updateTime: '2025-04-01T22:43:55.851Z'
---



# Settlement and Funding Timeline

After a transaction is settled, funds will pass through your merchant account to be paid out into your business bank account.


## Credit cards


### Settlement

Credit card transactions are divided into settlement batches and sent to the processing bank to confirm settlement. The cutoff time that determines which transactions are included in each settlement batch depends on your account setup and can't be changed. Any transactions submitted for settlement after the 8pm cut-off time will be included in the next day’s settlement batch.

Once Moneris receives confirmation that a transaction has successfully settled, your funds are ready for payout. You should see the funds deposited in your bank account based on the following schedule:


- **Visa/Mastercard**: 1-3 business days after transaction has settled
- **American Express**: 2-8 business days after transaction has settled*

*In our experience, Amex transactions are disbursed according to this schedule. Because Amex sets their own settlement batch cutoff times and handles your disbursements directly, you’ll need to contact them for details.


### Funding

Funding is issued by Moneris. While descriptors can look different depending on the bank your account is with, the descriptor for the deposits in your bank account should look similar to one of these two options:


- VSA DEP
- MC DEP

Depending on your bank, you’ll typically see the funds reflected in your account within 2 to 5 business days of the transaction settlement date.

By default, funds are paid out every weekday, excluding bank holidays. On weekends and bank holidays, funds will be sent to your bank account the following business day – it typically takes an additional business day before you see the funds in your account.


## Apple Pay

All Apple Pay transactions will be processed and paid out alongside your Amex credit card transactions. For questions on American Express disbursement timelines, you’ll need to contact Amex directly.


## PayPal

PayPal manages the disbursement of funds separately from your Braintree-managed account and there are [different funding options available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

