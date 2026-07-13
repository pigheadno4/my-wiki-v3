<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/manual-payment-gated-commits.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Payment-gated commits

Organizations commonly implement a prepaid model for their PLG customers. Customers must pay for usage in advance of using the product and organizations gate access pending successful payment. This can be implemented in Metronome using payment-gated commits. When a payment-gated commit is created, Metronome facilitates the following:

1. Metronome immediately triggers a payment attempt based on the invoice amount of the commit.
2. If the payment succeeds, Metronome releases the commit and the customer is granted access to the associated balance.
3. If the payment fails, Metronome voids the resource and sends a webhook notification.
4. If further action is required (e.g. for 2F authentication), Metronome sends a webhook notification.

<Note>
  **IMMEDIATELY**

  Metronome initiates payment with your configured billing provider and monitors for completion. In most success cases, payment is completed and credits are released within seconds, but actual timing depends on the payment provider, payment method, and potential authentication challenges.
</Note>

## Before you begin

* Ensure the customer has a default payment method configured in your payment provider (e.g., Stripe); otherwise, payments will fail and commits will not be created.
* Capture and store customer address during your checkout flow. If address is invalid or missing, subsequent payments for the customer will fail.
* **Map the commit's Metronome product to a Stripe product.** Payment-gated commits require that the Metronome product used on the commit has a corresponding Stripe Product ID mapped to it. Without this mapping, Stripe cannot generate the invoice line item and the payment attempt will fail. To configure this mapping, create a `stripe_product_id` custom field on the Metronome product entity, set its value to the corresponding Stripe Product ID, and add a Stripe integration mapping rule from `stripe_product_id` to `invoiceitem.price`. See [Assign line items to Stripe products](/integrations/invoice-integrations/stripe#create-optional-entity-mapping-rules) in the Stripe invoicing guide for step-by-step instructions.

## Add a payment-gated commit to an existing contract​

Payment gated commits can only be added to existing contracts. You can create a payment-gated commit by [editing the user's contract](/api-reference/contracts/edit-a-contract). Make sure the contract has a valid billing configuration.

See below for an example API call:

```json theme={null}
{
    "customer_id": "8cecbf69-960f-4f66-9575-edebb7d95e88",
    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "add_commits": [
        {
            "product_id": "d6be3bf4-1669-40c9-a8b1-388bb167ab16",
            "type": "prepaid",
            "invoice_schedule": {
                "schedule_items": [
                    {
                        "timestamp": "2025-04-01T00:00:00.000Z",
                        "amount": 2000
                    }
                ]
            },
            "access_schedule": {
                "schedule_items": [
                    {
                        "amount": 2000,
                        "starting_at": "2025-04-01T00:00:00.000Z",
                        "ending_before": "2026-04-01T00:00:00.000Z"
                    }
                ]
            },
            "payment_gate_config": {
                "payment_gate_type": "STRIPE",
                "tax_type": "STRIPE"
            },
            "priority": 100
        }
    ]
}
```

## Manage notifications​

Two types of webhook notifications are emitted when creating a payment-gated commit:

* `payment_gate.payment_status` after payment has been attempted. The status of that payment, `paid` or `failed` , is denoted in the `payment_status` field.
* `payment_gate.payment_pending_action_required` if intervention is required to process payment.

See our full set of our webhook notifications [here](/guides/platform-configuration/setup-webhooks#payment-gating-notifications).

## Handle failed payments​

If payment fails, the associated invoice in Metronome and Stripe is voided and no commit is created. To retry the payment, send a new API request with the relevant commit information.

<Note>
  **NO AUTOMATIC RETRIES**

  Metronome does not automatically retry failed payments (as any automatic
  retries would likely fail, too).
</Note>
