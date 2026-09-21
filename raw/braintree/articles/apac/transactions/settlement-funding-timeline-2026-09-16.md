<!-- Source URL: https://developer.paypal.com/braintree/articles/apac/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/apac/transactions/settlement-funding-timeline/
createTime: '2025-04-02T01:57:21.516Z'
updateTime: '2025-04-02T01:57:21.533Z'
---



# Settlement and Funding Timeline

After a transaction is settled, funds will pass through your merchant account to your bank account. Because you are using Braintree Direct, we service funding for you. If you have questions about or issues with your funding, [Contact us](/braintree/help/Reconciling).


## Credit cards


### Settlement

Transactions are currently submitted for settlement at 3am Central Time (US). Once the settlement batch is submitted, we mark the transactions as Settling. We then send the batch of transactions to the processing bank, which initiates the transfer of funds and generates a settlement acknowledgment report. When we receive this settlement confirmation, we mark the transactions as Settled and disburse them to your bank account. You should see the funds deposited in your bank account based on the following schedule:


- **Visa/Mastercard**: 1-3 business days after transaction has been submitted for settlement
- [**American Express**](/braintree/articles/apac/transactions/accepted-payment-methods#american-express): 2-8 business days after transaction has been submitted for settlement*

*In our experience, Amex transactions are disbursed according to this schedule. Because Amex sets their own settlement batch cutoff times and handles your disbursements directly, you’ll need to contact them for details.


### Funding

The funding descriptor on your deposits will look like this:

GIRO MISCELLANEOUS MISC C/A - SCB CARD STS PYT

Depending on your bank, you’ll typically see the funds reflected in your account within 2-5 business days of the transaction creation date.

By default, funds are disbursed every weekday, excluding bank holidays. On weekends and bank holidays, funds will be sent to your bank account the following business day. It typically takes an additional business day before you see the funds in your account.


## Apple Pay and Google Pay

All [Apple Pay and Google Pay](/braintree/articles/apac/transactions/accepted-payment-methods#alternative-payment-methods) transactions will be processed and disbursed alongside your credit card transactions.


## PayPal

PayPal manages the disbursement of funds separately from your Braintree-managed account and there are [different funding options available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

