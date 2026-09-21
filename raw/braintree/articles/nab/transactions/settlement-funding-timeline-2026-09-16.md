<!-- Source URL: https://developer.paypal.com/braintree/articles/nab/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/nab/transactions/settlement-funding-timeline/
createTime: '2025-04-01T22:43:41.514Z'
updateTime: '2025-04-01T22:43:41.534Z'
---



# Settlement and Funding Timeline

After a transaction is settled, funds will pass through your merchant account for disbursement into your business bank account.


## Credit cards

Credit card transactions are divided into settlement batches and sent to the processing bank to confirm settlement. The settlement batch cut-off time for your account is 9:55pm AET, and can't be changed. Any transactions submitted for settlement after that time will be included in the next day’s settlement batch.

Once we receive confirmation from the processor that a transaction has successfully settled, your funds are ready for disbursement. If your business bank account is also with NAB, you should see the funds deposited in your bank account based on the following schedule:


- **Visa/Mastercard**: 1-3 business days after transaction has been submitted for settlement
- **American Express**: 2-8 business days after transaction has been submitted for settlement*

*In our experience, Amex transactions are disbursed according to this schedule. Because Amex sets their own settlement batch cutoff times and handles your disbursements directly, you’ll need to contact them for details.

If your business bank account is through a different banking institution, there may be an additional delay to the schedule we’ve outlined. You’ll want to check with your bank for details.


### A special note on card verification

If you have enabled our [card verification](/braintree/articles/control-panel/vault/card-verification) feature, the Braintree gateway will verify all cards with $1 authorizations. If you choose to verify cards on an individual basis, make sure to run $1 authorizations; $0 authorization attempts will trigger a [validation error](/braintree/docs/reference/general/validation-errors/all#code-91741).


## Apple Pay and Google Pay

All [Apple Pay and Google Pay](/braintree/articles/nab/transactions/accepted-payment-methods#alternative-payment-methods) transactions funded by American Express cards will be processed and disbursed alongside your regular Amex transactions.


## PayPal

PayPal manages the disbursement of funds separately from your Braintree-managed account and there are [different funding options available](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).

