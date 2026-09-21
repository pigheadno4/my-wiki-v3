<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/recurring-billing/billing-cycles -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Billing Cycles
slug: /articles/guides/recurring-billing/billing-cycles/
createTime: '2025-04-02T01:44:05.455Z'
updateTime: '2025-04-02T01:44:05.558Z'
---



# Billing Cycles

Our recurring billing feature allows you to specify the length of a billing cycle, the billing date for a plan or subscription, and the number of billing cycles a subscription will last.

When the subscription billing date arrives, we’ll begin charging customers’ payment methods at 9am UTC. We run the recurring billing system a couple of times each day to balance the load on our servers, so it's possible that not all of your subscriptions will be processed simultaneously.

All recurring billing transactions are submitted for settlement on the chosen billing date, so funds will be collected immediately — regardless of weekends and holidays. If a customer’s payment method is declined and you want it to be retried, you can set up retry logic in the Control Panel.


## How it works

When creating a plan, you'll be able to specify the following Billing Details :


- billing cycle length
- billing date
- number of billing cycles


### Billing cycle length

The length of a billing cycle is the number of months between billing dates for a subscription plan. If a billing cycle is 3 months long, for example, then a customer on that subscription will only be charged 4 times a year, on the specified billing date. Billing cycles must be defined in monthly increments and will be the same for each subscription within a plan.


### Billing date

You can choose to have the billing cycle of a new plan start immediately when the customer signs up, or on a future date.

We set subscriptions to bill on specific dates, rather than billing after a certain number of days. This means that if you opt to begin the billing cycle immediately, the cycle will be based off of the date the customer signed up (e.g. if you create the subscription on the 3rd of the month and choose to bill immediately, the customer will always be billed on the 3rd day of the first month in a billing cycle).

If you select to have billing begin immediately, and it’s the 29th, 30th, or 31st of the month, our system will default to bill on the last day of the first month in a billing cycle. Since the last day of the month can vary, we recommend starting the subscription on a future date that every month has for consistency.


#### Identifying the next billing date

To confirm the next billing date for a subscription:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Subscriptions**in the navigation bar
- Define your desired parameters and click the**Search**button
- Locate the subscription and click on the subscription**ID**
- Scroll to the**Billing Details**section to find the**Next Bill Date**


**NOTE**
 When a subscription reaches its final [billing cycle](#number-of-billing-cycles), the date listed under **Next Bill Date** will be the final date of the subscription.

 


#### Changing the billing date

When creating a new subscription in a plan, you can override the plan’s billing date and specify a different one.

The billing date can't be changed after a subscription has been created. If you need to change the billing date, it’s best to cancel the subscription and create a new one.


### Number of billing cycles

You can set the length of a plan or subscription by selecting the number of billing cycles before expiration. For example, if a plan's billing cycle is 3 months long, and the number of billing cycles specified is 4, then the plan will expire after one year. If you prefer for a subscription to continue indefinitely, you can select Never expires in this field.

Like the [billing date](#changing-the-billing-date), you can override a plan's specified number of billing cycles when creating a new subscription.

