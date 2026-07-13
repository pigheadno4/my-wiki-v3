<!-- Source URL: https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set prepaid balance thresholds

Use *prepaid balance threshold billing* to enable a prepaid credit model for your products. This billing model requires customers to pay for usage ahead of using the product and to maintain a positive balance to continue accessing the product. Prepaid credits are modeled as [commits](/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit) in Metronome.

Prepaid balance thresholds work with both fiat currencies (such as USD) and [custom pricing units](/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits) (such as tokens or credits). This means you can configure auto recharge for customers whose balances are denominated in custom pricing units, not just fiat currency.

Prepaid balance thresholds enable:

* **Auto recharge:** Automatically recharge a customer's balance when it drops to the `threshold_amount`
* **Manual purchase:** [Manually purchase commits](/guides/pricing-packaging/billing-model-guides/enterprise-commit/) for customers who don't want to enable auto recharge
* **Payment gating:** Gate the release of the commit balance, from an auto recharge or a manual purchase, based on successful collection of payment

## Set up auto recharge with balance thresholds

Configuring auto recharge of the customer's balance on a contract ensures they never lose access to the product.

### Create a contract with balance thresholds

When you [create a contract](/api-reference/contracts/create-a-contract/) in Metronome, you can optionally configure a `prepaid_balance_threshold_configuration`. This config dictates:

* The `threshold_amount` for the customer's contract: the balance level when a customer is recharged.
  * **Note:** When evaluating whether the `threshold_amount` has been reached, Metronome considers the total balance of all contract- and customer-level commits and credits. [Individual seat-scoped credits](https://docs.metronome.com/guides/pricing-packaging/subscription/provision-your-customer#individual-seat-credit) are not included in this calculation.
* The `recharge_to_amount`: the balance the customer is topped up to after a recharge initiates.
* A `payment_gate_config`: configure whether to gate the release of balance on payment and what gateway to use.
  * Select `EXTERNAL` if you use a gateway that Metronome doesn't currently support.
  * If using Stripe, configure `PAYMENT_TYPE` to dictate whether payment is sent as an invoice through Stripe Billing or directly as a `paymentIntent` to Stripe's payment gateway.
  * If using Stripe, select your existing tax provider.
* If the config `is_enabled`. If a payment fails and payment gating is enabled, this shifts to `false`.

<Warning>
  **CONFIGURE BILLING**

  If using Stripe as your payment gateway, ensure there's a valid Stripe billing configuration set on the contract. Additionally, set `is_enabled` to `true` if you want Metronome to immediately evaluate the contract after its creation.
</Warning>

Additionally, users can optionally configure a `discount_config` on the `prepaid_balance_threshold_configuration`. This will discount the amount invoiced to the customer based on a percentage, where the invoice amount will be X% discounted from the access amount granted:

* `fraction`: the discount applied to the invoice amount, represented as a fraction
* `cap`: optionally the cap the discounted purchases up to an `amount`. The amount is tracked via a [spend tracker](/guides/customers-billing/manage-customers/spend-trackers). Once the accumulated spend hits this cap, new recharges will not be discounted for the remainder of the period defined in the spend tracker.

<Note>
  **DISCOUNTS WITH CPUS**

  When using Threshold Billing with CPUs, the invoice schedule amount is calculated via the overage rate. For example, if the conversion rate between AI credits and USD was 2:1, then a recharge for 100 AI credits will cost 50 USD. If there was a discount of 10% set on the config, the 100 AI credits would now cost 45 USD.
</Note>

Create contracts with prepaid balance thresholds in the [Metronome app](https://app.metronome.com/) or using the [Metronome API](/api-reference/contracts/create-a-contract).

```json theme={null}
{  
    "customer_id": "6352d562-213f-4a6e-819f-58fdabc3f2b9",  
    "rate_card_id": "a7bc3775-b651-46b6-b7e4-d225a7e55c4c",  
    "starting_at": "2025-05-01T00:00:00.000Z",  
    "billing_provider_configuration": {  
        "billing_provider_configuration_id": "0d40d6ef-6a79-45c2-a716-13eed27a9c8d"  
    },  
    "prepaid_balance_threshold_configuration": {  
        "commit": {  
            "product_id": "d6be3bf4-1669-40c9-a8b1-388bb167ab16",  
            "name": "prepaid_commit",  
            "description": "hello_its_me_im_in_california_dreaming"  
        },  
        "is_enabled": true,  
        "payment_gate_config": {  
            "payment_gate_type": "STRIPE",  
            "stripe_config": {  
                "payment_type": "PAYMENT_INTENT"  
            }  
        },  
        "threshold_amount": 500,  
        "recharge_to_amount": 2100,
        "discount_config": {
          "fraction": 0.9
        }
    }  
}
```

<Note>
  **RECHARGE MINIMUMS**

  When setting up Auto Recharge, the `recharge_threshold` has a minimum value of \$5, and the `recharge_to amount` must always be at least \$10 higher than your threshold. For example, if your threshold is \$10, your `recharge_to_amount` must be at least \$20.

  These minimums apply regardless of whether the balance is denominated in fiat currency or a custom pricing unit. When using custom pricing units, the threshold and recharge amounts are evaluated in the custom pricing unit and converted to fiat currency using the conversion rate defined on the customer's rate card.
</Note>

### Auto recharge with custom pricing units

Prepaid balance thresholds support [custom pricing units](/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits) in addition to fiat currencies. When a customer's contract uses a custom pricing unit (such as tokens or AI credits), the `threshold_amount` and `recharge_to_amount` are expressed in that custom pricing unit. Metronome converts the recharge amount to fiat currency using the conversion rate defined on the rate card when processing payment.

For example, consider an AI platform that prices usage in a custom pricing unit called "AI Tokens," where 1 AI Token = \$0.10 USD:

* The customer's contract has a prepaid balance of 500 AI Tokens
* You set a `threshold_amount` of 50 AI Tokens and a `recharge_to_amount` of 500 AI Tokens
* When the customer's balance drops to 50 AI Tokens, Metronome initiates an auto recharge
* Metronome creates a commit for 450 AI Tokens (the difference to reach 500) and charges the customer \$45.00 USD (450 × \$0.10) through the configured payment gateway

The conversion rate defined on the rate card determines how the custom pricing unit amount maps to the fiat currency charge. To learn how to set up custom pricing units and configure conversion rates on a rate card, see [Set currencies and custom pricing units](/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits).

### Update the contract's prepaid balance threshold

Update or add a `prepaid_balance_threshold_configuration` by editing the contract. For example, you can update the `threshold_amount` on a contract.

Note that these changes take effect immediately and Metronome forces an evaluation of the customer's current balance on each config change.

Edit contracts in the [Metronome app](https://app.metronome.com/) or with the [Metronome API](/api-reference/contracts/edit-a-contract). This API call adds a prepaid balance threshold to a contract:

```json theme={null}
{  
    "customer_id": "6352d562-213f-4a6e-819f-58fdabc3f2b9",  
    "contract_id": "e066a32a-3b59-4d07-a91f-a9e084903d45",  
    "update_prepaid_balance_threshold_configuration": {  
        "threshold_amount": 600,  
        "recharge_to_amount": 2700  
    }  
}
```

### Exclude balances from threshold calculations

By default, Metronome counts all prepaid commits and credits toward a contract's available balance when evaluating whether a threshold has been reached (with the exception of seat-scoped commits and credits, which are always excluded).

Use threshold balance specifiers to further narrow which balances count toward the threshold. This is useful when a contract contains commits or credits that serve different purposes and you don't want all of them factored into recharge decisions. Metronome will only trigger a recharge when the balances matching your specifier drop below the configured threshold\_amount.

For example, consider a database company that offers its core product on a prepaid credit model with auto top-up enabled. The company is launching an adjacent AI product and wants to give all customers \$10 in product-specific trial credits for the new product. Without any configuration, Metronome counts all prepaid balances — including the AI trial credits — when evaluating whether a recharge should trigger. This means a customer with a threshold amount of \$15 with \$10 in general credits and \$10 in AI trial credits has a combined balance of \$20, which fails to trigger a top-up even though the customer is running low on their general credits.

To ensure top-up fires based on general credit balance only, make a single API call to edit the contract to introduce the new AI trial credit with a custom field (`credit_type: ai_trial`) and exclude that tag from the threshold billing balance calculation.

```json theme={null}
{  
    "customer_id": "6352d562-213f-4a6e-819f-58fdabc3f2b9",  
    "contract_id": "e066a32a-3b59-4d07-a91f-a9e084903d45",  
    "update_prepaid_balance_threshold_configuration": {  
        "threshold_balance_specifiers": [{
            "exclude": [{
                "custom_field_filters": [{
                    "entity": "ContractCreditOrCommit",
                    "key": "credit_type",
                    "value": "ai_trial"
                  }]
              }]
          }]
    },
    "add_credits": [
    {
      "product_id": "ai-trial-product-id",
      "access_schedule": {
        "schedule_items": [
          {
            "amount": 1000,
            "starting_at": "2025-05-01T00:00:00.000Z",
            "ending_before": "2025-06-01T00:00:00.000Z"
          }
        ]
      },
      "custom_fields": {
        "credit_type": "ai_trial"
      },
      "priority": 1
    }
  ]
}
```

When multiple `custom_field_filters` objects are specified within the threshold balance specifier's exclusion condition, Metronome excludes any balance that matches at least one of the filters (OR logic). For example, you may want to run multiple trial credits. The following call to editContract excludes both commits and credits tagged with `credit_type: ai_trial` OR commits and credits tagged with `credit_type: june_product_launch_trial`.

```json theme={null}
{  
    "customer_id": "6352d562-213f-4a6e-819f-58fdabc3f2b9",  
    "contract_id": "e066a32a-3b59-4d07-a91f-a9e084903d45",  
    "update_prepaid_balance_threshold_configuration": {  
        "threshold_balance_specifiers": [{
            "exclude": [{
                "custom_field_filters": [{
                    "entity": "ContractCreditOrCommit",
                    "key": "credit_type",
                    "value": "ai_trial"
                  }],
                "custom_field_filters": [{
                    "entity": "ContractCreditOrCommit",
                    "key": "credit_type",
                    "value": "june_product_launch_trial"
                  }]
              }]
          }]
    }
}
```

If multiple custom field key-values are specified within a single `custom_field_filters` array, balances are only excluded when they match all key-value pairs within the filter (AND logic). For example, the following call would exclude only commits and credits that had both the custom fields `credit_type: ai_trial` AND `is_active: true`. Note that you cannot repeat the same custom field key within one custom field filter.

```json theme={null}
{  
    "customer_id": "6352d562-213f-4a6e-819f-58fdabc3f2b9",  
    "contract_id": "e066a32a-3b59-4d07-a91f-a9e084903d45",  
    "update_prepaid_balance_threshold_configuration": {  
        "threshold_balance_specifiers": [{
            "exclude": [{
                "custom_field_filters": [
                  {
                    "entity": "ContractCreditOrCommit",
                    "key": "credit_type",
                    "value": "ai_trial"
                  },
                  {
                    "entity": "ContractCreditOrCommit",
                    "key": "is_active",
                    "value": "true"
                  }
                ]
              }]
          }]
    }
}
```

## Prepaid balance threshold billing lifecycle

To best utilize prepaid balance threshold billing, consider its lifecycle: the actions Metronome takes and what actions you may need to take.

### 1. Charge for prepaid balance threshold amount (Metronome)

Once configured, Metronome evaluates the remaining balance available to the customer on the contract to determine when the `threshold_amount` has been reached. If the `payment_gate_config` is set to Stripe, Metronome attempts to charge the customer in Stripe.

If payment is successful, Metronome creates a commit for the amount that recharges the customer back to the `recharge_to_amount`.

### 2. Manage notifications (you)

Metronome fires three types of webhook notifications for prepaid balance threshold billing:

* `payment_gate.threshold_reached` when the customer hits their threshold.
* `payment_gate.payment_status` after payment has been attempted. The status of that payment, `paid` or `failed`, is denoted in the `payment_status` field.
* `payment_gate.payment_pending_action_required` if intervention is required to process payment.

Your webhook endpoint must be configured to handle these notifications accordingly.

### 3. Handle failed payments (you)

If a payment fails, you receive a `payment_gate.payment_status` with the value of `failed`. Additionally, the contract's `is_enabled` field is set to `false`.

You should expect to see a voided invoice in Metronome and Stripe for this transaction.

At this point, you should follow up with your customer directly or by creating an automated workflow triggered by this webhook notification.

Once you're ready to reattempt payment, set the contract's `is_enabled` field to `true`. This forces the contract to evaluate against the `threshold_amount`, resulting in a new payment attempt.

<Note>
  **No Automatic Retries**

  Metronome does not automatically retry failed payments (as any automatic retries would likely fail, too).
</Note>

## Use an external payment gate

If using the `EXTERNAL` option for `payment_gate_type`, you are responsible for facilitating payment and letting Metronome know the response. Follow this workflow:

1. Set the prepaid balance threshold config with `payment_gate_type` set to `EXTERNAL`.
2. Listen for `payment_gate.external_initiate` that indicates Metronome is ready to receive the outcome of the payment.
3. Save the `workflow_id` - you need this to release the commit.
4. Charge the customer in your payment gateway of choice.
5. Call [commits/threshold-billing/release](/api-reference/credits-and-commits/release-external-payment-gate-threshold-commit/) to either release the commit on successful payment, or cancel the commit in case of failure.
