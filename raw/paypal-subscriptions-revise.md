---
title: Upgrade or downgrade a subscription
slug: /docs/subscriptions/customize/revise-subscriptions/
createTime: "2024-08-15T07:23:08.692Z"
updateTime: "2025-05-13T15:11:40.745Z"
---

# Upgrade or downgrade a subscription

Subscription services usually offer different plans, often with different price points, to cater to a wide variety of consumers. For example, a music streaming service might have different these plans:

- Basic plan - Costs $4.99 per month with advertisements.
- Premium plan - Costs $9.99 per month with no advertisements.

A subscriber might start with the basic plan and then decide to upgrade to the premium plan to enjoy their music with no advertisements.

## Change subscription plan

You can upgrade or downgrade to subscription plans under the same product. To change a plan, copy the following code and modify it.

### Sample request

API endpoint used: [Revise plan or quantity of subscription](/docs/api/subscriptions/v1/#subscriptions_revise)

curl -v -X POST https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G/revise  
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-d '{
"plan_id": "P-5ML4271244454362WXNWU5NQ"
}'### Modify the code

After you copy the code in the sample request, modify the following:

- ACCESS-TOKEN - Your [access token](/api/rest/authentication/) .
- Subscription ID - In the URI for the API call, replace the sample ID with the ID for the subscription you want to update. In this example, the subscription ID is I-BW452GLLEP1G .
- Plan ID - Replace the sample ID with the new plan ID to upgrade or downgrade the subscription. In this example, the plan ID is P-5ML4271244454362WXNWU5NQ .

Subscriptions using PayPal require the user to login and re-consent to the change using the approve [HATEOAS URL](/api/rest/responses/#hateoas-links) returned in the response. If re-consent is not done or if it fails, the subscription continues to be billed on the existing plan. Subscriptions using direct card payment do not need re-consent.

## Billing changes

The new price is effective starting on the next billing cycle. Proration and one-time fees aren't automatically supported. If you want to prorate the difference at the time the plan changes or charge one-time fees, you need to do these manually.

In the following example, a subscriber's billing cycle is at the beginning of the month, and they upgrade their plan mid-cycle.

- Subscriber starts the Basic $4.99 streaming service on 1 January.
- Subscriber upgrades to the Premium $9.99 streaming service on 15 March.
- PayPal charges the subscriber the new price of $9.99 on the 1 April billing cycle onwards.

## See also

- [Subscriptions REST API](/docs/api/subscriptions/v1/#subscriptions) - Use the Subscriptions REST API manage subscriptions including updating, suspending, canceling a subscription.
