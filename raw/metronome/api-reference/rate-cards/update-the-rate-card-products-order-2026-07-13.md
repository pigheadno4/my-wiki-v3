<!-- Source URL: https://docs.metronome.com/api-reference/rate-cards/update-the-rate-card-products-order.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update the rate card products order

> The ordering of products on a rate card determines the order in which the products will appear on customers' invoices. Use this endpoint to set the order of specific products on the rate card by moving them relative to their current location.




## OpenAPI

````yaml /openapi.json post /v1/contract-pricing/rate-cards/moveRateCardProducts
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
  /v1/contract-pricing/rate-cards/moveRateCardProducts:
    post:
      tags:
        - Rate cards
      summary: Update the rate card products order
      description: >
        The ordering of products on a rate card determines the order in which
        the products will appear on customers' invoices. Use this endpoint to
        set the order of specific products on the rate card by moving them
        relative to their current location.
      operationId: moveRateCardProducts-v1
      requestBody:
        description: New rate card product ordering
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MoveRateCardProductsPayload'
            example:
              rate_card_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              product_moves:
                - product_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
                  position: 0
                - product_id: b086f2f4-9851-4466-9ca0-30d53e6a42ac
                  position: 1
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
                    $ref: '#/components/schemas/Id'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    MoveRateCardProductsPayload:
      type: object
      required:
        - rate_card_id
        - product_moves
      properties:
        rate_card_id:
          type: string
          format: uuid
          description: ID of the rate card to update
        product_moves:
          type: array
          items:
            type: object
            required:
              - product_id
              - position
            properties:
              product_id:
                type: string
                format: uuid
                description: ID of the product to move
              position:
                type: number
                description: 0-based index of the new position of the product
                minimum: 0
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
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
