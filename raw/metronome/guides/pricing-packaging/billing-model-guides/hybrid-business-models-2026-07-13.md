<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/hybrid-business-models.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Launch a hybrid business model

Modern SaaS pricing is evolving. Many companies that previously charged a flat rate per seat are now moving toward hybrid pricing models that combine recurring revenue with usage-based components. Metronome supports a wide range of hybrid business models, helping you balance predictability with upside.

This guide describes how to launch a hybrid business model using Metronome, including how to:

* Create customer contracts
* Cut off access to features when the customer runs out of credits
* Set up your end-user billing experience

## Use case​

This guide demonstrates a hybrid business model using SeatsCo, a fictional company with an existing seats-based model. In this example, you're introducing SeatsCo's first AI features, and you want to add a usage-based element to your AI products to protect margins and capture upside from power users.

Here's how the new *Team plan* pricing model works:

* The customer pays \$10/month (or \$100/year) per seat, and each seat includes 100 AI credits per month for AI products.
* The AI credits are pooled and available to anyone on the team. Each month's AI credits expire at the end of the month—they are use it or lose it.
* The AI credits apply to three AI products: AI Assistant, AI Preview, and AI Summary.
* Once the AI credits run out, the customer can no longer use AI functionality on the SeatsCo platform.
* The customer can choose to wait until the next month for their AI credits to reset, or they can purchase a top-up pack of credits. Top-up packs have a year-long expiry and cost \$80 for 1,000 credits.

When you enable this pricing model, Metronome fully owns the provisioning of credits. This means you don’t need to maintain any code to calculate prorations or grant new credits when the customer signs up for a new seat.

<Info>
  **INFO**

  Another common pricing model is seat-scoped credits, where each seat receives credits only they can use. See [Individual seat credit](/guides/pricing-packaging/subscription/provision-your-customer#individual-seat-credit) to model this use case in Metronome.
</Info>

## Metronome building blocks​

In Metronome, the [rate card](/guides/get-started/core-concepts/create-manage-rate-cards) is your centralized price book. This is where you encode pricing for all products, including subscriptions and usage-based products.

Start by setting up these core Metronome objects: a subscription product, billable metrics, usage products, and a rate card.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/billing-model-guides/hybrid-business/hybrid-model-229fb93b63564f29cdebe36b183a6d63.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=3201a981d90d5852bd0c25d12c852b71" alt="Hybrid business model" width="3558" height="1388" data-path="images/docs/pricing-packaging/billing-model-guides/hybrid-business/hybrid-model-229fb93b63564f29cdebe36b183a6d63.png" />
</Frame>

### Create subscription products​

Create a [subscription](/guides/pricing-packaging/billing-model-guides/create-a-subscription) product called Team Plan.

This API call shows how to create a subscription product with the [/v1/contract-pricing/products/create](/api-reference/products/create-a-product) endpoint:

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/products/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "name": "Team Plan",  
    "type": "SUBSCRIPTION"  
  }'
```

### Create usage products​

Create [billable metrics](/guides/get-started/core-concepts/create-billable-metrics/) to track the usage of the AI Assistant, AI Preview, and AI Summary. Then, create [usage products](/guides/get-started/core-concepts/create-products-contracts) referencing those billable metrics.

This API call shows how to create a usage product with the [/v1/contract-pricing/products/create](/api-reference/products/create-a-product) endpoint:

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/products/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "name": "AI Assistant",  
    "type": "USAGE",  
    "billable_metric_id": "00ca093f-f347-4dd3-bb9b-9705f1b015e3",  
    "tags": [  
        "AI Products"  
    ]  
  }'
```

### Create a rate card with subscription and usage products​

After creating your products, create a [rate card](/guides/get-started/core-concepts/create-manage-rate-cards). When creating the rate card, define the conversion rate between the custom pricing unit *AI credits* and USD.

This API call shows how to create a rate card with a credit pricing conversion using the [/v1/contract-pricing/rate-cards/create](/api-reference/rate-cards/create-a-rate-card) endpoint:

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/rate-cards/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "name": "Subscription and Usage Pricebook",  
    "fiat_credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
    "credit_type_conversions": [  
        {  
            "custom_credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",  
            "fiat_per_custom_credit": 100  
        }  
    ]  
  }'
```

Next, add the products you just created to the rate card.

This API call uses the [/contract-pricing/rate-cards/addRates](/api-reference/rate-cards/add-a-rate) endpoint to add the subscription product Team plan to the rate card with two billing frequencies: monthly and annual. Team plan is priced in USD. It also adds three usage products to the rate card: AI Assistant, AI Preview, and AI Summary, all priced in the custom pricing unit of AI credits.

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/rate-cards/addRates \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
    "rates": [  
        {  
            "product_id": "76f29162-7f5c-4ee6-89ed-ebbd592d767e",  
            "starting_at": "2025-01-01T00:00:00.000Z",  
            "entitled": true,  
            "rate_type": "FLAT",  
            "price": 10000,  
            "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
            "billing_frequency": "yearly"  
        },  
        {  
            "product_id": "76f29162-7f5c-4ee6-89ed-ebbd592d767e",  
            "starting_at": "2025-01-01T00:00:00.000Z",  
            "entitled": true,  
            "rate_type": "FLAT",  
            "price": 1000,  
            "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
            "billing_frequency": "monthly"  
        },  
        {  
            "product_id": "2fefe8b6-ca37-4355-a699-0a318e868902",  
            "starting_at": "2025-01-01T00:00:00.000Z",  
            "entitled": true,  
            "rate_type": "FLAT",  
            "price": 12,  
            "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6"  
        },  
        {  
            "product_id": "c3b1ecc0-66ec-4a18-8782-7496c6e05248",  
            "starting_at": "2025-01-01T00:00:00.000Z",  
            "entitled": true,  
            "rate_type": "FLAT",  
            "price": 5,  
            "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6"  
        },  
        {  
            "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
            "starting_at": "2025-01-01T00:00:00.000Z",  
            "entitled": true,  
            "rate_type": "FLAT",  
            "price": 7,  
            "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6"  
        }  
    ]  
  }'
```

At any point you can [update the rate card](/guides/get-started/core-concepts/create-manage-rate-cards#update-a-rate-card%E2%80%8B) to evolve the rates you charge for subscription and usage products.

## Implement a hybrid model for a customer​

A customer’s contract encodes their specific agreement with SeatsCo. To model hybrid pricing models where a seat comes with a given amount of credits, Metronome can link recurring credits and commits to a subscription object. When you increment or decrement the subscription’s quantity, credits are automatically provisioned and tracked based on proration behaviors that you set.

### Create a subscription and linked recurring credit​

Create a [customer contract](/guides/customers-billing/manage-customers/provision-a-customer#provision-a-customer-contract) referencing your rate card.

In this example, the customer signed up for the Team plan with an annual payment and an initial quantity of 4 seats. For each seat, the customer receives 100 AI credits in a shared pool monthly.

This API call shows how to create the described contract using the [/contracts/create](/api-reference/contracts/create-a-contract) endpoint. The `subscription_config` settings in this example indicate that if the customer adds a seat mid-month, the amount of AI credits granted for that seat get prorated.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "starting_at": "2025-06-01T00:00:00Z",  
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c",  
    "subscriptions": [  
      {  
        "collection_schedule": "advance",  
        "initial_quantity": 4,  
        "proration": {  
          "invoice_behavior": "BILL_IMMEDIATELY",  
          "is_prorated": true  
        },  
        "subscription_rate": {  
          "billing_frequency": "annual",  
          "product_id": "76f29162-7f5c-4ee6-89ed-ebbd592d767e"  
        },  
        "temporary_id": "team_plan_annual"  
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
        "recurrence_frequency": "monthly",  
        "product_id": "652e1298-7638-45a8-b691-cdf47e46cbc8",  
        "starting_at": "2025-06-01T00:00:00Z",  
        "subscription_config": {  
          "subscription_id": "team_plan_annual",  
          "apply_seat_increase_config": {  
            "is_prorated": true  
          }  
        }  
      }  
    ],  
    "billing_provider_configuration": {  
    "billing_provider":"STRIPE"  
    }  
  }'
```

### Increase seats and automatically provision credits​

When the customer signs up for another seat, [edit the contract](/manage-product-access/edit-contract/) to increment the quantity. You don’t need to touch the credits—Metronome automatically handles their provisioning and proration.

This API call shows how to increment the subscription seat quantity using the [editContract](/api-reference/contracts/edit-a-contract) endpoint:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c",  
    "contract_id": "d701e556-c30e-4e9c-98af-304782d49345",  
    "update_subscriptions": [  
        {  
            "subscription_id": "e8cb4466-3e55-485e-b0ae-d83dfc4e82e1",  
            "quantity_updates": [  
                {  
                    "starting_at": "2025-07-03T00:00:00Z",  
                    "quantity_delta": 1  
                }  
            ]  
        }  
    ]  
  }'
```

When a customer removes a seat, decrement the seat quantity. This API call shows how to decrement the quantity using the [editContract](/api-reference/contracts/edit-a-contract) endpoint:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c",  
    "contract_id": "d701e556-c30e-4e9c-98af-304782d49345",  
    "update_subscriptions": [  
        {  
            "subscription_id": "e8cb4466-3e55-485e-b0ae-d83dfc4e82e1",  
            "quantity_updates": [  
                {  
                    "starting_at": "2025-07-10T00:00:00Z",  
                    "quantity_delta": -1  
                }  
            ]  
        }  
    ]  
  }'
```

### Set threshold notification on credit balance

You can set [threshold notifications](/guides/customers-billing/set-up-notifications/create-and-manage-notifications) on credit balance to receive webhooks when the customer is almost out of AI credits and when they've fully depleted their AI credits.

Upon receiving these webhooks, you can gate the customer’s access to using any more AI credits until they purchase a top-up credit pack, or the month resets.

This API call shows how to create a threshold notification when the customer has 10 AI credits remaining using the [/alerts/create](/api-reference/alerts/create-an-alert) endpoint.

```bash theme={null}
curl https://api.metronome.com/v1/alerts/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "alert_type": "low_remaining_contract_credit_and_commit_balance_reached",  
    "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",  
    "threshold": 10,  
    "name": "10 AI credits remaining reached",  
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c"  
  }'
```

### Enable purchase of top-up credits​

If a customer purchases a top-up credit pack, edit their contract to add the purchased credits. To ensure that the monthly included AI credits are always consumed first, set the priority of the purchased credits to a larger number priority than the priority of the included AI credits.

You can choose to [gate these credits](/pricing-packaging/apply-credits-commits/manual-payment-gated-commits/) on payment in Stripe or any other billing provider. If you gate the payment, the credits only release once they're paid for, ensuring you’re protected against fraud.

In this example, the customer purchased a pack of top-up credits at the discounted rate of \$80 for 1,000 AI credits. These credits don't expire until a full year after their purchase, unlike the monthly included credits.

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c",  
    "contract_id": "d701e556-c30e-4e9c-98af-304782d49345",  
    "add_commits": [  
        {  
            "product_id": "d6be3bf4-1669-40c9-a8b1-388bb167ab16",  
            "type": "prepaid",  
            "invoice_schedule": {  
                "schedule_items": [  
                    {  
                        "timestamp": "2025-07-07T00:00:00.000Z",  
                        "amount": 8000  
                    }  
                ]  
            },  
            "access_schedule": {  
                "schedule_items": [  
                    {  
                        "amount": 1000,  
                        "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",  
                        "starting_at": "2025-07-07T00:00:00.000Z",  
                        "ending_before": "2026-07-07T00:00:00.000Z"  
                    }  
                ]  
            },  
            "payment_gate_config": {  
                "payment_gate_type": "STRIPE",  
                "tax_type": "STRIPE",  
                "stripe_config": {  
                    "payment_type": "PAYMENT_INTENT"  
                }  
            },  
            "priority": 100  
        }  
    ]  
  }'
```

## Optimize your customer's experience​

Use Metronome to offer your customers robust billing experiences.

### Create the customer billing experience​

With SeatsCo's new usage-based pricing component, it's important to provide a more robust customer billing experience, so customers have real-time visibility into their remaining balance and can set cost controls on a per-seat basis.

### Get the balance of the credit​

Use the [listCustomerBalances](/api-reference/credits-and-commits/list-balances) endpoint to show the current balance in AI credits, inclusive of usage by all seats.

### Set cost controls per seat​

The administrator of a team may want to cap the number of AI credits an individual user can spend. To do this, pass in the `user_id` performing an action in your event data, and set that `user_id` as a [group key](/guides/get-started/core-concepts/create-billable-metrics#3-define-group-keys%E2%80%8B) on the relevant billable metrics.

Then, create a spend alert for a specific `user_id`. You can cut the user off from spending more AI credits, notify their administrator, or notify them.

For example, this example spend alert sends a webhook notification when `user_id = user_1234` spends more than 1,000 AI credits in the billing period.

```bash theme={null}
curl https://api.metronome.com/v1/alerts/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "alert_type": "spend_threshold_reached",  
    "credit_type_id": "d3cb2827-dcb5-44af-9354-947a7197b9a6",  
    "name": "user_1234 AI credit spend alert",  
    "threshold": 1000,  
    "customer_id": "d8319d6f-8ee0-43a7-b76f-d7587c0a811c",  
    "group_values": [{  
        "key": "user_id",  
        "value": "user_1234"  
    }]  
  }'
```

## Conclusion​

SeatsCo is now ready to launch AI features with their new hybrid business model! They've set up a subscription plan with AI credits per seat, automatic provisioning and proration as seats are added or removed, low credit balance alerts, and the ability for customers to purchase top-up credits. SeatsCo also provides customers a transparent billing experience, with clear visibility into usage and spend controls.
