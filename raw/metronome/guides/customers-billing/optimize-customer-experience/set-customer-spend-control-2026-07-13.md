<!-- Source URL: https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/set-customer-spend-control.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enforce spend thresholds

To reduce fraud in Product-Led Growth (PLG) workflows, Metronome supports *spend threshold billing*. This feature allows you to cap the amount a customer can spend before being charged, thereby limiting your exposure to uncollected revenue.

After applying a spend threshold to a contract, watch for webhook notifications to be alerted when payments succeed or fail.

## Create a contract with spend thresholds

When you create a contract in Metronome, you can optionally configure a `spend_threshold_configuration`. This config dictates:

* The `threshold_amount` for the customer's contract: how much they can spend before a payment attempt is triggered
* The `payment_gate_config`:
  * Configure whether to payment gate the release of the commit and what gateway to use. Select `EXTERNAL` if you are using a gateway Metronome does not currently support. See [Use an external payment gate](/guides/customers-billing/optimize-customer-experience/set-customer-spend-control#using-external-payment-gate) for details.
  * If using Stripe, configure `PAYMENT_TYPE` to dictate whether payment is sent as an invoice through Stripe Billing or directly as a `paymentIntent` to Stripe's payment gateway.
  * If using Stripe, select your existing tax provider.
* What `product_id` should be used to represent the commit: the `product_id` dictates what the customer sees on their incremental invoice

<Warning>
  **CONFIGURE BILLING**

  If using Stripe as your payment gateway, ensure there is a valid Stripe billing configuration set on the contract. Additionally, set `spend_threshold_configuration.is_enabled` to `true` if you want Metronome to immediately evaluate the contract after its creation.
</Warning>

Create contracts with spend threshold in the [Metronome app](https://app.metronome.com/) or using the [Metronome API](/api-reference/contracts/edit-a-contract).

```json theme={null}
{
  "customer_id": "8cecbf69-960f-4f66-9575-edebb7d95e88",
  "rate_card_id": "a7bc3775-b651-46b6-b7e4-d225a7e55c4c",
  "starting_at": "2025-04-01T00:00:00.000Z",
  "billing_provider_configuration": {
    "billing_provider_configuration_id": "211ef270-098f-422c-9ca8-7999bb9156cb"
  },
  ...
  "spend_threshold_configuration": {
    "commit": {
      "product_id": "d6be3bf4-1669-40c9-a8b1-388bb167ab16",
      "name": "black_mesa_commit",
      "description": "hello_its_me_im_in_california_dreaming"
    },
    "is_enabled": true,
    "payment_gate_config": {
      "payment_gate_type": "NONE"
    },
    "threshold_amount": 200
  }
}
```

## Update a contract's spend threshold

You can update or add a `spend_threshold_configuration` at any point by editing the user's contract. Add spend threshold limits to existing, non-limited contracts or change existing limits on a contract (for example, after some period of successful payments).

Note that these changes take effect immediately.

Edit contracts in the [Metronome app](https://app.metronome.com/) or with the [Metronome API](/api-reference/authorization). This API call adds a spend threshold to a contract:

```json theme={null}
{
  "customer_id": "52f5a554-b887-4899-b919-4eb7789c6bf3",
  "contract_id": "8a5529d3-f353-4231-bedf-7e83f5e9331d",
  "add_spend_threshold_configuration": {
    "commit": {
      "product_id": "d6be3bf4-1669-40c9-a8b1-388bb167ab16",
      "name": "threshold_charge",
      "description": "one time for the one time"
    },
    "is_enabled": true,
    "payment_gate_config": {
      "payment_gate_type": "STRIPE",
      "stripe_config": {
        "payment_type": "INVOICE"
      }
    },
    "threshold_amount": 100
  }
}
```

This API call updates an existing spend threshold:

```json theme={null}
{
  "customer_id": "8cecbf69-960f-4f66-9575-edebb7d95e88",
  "contract_id": "6058587f-763c-400f-a822-3edb3eb2b86b",
  "update_spend_threshold_configuration": {
    "is_enabled": true,
    "threshold_amount": 100,
    "payment_gate_config": {
      "payment_gate_type": "STRIPE",
      "stripe_config": {
        "payment_type": "INVOICE"
      }
    }
  }
}
```

## Manage notifications and handle failed payments

To learn how to manage webhook notifications from Metronome and handle failed customer payments, see [the threshold billing lifecycle](/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds#prepaid-balance-threshold-billing-lifecycle).

## Using external payment gate

If using the `EXTERNAL` option for `payment_gate_type`, you are responsible for facilitating payment and letting Metronome know the response. Follow this workflow:

* Set the spend threshold config with `payment_gate_type` set to `EXTERNAL`

* Listen for `payment_gate.external_initiate` that indicates Metronome is ready to receive the outcome of the payment

* Save the `workflow_id` - you will need this to release the commit

* Charge the customer in your payment gateway of choice

* Call [commits/threshold-billing/release](/api-reference/credits-and-commits/release-external-payment-gate-threshold-commit) to either release the commit on successful payment, or cancel the commit in case of failure.
