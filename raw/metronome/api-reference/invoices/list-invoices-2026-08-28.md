<!-- Source URL: https://docs.metronome.com/api-reference/invoices/list-invoices.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List invoices

> Retrieves a paginated list of invoices for a specific customer, with flexible filtering options to narrow results by status, date range, credit type, and more. This endpoint provides a comprehensive view of a customer's billing history and current charges, supporting both real-time billing dashboards and historical reporting needs.

### Use this endpoint to:
- Display historical invoice details in customer-facing dashboards or billing portals.
- Retrieve current month draft invoices to show customers their month-to-date spend.
- Access finalized invoices for historical billing records and payment reconciliation.
- Validate customer pricing and credit applications for customer support queries. 
- Generate financial reports by filtering invoices within specific date ranges

### Key response fields:
Array of invoice objects containing:
- Invoice ID and status (DRAFT, FINALIZED, VOID)
- Invoice type (USAGE, SCHEDULED)
- Billing period start and end dates
- Issue date and due date
- Total amount, subtotal, and amount due
- Applied credits summary
- Contract ID reference
- External billing provider status (if integrated with Stripe, etc.)
- Pagination metadata `next_page` cursor

### Usage guidelines:
- The endpoint returns invoice summaries; use the Get Invoice endpoint for detailed line items
- Draft invoices are continuously updated as new usage is reported and will show real-time spend
- Results are ordered by creation date descending by default (newest first)
- When filtering by date range, the filter applies to the billing period, not the issue date
- For customers with many invoices, implement pagination to ensure all results are retrieved
External billing provider statuses (like Stripe payment status) are included when applicable
- Voided invoices are included in results by default unless filtered out by status




## OpenAPI

````yaml /openapi.json get /v1/customers/{customer_id}/invoices
openapi: 3.0.1
info:
  title: Metronome
  version: 1.0.0
servers:
  - url: https://api.metronome.com
    description: Production server
security:
  - bearerAuth: []
tags:
  - name: Customers
    description: >-
      [Customers](https://docs.metronome.com/provisioning/create-customers/) in
      Metronome represent your users for all billing and reporting. Use these
      endpoints to create, retrieve, update, and archive customers and their
      billing configuration.
  - name: Billable metrics
    description: >-
      [Billable
      metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics)
      in Metronome represent the various consumption components that Metronome
      meters and aggregates.
  - name: Usage
    description: >-
      [Usage
      events](https://docs.metronome.com/connecting-metronome/send-usage-data/)
      are the basis for billable metrics. Use these endpoints to send usage
      events to Metronome and retrieve aggregated event data.
  - name: Products
    description: Products are the items that customers purchase.
  - name: Rate cards
    description: Rate cards are used to define default pricing for products.
  - name: Contracts
    description: >-
      A contract defines a customer’s products, pricing, discounts, commitments,
      and more. Use these endpoints to create and update contracts data.
  - name: Credits and commits
    description: Credits and commits are used to manage customer balances.
  - name: Invoices
    description: >-
      [Invoices](https://docs.metronome.com/invoicing/) reflect how much a
      customer spent during a period, which is the basis for billing. Metronome
      automatically generates invoices based upon your pricing, packaging, and
      usage events. Use these endpoints to retrieve invoices.
  - name: Alerts
    description: >-
      [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor
      customer spending, balances, and other billing factors. Use these
      endpoints to create, retrieve, and archive customer alerts. To view sample
      alert payloads by alert type, navigate
      [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
  - name: Custom fields
    description: >-
      [Custom fields](https://docs.metronome.com/integrations/custom-fields/)
      enable adding additional data to Metronome entities. Use these endpoints
      to create, retrieve, update, and delete custom fields.
  - name: Security
    description: >-
      [Security](https://docs.metronome.com/developer-resources/security/)
      endpoints allow you to retrieve security-related data.
  - name: Settings
    description: >-
      Use these endpoints to configure a billing API key, a webhook secret, or
      invoice finalization behavior.
  - name: Named schedules
    description: >-
      Named schedules are used for storing custom data that can change over
      time. Named schedules are often used in custom pricing logic.
paths:
  /v1/customers/{customer_id}/invoices:
    get:
      tags:
        - Invoices
      summary: List invoices
      description: >
        Retrieves a paginated list of invoices for a specific customer, with
        flexible filtering options to narrow results by status, date range,
        credit type, and more. This endpoint provides a comprehensive view of a
        customer's billing history and current charges, supporting both
        real-time billing dashboards and historical reporting needs.


        ### Use this endpoint to:

        - Display historical invoice details in customer-facing dashboards or
        billing portals.

        - Retrieve current month draft invoices to show customers their
        month-to-date spend.

        - Access finalized invoices for historical billing records and payment
        reconciliation.

        - Validate customer pricing and credit applications for customer support
        queries. 

        - Generate financial reports by filtering invoices within specific date
        ranges


        ### Key response fields:

        Array of invoice objects containing:

        - Invoice ID and status (DRAFT, FINALIZED, VOID)

        - Invoice type (USAGE, SCHEDULED)

        - Billing period start and end dates

        - Issue date and due date

        - Total amount, subtotal, and amount due

        - Applied credits summary

        - Contract ID reference

        - External billing provider status (if integrated with Stripe, etc.)

        - Pagination metadata `next_page` cursor


        ### Usage guidelines:

        - The endpoint returns invoice summaries; use the Get Invoice endpoint
        for detailed line items

        - Draft invoices are continuously updated as new usage is reported and
        will show real-time spend

        - Results are ordered by creation date descending by default (newest
        first)

        - When filtering by date range, the filter applies to the billing
        period, not the issue date

        - For customers with many invoices, implement pagination to ensure all
        results are retrieved

        External billing provider statuses (like Stripe payment status) are
        included when applicable

        - Voided invoices are included in results by default unless filtered out
        by status
      operationId: listInvoices-v1
      parameters:
        - $ref: '#/components/parameters/CustomerId'
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/NextPage'
        - $ref: '#/components/parameters/InvoiceStatus'
        - $ref: '#/components/parameters/InvoiceType'
        - $ref: '#/components/parameters/SkipZeroQtyLineItems'
        - in: query
          name: sort
          description: >-
            Invoice sort order by issued_at, e.g. date_asc or date_desc. 
            Defaults to date_asc.
          required: false
          schema:
            type: string
            enum:
              - date_asc
              - date_desc
        - in: query
          name: credit_type_id
          description: Only return invoices for the specified credit type
          required: false
          schema:
            type: string
        - in: query
          name: contract_id
          description: Only return invoices for the specified contract
          required: false
          schema:
            type: string
            format: uuid
        - in: query
          name: starting_on
          description: >-
            RFC 3339 timestamp (inclusive). Invoices will only be returned for
            billing periods that start at or after this time.
          required: false
          schema:
            type: string
            format: date-time
        - in: query
          name: ending_before
          description: >-
            RFC 3339 timestamp (exclusive). Invoices will only be returned for
            billing periods that end before this time.
          required: false
          schema:
            type: string
            format: date-time
        - in: query
          name: webhook_notification_id
          x-mint:
            groups:
              - ff:api-allow-webhook-notification-id
          x-stainless-skip: true
          description: >-
            Indicates that this API request was triggered by a webhook
            notification with the provided ID.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                  - next_page
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Invoice'
                  next_page:
                    type: string
                    nullable: true
              examples:
                contracts:
                  value:
                    data:
                      - id: 6a37bb88-8538-48c5-b37b-a41c836328bd
                        customer_id: 617e39d8-68f4-4592-b8d2-c2bf26a76989
                        type: USAGE
                        start_timestamp: '2021-01-01T00:00:00Z'
                        end_timestamp: '2021-02-01T00:00:00Z'
                        credit_type:
                          id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                          name: USD (cents)
                        contract_id: 9de042a1-b955-43ce-9ab4-e3c2004570d1
                        line_items:
                          - credit_type:
                              id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                              name: USD (cents)
                            name: CPU hours
                            type: usage
                            quantity: 1488
                            total: 14392
                            product_id: 5c1f40cd-9ff8-4e90-ae53-5f81b0e9d1e8
                        total: 14392
                        status: FINALIZED
                    next_page: null
        '404':
          $ref: '#/components/responses/NotFound'
components:
  parameters:
    CustomerId:
      name: customer_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
      example: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
    PageLimit:
      name: limit
      in: query
      description: Max number of results that should be returned
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 100
    NextPage:
      name: next_page
      in: query
      description: Cursor that indicates where the next page of results should start.
      required: false
      schema:
        type: string
    InvoiceStatus:
      name: status
      in: query
      description: Invoice status, e.g. DRAFT, FINALIZED, or VOID
      required: false
      schema:
        type: string
    InvoiceType:
      name: type
      in: query
      description: Filter invoices by type. Defaults to returning all invoice types.
      required: false
      schema:
        type: string
        enum:
          - USAGE
          - USAGE_CONSOLIDATED
          - SCHEDULED
    SkipZeroQtyLineItems:
      name: skip_zero_qty_line_items
      in: query
      description: >-
        If set, all zero quantity line items will be filtered out of the
        response
      required: false
      schema:
        type: boolean
  schemas:
    Invoice:
      required:
        - id
        - customer_id
        - credit_type
        - line_items
        - status
        - total
        - type
      type: object
      properties:
        id:
          type: string
          format: uuid
        customer_id:
          type: string
          format: uuid
        customer_custom_fields:
          $ref: '#/components/schemas/CustomField'
        netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        salesforce_opportunity_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          description: >-
            This field's availability is dependent on your client's
            configuration.
        net_payment_terms_days:
          type: number
        credit_type:
          $ref: '#/components/schemas/CreditType'
        line_items:
          type: array
          items:
            $ref: '#/components/schemas/InvoiceLineItem'
        start_timestamp:
          description: Beginning of the usage period this invoice covers (UTC)
          type: string
          format: date-time
        end_timestamp:
          description: End of the usage period this invoice covers (UTC)
          type: string
          format: date-time
        issued_at:
          description: When the invoice was issued (UTC)
          type: string
          format: date-time
        created_at:
          description: >-
            When the invoice was created (UTC). This field is present for
            correction invoices only.
          type: string
          format: date-time
        status:
          $ref: '#/components/schemas/InvoiceStatus'
        total:
          type: number
        type:
          $ref: '#/components/schemas/InvoiceType'
        external_invoice:
          $ref: '#/components/schemas/ExternalInvoice'
          nullable: true
        revenue_system_invoices:
          type: array
          items:
            $ref: '#/components/schemas/RevenueSystemInvoice'
          nullable: true
        contract_id:
          type: string
          format: uuid
        contract_custom_fields:
          $ref: '#/components/schemas/CustomField'
        amendment_id:
          type: string
          format: uuid
        correction_record:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          required:
            - reason
            - memo
            - corrected_invoice_id
          type: object
          properties:
            reason:
              type: string
            memo:
              type: string
            corrected_invoice_id:
              type: string
              format: uuid
            corrected_external_invoice:
              $ref: '#/components/schemas/ExternalInvoice'
        reseller_royalty:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: object
          description: Only present for contract invoices with reseller royalties.
          required:
            - reseller_type
            - netsuite_reseller_id
            - fraction
          properties:
            reseller_type:
              $ref: '#/components/schemas/ResellerType'
            netsuite_reseller_id:
              type: string
            fraction:
              type: string
            aws_options:
              type: object
              properties:
                aws_account_number:
                  type: string
                aws_payer_reference_id:
                  type: string
                aws_offer_id:
                  type: string
            gcp_options:
              type: object
              properties:
                gcp_account_id:
                  type: string
                gcp_offer_id:
                  type: string
        custom_fields:
          x-cf-entity: invoice
          type: object
          x-mint:
            groups:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:9c7e2b27-9b4c-4b76-9df7-f9cb05665a6a
              - client_id:8e3a848a-4566-4cfb-be49-64d80118a7fc
          additionalProperties: true
        billable_status:
          $ref: '#/components/schemas/BillableStatus'
          x-mint:
            groups:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:9c7e2b27-9b4c-4b76-9df7-f9cb05665a6a
              - client_id:8e3a848a-4566-4cfb-be49-64d80118a7fc
          type: object
          description: >-
            Indicates if the invoice has been or will be sent to the configured
            customer billing provider. Defaults to `billable`.
        constituent_invoices:
          type: array
          description: >-
            Required on invoices with type USAGE_CONSOLIDATED. List of
            constituent invoices that were consolidated to create this invoice.
          items:
            type: object
            required:
              - contract_id
              - invoice_id
              - customer_id
            properties:
              contract_id:
                type: string
                format: uuid
              invoice_id:
                type: string
                format: uuid
              customer_id:
                type: string
                format: uuid
        payer:
          type: object
          required:
            - contract_id
            - customer_id
          properties:
            contract_id:
              type: string
              format: uuid
            customer_id:
              type: string
              format: uuid
          description: >-
            Required for account hierarchy usage invoices. An object containing
            the contract and customer UUIDs that pay for this invoice.
        regenerated_from_invoice_id:
          type: string
          format: uuid
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    CreditType:
      required:
        - name
        - id
      type: object
      properties:
        name:
          type: string
        id:
          type: string
          format: uuid
    InvoiceLineItem:
      required:
        - name
        - total
        - credit_type
        - type
      type: object
      properties:
        name:
          type: string
        quantity:
          type: number
          description: The quantity associated with the line item.
        total:
          type: number
        unit_price:
          type: number
          description: The unit price associated with the line item.
        list_price:
          $ref: '#/components/schemas/Rate'
          description: >
            Only present for contract invoices and when the
            `include_list_prices` query parameter is set to true. This will
            include the list rate for the charge if applicable.  Only present
            for usage and subscription line items.
        product_id:
          type: string
          format: uuid
          description: ID of the product associated with the line item.
        product_custom_fields:
          $ref: '#/components/schemas/CustomField'
        product_tags:
          $ref: '#/components/schemas/Tags'
          description: >-
            The current product tags associated with the line item's
            `product_id`.
        product_type:
          type: string
          description: >
            The type of the line item's product. Possible values are
            `FixedProductListItem` (for `FIXED` type products),
            `UsageProductListItem` (for `USAGE` type products),
            `SubscriptionProductListItem` (for `SUBSCRIPTION` type products) or
            `CompositeProductListItem` (for `COMPOSITE` type products).  For
            scheduled charges, commit and credit payments, the value is
            `FixedProductListItem`.
        type:
          type: string
          description: >
            The type of line item.


            - `scheduled`: Line item is associated with a scheduled charge. View
            the scheduled_charge_id on the line item.

            - `commit_purchase`: Line item is associated with a payment for a
            prepaid commit. View the commit_id on the line item.

            - `usage`: Line item is associated with a usage product or composite
            product. View the product_id on the line item to determine which
            product.

            - `subscription`: Line item is associated with a subscription. e.g.
            monthly recurring payment for an in-advance subscription.

            - `applied_commit_or_credit`: On metronome invoices, applied commits
            and credits are associated with their own line items. These line
            items have negative totals. Use the applied_commit_or_credit object
            on the line item to understand the id of the applied commit or
            credit, and its type. Note that the application of a postpaid commit
            is associated with a line item, but the total on the line item is
            not included in the invoice's total as postpaid commits are paid
            in-arrears.

            - `cpu_conversion`: Line item converting between a custom pricing
            unit and fiat currency, using the conversion rate set on the rate
            card. This line item will appear when there are products priced in
            custom pricing units, and there is insufficient prepaid
            commit/credit in that custom pricing unit to fully cover the spend.
            Then, the outstanding spend in custom pricing units will be
            converted to fiat currency using a cpu_conversion line item.
        netsuite_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
        is_prorated:
          type: boolean
          description: >-
            Indicates whether the line item is prorated for `SUBSCRIPTION` type
            product.
        credit_type:
          $ref: '#/components/schemas/CreditType'
        starting_at:
          type: string
          format: date-time
          description: The line item's start date (inclusive).
        ending_before:
          type: string
          format: date-time
          description: The line item's end date (exclusive).
        commit_id:
          type: string
          format: uuid
          description: >-
            For line items with product of `USAGE`, `SUBSCRIPTION`, or
            `COMPOSITE` types, the ID of the credit or commit that was applied
            to this line item. For line items with product type of `FIXED`, the
            ID of the prepaid or postpaid commit that is being paid for.
        applied_commit_or_credit:
          $ref: '#/components/schemas/AppliedCommitOrCredit'
          description: >-
            Details about the credit or commit that was applied to this line
            item. Only present on line items with product of `USAGE`,
            `SUBSCRIPTION` or `COMPOSITE` types.
        commit_custom_fields:
          $ref: '#/components/schemas/CustomField'
        commit_segment_id:
          type: string
          format: uuid
        commit_type:
          type: string
          description: >-
            `PrepaidCommit` (for commit types `PREPAID` and `CREDIT`) or
            `PostpaidCommit` (for commit type `POSTPAID`).
        commit_netsuite_sales_order_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
        commit_netsuite_item_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
        postpaid_commit:
          $ref: '#/components/schemas/PostpaidCommit'
          description: Only present for line items paying for a postpaid commit true-up.
        reseller_type:
          $ref: '#/components/schemas/ResellerType'
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: product
        pricing_group_values:
          type: object
          description: >-
            Includes the pricing group values associated with this line item if
            dimensional pricing is used.
          additionalProperties:
            type: string
        presentation_group_values:
          type: object
          description: >-
            Includes the presentation group values associated with this line
            item if presentation group keys are used.
          additionalProperties:
            type: string
            nullable: true
        metadata:
          type: string
        netsuite_invoice_billing_start:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          format: date-time
          description: The start date for the billing period on the invoice.
        netsuite_invoice_billing_end:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          format: date-time
          description: The end date for the billing period on the invoice.
        professional_service_id:
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
          type: string
          format: uuid
        professional_service_custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-mint:
            groups:
              - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
        scheduled_charge_id:
          type: string
          format: uuid
          description: ID of scheduled charge.
        scheduled_charge_custom_fields:
          $ref: '#/components/schemas/CustomField'
        subscription_custom_fields:
          $ref: '#/components/schemas/CustomField'
        subscription_id:
          type: string
          format: uuid
          description: >-
            ID of the subscription that this line item is associated with. Only
            present on line items with product of `SUBSCRIPTION` type.
        tier:
          $ref: '#/components/schemas/TierMetadata'
          description: Populated if the line item has a tiered price.
        discount_id:
          type: string
          format: uuid
          description: ID of the discount applied to this line item.
        discount_custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: discount
        origin:
          type: object
          description: >-
            Present on line items from invoices with type USAGE_CONSOLIDATED.
            Indicates the original customer, contract, invoice and line item
            from which this line item was copied.
          required:
            - line_item_id
            - invoice_id
            - customer_id
            - contract_id
          properties:
            line_item_id:
              type: string
              format: uuid
            invoice_id:
              type: string
              format: uuid
            customer_id:
              type: string
              format: uuid
            contract_id:
              type: string
              format: uuid
        quantity_consumed:
          type: number
          description: >-
            Present on applied commit line items for quantity-based commits.
            Represents the unit quantity deducted the commit.
    InvoiceStatus:
      type: string
      example: DRAFT, VOID, or FINALIZED
    InvoiceType:
      type: string
      example: SCHEDULED or USAGE
    ExternalInvoice:
      required:
        - billing_provider_type
      type: object
      properties:
        billing_provider_type:
          $ref: '#/components/schemas/BillingProviderType'
        invoice_id:
          type: string
        issued_at_timestamp:
          type: string
          format: date-time
        external_status:
          $ref: '#/components/schemas/ExternalInvoiceStatus'
        pdf_url:
          type: string
          format: uri
          description: >-
            A URL to the PDF of the invoice, if available from the billing
            provider.
        tax:
          x-mint:
            metadata:
              tag: Beta
          type: object
          description: Tax details for the invoice, if available from the billing provider.
          properties:
            total_tax_amount:
              type: number
              description: The total tax amount applied to the invoice.
            total_taxable_amount:
              type: number
              description: The total taxable amount of the invoice.
            transaction_id:
              type: string
              description: The transaction ID associated with the tax calculation.
        invoiced_total:
          x-mint:
            metadata:
              tag: Beta
          type: number
          description: The total amount invoiced, if available from the billing provider.
        invoiced_sub_total:
          x-mint:
            metadata:
              tag: Beta
          type: number
          description: >-
            The subtotal amount invoiced, if available from the billing
            provider.
        billing_provider_error:
          type: string
          description: Error message from the billing provider, if available.
        external_payment_id:
          type: string
          description: The ID of the payment in the external system, if available.
    RevenueSystemInvoice:
      required:
        - revenue_system_provider
        - sync_status
        - revenue_system_external_entity_type
      type: object
      properties:
        revenue_system_provider:
          type: string
        revenue_system_external_entity_id:
          type: string
        sync_status:
          type: string
        revenue_system_external_entity_type:
          type: string
        error_message:
          type: string
          description: The error message from the revenue system, if available.
    ResellerType:
      type: string
      enum:
        - AWS
        - AWS_PRO_SERVICE
        - GCP
        - GCP_PRO_SERVICE
    BillableStatus:
      type: string
      enum:
        - billable
        - unbillable
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
    Rate:
      type: object
      required:
        - rate_type
      properties:
        rate_type:
          type: string
          enum:
            - FLAT
            - flat
            - PERCENTAGE
            - percentage
            - SUBSCRIPTION
            - subscription
            - CUSTOM
            - custom
            - TIERED
            - tiered
            - TIERED_PERCENTAGE
            - tiered_percentage
          x-mint-enum:
            CUSTOM:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
            custom:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
            SUBSCRIPTION:
              - ff:legacy-subscriptions-enabled
            subscription:
              - ff:legacy-subscriptions-enabled
            TIERED_PERCENTAGE:
              - ff:support-charge-ga
            tiered_percentage:
              - ff:support-charge-ga
          x-mint:
            groups:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
        price:
          type: number
          description: >-
            Default price. For FLAT rate_type, this must be >=0. For PERCENTAGE
            rate_type, this is a decimal fraction, e.g. use 0.1 for 10%; this
            must be >=0 and <=1.
        custom_rate:
          x-mint:
            groups:
              - client_id:5b9e3072-415b-4842-94f0-0b6700c8b6be
              - client_id:179e395f-5349-4fe2-bf12-64ab4e5bc560
              - client_id:f157d376-0781-4ef3-9db9-775a9052148e
              - client_id:7dd2f652-7629-4925-9069-77f5c5d3db37
              - client_id:c0ce3dc0-6d3e-4f6b-aadf-dfb90f2bf9f5
              - client_id:cf874b25-ca3b-460b-b6fe-5f33b3c2ea33
              - client_id:97c07a0c-70db-448a-a1d4-adcd2b8bd1c7
          type: object
          additionalProperties: true
          description: >-
            Only set for CUSTOM rate_type. This field is interpreted by custom
            rate processors.
        quantity:
          type: number
          x-mint:
            groups:
              - ff:legacy-subscriptions-enabled
          description: Default quantity. For SUBSCRIPTION rate_type, this must be >=0.
        is_prorated:
          type: boolean
          x-mint:
            groups:
              - ff:legacy-subscriptions-enabled
          description: >-
            Default proration configuration. Only valid for SUBSCRIPTION
            rate_type. Must be set to true.
        tiers:
          type: array
          items:
            $ref: '#/components/schemas/Tier'
          description: Only set for TIERED rate_type.
        minimum_config:
          $ref: '#/components/schemas/MinimumConfig'
          x-stainless-skip: true
          x-mint:
            groups:
              - ff:support-charge-ga
        pricing_group_values:
          type: object
          description: >-
            if pricing groups are used, this will contain the values used to
            calculate the price
          additionalProperties:
            type: string
        credit_type:
          $ref: '#/components/schemas/CreditType'
    Tags:
      type: array
      items:
        type: string
    AppliedCommitOrCredit:
      type: object
      required:
        - id
        - type
      properties:
        access_type:
          x-mint:
            groups:
              - ff:create-quantity-based-commits
          x-stainless-skip: true
          type: string
          enum:
            - SPEND
            - QUANTITY
          description: >-
            Indicates how the balance is drawn down. `SPEND` deducts the dollar
            cost of usage. `QUANTITY` deducts the number of units used.
        id:
          type: string
          format: uuid
        type:
          type: string
          enum:
            - PREPAID
            - POSTPAID
            - CREDIT
    PostpaidCommit:
      type: object
      required:
        - id
      description: ID of the commit.
      properties:
        id:
          type: string
          format: uuid
    TierMetadata:
      required:
        - level
        - starting_at
      type: object
      properties:
        size:
          type: string
          nullable: true
        level:
          type: number
        starting_at:
          type: string
    BillingProviderType:
      type: string
      enum:
        - aws_marketplace
        - stripe
        - netsuite
        - custom
        - azure_marketplace
        - quickbooks_online
        - workday
        - gcp_marketplace
        - metronome
      x-mint-enum:
        netsuite:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
        custom:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
        workday:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
        gcp_marketplace:
          - client_id:11db091c-975b-4908-9f67-b1ceb126acdf
    ExternalInvoiceStatus:
      type: string
      enum:
        - DRAFT
        - FINALIZED
        - PAID
        - PARTIALLY_PAID
        - UNCOLLECTIBLE
        - VOID
        - DELETED
        - PAYMENT_FAILED
        - INVALID_REQUEST_ERROR
        - SKIPPED
        - SENT
        - QUEUED
    Tier:
      type: object
      required:
        - price
      properties:
        size:
          type: number
        price:
          type: number
    MinimumConfig:
      type: object
      description: >-
        Only set for TIERED_PERCENTAGE or PERCENTAGE rate_type. Any
        commit-specific overrides will not apply if there is a minimum set on
        the rate/applied override.
      required:
        - minimum
      properties:
        minimum:
          type: number
  responses:
    NotFound:
      description: The specified resource was not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
