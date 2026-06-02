---
title: Billing cycles
slug: /docs/subscriptions/customize/billing-cycles/
createTime: "2024-08-15T05:55:46.375Z"
updateTime: "2025-05-12T15:31:07.086Z"
---

# Billing cycles

When you create a plan, you set the regular period billing cycle duration. A plan’s billing cycle defines the recurring frequency with which the subscriber is charged. For example, a plan with a weekly billing cycle charges the subscriber on a recurring frequency of one week.

You can choose from the following billing cycles:

- Day
- Week
- Month
- Year
- Custom: customize the billing cycle for more flexible options like two weeks or three months.

## Finite and infinite

Billing cycles can continue for a specified period of time, a finite plan, or until the user cancels the subscription, an infinite plan.

- **Finite plan** - A plan with a fixed number of billing cycles. Create a finite plan if you want to associate a pre-defined number of cycles to the plan. Once a buyer subscribes to a finite plan, the subscription remains active for the specified number of billing cycles. You create a finite plan by specifying the total_cycles of billing cycles when you create the plan.

Example: An online tutorial course priced at $10 per month and scheduled to last for five monthly cycles. The subscriber is charged $10 for five monthly cycles with the subscription ending after the fifth cycle.

- **Infinite plan** - A plan without a fixed number of cycles. Create an infinite plan if you don’t want to associate a pre-defined number of cycles to the plan. Once a buyer subscribes to an infinite plan, the subscription remains active until cancelation. You create an infinite plan by specifying the total_cycles of billing cycles as 0 when you create the plan.

Example: A plan for video streaming service priced at $20 per month. The subscriber is charged $20 per month until they cancel the subscription.

### Example: finite plan

This example sets a finite plan with the following characteristics:

- Five cycles
- Each billing cycle is one month

curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans /
-H "Content-Type: application/json" /
-H "Authorization: Bearer ACCESS-TOKEN" /
-d '{
"name": "Beginner Plan",
"description": "Five month beginner course",
"product_id": "PROD-5RN21878H3527870P",
"billing_cycles": [
{
"frequency": {
"interval_unit": "MONTH",
"interval_count": 1
},
"tenure_type": "REGULAR",
"sequence": 1,
"total_cycles": 5,
"pricing_scheme": {
"fixed_price": {
"value": "10",
"currency_code": "USD"
}
}
}
],
"payment_preferences": {
"auto_bill_outstanding": true,
"payment_failure_threshold": 1
}
}'### Example: infinite plan
This example sets an infinite plan with the following characteristics:

- Billing continues until the subscriber cancels. Create an infinite plan by specifying the total_cycles of billing cycles as 0.
- Each billing cycle is one month

curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans /
-H "Content-Type: application/json" /
-H "Authorization: Bearer ACCESS-TOKEN" /
-d '{
"name": "Premium Video Plus",
"description": "Premium plan with video download feature",
"product_id": "PROD-5RN21878H3527870P",
"billing_cycles": [
{
"frequency": {
"interval_unit": "MONTH",
"interval_count": 1
},
"tenure_type": "REGULAR",
"sequence": 1,
"total_cycles": 0,
 "pricing_scheme": {
"fixed_price": {
"value": "20",
"currency_code": "USD"
}
}
}
],
"payment_preferences": {
"auto_bill_outstanding": true,
"payment_failure_threshold": 1
}
}'## See also

- [Create a plan](/docs/subscriptions/#2-create-plan) - You set the billing cycle frequency and the length of the subscription when you create the plan.
