---
title: Charge a setup fee
slug: /docs/subscriptions/customize/one-time-fee/
createTime: "2024-08-15T06:08:31.275Z"
updateTime: "2025-05-14T09:56:20.140Z"
---

# Charge a setup fee

Use a setup fee to charge the subscriber before the subscription begins, typically for items that aren't part of the regular subscription billing.

You set up the fee when you [create the plan](/docs/subscriptions/#2-create-plan) .

## Example: Software license onboarding fee

The following example creates a setup fee with the following characteristics:

- $10 setup fee for onboarding and configuration of a network vendor subscriber before purchasing a software license.
- $15 per month for the regular billing cycle.

## Sample request

Set the value for the setup_fee in the [payment_preferencesobject](/docs/api/subscriptions/v1/#definition-payment_preferences) .

"payment_preferences": {
"setup_fee": {
"value": "10",
"currency_code": "USD"
},
},

## See also

- [Offer a trial period](/docs/subscriptions/customize/trial-period/)
- [Pricing plans](/docs/subscriptions/customize/pricing-plans/)
