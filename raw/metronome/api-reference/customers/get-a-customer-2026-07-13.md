<!-- Source URL: https://docs.metronome.com/api-reference/customers/get-a-customer.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a customer

> Get detailed information for a specific customer by their Metronome ID. Returns customer profile data including name, creation date, ingest aliases, configuration settings, and custom fields. Use this endpoint to fetch complete customer details for billing operations or account management.

Note: If searching for a customer billing configuration, use the `/getCustomerBillingConfigurations` endpoint.




## OpenAPI

````yaml /openapi.json get /v1/customers/{customer_id}
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
  /v1/customers/{customer_id}:
    get:
      tags:
        - Customers
      summary: Get a customer
      description: >
        Get detailed information for a specific customer by their Metronome ID.
        Returns customer profile data including name, creation date, ingest
        aliases, configuration settings, and custom fields. Use this endpoint to
        fetch complete customer details for billing operations or account
        management.


        Note: If searching for a customer billing configuration, use the
        `/getCustomerBillingConfigurations` endpoint.
      operationId: getCustomer-v1
      parameters:
        - $ref: '#/components/parameters/CustomerId'
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                properties:
                  data:
                    $ref: '#/components/schemas/CustomerDetail'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  created_at: '2024-01-01T00:00:00.000Z'
                  updated_at: '2024-01-01T00:00:00.000Z'
                  external_id: team@example.com
                  ingest_aliases:
                    - team@example.com
                  name: Example, Inc.
                  customer_config:
                    salesforce_account_id: 0015500001WO1ZiABL
                  custom_fields:
                    x_account_id: KyVnHhSBWl7eY2bl
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
  schemas:
    CustomerDetail:
      required:
        - external_id
        - id
        - name
        - created_at
        - updated_at
        - customer_config
        - ingest_aliases
        - custom_fields
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: the Metronome ID of the customer
        external_id:
          type: string
          description: >-
            (deprecated, use ingest_aliases instead) the first ID (Metronome or
            ingest alias) that can be used in usage events
        ingest_aliases:
          type: array
          description: >-
            aliases for this customer that can be used instead of the Metronome
            customer ID in usage events
          items:
            type: string
        name:
          type: string
        customer_config:
          $ref: '#/components/schemas/CustomerConfig'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: customer
        created_at:
          type: string
          format: date-time
          description: RFC 3339 timestamp indicating when the customer was created.
        archived_at:
          type: string
          format: date-time
          description: >-
            RFC 3339 timestamp indicating when the customer was archived. Null
            if the customer is active.
          nullable: true
        updated_at:
          type: string
          format: date-time
          description: RFC 3339 timestamp indicating when the customer was last updated.
        current_billable_status:
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
          required:
            - value
          type: object
          description: >-
            This field's availability is dependent on your client's
            configuration.
          properties:
            value:
              $ref: '#/components/schemas/BillableStatus'
            effective_at:
              type: string
              format: date-time
              nullable: true
    CustomerConfig:
      required:
        - salesforce_account_id
      type: object
      properties:
        salesforce_account_id:
          type: string
          description: The Salesforce account ID for the customer
          nullable: true
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    BillableStatus:
      type: string
      enum:
        - billable
        - unbillable
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
