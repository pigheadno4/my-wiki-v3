<!-- Source URL: https://docs.metronome.com/api-reference/customers/update-a-customer-name.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a customer name

> Updates the display name for a customer record. Use this to correct customer names, update business names after rebranding, or maintain accurate customer information for invoicing and reporting. Returns the updated customer object with the new name applied immediately across all billing documents and interfaces.




## OpenAPI

````yaml /openapi.json post /v1/customers/{customer_id}/setName
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
  /v1/customers/{customer_id}/setName:
    post:
      tags:
        - Customers
      summary: Update a customer name
      description: >
        Updates the display name for a customer record. Use this to correct
        customer names, update business names after rebranding, or maintain
        accurate customer information for invoicing and reporting. Returns the
        updated customer object with the new name applied immediately across all
        billing documents and interfaces.
      operationId: setCustomerName-v1
      parameters:
        - $ref: '#/components/parameters/CustomerId'
      requestBody:
        description: The customer name
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetCustomerNamePayload'
            example:
              name: Example, Inc.
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
                    $ref: '#/components/schemas/Customer'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  external_id: team@example.com
                  ingest_aliases:
                    - team@example.com
                  name: Example, Inc.
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
    SetCustomerNamePayload:
      required:
        - name
      type: object
      properties:
        name:
          type: string
          description: >-
            The new name for the customer. This will be truncated to 160
            characters if the provided name is longer.
    Customer:
      required:
        - external_id
        - ingest_aliases
        - id
        - name
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
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: customer
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
