<!-- Source URL: https://docs.metronome.com/integrations/invoice-integrations/custom-invoice-integrations.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoice with other systems

This guide explores how to set up invoicing in systems not covered by Metronome’s native integrations.

To support these workflows, you can collaborate with Metronome to create [data exports](/guides/reporting-insights/data-export/overview) or build a managed integration that connects to your billing system of choice. Managed integrations get built using the data export feature or Metronome APIs.

## Integration approach

Often, out-of-the-box integrations to invoicing platforms don’t meet the core requirements of clients and require significant customization. This is because they focus on syncing data without considering the end-to-end use case and business model. In contrast, managed integrations with Metronome take a first-principles approach to meeting client invoicing requirements.

As Metronome invests deeper into different business models, we continuously assess whether to build new native integrations to more billing platforms like our [Invoicing with Stripe](/integrations/invoice-integrations/stripe), [Invoicing with NetSuite](/integrations/invoice-integrations/netsuite), and [Invoicing with marketplaces](/integrations/marketplace-integrations/aws) solutions.

For more information on how to set up a managed integration, contact your Metronome representative.

## External billing provider setup

This setup describes how you could send invoice data to external downstream billing providers using the Metronome API. While this example is specific to QuickBooks, the pattern and design decisions apply across other use cases.

Before setting up in Metronome, check if your billing platform requires additional setup, such as organizational requirements or permissions to create invoices. For example, QuickBooks requires a Developer app to sync invoices:

1. **Create an Intuit Developer app.** Go to [developer.intuit.com](https://developer.intuit.com), create an app, and select the **Accounting** scope.
2. **Record your Client ID and Client Secret** from the app's Keys & Credentials page.
3. **Set a Redirect URI** for your OAuth callback endpoint.
4. **Complete the OAuth 2.0 flow** to obtain an access token and refresh token.
5. **Note your Realm ID** (Company ID) — this identifies which QBO company you're writing to.

Once this setup is complete, proceed with the next steps.

### Configure required objects

To support this use case, start by building out your customer and item objects inside of your selected billing system and store them in custom fields in Metronome. Learn more about how to use [custom fields](/api-reference/custom-fields).

Recommended custom fields in Metronome:

| Metronome entity | Custom field key  | Value                                                          |
| ---------------- | ----------------- | -------------------------------------------------------------- |
| Product          | `qbo_item_id`     | The QBO Item ID for this Metronome product                     |
| Customer         | `qbo_customer_id` | The QBO Customer ID for this Metronome customer                |
| Contract         | `qbo_memo_ref`    | Optional — reference to help link contracts to invoices in QBO |

### Customer mapping

For each Metronome customer, either find or create a corresponding QBO Customer. The recommended approach is to store the QBO Customer ID as a custom field on the Metronome customer object (e.g., `qbo_customer_id`).

If no match is found, create the customer in QBO and store the resulting QBO Customer ID back in Metronome as a custom field.

### Item mapping

You have two strategies for mapping Metronome line items to QBO Items:

| Strategy         | How it works                                                                                                 | Trade-offs                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Per-product item | Create a QBO item for each Metronome product (e.g., "Warehouse Compute", "API Calls"). Map via `product_id`. | QBO reports break down revenue by product. Requires item governance and naming conventions. |
| Single Item      | Create one generic QBO item (e.g. “Metronome Usage”). All line items reference this one item.                | Less detail in QBO reports (all revenue appears under one category). Simple and fast setup. |

### Integrate through the API

Follow this recommended approach to push invoices to your downstream billing provider by building an integration on top of Metronome APIs:

1. Set up a [webhook endpoint](/guides/platform-configuration/setup-webhooks) and listen for the `invoice.finalized` event. This event gets created once an invoice is finalized in Metronome after the grace period ends.

```json theme={null}
{
  "id": "f4988a54-effe-49a2-9a07-8adfedb7541c",
  "type": "invoice.finalized",
  "properties": {
    "invoice_id": "d23458e0-c9a0-5538-8e81-251835b9f57a",
    "customer_id": "e0ac4251-74f7-4040-a1bd-9d0ef0fbc5bc",
    "invoice_finalized_date": "2024-10-09T17:52:27.371Z"
  }
}
```

<Note>
  **NOTE**

  The `invoice.finalized` event is not enabled by default for Metronome clients. To turn this event on, contact your Metronome representative.
</Note>

2. This webhook provides `customer_id` and `invoice_id`. Use `customer_id` to query the `/listInvoices` endpoint for `finalized` invoices from the associated billing period.

```bash theme={null}
curl -X GET https://api.metronome.com/v1/customers/e0ac4251-74f7-4040-a1bd-9d0ef0fbc5bc/invoices \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d "status=FINALIZED" \
  -d "starting_on=2024-10-09T00:00:00.000Z" \
  -d "ending_before=2024-10-10T00:00:00.000Z"
```

The response includes the full invoice objects with header-level fields (`id`, `status`, `total`, `subtotal`, `issued_at`, `start_timestamp`, `end_timestamp`, `contract_id`) and the `line_items` array with per-line details (`name`, `type`, `quantity`, `unit_price`, `total`, `product_id`, etc.).

3. Parse and transform the response into the appropriate format and upsert the invoice and line items.

   <Note>
     **NOTE**

     For QuickBooks, you need a customer and at least one item to exist.
   </Note>

### Transform and map fields

This is the core of the integration — converting Metronome's invoice schema into expected formats for invoices. Below is an example mapping to QuickBooks fields.

#### Invoice header mapping

| Metronome field | QBO field         | Notes                                                                                     |
| --------------- | ----------------- | ----------------------------------------------------------------------------------------- |
| customer\_id    | CustomerRef.value | Use your stored QBO Customer ID mapping                                                   |
| issued\_at      | TxnDate           | Date portion only. Fall back to end\_timestamp if null                                    |
| invoice.id      | DocNumber         | QBO has a strict length limit. Use "MTR-" + first 8 chars of UUID                         |
| end\_timestamp  | DueDate           | Or set a payment term (e.g. Net30) from the TxnDate                                       |
| (multiple)      | PrivateNote       | Store fields such as: full Invoice ID, status, billing period, contract ID, contract name |
| (multiple)      | CustomerMemo      | Human-readable summary of the billing period and plan                                     |

#### Line item mapping

| Metronome field  | QBO field                     | Notes                                                                    |
| ---------------- | ----------------------------- | ------------------------------------------------------------------------ |
| line.name        | SalesItemLineDetail.ItemRef   | Map to your QBO Item (single or per-product)                             |
| line.quantity    | SalesItemLineDetail.Qty       | Pass through directly                                                    |
| line.unit\_price | SalesItemLineDetail.UnitPrice | Pass through directly                                                    |
| line.total       | Line.Amount                   | Check if amounts are in cents or dollars and convert accordingly         |
| (composite)      | Line.Description              | Include: line name, type, time window, pricing group values, product\_id |

### Create the invoice

With all dependencies resolved and fields mapped, assemble and POST the invoice. In QuickBooks, the format looks like:

```http theme={null}
POST /v3/company/{realmId}/invoice?minorversion=75
Authorization: Bearer {access_token}
Content-Type: application/json
{
  "CustomerRef": { "value": "{qbo_customer_id}" },
  "TxnDate": "2026-03-01",
  "DocNumber": "MTR-EF9E4917",
  "PrivateNote": "Metronome invoice ef9e4917-... ",
  "Line": [
    {
      "Amount": 7599.42,
      "DetailType": "SalesItemLineDetail",
      "Description": "Warehouse Compute (usage)...",
      "SalesItemLineDetail": {
        "ItemRef": { "value": "{qbo_item_id}" },
        "Qty": 140.73,
        "UnitPrice": 54.00
      }
    }
  ]
}
```

### Orchestration

To build the necessary orchestration layer, you can choose to leverage existing developer environments or a third-party tool.

If you’re investigating third-party tools, Metronome recommends using the IPaaS system Workato. Workato is an automation tool that enables organizations to transform and transmit data using point-and-click workflow building capabilities. Metronome published a [connector](/integrations/platform-integrations/workato-connector) in the Workato Public library, which acts as a wrapper to the Metronome API similar to an SDK. Leveraging these public connectors can accelerate the speed of development and provide additional clarity on how to interact with the distinct endpoints.

For more information on integrating with the API or leveraging public connectors, contact your Metronome representative.
