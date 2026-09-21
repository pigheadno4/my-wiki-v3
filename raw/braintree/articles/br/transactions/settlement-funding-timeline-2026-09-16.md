<!-- Source URL: https://developer.paypal.com/braintree/articles/br/transactions/settlement-funding-timeline -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement and Funding Timeline
slug: /articles/br/transactions/settlement-funding-timeline/
createTime: '2025-04-02T01:13:06.905Z'
updateTime: '2025-04-02T01:13:06.929Z'
---



# Settlement and Funding Timeline

After a transaction is settled, funds will pass through your linked PayPal Business Account before being swept to your bank account. Because you are using Braintree Direct, we manage funding for you. If you have questions about or issues with your funding, [Contact us](/braintree/help/Reconciling).


## Credit cards

Credit card transactions are divided into settlement batches and sent to the schemes to confirm the settlement. The final settlement batch cut-off time for your account is 10:45 pm CT, and can't be changed. Any transactions submitted for settlement after that time will be included in the next day’s settlement batch.

Once we receive confirmation from the processor that funds have successfully settled, we will disburse the funds to your account. Funds are first disbursed to your linked PayPal account and will be swept from the PayPal account to your bank account once per day.

You should see the funds deposited in your bank account 30-32 calendar days after the transaction has settled.


## Installment Transaction disbursements

For transactions paid in installments, you can expect to receive an evenly divided portion of these funds every 30 days over the number of installments associated with each transaction, beginning 30-32 calendar days after the transaction has settled. If a transaction is not equally divisible by the number of installments passed, you can expect this remainder to be paid in the final installment disbursement.


## Debit cards

When accepting debit cards, you can expect payments to be deposited into your PayPal account within 2 days. Debit card transactions are not eligible for installments.

Funds are disbursed to your bank account every weekday. In the event of a bank holiday, funds are disbursed the next business day.


## Disbursement information

You can view disbursement details for a settled transaction in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Disbursement Information**section to view the Disbursement Date and Settlement Amount

Keep in mind, the disbursement date represents the date that the money was sent to your bank account and won’t necessarily align with the date that the funds appear in your bank account. [Learn how to reconcile these deposits.](/braintree/articles/br/reporting-reconciliation/reconciliation#disbursement-summary-report)


## PayPal

PayPal manages disbursements separately from your Braintree account. [Learn more about PayPal funding](/braintree/articles/guides/payment-methods/paypal/funding-reconciliation).


## Refunds

When refunding a transaction that has already been disbursed, you can expect the refunded amount to be applied within the next 2 business days once it’s been settled.

If a transaction has not yet been disbursed, the refunded amount will be applied to the transaction pending disbursement.


### Installment Transaction Refunds

If a refund is issued on a transaction with installments, you can expect the following:


#### Refunds before funds have started disbursing

The amount refunded will be divided across the number of installments of the sale.

**Full refunds:** All installments will be adjusted to zero; you will not receive any funds for the refunded sale transaction.

**Partial refunds:** Each installment will be adjusted by the refund amount divided by the number of installments. You will receive funds for the remaining un-refunded amount of each installment according to your installments schedule.


#### Refunds after funds have started disbursing

Just as with refunds that occur before funds have disbursed, the amount refunded for these installments will be divided across the number of installments of the sale.

**Full refunds:** Adjustments for any installments that have already been disbursed will be debited within the next two business days. Future installments will be adjusted to zero; you will not receive any funds for upcoming disbursements.

**Partial refunds:** Refunds for less than the full amount of the transaction will create adjustments to each installment. The adjustment amount is the refund amount divided by the number of installments. You will receive funds for the remaining un-refunded amount of each installment according to your installments schedule.


#### Refunds after all funds have been disbursed

Once a transaction has been fully disbursed, the funds will be refunded as if it were a regular non-installment transaction. Since all installments have already been paid, the amount will be applied to your disbursement within the next two business days.

