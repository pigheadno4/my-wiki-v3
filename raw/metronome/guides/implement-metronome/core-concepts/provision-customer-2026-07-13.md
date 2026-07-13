<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/provision-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Provision a customer

In Metronome, customers are the recipients of an invoice and may represent individual users, enterprises, API keys, or whatever specification your organization needs. This guide describes how to create a customer in Metronome.

Creating your customer includes creating the customer object and configuring the optional associated billing configurations.

<Info>
  **INFO**

  A customer needs at least one [contract](/guides/get-started/core-concepts/provision-contract) provisioned to start rating for billing. You can also configure multiple contracts per customer, if needed.
</Info>

## Create a customer​

Create an individual customer object in Metronome or build a flow to create customers programmatically from system triggers.

### Understand ingest aliases​

Ingest aliases map your internal customer identifiers to Metronome’s customer ID. When you send usage keyed on an ingest alias, Metronome automatically associates it to the correct Metronome customer. This allows you to maintain your existing customer entities without needing to swap in a Metronome customer ID.

Ingest aliases can also be used to maintain account hierarchy. Enterprise customers often have sub-organizations that roll up to a single contract. Use ingest aliases to model this. For example, you can represent the enterprise organization as a customer in Metronome, with each sub-organization represented by an ingest alias attached to that customer:

```js theme={null}
Parent Account - Metronome Customer e7f893e5-07f7-483b-8c16-6905944c6a89  
  + Sub-Org 1 - IngestAlias1  
  + Sub-Org 2 - IngestAlias2  
  + Sub-Org 3 - IngestAlias3  
  + Sub-Org 4 - IngestAlias4
```

You can split out each sub-organization’s usage on the invoice Metronome generates. Learn how to use [group keys](/guides/get-started/core-concepts/create-billable-metrics#3-define-group-keys%E2%80%8B) to modify invoice presentation.

Ingest aliases can be specified on the Metronome customer object at time of creation or any point after. Retroactively adding an ingest alias on the customer is a way to take Metronome out of the hot path of customer signup while properly metering usage. For example, if you first send usage keyed on `IngestAlias1` and later add this ingest alias to an existing customer, Metronome retroactively associates that usage to the correct customer.

### Create a customer with the Metronome app​

To create a customer using the app:

1. Go to the **Customers** page → **Add a customer.**
2. Add a name.
3. Add an ingest alias.
4. (Optional) Set a custom field for the customer on the **Settings** tab.

### Build a customer creation flow with the API​

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

A customer in Metronome can be billed in different destinations, often depending on your billing motion. You must first create a `customer_billing_provider_configuration` on the customer and then assign it to a contract. Metronome allows you to configure multiple `customer_billing_provider_configurations` per customer, which means one customer can be billed in multiple systems - one per contract.

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
