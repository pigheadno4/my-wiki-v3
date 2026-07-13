<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/model-hierarchical-customer-relationships.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Model hierarchical customer relationships

For companies with direct sales motions selling to multiple organizational levels, account hierarchies enable you to model complex parent-child relationships in Metronome. This feature supports enterprise contracting scenarios where parent organizations may be responsible for subsidiary usage, commitments, and billing across different sub organizations.

## Overview

Account hierarchies allow you to:

* Model parent-child relationships between distinct Metronome customers (up to 10 nodes)
* Share commits and credits across hierarchical levels
* Configure flexible payment arrangements (parent pays, child pays, or mixed)
* Consolidate child usage onto a single invoice at the parent level
* Maintain distinct pricing and contracts for each entity

Consider a multinational corporation like Disney contracting with a cloud infrastructure provider for content delivery services. Disney and its subsidiaries (Hulu, ESPN, ABC) stream massive amounts of video content, paying for each gigabyte of data transferred through the provider's CDN. With account hierarchies, you can configure various billing models:

* Disney could pay for all CDN data transfer across subsidiaries while each maintains their own contracts and pricing
* Disney could purchase a \$10M shared commit for CDN data transfer that Hulu, ESPN, and other subsidiaries draw from before paying overages
* Each subsidiary could have their own pricing and commits, with Disney receiving a single consolidated invoice showing detailed usage breakdowns

## Prerequisites

Before implementing account hierarchies, ensure you have:

* Customer objects created for both parent and child organizations
* A billing configuration set up for each customer. Currently, Stripe billing is supported.
* Understanding of your organizational billing structure and payment flows

Note: Hierarchy relationships are configured during contract creation, not as a separate step.

### Example 1: Parent with shared commit pool

In this scenario, Disney purchases a \$10M commit that all subsidiaries can access for their usage.

Create the parent contract with shared commit:

```bash theme={null}
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "disney_parent_id",
    "name": "Disney Master Agreement",
    "rate_card_id": "enterprise_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "commits": [{
      "type": "prepaid",
      "product_id": "prepaid_commit_product_id",
      "access_schedule": {
        "schedule_items": [{
          "amount": 10000000,
          "starting_at": "2025-01-01T00:00:00Z",
          "ending_before": "2026-01-01T00:00:00Z"
        }]
      },
      "invoice_schedule": {
        "schedule_items": [{
          "amount": 10000000,
          "timestamp": "2025-01-01T00:00:00Z"
        }]
      },
      "hierarchy_configuration": {
        "child_access": {
          "type": "all"
        }
      }
    }]
  }'
```

Create child contracts that can access the shared commit:

```bash theme={null}
# Hulu contract - pays for own overages
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "hulu_customer_id",
    "name": "Hulu - Disney Subsidiary",
    "rate_card_id": "enterprise_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "hierarchy_configuration": {
      "parent": {
        "contract_id": "disney_contract_id",
        "customer_id": "disney_parent_id"
      },
      "payer": "SELF",
      "usage_statement_behavior": "SEPARATE"
    }
  }'

# ESPN contract - pays for own overages
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "espn_customer_id",
    "name": "ESPN - Disney Subsidiary",
    "rate_card_id": "enterprise_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "hierarchy_configuration": {
      "parent": {
        "contract_id": "disney_contract_id",
        "customer_id": "disney_parent_id"
      },
      "payer": "SELF",
      "usage_statement_behavior": "SEPARATE"
    }
  }'
```

In this setup:

* All children draw from Disney's \$10M commit
* Each child pays their own overages once the shared commit is exhausted
* Each child receives their own invoices

### Example 2: Parent pays with consolidated invoicing

In this scenario, each subsidiary has their own commits, but Disney receives and pays all invoices with usage consolidated into a single statement.

Create the parent contract with invoice consolidation enabled:

```bash theme={null}
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "disney_parent_id",
    "name": "Disney Master Agreement - Consolidated Billing",
    "rate_card_id": "enterprise_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "hierarchy_configuration": {
      "parent_behavior": {
        "invoice_consolidation_type": "CONCATENATE"
      }
    },
    "commits": [{
      "type": "prepaid",
      "product_id": "prepaid_commit_product_id",
      "access_schedule": {
        "schedule_items": [{
          "amount": 200000,
          "starting_at": "2025-01-01T00:00:00Z",
          "ending_before": "2026-01-01T00:00:00Z"
        }]
      },
      "invoice_schedule": {
        "schedule_items": [{
          "amount": 200000,
          "timestamp": "2025-01-01T00:00:00Z"
        }]
      },
      "hierarchy_configuration": {
        "child_access": {
          "type": "none"
        }
      }
    }]
  }'
```

Create child contracts with parent as payer:

```bash theme={null}
# Hulu with its own commit, parent pays
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "hulu_customer_id",
    "name": "Hulu - Disney Subsidiary",
    "rate_card_id": "enterprise_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "hierarchy_configuration": {
      "parent": {
        "contract_id": "disney_contract_id",
        "customer_id": "disney_parent_id"
      },
      "payer": "PARENT",
      "usage_statement_behavior": "CONSOLIDATE"
    },
    "commits": [{
      "type": "prepaid",
      "product_id": "prepaid_commit_product_id",
      "access_schedule": {
        "schedule_items": [{
          "amount": 500000,
          "starting_at": "2025-01-01T00:00:00Z",
          "ending_before": "2026-01-01T00:00:00Z"
        }]
      },
      "invoice_schedule": {
        "schedule_items": [{
          "amount": 500000,
          "timestamp": "2025-01-01T00:00:00Z"
        }]
      }
    }]
  }'
```

In this setup:

* Disney has its own \$200K commit that only it can access (child\_access: "none")
* Hulu has its own \$500K commit that only it can access
* Disney pays for all commits including Hulu's \$500K commit invoice
* Disney receives a single consolidated usage statement invoice containing Disney's own usage and Hulu’s usage with line items indicating the origin customer and contract
* All invoices are routed to Disney’s billing provider

Note: Even in a consolidation scenario, all children and the parent will still have their own standalone usage statements generated by Metronome which will be visible over Metronome’s UI, API and data export. These standalone usage statements will not, however, be sent to downstream billing providers when consolidation is set to occur. You may wish to filter out the standalone parent usage statement when showing spend detail to the parent in your UI so as to not double count parent spend across the standalone and consolidated invoices.

### Example 3: Selective commit access with distinct pricing

In this scenario, Disney has multiple commits with selective access, and each subsidiary has custom pricing.

Create parent contract:

```bash theme={null}
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "disney_parent_id",
    "name": "Disney Master Agreement - Selective Access",
    "rate_card_id": "enterprise_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z"
  }'
```

Create child contracts with pricing overrides:

```bash theme={null}
# Hulu with 20% discount on cdn data transfer
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "hulu_customer_id",
    "name": "Hulu - Disney Subsidiary",
    "rate_card_id": "streaming_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "hierarchy_configuration": {
      "parent": {
        "contract_id": "disney_contract_id",
        "customer_id": "disney_parent_id"
      },
      "payer": "SELF",
      "usage_statement_behavior": "SEPARATE"
    },
    "overrides": [{
      "product_id": "cdn_data_transfer_gb_id",
      "multiplier": 0.8
    }]
  }'

# ABC (no access to premium commit)
curl -X POST https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "abc_customer_id",
    "name": "ABC - Disney Subsidiary",
    "rate_card_id": "broadcast_rate_card_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "hierarchy_configuration": {
      "parent": {
        "contract_id": "disney_contract_id",
        "customer_id": "disney_parent_id"
      },
      "payer": "SELF",
      "usage_statement_behavior": "SEPARATE"
    }
  }'
```

Add shared commits with selective access to parent contract:

```bash theme={null}
curl -X POST https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "disney_parent_id",
    "contract_id": "disney_contract_id",
    "starting_at": "2025-01-01T00:00:00Z",
    "add_commits": [{
      "type": "prepaid",
      "name": "Premium Infrastructure Commit - Streaming Only",
      "product_id": "prepaid_commit_product_id",
      "applicable_product_ids": ["premium_cdn_transfer_gb"],
      "access_schedule": {
        "schedule_items": [{
          "amount": 5000000,
          "starting_at": "2025-01-01T00:00:00Z",
          "ending_before": "2026-01-01T00:00:00Z"
        }]
      },
      "invoice_schedule": {
        "schedule_items": [{
          "amount": 5000000,
          "timestamp": "2025-01-01T00:00:00Z"
        }]
      },
      "hierarchy_configuration": {
        "child_access": {
          "type": "contract_ids",
          "contract_ids": ["hulu_contract_id", "espn_contract_id"]
        }
      }
    }, {
      "type": "prepaid",
      "name": "Standard Infrastructure Commit - All Properties",
      "product_id": "prepaid_commit_product_id_2",
      "applicable_product_ids": ["standard_cdn_transfer_gb"],
      "access_schedule": {
        "schedule_items": [{
          "amount": 2000000,
          "starting_at": "2025-01-01T00:00:00Z",
          "ending_before": "2026-01-01T00:00:00Z"
        }]
      },
      "invoice_schedule": {
        "schedule_items": [{
          "amount": 2000000,
          "timestamp": "2025-01-01T00:00:00Z"
        }]
      },
      "hierarchy_configuration": {
        "child_access": {
          "type": "all"
        }
      }
    }]
  }'
```

In this setup:

* Different rate cards: Each subsidiary uses a rate card tailored to their business (streaming vs. broadcast) with appropriate products and pricing
* Selective commit access: Hulu and ESPN can access both premium and standard commits, while ABC only accesses the standard commit
* Contract-specific pricing: Hulu gets 20% off GB of CDN data transfer when drawing from the premium commit or paying overages
* Individual billing: Each subsidiary pays for their own overages and maintains separate billing configurations

## Viewing hierarchy relationships

### Get contract with hierarchy details

Retrieve complete hierarchy information for any contract:

```bash theme={null}
curl -X POST https://api.metronome.com/v2/contracts/get \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "disney_parent_id",
    "contract_id": "disney_contract_id"
  }'
```

Parent contracts show their children:

```
{
  "hierarchy_configuration": {
    "parent_behavior": {
      "invoice_consolidation_type": "CONCATENATE"
    },
    "children": [{
      "contract_id": "hulu_contract_id",
      "customer_id": "hulu_customer_id"
    }, {
      "contract_id": "espn_contract_id",
      "customer_id": "espn_customer_id"
    }]
  }
}
```

### View consolidated invoices

When configured for consolidation, parent invoices include all subsidiary usage:

```bash theme={null}
curl -X POST https://api.metronome.com/v1/invoices/get \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "disney_parent_id",
    "invoice_id": "consolidated_invoice_id"
  }'
```

Response includes origin details for each line item:

```
{
  "type": "USAGE_CONSOLIDATED",
  "constituent_invoices": [
    {"invoice_id": "parent_invoice", "customer_id": "disney_parent_id", "contract_id": "disney_contract_id"},
    {"invoice_id": "hulu_invoice", "customer_id": "hulu_customer_id", "contract_id": "hulu_contract_id"},
    {"invoice_id": "espn_invoice", "customer_id": "espn_customer_id", "contract_id": "espn_contract_id"}
  ],
  "line_items": [{
    "type": "usage",
    "amount": 15000,
    "product_id": "streaming_compute_id",
    "origin": {
      "invoice_id": "hulu_invoice",
      "line_item_id": "hulu_line_item_id",
      "contract_id": "hulu_contract_id",
      "customer_id": "hulu_customer_id"
    }
  }]
}
```

### Break down consolidated invoices

Analyze usage distribution across the hierarchy using invoice breakdowns. This is particularly useful for understanding spend patterns across subsidiaries.

```bash theme={null}
curl -X POST https://api.metronome.com/v1/invoices/breakdown \
  -H "Authorization: Bearer $METRONOME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "disney_parent_id",
    "invoice_id": "consolidated_invoice_id",
    "breakdown_start_timestamp": "2025-01-01T00:00:00Z",
    "breakdown_end_timestamp": "2025-01-02T00:00:00Z"
  }'
```

The breakdown response for consolidated invoices includes origin information for each line item:

```
{
  "breakdown_start_timestamp": "2025-01-01T00:00:00Z",
  "breakdown_end_timestamp": "2025-01-02T00:00:00Z",
  "id": "consolidated_invoice_id",
  "customer_id": "disney_parent_id",
  "type": "USAGE_CONSOLIDATED",
  "line_items": [
    {
      "amount": 15000,
      "product_id": "cdn_data_transfer_gb_id",
      "quantity": 1500,
      "unit_price": 10,
      "timestamp": "2025-01-01T08:00:00Z",
      "origin": {
        "invoice_id": "hulu_usage_invoice_123",
        "contract_id": "hulu_contract_id",
        "customer_id": "hulu_customer_id"
      }
    },
    {
      "amount": 8000,
      "product_id": "cdn_data_transfer_gb_id",
      "quantity": 800,
      "unit_price": 10,
      "timestamp": "2025-01-01T14:00:00Z",
      "origin": {
        "invoice_id": "espn_usage_invoice_456",
        "contract_id": "espn_contract_id",
        "customer_id": "espn_customer_id"
      }
    },
    {
      "amount": 5000,
      "product_id": "cdn_data_transfer_gb_id",
      "quantity": 500,
      "unit_price": 10,
      "timestamp": "2025-01-01T20:00:00Z",
      "origin": {
        "invoice_id": "disney_usage_invoice_789",
        "contract_id": "disney_contract_id",
        "customer_id": "disney_parent_id"
      }
    }
  ]
}
```

Use the origin information to:

* Analyze spend by subsidiary: Group line items by `origin.customer_id` to see each entity's usage
* Track contract performance: Use `origin.contract_id` to measure usage against specific contracts

## Best practices

**Design your hierarchy thoughtfully**

* Map organizational relationships before implementation
* Consider payment flows and invoice routing requirements

**Set clear commit access rules**

* Use `type: "all"` for organization-wide shared resources
* Use `type: "contract_ids"` for department or tier-specific access

**Monitor usage patterns**

* Review consolidated invoices to understand usage distribution
* Use invoice breakdowns to analyze spending by subsidiary

**Coordinate contract timing**

* Align contract start dates when possible
* Plan renewal strategies across the hierarchy
* Consider commit rollover implications for renewals

## Troubleshooting

**Child cannot access parent commit**

* Verify the parent commit's `child_access` configuration includes the child
* Ensure the child contract correctly references the parent contract ID
* Confirm both contracts are active during the same time period

**Child invoices not appearing on consolidated invoice:**

* Verify parent contract has `invoice_consolidation_type: "CONCATENATE"`
* Check child contract has `usage_statement_behavior: "CONSOLIDATE"`
* Ensure child's usage service period is bounded by parent's service period
  * Example: If parent invoice covers Jan 1-31 and child invoice covers Jan 5-31, child usage will consolidate. But if child invoice covers Dec 28 - Jan 28, child usage will not consolidate
* Confirm the issue dates align (same day) between parent and child invoices

**Cannot set consolidation with self-payment:**

* `usage_statement_behavior: "CONSOLIDATE"` requires `payer: "PARENT"`
* Child contracts paying themselves must use `usage_statement_behavior: "SEPARATE"`

## Current limitations

1. **Hierarchy depth**: Only one level supported (parent-child); no grandchildren or multi-level hierarchies
2. **Hierarchy size**: Maximum active 10 nodes supported in a hierarchy
3. **Billing providers**: Only Stripe is supported; marketplace billing coming soon
4. **Contract structure**: Each Metronome customer requires their own contract - no single contract can automatically apply to all children
5. **Usage rating**: Each child's usage is rated separately based on their contract. Parent tiered pricing only applies to direct parent usage, not aggregated child usage
6. **Alert scope**:
   * Commit balance alerts on parent contracts don't automatically trigger when children consume the commit
   * Alerts evaluate when the parent receives usage data
   * If only children receive usage, parent alerts may be delayed until parent usage arrives
   * Additionally, parent spend alerts only include parent's
7. **Embeddable dashboards**: Invoice and commit dashboards don't work with customers that have a contract in a hierarchy
