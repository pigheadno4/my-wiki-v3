---
title: Offer a trial period
slug: /docs/subscriptions/customize/trial-period/
createTime: "2024-12-10T13:34:38.684Z"
updateTime: "2025-05-13T15:04:04.762Z"
---

# Offer a trial period

Use a trial period to let subscribers try your product at a free or discounted price before regular billing cycles
start. After the trial period ends, the regular billing period for the subscription begins. You can have up to 2
trial periods per plan.

The following sample requests show how to offer trial periods. Use these samples to adjust your code when you [create a plan](/docs/subscriptions/#2-create-plan) .

## Example: Music service

The following example creates a trial period with the following characteristics:

- $0 for the first month.
- $15 per month following the trial period.

1curl-v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans2-H"Accept: application/json"3-H"Authorization: Bearer ACCESS-TOKEN"4-H"Content-Type: application/json"5-H"PayPal-Request-Id: PLAN-18062020-002"6-d'{7"name": "Premium Music Plus",8"description": "A premium plan with music download feature",9"product_id": "PROD-5RN21878H3527870P",10"billing_cycles": [{11"frequency": {12"interval_unit": "MONTH",13"interval_count": 114},15"tenure_type": "TRIAL",16"sequence": 1,17"total_cycles": 1,18"pricing_scheme": {19"fixed_price": {20"value": "0",21"currency_code": "USD"22}23}24}, {25"frequency": {26"interval_unit": "MONTH",27"interval_count": 128},29"tenure_type": "REGULAR",30"sequence": 2,31"total_cycles": 0,32"pricing_scheme": {33"fixed_price": {34"value": "15",35"currency_code": "USD"36}37}38}], "payment_preferences": {39"auto_bill_outstanding": true,40"payment_failure_threshold": 141}42}'

## Example: Online tutorial service

The following example creates a trial period with the following characteristics:

- $0 free trial for the first week.
- $5 per week discounted trial for the next 3 weeks.
- $10 per week following the trial period.

1curl-v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans2-H"Accept: application/json"3-H"Authorization: Bearer ACCESS-TOKEN"4-H"Content-Type: application/json"5-H"PayPal-Request-Id: PLAN-18062020-003"6-d'{7"name": "Music Tutorial Premium Plus",8"description": "Offering a premium music tutorial with download feature",9"product_id": "PROD-5RN21878H3527870P",10"billing_cycles": [{11"frequency": {12"interval_unit": "WEEK",13"interval_count": 114},15"tenure_type": "TRIAL",16"sequence": 1,17"total_cycles": 1,18"pricing_scheme": {19"fixed_price": {20"value": "0",21"currency_code": "USD"22}23}24}, {25"frequency": {26"interval_unit": "WEEK",27"interval_count": 128},29"tenure_type": "TRIAL",30"sequence": 2,31"total_cycles": 3,32"pricing_scheme": {33"fixed_price": {34"value": "5",35"currency_code": "USD"36}37}38}, {39"frequency": {40"interval_unit": "WEEK",41"interval_count": 142},43"tenure_type": "REGULAR",44"sequence": 3,45"total_cycles": 0,46"pricing_scheme": {47"fixed_price": {48"value": "10",49"currency_code": "USD"50}51}52}], "payment_preferences": {53"auto_bill_outstanding": true,54"payment_failure_threshold": 155}56}'## See also

- [Charge a setup fee](https:/docs/subscriptions/customize/one-time-fee/)
- [Pricing plans](https:/docs/subscriptions/customize/pricing-plans/)
