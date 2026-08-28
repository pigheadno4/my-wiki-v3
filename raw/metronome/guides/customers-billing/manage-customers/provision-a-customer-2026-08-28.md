<!-- Source URL: https://docs.metronome.com/guides/customers-billing/manage-customers/provision-a-customer.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Provision a customer

> In Metronome, customers are the recipients of an invoice and may represent individual users, enterprises, API keys, or whatever specification your organization needs. This guide describes how to provision a customer in Metronome.

Provisioning your customer includes creating the customer object and configuring the associated contract that outlines their terms of use. A customer needs at least one contract provisioned to them to start metering and rating for billing. You can also configure multiple contracts per customer, if needed.

## Prerequisites

Before provisioning a customer you must have:

* Your [usage events](/guides/events/design-usage-events) connected to Metronome
* A [billable metric](/guides/get-started/core-concepts/create-billable-metrics/)
* A [product](/guides/get-started/core-concepts/create-products-contracts)
* A [rate card](/guides/get-started/core-concepts/create-manage-rate-cards)

## Create a customer

Create an individual customer object in Metronome or build a flow to create customers programmatically from system triggers.

### Understand ingest aliases

Ingest aliases map your internal customer identifiers to Metronome's customer ID. When you send usage keyed on an ingest alias, Metronome automatically associates it to the correct Metronome customer. This allows you to maintain your existing customer entities without needing to swap in a Metronome customer ID.

Ingest aliases can also be used to maintain account hierarchy. Enterprise customers often have sub-organizations that roll up to a single contract. Use ingest aliases to model this. For example, you can represent the enterprise organization as a customer in Metronome, with each sub-organization represented by an ingest alias attached to that customer:

```
Parent Account - Metronome Customer e7f893e5-07f7-483b-8c16-6905944c6a89
  + Sub-Org 1 - IngestAlias1
  + Sub-Org 2 - IngestAlias2
  + Sub-Org 3 - IngestAlias3
  + Sub-Org 4 - IngestAlias4
```

You can split out each sub-organization's usage on the invoice Metronome generates. Learn how to use [group keys](/guides/get-started/core-concepts/create-billable-metrics#3-define-group-keys%E2%80%8B) to modify invoice presentation.

Ingest aliases can be specified on the Metronome customer object at time of creation or any point after. Retroactively adding an ingest alias on the customer is a way to take Metronome out of the hot path of customer signup while properly metering usage. For example, if you first send usage keyed on `IngestAlias1` and later add this ingest alias to an existing customer, Metronome retroactively associates that usage to the correct customer.

### Create a customer with the Metronome app

To create a customer using the app:

1. Go to the **Customers** page → **Add a customer**.
2. Add a name.
3. Add an ingest alias.
4. (Optional) Set a custom field for the customer on the **Settings** tab.

### Build a customer creation flow with the API

Use the Metronome API to build a flow for creating customers in Metronome programmatically based on sales-led or product-led motions.

For a sales-led motion, you might use Salesforce CPQ to capture opportunities. When an opportunity closes, you can schedule a job to create a customer using the Metronome API.

This example request shows how to:

* Create a mock customer, WidgetsExpress, in Metronome
* Codify the relationship between the Metronome customer and the SFDC account by storing the `sfdc_account_id` in a custom field

```bash theme={null}
curl https://api.metronome.com/v1/customers \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "ingest_aliases": [
      "team@widgetsexpress.com"
    ],
    "name": "WidgetsExpress",
    "custom_fields": {
      "sfdc_account_id": "sfdc1001"
    }
  }'
```

For a product-led growth motion, create a similar workflow where the trigger originates from a signup on your website. Store the relationship between the Metronome customer and your internal customer object.

### Add a billing configuration to a customer

A customer in Metronome can billed in different destinations, often depending on your billing motion. You must first create a `customer_billing_provider_configuration` on the customer and then assign it to a contract. Metronome allows you to configure multiple `customer_billing_provider_configurations` per customer, which means one customer can be billed in multiple systems - one per contract.

<Note>
  **INFO**

  Before setting up a `customer_billing_provider_configuration`, Metronome must first be connected to the relevant system. Follow the steps in [Invoice with Stripe](/integrations/invoice-integrations/stripe) or [Invoice with the Marketplaces (AWS and Azure)](/integrations/marketplace-integrations/aws).
</Note>

Metronome recommends setting the `customer_billing_provider_configurations` on customer creation. For example, let's say WidgetsExpress purchased your product via AWS Marketplace. Amend the previous call to add a `customer_billing_provider_configurations` to the WidgetExpress customer:

```bash theme={null}
curl https://api.metronome.com/v1/customers \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "ingest_aliases": [
      "team@widgetsexpress.com"
    ],
    "name": "WidgetsExpress",
    "custom_fields": {
      "sfdc_account_id": "sfdc1001"
    },
    "customer_billing_provider_configurations": [
      {
        "billing_provider": "aws_marketplace",
        "configuration": {
          "aws_customer_id": "ABC123ABC12",
          "aws_product_code": "my_product",
          "aws_region": "us-west-1"
        },
        "delivery_method": "direct_to_billing_provider"
      }
    ]
  }'
```

After submission, the customer will be created with the associated AWS configuration. However, it will not be billed to AWS until a contract is created with AWS set as the contract's `billing_provider_configuration`. If you do not set a `customer_billing_provider_configuration` on customer creation, you can add one later using the `/setCustomerBillingProviderConfigurations` endpoint.

<Note>
  **BETA**

  You can archive a `customer_billing_provider_configuration` by either archiving the customer or archiving the specific configuration via the `/archiveCustomerBillingProviderConfigurations` endpoint. When you archive a billing configuration, it becomes available for reuse on a new customer. If you archive a `customer_billing_provider_configuration` that is attached to an active contract, the config will be archived on the contract immediately and no longer bill to the associated destination. A new `billing_provider_configuration` cannot be provisioned on the contract.
</Note>

## Provision a customer contract

Define a contract in Metronome that encodes the products customers can access, rates for each product, and access duration. Just as rate cards are built on products, contracts are built on rate cards. A contract references a specific rate card and bundles it with other Metronome models like [commits,](/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit) discounts, fixed products that don't live on the rate card, and more.

Create contracts with the Metronome app or with the [/contracts/create endpoint](/api-reference/contracts/create-a-contract).

### Create a contract

Consider an example where your customer, WidgetsExpress, purchased a prepaid commit for \$10,000 that applies to your cloud products via AWS Marketplace. This commit lasts for a year. As part of the contract, they also pay a \$1,000 platform fee each quarter to use your service. They pay for the prepaid commit once upfront and for usage on a monthly basis.

To provision this contract with the [Metronome app](https://app.metronome.com/):

1. Navigate to *Customers* and select your newly created customer.
2. On the *Overview* tab, click the **+ Add** button on the right hand side of the *Contracts* pane.
3. Fill in the *Basic* info for the contract like the contract name, start date, and rate card to use. Be sure to set the billing provider to AWS.
4. Under *Terms*, click **Add -> Commit** and fill in the details for the prepaid commit.
5. Under *Terms*, click **Add -> Scheduled charges** and add the platform fee as a scheduled charge.

The final contract looks like:

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/manage-customers/provision-contract-fe412f3eebd53427e5c051a091504620.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=f65fd32892d905d20bf0223a1c8b6350" alt="Final contract" width="2178" height="1220" data-path="images/manage-customers/provision-contract-fe412f3eebd53427e5c051a091504620.png" />
</Frame>

To create the example contract with the `/contracts/create` API, execute this call:

```bash theme={null}
    curl https://api.metronome.com/v1/contracts/create \
      -H "Authorization: Bearer <TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "customer_id": "aa58107d-162f-407e-9f09-940f16adbb1c",
        "rate_card_alias": "base_usage_products",
        "starting_at": "2024-11-01T00:00:00.000Z",
        "billing_provider_configuration": {
          "billing_provider": "aws_marketplace",
          "delivery_method": "direct_to_billing_provider"
        },
        "commits": [
          {
            "type": "prepaid",
            "name": "Contract Prepaid Commit",
            "product_id": "a1f4e40b-f8c4-496b-b687-0a103396b479",
            "access_schedule": {
              "schedule_items": [
                {
                  "amount": 1000000,
                  "starting_at": "2024-11-01T00:00:00.000Z",
                  "ending_before": "2025-11-01T00:00:00.000Z"
                }
              ]
            },
            "invoice_schedule": {
              "schedule_items": [
                {
                  "unit_price": 1000000,
                  "quantity": 1,
                  "timestamp": "2024-11-01T00:00:00.000Z"
                }
              ]
            },
            "applicable_product_tags": ["cloud"],
            "description": "Usage Commit"
          }
        ],
        "scheduled_charges": [
          {
            "product_id": "06cf3703-3f5e-467c-8ba1-0ee934c740b9",
            "name": "Platform Charge",
            "schedule": {
              "recurring_schedule": {
                "starting_at": "2024-11-01T00:00:00.000Z",
                "ending_before": "2025-11-01T00:00:00.000Z",
                "frequency": "quarterly",
                "unit_price": 100000,
                "quantity": 1,
                "amount_distribution": "each"
              }
            }
          }
        ],
        "usage_statement_schedule": {
          "frequency": "monthly",
          "day": "contract_start"
        }
      }'
```

## Consolidate usage and scheduled invoices

You have the option to specify if scheduled invoices should consolidate onto a customer's usage invoices.

This setting applies to all charges (including commits) on the contract. It follows this logic to determine whether to consolidate invoices:

* The last day of the usage service period (exclusive) falls on the same day as the scheduled date for the scheduled invoice.
* The corresponding usage invoice hasn't finalized.

Consolidation occurs at the time of contract creation and upon any contract changes in the future.

Consider an example where a new customer buys the Best package on your website, which costs \$75 per month. As part of this package, they receive a \$100 monthly commit. The contract and recurring commit start on January 1 with no end date. If `scheduled_charges_on_usage_invoices` is set to `ALL`, the contract creates these invoices:

* **Invoice 1:** Issued and finalized on January 1 with one line item for the \$75 monthly charge.
* **Invoice 2:** Created in draft with one line item for the \$75 monthly charge in February in addition to all usage charges for January.
* **Invoice X:** Assuming no changes to the contract, all future invoices will model invoice 2.

## Add contract discounts and overrides

Provide discounts during contract creation or by editing an existing contract.

Apply discounts with credits, [overrides for product rates](/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract), price tiers, and more. If you use dimensional pricing, set price overrides for each combination of group key and product. To add additional terms like credits, commits, overrides for product rates, and more, edit the contract.

Consider the example with your mock customer WidgetsExpress to see this in practice. The customer negotiated a discount on cloud products. To address this, edit the contract by overriding products with the `cloud` tag to be 5% off of the basic rate card.

To edit a contract with the Metronome app, go to the WidgetsExpress customer → Contracts -> and select the contract that you would like to edit.

To edit a contract through the API, execute this call:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "aa58107d-162f-407e-9f09-940f16adbb1c",
    "contract_id": "0a6180da-336a-40e6-98f4-20b6be08211d",
    "add_overrides": [
      {
        "starting_at": "2024-11-01T00:00:00.000Z",
        "entitled": true,
        "type": "multiplier",
        "multiplier": 0.95,
        "applicable_product_tags": ["cloud"]
      }
    ]
  }'
```

## Create a usage filter

You can provision a customer with multiple contracts simultaneously. These contracts can use distinct rate cards, have different start and end dates, discounts, and more. They can all draw down from shared customer-level commits and credits. To specify that usage should count against one contract instead of another, create a usage filter for that contract.

For example, your mock customer WidgetsExpress has three sub-divisions: US, EU, and APAC. Each division negotiated different discounts. To model this in Metronome, create a contract for each sub-division and use usage filters to ensure only the appropriate usage gets routed to each contract.

When creating the US contract, ensure that only events with the property  `region` and value ` US` are included in this contract using this API call:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "starting_at": "2024-10-01T00:00:00.000Z",
    "usage_filter": {
      "group_key": "region",
      "group_values": [
        "US"
      ]
    }
  }'
```

You can update the usage filter on a contract at any time, on a schedule. For example, imagine that as of 2025, WidgetsExpress no longer wants usage within their EU division invoiced separately. Instead, they should get billed through the US contract, using US prices.

This API call shows how to update the usage filter, with the edit taking effect on Jan 01, 2025:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/setUsageFilter \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "group_key": "region",
    "group_values": ["US", "EU"],
    "starting_at": "2025-01-01T00:00:00.000Z"
  }'
```

Usage filters have these limitations:

* For [streaming billable metrics](/guides/get-started/core-concepts/create-billable-metrics/), you must define the usage filter as a group key on the underlying billable metric. If you're also using dimensional pricing and presentation group keys, the usage filter group key must be defined in a compound group key on the underlying billable metric with the dimensional pricing and presentation group keys.
* For [SQL billable metrics](/guides/get-started/core-concepts/create-billable-metrics#define-group-keys-on-sql-billable-metrics%E2%80%8B/), the group key for the usage filter must be present as property value in the underlying events (for example, `properties.region`).
* `LATEST` billable metrics are not currently compatible with contract-level usage filters. Applying a contract-level usage filter to a contract that rates a product backed by a `LATEST` billable metric can cause invoice computation errors. Use `LATEST` only on contracts without usage filters.

## Add custom fields

Use [custom fields](/developer-resources/custom-fields/) to add additional metadata to the contract or commit. This metadata can power downstream processes like revenue recognition workflows.

For example, if you're integrating with SFDC, you can create a custom field for `salesforce_opportunity_id` to map Metronome contracts, and revenue derived from it, to the associated SFDC opportunity.
