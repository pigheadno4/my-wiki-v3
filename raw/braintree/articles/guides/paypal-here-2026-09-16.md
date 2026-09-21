<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/paypal-here -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: PayPal Here on Braintree
slug: /articles/guides/paypal-here/
createTime: '2025-04-01T23:11:51.602Z'
updateTime: '2025-04-01T23:11:51.619Z'
---



# PayPal Here on Braintree

If you accept in-store payments via [PayPal Here](https://us.paypal-here.com/), you can link your Braintree and PayPal Here integrations to view your in-store transactions in Braintree, right alongside your online Braintree transactions. In the US, you can also set up your PayPal Here integration to save in-store cards in the Braintree Vault.


## Fees

There is no additional cost to using PayPal Here on Braintree on top of standard [PayPal Here pricing](https://www.paypal.com/us/webapps/mpp/credit-card-reader).


## Compatibility

PayPal Here on Braintree is available to merchants in the US, UK, and Australia. Vaulting payment information from PayPal Here is only available in the US.


## Setup

PayPal Here is not enabled on your account by default. Follow these steps to [enable PayPal Here on Braintree](/braintree/docs/guides/paypal-here#onboarding).


## How it works

By enabling PayPal Here on Braintree, you can view and manage your in-store PayPal Here transactions via the Braintree Control Panel or API. These transactions are easily identifiable by a PayPal Here logo alongside the payment information.

The following will be visible for PayPal Here transactions in the Control Panel:


- Card Brand
- Last 4
- Reader method (swipe, chip, etc.)
- Transaction Fee
- Date Initiated
- Date Updated
- PayPal Sale ID
- PayPal Authorization ID
- PayPal Capture ID
- PayPal Refund ID
- PayPal Invoice ID
- Line item details

You will be able to submit these transactions for settlement, void authorizations, and issue refunds, like any other Braintree transactions.

If you have created a custom point of sale app with the [PayPal Here SDK](https://developer.paypal.com/docs/integration/paypal-here/), you can vault customer payment information in addition to procesing the transaction. When PayPal Here on Braintree is first enabled, we use OAuth to automatically authorize PayPal Here to add to your vault.


## Reporting

To view information about PayPal Here transactions in aggregate, use [transaction search](/braintree/articles/control-panel/search#transactions) with a payment method type of "PayPal Here." Transaction search is also available [via API](/braintree/docs/reference/request/transaction/search#payment_instrument_type).


## Contact

If you have further questions about PayPal Here, [reach out to PayPal directly](http://www.paypal-support.com).

