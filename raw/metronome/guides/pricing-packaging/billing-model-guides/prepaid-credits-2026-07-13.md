<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/prepaid-credits.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Launch a prepaid credits business model

Prepaid credits refers to a payment model where customers purchase a batch of credits upfront. These credits are then consumed as the customer uses your software's resources or features. Unlike pay-as-you-go models, users must maintain a positive credit balance to continue accessing your platform's services. Once credits are fully depleted, a user’s access suspends until they purchase additional credits.

The prepaid credits model creates a clear pay-before-you-use framework that's gained traction across various SaaS platforms, particularly those concerned with reducing financial risk. Customers typically purchase credit packages through a company's website, selecting from predefined amounts based on their anticipated usage needs.

Companies implement prepaid credits models at different stages. For example:

* Risk-conscious startups seeking to eliminate payment defaults
* Established companies looking to reduce revenue leakage and churn
* Businesses operating in markets with higher fraud potential

In this guide, you'll learn how to implement a prepaid credits business model on Metronome, including setting up auto-recharge options that allow users to maintain uninterrupted service while preserving your upfront payment requirement.

## Use case​

In this guide, your customer Example Inc. signs up for your platform using Stripe as your billing provider. They purchase 2,000 credits to use on your platform, which expire after one year. When the Example Inc. user clicks `purchase credits` in your system, payment is immediately triggered, and credits are only granted once payment is confirmed successful. With credits in hand, they can use your system and watch their credit balance decrease in real time. Once their balance reaches zero, your system should cut them off from further use until they purchase another batch of credits.

## Metronome building blocks​

Regardless of the commercial model you choose, Metronome’s core job is to turn usage data into accurate spend data.

Before implementing the prepaid credit model, set up these core Metronome objects:

* [Billable metrics](/guides/get-started/core-concepts/create-billable-metrics/): Create a billable metric for each unit of what customers consume by using your platform (like compute, storage, or API calls).
* [Product](/guides/get-started/core-concepts/create-products-contracts): Create a usage-based product for each of your billable metrics so you can configure how your usage spend appears to your users. Also create a fixed product to represent the credit-purchased charges.
* [Rate card](/guides/get-started/core-concepts/create-manage-rate-cards) and rates: Create a rate card that contains the burn-down rates for each of the usage-based products that you plan to offer to your users.

To learn how to set up these objects, see the [Quickstart](/launch-guides/quickstart/).

## Implement prepaid credits​

After completing this guide, you’ll have a prepaid credits model built out in Metronome.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/billing-model-guides/prepaid-credits/prepaid-credits-model-edc8c2b037014f4ee95500d904c76eed.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=415b15a7888f704436d94b5aa9a67a3a" alt="Prepaid credits model" width="1817" height="525" data-path="images/docs/pricing-packaging/billing-model-guides/prepaid-credits/prepaid-credits-model-edc8c2b037014f4ee95500d904c76eed.png" />
</Frame>

### Set up a billing provider​

Within the prepaid credit flow, Metronome facilitates payment from your billing provider to immediately charge customers and ensure that payments complete before credits are granted. As such, you first need to connect your billing provider to allow Metronome to send and finalize invoices on your behalf.

The most common billing provider in the prepaid credits flow is Stripe. To learn how to connect your Stripe account, see [Invoice with Stripe](/integrations/invoice-integrations/stripe).

### Set up a webhook​

The prepaid credits flow relies on your system receiving real-time webhook notifications from Metronome. These are used to send a signal:

* When users run out of balance, so that your system can cut off their platform access
* Upon successful or failed payment, so that your system can enable or disable customers as needed

Before starting, ensure that you have a [webhook destination](/guides/platform-configuration/setup-webhooks) set up to receive requests from Metronome.

### Configure the credit lifecycle​

Implementing a prepaid credits model on Metronome involves taking steps at different parts of the purchase lifecycle.

#### Customer sign-up​

When a customer signs up in your application:

* Ensure that you've created their customer record in Metronome and your billing provider (for example, Stripe).
* Start their contract to encode the rates that Metronome should use as customer usage events start to flow through the system.

The end-to-end flow to purchase when using Stripe is:

1. A user signs up for an account in your platform, entering their credit card information.
2. You create the user as a customer in Stripe.
3. You set their entered payment method as their default in Stripe.
4. You create a customer in Metronome, linking the Stripe customer ID.
5. You create a contract for the customer in Metronome.

<Tip>
  **TIP**

  We recommend configuring contracts with first of the month billing. While users won't get billed in arrears in a prepaid credits model, using first of the month billing makes it easier to group spend revenue data by monthly boundaries.
</Tip>

See this example of using the `customers` endpoint to create a customer, linking to the customer's Stripe customer ID:

```bash theme={null}
curl https://api.metronome.com/v1/customers \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "ingest_aliases": [  
        "team@example.com"  
    ],  
    "name": "Example, Inc.",  
    "customer_billing_provider_configurations": [  
        {  
            "billing_provider": "stripe",  
            "delivery_method": "direct_to_billing_provider",  
            "configuration": {  
                "stripe_customer_id": "cus_123",  
                "stripe_collection_method": "charge_automatically"  
            }  
        }  
    ]  
  }'
```

See this example of using the `contracts/create` endpoint to create a contract:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
    "starting_at": "2025-04-15T00:00:00.000Z",  
    "billing_provider_configuration": {  
        "billing_provider": "stripe",  
        "delivery_method": "direct_to_billing_provider"  
    }  
  }'
```

As users haven't purchased any credits yet, their default entitlement state in your system should be `false`.

#### Credit purchases​

In a prepaid credits model, customers must have a positive credit balance to be able to use your system. To have a positive credit balance, they must purchase batches of credits. This is generally included in the initial sign-up flow, and customers then have the ability to purchase ad-hoc credits through your platform as needed.

This flow should look like:

1. User clicks **purchase credits in your platform** with the desired amount.

2. You send an API request to Metronome to facilitate the end-to-end prepaid credit. Metronome initiates the payment in Stripe.

   * Upon success, Metronome creates a commit object to increase the customer balance and sends a webhook with notice of a successful payment.
   * Upon failure, Metronome voids the commit object in the system and sends a webhook with notice of a failed payment.

3. Upon successful payment, you set a customer's entitlement state to `true` to allow them to start to spend.

See this example of using the `contracts/edit` endpoint to facilitate the prepaid credit:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
    "add_commits": [  
        {  
            "product_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
            "access_schedule": {  
                "schedule_items": [  
                    {  
                        "amount": 2000,  
                        "ending_before": "2025-04-01T00:00:00.000Z",  
                        "starting_at": "2026-04-01T00:00:00.000Z"  
                    }  
                ]  
            },  
            "invoice_schedule": {  
                "schedule_items": [  
                    {  
                        "amount": 2000,  
                        "timestamp": "2025-04-01T00:00:00.000Z"  
                    }  
                ]  
            },  
            "priority": 10,  
            "payment_gate_config": {  
                "payment_gate_type": "STRIPE"  
            }  
        }  
    ]  
  }'
```

#### Manage entitlement​

We recommend that a customer’s entitlement state is managed within your system and database. At its most simple, this could be a true/false value for a particular customer that's checked before they take an action. We recommend that this is maintained within your system so that it can be fetched with the latency that your system will require, and so that it's resilient to any failures between your system and Metronome.

At a high level, when a customer action is taken, this is the state you should check:

```javascript theme={null}
if (customer_entitled) {  
    do_action();  
    send_usage_to_metronome();  
} else {  
    error("Not enough credits");  
}
```

The customer entitlement state should be informed by whether the customer has an active balance. As such, you should use real-time signals from Metronome to drive the state of this customer entitlement flag. The primary mechanism that we recommend for this is to set an alert for all customers to send when customer balance reaches \$0. This way, Metronome sends you a signal when each customer runs out of credits to change their entitlement state.

Here's an example of a webhook for when a customer reaches 0. This is your signal to set a customer’s `customer_entitled` to `false`.

```json theme={null}
{  
  "id": "8d9cebd2-9c57-4a35-a468-bd73fa2ffa89",  
  "properties": {  
    "customer_id": "ac39ecc3-87ee-4d58-8ec0-24041464a5dd",  
    "alert_id": "618a4ca8-c8d9-4822-addc-bd3008eb8428",  
    "timestamp": "2025-04-07T15:08:44.865Z",  
    "threshold": 0,  
    "alert_name": "Balance low",  
    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
    "remaining_balance": 0,  
    "triggered_by": "usage"  
  },  
  "type": "alerts.low_remaining_contract_credit_and_commit_balance_reached"  
}
```

## Optimize your customer's experience​

Use Metronome to offer experiences to your customers like automatic recharge and spend previews.

### Enable automatic recharge​

You can offer automatic recharge to your customers. This allows them to automatically purchase more credits when a threshold is reached, ensuring that they never reach a \$0 balance. For instance, a customer may opt to the following: when my balance reaches \$5 remaining, recharge me back to \$20. If implemented, they should expect increments of \$15 credit purchases after the initial \$20 purchase.

You can set up a customer’s desired auto recharge threshold on their contract object. Once set up, Metronome handles all of the recharge actions asynchronously based on customer usage. To set this up, use the `threshold_billing_configuration` object within the create contract request:

```bash theme={null}
curl https://api.staging.metronome.com/v1/contracts/create \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "f7ed0bb0-7079-4fd1-baa8-713bf70dcb3b",  
    "rate_card_id": "8664db91-4c22-459a-b3c5-5fb11ce085fe",  
    "starting_at": "2025-04-01T00:00:00.000Z",  
    "credit_balance_threshold_configuration": {  
        "is_enabled": true,  
        "threshold_amount": 300,  
        "recharge_to_amount": 2000,  
        "payment_gate_config": {  
            "payment_gate_type": "STRIPE"  
        },  
        "commit": {  
            "product_id": "ff6c5ff2-28d9-443c-bb49-68df8191b05f"  
        }  
    }  
  }'
```

Once set up, Metronome handles all of the recharge actions asynchronously based on customer usage. As payments happen, Metronome sends webhooks to your system indicating if payments succeed or fail in the billing provider. In the event of payment failure, Metronome sets the status of the recharge settings `is_enabled` to `false`. To remediate, we recommend sending an email or in-platform notification to the customer prompting them to update their billing information. Upon update of this information, you should edit the contract and `set is_enabled` back to `true`, which triggers another recharge.

### Present spend to your customers​

As a customer’s experience with your platform changes when they run out of credits, you should give them the ability to see their balance updated in real time through your platform. The Metronome [listBalances API](/api-reference/credits-and-commits/list-balances) supports these UI components.

This API call shows how to fetch the balance for a particular customer:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/customerBalances/list \  
  -H "Authorization: Bearer $TOKEN" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
    "id": "6162d87b-e5db-4a33-b7f2-76ce6ead4e85",  
    "include_balance": true,  
    "include_contracts_balances": true  
  }'
```

This example table shows how you could display this information to your customer:

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/billing-model-guides/prepaid-credits/commit-tracking-ad8d69832510b0565b8fea1ce51e8d97.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=a19d8d057d11c6e01adc5f8e6d5e0c1a" alt="Commit tracking table" width="2614" height="648" data-path="images/docs/pricing-packaging/billing-model-guides/prepaid-credits/commit-tracking-ad8d69832510b0565b8fea1ce51e8d97.png" />
</Frame>

To view more common workflows for displaying spend data within your application, see [Build API-powered customer dashboards](/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting).
