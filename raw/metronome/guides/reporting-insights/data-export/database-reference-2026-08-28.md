<!-- Source URL: https://docs.metronome.com/guides/reporting-insights/data-export/database-reference.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Database reference

This page provides a comprehensive schema reference for all data exported from Metronome to your data warehouse. Use this reference to understand the structure and contents of each table available in your exports.

For SQL query examples, see the [SQL cookbook](/guides/reporting-insights/data-export/cookbook).

<Note>
  **NULLABLE COLUMNS**

  Due to our export methodology, all columns may appear as nullable in your destination schema.
</Note>

## Core entities

Foundational data types and entities used throughout Metronome.

<AccordionGroup>
  <Accordion title="billable_metric">
    ### `billable_metric`

    | Column             | Type        | Description                                                       |
    | ------------------ | ----------- | ----------------------------------------------------------------- |
    | `id`               | `string`    | ID of the billable metric                                         |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`              |
    | `aggregate`        | `string`    | The aggregation type                                              |
    | `aggregate_keys`   | `json`      | The keys used for aggregation                                     |
    | `group_keys`       | `json`      | The group by keys associated with this billable metric            |
    | `name`             | `string`    | Name of the billable metric                                       |
    | `created_at`       | `timestamp` | The timestamp (UTC) of when the billable\_metric was created      |
    | `archived_at`      | `timestamp` | The timestamp (UTC) of when the billable\_metric was archived     |
    | `updated_at`       | `timestamp` | The timestamp (UTC) of when the billable\_metric was last updated |
  </Accordion>

  <Accordion title="credit_type">
    ### `credit_type`

    | Column                   | Type        | Description                                                 |
    | ------------------------ | ----------- | ----------------------------------------------------------- |
    | `_metronome_metadata_id` | `string`    | Metronome metadata ID                                       |
    | `id`                     | `string`    | The credit type ID                                          |
    | `environment_type`       | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`        |
    | `name`                   | `string`    | The name of the credit type                                 |
    | `is_currency`            | `boolean`   | Whether or not the credit type is a currency, TRUE or FALSE |
    | `updated_at`             | `timestamp` | The timestamp (UTC) this row was last updated               |
  </Accordion>
</AccordionGroup>

### Events

The full set of deduplicated raw events received by Metronome, regardless of whether or not they matched a billable metric.

<AccordionGroup>
  <Accordion title="events">
    ### `events`

    | Column                   | Type        | Description                                          |
    | ------------------------ | ----------- | ---------------------------------------------------- |
    | `transaction_id`         | `string`    | The unique ID of the event                           |
    | `environment_type`       | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION` |
    | `customer_id`            | `string`    | The ID of the customer the event applies to          |
    | `timestamp`              | `timestamp` | The timestamp (UTC) of the event                     |
    | `event_type`             | `string`    | The event type                                       |
    | `properties`             | `json`      | The properties of the event                          |
    | `_metronome_metadata_id` | `string`    | Metronome metadata ID                                |
    | `updated_at`             | `timestamp` | The timestamp (UTC) this row was last updated        |
  </Accordion>
</AccordionGroup>

### Customers

Includes customer metadata stored in Metronome including their ingest aliases, which can be joined with the `events` table. The `archived_at` column is used to determine if the customer is active.

<AccordionGroup>
  <Accordion title="customer">
    ### `customer`

    | Column                         | Type        | Description                                                          |
    | ------------------------------ | ----------- | -------------------------------------------------------------------- |
    | `id`                           | `string`    | The Metronome ID of the customer                                     |
    | `environment_type`             | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                 |
    | `name`                         | `string`    | The name of the customer                                             |
    | `ingest_aliases`               | `json`      | The ingest aliases of the customer                                   |
    | `salesforce_account_id`        | `string`    | The Salesforce account ID for the customer                           |
    | `billing_provider_type`        | `string`    | The billing provider connected to the customer                       |
    | `billing_provider_customer_id` | `string`    | The billing provider ID of the customer                              |
    | `custom_fields`                | `json`      | Custom fields attached to the customer                               |
    | `created_at`                   | `timestamp` | The timestamp (UTC) of when the customer was created                 |
    | `updated_at`                   | `timestamp` | The timestamp (UTC) of when the customer was last updated            |
    | `archived_at`                  | `timestamp` | The timestamp (UTC) of when the customer was archived, if applicable |
  </Accordion>
</AccordionGroup>

## Invoicing

All invoice-related data including finalized invoices, drafts, and detailed breakdowns.

### Finalized invoices

Includes all invoices to customers that have been finalized or voided. No further changes can be made to these invoices or their corresponding line items.

<AccordionGroup>
  <Accordion title="invoice">
    ### `invoice`

    | Column                                     | Type        | Description                                                                       |
    | ------------------------------------------ | ----------- | --------------------------------------------------------------------------------- |
    | `id`                                       | `string`    | The Metronome invoice ID                                                          |
    | `environment_type`                         | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                              |
    | `status`                                   | `string`    | The Metronome invoice status: `FINALIZED` or `VOID`                               |
    | `total`                                    | `decimal`   | The invoice total                                                                 |
    | `credit_type_id`                           | `string`    | The credit type ID for the invoice                                                |
    | `credit_type_name`                         | `string`    | The name of the credit type associated with the invoice                           |
    | `customer_id`                              | `string`    | The Metronome ID of the customer                                                  |
    | `plan_id`                                  | `string`    | Deprecated field - expect to be `NULL`                                            |
    | `plan_name`                                | `string`    | Deprecated field - expect to be `NULL`                                            |
    | `contract_id`                              | `string`    | The contract ID associated with the invoice                                       |
    | `billing_provider_invoice_id`              | `string`    | The external invoice ID from the billing provider (e.g., Stripe)                  |
    | `billing_provider_type`                    | `string`    | The type of external system billing provider (e.g. Stripe)                        |
    | `billing_provider_invoice_created_at`      | `timestamp` | The timestamp (UTC) the external invoice was created by Metronome                 |
    | `billing_provider_invoice_external_status` | `string`    | The status of the invoice in the external system (e.g. Stripe)                    |
    | `invoice_label`                            | `string`    | The categorical label of the invoice                                              |
    | `metadata`                                 | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata) |
    | `start_timestamp`                          | `timestamp` | Beginning of the usage period that this invoice covers (UTC)                      |
    | `end_timestamp`                            | `timestamp` | End of the usage period that this invoice covers (UTC)                            |
    | `issued_at`                                | `timestamp` | The timestamp (UTC) of when the invoice was issued                                |
    | `updated_at`                               | `timestamp` | The timestamp (UTC) of when this row was last updated                             |
  </Accordion>

  <Accordion title="line_item">
    ### `line_item`

    | Column                 | Type        | Description                                                                                      |
    | ---------------------- | ----------- | ------------------------------------------------------------------------------------------------ |
    | `id`                   | `string`    | The line item ID                                                                                 |
    | `environment_type`     | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                             |
    | `invoice_id`           | `string`    | The Metronome invoice ID associated with the line item                                           |
    | `credit_grant_id`      | `string`    | Deprecated field - expect to be `NULL`                                                           |
    | `credit_type_id`       | `string`    | The credit type ID associated with the line item                                                 |
    | `credit_type_name`     | `string`    | The name of the credit type associated with the line item                                        |
    | `name`                 | `string`    | The line item description                                                                        |
    | `quantity`             | `decimal`   | The quantity associated with the line item; this will always be `1` for invoice adjustments      |
    | `total`                | `decimal`   | The line item total                                                                              |
    | `commit_id`            | `string`    | The commit ID associated with the line item. Only present for Contract Invoices                  |
    | `product_id`           | `string`    | The product ID associated with the line item; this will always be `NULL` for invoice adjustments |
    | `group_key`            | `string`    | The group key associated with the line item                                                      |
    | `group_value`          | `string`    | The group value associated with the line item                                                    |
    | `unit_price`           | `decimal`   | The price associated with the line item                                                          |
    | `pricing_group_values` | `json`      | Optional pricing group values array                                                              |
    | `metadata`             | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                |
    | `subscription_id`      | `string`    | The subscription ID associated with the line item. Only present for subscription charges.        |
    | `is_prorated`          | `boolean`   | Indicates if the value is prorated over the period. For subscription charges only.               |
    | `starting_at`          | `timestamp` | The timestamp (UTC) of when the line item is effective from (inclusive)                          |
    | `ending_before`        | `timestamp` | The timestamp (UTC) of when the line item is effective to (exclusive)                            |
    | `updated_at`           | `timestamp` | The timestamp (UTC) of when the line item was last updated                                       |
  </Accordion>
</AccordionGroup>

### Draft invoices

Includes all invoices to customers that are in a draft state. These tables are daily snapshots of invoices based on each customer's configuration and usage at a point-in-time during the day. The `updated_at` column is the time that the invoice row was calculated while the `snapshot_time` corresponds to the start of day (UTC). An invoice row will be populated once per day throughout a billing period until it is finalized or voided.

If an invoice is in a `DRAFT_INCOMPLETE` state, it means that Metronome hasn't fully computed the invoice. There will be no line items or total on the invoice. Exporting these invoices lets you know that the invoice exists, but Metronome has failed to compute it for some reason. Exporting incomplete invoices enables Metronome to send data to the specified destination as soon as possible. We expect these incomplete invoices to be hydrated in future snapshots.

<AccordionGroup>
  <Accordion title="draft_invoice">
    ### `draft_invoice`

    | Column                                | Type        | Description                                                                                                               |
    | ------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- |
    | `_metronome_metadata_id`              | `string`    | Unique identifier for each draft invoice ID + snapshot\_time pair                                                         |
    | `id`                                  | `string`    | The Metronome invoice ID                                                                                                  |
    | `environment_type`                    | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                      |
    | `snapshot_time`                       | `timestamp` | The timestamp (UTC) aligning with the start of the snapshot                                                               |
    | `status`                              | `string`    | The Metronome invoice status: `DRAFT` or `DRAFT_INCOMPLETE` (see the `invoice` table for `FINALIZED` and `VOID` invoices) |
    | `total`                               | `decimal`   | The invoice total                                                                                                         |
    | `credit_type_id`                      | `string`    | The credit type ID for the invoice                                                                                        |
    | `credit_type_name`                    | `string`    | The name of the credit type associated with the invoice                                                                   |
    | `customer_id`                         | `string`    | The Metronome ID of the customer                                                                                          |
    | `plan_id`                             | `string`    | Deprecated field - expect to be `NULL`                                                                                    |
    | `plan_name`                           | `string`    | Deprecated field - expect to be `NULL`                                                                                    |
    | `contract_id`                         | `string`    | The contract ID associated with the invoice                                                                               |
    | `billable_status`                     | `string`    | Billable status of the invoice, `BILLABLE` or `UNBILLABLE`                                                                |
    | `billing_provider_invoice_id`         | `string`    | The external invoice ID from the billing provider (e.g., Stripe)                                                          |
    | `billing_provider_invoice_created_at` | `timestamp` | The timestamp (UTC) of when the external invoice was created by Metronome                                                 |
    | `label`                               | `string`    | The categorical label of the invoice                                                                                      |
    | `start_timestamp`                     | `timestamp` | Beginning of the usage period that this invoice covers (UTC)                                                              |
    | `end_timestamp`                       | `timestamp` | End of the usage period that this invoice covers (UTC)                                                                    |
    | `updated_at`                          | `timestamp` | The timestamp (UTC) this row was last updated                                                                             |
  </Accordion>

  <Accordion title="draft_line_item">
    ### `draft_line_item`

    | Column                   | Type        | Description                                                                                      |
    | ------------------------ | ----------- | ------------------------------------------------------------------------------------------------ |
    | `_metronome_metadata_id` | `string`    | Opaque unique identifier for each row                                                            |
    | `id`                     | `string`    | The line item ID                                                                                 |
    | `environment_type`       | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                             |
    | `snapshot_time`          | `timestamp` | The timestamp (UTC) aligning with the start of the snapshot                                      |
    | `invoice_id`             | `string`    | The Metronome invoice ID associated with the line item                                           |
    | `credit_grant_id`        | `string`    | Deprecated field - expect to be `NULL`                                                           |
    | `credit_type_id`         | `string`    | The credit type ID associated with the line item                                                 |
    | `credit_type_name`       | `string`    | The name of the credit type associated with the line item                                        |
    | `name`                   | `string`    | The line item description                                                                        |
    | `quantity`               | `decimal`   | The quantity associated with the line item; this will always be `1` for invoice adjustments      |
    | `total`                  | `decimal`   | The line item total                                                                              |
    | `commit_id`              | `string`    | The commit ID associated with the line item. Only present for Contract Invoices                  |
    | `product_id`             | `string`    | The product ID associated with the line item; this will always be `NULL` for invoice adjustments |
    | `group_key`              | `string`    | The group key associated with the line item                                                      |
    | `group_value`            | `string`    | The group value associated with the line item                                                    |
    | `unit_price`             | `decimal`   | The price associated with the line item                                                          |
    | `pricing_group_values`   | `json`      | Optional pricing group values array                                                              |
    | `subscription_id`        | `string`    | The subscription ID associated with the line item. Only present for subscription charges.        |
    | `is_prorated`            | `boolean`   | Indicates if the value is prorated over the period. For subscription charges only.               |
    | `metadata`               | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                |
    | `starting_at`            | `timestamp` | The timestamp (UTC) of when the line item is effective from (inclusive)                          |
    | `ending_before`          | `timestamp` | The timestamp (UTC) of when the line item is effective to (exclusive)                            |
    | `updated_at`             | `timestamp` | The timestamp (UTC) of when the line item was last updated                                       |
  </Accordion>
</AccordionGroup>

### Invoice breakdowns

Invoice breakdowns are stored in four separate tables that are exported to your warehouse destination daily. The draft invoice data exports in snapshots that contains all month-to-date breakdown periods up to the snapshot timestamp. This ensures that any mid-billing period pricing and packaging changes, as well as backdated usage data, correctly reflect in the most recent draft invoice breakdown snapshot.

Finalized invoice breakdowns export incrementally as invoices finalize.

<Note>
  **INVOICE BREAKDOWN FILTERS**

  To reduce the volume of data exported to your data warehouse destination, you can filter invoice breakdown exports to ignore:

  * All \$0 total and >0 quantity invoices and line items
  * All \$0 and 0 quantity invoices and line items

  To enable filters, contact us via the [Metronome support portal](https://support.metronome.com/).
</Note>

<AccordionGroup>
  <Accordion title="breakdowns_invoices">
    ### `breakdowns_invoices`

    | Column                      | Type        | Description                                                                       |
    | --------------------------- | ----------- | --------------------------------------------------------------------------------- |
    | `id`                        | `string`    | The Metronome invoice breakdown ID                                                |
    | `environment_type`          | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                              |
    | `snapshot_timestamp`        | `timestamp` | The timestamp (UTC) aligning with the start of the snapshot                       |
    | `invoice_id`                | `string`    | The Metronome invoice ID associated with the breakdown                            |
    | `customer_id`               | `string`    | The Metronome customer ID associated with the breakdown                           |
    | `transfer_id`               | `string`    | The Metronome transfer ID for this invoice breakdown                              |
    | `credit_type_id`            | `string`    | The ID of the credit type associated with the invoice                             |
    | `net_payment_term_days`     | `integer`   | The net payment term in days associated with the invoice                          |
    | `credit_type_name`          | `string`    | The name of the credit type associated with the invoice                           |
    | `subtotal`                  | `decimal`   | Deprecated field—expect to be `NULL` unless using Plans data model                |
    | `total`                     | `decimal`   | The total for the invoice                                                         |
    | `type`                      | `string`    | The invoice type                                                                  |
    | `external_invoice`          | `json`      | The external invoice data                                                         |
    | `plan_id`                   | `string`    | Deprecated field—expect to be `NULL` unless using Plans data model                |
    | `contract_id`               | `string`    | The contract ID associated with the invoice                                       |
    | `amendment_id`              | `string`    | The amendment ID associated with the invoice                                      |
    | `custom_fields`             | `json`      | Custom fields that apply to the invoice                                           |
    | `billable_status`           | `string`    | The invoice's billable status                                                     |
    | `window_size`               | `string`    | The size of the breakdown window—typically `DAILY`                                |
    | `metadata`                  | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata) |
    | `issued_at`                 | `timestamp` | The timestamp (UTC) when this invoice was issued                                  |
    | `invoice_start_timestamp`   | `timestamp` | Beginning of the usage period that this invoice covers (UTC) (inclusive)          |
    | `invoice_end_timestamp`     | `timestamp` | End of the usage period that this invoice covers (UTC) (exclusive)                |
    | `breakdown_start_timestamp` | `timestamp` | The timestamp corresponding with the start of the breakdown window (inclusive)    |
    | `breakdown_end_timestamp`   | `timestamp` | The timestamp corresponding with the end of the breakdown window (exclusive)      |
    | `updated_at`                | `timestamp` | The timestamp (UTC) when this row last updated                                    |
  </Accordion>

  <Accordion title="breakdowns_line_items">
    ### `breakdowns_line_items`

    | Column                      | Type        | Description                                                                                                                |
    | --------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------- |
    | `id`                        | `string`    | The Metronome line item breakdown ID                                                                                       |
    | `environment_type`          | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                       |
    | `snapshot_timestamp`        | `timestamp` | The timestamp (UTC) aligning with the start of the snapshot                                                                |
    | `watermark_timestamp`       | `timestamp` | The timestamp indicating the latest modification to this row                                                               |
    | `invoice_breakdown_id`      | `string`    | The Metronome invoice breakdown ID associated with the line item                                                           |
    | `name`                      | `string`    | The name of the line item associated with the breakdown                                                                    |
    | `transfer_id`               | `string`    | The Metronome transfer ID for this line item breakdown                                                                     |
    | `group_key`                 | `string`    | The group key associated with the line item                                                                                |
    | `group_value`               | `string`    | The group value associated with the line item                                                                              |
    | `quantity`                  | `decimal`   | The quantity of this line item breakdown row—always 1 for invoice adjustments                                              |
    | `total`                     | `decimal`   | The total for the line item breakdown                                                                                      |
    | `unit_price`                | `decimal`   | The unit price for the line item                                                                                           |
    | `product_id`                | `string`    | The ID of the product for the line item—always NULL for invoice adjustments                                                |
    | `product_type`              | `string`    | The type of product for the line item breakdown                                                                            |
    | `credit_type_id`            | `string`    | The credit type ID associated with the line item                                                                           |
    | `credit_type_name`          | `string`    | The name of the credit type associated with the line item                                                                  |
    | `commit_id`                 | `string`    | The commit ID associated with the line item breakdown                                                                      |
    | `commit_segment_id`         | `string`    | The commit segment ID associated with the line item breakdown                                                              |
    | `commit_type`               | `string`    | The commit type associated with the line item breakdown                                                                    |
    | `subscription_id`           | `string`    | The subscription ID associated with the line item breakdown—only present for subscription charges.                         |
    | `is_prorated`               | `boolean`   | Indicates if the value is prorated over the period. For subscription charges only.                                         |
    | `line_item_id`              | `string`    | The unique line item id that can be used to join with records in the line\_item table                                      |
    | `line_item_type`            | `string`    | The unique line item type that defines the type of revenue represented in the line item                                    |
    | `custom_fields`             | `json`      | Custom fields that apply to the breakdown                                                                                  |
    | `pricing_group_values`      | `json`      | The pricing group values associated with the line item breakdown                                                           |
    | `presentation_group_values` | `json`      | The presentation group values associated with the line item breakdown                                                      |
    | `billable_metric_id`        | `string`    | The billable metric ID that applies to the line item breakdown                                                             |
    | `metadata`                  | `json`      | Additional metadata in JSON format (see [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)) |
    | `breakdown_start_timestamp` | `timestamp` | The timestamp corresponding with the start of the breakdown window (inclusive)                                             |
    | `breakdown_end_timestamp`   | `timestamp` | The timestamp corresponding with the end of the breakdown window (exclusive)                                               |
    | `updated_at`                | `timestamp` | The timestamp (UTC) when this row last updated                                                                             |
  </Accordion>

  <Accordion title="breakdowns_draft_invoices">
    ### `breakdowns_draft_invoices`

    | Column                      | Type        | Description                                                                    |
    | --------------------------- | ----------- | ------------------------------------------------------------------------------ |
    | `id`                        | `string`    | The Metronome invoice breakdown ID                                             |
    | `environment_type`          | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                           |
    | `snapshot_timestamp`        | `timestamp` | The timestamp (UTC) aligning with the start of the snapshot                    |
    | `invoice_id`                | `string`    | The Metronome invoice ID associated with the breakdown                         |
    | `customer_id`               | `string`    | The Metronome customer ID associated with the breakdown                        |
    | `transfer_id`               | `string`    | The Metronome transfer ID for this invoice breakdown                           |
    | `credit_type_id`            | `string`    | The ID of the credit type associated with the invoice                          |
    | `net_payment_term_days`     | `integer`   | The net payment term in days associated with the invoice                       |
    | `credit_type_name`          | `string`    | The name of the credit type associated with the invoice                        |
    | `subtotal`                  | `decimal`   | Deprecated field—expect to be `NULL` unless using Plans data model             |
    | `total`                     | `decimal`   | The total for the invoice                                                      |
    | `type`                      | `string`    | The invoice type                                                               |
    | `external_invoice`          | `json`      | The external invoice data                                                      |
    | `plan_id`                   | `string`    | Deprecated field—expect to be `NULL` unless using Plans data model             |
    | `contract_id`               | `string`    | The contract ID associated with the invoice                                    |
    | `amendment_id`              | `string`    | The amendment ID associated with the invoice                                   |
    | `custom_fields`             | `json`      | Custom fields that apply to the invoice                                        |
    | `billable_status`           | `string`    | The invoice's billable status                                                  |
    | `window_size`               | `string`    | The size of the breakdown window—typically `DAILY`                             |
    | `metadata`                  | `json`      | Additional metadata in JSON format                                             |
    | `issued_at`                 | `timestamp` | The timestamp (UTC) when this invoice was issued                               |
    | `invoice_start_timestamp`   | `timestamp` | Beginning of the usage period that this invoice covers (UTC) (inclusive)       |
    | `invoice_end_timestamp`     | `timestamp` | End of the usage period that this invoice covers (UTC) (exclusive)             |
    | `breakdown_start_timestamp` | `timestamp` | The timestamp corresponding with the start of the breakdown window (inclusive) |
    | `breakdown_end_timestamp`   | `timestamp` | The timestamp corresponding with the end of the breakdown window (exclusive)   |
    | `updated_at`                | `timestamp` | The timestamp (UTC) when this row last updated                                 |
  </Accordion>

  <Accordion title="breakdowns_draft_line_items">
    ### `breakdowns_draft_line_items`

    | Column                      | Type        | Description                                                                                                                |
    | --------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------- |
    | `id`                        | `string`    | The Metronome line item breakdown ID                                                                                       |
    | `environment_type`          | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                       |
    | `snapshot_timestamp`        | `timestamp` | The timestamp (UTC) aligning with the start of the snapshot                                                                |
    | `watermark_timestamp`       | `timestamp` | The timestamp indicating the latest modification to this row                                                               |
    | `invoice_breakdown_id`      | `string`    | The Metronome invoice breakdown ID associated with the line item                                                           |
    | `name`                      | `string`    | The name of the line item associated with the breakdown                                                                    |
    | `transfer_id`               | `string`    | The Metronome transfer ID for this line item breakdown                                                                     |
    | `group_key`                 | `string`    | The group key associated with the line item                                                                                |
    | `group_value`               | `string`    | The group value associated with the line item                                                                              |
    | `quantity`                  | `decimal`   | The quantity of this line item breakdown row; always 1 for invoice adjustments                                             |
    | `total`                     | `decimal`   | The total for the line item breakdown                                                                                      |
    | `unit_price`                | `decimal`   | The unit price for the line item                                                                                           |
    | `product_id`                | `string`    | The ID of the product for the line item; always NULL for invoice adjustments                                               |
    | `product_type`              | `string`    | The type of product for the line item breakdown                                                                            |
    | `credit_type_id`            | `string`    | The credit type ID associated with the line item                                                                           |
    | `credit_type_name`          | `string`    | The name of the credit type associated with the line item                                                                  |
    | `commit_id`                 | `string`    | The commit ID associated with the line item breakdown                                                                      |
    | `commit_segment_id`         | `string`    | The commit segment ID associated with the line item breakdown                                                              |
    | `commit_type`               | `string`    | The commit type associated with the line item breakdown                                                                    |
    | `subscription_id`           | `string`    | The subscription ID associated with the line item breakdown; only present for subscription charges.                        |
    | `is_prorated`               | `boolean`   | Indicates if the value is prorated over the period. For subscription charges only.                                         |
    | `line_item_id`              | `string`    | The unique line item id that can be used to join with records in the line\_item table                                      |
    | `line_item_type`            | `string`    | The unique line item type that defines the type of revenue represented in the line item                                    |
    | `custom_fields`             | `json`      | Custom fields that apply to the breakdown                                                                                  |
    | `pricing_group_values`      | `json`      | The pricing group values associated with the line item breakdown                                                           |
    | `presentation_group_values` | `json`      | The presentation group values associated with the line item breakdown                                                      |
    | `billable_metric_id`        | `string`    | The billable metric ID that applies to the line item breakdown                                                             |
    | `metadata`                  | `json`      | Additional metadata in JSON format (see [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)) |
    | `breakdown_start_timestamp` | `timestamp` | The timestamp corresponding with the start of the breakdown window (inclusive)                                             |
    | `breakdown_end_timestamp`   | `timestamp` | The timestamp corresponding with the end of the breakdown window (exclusive)                                               |
    | `updated_at`                | `timestamp` | The timestamp (UTC) when this row last updated                                                                             |
  </Accordion>
</AccordionGroup>

## Contracts

Includes contract information. The `archived_at` column defines whether the contract has been archived or not.

<AccordionGroup>
  <Accordion title="contracts_contracts">
    ### `contracts_contracts`

    | Column                                | Type                                                                              | Description                                                                                                                                                                                                                                     |
    | ------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                                  | `string`                                                                          | ID of the contract                                                                                                                                                                                                                              |
    | `environment_type`                    | `string`                                                                          | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                                                                                                                            |
    | `snapshot_id`                         | `string`                                                                          | The snapshot ID for the contract row                                                                                                                                                                                                            |
    | `name`                                | `string`                                                                          | Name of the contract                                                                                                                                                                                                                            |
    | `customer_id`                         | `string`                                                                          | The customer ID of the contract                                                                                                                                                                                                                 |
    | `package_id`                          | `string`                                                                          | The ID of the package the contract was created from, if applicable.                                                                                                                                                                             |
    | `rate_card_id`                        | `string`                                                                          | The rate card ID of the contract                                                                                                                                                                                                                |
    | `starting_at`                         | `timestamp`                                                                       | The contract start timestamp (UTC)                                                                                                                                                                                                              |
    | `ending_before`                       | `timestamp`                                                                       | The contract end timestamp (UTC). This timestamp is exclusive.                                                                                                                                                                                  |
    | `archived_at`                         | `timestamp`                                                                       | The timestamp (UTC) of when the contract was archived.                                                                                                                                                                                          |
    | `multiplier_override_prioritization`  | `string`                                                                          | The prioritization for a multiplier override. There are two options: <br />• Lowest multiplier (default): The lowest multiplier, aka the biggest discount, is used.<br />• Explicit: The override with the lowest priority will be prioritized. |
    | `net_payment_terms_days`              | `integer`                                                                         | The amount of time a customer has to pay a contract. For example, "net 30"                                                                                                                                                                      |
    | `usage_statement_schedule_frequency`  | `string`                                                                          | The usage statement generation frequency. For example, "monthly" or "quarterly".                                                                                                                                                                |
    | `scheduled_charges_on_usage_invoices` | `string`                                                                          | Valid values are `ALL` if scheduled invoices will be combined with usage invoices on the same date, otherwise null.                                                                                                                             |
    | `metadata`                            | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata) | JSON encoded object                                                                                                                                                                                                                             |
    | `created_at`                          | `timestamp`                                                                       | The timestamp (UTC) of when the contract was created                                                                                                                                                                                            |
    | `created_by`                          | `string`                                                                          | The entity the contract was created by                                                                                                                                                                                                          |
    | `updated_at`                          | `timestamp`                                                                       | The timestamp (UTC) at which this row was exported                                                                                                                                                                                              |
  </Accordion>

  <Accordion title="contracts_commits">
    ### `contracts_commits`

    <Note>
      The commits table only includes contract-level **commits**. It does not include customer-level commits or credits, or contract-level credits.
    </Note>

    | Column                         | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | ------------------------------ | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                           | `string`    | The commit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | `environment_type`             | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | `snapshot_id`                  | `string`    | The snapshot ID of the row                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | `contract_id`                  | `string`    | The contract ID of the commit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | `amendment_id`                 | `string`    | The amendment ID associated with the commit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | `type`                         | `string`    | The type of commit: `postpaid` or `prepaid`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | `name`                         | `string`    | The name of the commit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | `priority`                     | `float`     | The priority that defines the order in which commits should be applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | `description`                  | `string`    | The description of the commit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | `product_id`                   | `string`    | The product ID associated with the commit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | `amount`                       | `float`     | Deprecated (use the amount from the schedule items instead)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | `access_schedule`              | `json`      | [`AccessSchedule`](/guides/reporting-insights/data-export/database-reference#contracts-commits-accessschedule)                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | `invoice_schedule`             | `json`      | [`InvoiceSchedule`](/guides/reporting-insights/data-export/database-reference#contracts-commits-invoiceschedule) The `invoice_schedule` is always set for "postpaid" commits, sometimes set for "prepaid" commits, and never for "credit"                                                                                                                                                                                                                                                                                                    |
    | `rollover_fraction`            | `float`     | The fraction of the commit that was rolled over                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | `rate_type`                    | `string`    | Either `COMMIT_RATE` or `LIST_RATE`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | `applicable_product_ids`       | `json`      | JSON encoded list of applicable product IDs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | `applicable_product_tags`      | `json`      | JSON encoded list of applicable product tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | `specifiers`                   | `json`      | [`CommitSpecifier[]`](/guides/reporting-insights/data-export/database-reference#contracts-commits-commitspecifier) - JSON encoded list of applicable usage                                                                                                                                                                                                                                                                                                                                                                                   |
    | `ledger`                       | `json`      | [`CommitLedgerEntry[]`](/guides/reporting-insights/data-export/database-reference#contracts-commits-commitledgerentry)                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | `rolled_over_from_commit_id`   | `string`    | The commit ID the commit was rolled over from                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | `rolled_over_from_contract_id` | `string`    | The contract ID the commit was rolled over from                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | `recurring_commit_id`          | `string`    | The ID of the parent config that created this commit (null if this commit was not created by a recurring commit)                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | `metadata`                     | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference#metadata)                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | `balance`                      | `float`     | The current balance of the commit. This balance reflects the amount of commit that the customer has access to use at this moment. Expired and upcoming commit segments contribute 0 to the balance. The balance matches the sum of all ledger entries except when the sum of negative manual ledger entries exceeds the positive amount remaining on the commit. In that case, the balance is 0. All manual ledger entries associated with active commit segments are included in the balance, including future-dated manual ledger entries. |
    | `cost_basis`                   | `float`     | The ratio of the amount paid for the commit to the amount of credit granted                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | `updated_at`                   | `timestamp` | The timestamp (UTC) of when the commit was last updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

    #### `contracts_commits.AccessSchedule`

    ```typescript theme={null}
    interface AccessSchedule {
      credit_type_id: string;
      credit_type_name: string;
      schedule_items: Array<{
        id: string;
        /** ISO-8601 formatted timestamp */
        date: string;
        /** ISO-8601 formatted timestamp */
        end_date: string | null;
        /** Float */
        amount: number;
      }>;
    }
    ```

    #### `contracts_commits.InvoiceSchedule`

    ```typescript theme={null}
    interface InvoiceSchedule {
      credit_type_id: string;
      credit_type_name: string;
      do_not_invoice: boolean;
      schedule_items: Array<{
        id: string;
        /** ISO-8601 formatted timestamp */
        date: string;
        /** Float */
        amount: number;
        invoice_id: string | null;
      }>;
      recurring_schedule: {
        /** ISO-8601 formatted timestamp */
        start_date: string;
        /** ISO-8601 formatted timestamp */
        end_date: string;
        /** Float */
        amount: number;
        amount_distribution: "divided" | "divided_rounded" | "each";
        frequency: "annual" | "monthly" | "quarterly" | "semi_annual";
        /** Float */
        quantity?: number;
        /** Float */
        unit_price?: number;
      } | null;
    }
    ```

    #### `contracts_commits.CommitLedgerEntry`

    ```typescript theme={null}
    type LedgerEntry =
      | {
          /**
           * Represents the starting balance of a postpaid commit.
           */
          type: "postpaid_initial_balance";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
        }
      | {
          /**
           * Represents deductions from the remaining obligation of the
           * postpaid commit as the result of an invoice with usage that
           * applies to this commit.
           */
          type: "postpaid_automated_invoice_deduction";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          invoice_id: string;
        }
      | {
          /**
           * Represents a true-up invoice that was issued for this commit to
           * cover usage that was not covered by automated usage invoices.
           */
          type: "postpaid_trueup";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          invoice_id: string;
        }
      | {
          /**
           * Represents that a prepaid commit segment was started and the customer
           * now has access to the usage amount for that segment. These segments
           * are described in the access schedule of the prepaid commit.
           */
          type: "prepaid_segment_start";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
        }
      | {
          /**
           * Represents deductions from the prepaid commit segment caused by a
           * usage invoice that included usage applicable to this commit.
           */
          type: "prepaid_automated_invoice_deduction";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          /**
           * Represents unused usage from the prepaid commit which was rolled
           * over to a new contract.
           */
          type: "prepaid_rollover";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          new_contract_id: string;
          new_commit_id: string;
        }
      | {
          type: "prepaid_commit_canceled";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          type: "prepaid_commit_credited";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          /**
           * Represents commit amount that was unused and expired at the end of
           * a commit segment. Does not include usage that rolled over to a new
           * contract.
           */
          type: "prepaid_segment_expiration";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
        }
      | {
          type: "prepaid_manual";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          reason: string;
        }
      | {
          type: "postpaid_manual";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
        };
    ```

    #### `contracts_commits.CommitSpecifier`

    ```typescript theme={null}
    type CommitSpecifier = {
      product_id?: string;
      product_tags?: string[];
      presentation_group_values?: {
        [key: string]: string;
      };
      pricing_group_values?: {
        [key: string]: string;
      };
    }
    ```
  </Accordion>

  <Accordion title="contracts_balances">
    ### `contracts_balances`

    | Column                         | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | ------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                           | `string`    | The ID of the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | `environment_type`             | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | `snapshot_id`                  | `string`    | The snapshot ID of the row                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | `customer_id`                  | `string`    | The customer ID of the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | `contract_id`                  | `string`    | The contract ID of the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | `amendment_id`                 | `string`    | The amendment ID of the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | `type`                         | `string`    | Either `postpaid`, `prepaid`, or `credit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
    | `name`                         | `string`    | The name of the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | `priority`                     | `float`     | The priority that defines the order of balance application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | `description`                  | `string`    | The description of the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | `product_id`                   | `string`    | The product ID associated with the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | `access_schedule`              | `json`      | [`AccessSchedule`](/guides/reporting-insights/data-export/database-reference#contracts-balances-accessschedule)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | `invoice_schedule`             | `json`      | [`InvoiceSchedule`](/guides/reporting-insights/data-export/database-reference#contracts-balances-invoiceschedule) - The `invoice_schedule` is always set for "postpaid" commits, sometimes set for "prepaid" commits, and never for "credit"                                                                                                                                                                                                                                                                                                                                                   |
    | `rollover_fraction`            | `float`     | The fraction of the balance that was rolled over                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | `rate_type`                    | `string`    | Either `COMMIT_RATE` or `LIST_RATE`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | `applicable_product_ids`       | `json`      | JSON encoded list of applicable product IDs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | `applicable_product_tags`      | `json`      | JSON encoded list of applicable product tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | `specifiers`                   | `json`      | [`CommitSpecifier[]`](/guides/reporting-insights/data-export/database-reference#contracts-balances-commitspecifier) - JSON encoded list of applicable usage                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | `applicable_contract_ids`      | `json`      | JSON encoded list of applicable contract IDs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | `invoice_contract_id`          | `string`    | The invoice contract ID associated with the balance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | `ledger`                       | `json`      | [`CommitLedgerEntry[]`](/guides/reporting-insights/data-export/database-reference#contracts-balances-commitledgerentry)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | `rolled_over_from_commit_id`   | `string`    | The commit ID the balance was rolled over from                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | `rolled_over_from_contract_id` | `string`    | The contract ID the balance was rolled over from                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | `recurring_commit_id`          | `string`    | The ID of the parent config that created this commit / credit (null if this commit was not created by a recurring commit / credit)                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | `metadata`                     | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference#metadata)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | `balance`                      | `float`     | The current balance of the credit or commit. This balance reflects the amount of credit or commit that the customer has access to use at this moment. Expired and upcoming credit or commit segments contribute 0 to the balance. The balance matches the sum of all ledger entries except when the sum of negative manual ledger entries exceeds the positive amount remaining on the credit or commit. In that case, the balance is 0. All manual ledger entries associated with active credit or commit segments are included in the balance, including future-dated manual ledger entries. |
    | `cost_basis`                   | `float`     | The ratio of the amount paid for the commit to the amount of credit granted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | `updated_at`                   | `timestamp` | The timestamp (UTC) at which this row was exported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

    #### `contracts_balances.AccessSchedule`

    ```typescript theme={null}
    interface AccessSchedule {
      credit_type_id: string;
      credit_type_name: string;
      schedule_items: Array<{
        id: string;
        /** ISO-8601 formatted timestamp */
        date: string;
        /** ISO-8601 formatted timestamp */
        end_date: string | null;
        /** Float */
        amount: number;
      }>;
    }
    ```

    #### `contracts_balances.InvoiceSchedule`

    ```typescript theme={null}
    interface InvoiceSchedule {
      credit_type_id: string;
      credit_type_name: string;
      do_not_invoice: boolean;
      schedule_items: Array<{
        id: string;
        /** ISO-8601 formatted timestamp */
        date: string;
        /** Float */
        amount: number;
        invoice_id: string | null;
      }>;
      recurring_schedule: {
        /** ISO-8601 formatted timestamp */
        start_date: string;
        /** ISO-8601 formatted timestamp */
        end_date: string;
        /** Float */
        amount: number;
        amount_distribution: "divided" | "divided_rounded" | "each";
        frequency: "annual" | "monthly" | "quarterly" | "semi_annual";
        /** Float */
        quantity?: number;
        /** Float */
        unit_price?: number;
      } | null;
    }
    ```

    #### `contracts_balances.CommitLedgerEntry`

    ```typescript theme={null}
    type LedgerEntry =
      | {
          /**
           * Represents the starting balance of a postpaid commit.
           */
          type: "postpaid_initial_balance";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
        }
      | {
          /**
           * Represents deductions from the remaining obligation of the
           * postpaid commit as the result of an invoice with usage that
           * applies to this commit.
           */
          type: "postpaid_automated_invoice_deduction";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          invoice_id: string;
        }
      | {
          /**
           * Represents a true-up invoice that was issued for this commit to
           * cover usage that was not covered by automated usage invoices.
           */
          type: "postpaid_trueup";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          invoice_id: string;
        }
      | {
          /**
           * Represents that a prepaid commit segment was started and the customer
           * now has access to the usage amount for that segment. These segments
           * are described in the access schedule of the prepaid commit.
           */
          type: "prepaid_segment_start";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
        }
      | {
          /**
           * Represents deductions from the prepaid commit segment caused by a
           * usage invoice that included usage applicable to this commit.
           */
          type: "prepaid_automated_invoice_deduction";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          /**
           * Represents unused usage from the prepaid commit which was rolled
           * over to a new contract.
           */
          type: "prepaid_rollover";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          new_contract_id: string;
          new_commit_id: string;
        }
      | {
          type: "prepaid_commit_canceled";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          type: "prepaid_commit_credited";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          /**
           * Represents commit amount that was unused and expired at the end of
           * a commit segment. Does not include usage that rolled over to a new
           * contract.
           */
          type: "prepaid_segment_expiration";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
        }
      | {
          type: "prepaid_manual";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          reason: string;
        }
      | {
          type: "postpaid_manual";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
        }
      | {
          /**
           * Represents that a credit segment was started and the customer
           * now has access to the usage amount for that segment. These segments
           * are described in the access schedule of the credit.
           */
          type: "credit_segment_start";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
        }
      | {
          /**
           * Represents deductions from the credit segment caused by a
           * usage invoice that included usage applicable to this credit.
           */
          type: "credit_automated_invoice_deduction";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          type: "credit_commit_canceled";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          type: "credit_commit_credited";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          invoice_id: string;
        }
      | {
          /**
           * Represents credit amount that was unused and expired at the end of
           * a credit segment.
           */
          type: "credit_segment_expiration";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
        }
      | {
          type: "credit_manual";
          /** ISO-8601 formatted timestamp */
          timestamp: string;
          /** Float */
          amount: number;
          segment_id: string;
          reason: string;
        };
    ```

    #### `contracts_balances.CommitSpecifier`

    ```typescript theme={null}
    type CommitSpecifier = {
      product_id?: string;
      product_tags?: string[];
      presentation_group_values?: {
        [key: string]: string;
      };
      pricing_group_values?: {
        [key: string]: string;
      };
    }
    ```
  </Accordion>

  <Accordion title="contracts_recurring_commits_and_credits">
    <Note>
      This includes any recurring commits and credits that are defined on contracts.
    </Note>

    ### `contracts_recurring_commits_and_credits`

    | Column                    | Type        | Description                                                                                                                                                                                                                                                                                                                                         |
    | ------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                      | `string`    | The unique ID of the recurring commit/credit                                                                                                                                                                                                                                                                                                        |
    | `environment_type`        | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                                                                                                                                                                                                                                |
    | `snapshot_id`             | `string`    | The snapshot ID of the row                                                                                                                                                                                                                                                                                                                          |
    | `contract_id`             | `string`    | The contract ID of the recurring commit/credit                                                                                                                                                                                                                                                                                                      |
    | `customer_id`             | `string`    | The customer ID associated with the recurring commit/credit                                                                                                                                                                                                                                                                                         |
    | `type`                    | `string`    | The type: `commit` or `credit`                                                                                                                                                                                                                                                                                                                      |
    | `name`                    | `string`    | The name that's passed down to created commits/credits                                                                                                                                                                                                                                                                                              |
    | `priority`                | `float`     | The priority that's passed down to created commits/credits                                                                                                                                                                                                                                                                                          |
    | `description`             | `string`    | The description that's passed down to created commits/credits                                                                                                                                                                                                                                                                                       |
    | `product_id`              | `string`    | The product ID that's passed down to created commits/credits                                                                                                                                                                                                                                                                                        |
    | `access_amount`           | `json`      | [`AccessAmount`](/guides/reporting-insights/data-export/database-reference/#contracts_recurring_commits_and_credits-accessamount)                                                                                                                                                                                                                   |
    | `invoice_amount`          | `json`      | [`InvoiceAmount`](/guides/reporting-insights/data-export/database-reference/#contracts_recurring_commits_and_credits-invoiceamount) - Not set for recurring credits, but optional for recurring commits                                                                                                                                             |
    | `rollover_fraction`       | `float`     | The rollover amount that's passed down to created commits/credits. Note that this controls rollover between contracts on contract transition, and not rollover from one period to the next.                                                                                                                                                         |
    | `rate_type`               | `string`    | The rate type that's passed down to created commits/credits                                                                                                                                                                                                                                                                                         |
    | `applicable_product_ids`  | `json`      | The applicable product IDs passed down to created commits/credits                                                                                                                                                                                                                                                                                   |
    | `applicable_product_tags` | `json`      | The applicable product tags passed down to created commits/credits                                                                                                                                                                                                                                                                                  |
    | `specifiers`              | `json`      | [`CommitSpecifier[]`](/guides/reporting-insights/data-export/database-reference/#contracts_recurring_commits_and_credits-commitspecifier) - JSON encoded list of applicable usage                                                                                                                                                                   |
    | `commit_duration`         | `json`      | [`CommitDuration`](/guides/reporting-insights/data-export/database-reference/#contracts_recurring_commits_and_credits-commitduration) How long each created commit is valid for starting from the start date. Currently the unit is always `PERIODS`, representing the length of the contract's billing periods (e.g. monthly, quarterly or annual) |
    | `proration`               | `string`    | Used to control whether the first or last billing periods are prorated. Valid values are `NONE`, `FIRST`, `LAST`, and `FIRST_AND_LAST`. Default is `FIRST_AND_LAST`.                                                                                                                                                                                |
    | `proration_rounding`      | `json`      | [`ProrationRounding`](/guides/reporting-insights/data-export/database-reference/#contracts_recurring_commits_and_credits-prorationrounding) - Optional configuration for improved commit and invoice presentation.                                                                                                                                  |
    | `recurrence_frequency`    | `string`    | If set, commits or credits are created based on the frequency specified and begin to recur at the start date specified on the recurring commit or credit config. Accepted values are `MONTHLY`, `QUARTERLY`, and `ANNUAL`.                                                                                                                          |
    | `metadata`                | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                                                                                                                                                                                                                                                                   |
    | `subscription_config`     | `json`      | [`SubscriptionConfig`](/guides/reporting-insights/data-export/database-reference/#contracts_recurring_commits_and_credits-subscriptionconfig) - Configuration for linked subscription                                                                                                                                                               |
    | `starting_at`             | `timestamp` | The timestamp (UTC) of when the recurring credit or commit starts (inclusive)                                                                                                                                                                                                                                                                       |
    | `ending_before`           | `timestamp` | The timestamp (UTC) of when the recurring credit or commit ends (exclusive)                                                                                                                                                                                                                                                                         |
    | `updated_at`              | `timestamp` | The timestamp (UTC) of when the recurring commit / credit was last updated                                                                                                                                                                                                                                                                          |

    #### `contracts_recurring_commits_and_credits.AccessAmount`

    ```typescript theme={null}
    interface AccessAmount {
      unit_price: number;
      quantity: number;
      credit_type_id: string;
      credit_type_name: string;
    }
    ```

    #### `contracts_recurring_commits_and_credits.InvoiceAmount`

    ```typescript theme={null}
    interface InvoiceAmount {
      unit_price: number;
      quantity: number;
      credit_type_id: string;
      credit_type_name: string;
    }
    ```

    #### `contracts_recurring_commits_and_credits.CommitSpecifier`

    ```typescript theme={null}
    type CommitSpecifier = {
      product_id?: string;
      product_tags?: string[];
      presentation_group_values?: {
        [key: string]: string;
      };
      pricing_group_values?: {
        [key: string]: string;
      };
    }
    ```

    #### `contracts_recurring_commits_and_credits.CommitDuration`

    ```typescript theme={null}
    enum CommitDurationUnit {
      PERIODS = "PERIODS",
    }

    interface CommitDuration {
      unit: CommitDurationUnit;
      value: number;
    }
    ```

    #### `contracts_recurring_commits_and_credits.ProrationRounding`

    ```typescript theme={null}
    interface ProrationRounding {
      access: {
        rounding_method: "round_up" | "round_down" | "round_half_up";
        decimal_places: number;
      };
      invoice: {
        rounding_method: "round_up" | "round_down" | "round_half_up";
        decimal_places: number;
      };
    }
    ```

    #### `contracts_recurring_commits_and_credits.SubscriptionConfig`

    ```typescript theme={null}
    enum SubscriptionAllocationForRecurringCommitEnum {
      POOLED = "pooled",
      INDIVIDUAL = "individual",
    }

    type SubscriptionConfig = {
      subscription_id: string;
      apply_seat_increase_config: {
        is_prorated: boolean;
      };
      allocation: SubscriptionAllocationForRecurringCommitEnum;
    };
    ```
  </Accordion>

  <Accordion title="contracts_usage_filter_schedule">
    <Tip>
      Usage filters change over time, so each row represents a distinct version of a usage filter. To determine the correct version of a usage filter at a given point in time, filter the table by:

      * `contract_id`
      * `starting_at >= {TIME_PERIOD_START}`
      * `ending_before <= {TIME_PERIOD_END}`

      (Filter by all three qualifiers combined.)
    </Tip>

    ### `contracts_usage_filter_schedule`

    | Column          | Type        | Description                                                                          |
    | --------------- | ----------- | ------------------------------------------------------------------------------------ |
    | `id`            | `string`    | The Metronome ID of the contract usage filter                                        |
    | `contract_id`   | `string`    | The ID of the contract associated with the usage filter                              |
    | `starting_at`   | `timestamp` | The timestamp (UTC) of the starting timestamp the usage filter is active (inclusive) |
    | `ending_before` | `timestamp` | The timestamp (UTC) of the ending timestamp the usage filter is active (inclusive)   |
    | `group_key`     | `string`    | The group key for the usage filter                                                   |
    | `group_values`  | `json`      | Group values for this usage filter row, stored in a JSON encoded list                |
    | `metadata`      | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)    |
    | `updated_at`    | `timestamp` | The timestamp (UTC) at which this row was exported                                   |
  </Accordion>

  <Accordion title="contracts_usage_filters">
    ### `contracts_usage_filters`

    <Tip>
      Usage filters change over time, so each row represents a distinct version of a usage filter. To determine the correct version of a usage filter at a given point in time:

      * Filter the table by `contract_id` and `starting_at <= {TIME}`
      * Select the row with the largest `version`
    </Tip>

    | Column             | Type        | Description                                                                          |
    | ------------------ | ----------- | ------------------------------------------------------------------------------------ |
    | `id`               | `string`    | The Metronome ID of the contract usage filter                                        |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                 |
    | `snapshot_id`      | `string`    | The ID of the snapshot this row was transferred during                               |
    | `contract_id`      | `string`    | The ID of the contract associated with the usage filter                              |
    | `version`          | `integer`   | The version of the usage filter                                                      |
    | `starting_at`      | `timestamp` | The timestamp (UTC) of the starting timestamp the usage filter is active (inclusive) |
    | `group_key`        | `string`    | The group key for the usage filter                                                   |
    | `group_values`     | `json`      | Group values for this usage filter row, stored in a JSON encoded list                |
    | `metadata`         | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)    |
    | `updated_at`       | `timestamp` | The timestamp (UTC) at which this row was exported                                   |
  </Accordion>

  <Accordion title="contracts_prepaid_balance_threshold_configurations">
    ### `contracts_prepaid_balance_threshold_configurations`

    | Column                           | Type        | Description                                                                                                                                    |
    | -------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                             | `string`    | Same as `contract_id`                                                                                                                          |
    | `environment_type`               | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                           |
    | `snapshot_id`                    | `string`    | The snapshot ID for the row                                                                                                                    |
    | `contract_id`                    | `string`    | The contract ID associated with the prepaid balance threshold configuration                                                                    |
    | `enabled`                        | `boolean`   | Whether prepaid balance threshold billing is enabled                                                                                           |
    | `threshold_amount`               | `float`     | The prepaid balance threshold at which to trigger threshold commit creation                                                                    |
    | `recharge_to_amount`             | `float`     | The amount to recharge the balance to when the threshold is reached                                                                            |
    | `commit_name`                    | `string`    | The name to use as the line item of the threshold charge                                                                                       |
    | `commit_description`             | `string`    | The description used in the threshold commit                                                                                                   |
    | `commit_product_id`              | `string`    | The fixed product ID used for prepaid balance threshold commits                                                                                |
    | `commit_applicable_product_ids`  | `json`      | JSON encoded list of applicable product IDs for the commit                                                                                     |
    | `commit_applicable_product_tags` | `json`      | JSON encoded list of applicable product tags for the commit                                                                                    |
    | `payment_gate_type`              | `string`    | The payment gate type: `STRIPE`, `EXTERNAL`, or `NONE`                                                                                         |
    | `tax_type`                       | `string`    | The tax provider used: `STRIPE`, `ANROK`, `PRECALCULATED`, or `NONE`                                                                           |
    | `stripe_payment_type`            | `string`    | The payment type if using Stripe payment gate: `PAYMENT_INTENT` or `INVOICE`                                                                   |
    | `metadata`                       | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                                                              |
    | `updated_at`                     | `timestamp` | The timestamp (UTC) at which this row was exported                                                                                             |
    | `commit_duration_value`          | `integer`   | The numeric component of the commit duration, starting from the end of the invoice's service period. If not set, defaults to one year          |
    | `commit_duration_unit`           | `string`    | The unit component of the commit duration: `DAYS`, `WEEKS`, `MONTHS`, or `YEARS`. If not set, defaults to one year                             |
    | `commit_rollover_fraction`       | `float`     | Fraction of the created commit's unused balance that will roll over on contract transitions. Between 0 and 1. If not set, defaults to 1 (100%) |
    | `commit_rate_type`               | `string`    | Either `COMMIT_RATE` or `LIST_RATE`                                                                                                            |
  </Accordion>

  <Accordion title="contracts_spend_threshold_configurations">
    ### `contracts_spend_threshold_configurations`

    | Column                | Type        | Description                                                                       |
    | --------------------- | ----------- | --------------------------------------------------------------------------------- |
    | `id`                  | `string`    | Same as `contract_id`                                                             |
    | `environment_type`    | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                              |
    | `snapshot_id`         | `string`    | The snapshot ID for the row                                                       |
    | `contract_id`         | `string`    | The contract ID associated with the spend threshold configuration                 |
    | `enabled`             | `boolean`   | Whether spend threshold billing is enabled                                        |
    | `threshold_amount`    | `float`     | The spend threshold at which to trigger threshold commit creation                 |
    | `commit_name`         | `string`    | The name to use as the line item of the threshold charge                          |
    | `commit_description`  | `string`    | The description used in the threshold commit                                      |
    | `commit_product_id`   | `string`    | The ID of the fixed product used for spend threshold commits                      |
    | `payment_gate_type`   | `string`    | The payment gate type: `STRIPE`, `EXTERNAL`, or `NONE`                            |
    | `tax_type`            | `string`    | The tax provider used: `STRIPE`, `ANROK`, `PRECALCULATED`, or `NONE`              |
    | `stripe_payment_type` | `string`    | The payment type if using Stripe payment gate: `PAYMENT_INTENT` or `INVOICE`      |
    | `metadata`            | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata) |
    | `updated_at`          | `timestamp` | The timestamp (UTC) at which this row was exported                                |
  </Accordion>

  <Accordion title="contracts_subscriptions">
    ### `contracts_subscriptions`

    | Column                 | Type        | Description                                                                                                                                                                             |
    | ---------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                   | `string`    | The ID of the subscription                                                                                                                                                              |
    | `environment_type`     | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                                                                    |
    | `snapshot_id`          | `string`    | The snapshot ID for the row                                                                                                                                                             |
    | `customer_id`          | `string`    | The Metronome ID of the customer                                                                                                                                                        |
    | `contract_id`          | `string`    | The current contract ID                                                                                                                                                                 |
    | `product_id`           | `string`    | The product ID of the subscription                                                                                                                                                      |
    | `name`                 | `string`    | The name of the subscription                                                                                                                                                            |
    | `description`          | `string`    | The description of the subscription                                                                                                                                                     |
    | `billing_frequency`    | `string`    | The billing frequency of the subscription                                                                                                                                               |
    | `billing_cycle_config` | `json`      | [`BillingCycleConfig`](/guides/reporting-insights/data-export/database-reference/#contracts_subscriptions-billingcycleconfig) - Configuration for subscription billing and invoicing    |
    | `collection_schedule`  | `string`    | The collection schedule of the subscription                                                                                                                                             |
    | `is_prorated`          | `boolean`   | Whether or not the subscription is prorated                                                                                                                                             |
    | `proration_rounding`   | `json`      | [`ProrationRounding`](/guides/reporting-insights/data-export/database-reference/#contracts_subscriptions-prorationrounding) - Optional configuration for improved invoice presentation. |
    | `invoice_behavior`     | `string`    | The invoice behavior of the subscription                                                                                                                                                |
    | `quantity_schedule`    | `json`      | The quantity schedule of the subscription                                                                                                                                               |
    | `fiat_credit_type_id`  | `string`    | The fiat credit type ID used by the subscription                                                                                                                                        |
    | `metadata`             | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                                                                                                       |
    | `starting_at`          | `timestamp` | The timestamp (UTC) of when the subscription starts                                                                                                                                     |
    | `ending_before`        | `timestamp` | The timestamp (UTC) of when the subscription ends                                                                                                                                       |
    | `updated_at`           | `timestamp` | The timestamp (UTC) at which this row was exported                                                                                                                                      |

    #### `contracts_subscriptions.BillingCycleConfig`

    ```typescript theme={null}
    enum SubscriptionInvoicePlacementEnum {
      ON_USAGE_INVOICE = "ON_USAGE_INVOICE",
      ON_SCHEDULED_INVOICE = "ON_SCHEDULED_INVOICE",
    }

    interface BillingCycleConfig {
      anchor_date: timestamp;
      invoice_placement: SubscriptionInvoicePlacementEnum;
    }
    ```

    #### `contracts_subscriptions.ProrationRounding`

    ```typescript theme={null}
    interface ProrationRounding {
      rounding_method: "round_up" | "round_down" | "round_half_up";
      decimal_places: number;
    }
    ```
  </Accordion>

  <Accordion title="contracts_scheduled_charges">
    ### `contracts_scheduled_charges`

    | Column             | Type        | Description                                                                                                   |
    | ------------------ | ----------- | ------------------------------------------------------------------------------------------------------------- |
    | `id`               | `string`    | The ID of the scheduled charge                                                                                |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                          |
    | `snapshot_id`      | `string`    | The snapshot ID for the row                                                                                   |
    | `contract_id`      | `string`    | The contract ID associated with the scheduled charge                                                          |
    | `amendment_id`     | `string`    | The amendment ID associated with the scheduled charge                                                         |
    | `name`             | `string`    | The name of the scheduled charge                                                                              |
    | `description`      | `string`    | The description of the scheduled charge                                                                       |
    | `product_id`       | `string`    | The product ID associated with the scheduled charge                                                           |
    | `credit_type_id`   | `string`    | The ID of the credit type or currency                                                                         |
    | `credit_type_name` | `string`    | The name of the credit type or currency                                                                       |
    | `schedule`         | `json`      | [`Schedule`](/guides/reporting-insights/data-export/database-reference/#contracts-scheduled-charges-schedule) |
    | `metadata`         | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                             |
    | `updated_at`       | `timestamp` | The timestamp (UTC) at which this row was exported                                                            |

    #### `contracts_scheduled_charges.Schedule`

    ```typescript theme={null}
    interface Schedule {
      schedule_items: Array<{
        id: string;
        /** ISO-8601 formatted timestamp */
        date: string;
        /** Float */
        amount: number;
      }>;
      recurring_schedule: {
        /** ISO-8601 formatted timestamp */
        start_date: string;
        /** ISO-8601 formatted timestamp */
        end_date: string;
        /** Float */
        amount: number;
        amount_distribution: "divided" | "divided_rounded" | "each";
        frequency: "annual" | "monthly" | "quarterly" | "semi_annual";
        /** Float */
        quantity?: number;
        /** Float */
        unit_price?: number;
      } | null;
    }
    ```
  </Accordion>

  <Accordion title="contract_hierarchy_configurations">
    ### `contract_hierarchy_configurations`

    | Column                       | Type        | Description                                                                                                                            |
    | ---------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                         | `string`    | Same as `contract_id`                                                                                                                  |
    | `contract_id`                | `string`    | The contract ID associated with the hierarchy configuration                                                                            |
    | `parent_contract_id`         | `string`    | The ID of the parent contract in the hierarchy. Only populated for child contracts.                                                    |
    | `parent_customer_id`         | `string`    | The ID of the parent customer in the hierarchy. Only populated for child contracts.                                                    |
    | `child_info`                 | `json`      | JSON encoded array of child contract information (each containing contract\_id and customer\_id). Only populated for parent contracts. |
    | `updated_at`                 | `timestamp` | The timestamp (UTC) at which this row was last updated                                                                                 |
    | `metadata`                   | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                                                      |
    | `environment_type`           | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                   |
    | `snapshot_id`                | `string`    | The snapshot ID for the row                                                                                                            |
    | `payer`                      | `string`    | The payer associated with the contract. Only populated for child contracts.                                                            |
    | `usage_statement_behavior`   | `string`    | The usage statement behavior configuration. Only populated for child contracts.                                                        |
    | `invoice_consolidation_type` | `string`    | The type of invoice consolidation configured. Only populated for parent contracts.                                                     |
  </Accordion>
</AccordionGroup>

### Contract modifications

Includes any modifications of contracts. The `contracts_overrides` table holds any overrides on top of an existing contract. The `contracts_transitions` and `contracts_edits` tables contain information about contracts ending, renewing, or changing.

<AccordionGroup>
  <Accordion title="contracts_overrides">
    ### `contracts_overrides`

    | Column                    | Type        | Description                                                                                                               |
    | ------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- |
    | `id`                      | `string`    | The ID of the override                                                                                                    |
    | `environment_type`        | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                      |
    | `snapshot_id`             | `string`    | The snapshot ID for the row                                                                                               |
    | `contract_id`             | `string`    | The contract ID of the override                                                                                           |
    | `amendment_id`            | `string`    | The amendment ID of the override                                                                                          |
    | `product_id`              | `string`    | The product ID of the override                                                                                            |
    | `entitled`                | `boolean`   | Whether or not the override is entitled                                                                                   |
    | `rate_type`               | `string`    | Either `multiplier`, `overwrite_flat`, or `overwrite_percentage`. `NULL` if this does not override the rate               |
    | `multiplier`              | `float`     | The multiplier of the override                                                                                            |
    | `priority`                | `float`     | Only defined for contracts with EXPLICIT multiplier override prioritization                                               |
    | `new_rate`                | `json`      | [`Rate`](/guides/reporting-insights/data-export/database-reference/#contracts-overrides-rate)                             |
    | `credit_type_id`          | `string`    | Only defined for "overwrite\_flat", "overwrite\_tiered", "overwrite\_subscription", or "overwrite\_custom" rate types     |
    | `credit_type_name`        | `string`    | Only defined for "overwrite\_flat", "overwrite\_tiered", "overwrite\_subscription", or "overwrite\_custom" rate types     |
    | `applicable_product_tags` | `json`      | JSON encoded list of strings                                                                                              |
    | `override_specifiers`     | `json`      | [`OverrideSpecifier[]`](/guides/reporting-insights/data-export/database-reference/#contracts-overrides-overridespecifier) |
    | `target`                  | `string`    | Either `COMMIT_RATE` or `LIST_RATE`. Indicates which rate the override applies to                                         |
    | `is_commit_specific`      | `boolean`   | Whether or not the override is commit specific                                                                            |
    | `metadata`                | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)                                         |
    | `tiered_override`         | `json`      | Rates and tiers for tiered overrides                                                                                      |
    | `starting_at`             | `timestamp` | The timestamp (UTC) of when the override starts (inclusive)                                                               |
    | `ending_before`           | `timestamp` | The timestamp (UTC) of when the override ends (exclusive)                                                                 |
    | `created_at`              | `timestmap` | The timestamp (UTC) of when the override was created                                                                      |
    | `updated_at`              | `timestamp` | The timestamp (UTC) at which this row was exported                                                                        |

    #### `contracts_overrides.OverrideSpecifier`

    ```typescript theme={null}
    type OverrideSpecifier = {
      commit_ids?: string[];
      product_id?: string;
      product_tags?: string[];
      pricing_group_values?: Array<{
        name: string;
        value: string;
      }>;
      presentation_group_values?: Array<{
        name: string;
        value: string;
      }>;
      // If set, the override will only apply to usage that burns down commits / credits that were created by the specified recurring config
      recurring_commit_ids?: string[];
      any_commit_or_credit_ids?: string[];
    };
    ```

    #### `contracts_overrides.Rate`

    ```typescript theme={null}
    type Rate =
      | {
          type: "flat";
          unit_price: number;
        }
      | {
          type: "percentage";
          fraction: number;
          use_list_prices: boolean;
        }
      | {
          type: "subscription";
          unit_price: number;
          quantity: number;
        };
    ```
  </Accordion>

  <Accordion title="contracts_transitions">
    ### `contracts_transitions`

    | Column             | Type        | Description                                                                       |
    | ------------------ | ----------- | --------------------------------------------------------------------------------- |
    | `id`               | `string`    | The ID of the transition event                                                    |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                              |
    | `snapshot_id`      | `string`    | The snapshot ID for the row                                                       |
    | `type`             | `string`    | The transition type, e.g. "renewal"                                               |
    | `contract_id`      | `string`    | The current contract ID                                                           |
    | `from_contract_id` | `string`    | The contract ID that applies prior to the transition                              |
    | `to_contract_id`   | `string`    | The contract ID that applies after the transition                                 |
    | `date`             | `timestamp` | The timestamp (UTC) of the transition                                             |
    | `metadata`         | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata) |
    | `updated_at`       | `timestamp` | The timestamp (UTC) at which this row was exported                                |
  </Accordion>

  <Accordion title="contracts_edits">
    ### `contracts_edits`

    | Column             | Type        | Description                                                                       |
    | ------------------ | ----------- | --------------------------------------------------------------------------------- |
    | `id`               | `string`    | The ID of the contract edit                                                       |
    | `contract_id`      | `string`    | The contract ID of the edit                                                       |
    | `timestamp`        | `timestamp` | The timestamp (UTC) of the edit                                                   |
    | `edits`            | `json`      | Details of the edits made                                                         |
    | `metadata`         | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata) |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                              |
    | `created_by`       | `string`    | The entity the contract edit was created by                                       |
    | `updated_at`       | `timestamp` | The timestamp (UTC) at which this row was exported                                |
    | `snapshot_id`      | `string`    | The snapshot ID for the row                                                       |
  </Accordion>

  <Accordion title="contracts_amendments">
    ### `contracts_amendments`

    | Column             | Type        | Description                                                                       |
    | ------------------ | ----------- | --------------------------------------------------------------------------------- |
    | `id`               | `string`    | The ID of the contract amendment                                                  |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                              |
    | `snapshot_id`      | `string`    | The snapshot ID for the row                                                       |
    | `contract_id`      | `string`    | The contract ID of the amendment                                                  |
    | `effective_at`     | `timestamp` | The timestamp (UTC) of when the contract amendment is effective starting at       |
    | `metadata`         | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata) |
    | `created_at`       | `timestamp` | The timestamp (UTC) of when the contract amendment was created                    |
    | `created_by`       | `string`    | The entity the contract amendment was created by                                  |
    | `updated_at`       | `timestamp` | The timestamp (UTC) at which this row was exported                                |
  </Accordion>
</AccordionGroup>

### Contract pricing

Includes all information about pricing for a contract.

<AccordionGroup>
  <Accordion title="contracts_rate_cards">
    ### `contracts_rate_cards`

    | Column                    | Type        | Description                                                                      |
    | ------------------------- | ----------- | -------------------------------------------------------------------------------- |
    | `id`                      | `string`    | The Metronome contract rate card ID                                              |
    | `environment_type`        | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                             |
    | `snapshot_id`             | `string`    | The ID of the snapshot this row was transferred during                           |
    | `credit_type_conversions` | `json`      | The credit type conversions associated with the row                              |
    | `metadata`                | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference#metadata) |
    | `aliases`                 | `json`      | List of aliases for the rate card                                                |
    | `fiat_credit_type_id`     | `string`    | The fiat credit type ID associated with the rate card                            |
    | `fiat_credit_type_name`   | `string`    | The name of the fiat credit type associated with the rate card                   |
    | `description`             | `string`    | The description of the rate card                                                 |
    | `name`                    | `string`    | The name of the rate card                                                        |
    | `created_by`              | `string`    | The creator of the rate card                                                     |
    | `created_at`              | `timestamp` | The timestamp (UTC) this row was created                                         |
    | `updated_at`              | `timestamp` | The timestamp (UTC) this row was last updated                                    |
    | `archived_at`             | `timestamp` | The timestmap (UTC) this row was archived if applicable                          |
  </Accordion>

  <Accordion title="contracts_rate_card_entries">
    ### `contracts_rate_card_entries`

    | Column                 | Type        | Description                                                                      |
    | ---------------------- | ----------- | -------------------------------------------------------------------------------- |
    | `id`                   | `string`    | The Metronome contract rate card entry ID                                        |
    | `environment_type`     | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                             |
    | `rate_card_id`         | `string`    | The Metronome rate card ID associated with this entry                            |
    | `product_id`           | `string`    | The product ID associated with this entry                                        |
    | `version`              | `integer`   | The version of this rate card entry                                              |
    | `entitled`             | `boolean`   | Whether or not the entry is entitled                                             |
    | `rate`                 | `string`    | The rate that applies to the entry                                               |
    | `commit_rate`          | `string`    | The commit rate that applies to the entry (if applicable)                        |
    | `product_order`        | `integer`   | The product order associated with the entry                                      |
    | `pricing_group_values` | `json`      | The pricing group values that apply to the entry                                 |
    | `snapshot_id`          | `string`    | The ID of the snapshot this row was transferred during                           |
    | `metadata`             | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference#metadata) |
    | `credit_type_id`       | `string`    | The credit type ID associated with the rate card                                 |
    | `credit_type_name`     | `string`    | The name of the credit type associated with the rate card                        |
    | `billing_frequency`    | `string`    | The billing frequency associated with the entry. For subscriptions only.         |
    | `starting_at`          | `timestamp` | The timestamp (UTC) the rate card entry starts at (inclusive)                    |
    | `ending_before`        | `timestamp` | The timestamp (UTC) the rate card entry ends at (exclusive)                      |
    | `updated_at`           | `timestamp` | The timestamp (UTC) this row was last updated                                    |
  </Accordion>

  <Accordion title="contracts_product_list_item_versions">
    ### `contracts_product_list_item_versions`

    | Column                    | Type        | Description                                                                                    |
    | ------------------------- | ----------- | ---------------------------------------------------------------------------------------------- |
    | `id`                      | `string`    | The Metronome product list item version ID                                                     |
    | `environment_type`        | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                           |
    | `snapshot_id`             | `string`    | The ID of the snapshot this row was transferred during                                         |
    | `product_list_item_id`    | `string`    | The product list item ID associated with the row                                               |
    | `type`                    | `string`    | The type of the product list item version                                                      |
    | `version`                 | `integer`   | The version of the product list item                                                           |
    | `name`                    | `string`    | The name of the product list item version                                                      |
    | `is_refundable`           | `boolean`   | Whether or not the product list item version is refundable                                     |
    | `billable_metric_id`      | `string`    | The billable metric ID associated with the product list item version                           |
    | `composite_product_ids`   | `json`      | The list of composite product IDs associated with the row                                      |
    | `composite_scope`         | `string`    | The scope of the composite product, `CONTRACT` or `CUSTOMER`                                   |
    | `tags`                    | `json`      | The list of tags associated with the row                                                       |
    | `composite_tags`          | `json`      | The list of composite tags associated with the row                                             |
    | `include_composite_spend` | `boolean`   | Whether or not the composite product is allowed to include spend from other composite products |
    | `quantity_conversion`     | `json`      | The quantity conversion for the row                                                            |
    | `quantity_rounding`       | `json`      | The quantity rounding for the row                                                              |
    | `pricing_group_key`       | `json`      | The pricing group key for the row                                                              |
    | `presentation_group_key`  | `json`      | The presentation group key for the row                                                         |
    | `metadata`                | `json`      | [`Metadata`](/guides/reporting-insights/data-export/database-reference/#metadata)              |
    | `starting_at`             | `timestamp` | The timestamp (UTC) the version is active starting at (inclusive)                              |
    | `created_at`              | `timestamp` | The timestamp (UTC) this row was created at                                                    |
    | `created_by`              | `string`    | The entity this row was created by                                                             |
    | `updated_at`              | `timestamp` | The timestamp (UTC) this row was last updated                                                  |
  </Accordion>
</AccordionGroup>

## Packages

Includes information related to packages.

<AccordionGroup>
  <Accordion title="packages">
    ### `packages`

    | Column                                | Type                    | Description                                                                                                                                                                                                                                                       |
    | ------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`                                  | `string`                | ID of the package                                                                                                                                                                                                                                                 |
    | `name`                                | `string`                | Name of the package                                                                                                                                                                                                                                               |
    | `rate_card_id`                        | `string`                | The ID of the rate card used on the package                                                                                                                                                                                                                       |
    | `duration_unit`                       | `string`                | The unit of the package duration. Available values are `DAYS`, `WEEKS`, `MONTHS`, `YEARS`                                                                                                                                                                         |
    | `duration_value`                      | `integer`               | The value of the package duration. `duration_unit` + `duration_value` represent the length of the package                                                                                                                                                         |
    | `multiplier_override_prioritization`  | `string`                | The prioritization for a multiplier override. There are two options: <br /> <ul><li>Lowest multiplier (default): The lowest multiplier, aka the biggest discount, is used.</li><li>Explicit: The override with the lowest priority will be prioritized.</li></ul> |
    | `net_payment_terms_days`              | `integer`               | The amount of time a customer has to pay a contract. For example, “net 30"                                                                                                                                                                                        |
    | `usage_statement_schedule_frequency`  | `string`                | The usage statement generation frequency. For example, “monthly” or “quarterly”.                                                                                                                                                                                  |
    | `scheduled_charges_on_usage_invoices` | `string`                | Valid values are `ALL` if scheduled invoices will be combined with usage invoices on the same date, otherwise null.                                                                                                                                               |
    | `billing_provider`                    | `string`                | The billing provider used on a contract created from the package.                                                                                                                                                                                                 |
    | `delivery_method`                     | `string`                | The delivery method used on a contract created from the package.                                                                                                                                                                                                  |
    | `aliases`                             | `json`                  | List of scheduled aliases for the package                                                                                                                                                                                                                         |
    | `created_at`                          | `timestamp`             | The timestamp (UTC) of when the package was created                                                                                                                                                                                                               |
    | `created_by`                          | `string`                | The entity the package was created by                                                                                                                                                                                                                             |
    | `archived_at`                         | `timestamp`             | The timestamp (UTC) of when the package was archived                                                                                                                                                                                                              |
    | `updated_at`                          | `timestamp`             | The timestamp (UTC) at which this row was exported                                                                                                                                                                                                                |
    | `environment_type`                    | `string`                | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                                                                                                                                              |
    | `snapshot_id`                         | `string`                | The snapshot ID for the contract row                                                                                                                                                                                                                              |
    | `metadata`                            | [`Metadata`](#metadata) | JSON encoded object                                                                                                                                                                                                                                               |
  </Accordion>
</AccordionGroup>

## Payments

<Note>
  **Private Beta**

  Metronome invoicing is currently in Private Beta. Contact us via the [Metronome support portal](https://support.metronome.com/) for early access.
</Note>

Payment information when invoicing with Metronome.

<AccordionGroup>
  <Accordion title="payment">
    ### `payment`

    | Column             | Type        | Description                                                                                                                                                                          |
    | ------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | `id`               | `string`    | The ID of the payment                                                                                                                                                                |
    | `invoice_id`       | `string`    | The invoice ID associated with the payment                                                                                                                                           |
    | `customer_id`      | `string`    | The customer ID associated with the payment                                                                                                                                          |
    | `contract_id`      | `string`    | The contract ID associated with the payment                                                                                                                                          |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                                                                                                 |
    | `amount`           | `decimal`   | The total amount of the payment                                                                                                                                                      |
    | `amount_paid`      | `decimal`   | The amount that has been paid; equals `amount` if status is `PAID`, otherwise `0`                                                                                                    |
    | `credit_type_id`   | `string`    | The credit type ID (fiat currency) for the payment                                                                                                                                   |
    | `credit_type_name` | `string`    | The name of the credit type associated with the payment                                                                                                                              |
    | `status`           | `string`    | The status of the payment                                                                                                                                                            |
    | `error_message`    | `string`    | Error message from the payment provider, if applicable                                                                                                                               |
    | `payment_gateway`  | `json`      | [`PaymentGateway`](/guides/reporting-insights/data-export/database-reference/#payment-paymentgateway) - Payment gateway details (e.g., Stripe payment intent and method information) |
    | `created_at`       | `timestamp` | The timestamp (UTC) of when the payment was created                                                                                                                                  |
    | `updated_at`       | `timestamp` | The timestamp (UTC) of when the payment was last updated                                                                                                                             |

    #### `payment.PaymentGateway`

    ```typescript theme={null}
    type PaymentGateway = {
      type: "stripe";
      stripe: {
        payment_intent_id: string;
        payment_method_id: string;
        error: string | null;
      };
    } | null;
    ```
  </Accordion>
</AccordionGroup>

## Alerts

Includes alerts and the history of customer alerts triggered.

<AccordionGroup>
  <Accordion title="alert">
    ### `alert`

    | Column             | Type        | Description                                                                                              |
    | ------------------ | ----------- | -------------------------------------------------------------------------------------------------------- |
    | `id`               | `string`    | The ID of the alert                                                                                      |
    | `name`             | `string`    | The name of the alert                                                                                    |
    | `alert_type`       | `string`    | The type of alert                                                                                        |
    | `threshold`        | `decimal`   | The threshold to trigger the alert                                                                       |
    | `webhooks_enabled` | `boolean`   | Indicates if the alert is configured for webhooks                                                        |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                                                     |
    | `created_at`       | `timestamp` | The timestamp (UTC) of when the alert was created                                                        |
    | `disabled_at`      | `timestamp` | The timestamp (UTC) of when the alert was disabled                                                       |
    | `updated_at`       | `timestamp` | The timestamp (UTC) of when the alert was last updated                                                   |
    | `archived_at`      | `timestamp` | The timestamp (UTC) of when the alert was archived                                                       |
    | `group_values`     | `json`      | The group value filters associated with the alert. Only present for `spend_threshold_reached` alerts.    |
    | `seat_filter`      | `json`      | The seat filter associated with the alert. Only present for `low_remaining_seat_balance_reached` alerts. |
    | `customer_id`      | `string`    | The customer ID associated with the alert. If null, the configured alert applies to all customers.       |
  </Accordion>

  <Accordion title="customer_alert_history">
    ### `customer_alert_history`

    | Column             | Type        | Description                                                         |
    | ------------------ | ----------- | ------------------------------------------------------------------- |
    | `id`               | `string`    | The Metronome ID of the customer alert history                      |
    | `environment_type` | `string`    | The Metronome environment, `SANDBOX` or `PRODUCTION`                |
    | `customer_id`      | `string`    | The name of the customer associated with the alert history          |
    | `alert_id`         | `string`    | The alert ID associated with the row                                |
    | `alert_status`     | `string`    | The alert status associated with the row                            |
    | `additional_data`  | `json`      | Additional data about the alert                                     |
    | `created_at`       | `timestamp` | Timestamp (UTC) when the alert was evaluated and the status changed |
  </Accordion>
</AccordionGroup>

## Metadata

Many tables in the data export include a `metadata` column. Clients using Metronome have a variety of external systems and require different metadata to be stored. This metadata is client-specific and is stored as a JSON object in the `metadata` column of the table.
