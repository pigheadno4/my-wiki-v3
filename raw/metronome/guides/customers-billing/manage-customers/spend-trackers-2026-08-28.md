<!-- Source URL: https://docs.metronome.com/guides/customers-billing/manage-customers/spend-trackers.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Spend trackers

<Note>
  **Public Beta**

  Spend trackers are currently in a Public Beta. Breaking changes may occur between now and GA. Please use the [Metronome support portal](https://support.metronome.com/) to request access.
</Note>

For certain billing models, it might be useful to track the spend of a customer over-time. These trackers might be used to inform discounting schemes or provide visibility to the end-customer. Create a `spend_tracker` on the contract to track the total spend for specific charges over time.

## Create a spend tracker

Spend trackers return the summation of specified charges over a period of time - `spend_tracker.reset_frequency`. Spend trackers can be set on Package creation, contract creation, or contract edit. Other configurations on the contract can point at the spend tracker to manage spend based thresholds. For example, we can create a spend tracker to cap the amount of discounted prepaid commit purchases a customer can get in a single month.

`applicable_spend_specifiers` specify which charges should count against the spend tracker:

* *`spend_type`:* Today, only commit purchases can count towards a spend tracker.
* *`sources`:* Specify whether commits created manually and / or threshold billing commits count towards the spend tracker.
* *`discounted`:* Optionally specify whether commits marked as "discounted" count towards the spend tracker. For manual commits, this is defined via `spend_tracker_attributes.count_as_discounted`. For threshold billing commits, it is defined via the `discount_config`.

See the example contract below:

```bash theme={null}
    curl https://api.metronome.com/v1/contracts/create \
      -H "Authorization: Bearer <TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
            "customer_id": "8cecbf69-960f-4f66-9575-edebb7d95e88",
            "rate_card_id": "a7bc3775-b651-46b6-b7e4-d225a7e55c4c",
            "starting_at": "2025-04-01T00:00:00.000Z",
            ...
            "spend_trackers": [
              {
                "alias": "promo-cap",
                "credit_type_id": "usd_credit_type_id",
                "reset_frequency": "BILLING_PERIOD",
                "applicable_spend_specifiers": [
                  {
                    "spend_type": "COMMIT_PURCHASE",
                    "sources": ["THRESHOLD_RECHARGE", "MANUAL"],
                    "discounted": "DISCOUNTED_ONLY"
                  }
                ]
              }
            ],
            "prepaid_balance_threshold_configuration": {
              "commit": {
                "product_id": "d6be3bf4-1669-40c9-a8b1-388bb167ab16",
                "name": "prepaid-balance",
                "description": "threshold billing recharges"
              },
              "discount_config": {
                "fraction": 0.90,
                "cap": {
                  "spend_tracker_alias": "promo-cap",
                  "amount": 20000
                }
              },
              "is_enabled": true,
              "payment_gate_config": {
                "payment_gate_type": "STRIPE",
                  "stripe_config": {
                    "payment_type": "INVOICE"
                  }
              },
              "threshold_amount": 500,
              "recharge_to_amount": 2000
            }
          }'
```

For this contract, we have a spend tracker that is scoped to include discounted manual and threshold billing commits. The `discount_config` on the `prepaid_balance_threshold_configuration` points at this spend tracker to enforce a cap. When the cap is reached, new threshold commits will not be discounted until the start of the next billing period.

## Get spend tracker total

Once set up, you can query the contract to return the current spend counted towards the tracker within the current period. See an example below:

```bash theme={null}
    curl https://api.metronome.com/v2/contracts/get \
      -H "Authorization: Bearer <TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
            "data": {
            "id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
            ...
            "spend_trackers": [
              {
                "alias": "promo-cap",
                "credit_type_id": "usd_credit_type_id",
                "reset_frequency": "BILLING_PERIOD",
                "accumulated_spend": {
                  "amount": 14253.22,
                  "period_starting_at": "2026-05-01T00:00:00.000Z",
                  "period_ending_before": "2026-06-01T00:00:00.000Z"
                },
                "applicable_spend_specifiers": [
                  {
                    "spend_type": "COMMIT_PURCHASE",
                    "sources": ["THRESHOLD_RECHARGE", "MANUAL"],
                    "discounted": "DISCOUNTED_ONLY"
                  }
                ]
              }
            ]
          }
        }'
```

While spend trackers can be used to dynamically trigger certain configurations, like the threshold billing discount config shown above, users can leverage this spend tracker to enforce internal pricing schemes. For example, if you wanted to enforce a spend cap for [payment gated commits](/guides/pricing-packaging/apply-credits-and-commits/manual-payment-gated-commits), you could check the spend tracker before issuing the commit to enforce a cap.
