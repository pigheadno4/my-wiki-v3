<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/how-invoicing-works.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How Metronome invoices work

Invoices in Metronome represent the products or services sold to or consumed by your customers. This page describes invoice types, statuses, line items, and configurable presentation.

<Note>
  **CUSTOMER BILLING**

  To learn how to bill your customers and collect payment for Metronome invoices, view our [invoicing guides](/guides/invoices/overview)
</Note>

In the context of usage-based billing, where customers are charged based on actual consumption of a service (like cloud storage, API calls, or data processing), the invoice plays a crucial role for several reasons:

* **Transparency** In a usage-based model, the amount charged can vary month to month. The invoice itemizes what was used, when it was used, and how charges were calculated, providing clarity to the customer about what they're paying for.
* **Accuracy** Accurate invoices ensure that the customer is billed only for the resources they actually consumed. This minimizes disputes and ensures trust between the service provider and the customer.
* **Revenue recognition** For businesses, invoices are necessary for tracking revenue and ensuring that the right amounts are recorded based on actual usage.
* **Compliance** In many industries, regulatory requirements mandate accurate invoicing for tax and legal purposes. Invoices help companies comply with tax laws, as they document when services were provided and when payments are due.
* **Cash flow management** Invoices also signal to customers when payments are due, helping businesses manage their cash flow. In usage-based billing, timely invoicing helps businesses maintain steady revenue from varying usage patterns.

The primary mechanism generating invoices in Metronome is the contract. When you provision a contract for a customer, it automatically produces invoices throughout its lifecycle on predefined schedules.

## Types of Metronome invoices​

Metronome produces two types of invoices: usage invoices and scheduled invoices.

### Usage invoices​

Usage invoices record the products or services a customer is entitled to and what they've consumed in a given period. These are generated according to the usage statement schedule and frequency defined in the contract. They're continuously updated in real time, providing visibility into customer spend.

If a customer has a credit or prepaid commitment applied, the usage invoice may reflect a zero-dollar total and not require payment. In these cases, the usage invoice serves as a record for revenue recognition and can be displayed through a dashboard instead of getting sent for payment collection.

A usage invoice includes:

* All services the customer is entitled to, as listed on the rate card with the list price, customer-specific price, and the quantity consumed
* All commitments and credits applied to the invoice

**Unique features**

Schedule changes to any product, rate, commitment, or credit in Metronome. These changes are automatically reflected on the invoice without requiring the issuance of a new invoice. Additionally, Metronome breaks down the usage invoice into distinct time periods, detailing when various services were entitled, rates were active, and commitments or credits were available. Metronome applies the commitments or credits to each line item and calculates the overage per item. This flexibility helps you schedule mid-period changes to a billable metric or price and have the invoice automatically adjust.

**Schema**

Usage invoices are identified by the type `USAGE` and are always associated with a billing period, defined by the `billing_period_start_date` and `billing_period_end_date`. Usage invoices have a configurable grace period, during which usage can still be reported after the `billing_period_end_date`. Once finalized, the invoice is issued on the `issue_date`.

### Scheduled invoices​

Metronome contracts can also produce scheduled invoices. These are used for fixed charges like commitment prepayments, postpaid commitment true-ups, or simple upfront or recurring fees. Generate a scheduled invoice by adding a commitment or scheduled charge to a contract.

**Unique features**

Metronome offers a highly flexible set of scheduling options. Create a custom billing schedule that meets your customer needs, enabling you to close deals faster. Schedule charges to invoice monthly, quarterly, or even define precise custom schedules. Metronome automatically groups all scheduled charges onto the same invoice.

**Schema**

Scheduled invoices are identified by the type `SCHEDULED`. There is no grace period for these invoices. They are finalized on the configured `issue_date` (see limitations below) and do not have a `billing_period_start_date` or `billing_period_end_date`.

<Note>
  **SCHEDULED INVOICE FINALIZATION MECHANICS**

  Scheduled invoices are finalized according to specific timing rules based on their issue date and contract creation time:

  * If the issue date is in the past or present, the invoice is finalized immediately
  * If the issue date is within 2 hours of contract creation, the invoice is finalized within 2 hours and 30 minutes of the contract being created
  * If the issue date is more than 2 hours from contract creation, the invoice is finalized within 30 minutes of the issue date
</Note>

## Invoice lifecycle​

All invoices are in one of four states: draft, grace period, finalized, or void.

### Draft invoices​

Draft is an initial invoice state. What occurs during or after that state depends upon the invoice type.

**Usage invoices**

As soon as a contract billing period starts, Metronome creates a draft usage invoice (`status` = `DRAFT`). As usage data is sent to Metronome, the draft invoice continuously updates to reflect real-time spend.

**Scheduled invoices**

Once you add scheduled charges or prepaid commitments to a contract, Metronome creates draft scheduled invoices (`status` = `DRAFT`). These remain in draft until the scheduled invoice date.

For postpaid commitments, Metronome automatically creates a draft true-up invoice (`status` = `DRAFT`). This invoice tracks how much more the customer needs to spend to meet their commitment. It finalizes after the last usage invoice for that contract finalizes.

### Grace period​

After the billing period ends, Metronome enforces a grace period before finalizing the invoice. This buffer period allows for late-arriving usage data and invoice corrections. The grace period is 24 hours by default. Contact us via the [Metronome support portal](https://support.metronome.com/) to customize the grace period.

### Finalized invoices​

Once an invoice is finalized (`status` = `FINALIZED`), no further changes can be made, even if additional usage is reported for the period. The finalized invoice is immutable and ready for customer delivery and official reporting. If the finalized invoice contains errors, it can be voided and regenerated, incorporating any updated changes. Finalized invoices are distributed and collected based on your contract's [billing configuration](/guides/customers-billing/manage-customers/provision-a-customer#add-a-billing-configuration-to-a-customer).

### Voided invoices

A finalized invoice can be voided (`status` = `VOID`) if it was created in error due to a provisioning issue.

<Note>
  **REGENERATE VOIDED INVOICES**

  Once an invoice has been voided, you can regenerate it through the UI when viewing the invoice, or through the [/invoices/regenerate](/api-reference/invoices/regenerate-an-invoice) API endpoint. When an invoice is regenerated, it will be recalculated using up-to-date usage and pricing terms.
</Note>

## Invoice line items

Each invoice consists of line items corresponding to products and services in Metronome. Each line item includes:

* **Display name** , the name of the product or service
* **Quantity (decimal number)** , a default quantity or one computed from customer usage data
* **Unit price** , the price per unit of the service
* **Total** , automatically calculated by multiplying the quantity by the unit price
* **Pricing and presentation group keys** , optional grouping information to organize pricing data

## Invoice example​

This example shows how Metronome creates invoice line items.

Your customer is provisioned with access to a product named API Tokens with a unit price of \$1 per unit. The customer also prepurchased a \$50 prepaid commit, which corresponds to 50 tokens. If the customer used 80 tokens in the current billing period, the Draft invoice is broken down into:

<Info>
  All monetary values in this invoice are in the currency's denomination. For USD, values are in **cents** — so a `"total"` of `3000` means \$30.00 and a `"unit_price"` of `100` means \$1.00. Other currencies may use whole units. See [currency denomination](/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits#currency-denomination) for details.
</Info>

* A line item for the first 50 tokens consumed resulting in a total of \$50
* A line item adjustment indicating that the \$50 prepaid commitment offset the total for the first \$50
* A line item covering the remaining 30 tokens consumed for a total of \$30

```json theme={null}
{  
  "id": "INVOICE_ID",  
  "issued_at": "2024-10-02T00:00:00+00:00",  
  "start_timestamp": "2024-09-01T00:00:00+00:00",  
  "end_timestamp": "2024-10-01T00:00:00+00:00",  
  "customer_id": "CUSTOMER_ID",  
  "customer_custom_fields": {},  
  "type": "USAGE",  
  "credit_type": {  
    "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
    "name": "USD (cents)"  
  },  
  "status": "DRAFT",  
  "total": 3000,  
  "external_invoice": null,  
  "contract_id": "CONTRACT_ID",  
  "contract_custom_fields": {},  
  "custom_fields": {},  
  "billable_status": "billable",  
  "line_items": [  
    {  
      "product_id": "PRODUCT_ID",  
      "product_type": "UsageProductListItem",  
      "product_custom_fields": {},  
      "name": "Tokens Consumed",  
      "total": 5000,  
      "credit_type": {  
        "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
        "name": "USD (cents)"  
      },  
      "starting_at": "2024-09-01T00:00:00+00:00",  
      "ending_before": "2024-10-01T00:00:00+00:00",  
      "commit_id": "COMMIT_ID",  
      "commit_segment_id": "COMMIT_SEGMENT_ID",  
      "commit_type": "PrepaidCommit",  
      "commit_custom_fields": {},  
      "unit_price": 100,  
      "quantity": 50  
    },  
    {  
      "product_id": "PRODUCT_ID",  
      "product_type": "UsageProductListItem",  
      "product_custom_fields": {},  
      "name": "Prepaid Tokens applied",  
      "total": -5000,  
      "credit_type": {  
        "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
        "name": "USD (cents)"  
      },  
      "starting_at": "2024-09-01T00:00:00+00:00",  
      "ending_before": "2024-10-01T00:00:00+00:00",  
      "commit_id": "COMMIT_ID",  
      "commit_segment_id": "COMMIT_SEGMENT_ID",  
      "commit_type": "PrepaidCommit",  
      "commit_custom_fields": {}  
    },  
    {  
      "product_id": "PRODUCT_ID",  
      "product_type": "UsageProductListItem",  
      "product_custom_fields": {},  
      "name": "Tokens Consumed",  
      "total": 3000,  
      "credit_type": {  
        "id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
        "name": "USD (cents)"  
      },  
      "starting_at": "2024-09-01T00:00:00+00:00",  
      "ending_before": "2024-10-01T00:00:00+00:00",  
      "unit_price": 100,  
      "quantity": 30  
    }  
  ]  
}
```

The [Metronome app](https://app.metronome.com/) visualizes the invoice object, showing the usage quantity continuously updated as usage events are ingested for this customer and adjustments like prepaid commit and credits grants applied.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/get-started/core-concepts/invoicing/invoice-visualization-0c80fcdcdf83c0cc8f24897d213a430b.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=0431ce544e3a1341a73878b3003ca9fe" alt="Invoice visualization" width="855" height="364" data-path="images/docs/get-started/core-concepts/invoicing/invoice-visualization-0c80fcdcdf83c0cc8f24897d213a430b.png" />
</Frame>

## Invoice presentation​

In Metronome, you control how your invoices are structured and the level of granularity to provide your customers to ensure trust and confidence. You can configure:

* A clear product name that Metronome shows as the line item description.
* The optional pricing group keys to add granularity on each usage product. For example, you can set a different price for input and output tokens.
* The optional presentation group keys for grouping usage products under a property like a team name or an organization name.

### Line items with pricing group keys​

You can configure usage products with one or multiple pricing grouping keys and set a rate for each pricing group key combination. Metronome invoices automatically have a separate line item for each combination of pricing group keys.

Consider the example of `Tokens Consumed`, where you add a pricing group key `type` to the product and set two rates in the rate card: one for `type = input` and one for `type = output`. The invoice now has two line items, showing the pricing group key value for each:

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/get-started/core-concepts/invoicing/invoice-pricing-group-keys-8a6bf1ee9499a71314f996c72c90e2fa.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=784fd04d6060a68d51197eba5786e077" alt="Invoice with pricing grouped keys" width="1688" height="782" data-path="images/docs/get-started/core-concepts/invoicing/invoice-pricing-group-keys-8a6bf1ee9499a71314f996c72c90e2fa.png" />
</Frame>

Note that unlike usage products without a pricing group key, Metronome does not create line items for each pricing group key unless it has usage data.

### Group line items with presentation group keys​

On top of pricing group keys, group usage products on an invoice by any relevant property. This helps your customers do things like allocate spend to the appropriate business unit.

Consider the previous example where customers create `projects` and consume tokens by project. You want to group the usage line items by `project_name` on the invoice. To do so, set a presentation group key on your `Tokens Consumed` product. The Metronome invoice automatically groups line items by `project_name`.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/get-started/core-concepts/invoicing/invoice-presentation-group-keys-6fb71250f9fd6c7e1302157df51a349d.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=10b6e816f60da5156d875b6a05622158" alt="Invoice with presentation grouped keys" width="1690" height="1074" data-path="images/docs/get-started/core-concepts/invoicing/invoice-presentation-group-keys-6fb71250f9fd6c7e1302157df51a349d.png" />
</Frame>
