<!-- Source URL: https://docs.metronome.com/guides/customers-billing/manage-customers/schedule-billing-provider-change.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Schedule a billing provider change

> Switch billing providers on an existing contract without creating a new one.

Metronome supports switching between any combination of Stripe, NetSuite, and marketplace providers (AWS, Azure, GCP) on a contract. A contract stores a **billing provider configuration schedule** — an ordered list of segments each with an `effective_at` timestamp aligned to a billing period boundary. The active configuration for a given invoice is the segment with the latest `effective_at` date before the service period end date or `issued~at` date if there is no service period end date.

## Supported transitions

| From → To                                | Current period | Next period |
| :--------------------------------------- | :------------: | :---------: |
| Stripe → Stripe                          |        ✅       |      ✅      |
| Stripe → NetSuite                        |        ✅       |      ✅      |
| NetSuite → Stripe                        |        ✅       |      ✅      |
| Stripe → Marketplace (AWS / Azure / GCP) |        ❌       |      ✅      |
| Marketplace → Stripe                     |        ❌       |      ✅      |
| Marketplace → Marketplace                |        ❌       |      ✅      |
| NetSuite → Marketplace                   |        ❌       |      ✅      |
| Marketplace → NetSuite                   |        ❌       |      ✅      |

## Schedule a change

Use the `add_billing_provider_configuration_update` field on `POST v2/contracts/edit`. The `effective_at` controls when the new configuration takes effect: `START_OF_CURRENT_PERIOD` or `START_OF_NEXT_PERIOD`.

**Example: Correct a Stripe misconfiguration, effective immediately**

Switch from one Stripe configuration to another at the start of the current period. The current draft invoice will be routed to the new configuration. If an invoice was already finalized and sent to Stripe during this period, the new configuration will not apply to it — all invoices are guaranteed to be sent exactly once.

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "8cecbf69-960f-4f66-9575-edebb7d95e88",
    "contract_id": "6058587f-763c-400f-a822-3edb3eb2b86b",
    "add_billing_provider_configuration_update": {
      "billing_provider_configuration": {
        "billing_provider_configuration_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      },
      "schedule": {
        "effective_at": "START_OF_CURRENT_PERIOD"
      }
    }
  }'
```

**Example: Transition from Stripe to AWS Marketplace, effective next period**

All invoices from the current billing period are routed based on the existing Stripe configuration. The marketplace configuration takes effect at the start of the next period.

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "8cecbf69-960f-4f66-9575-edebb7d95e88",
    "contract_id": "6058587f-763c-400f-a822-3edb3eb2b86b",
    "add_billing_provider_configuration_update": {
      "billing_provider_configuration": {
        "billing_provider_configuration_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901"
      },
      "schedule": {
        "effective_at": "START_OF_NEXT_PERIOD"
    }
  }'
```

## View the billing provider configuration schedule

Fetch a contract using `POST v2/contracts/get` to view the full schedule. The `customer_billing_provider_configuration` field returns the currently-active configuration unchanged. The `billing_provider_configuration_schedule` field returns an ordered list of all past, current, and future segments.

```json theme={null}
{
  "data": {
    "id": "6058587f-763c-400f-a822-3edb3eb2b86b",
    "customer_id": "8cecbf69-960f-4f66-9575-edebb7d95e88",
    "customer_billing_provider_configuration": {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "billing_provider": "stripe",
      "delivery_method": "direct_to_billing_provider"
    },
    "billing_provider_configuration_schedule": [
      {
        "billing_provider_configuration": {
          "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "billing_provider": "stripe",
          "delivery_method": "direct_to_billing_provider"
        },
        "effective_at": "2025-01-01T00:00:00.000Z",
        "effective_until": "2025-06-01T00:00:00.000Z"
      },
      {
        "billing_provider_configuration": {
          "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
          "billing_provider": "aws_marketplace",
          "delivery_method": "direct_to_billing_provider"
        },
        "effective_at": "2025-06-01T00:00:00.000Z",
        "effective_until": null
      }
    ]
  }
}
```

## Constraints and considerations

<Note>
  **Changes align to billing period boundaries.** `START_OF_CURRENT_PERIOD` resolves to the start of the current usage invoice service period. `START_OF_NEXT_PERIOD` resolves to the start of the following service period. Each invoice maps to exactly one billing provider configuration based on its service period start date.
</Note>

<Note>
  **Marketplace transitions require `START_OF_NEXT_PERIOD`.** Marketplace billing is metered from the start of a period, so mid-period transitions are not supported. When transitioning to a marketplace, the current period completes fully on the existing configuration. When transitioning away, the marketplace continues to bill through the end of the current period.
</Note>

<Note>
  **Threshold billing must be disabled before switching to a marketplace provider.** If a contract has an active threshold billing configuration, it must be removed before scheduling a transition to any marketplace provider.
</Note>

<Note>
  **`customer_billing_provider_configuration` is unchanged and backward compatible.** The existing field on `contracts/get` and `contracts/list` responses continues to return the currently-active configuration. No changes are required to existing integrations that read this field.
</Note>

<Note>
  **A maximum of 10 schedule segments per contract.** If you need additional capacity on a specific contract, contact your account team.
</Note>

<Note>
  **To cancel a scheduled future change**, schedule a new segment covering the same period. The latest segment takes precedence.
</Note>
