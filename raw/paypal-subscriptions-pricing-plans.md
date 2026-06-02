---
title: Pricing plans
slug: /docs/subscriptions/customize/pricing-plans/
createTime: "2024-08-15T08:10:34.475Z"
updateTime: "2025-05-14T09:35:37.628Z"
---

# Pricing plans

When you set up your subscription plan, you can choose from four different pricing models:

- [Fixed](#fixed-pricing-plan)
- [Quantity](#quantity-based-plan) , also known as user or seat-based
- [Volume-based](#volume-based-plan)
- [Tiered-based](#tiered-based-plan)

## Fixed-pricing plan

A fixed-pricing plan is a frequency-based subscription plan that charges customers a fixed amount at a fixed frequency.

Sample use cases:

- Video or music streaming services that charge a monthly or yearly fee.
- Gym or club membership.
- Box subscriptions, such as grooming, clothing, beauty, and food.

### Examples

- Plan 1: $5 per month for a music streaming service
- Plan 2: $100 per year for a gym membership

### Sample request

The following sample request shows how to create a fixed pricing plan. Use this sample to adjust your code when you [create a plan](/docs/subscriptions/#2-create-plan) .

API endpoint used: [Create plan](/docs/api/subscriptions/v1/#plans_create)

curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans \
 -H "Accept: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "Content-Type: application/json" \
 -H "PayPal-Request-Id: PLAN-18062020-001" \
 -d '{
"name": "Premium Music Plus",
"description": "A premium plan with music download feature",
"product_id": "PROD-5RN21878H3527870P",
"billing_cycles": [{
"frequency": {
"interval_unit": "MONTH",
"interval_count": 1
},
"tenure_type": "REGULAR",
"sequence": 1,
"total_cycles": 0,
"pricing_scheme": {
"fixed_price": {
"value": "5",
"currency_code": "USD"
}
}
}],
"payment_preferences": {
"auto_bill_outstanding": true,
"payment_failure_threshold": 1
}
}'

## Quantity-based plan

A quantity-based pricing plan charges subscribers by the quantity of goods or services to which they subscribed.

Sample use cases:

- Service company offers remote tech support to small companies.
- A software company charges for the number of software licenses.
- Pet store offers a dog food subscription that charges customers based on the number of bags.

### Examples

- Plan 1: $5 per software license per month
- Plan 2: $9 per dog food bag per week

During subscription creation, the subscriber chooses a quantity. That quantity determines the amount charged every regular billing cycle.

- Subscription 1: - A subscriber signs up for a plan of $5 per software license per month
- A subscriber requests 10 licenses when they sign up
- The net subscription price is 10 x 5 = $50 per month

- Subscription 2: - A subscriber signs up for a plan of $9 per food bag per week
- A subscriber requests 5 food bags when they sign up
- The net subscription price is 9 x 5 = $45 per week

**Note:** Subscribers can request an update to the quantity as things change. The new quantity and definition determine the new price that's applicable to subsequent billing cycles.

### Sample request

The following sample request shows how to create a quantity-based pricing plan. Use this sample to adjust your code when you [create a plan](/docs/subscriptions/#2-create-plan) .

In this sample, the quantity_supported parameter indicates that this plan is a quantity-based plan.

API endpoint used: [Create plan](/docs/api/subscriptions/v1/#plans_create)

curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans \
 -H "Accept: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "Content-Type: application/json" \
 -H "PayPal-Request-Id: PLAN-18062020-001" \
 -d '{
"name": "Classic treat",
"description": "500gm dog food per bag",
"product_id": "PROD-6DN21878H3529990P",
"billing_cycles": [{
"frequency": {
"interval_unit": "WEEK",
"interval_count": 1
},
"tenure_type": "REGULAR",
"sequence": 1,
"total_cycles": 0,
"pricing_scheme": {
"fixed_price": {
"value": "9",
"currency_code": "USD"
}
}
}],
"quantity_supported": true,
"payment_preferences": {
"auto_bill_outstanding": true,
"payment_failure_threshold": 1
}
}'

## Volume-based plan

A volume-based pricing model defines the subscription's price based on the price per unit of the number of product units within a specified range.

Sample use cases:

- Bulk SMS, email, and voice services
- Bulk SAAS based platform charges for a given number of product licenses
- Cloud based service platform charges for data storage based on volume

### Examples

#### Plan 1

A merchant offers a volume-based monthly plan that provides software licenses to businesses using these defined fees:

| Number of software licenses | Price per license (per month) |
| --------------------------- | ----------------------------- |
| 1-5                         | $15                           |
| 6-10                        | $14                           |
| 11-15                       | $13                           |
| 16-20                       | $12                           |
| 21 and beyond               | $11                           |

During subscription creation, the subscriber chooses a quantity. That quantity determines the amount charged every regular billing cycle.

- Subscription 1

- A subscriber signs up for plan 1
- A subscriber requests 14 licenses when they sign up. The price is calculated based on 3rd tier (11-15)
- The net subscription price is 14 x 13 = $182 per month

- Subscription 2

- A subscriber signs up for plan 1
- A subscriber requests 25 licenses when they sign up. The price is calculated based on 5th tier (21 and beyond)
- The net subscription price is 25 x 11 = $275 per month

#### Plan 2

A merchant offers a volume-based monthly plan that provides tech support and assistance to relevant businesses with the using these defined fees:

| Number of technicians (Tech Support) | Price per technician (per month) |
| ------------------------------------ | -------------------------------- |
| 1-10                                 | $30                              |
| 11-20                                | $29                              |
| 21-30                                | $28                              |
| 31 and beyond                        | $27.5                            |

- Subscription 1

- A subscriber signs up for plan 2
- A subscriber requests 8 licenses when they sign up. The price is calculated based on 1st tier (1-10)
- The net subscription price is 8 x 30 = $240 per month

- Subscription 2

- A subscriber signs up for plan 2
- A subscriber requests 25 licenses when they sign up. The price will be calculated based on 3rd tier (21-30)
- The net subscription price is 25 x 28 = $700 per month

**Note:** Subscribers can request an update to the quantity as things change. You can also customize the price for a subscriber or plan level at any time. The new quantity and definition determine the new price that's applicable to subsequent billing cycles.

### Sample request

The following sample request shows how to create a volume-based pricing plan. Use this sample to adjust your code when you [create a plan](/docs/multiparty/subscriptions/integrate/) .

In this sample, the pricing_model and quantity_supported parameters indicate that this plan is a volume-based plan.

API endpoint used: [Create plan](/docs/api/subscriptions/v1/#plans_create)

curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans \
 -H "Accept: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "Content-Type: application/json" \
 -H "PayPal-Request-Id: PLAN-18062020-001" \
 -d '{
"name": "Standard Plan",
"description": "Volume based Software Licenses",
"product_id": "PROD-6DN21878H3529990P",
"billing_cycles": [{
"frequency": {
"interval_unit": "MONTH",
"interval_count": 1
},
"tenure_type": "REGULAR",
"sequence": 1,
"total_cycles": 0,
"pricing_scheme": {
"pricing_model": "VOLUME",
"tiers": [
{
"starting_quantity": "1",
"ending_quantity": "5",
"amount": {
"value": "15",
"currency_code": "USD"
}
},
{
"starting_quantity": "6",
"ending_quantity": "10",
"amount": {
"value": "14",
"currency_code": "USD"
}
},
{
"starting_quantity": "11",
"ending_quantity": "15",
"amount": {
"value": "13",
"currency_code": "USD"
}
},
{
"starting_quantity": "16",
"ending_quantity": "20",
"amount": {
"value": "12",
"currency_code": "USD"
}
},
{
"starting_quantity": "21",
"amount": {
"value": "11",
"currency_code": "USD"
}
}
]
}
}],
"quantity_supported": true,
"payment_preferences": {
"auto_bill_outstanding": true,
"payment_failure_threshold": 1
}
}'

## Tiered-based plan

A tier-based pricing model defines the subscription's price and any price changes based on the quantity of product units within a tier.

Sample use cases:

- Bulk SMS, email, and voice services
- SAAS charges for a given number of product licenses priced differently across tiers
- Cloud based service platform changes for data storage priced differently across tiers

### Examples

#### Plan 1

A merchant offers a tiered-based monthly plan that provides software licenses to businesses using these defined fees:

| Number of software licenses | Price per license (per month) |
| --------------------------- | ----------------------------- |
| 1-5                         | $15                           |
| 6-10                        | $14                           |
| 11-15                       | $13                           |
| 16-20                       | $12                           |
| 21 and beyond               | $11                           |

During subscription creation, the subscriber chooses a quantity. That quantity determines the amount charged every regular billing cycle.

- Subscription 1

- A subscriber signs up for plan 1
- A subscriber requests 14 licenses when they sign up
- The net subscription price is 5 x 15 + 5 x 14 + 4 x 13 = $197 per month

- Subscription 2

- A subscriber signs up for Plan 1
- A subscriber requests 25 licenses when they sign up
- The net subscription price is 5 x 15 + 5 x 14 + 5 x 13 + 5 x 12 + 5 x 11 = $325 per month

#### Plan 2

A merchant offers a tiered-based monthly plan that provides tech support and assistance to relevant businesses with the following fee schedule:

| Number of technicians (Tech Support) | Price per technician (per month) |
| ------------------------------------ | -------------------------------- |
| 1-10                                 | $30                              |
| 11-20                                | $29                              |
| 21-30                                | $28                              |
| 31 and beyond                        | $27.5                            |

During subscription creation, the subscriber chooses a quantity. That quantity determines the amount charged every regular billing cycle.

- Subscription 1

- A subscriber signs up for Plan 2
- A subscriber requests 14 licenses when they sign up
- The net subscription price is 10 x 30 + 4 x 29 = $416 per month

- Subscription 2

- A subscriber signs up for Plan 2
- A subscriber requests 25 licenses when they sign up
- The net subscription price is 10 x 30 + 10 x 29 + 5 x 28 = $730 per month

**Note:** Subscribers can request an update to the quantity as things change. You can also customize the price for a subscriber or plan level at any time. The new quantity and definition determine the new price that's applicable to subsequent billing cycles.

### Sample request

The following sample request shows how to create a tiered-based pricing plan. Use this sample to adjust your code when you [create a plan](/docs/multiparty/subscriptions/integrate/) .

In this sample, the pricing_model and quantity_supported parameters indicate that this plan is a tiered-based plan.

API endpoint used: [Create plan](/docs/api/subscriptions/v1/#plans_create)

curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans \
 -H "Accept: application/json" \
 -H "Authorization: Bearer ACCESS-TOKEN" \
 -H "Content-Type: application/json" \
 -H "PayPal-Request-Id: PLAN-18062020-001" \
 -d '{
"name": "Platinum Plan",
"description": "Tiered based pricing for technical support",
"product_id": "PROD-6DN21878H3529990P",
"billing_cycles": [{
"frequency": {
"interval_unit": "MONTH",
"interval_count": 1
},
"tenure_type": "REGULAR",
"sequence": 1,
"total_cycles": 0,
"pricing_scheme": {
"pricing_model": "TIERED",
"tiers": [
{
"starting_quantity": "1",
"ending_quantity": "10",
"amount": {
"value": "30",
"currency_code": "USD"
}
},
{
"starting_quantity": 11",
"ending_quantity": "20",
"amount": {
"value": "29",
"currency_code": "USD"
}
},
{
"starting_quantity": "21",
"ending_quantity": "30",
"amount": {
"value": "28",
"currency_code": "USD"
}
},
{
"starting_quantity": "31",
"amount": {
"value": "27.5",
"currency_code": "USD"
}
}
]
}
}],
"quantity_supported": true,
"payment_preferences": {
"auto_bill_outstanding": true,
"payment_failure_threshold": 1
}
}'

## See also

- Use the [Plans resource group](/docs/api/subscriptions/v1/#plans) of the Subscriptions REST API to manage plans, including updating pricing, updating the plan, and deactivating the plan.

export const \_frontmatter = {"title":"Pricing plans","contentType":"Docs","keywords":"subscriptions, pricing plans","productStatus":"Current","apiVersion":"v1","date":"2022-04-06T23:06:12.000Z"}
