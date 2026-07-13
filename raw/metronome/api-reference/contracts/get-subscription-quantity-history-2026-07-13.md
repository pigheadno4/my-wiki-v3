<!-- Source URL: https://docs.metronome.com/api-reference/contracts/get-subscription-quantity-history.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get subscription quantity history

> Get the history of subscription quantities and prices over time for a given `subscription_id`. This endpoint can be used to power an in-product experience where you show a customer their historical changes to seat count. Future changes are not included in this endpoint - use the `getContract` endpoint to view the future scheduled changes to a subscription's quantity. 

Subscriptions are used to model fixed recurring fees as well as seat-based recurring fees. To model changes to the number of seats in Metronome, you can increment or decrement the quantity on a subscription at any point in the past or future.




## OpenAPI

````yaml /openapi.json post /v1/contracts/getSubscriptionQuantityHistory
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
  /v1/contracts/getSubscriptionQuantityHistory:
    post:
      tags:
        - Contracts
      summary: Get subscription quantity history
      description: >
        Get the history of subscription quantities and prices over time for a
        given `subscription_id`. This endpoint can be used to power an
        in-product experience where you show a customer their historical changes
        to seat count. Future changes are not included in this endpoint - use
        the `getContract` endpoint to view the future scheduled changes to a
        subscription's quantity. 


        Subscriptions are used to model fixed recurring fees as well as
        seat-based recurring fees. To model changes to the number of seats in
        Metronome, you can increment or decrement the quantity on a subscription
        at any point in the past or future.
      operationId: getSubscriptionQuantityHistory-v1
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - customer_id
                - contract_id
                - subscription_id
              properties:
                customer_id:
                  type: string
                  format: uuid
                contract_id:
                  type: string
                  format: uuid
                subscription_id:
                  type: string
                  format: uuid
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              subscription_id: 1a824d53-bde6-4d82-96d7-6347ff227d5c
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
                    $ref: '#/components/schemas/SubscriptionQuantityHistory'
              example:
                data:
                  subscription_id: 1a824d53-bde6-4d82-96d7-6347ff227d5c
                  fiat_credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                  history:
                    - starting_at: '2020-01-01T00:00:00.000Z'
                      data:
                        - quantity: 100
                          unit_price: 1000
                          total: 100000
                    - starting_at: '2020-02-01T00:00:00.000Z'
                      data:
                        - quantity: 100
                          unit_price: 1000
                          total: 100000
                        - quantity: 200
                          unit_price: 2000
                          total: 400000
        '400':
          description: Error
          content:
            application/json:
              schema:
                type: object
                required:
                  - code
                  - message
                properties:
                  code:
                    type: string
                    enum:
                      - ContractNotFound
                      - CustomerNotFound
                      - SubscriptionNotFound
                  message:
                    type: string
components:
  schemas:
    SubscriptionQuantityHistory:
      type: object
      properties:
        subscription_id:
          type: string
          format: uuid
        fiat_credit_type_id:
          type: string
          format: uuid
        history:
          type: array
          items:
            type: object
            required:
              - starting_at
              - data
            properties:
              starting_at:
                type: string
                format: date-time
              data:
                type: array
                items:
                  type: object
                  required:
                    - quantity
                    - unit_price
                    - total
                  properties:
                    quantity:
                      type: number
                    total:
                      type: number
                    unit_price:
                      type: number
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
