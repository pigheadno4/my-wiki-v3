<!-- Source URL: https://docs.metronome.com/api-reference/rate-cards/get-a-rate-card.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a rate card

> Return details for a specific rate card including name, description, and aliases. This endpoint does not return rates - use the dedicated getRates or getRateSchedule endpoints to understand the rates on a rate card.




## OpenAPI

````yaml /openapi.json post /v1/contract-pricing/rate-cards/get
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
  /v1/contract-pricing/rate-cards/get:
    post:
      tags:
        - Rate cards
      summary: Get a rate card
      description: >
        Return details for a specific rate card including name, description, and
        aliases. This endpoint does not return rates - use the dedicated
        getRates or getRateSchedule endpoints to understand the rates on a rate
        card.
      operationId: getRateCard-v1
      requestBody:
        description: The ID of the rate card to get
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Id'
            example:
              id: f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe
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
                    $ref: '#/components/schemas/RateCard'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
                  name: Test rate card
                  description: Test rate card description
                  fiat_credit_type:
                    id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                    name: USD (cents)
                  created_at: '2019-12-30T04:24:55.123Z'
                  created_by: Bob
                  aliases:
                    - name: test-rate-card
                  custom_fields:
                    x_account_id: KyVnHhSBWl7eY2bl
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    RateCard:
      type: object
      required:
        - id
        - name
        - created_at
        - created_by
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        description:
          type: string
        fiat_credit_type:
          $ref: '#/components/schemas/CreditType'
        credit_type_conversions:
          type: array
          items:
            $ref: '#/components/schemas/CreditTypeConversion'
        aliases:
          type: array
          items:
            $ref: '#/components/schemas/RateCardAlias'
        custom_fields:
          $ref: '#/components/schemas/CustomField'
          x-cf-entity: rate_card
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
    CreditTypeConversion:
      required:
        - fiat_per_custom_credit
        - custom_credit_type
      type: object
      properties:
        fiat_per_custom_credit:
          type: string
        custom_credit_type:
          $ref: '#/components/schemas/CreditType'
    RateCardAlias:
      type: object
      required:
        - name
      properties:
        name:
          type: string
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
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
