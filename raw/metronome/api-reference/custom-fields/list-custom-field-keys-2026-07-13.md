<!-- Source URL: https://docs.metronome.com/api-reference/custom-fields/list-custom-field-keys.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List custom field keys

> Retrieve all your active custom field keys, with optional filtering by entity type (customer, contract, product, etc.). Use this endpoint to discover what custom field keys are available before setting values on entities or to audit your custom field configuration across different entity types.




## OpenAPI

````yaml /openapi.json post /v1/customFields/listKeys
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
  /v1/customFields/listKeys:
    post:
      tags:
        - Custom fields
      summary: List custom field keys
      description: >
        Retrieve all your active custom field keys, with optional filtering by
        entity type (customer, contract, product, etc.). Use this endpoint to
        discover what custom field keys are available before setting values on
        entities or to audit your custom field configuration across different
        entity types.
      operationId: listCustomFieldKeys-v1
      parameters:
        - $ref: '#/components/parameters/NextPage'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                entities:
                  type: array
                  description: Optional list of entity types to return keys for
                  items:
                    $ref: '#/components/schemas/ManagedEntity'
            example:
              entities:
                - customer
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
                      type: object
                      required:
                        - entity
                        - key
                        - enforce_uniqueness
                      properties:
                        entity:
                          $ref: '#/components/schemas/ManagedEntity'
                        key:
                          type: string
                        enforce_uniqueness:
                          type: boolean
                  next_page:
                    type: string
                    nullable: true
              example:
                data:
                  - entity: customer
                    key: x_account_id
                    enforce_uniqueness: true
                next_page: null
components:
  parameters:
    NextPage:
      name: next_page
      in: query
      description: Cursor that indicates where the next page of results should start.
      required: false
      schema:
        type: string
  schemas:
    ManagedEntity:
      type: string
      enum:
        - alert
        - billable_metric
        - charge
        - commit
        - contract_credit
        - contract_product
        - contract
        - customer
        - discount
        - invoice
        - professional_service
        - product
        - rate_card
        - scheduled_charge
        - subscription
        - package_commit
        - package_credit
        - package_subscription
        - package_scheduled_charge
      x-mint-enum:
        professional_service:
          - client_id:e3147d6d-4101-4cd1-9888-ce3afeeac5b2
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
