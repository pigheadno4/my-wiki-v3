<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/processing -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Processing
slug: /articles/guides/payment-methods/paypal/processing/
createTime: '2025-04-02T01:58:49.176Z'
updateTime: '2025-08-07T11:44:00.318Z'
---



# Processing

The streamlined Pay with PayPal payment experience accelerates the buyer's checkout journey for [One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal), [Vaulted Payments](/braintree/docs/guides/paypal/vault), and [Recurring Payments](/braintree/docs/guides/paypal/recurring-payments).


## PayPal transaction lifecycle

PayPal transactions go through [a similar lifecycle as other payment types](/braintree/articles/get-started/transaction-lifecycle), but with a unique [settlement](#settlement) process.


### Authorization

The simplest approach when processing a transaction is to authorize and submit for settlement at the same time. That being said, Braintree and PayPal do support separate authorization and capture. This option can be helpful if you have a delayed order fulfillment process and prefer to wait to capture funds until you’re ready to provide your goods or services.

You can attempt to capture funds for up to 29 days after a successful authorization, but we recommend capturing sooner rather than later – PayPal can't ensure that 100% of the authorized funds will be available during that entire 29-day period.


**NOTE**
 
- PayPal will not allow you to capture funds if your customer's account is restricted or locked, or if your account has a high restriction level.


- You can't settle more than the authorized amount unless your industry and processor support settlement adjustment (settling a certain percentage over the authorized amount); [contact us](/braintree/help) for details.



 

For more details on PayPal authorizations, see PayPal's article on [Authorization & Capture](https://developer.paypal.com/docs/checkout/standard/customize/authorization/).


### Settlement

Unlike other payment methods, PayPal transactions are not settled [in batches](/braintree/articles/control-panel/reporting/settlement-batch-summary) ; instead, funds are captured right after you submit each transaction for settlement. This allows us to instantly inform you when a settlement is successful, so you can confidently ship your goods or provide your services immediately.

When settlement is successful, you'll receive a [processor settlement response](/braintree/docs/reference/general/processor-responses/settlement-responses) of Settling. Within two hours, Settling PayPal transactions transition to Settled. Otherwise, you’ll receive a declined or pending response, depending on the situation and whether you’re using multiple partial settlements. [See our transaction status reference for more info.](/braintree/docs/reference/general/statuses#transaction)


#### Multiple partial settlements

Multiple partial settlements are available for PayPal and Venmo transactions, and allow you to settle multiple amounts against a single authorization. This method can be helpful if you have a delayed order fulfillment process or if you send physical goods to customers in multiple shipments. You can create a parent authorization for the entire order amount, and when you’re ready to send each portion of the order, you will charge the customer for that portion in a separate child transaction. [Learn more in our developer documentation.](/braintree/docs/reference/request/transaction/submit-for-partial-settlement)


## Refunds and voids

Just like with other payment types, you can issue voids and full or partial refunds for PayPal transactions. We recommend that you do this in the Control Panel or via the Braintree API to ensure the transaction status is accurate in both your PayPal console and the Braintree Control Panel.

PayPal requires that refunds are issued within 180 days of the initial sale.


## Disputes

Disputed PayPal transactions can be managed in either the Braintree Control Panel or in the PayPal Resolution Center. [Learn more.](/braintree/articles/guides/payment-methods/paypal/disputes)


### Seller Protection

Braintree supports [PayPal's Seller Protection](https://www.paypal.com/webapps/mpp/security/seller-protection) for merchants who sell shipped goods online. To qualify for Seller Protection and avoid certain types of chargebacks, you must:


- Pass a properly-formatted[shipping address](/braintree/docs/guides/paypal/server-side#shipping-addresses)with each PayPal transaction
- Meet PayPal's Seller Protection requirements  


## Storing in the Vault

If you are using our Vault flow, PayPal customers will be prompted to enter their PayPal credentials and accept an agreement that will let you [store their information in the Braintree Vault](/braintree/docs/guides/customers) for future use.


**NOTE**
 This is a legacy integration. [Learn more about Vaulted Payments.](/braintree/docs/guides/paypal/vault)

 

![new_vault_flow](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/pay-with-paypal/new_vault_flow.png)

Your customer can cancel or change the payment method associated with this agreement at any time in their [PayPal Account Profile](https://www.paypal.com/signin). This agreement is associated with the PayPal Business Account credentials that you [entered in the Control Panel](/braintree/articles/guides/payment-methods/paypal/setup-guide#enter-your-paypal-credentials-in-the-braintree-control-panel) ; if you change which PayPal Business Account you use with Braintree, customers will have to re-enter their PayPal credentials and accept a new agreement.

Depending on your specific integration, you may need to pass [additional information](/braintree/docs/guides/paypal/vault#collecting-device-data) with individual PayPal transactions created from the Vault via the API. [Learn more about integration options when accepting PayPal.](/braintree/docs/guides/paypal/overview)

