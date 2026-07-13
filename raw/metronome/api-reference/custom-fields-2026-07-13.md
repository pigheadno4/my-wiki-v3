<!-- Source URL: https://docs.metronome.com/api-reference/custom-fields.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom fields

Custom fields are properties that you can add to Metronome objects to store metadata like foreign keys or other descriptors. This metadata can get transferred to or accessed by other systems to contextualize Metronome data and power business processes. For example, to service workflows like [revenue recognition](/guides/reporting-insights/financial-reporting/revenue-recognition-examples), [reconciliation](/guides/reporting-insights/financial-reporting/reconcile-data), and [invoicing in Stripe](/integrations/invoice-integrations/stripe), custom fields help Metronome know the relationship between entities in the platform and third-party systems.

## How custom fields work​

You can add custom fields to most Metronome entities: customer, product, contract, commit, credit, scheduled charge, rate card, and alert. These fields are persisted across the platform and can be fetched in the UI, API, and data export wherever the object appears.

When deciding when to create custom fields and where to put them, it’s important to think through the relationship of entities between a given external system and Metronome. For example, to model a NetSuite ERP integration in Metronome, you want to identify what the counterpart is for each object that you want to sync. Frequently, clients sync Metronome invoices to NetSuite and attach the invoices to the related NetSuite customer ID. To store the relationship between them, create a custom field called `netsuite_customer_id` on the Metronome customer object. This field enables a user to query the customer object and determine the foreign key mapping between the two systems.

The next example walks through how to associate a line item to a product ID (or SKU) in Stripe by adding a custom field called `stripe_product_id` to the Metronome product.

## Create a custom field​

You can create a custom field using the [Metronome app](https://app.metronome.com/) or API.

To create a custom field on a product in the Metronome app:

1. Click **Connections**.
2. Within Connections, click the **Custom fields** tab.
3. Within custom fields, click **Add new field key**.
4. In the resulting modal, select **Product (Contracts)** for entity, enter **stripe\_product\_id** for the **Key** , and turn on the **Unique values required**.
5. Click **Save**.

<Warning>
  **CAUTION**

  Enforcing unique values limits the ability to set the same value across multiple objects.

  Use this to map foreign entities that have a one-to-one relationship with a Metronome object. Uniqueness is enforced even when an object is archived. To resolve a duplicate issue with an archived object, reset the value of the field.
</Warning>

To create a custom field with the API, make a POST request to `/customFields/addKey`. The endpoint takes three parameters, all required:

* `entity`
* `key`
* `enforce_uniqueness`

```bash theme={null}
    curl https://api.metronome.com/v1/customFields/addKey \  
      -H "Authorization: Bearer <TOKEN>" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "entity": "contract_product",  
        "key": "stripe_product_id",  
        "enforce_uniqueness": true  
      }'
```

## Set a custom field value​

Once you've defined a custom field on an entity, set values for that field on individual entity instances using the [Metronome app](https://app.metronome.com/) or API.

To set a custom field value in the Metronome app:

1. Go to the the **Contract Pricing** page and find the product on the **Product List**.
2. Click on the product record to open the drawer containing the product metadata.
3. Click the overflow button in the top right corner of the drawer and click **Manage custom fields**.
4. Within customer settings, click **Custom fields** —> **Manage**.
5. Within the custom fields page, click **Set custom field**.
6. In the resulting modal, select the field name and provide the field value.
7. Click **Save**.

To set a custom field value with the API, make a POST request to `/customFields/setValues`. The endpoint takes three parameters, all required:

* `entity`
* `entity_id`
* `custom_fields`

The `custom_fields` parameter accepts an array of key-value pairs, allowing you to set multiple custom field values—on a single entity instance—in one API call.

This request updates a specific product, adding the corresponding `stripe_product_id` value:

```bash theme={null}
    curl https://api.metronome.com/v1/customFields/setValues \  
      -H "Authorization: Bearer <TOKEN>" \  
      -H "Content-Type: application/json" \  
      -d '{  
        "entity": "contract_product",  
        "entity_id": "76e57c3a-064f-49ad-8740-2bff58f2f808",  
        "custom_fields": {  
          "stripe_product_id": "prod_KyVnHhSBWl7eY2bl"  
        }  
      }'
```

Alternatively, you can set a custom field value on the creation of an object. For example, to set a custom field value on the contract object, you could do this within the POST request to the `/createContract` endpoint.

## Fetch a custom field value​

Once you set a custom field value on an object instance (like a product), the value gets returned when you request that object, including in the Metronome app, API calls, and data exports.

As an example, consider the invoice response. Given that products in Metronome map to line items on invoices, the `stripe_product_id` custom field propagates to its associated line item. This mapping enables Metronome to link line items to Stripe products when creating invoices in Stripe. Here’s an example invoice payload:

```json theme={null}
    {  
      "data": {  
        "id": "09abf41e-2e68-622f-93bc-ce8ef21215de",  
        "issued_at": "2024-09-02T00:00:00+00:00",  
        "start_timestamp": "2024-08-01T00:00:00+00:00",  
        "end_timestamp": "2024-09-01T00:00:00+00:00",  
        "customer_id": "195826717-122e-5150-a96e-ab7ef9744e9c",  
        "customer_custom_fields": {},  
        "type": "USAGE",  
        "credit_type": {  
          "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
          "name": "USD (cents)"  
        },  
        "status": "DRAFT",  
        "total": 22000,  
        "external_invoice": null,  
        "contract_id": "ccffadcf-5e3b-407d-8c5e-3f678508bfd1",  
        "contract_custom_fields": {},  
        "line_items": [  
          {  
            "product_id": "d3d10cd4-e234-4265-91c1-a95f09e6a69c",  
            "product_type": "UsageProductListItem",  
            "product_custom_fields": {  
              "stripe_product_id": "prod_KyVnHhSBWl7eY2bl"  
            },  
            "name": "Usage Product",  
            "total": 22000,  
            "credit_type": {  
                "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
                "name": "USD (cents)"  
            },  
            "starting_at": "2024-08-01T00:00:00+00:00",  
            "ending_before": "2024-09-01T00:00:00+00:00",  
            "unit_price": 110,  
            "quantity": 200  
          },  
          ...  
        ]  
      }  
     }
```
