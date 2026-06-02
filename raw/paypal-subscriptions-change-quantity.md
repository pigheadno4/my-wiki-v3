---
title: Change subscription quantity
slug: /docs/subscriptions/customize/change-quantity/
createTime: "2024-08-15T06:20:54.990Z"
updateTime: "2024-09-24T16:27:46.469Z"
---

# Change subscription quantity

Quantity-based, also known as user or seat-based, subscriptions allow consumers to subscribe to a plan and specify the number of units at the time of subscription. This gives subscribers the flexibility to change from one quantity to another depending on their need. For example, a remote tech support agency might have these different plans:

- Basic Plan - $4 per tech support agent, monthly plan.
- Premium Plan - $6 per tech support agent, monthly plan.

A subscribing company might start with the basic plan and 4 agents and then decide to increase to 10 agents to accommodate growth in the company.

## Change quantity

To change the quantity of seats or units for a subscription, copy the following code and modify it.

### Sample request

API endpoint used: [Revise plan or quantity of subscription](/docs/api/subscriptions/v1/#subscriptions_revise)

curl -v -X POST https://api-m.sandbox.paypal.com/v1/subscriptions/I-BW452GLLEP1G/revise  
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-d '{
"plan_id": "P-5ML4271244454362WXNWU5NQ",
"quantity": "10"
}'### Modify the code
After you copy the code in the sample request, modify the following:

- ACCESS-TOKEN - Your [access token](/api/rest/authentication/) .
- Subscription ID - In the URI for the API call, replace the sample ID with the ID for the subscription you want to update. In this example the subscription ID is I-BW452GLLEP1G .
- Plan ID - Replace the sample ID with the plan ID you want to use in the subscription. In this example the plan ID is P-5ML4271244454362WXNWU5NQ .
- Quantity - Replace the sample quantity with the number of units you want.

While this sample code increases the number of units, you can also decrease the number of units in a similar manner.

Subscriptions using PayPal require the user to login and re-consent to the change using the approve [HATEOAS URL](/api/rest/responses/#hateoas-links) returned in the response. If re-consent is not done or if it fails, the subscription continues to be billed on the existing quantity. Subscriptions using direct card payment do not need re-consent.

## Billing changes

The new price is effective starting on the next billing cycle. Proration and one-time fees aren't automatically supported. If you want to prorate the difference at the time the plan changes or charge one-time fees, you need to do these manually.

In the following example, a subscriber's billing cycle is at the beginning of the month, and they change the quantity of their plan mid-cycle.

- Subscriber starts the Basic $4 per unit quantity plan with 5 tech support agents, which amounts to $20 on 1 January.
- Subscriber increases to 10 tech support agents on 15 March.
- Subscriber is charged the new price of $40 ($4 per unit \* 10) from 1 April billing cycle onwards.

## See also

- [Pricing plans](/docs/subscriptions/customize/pricing-plans/)
- [Subscriptions REST API](/docs/api/subscriptions/v1/#subscriptions) - Use the Subscriptions REST API to manage subscriptions, including updating, suspending, and canceling a subscription.
