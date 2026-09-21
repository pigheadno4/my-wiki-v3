<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/recurring-billing/add-ons-discounts -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Add-ons and Discounts
slug: /articles/guides/recurring-billing/add-ons-discounts/
createTime: '2025-04-02T00:57:26.870Z'
updateTime: '2025-04-02T00:57:26.884Z'
---



# Add-ons and Discounts

You can use add-ons to charge customers for additional features or services on top of the normal subscription price. Discounts are used to reduce the price of a subscription as part of a promotion or price break. Both of these options modify a subscription price for a specific customer without having to change the price of the base plan.

Add-ons and discounts can be applied manually on a case-by-case basis, or you can associate them with certain plans to apply them automatically to new subscriptions. For instance, if you’re running a promotion for $10 off a 6-month subscription, then you can associate a $10 discount with your 6-month plan for as long as the promotion is available.


## Creating an add-on or discount


**NOTE**
 You must create and delete add-ons and discounts from the Control Panel. Via the API, you can only [view existing add-ons and discounts](/braintree/docs/guides/recurring-billing/plans#add-ons-and-discounts) and [add them to a subscription](/braintree/docs/guides/recurring-billing/create#overriding-plan-details) (either as-is or with modifications).

 

Before you can associate an add-on or discount with an individual subscription or a plan, you must create it via the Control Panel.


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Subscriptions**in the navigation bar
- Click the**Add Ons/Discounts**tab
- Click either the**Create An Add-On**or**Create A Discount**button
- Fill in any required or optional details
- Click the**Create**button

When creating an add-on or discount, keep these things in mind:


- You can[override](/braintree/docs/reference/request/subscription/create#override-plan-details)the following details for an add-on or discount when creating a new subscription or applying it to an existing subscription:
- number of billing cycles
- amount
- quantity


- An add-on or discount can't be deleted from the Control Panel if it is associated with a subscription

