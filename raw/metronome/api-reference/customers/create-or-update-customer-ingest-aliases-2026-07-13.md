<!-- Source URL: https://docs.metronome.com/api-reference/customers/create-or-update-customer-ingest-aliases.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or update customer ingest aliases

> Sets the ingest aliases for a customer. Use this endpoint to associate a Metronome customer with an internal ID for easier tracking between systems. Ingest aliases can be used in the `customer_id` field when sending usage events to Metronome. 

### Usage guidelines:
- This call is idempotent and fully replaces the set of ingest aliases for the given customer.
- Switching an ingest alias from one customer to another will associate all corresponding usage to the new customer.
- Use multiple ingest aliases to model child organizations within a single Metronome customer.




## OpenAPI

````yaml /openapi.json post /v1/customers/{customer_id}/setIngestAliases
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
  /v1/customers/{customer_id}/setIngestAliases:
    post:
      tags:
        - Customers
      summary: Create or update customer ingest aliases
      description: >
        Sets the ingest aliases for a customer. Use this endpoint to associate a
        Metronome customer with an internal ID for easier tracking between
        systems. Ingest aliases can be used in the `customer_id` field when
        sending usage events to Metronome. 


        ### Usage guidelines:

        - This call is idempotent and fully replaces the set of ingest aliases
        for the given customer.

        - Switching an ingest alias from one customer to another will associate
        all corresponding usage to the new customer.

        - Use multiple ingest aliases to model child organizations within a
        single Metronome customer.
      operationId: setIngestAliases-v1
      parameters:
        - $ref: '#/components/parameters/CustomerId'
      requestBody:
        description: The aliases to add
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetIngestAliasesPayload'
            example:
              ingest_aliases:
                - team@example.com
      responses:
        '200':
          description: Success
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
    SetIngestAliasesPayload:
      required:
        - ingest_aliases
      type: object
      properties:
        ingest_aliases:
          type: array
          items:
            type: string
            minLength: 1
            maxLength: 128
          maxItems: 2000
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
