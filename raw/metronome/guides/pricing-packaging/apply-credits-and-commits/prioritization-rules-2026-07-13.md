<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/prioritization-rules.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understand prioritization rules

To ensure consistent and predictable billing, Metronome follows a structured set of prioritization rules to determine burn down of commits and credits. The page explains the complete burn down sequence for different types of financial instruments, as well as how line items on invoices are prioritized.

## Prioritizing between commits and credits​

If a customer has multiple active credits or commits that can apply against the same usage, Metronome uses a series of rules to determine which credit or commit to consume first.

### Overall burn-down order

Before applying the rules within each type, Metronome burns down commits in this sequence:

1. **Rollover commits** (post-paid commits rollover before prepaid commits/credits)
2. **Prepaid commits and credits**
3. **Post-paid commits**

**Commit type always takes precedence over priority.** The `priority` field only controls ordering *within* the same commit type—it cannot cause a post-paid commit to burn down before a prepaid commit, or vice versa.

### Rollover commits and credits​

1. If there are multiple rollover commits or credits, burn down is based on **commit or credit type.** Post-paid rollover commits burn down before prepaid commits and credits.
2. If there are multiple rollover commits or credits with the same type, burn down is based on **priority.**
3. If there are multiple rollover commits or credits with the same type and priority, burn down is based on **product applicability.** Commits with the fewest applicable products first, most applicable products last.
4. If there are multiple rollover commits or credits with the same type, priority, and product applicability, burn down is based on **usage applicability** —the number of group value specifiers a commit has. Commits with the fewest applicable usage get consumed first, and the most applicable usage get consumed last.
5. If there are multiple rollover commits or credits with the same type, priority, and product and usage applicability, burn down is based on `ending_before`. The earlier `ending_before` gets burned down first.

<Info>
  **INFO**

  Group value specifiers are specifiers with only `presentation_group_value` or `pricing_group_value` defined. Commits with `applicable_product_ids` or `applicable_product_tags` have no usage applicability since they lack group value specifiers.
</Info>

### Prepaid commits and credits​

Prepaid commits and credits always burn down before post-paid commits, regardless of priority values.

1. If there are multiple prepaid commits and credits, burn down is based on **priority.**
2. If there are multiple other prepaid commits or credits with the same priority, burn down is based on **commit cost basis**. \$0 cost basis burns down first, then paid.
3. If there are multiple other prepaid commits or credits with the same priority and cost basis, burn down is based on **product applicability** . The fewest applicable products first, most applicable products last.
4. If there are multiple other prepaid commits or credits with the same commit type, priority, and product applicability, burn down is based on **usage applicability** —the number of group value specifiers a commit has. Commits with the fewest applicable usage get consumed first, and the most applicable usage get consumed last.
5. If there are multiple other prepaid commits or credits with the same priority, cost basis, and product and usage applicability, burn down is based on `ending_before`. The earlier `ending_before` burns down first.
6. If there are multiple prepaid commits or credits with the same priority, cost basis, product and usage applicability, and `ending_before`, burn down is based on `starting_on`. The earlier `starting_on` burns down first.
7. If there are multiple prepaid commits or credits with the same priority, cost basis, product and usage applicability, `ending_before`, and `starting_on`, burn down is based on the **number of contracts a commit applies to**. The commit with the least number of applicable contracts burns down first.

### Post-paid commits​

Post-paid commits always burn down after prepaid commits and credits, regardless of priority values. Within post-paid commits, burn down follows the same order logic as prepaid commits: priority, cost basis, product applicability, `ending_before`, `starting_on`, then number of applicable contracts.

This example API request creates the contract with prepaid commits.

The contract's prepaid commits burn down in this order:

1. Prepaid Commit A since it has the highest priority.
2. Prepaid Commit B since it has a zero-cost basis for commits with the same priority.
3. Prepaid Commit C since it has the lowest usage applicability for commits with the same priority, cost basis, and product applicability.
4. Prepaid Commit D since it has the earliest `ending_before` for commits with the same priority, cost basis, and product and usage applicability.
5. Prepaid Commit E since it has the next earliest `ending_before` for commits with the same priority, cost basis, and product and usage applicability.
6. Prepaid Commit F since it's applicable to all usage and products for commits with the same priority.

```bash theme={null}
curl https://api.staging.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
  "customer_id": "bc20325a-80a0-468e-868f-a2f28b972af8",
  "starting_at": "2024-10-01T00:00:00.000Z",
  "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
  "commits": [
    {
      "type": "prepaid",
      "priority": 50,
      "name": "Prepaid Commit A",
      "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2025-10-01T00:00:00.000Z"
          }
        ]
      },
      "invoice_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "unit_price": 1000000,
            "quantity": 1,
            "timestamp": "2024-10-01T00:00:00.000Z"
          }
        ]
      }
    },
    {
      "type": "prepaid",
      "priority": 100,
      "name": "Prepaid Commit B",
      "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2025-10-01T00:00:00.000Z"
          }
        ]
      }
    },
    {
      "type": "prepaid",
      "priority": 100,
      "name": "Prepaid Commit C",
      "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2025-10-01T00:00:00.000Z"
          }
        ]
      },
      "invoice_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "unit_price": 1000000,
            "quantity": 1,
            "timestamp": "2024-10-01T00:00:00.000Z"
          }
        ]
      },
      "applicable_product_ids": [
        "dbb46a31-3437-4df2-ade1-46a2641623ab"
      ]
    },
    {
      "type": "prepaid",
      "priority": 100,
      "name": "Prepaid Commit D",
      "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2025-10-01T00:00:00.000Z"
          }
        ]
      },
      "invoice_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "unit_price": 1000000,
            "quantity": 1,
            "timestamp": "2024-10-01T00:00:00.000Z"
          }
        ]
      },
      "specifiers": [
        {
          "product_id": "dbb46a31-3437-4df2-ade1-46a2641623ab",
          "pricing_group_values": {
            "region": "us-east-1"
          }
        },
        {
          "pricing_group_values": {
            "region": "us-west-1"
          }
        }
      ]
    },
    {
      "type": "prepaid",
      "priority": 100,
      "name": "Prepaid Commit E",
      "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2026-10-01T00:00:00.000Z"
          }
        ]
      },
      "invoice_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "unit_price": 1000000,
            "quantity": 1,
            "timestamp": "2024-10-01T00:00:00.000Z"
          }
        ]
      },
      "specifiers": [
        {
          "product_id": "dbb46a31-3437-4df2-ade1-46a2641623ab",
          "pricing_group_values": {
            "region": "us-east-1"
          }
        },
        {
          "pricing_group_values": {
            "region": "us-west-1"
          }
        }
      ]
    },
    {
      "type": "prepaid",
      "priority": 100,
      "name": "Prepaid Commit F",
      "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
      "access_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "amount": 1000000,
            "starting_at": "2024-10-01T00:00:00.000Z",
            "ending_before": "2025-10-01T00:00:00.000Z"
          }
        ]
      },
      "invoice_schedule": {
        "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        "schedule_items": [
          {
            "unit_price": 1000000,
            "quantity": 1,
            "timestamp": "2024-10-01T00:00:00.000Z"
          }
        ]
      }
    }
  ]
}'
```

## Line item prioritization​

If there are multiple line items on the invoice eligible for commit or credit application, Metronome uses rules to determine which line item to apply commit or credit to first:

1. Commits or credits are applied against usage products first, then subscription products, then composite products.
2. If there are multiple products of the same type, Metronome uses the start date of the line item, applied against earlier start dates first.
3. If there are multiple products of the same type with the same start date, Metronome uses the unit price of the line item, applied against line items with higher unit prices first.
4. If there are multiple products of the same type with the same type, start date and unit price, Metronome uses the line item name, applied alphabetically from A to Z.

For example, imagine a usage invoice with two usage products: Data Storage with a unit price of \$1, and Data Reads with a unit price of \$2.6 dollars. The line items have the same effective dates spanning the entire billing period. Any commit or credit first gets applied against Data Reads, as it has the higher unit price.
