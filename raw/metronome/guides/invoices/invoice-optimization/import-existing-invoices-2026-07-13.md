<!-- Source URL: https://docs.metronome.com/guides/invoices/invoice-optimization/import-existing-invoices.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Import existing invoices

Metronome offers a unified source of truth for your customers' billing history, even if you initially provisioned them outside of Metronome. You can easily import existing contracts and invoices into Metronome.

This guide describes how to import an example contract and its corresponding invoices with the Metronome API. You can also use the Metronome SDK to import existing invoices.

## Use case

The fictional company used in this guide, called Acme Inc, is a new Metronome client. In this example, today's date is August 15, 2024. Acme Inc has a contract outside of Metronome with a monthly billing schedule that started on June 1, 2024. Invoices for June and July were already issued outside of Metronome.

## Create the contract

First, create the contract using the `/contracts/create` endpoint, entering the original contract details (for example, starting commit/credit balances and start date). Set the `usage_statement_schedule.invoice_generation_starting_at` field to indicate when Metronome should begin generating invoices. In our example, that date is August 1, 2024, since the customer hasn't been billed for August yet.

```http theme={null}
POST /v1/contracts/create HTTP/1.1  
Host: api.metronome.com  
Authorization: Bearer <TOKEN>  
Content-Type: application/json  

{  
  "customer_id": "<the Metronome customer ID>",  
  "rate_card_id": "<the Metronome rate card ID>",  
  "starting_at": "2024-06-01T00:00:00.000Z",  
  "usage_statement_schedule": {  
    "frequency": "monthly",  
    "invoice_generation_starting_at": "2024-08-01T00:00:00.000Z"  
  }  
}
```

With the contract created, Metronome generates a draft invoice for August. No invoices are created for June and July.

## Import the invoices

After creating the contract, import the corresponding invoices with the `/contracts/createHistoricalInvoices` endpoint. All you'll need is the quantities for each line item on the invoice. Metronome combines these with the unit prices specified on the contract to calculate the total amount on the invoice and the effects on the customer's credit and commit balances.

```http theme={null}
POST /v1/contracts/createHistoricalInvoices HTTP/1.1  
Host: api.metronome.com  
Authorization: Bearer <TOKEN>  
Content-Type: application/json  

{  
  "invoices": [  
    {  
      "customer_id": "<the Metronome customer ID>",  
      "contract_id": "<the Metronome contract ID>",  
      "credit_type_id": "<the Metronome credit type ID>",  
      "inclusive_start_date": "2024-06-01T00:00:00.000Z",  
      "exclusive_end_date": "2024-07-01T00:00:00.000Z",  
      "issue_date": "2024-07-03T00:00:00.000Z",  
      "usage_line_items": [  
        {  
          "product_id": "<the Metronome product ID>",  
          "inclusive_start_date": "2024-06-01T00:00:00.000Z",  
          "exclusive_end_date": "2024-07-01T00:00:00.000Z",  
          "quantity": 10  
        }  
      ]  
    },  
    {  
      "customer_id": "<the Metronome customer ID>",  
      "contract_id": "<the Metronome contract ID>",  
      "credit_type_id": "<the Metronome credit type ID>",  
      "inclusive_start_date": "2024-07-01T00:00:00.000Z",  
      "exclusive_end_date": "2024-08-01T00:00:00.000Z",  
      "issue_date": "2024-08-03T00:00:00.000Z",  
      "usage_line_items": [  
        {  
          "product_id": "<the Metronome product ID>",  
          "inclusive_start_date": "2024-07-01T00:00:00.000Z",  
          "exclusive_end_date": "2024-08-01T00:00:00.000Z",  
          "quantity": 20  
        }  
      ]  
    }  
  ],  
  "preview": true  
}
```

<Tip>
  **TIP**

  Use the `preview` option to perform a dry run of the import to verify any differences between the existing and imported invoices before saving them.
</Tip>

Access imported invoices on the **Contracts** page in the Metronome app or with the API.

## (Optional) Import hourly or daily breakdowns

To use Metronome to retrieve hourly or daily breakdowns of customer usage and costs, specify time-windowed quantities by populating the `subtotals_with_quantity` field of the line item in lieu of the `quantity` field. Specify the `breakdown_granularity` of the invoice. When generating the invoice for the entire billing period, Metronome sums up the subtotals of each window.

```http theme={null}
POST /v1/contracts/createHistoricalInvoices HTTP/1.1  
Host: api.metronome.com  
Authorization: Bearer <TOKEN>  
Content-Type: application/json  

{  
  "invoices": [  
    {  
      "customer_id": "<the Metronome customer ID>",  
      "contract_id": "<the Metronome contract ID>",  
      "credit_type_id": "<the Metronome credit type ID>",  
      "inclusive_start_date": "2024-06-01T00:00:00.000Z",  
      "exclusive_end_date": "2024-07-01T00:00:00.000Z",  
      "issue_date": "2024-07-03T00:00:00.000Z",  
      "breakdown_granularity": "day",  
      "usage_line_items": [  
        {  
          "product_id": "<the Metronome product ID>",  
          "inclusive_start_date": "2024-06-01T00:00:00.000Z",  
          "exclusive_end_date": "2024-07-01T00:00:00Z",  
          "subtotals_with_quantity": [  
            {  
              "inclusive_start_date": "2024-06-01T00:00:00.000Z",  
              "exclusive_end_date": "2024-06-02T00:00:00.000Z",  
              "quantity": 1  
            }  
          ]  
        }  
      ]  
    }  
  ],  
  "preview": true  
}
```

<Note>
  **INFO**

  Metronome doesn't send imported invoices to the Stripe integration. This prevents sending duplicate invoices to customers.
</Note>
