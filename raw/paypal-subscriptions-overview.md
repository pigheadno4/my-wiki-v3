---
title: "Subscriptions "
slug: /docs/subscriptions/
createTime: "2024-07-08T05:25:46.497Z"
updateTime: "2025-05-09T10:15:17.595Z"
---

# Subscriptions

Create subscriptions to bill customers at regular intervals. You can customize a subscriptions integration to:

- Create plans that charge users a fixed amount at regular intervals or a variable amount based on the number of users subscribed.
- Create plans that charge users based on volume or tier.
- Offer your subscribers free or discounted trials.
- Enable subscribers to upgrade or downgrade their plans.
- Automate payment recovery for failed payments.

## How it works

![How,subscriptions,work](assets/paypal-subscriptions-how-it-works.png)

- Create a product to represent your goods or services.
- Create a plan to represent the payment cycles for your subscription.
- Use the JavaScript SDK to present the PayPal button, which starts the subscription process.
- The buyer agrees and subscribes.
- The button calls the Subscriptions API to create the subscription.
- The buyer sees the subscription confirmation.

## Choose a Subscriptions solution

### Subscriptions REST APIs

[Customize Subscriptions to fit into your product UI](/docs/subscriptions/integrate/)

If you have your own product UI, you can customize the Subscriptions APIs and integrate them into your product.

### PayPal business account

[Manage Subscriptions on your account dashboard](https://www.paypal.com/merchantapps/appcenter/acceptpayments/subscriptions)

Recommended if you don't need to integrate Subscriptions into your product UI.
