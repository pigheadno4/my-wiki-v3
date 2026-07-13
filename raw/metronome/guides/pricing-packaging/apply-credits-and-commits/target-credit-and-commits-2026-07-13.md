<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Target usage with credits and commits

You can grant credits and create commitments that are only applicable to a subset of a customer’s usage. Choose to target the usage of specific products, product families, pricing dimensions, and even dimensions not used for pricing. This gives you the flexibility to negotiate enterprise commitments based on any dimension and to try out different pricing incentives.

Metronome provides two options to target credits and commits:

* Target with `applicable_product_ids` and `applicable_product_tags` if you want to filter only on product ID or product family, and don’t require complex AND/OR logic
* Target with `specifiers` if you want to filter based on pricing group values or presentation group values, or require complex AND/OR logic

## Target with `applicable_product_ids` and `applicable_product_tags`​

For simple use cases that don't require complex AND/OR logic, use the `applicable_product_ids` and `applicable_product_tags` fields to target your credit or commit.

Usage that matches *any* of the listed product IDs and product tags is eligible to consume the credit or commit.

## Target with `specifiers`​

Specifiers provide the flexibility to power more complex use cases involving pricing group values, presentation group values, or advanced boolean logic.

The `specifiers` field takes in an array of objects, where each object is called a specifier. Within each specifier all fields are ANDed together. If the conditions of any specifier in the array are met, the line item is eligible to consume the commit or credit. This is logic identical to [override\_specifiers](/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract#target-overrides), which you can use to grant discounts based on complex logic.

Note that if you use pricing group values and/or presentation group values in a specifier, only usage of products with the corresponding pricing and presentation group values will match that specifier. For example, if you create a credit that applies when pricing group value `region` = `us-east-1`, products that do not have the pricing group key `region` will never draw down the credit. Subscriptions and composite products never have pricing or presentation group values, so would not draw down the commit.

### Example: Commit applies to only two `regions` (pricing group value)​

Consider a scenario where you’ve negotiated an enterprise commitment with a large customer. They only plan to use your product in two specific `regions`, and you’ve negotiated that the commitment only covers usage in those `regions`. `region` is a pricing group key for your products. Your products are available in many regions, and you use [dimensional pricing](/guides/get-started/core-concepts/create-manage-rate-cards#how-dimensional-pricing-works%E2%80%8B) to price a single product differently by region.

This example API call creates a contract that specifies the `pricing_group_values` for the `us-east-1` and `us-east-2` regions.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "47e8f505-3c08-4c9d-8323-14d36c21658e",
    "contract_id": "cf4b3e2d-d697-4c4b-869b-5db2dbb224f5",
    "starting_at": "2025-06-01T00:00:00.000Z",
    "commits": [
        {
            "type": "PREPAID",
            "name": "Commit - us-east-1 and us-west-1 only",
            "product_id": "ffa5d53f-0b84-4d8d-bdb4-d21e7e104aa5",
            "access_schedule": {
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "schedule_items": [
                    {
                        "amount": 50000,
                        "starting_at": "2025-06-01T00:00:00.000Z",
                        "ending_before": "2026-06-01T00:00:00.000Z"
                    }
                ]
            },
            "invoice_schedule": {
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "schedule_items": [
                    {
                        "amount": 50000,
                        "timestamp": "2025-06-01T00:00:00.000Z"
                    }
                ]
            },
            "specifiers": [
                {
                    "pricing_group_values": {
                        "region":"us-east-1"
                    }
                },
                {
                    "pricing_group_values": {
                        "region":"us-west-1"
                    }
                }
            ]
        }
    ]
}'
```

### Example: Credit applies to only one `user_id` (presentation group value)​

Consider a scenario where you want to grant a credit that's only usable for a specific `user_id` within an organization. You don’t price differently based on `user_id`, but you want to grant this specific user a credit in return for taking part in user research. `user_id` is a presentation group key across your products.

This example API call edits a contract to add credits by specifying the `presentation_group_values` for a specific `user_id`:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "47e8f505-3c08-4c9d-8323-14d36c21658e",
    "contract_id": "cf4b3e2d-d697-4c4b-869b-5db2dbb224f5",
    "add_credits": [
        {
            "type": "PREPAID",
            "name": "Credit - user_123 only only",
            "product_id": "ffa5d53f-0b84-4d8d-bdb4-d21e7e104aa5",
            "access_schedule": {
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "schedule_items": [
                    {
                        "amount": 500,
                        "starting_at": "2025-06-01T00:00:00.000Z",
                        "ending_before": "2026-06-01T00:00:00.000Z"
                    }
                ]
            },
            "specifiers": [
                {
                    "presentation_group_values": {
                        "user_id": "user_123"
                    }
                }
            ]
        }
    ]
}'
```

### Example: Commit applies to products with both product tags​

Product tags make it very straightforward to launch new products. Consider a scenario where, as part of negotiating an enterprise contract, you’ve agreed that a postpaid commitment applies to all products in the *Audio* model family that are also *Basic* models (a non-premium offering). By using product tags, any new products you launch that are *Basic* , *Audio* models automatically draw down from the postpaid commitment, with no additional work required. *Basic* and *Audio* models are both product tags.

This example API call edits a contract to add a commit, specifying the `product_tags` `Audio` and `Basic`:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "47e8f505-3c08-4c9d-8323-14d36c21658e",
    "contract_id": "cf4b3e2d-d697-4c4b-869b-5db2dbb224f5",
    "starting_at": "2025-06-01T00:00:00.000Z",
        "add_commits": [
        {
            "type": "PREPAID",
            "name": "Commit - basic audio models",
            "product_id": "ffa5d53f-0b84-4d8d-bdb4-d21e7e104aa5",
            "access_schedule": {
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "schedule_items": [
                    {
                        "amount": 50000,
                        "starting_at": "2025-06-01T00:00:00.000Z",
                        "ending_before": "2026-06-01T00:00:00.000Z"
                    }
                ]
            },
            "invoice_schedule": {
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "schedule_items": [
                    {
                        "amount": 50000,
                        "timestamp": "2025-06-01T00:00:00.000Z"
                    }
                ]
            },
            "specifiers": [
                {
                    "product_tags": [
                        "Audio",
                        "Basic"
                    ]
                }
            ]
        }
    ]
}'
```
