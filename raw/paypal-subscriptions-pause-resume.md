---
title: Pause or resume a subscription
slug: /docs/subscriptions/customize/pause-resume/
createTime: "2024-08-15T07:11:52.053Z"
updateTime: "2025-05-14T09:45:42.330Z"
---

# Pause or resume a subscription

With subscription services, you may encounter situations where consumers want to pause their subscription service for a period of time, such as when pausing cable service or a gym subscription during a vacation. Providing this ability helps you reduce customer churn.

You can also use this functionality as a "soft cancellation": when a consumer wants to stop their subscription, you can mark it inactive by pausing it and allowing it to be reactivated later. This saves consumers from having to go through the sign-up steps needed to re-subscribe from a [hard cancellation](/docs/api/subscriptions/v1/#subscriptions_cancel) .

When a subscription is paused, or soft-canceled, PayPal will stop processing payments until it is reactivated. You can still recover any outstanding balances during the pause.

## Pausing subscriptions

To pause a customer subscription, copy the following code and modify it.

### Sample request

API endpoint used: [Suspend subscription](/docs/api/subscriptions/v1/#subscriptions_suspend)

curl -v -X POST https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G/suspend
-H "Content-Type: application/json"
-H "Authorization: Bearer ACCESS-TOKEN"
-d '{
"reason": "Customer-requested pause"
}'

### Modify the code

- Access-Token - replace ACCESS-TOKEN with your access token.
- Subscription ID - In the URI for the API call, replace the sample ID with the ID for the subscription you want to update. In this example, the subscription ID is I-BW452GLLEP1G .
- Reason - Enter the reason for pausing or suspending the subscription as a string. Here, the reason is Customer-requested pause .

## Resume subscriptions

To resume a paused customer subscription, copy the sample below, and modify it in the same way as described in Pausing subscriptions.

### Sample request

API endpoint used: [Activate subscription](/docs/api/subscriptions/v1/#subscriptions_activate) .

curl -v -X POST https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G/activate
-H "Content-Type: application/json"
-H "Authorization: Bearer ACCESS-TOKEN"
-d '{
"reason": "Reactivating on customer request"
}'
