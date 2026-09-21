<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/processing -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Processing
slug: /articles/guides/braintree-marketplace/processing/
createTime: '2025-04-02T00:13:27.812Z'
updateTime: '2025-04-02T00:13:27.830Z'
---



# Processing


**AVAILABILITY**
 If you're a new merchant looking for a marketplace solution, [contact our Sales team](mailto:sales@braintreepayments.com).

 


## Service fees

A service fee allows you to take a portion of your sub-merchant's transaction revenue and route those funds to your master merchant account. The remainder will be disbursed to your sub-merchant. You can specify a service fee when creating a transaction either [via the Control Panel](/braintree/articles/control-panel/transactions/create) or [via the API](/braintree/docs/guides/braintree-marketplace/create).

For example, let’s say you’ve created a $100 transaction for one of your sub-merchants. If you specify a $10 service fee, we’ll disburse $90 to the sub-merchant and $10 (less any Braintree transaction fees) to you.


**NOTE**
 If the Braintree transaction fee is greater than your service fee, we’ll first pull funds from the settled amount on your master merchant account; this amount includes all collected service fees and any income from transactions processed directly through your master merchant account. If these settled funds are not sufficient, we will then debit your bank account for the remaining balance.

 


## Escrow

Escrow allows you to withhold your sub-merchants’ disbursements and release them at a later date. This can help mitigate financial risks when a sub-merchant fails to deliver a service or product. For example, if a concert is canceled, holding funds in escrow guarantees that there will be money available to cover refunds to the sub-merchant's customers who purchased concert tickets.

You must indicate that you would like to hold funds in escrow [via the API](/braintree/docs/guides/braintree-marketplace/create#holding-funds-in-escrow) — either upon transaction creation, or anytime before submitting the transaction for settlement. We will hold the funds in escrow until you make an API call to release them.

When using escrow, you are required to hold and release entire transactions, including any service fees. If you need to break up transactions into partial disbursements (e.g. 50% immediately and 50% upon delivery of a product), you must create two separate transactions. When you [release funds from escrow](/braintree/docs/reference/request/transaction/release-from-escrow), disbursement will follow the [standard Braintree Marketplace funding timeline](/braintree/articles/guides/braintree-marketplace/funding#master-merchant-funding).


**NOTE**
 We recommend that you don’t hold funds in escrow for longer than 30 days. [Contact us](/braintree/help) for more information.

 


## Refunds

Refunds work a little differently depending on whether or not the funds are being held in escrow. If they are in escrow, the full amount of the transaction will be **pulled from escrow** and returned to the customer. Partial refunds are not supported until the funds are released from escrow.

If the funds are not in escrow, you can issue both full and partial refunds. Either way, the amount will be **deducted from your master merchant bank account**, not your sub-merchant’s funding source. For some suggestions on recouping these funds, [learn more about collecting funds from your sub-merchants](#collecting-funds-from-your-sub-merchants).


## Disputes

We will contact you if a [chargeback or retrieval](/braintree/articles/risk-and-security/chargebacks-retrievals/overview) is issued against one of your sub-merchant’s transactions. Funds for the chargeback, along with any associated fees, will be deducted from your master merchant bank account.


## Collecting funds from your sub-merchants

Because refunds and chargebacks pull funds from your bank account and not your sub-merchants’ funding sources, here are some ways you can recoup those funds:


- Increase your service fees to mitigate losses due to high refund or chargeback rates from sub-merchants.
- Build logic in your integration that increases a sub-merchant’s service fees until any refund or chargeback balance is paid off.
- Collect payment information from your sub-merchants and store it in your Vault. When your master merchant bank account is debited for a refund or chargeback, you can charge your sub-merchant’s payment method. Keep in mind that standard Braintree transaction fees will apply.

