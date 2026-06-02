---
title: Update plan pricing
slug: /docs/subscriptions/customize/update-plan-pricing/
createTime: "2024-07-11T11:08:42.014Z"
updateTime: "2025-05-14T09:07:13.139Z"
---

# Update plan pricing

### Update pricing for the subscription plan

You can modify subscription pricing for all subscribers at once by changing the pricing at the plan level, without needing to migrate subscriptions individually.

For example, if you provide a video streaming service and offer a subscription plan at $5 per month, you can update the price for future cycles to $7 for all existing subscribers.

## How it works

When you update the plan price:

- New subscribers see the new price.
- Existing subscribers are notified by email about the price change, and given 10 days to modify their subscription.
- If the next billing cycle is within 10 days of the price change, subscribers are not changed the new price until the next billing cycle.

For example, you update the plan price from $20 to $25 on the 10th of the month. An existing subscriber is enrolled on this plan with the next billing cycle starting on the 15th of the month. This subscriber pays $20 for their subscription on the 15th of the month, and on the following month pays $25.

API endpoint used: [Update pricing schemes endpoint](https://developer.paypal.com/docs/api/subscriptions/v1/)

### Sample request

#### **`Sample Request`**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v1/billing/plans/P-7GL4271244454362WXNWU5NQ/update-pricing-schemes
-H "Content-Type: application/json"
-H "Authorization: Bearer ACCESS-TOKEN"
-d '{
"pricing_schemes": [{
  "billing_cycle_sequence": 1,
  "pricing_scheme": {
    "fixed_price": {
      "value": "50",
      "currency_code": "USD"
    }
  }
}, {
  "billing_cycle_sequence": 2,
  "pricing_scheme": {
    "fixed_price": {
      "value": "100",
      "currency_code": "USD"
    },
    "pricing_model": "VOLUME",
    "tiers": [{
      "starting_quantity": "1",
      "ending_quantity": "1000",
      "amount": {
        "value": "150",
        "currency_code": "USD"
      }
    }, {
      "starting_quantity": "1001",
      "amount": {
        "value": "250",
        "currency_code": "USD"
      }
    }]
  }
}]
}'
```

## Modify the code

Replace ACCESS-TOKEN with your access token.

In the URI for the API call, replace the sample subscription ID with the ID for the subscription you want to update. In this example, the subscription ID is P-7GL4271244454362WXNWU5NQ .
