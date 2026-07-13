<!-- Source URL: https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/preview-event-cost.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preview event costs

> Preview the cost of customer actions before they’re incurred.

Help customers understand the financial impact of their actions before they commit to taking them. The preview events endpoint allows you to simulate how events would affect a customer's invoice without actually processing or billing for them.

## Why preview costs?

Cost transparency builds trust and empowers customers to make informed decisions. Common scenarios include:

* **Resource-intensive operation cost previews**: Show users how much a compute job or data processing task will cost before confirming execution
* **Budget planning**: Help customers forecast costs for planned usage patterns with interactive cost calculators
* **What-if analysis**: Let customers explore different usage scenarios to optimize their spending

## How cost preview works

The preview events endpoint evaluates events against a customer's actual contract configuration, including all pricing complexity:

* **Tiered pricing**: Correctly applies volume discounts and tier transitions
* **Commits and credits**: Shows what usage is covered by commit and credit balances and what spills into overage
* **Free allotments**: Accounts for included usage in the contract
* **Multiple products**: Calculates costs across all products in the contract

## Preview modes

There are two different ways you can choose to evaluate preview events:

### Merge mode

Combines preview events with the customer's existing usage for the billing period. Use this to show incremental cost impact.

**Example**: A customer has used 99 API calls this month (with 100 free). Previewing 5 calls in merge mode shows 1 free and 4 billable.

### Replace mode

Evaluates only the preview events, ignoring existing usage. Use this for hypothetical "clean slate" scenarios.

**Example**: Show the total monthly cost if a customer only performed the specific actions in the preview.

## Set up a cost preview

### Basic example

Preview how 100 compute hours would affect a customer's invoice:

```bash theme={null}
curl --request POST \
  --url https://api.metronome.com/v1/customers/{customer_id}/previewEvents \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "events": [
      {
        "event_type": "compute_usage",
        "timestamp": "2025-11-15T10:00:00Z",
        "properties": {
          "compute_hours": "100",
          "instance_type": "gpu-large"
        }
      }
    ],
    "mode": "merge"
  }'
```

### Response structure

The endpoint returns draft invoices showing the calculated costs:

```json theme={null}
{
  "data": [
    {
      "id": "68e0bc1c-a8ec-5765-856b-f896285b4cdb",
      "issued_at": "2025-12-02T12:00:00+00:00",
      "start_timestamp": "2025-11-01T00:00:00+00:00",
      "end_timestamp": "2025-12-01T00:00:00+00:00",
      "customer_id": "46b2c479-6202-4db6-b392-5a156a9dd5c8",
      "customer_custom_fields": {
        "bill_customer_id": "0du01JDIRIUDQKDS6wm2"
      },
      "type": "USAGE",
      "credit_type": {
        "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "name": "USD (cents)"
      },
      "status": "DRAFT",
      "total": 49000,
      "external_invoice": null,
      "contract_id": "688d9619-bd2c-42db-8dcb-288f02f741df",
      "contract_custom_fields": {},
      "line_items": [
        {
          "product_id": "c2ab408b-d212-4dca-a99b-f2b450abad45",
          "product_type": "UsageProductListItem",
          "product_custom_fields": {
            "org_id": "prod_NbZryAoW6ugALt"
          },
          "product_tags": [
            "compute"
          ],
          "name": "GPU Compute Hours",
          "type": "usage",
          "total": 0,
          "credit_type": {
            "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            "name": "USD (cents)"
          },
          "starting_at": "2025-11-01T00:00:00+00:00",
          "ending_before": "2025-12-01T00:00:00+00:00",
          "netsuite_item_id": "f2b4-50ab-ad45",
          "unit_price": 4900,
          "quantity": 10
        }
      ],
      "custom_fields": {},
      "billable_status": "billable"
    }
  ]
}
```

For customers with multiple active contracts, the endpoint returns separate invoices for each:

```json theme={null}
{
  "data": [
    {
      "contract_id": "contract-1-id",
      "total": 50000,
      // ... invoice details for contract 1
    },
    {
      "contract_id": "contract-2-id",
      "total": 25000,
      // ... invoice details for contract 2
    }
  ]
}
```

### Event deduplication

The preview endpoint follows the same deduplication logic as the ingest endpoint:

* Events with identical `transaction_id` values passed in the same request payload are deduplicated against each other
* Events with identical `transaction_id` values to those passed to `/ingest` in the prior 34 days are deduplicated as well

## Best practices & limitations

### Performance considerations

The endpoint has an 8 RPS rate limit per client and is not suitable for real-time validation of every event. Consider these strategies:

* **Cache preview results**: When showing repeated calculations for similar usage patterns, cache the results
* **Batch multiple events**: Preview multiple events in a single request rather than making separate calls

### Accuracy tips

* Include all relevant event properties that affect pricing
* Test both `merge` and `replace` modes during development

### Limitations

* Customers using SQL-based billable metrics cannot use this endpoint. If SQL BMs are present on the customer invoice being evaluated when passing in events to preview, the endpoint will return a 400 error.
