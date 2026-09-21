<!-- Source URL: https://developer.paypal.com/braintree/articles/br/payment-capabilities -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Payment Capabilities
slug: /articles/br/payment-capabilities/
createTime: '2025-04-02T02:08:58.088Z'
updateTime: '2025-04-02T02:08:58.101Z'
---



## Installments

In Brazil, Braintree and PayPal allow for merchants to accept payments from customers in the form of installments. When a customer opts to pay for a sale transaction in installments, the sale amount will be evenly divided by the number of installments selected by the customer from your checkout workflow. Braintree supports installment plans that span anywhere from two to twelve months.

When a customer opts to pay for a sale in installments, they will be debited once every 30 days for the installment amount. Likewise, you will also be paid the installment amount every 30 days until the full plan has been fulfilled.


### Installment Reporting

Tracking installment data can be difficult without reporting. PayPal and Braintree provide a series of reports that make it easy to track all installment lifecycle events:


- [Activity Report](/braintree/articles/br/reporting-reconciliation/activity-report)
- [Disbursement Report](/braintree/articles/br/reporting-reconciliation/disbursement-report)
- [Transaction Level Fee Report](/braintree/articles/br/reporting-reconciliation/transaction-level-fee-report)


### Installment Disbursements

Installment transaction disbursements are distributed evenly across the total number of installments associated with each transaction. Where the total transaction value does not divide evenly across the number of installments, the remainder is paid with the final installment. Learn more about disbursement behavior and reconciliation in [Settlement and Funding Timeline](/braintree/articles/br/transactions/settlement-funding-timeline).


### Creating and Managing Installment payments

In order to use installment payments, you will need to make some updates to your integrations when creating and managing transactions. Click the links below for more information about how to make these changes:


- [Creating Installment Transactions](/braintree/articles/br/transactions/installments#creating-installments)
- [Refunding Installment Transactions](/braintree/articles/br/transactions/installments#refunding-installments)
- [Searching for Installment Transactions](/braintree/articles/br/transactions/installments#getting-installment-details)


### Chargebacks, retrievals, and pre-arbitratition cases on installments

There are no changes to the process of finding and responding to disputes for Installment Transactions. Disputes continue to be assessed against a single transaction; customers cannot dispute an individual installment.

Debits and credits associated with disputes will be applied evenly across every installment associated with the disputed transaction. Use the [Disputes Financial Impact Report](/braintree/articles/br/chargebacks-retrievals-prearbs#disputes-financial-impact-report) to reconcile disputes financial activity with your statement.


## See also


- [Installments](/braintree/articles/br/transactions/installments)

