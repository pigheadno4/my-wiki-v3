<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/enterprise-commit.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Launch an enterprise commit model

This guide describes how to launch an enterprise commit model using Metronome, including:

* Best practices for provisioning enterprise contracts for customers
* How to execute against an SLG motion from initial provisioning through contract upsell, contract renewal, and financial reporting

As companies begin to sell upmarket to enterprise customers, business models tend to get more complex. These customers have different expectations than individual consumers due to their comparatively high volume of usage. As a result, enterprise customers tend to negotiate longer term contracts in return for discounts and premium products. Often times, these contracts are based on a commitment by the enterprise to spend a certain amount.

The Metronome data model provides first-class support for enterprise deal requirements like prepaid and postpaid commitments, negotiated discounts, one-time charges, contract renewals, and more.

## Use case​

This guide walks through an example using an infrastructure SaaS company, InfraX. InfraX sells storage and analysis products and is developing a sales-led growth (SLG) commit-based model.

Your sales team at InfraX just closed its first enterprise deal with these terms:

* The customer commits to spending \$500,000 over a three-year contract.
  * Usage is expected to ramp up as adoption at the customer organization increases, so they commit to a three-year schedule (allotment of usage):
    * Year 1: \$50,000
    * Year 2: \$200,000
    * Year 3: \$250,000
  * They agree to pay for this commit across two installations:
    * Year 1: \$250,000
    * Year 3: \$250,000
* In exchange for this prepaid commitment, the customer receives a 10% discount on all `storage` products in year 1 and a 20% discount thereafter.
* If the customer completes an on-time renewal, they can roll over up to 25% of the original balance from their prepaid commitment. This was an important clause for the customer who was unsure whether they were agreeing to too large of a commitment.
* The customer has purchased \$5,000 in professional support to help triage technical issues, which is paid in month 3 of the contract.

Model these terms in Metronome after you design the Metronome building blocks for the enterprise.

## Metronome building blocks​

Even in enterprise sales, where customization is the norm, the basics of your business model remain the same. This is why Metronome [products](/guides/get-started/core-concepts/create-products-contracts) and [rate cards](/guides/get-started/core-concepts/create-manage-rate-cards) are common across all customers. Streamline the provisioning of contracts by setting up products and rate cards with enterprise commit models in mind.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/billing-model-guides/enterprise-commit/enterprise-commit-model-76b33a992199498966431da1792deb93.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=201bef976ae48519b8487a05296aaa44" alt="Enterprise commit model" width="3478" height="1350" data-path="images/docs/pricing-packaging/billing-model-guides/enterprise-commit/enterprise-commit-model-76b33a992199498966431da1792deb93.png" />
</Frame>

Follow these best practices to design your products and rate cards for enterprise.

### Use product tags to simplify discounts​

In an enterprise commit model, your customer typically agrees to commit to a certain amount of spend and, in return, you offer them discounted rates.

Metronome [contracts](/guides/customers-billing/manage-customers/provision-a-customer) support rate overrides, which modify the default rate from a rate card to account for something like a discount. These overrides can target individual products or all products with one or more tags. These tags represent some grouping of products priced, discounted, or packaged similarly.

You can change a product's tag at any time with the API or the [Metronome app](https://app.metronome.com/), but if you know in advance that you tend to discount certain products together, you'll save time by organizing products with tags up front. By doing this, you remove the need to store the `product.id` of each product that might be discounted as part of an enterprise deal. For a typical infrastructure SaaS company, this could mean storing a few tags as opposed to dozens of products.

For this guide’s example, your company InfraX wants to give a discount on all products labeled with the `storage` tag.

### Make products for every kind of charge​

In Metronome, every charge on an invoice is associated with a [product](/guides/get-started/core-concepts/create-products-contracts). This includes one-time charges and upfront payments for prepaid commitments. Create these products with the `fixed` product type. Thinking through the different types of charges your sales team may offer leads to a smooth contract provisioning process.

### Design products with finance workflows in mind​

Downstream processes like tax calculation, data reconciliation for audits, or revenue recognition often need to know something about the charge. The Metronome product stores this information in a reusable way.

For example, store the SKU ID from the relevant ERP system on the Product entity or the account ID from your CRM system on the customer entity as [custom fields](/developer-resources/custom-fields/). This can serve as a foreign key mapping between line items on the Metronome invoice and revenue buckets in the ERP system or other third-party entities.

## Implement the enterprise commit model​

Now that you’ve set things up following enterprise best practices, explore the end-to-end customer lifecycle from contract creation to contract upsell, renewal, and financial reporting.

### Provision customers with commitments​

In our example, InfraX’s sales team uses Salesforce CPQ to track the state of a given opportunity. Once the opportunity is closed in SFDC, encode the terms of the deal in Metronome.

To encode deal terms in Metronome:

1. Create the customer in Metronome (if they don't already exist).
2. Provision the customer with a contract.

### Create the customer​

In Metronome, model the SFDC account as a Metronome customer and make the following POST request to `/customers` :

```bash theme={null}
curl https://api.metronome.com/v1/customers \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "ingest_aliases": [  
      "internal_customer_id"  
    ],  
    "name": "Customer X",  
    "customer_config": {  
      "salesforce_account_id": "sfdc_account_01"  
    }  
  }'
```

This API call returns the created Metronome `customer.id`. Store this value, as you’ll need it to provision the customer with a contract.

<Tip>
  **TIP**

  The customer object can now serve as a join table between Metronome, SFDC, and your internal product. This can be useful for workflows like data reconciliation and revenue recognition.
</Tip>

### Provision a contract​

Now that the customer exists in Metronome, set the terms of their signed contract with an API call to `/contracts/create`. This example stores the relationship between the opportunity in SFDC and the contract in Metronome by setting the custom field on the contract object for `sfdc_opportunity_id`:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "c247f641-aa10-4167-bdbf-e1266810c4e4",  
    "rate_card_alias": "my-rate-card",  
    "starting_at": "2024-01-01T00:00:00Z",  
    "ending_before": "2027-01-01T00:00:00Z",  
    "commits": [  
      {  
        "type": "prepaid",  
        "product": "76e57c3a-064f-49ad-8740-2bff58f2f808",  
        "access_schedule": {  
          "schedule_items": [  
            {  
              "amount": 5000000,  
              "starting_at": "2024-01-01T00:00:00Z",  
              "ending_before": "2025-01-01T00:00:00Z"  
            },  
            {  
              "amount": 20000000,  
              "starting_at": "2025-01-01T00:00:00Z",  
              "ending_before": "2026-01-01T00:00:00Z"  
            },  
            {  
              "amount": 25000000,  
              "starting_at": "2026-01-01T00:00:00Z",  
              "ending_before": "2027-01-01T00:00:00Z"  
            }  
          ]  
        },  
        "invoice_schedule": {  
          "schedule_items": [  
            {  
              "amount": 25000000,  
              "timestamp": "2024-01-01T00:00:00Z"  
            },  
            {  
              "amount": 25000000,  
              "timestamp": "2026-01-01T00:00:00Z"  
            }  
          ]  
        },  
        "rollover_fraction": 0.25  
      }  
    ],  
    "overrides": [  
      {  
        "starting_at": "2024-01-01T00:00:00Z",  
        "type": "multiplier",  
        "multiplier": 0.9,  
        "applicable_product_tags": ["storage"]  
      },  
      {  
        "starting_at": "2025-01-01T00:00:00Z",  
        "type": "multiplier",  
        "multiplier": 0.8,  
        "applicable_product_tags": ["storage"]  
      }  
    ],  
    "scheduled_charges": [  
      {  
        "product_id": "0afe45f6-f048-44a5-8fc5-9e9b9592d029",  
        "schedule": {  
          "schedule_items": [
            {
              "amount": 500000,
              "timestamp": "2024-03-01T00:00:00Z"
            }
          ]  
        }  
      }  
    ],  
    "custom_fields": {  
      "sfdc_opportunity_id": "opp_id_01"  
    }  
  }'
```

This API call returns the `contract.id`. Save this ID in your internal database to manage the customer lifecycle in Metronome.

## Optimize your customer’s experience​

The customer journey doesn't end when they sign the contract - consider their experience as they onboard to your product. The customer may adopt your products too slowly, or burn through their prepaid commitment faster than expected. With Metronome, you can provide the end customer with this transparency so they can take action based on their desired usage behaviors.

### Create a cost explorer for your customer​

In this guide’s example, the customer negotiated a discount for storage products. Due to this, they will want to assess what proportion of their usage comes from these features in comparison to others. If they discover it’s a low percentage, they may want to change their discount structure during the next contract negotiation.

[Build a cost explorer](/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting) within your product that highlights spend breakdown over time, with the ability to segment or filter on relevant properties like `product.name`.

### Provide spend control​

Beyond transparency, the customer wants additional capabilities to control their consumption. Metronome’s [spend controls](/enhance-customer-experience/customer-controls/) provide the ability to proactively cap spend based on a variety of considerations.

For the example customer’s contract, they only have \$50,000 of spend in year 1 compared to \$200,000 in year 2. If adoption occurs quicker than expected, they may want to get notified when they hit a certain threshold, like \$5,000 of spend remaining. This enables them to take action, potentially by negotiating for the year 2 allotment to be accelerated, before going into overage.

## Manage mid-contract changes and renewals​

At some point, your customer may need new contract terms, potentially to change the discounting on their contract or to alter the schedule and amount on their commit.

### Prepare your sales team​

To prepare for this negotiation, Metronome empowers your sales team with granular insights into the customer’s usage with its native [Salesforce connector](/integrations/platform-integrations/sfdc-integration). Metronome can sync important data to the system your sales team operates in, like the balance remaining on a commit, spend by product, usage over time, and more. With access to this data, your sales team can effectively engage the customer with a clear understanding of the value they get from the product.

### Execute an upsell​

Metronome contract edits and transitions help you handle changes to existing contracts. Edit a contract to add terms without starting a new contract. Use a contract transition to start a new contract with a customer. With contract transitions, Metronome keeps track of the relationship with the original contract and applies transition logic like rolling over unused commitments or credits during a renewal.

For example, after several conversations with your customer, your InfraX sales team effectively negotiates an upsell on the existing contract on Jan 01, 2025:

* In addition to the existing commit, the customer agrees to buy a new \$300,000 commit.
* In return for this commit, the customer negotiates a new discount of 15% on `analysis` products.

Execute this edit with an API call:

```bash theme={null}
curl https://api.metronome.com/v2/contracts/edit \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
    "add_scheduled_charges": [  
      {  
        "product_id": "76e57c3a-064f-49ad-8740-2bff58f2f808",  
        "schedule": {  
          "schedule_items": [  
            {  
              "timestamp": "2025-01-01T00:00:00Z",  
              "amount": 30000000  
            }  
          ]  
        }  
      }  
    ],  
    "add_overrides": [  
      {  
        "starting_at": "2025-01-01T00:00:00Z",  
        "type": "multiplier",  
        "multiplier": 0.85,  
        "applicable_product_tags": ["analysis"]  
      }  
    ]  
  }'
```

## Power financial workflows​

Ensure your finance teams are set up for success. As you set up contract and customer objects, you established relationships between entities in different systems. This is critical for workflows like reconciliation, which are an audit performed by finance to ensure the accuracy of information in revenue systems. To learn more about powering finance workflows in Metronome, see:

* **[Data reconciliation](/guides/reporting-insights/financial-reporting/reconcile-data)** : By leveraging stored foreign key relationships, determine if all of the necessary data made it from the upstream CRM tool to Metronome to the downstream accounting system. This is a critical process for minimizing revenue leakage when closing the books at the end of the month and demonstrating an audit trail between systems for third-party auditors.
* **[Revenue recognition](/guides/reporting-insights/financial-reporting/revenue-recognition)** : Given the appropriate SKU IDs are on the Metronome invoice through product custom fields, effectively map line items to the appropriate revenue buckets in your ERP system.
