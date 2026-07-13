<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/subscription/provision-your-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Provision your customer

Once your products and rates are configured, you can provision your customer with a [contract](/api-reference/contracts/create-a-contract). Metronome supports three types of subscription configurations on a contract:

* **Standard subscription:** Customers pay a recurring fee each billing period and all usage is either included or paid for separately in-arrears.
* **Seat-based credit pool:** Customers pay a recurring fee each billing period and are granted access to a pool of usage credits. Each seat on the subscription draws down from the shared credit pool. Overages are billed at the contract level.
* **Individual seat credits:** Customers pay a recurring fee each billing period and are granted access to credits scoped to individual seats. Overages are billed at the contract level.

## Create a standard subscription

Subscriptions are configured on the customer's contract. To configure the subscription, you must first ensure the correct subscription rate from the rate card is specified and then complete the subscription configuration

### Pass the subscription config​

For each subscription on a contract, set the `subscriptions` config on the create contract call. Specify:

* `subscription_rate`: Similar to overrides, specify which subscription rate on your rate card this config applies to using the `billing_frequency` and `product_id`.

* `collection_schedule`: Either `advance` or `arrears`.

* `initial_quantity`: The current quantity for the subscription. For seats, this is the initial seat count. For a platform license, this is likely just `1`.

* `proration`: Define whether to prorate for mid-period quantity changes and whether mid-period changes should invoice immediately or on the next billing cycle. Optionally include a `rounding` object to round prorated subscription charges for improved invoice presentation.

* *Optional fields*: Optionally set the start and end dates of the subscription if different from the contract. Add a name or description for the subscription. These appear on the subscription line item.

### Optionally override the subscription rate

Use override functionality to discount the list rate and ensure the rate is `enabled` on the contract. To perform an override on a subscription rate, you must specify both the `billing_frequency` and the `product_id` given that a single `product_id` may map to multiple rates.

<Warning>
  **WARNING**

  Metronome will not charge for the subscription on the contract unless there is a subscription config set and the associated rate is `enabled`.
</Warning>

### Customize the billing cycle configuration

Customize how subscription billing periods are anchored and where subscription charges appear on invoices using the `billing_cycle_config` object on the subscription. Specify:

* `anchor_date`: The date from which Metronome begins generating subscription billing periods. Must be on or before the subscription start date, and is only supported for advance subscriptions. By default, subscriptions anchor to the same date as the contract's usage invoice anchor (typically the 1st of the month). Set a custom `anchor_date` to decouple the subscription billing cycle from the contract — for example, to bill each customer on the anniversary of their subscription start date rather than the first of the month or the contract start date.
* `invoice_placement`: Controls where subscription charges appear on invoices. Defaults to `ON_USAGE_INVOICE` so that subscription charges appear on the usage invoice with the matching billing date. Optionally set this field to `ON_SCHEDULED_INVOICE` to place subscription charges on scheduled invoices. If a scheduled invoice with the same billing date already exists, the charge is appended to it; otherwise a new scheduled invoice is created.

### Create the contract

See example contract creation below, where a contract is created with a subscription. Note that the subscription is configured to bill for prorated charges immediately, and round the unit price for prorated charges to the nearest dollar (because USD rates are expressed in cents).

```json theme={null}
{
    "customer_id": "4c09936b-455d-4c72-a120-d71b600a7546",
    "rate_card_id": "740a2ca1-64f6-417d-807a-05f154b3b1fe",
    "starting_at": "2025-04-23T00:00:00.000Z",
    "billing_provider_configuration": {
        "billing_provider_configuration_id": "e045c62b-65e7-4e84-a924-3f06f8b621d0"
    },
    "overrides": [
        {
            "starting_at": "2025-04-01T00:00:00.000Z",
            "override_specifiers": [
                {
                    "billing_frequency": "annual",
                    "product_id": "ed518bcb-acc1-4cd8-85dd-880c2eb38994"
                }
            ],
            "entitled": true
        }
    ],
    "subscriptions": [
        {
            "collection_schedule": "advance",
            "initial_quantity": 2,
            "proration": {
                "invoice_behavior": "bill_immediately",
                "is_prorated": true,
                "rounding": { "rounding_method": "HALF_UP", "decimal_places": -2 }
            },
            "subscription_rate": {
                "billing_frequency": "annual",
                "product_id": "ed518bcb-acc1-4cd8-85dd-880c2eb38994"
            },
            "description": "pro plan no additions",
            "name": "Pro Plan",
            "custom_fields": {
                 "plan_tier": "pro"
            }
        }
    ]
}
```

<Info>
  **INVOICING**

  You must specify a `billing_provider_configuration` on the contract for Metronome to successfully route invoices and collect payment on your behalf. See this guide for more information on [billing configurations](/guides/get-started/core-concepts/provision-customer#add-a-billing-configuration-to-a-customer).
</Info>

## Seat-based credit pool

Commonly, Metronome clients offer some amount of usage credits as part of their subscription offering. One way to model this is to provide a shared pool of credits that all seats on the subscription can consume. In order to model this in Metronome, you would follow the same instructions above for creating the subscription but additionally link the subscription to a [recurring credit](/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit#provision-recurring-usage-credits%E2%80%8B).

To link a subscription to a recurring credit on contract creation, add a `temporary_id` to your subscription config. Then, on the recurring credit config, reference the `temporary_id`. Each billing period, a credit balance equal to `access_amount` will be provided on the contract per seat. When new seats are added to the contract, new balance will be made available in the shared pool based upon the defined proration settings.

```json theme={null}
{
    "customer_id": "4c09936b-455d-4c72-a120-d71b600a7546",
    "rate_card_id": "740a2ca1-64f6-417d-807a-05f154b3b1fe",
    "starting_at": "2025-04-23T00:00:00.000Z",
    "billing_provider_configuration": {
        "billing_provider_configuration_id": "e045c62b-65e7-4e84-a924-3f06f8b621d0"
    },
    "overrides": [
        {
            "starting_at": "2025-04-01T00:00:00.000Z",
            "override_specifiers": [
                {
                    "billing_frequency": "annual",
                    "product_id": "ed518bcb-acc1-4cd8-85dd-880c2eb38994"
                }
            ],
            "entitled": true
        }
    ],
    "subscriptions": [
        {
            "collection_schedule": "advance",
            "initial_quantity": 2,
            "proration": {
                "invoice_behavior": "bill_on_next_collection_date",
                "is_prorated": true
            },
            "subscription_rate": {
                "billing_frequency": "annual",
                "product_id": "ed518bcb-acc1-4cd8-85dd-880c2eb38994"
            },
            "description": "pro plan no additions",
            "name": "Pro Plan",
            "custom_fields": {
                 "plan_tier": "pro"
            },
            "temporary_id": "pro_plan_annual"
        }
    ],
    "recurring_credits": [  
      {  
        "access_amount": {  
          "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",  
          "unit_price": 100  
        },  
        "commit_duration": {  
          "value": 1,  
          "unit": "periods"  
        },  
        "priority": 1,   
        "product_id": "652e1298-7638-45a8-b691-cdf47e46cbc8",  
        "starting_at": "2025-06-01T00:00:00Z",  
        "subscription_config": {  
          "subscription_id": "pro_plan_annual",  
          "apply_seat_increase_config": {  
            "is_prorated": true  
          }  
        }  
      }  
  ]
}
```

<Tip>
  **TIP**

  If you have an existing contract with a standard subscription, you can link it to a recurring credit using the `add_recurring_credits` object on the `/contracts/edit` end point.
</Tip>

## Individual seat credit

Alternatively, some organizations may wish to issue seat-scoped credits as part of their subscription package. In this model, each seat is entitled to a certain balance each period and only they can consume that balance. To configure seat-scoped credits, you need to specify a user ID for each seat. Metronome uses this ID to map usage to an individual seat.

<Tip>
  **TIP**

  By default, Metronome supports up to 1000 seats with individual seat credits. Reach out to Metronome if your use case requires more than 1000 seats.
</Tip>

### Prerequisites

Before configuring individual seat credits on a contract, you must set up seat-based pricing on your usage products. This involves three steps:

<Steps>
  <Step title="Define the group key on your billable metric">
    Add a [group key](/guides/get-started/core-concepts/create-billable-metrics#3-define-group-keys) on the billable metric that underlies your usage product e.g. `seat_id`. Group keys must be defined at the metric level before they can be used on products.

    <Note>Group keys cannot be edited after a streaming billable metric is created. If your existing metric doesn't include `seat_id` as a group key, you need to create a new metric with it defined.</Note>
  </Step>

  <Step title="Add the presentation group key to your product">
    Set `seat_id` as a [presentation group key](/guides/get-started/core-concepts/create-products-contracts#presentation-group-keys) on each usage product that should track per-seat consumption. The product's group keys must reference group keys already defined on the underlying billable metric.
  </Step>

  <Step title="Include seat_id in your usage events">
    Every usage event you send to Metronome must include a `seat_id` property so usage is correctly attributed to the right seat. Here's an example:

    ```json theme={null}
    {
      "event_type": "video_generation",
      "properties": {
        "model_name": "claude-3-opus",
        "resolution": "1080p",
        "environment": "production",
        "video_duration_seconds": 20,
        "seat_id": "example@metronome.com"
      },
      "transaction_id": "21f00039-0572-4f63-bf0f-b19faa3d10f8",
      "customer_id": "94fbf9f3-2826-4503-8446-013c68817744",
      "timestamp": "2025-10-15T15:23:48.751Z"
    }
    ```

    The `seat_id` value should be a stable, unique identifier for each seat—such as an email address or user ID.
  </Step>
</Steps>

### Configure the contract

Specify [`quantity_management_mode`](/api-reference/contracts/create-a-contract#body-subscriptions-items-quantity_management_mode) as `SEAT_BASED`. Then, instead of using the `quantity` field to pass the number of seats, populate the `seat_config`. This object is composed of three fields:

* `initial_seat_ids`: An array representing the unique identifier for each seat.
* `initial_unassigned_seats_quantity`: The number of seats that do not yet have a user associated to it. This will add to the total seat count for the subscription, but will not generate credits until a `seat_id` is specified.
* `seat_group_key`: The presentation group key provided on the usage products. Metronome uses this key to map the `seat_id` to the correct usage and products.

An example contract call is shown below:

```json theme={null}
{
    "customer_id": "1f79c5c6-400a-4be4-9573-30c667454e4c",
    "rate_card_id": "79b2716d-530c-4ff9-86f8-3ee91f442b1b",
    "starting_at": "2025-09-01T00:00:00Z",
    "name": "Extend RC 2",
    "billing_provider_configuration": {
        "billing_provider_configuration_id": "e045c62b-65e7-4e84-a924-3f06f8b621d0"
    },
    "subscriptions": [
        {
            "collection_schedule": "advance",
            "proration": {
                "invoice_behavior": "bill_on_next_collection_date",
                "is_prorated": true
            },
            "subscription_rate": {
                "billing_frequency": "annual",
                "product_id": "ed518bcb-acc1-4cd8-85dd-880c2eb38994"
            },
            "description": "pro plan no additions",
            "name": "Pro Plan",
            "custom_fields": {
                 "plan_tier": "pro"
            },
            "quantity_management_mode": "SEAT_BASED",
            "seat_config": {
                "initial_seat_ids": ["seat1@metronome.com", "seat2@metronome.com", "seat3@metronome.com"],
                "seat_group_key": "seat_id"
            },
            "temporary_id": "pro_plan_annual"
        }
    ],
    "recurring_commits": [
        {
            "product_id": "35a467c7-fc24-46c2-884b-66af8d349674",
            "access_amount": {
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "unit_price": 1000
            },
            "invoice_amount": {
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "unit_price": 1000,
                "quantity": 1
            },
            "priority": 100,
            "starting_at": "2025-09-01T00:00:00Z",
            "ending_before": "2025-11-16T00:00:00Z",
            "commit_duration": {
                "value": 1
            },
            "rollover_fraction": 0.5,
            "subscription_config": {
                "apply_seat_increase_config": {
                    "is_prorated": true
                },
                "subscription_id": "pro_plan_annual",
                "allocation": "INDIVIDUAL"
            }
        }
    ]
}
```
