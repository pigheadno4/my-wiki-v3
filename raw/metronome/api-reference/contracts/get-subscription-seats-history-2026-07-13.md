<!-- Source URL: https://docs.metronome.com/api-reference/contracts/get-subscription-seats-history.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get subscription seats history

> Get the history of subscription seats schedule over time for a given `subscription_id`. This endpoint provides information about seat assignments and total quantities for different time periods, allowing you to track how seat assignments have changed over time.

### Use this endpoint to:
- Track changes to seat assignments over time
- Get seat schedule for a specific date using the `covering_date` parameter
- Get seat schedule history with optional date range filtering using `starting_at` and `ending_before`

### Key response fields:
- data: array of seat schedule entries with time periods, quantity, and assignments
- next_page: cursor for pagination to retrieve additional results

### Usage guidelines:
- Use `covering_date` to get the active seats for a specific point in time. `covering_date` cannot be used with `starting_at` or `ending_before`.
- Use `starting_at` and `ending_before` to filter results by time range. `starting_at` and `ending_before` cannot be used with `covering_date`.
- Maximum limit is 10 seat schedule entries per request
- Results are ordered by `starting_at` timestamp




## OpenAPI

````yaml /openapi.json post /v1/contracts/getSubscriptionSeatsHistory
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
  /v1/contracts/getSubscriptionSeatsHistory:
    post:
      tags:
        - Contracts
      summary: Get subscription seats history
      description: >
        Get the history of subscription seats schedule over time for a given
        `subscription_id`. This endpoint provides information about seat
        assignments and total quantities for different time periods, allowing
        you to track how seat assignments have changed over time.


        ### Use this endpoint to:

        - Track changes to seat assignments over time

        - Get seat schedule for a specific date using the `covering_date`
        parameter

        - Get seat schedule history with optional date range filtering using
        `starting_at` and `ending_before`


        ### Key response fields:

        - data: array of seat schedule entries with time periods, quantity, and
        assignments

        - next_page: cursor for pagination to retrieve additional results


        ### Usage guidelines:

        - Use `covering_date` to get the active seats for a specific point in
        time. `covering_date` cannot be used with `starting_at` or
        `ending_before`.

        - Use `starting_at` and `ending_before` to filter results by time range.
        `starting_at` and `ending_before` cannot be used with `covering_date`.

        - Maximum limit is 10 seat schedule entries per request

        - Results are ordered by `starting_at` timestamp
      operationId: getSubscriptionSeatsHistory-v1
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
                limit:
                  type: integer
                  default: 10
                  nullable: true
                  description: >-
                    Maximum number of seat schedule entries to return. Defaults
                    to 10. Required range: 1 <= x <= 10.
                cursor:
                  type: string
                  nullable: true
                  description: >-
                    Cursor for pagination. Use the value from the `next_page`
                    field of the previous response to retrieve the next page of
                    results.
                covering_date:
                  type: string
                  format: date-time
                  nullable: true
                  description: >-
                    Get the seats history segment for the covering date. Cannot
                    be used with `starting_at` or `ending_before`.
                starting_at:
                  type: string
                  format: date-time
                  nullable: true
                  description: >-
                    Include seats history segments that are active at or after
                    this timestamp. Use with `ending_before` to get a specific
                    time range. If not set, there's no lower bound.
                ending_before:
                  type: string
                  format: date-time
                  nullable: true
                  description: >-
                    Include seats history segments that are active at or before
                    this timestamp. Use with `starting_at` to get a specific
                    time range. If not set, there's no upper bound.
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              contract_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              subscription_id: 1a824d53-bde6-4d82-96d7-6347ff227d5c
              covering_date: '2024-01-15T00:00:00.000Z'
              limit: 10
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
                      $ref: '#/components/schemas/SubscriptionSeatsScheduleEntry'
                  next_page:
                    type: string
                    nullable: true
                    description: Cursor for the next page of results
              example:
                data:
                  - starting_at: '2024-01-01T00:00:00.000Z'
                    ending_before: '2024-01-15T00:00:00.000Z'
                    total_quantity: 5
                    assigned_seat_ids:
                      - seat-1
                      - seat-2
                      - seat-3
                      - seat-4
                      - seat-5
                  - starting_at: '2024-01-15T00:00:00.000Z'
                    ending_before: null
                    total_quantity: 3
                    assigned_seat_ids:
                      - seat-1
                      - seat-2
                      - seat-3
                next_page: eyJzdGFydGluZ19hdCI6IjIwMjQtMDEtMTVUMDA6MDA6MDAuMDAwWiJ9
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
                      - InvalidArgument
                  message:
                    type: string
components:
  schemas:
    SubscriptionSeatsScheduleEntry:
      type: object
      required:
        - starting_at
        - ending_before
        - total_quantity
        - assigned_seat_ids
      properties:
        starting_at:
          type: string
          format: date-time
          description: The start time of this seat schedule period
        ending_before:
          type: string
          format: date-time
          nullable: true
          description: The end time of this seat schedule period (null if ongoing)
        total_quantity:
          type: integer
          minimum: 0
          description: Total number of assigned and unassigned seats in this period
        assigned_seat_ids:
          type: array
          items:
            type: string
          description: Array of seat IDs that are assigned in this period
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
