<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/recurring-billing/subscriptions -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Subscriptions
slug: /articles/guides/recurring-billing/subscriptions/
createTime: '2025-04-02T01:10:35.320Z'
updateTime: '2025-04-02T01:10:35.344Z'
---



# Subscriptions

A subscription allows you to charge your customers automatically in monthly increments for a service or product. The sections below will help you manage your subscriptions.


## Creating a subscription


**NOTE**
 Before you can create a subscription, you need to [create a plan](/braintree/articles/guides/recurring-billing/plans).

 

To create a subscription:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- [Create a new customer](/braintree/articles/control-panel/vault/create), or[search for an existing customer](/braintree/articles/control-panel/search#vault)in the Vault and click on the customer's**ID**link
- Scroll to the**Payment Methods**section
- Click the**New Subscription**link located to the right of the desired payment method
- Fill out any relative information – including:
- The[billing date](/braintree/articles/guides/recurring-billing/billing-cycles#billing-date)
- The[number of billing cycles](/braintree/articles/guides/recurring-billing/billing-cycles#number-of-billing-cycles)
- [Add-ons or discounts](/braintree/articles/guides/recurring-billing/add-ons-discounts)
- [Trial periods](/braintree/articles/guides/recurring-billing/trial-periods)


- Click the**Create Subscription**button


**IMPORTANT**
 If you are including a trial period with a subscription, read the trial period [risks and requirements](/braintree/articles/guides/recurring-billing/trial-periods#risks-and-requirements) first.

 

There is no limit on the number of subscriptions that can be associated with a payment method. Additionally, **duplicate subscriptions are not subject to** [duplicate transaction checking rules](/braintree/articles/control-panel/transactions/duplicate-checking), so it is possible to unintentionally overbill customers.


## Updating a subscription


**IMPORTANT**
 Merchants operating in the European Union must give customers 4 weeks’ notice before changing the price of their recurring billing plan; 4 weeks’ notice is also required before billing customers if it has been 6+ months since their last payment. If you don’t operate in the EU, these notices aren't required (but they're still good practice).

 

The status of a subscription affects which details you can change. If you are unable to update a particular detail based on the subscription’s status, it’s best to cancel the subscription and create a new one from a plan that meets the requirements.


#### Pending and Active

For [Pending](/braintree/docs/guides/recurring-billing/overview#pending) and [Active](/braintree/docs/guides/recurring-billing/overview#active) subscriptions, you can update these fields:


- Subscription ID
- Price
- Plan (only if it has the same billing cycle)
- Payment method
- Add-on and discount details
- Merchant account
- Descriptor


#### Past Due

For [Past Due](/braintree/docs/guides/recurring-billing/overview#past-due) subscriptions, you can update these fields:


- Subscription ID
- Payment method
- Merchant account
- Descriptor


#### Expired and Canceled

You can't update [Expired](/braintree/docs/guides/recurring-billing/overview#expired) or [Canceled](/braintree/docs/guides/recurring-billing/overview#canceled) subscriptions. You’ll need to create a new subscription instead.


### Subscription payment method

Simply adding a new payment method to a customer’s Vault record will not automatically update any of their subscriptions. In order to change which payment method actually funds a subscription, you must update the contents of that subscription's payment method token within the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- [Search for the customer](/braintree/articles/control-panel/search#vault)in the Vault
- Click on the customer's**ID**link
- Scroll to the**Subscriptions**section
- Click the**Subscription ID**link for the subscription you'd like to change
- Scroll to the**Customer Details**section
- Click on the link in thePayment Method Tokenfield
- Click the**Edit**button at the top of the page
- Make any desired changes
- Click the**Save**button

If you prefer to make updates via the API, you can either update the payment method token or select a different payment method from the customer's Vault record. [Learn more about updating subscriptions via the API.](/braintree/docs/guides/recurring-billing/manage#updating-subscriptions)

When you update a payment method that is associated with a subscription, the new card will be charged for the subscription on the next billing date.


### Subscription price

When you update a plan's price, only future subscriptions will reflect the change; the price of existing subscriptions associated with the plan will not change automatically. The only way to update the price of a subscription is to edit that subscription directly.

The easiest way to do this is [via the API](/braintree/docs/guides/recurring-billing/manage#updating-subscriptions), particularly if you have a large number of subscriptions to update. Alternatively, you can make these changes one-by-one in the Control Panel by doing the following:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Subscriptions**in the navigation bar
- Define your desired parameters and click the**Search**button
- Click the**Edit**link located to the right of the subscription you'd like to change
- Scroll to the**Subscription Details**section
- Enter the new amount in thePricefield
- Click the**Save**button
- Click the**Yes**button to confirm the change
- Repeat for the remaining subscriptions


## Retrying a Past Due subscription


**IMPORTANT**
Merchants operating in the European Union must give 4 weeks' notice before billing customers if it has been 6+ months since their last payment. There are also [rules around retrying declined recurring transactions](/braintree/articles/control-panel/transactions/declines#retrying-declined-transactions).

 

You can retry a past due subscription by following these steps:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Subscriptions**in the navigation bar
- Define your desired parameters and click the**Search**button
- Click the**Retry Charge**link located in theActionscolumn of the desired subscription
- If desired, adjust the price of the subscription
- Click the**Create Transaction**button


## Refunding a subscription

You can refund the sale transaction associated with a subscription when it has the status of [Settled](/braintree/articles/get-started/transaction-lifecycle#settled) or [Settling](/braintree/articles/get-started/transaction-lifecycle#settling). If you do not want to refund the full amount of the sale transaction, you can specify an amount for the partial refund. For example, if your customer has an annual subscription and you want to refund them for 6 months, you would issue a refund against the original transaction for half the sale amount.

You can issue a refund in the Control Panel by doing the following:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters to find the original transaction and click the**Search**button
- Click on the desired transaction**ID**link
- Click the**Refund**button at the top of the page
- Enter the amount you'd like to refund
- Click the**Refund**button

You can also refund subscriptions via the API. [Learn more in our developer docs.](/braintree/docs/guides/recurring-billing/manage#refunding-a-subscription)


## Canceling an Active subscription

You can cancel an active subscription by following these steps:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Subscriptions**in the navigation bar
- Define your desired parameters and click the**Search**button
- Click the**Subscription ID**link next to the one you'd like to cancel
- Click the**Cancel Subscription**button at the top of the page
- Click the**Yes**button to confirm the cancellation


**NOTE**
 Canceling a subscription will not delete it from your Control Panel. This is by design so that historical subscription data will always be available.

 


## Searching for subscriptions

​You can run a search for all of your subscriptions by visiting the **Subscriptions** page in the top navigation. You can download the results as a CSV file by clicking the **Download Subscriptions** button at the top of your search results page.

If you want to download a report of your [add-ons and discounts](/braintree/articles/guides/recurring-billing/add-ons-discounts), you can click the **Download Add-On/Discounts** button to download those as a separate CSV.



 The subscription cancellation date is not included in search results. If you are interested in this value, you can enable the [Subscription Canceled webhook](/braintree/docs/reference/general/webhooks/overview#triggers) and store the data in a local database.

 

